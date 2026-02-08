import sqlite3
import time
import json
import os
import sys
import logging
import traceback
import io
from flask import Flask, jsonify, request, Response, redirect, send_from_directory
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for server
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from flask_cors import CORS
from flask_compress import Compress
import pandas as pd
import numpy as np
from datetime import datetime

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import (DB_PATH, get_db_connection, SCHEMA_CACHE_TTL, DEFAULT_PORT,
                      CACHE_CONTROL_MAX_AGE, WORKSPACE_FILENAME,
                      WORKSPACE_TEMP_SUFFIX, HTTP_OK, HTTP_BAD_REQUEST,
                      HTTP_NOT_FOUND, HTTP_INTERNAL_ERROR,
                      resolve_ticker_alias, TICKER_ALIASES)
from constants import USE_DUCKDB

# Shared helpers (schema cache, DuckDB availability, utilities)
from helpers import (
    basedir as _helpers_basedir, get_table_columns, fetch_ticker_data,
    fiscal_to_calendar_quarter, _check_playwright, FRED_INDICATORS,
    DUCKDB_AVAILABLE, USE_DUCKDB as _USE_DUCKDB,
    _schema_cache, _schema_cache_time,
)
# Re-import DuckDB query functions when available (used directly by routes still in app.py)
if USE_DUCKDB and DUCKDB_AVAILABLE:
    from duckdb_queries import (
        get_price_data, get_volume_data,
        get_all_tickers_list, get_available_tickers, get_futures_tickers,
        get_bond_tickers, get_metadata, get_dashboard_prices
    )

# Import backup functionality
import subprocess
from pathlib import Path

# Configure logging to output to stdout for easier debugging
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)
CORS(app)
Compress(app)  # Enable gzip compression for responses

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = f'max-age={CACHE_CONTROL_MAX_AGE}, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    # Allow cross-origin requests (e.g., sandbox running on :5500)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

# basedir, schema cache, and other shared state now live in helpers.py
basedir = _helpers_basedir

# --- Start of Diagnostic Logging ---
app.logger.info(f"SCRIPT_DIR: {basedir}")
app.logger.info(f"DB_PATH: {DB_PATH}")
app.logger.info(f"USE_DUCKDB: {USE_DUCKDB}, DUCKDB_AVAILABLE: {DUCKDB_AVAILABLE}")
if not os.path.exists(DB_PATH):
    app.logger.error("FATAL: DATABASE NOT FOUND AT THE CALCULATED PATH!")
else:
    app.logger.info("SUCCESS: Database file was found at the path.")
# --- End of Diagnostic Logging ---

# get_table_columns() now imported from helpers.py

# fetch_ticker_data() now imported from helpers.py
# Diag routes (/, /api/health, /api/diag, /api/diag_reduce, /api/diag_series) moved to diag_routes.py

# Sandbox, workspace, commentary, and ETF routes moved to content_routes.py

# Data routes (tickers, metadata, ticker-aliases, data, volume) moved to data_routes.py



# Fundamentals routes (revenue, overview, earnings, income, balance, cashflow, chart) moved to fundamentals_routes.py

# Short interest routes moved to short_interest_routes.py
# IV routes moved to iv_routes.py


import csv
import io

# FRED_INDICATORS now imported from helpers.py


def _build_dashboard_rows(filter_text='', sort_col='ticker', sort_dir='asc'):
    """
    Build dashboard rows for all tickers (excluding FRED indicators).
    Returns a list of dicts with ticker data, filtered and sorted.
    Used by both /api/dashboard and /api/dashboard/export.

    Args:
        filter_text: Filter string for ticker/name/page_name matching
        sort_col: Column to sort by
        sort_dir: 'asc' or 'desc'
    Returns:
        List of ticker data dicts
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()

        # Load workspace to get page/chart info
        workspace_path = os.path.join(basedir, WORKSPACE_FILENAME)
        page_info = {}  # ticker -> [{page, chart_title}, ...]
        page_names = {}

        if os.path.exists(workspace_path):
            with open(workspace_path, 'r') as f:
                workspace = json.load(f)

            # Get page names
            if 'pages' in workspace and 'names' in workspace['pages']:
                page_names = workspace['pages']['names']

            # Build ticker -> page/chart mapping
            cards = workspace.get('cards', [])
            for card in cards:
                page_num = str(card.get('page', 1))
                page_name = page_names.get(page_num, f'Page {page_num}')
                chart_title = card.get('title', '')
                tickers = card.get('tickers', [])

                for ticker in tickers:
                    if ticker not in page_info:
                        page_info[ticker] = []
                    page_info[ticker].append({
                        'page': int(page_num),
                        'page_name': page_name,
                        'chart_title': chart_title
                    })

        # Get all tickers with data
        all_tickers = set(page_info.keys())

        # Also get tickers from metadata table
        cursor.execute("SELECT ticker, name, first_date, last_date, data_points FROM ticker_metadata")
        metadata = {}
        for row in cursor.fetchall():
            ticker, name, first_date, last_date, data_points = row
            metadata[ticker] = {
                'name': name,
                'first_date': first_date,
                'last_date': last_date,
                'data_points': data_points
            }
            all_tickers.add(ticker)

        # Get short interest data (latest per ticker)
        short_interest = {}
        try:
            cursor.execute("""
                SELECT si.ticker, si.settlement_date, si.short_interest,
                       si.short_percent_float, si.short_percent_outstanding, si.days_to_cover
                FROM short_interest si
                INNER JOIN (
                    SELECT ticker, MAX(settlement_date) as max_date
                    FROM short_interest
                    GROUP BY ticker
                ) latest ON si.ticker = latest.ticker AND si.settlement_date = latest.max_date
            """)
            for row in cursor.fetchall():
                short_interest[row[0]] = {
                    'si_date': row[1],
                    'si_shares': row[2],
                    'si_percent_float': row[3],
                    'si_percent_outstanding': row[4],
                    'si_days_to_cover': row[5],
                }
        except Exception as e:
            app.logger.warning(f"Could not load short interest: {e}")

        # Get fundamentals from company_overview table
        fundamentals = {}
        try:
            cursor.execute("""
                SELECT ticker, sector, industry, market_cap, pe_ratio, peg_ratio, eps,
                       dividend_yield, beta, moving_avg_50, moving_avg_200, shares_outstanding,
                       profit_margin, operating_margin, return_on_assets, return_on_equity,
                       revenue, revenue_per_share, quarterly_revenue_growth, gross_profit,
                       ebitda, diluted_eps, quarterly_earnings_growth, analyst_target_price,
                       trailing_pe, forward_pe, price_to_sales, price_to_book,
                       ev_to_revenue, ev_to_ebitda
                FROM company_overview
            """)
            for row in cursor.fetchall():
                fundamentals[row[0]] = {
                    'sector': row[1],
                    'industry': row[2],
                    'market_cap': row[3],
                    'pe_ratio': row[4],
                    'peg_ratio': row[5],
                    'eps': row[6],
                    'dividend_yield': row[7],
                    'beta': row[8],
                    'moving_avg_50': row[9],
                    'moving_avg_200': row[10],
                    'shares_outstanding': row[11],
                    'profit_margin': row[12],
                    'operating_margin': row[13],
                    'return_on_assets': row[14],
                    'return_on_equity': row[15],
                    'revenue': row[16],
                    'revenue_per_share': row[17],
                    'quarterly_revenue_growth': row[18],
                    'gross_profit': row[19],
                    'ebitda': row[20],
                    'diluted_eps': row[21],
                    'quarterly_earnings_growth': row[22],
                    'analyst_target_price': row[23],
                    'trailing_pe': row[24],
                    'forward_pe': row[25],
                    'price_to_sales': row[26],
                    'price_to_book': row[27],
                    'ev_to_revenue': row[28],
                    'ev_to_ebitda': row[29],
                }
        except Exception as e:
            app.logger.warning(f"Could not load fundamentals: {e}")

        # Get column names from stock_prices_daily
        columns = get_table_columns('stock_prices_daily', conn)
        # Exclude FRED indicators - they go in the Macro Dashboard
        valid_tickers = [t for t in all_tickers if t in columns and t not in FRED_INDICATORS]

        if not valid_tickers:
            return []

        # Get latest prices and previous day prices for all tickers
        ticker_cols = ', '.join([f'"{t}"' for t in valid_tickers])

        # Get last 252 rows for calculating changes
        query = f'''
            SELECT Date, {ticker_cols}
            FROM stock_prices_daily
            ORDER BY Date DESC
            LIMIT 252
        '''
        cursor.execute(query)
        rows = cursor.fetchall()

        # Process price data
        result = []
        for ticker in valid_tickers:
            idx = valid_tickers.index(ticker) + 1  # +1 for Date column

            # Find latest price
            latest_price = None
            latest_date = None
            prev_price = None
            week_ago_price = None
            month_ago_price = None
            year_ago_price = None

            for i, row in enumerate(rows):
                price = row[idx]
                if price is not None:
                    try:
                        price = float(price)
                    except (TypeError, ValueError):
                        continue
                    if latest_price is None:
                        latest_price = price
                        latest_date = row[0]
                    elif prev_price is None:
                        prev_price = price
                    if i >= 4 and week_ago_price is None:
                        week_ago_price = price
                    if i >= 20 and month_ago_price is None:
                        month_ago_price = price
                    if i >= 250 and year_ago_price is None:
                        year_ago_price = price
                        break

            if latest_price is None:
                continue

            # Calculate changes
            daily_change = ((latest_price - prev_price) / prev_price * 100) if prev_price else None
            weekly_change = ((latest_price - week_ago_price) / week_ago_price * 100) if week_ago_price else None
            monthly_change = ((latest_price - month_ago_price) / month_ago_price * 100) if month_ago_price else None
            yearly_change = ((latest_price - year_ago_price) / year_ago_price * 100) if year_ago_price else None

            # Get 52-week high/low
            prices_52w = []
            for row in rows[:252]:
                p = row[idx]
                if p is not None:
                    try:
                        prices_52w.append(float(p))
                    except (TypeError, ValueError):
                        pass
            high_52w = max(prices_52w) if prices_52w else None
            low_52w = min(prices_52w) if prices_52w else None

            meta = metadata.get(ticker, {})
            pages = page_info.get(ticker, [])
            fund = fundamentals.get(ticker, {})
            si = short_interest.get(ticker, {})

            result.append({
                'ticker': ticker,
                'name': meta.get('name', ticker),
                'latest_price': round(latest_price, 2) if latest_price else None,
                'latest_date': latest_date,
                'daily_change': round(daily_change, 2) if daily_change is not None else None,
                'weekly_change': round(weekly_change, 2) if weekly_change is not None else None,
                'monthly_change': round(monthly_change, 2) if monthly_change is not None else None,
                'yearly_change': round(yearly_change, 2) if yearly_change is not None else None,
                'high_52w': round(high_52w, 2) if high_52w else None,
                'low_52w': round(low_52w, 2) if low_52w else None,
                'first_date': meta.get('first_date'),
                'last_date': meta.get('last_date'),
                'data_points': meta.get('data_points'),
                'pages': pages,
                # Fundamentals data
                'sector': fund.get('sector'),
                'industry': fund.get('industry'),
                'market_cap': fund.get('market_cap'),
                'pe_ratio': fund.get('pe_ratio'),
                'peg_ratio': fund.get('peg_ratio'),
                'eps': fund.get('eps'),
                'dividend_yield': fund.get('dividend_yield'),
                'beta': fund.get('beta'),
                'moving_avg_50': fund.get('moving_avg_50'),
                'moving_avg_200': fund.get('moving_avg_200'),
                'shares_outstanding': fund.get('shares_outstanding'),
                'profit_margin': fund.get('profit_margin'),
                'operating_margin': fund.get('operating_margin'),
                'return_on_assets': fund.get('return_on_assets'),
                'return_on_equity': fund.get('return_on_equity'),
                'revenue': fund.get('revenue'),
                'revenue_per_share': fund.get('revenue_per_share'),
                'quarterly_revenue_growth': fund.get('quarterly_revenue_growth'),
                'gross_profit': fund.get('gross_profit'),
                'ebitda': fund.get('ebitda'),
                'diluted_eps': fund.get('diluted_eps'),
                'quarterly_earnings_growth': fund.get('quarterly_earnings_growth'),
                'analyst_target_price': fund.get('analyst_target_price'),
                'trailing_pe': fund.get('trailing_pe'),
                'forward_pe': fund.get('forward_pe'),
                'price_to_sales': fund.get('price_to_sales'),
                'price_to_book': fund.get('price_to_book'),
                'ev_to_revenue': fund.get('ev_to_revenue'),
                'ev_to_ebitda': fund.get('ev_to_ebitda'),
                # Short interest data
                'si_date': si.get('si_date'),
                'si_shares': si.get('si_shares'),
                'si_percent_float': si.get('si_percent_float'),
                'si_percent_outstanding': si.get('si_percent_outstanding'),
                'si_days_to_cover': si.get('si_days_to_cover'),
            })
    finally:
        conn.close()

    # Apply filter if provided (ticker, name, sector, industry, or page_name)
    if filter_text:
        filter_lower = filter_text.lower()
        result = [r for r in result if
                  filter_lower in r['ticker'].lower() or
                  (r['name'] and filter_lower in r['name'].lower()) or
                  (r.get('sector') and filter_lower in r['sector'].lower()) or
                  (r.get('industry') and filter_lower in r['industry'].lower()) or
                  any(filter_lower in p['page_name'].lower() for p in r['pages']) or
                  any(filter_lower in (p.get('chart_title') or '').lower() for p in r['pages'])]

    # Sort results
    reverse = sort_dir == 'desc'

    def numeric_sort_key(field):
        """Create a sort key function for numeric fields that handles None values."""
        return lambda x: x[field] if x[field] is not None else (float('inf') if reverse else float('-inf'))

    def string_sort_key(field):
        """Create a sort key function for string fields."""
        return lambda x: (x[field] or '').lower()

    sort_key_map = {
        # Existing fields
        'ticker': string_sort_key('ticker'),
        'name': string_sort_key('name'),
        'latest_price': numeric_sort_key('latest_price'),
        'daily_change': numeric_sort_key('daily_change'),
        'weekly_change': numeric_sort_key('weekly_change'),
        'monthly_change': numeric_sort_key('monthly_change'),
        'yearly_change': numeric_sort_key('yearly_change'),
        'high_52w': numeric_sort_key('high_52w'),
        'low_52w': numeric_sort_key('low_52w'),
        'data_points': numeric_sort_key('data_points'),
        # Fundamental fields - strings
        'sector': string_sort_key('sector'),
        'industry': string_sort_key('industry'),
        # Fundamental fields - numeric
        'market_cap': numeric_sort_key('market_cap'),
        'pe_ratio': numeric_sort_key('pe_ratio'),
        'peg_ratio': numeric_sort_key('peg_ratio'),
        'eps': numeric_sort_key('eps'),
        'dividend_yield': numeric_sort_key('dividend_yield'),
        'beta': numeric_sort_key('beta'),
        'moving_avg_50': numeric_sort_key('moving_avg_50'),
        'moving_avg_200': numeric_sort_key('moving_avg_200'),
        'shares_outstanding': numeric_sort_key('shares_outstanding'),
        'profit_margin': numeric_sort_key('profit_margin'),
        'operating_margin': numeric_sort_key('operating_margin'),
        'return_on_assets': numeric_sort_key('return_on_assets'),
        'return_on_equity': numeric_sort_key('return_on_equity'),
        'revenue': numeric_sort_key('revenue'),
        'revenue_per_share': numeric_sort_key('revenue_per_share'),
        'quarterly_revenue_growth': numeric_sort_key('quarterly_revenue_growth'),
        'gross_profit': numeric_sort_key('gross_profit'),
        'ebitda': numeric_sort_key('ebitda'),
        'diluted_eps': numeric_sort_key('diluted_eps'),
        'quarterly_earnings_growth': numeric_sort_key('quarterly_earnings_growth'),
        'analyst_target_price': numeric_sort_key('analyst_target_price'),
        'trailing_pe': numeric_sort_key('trailing_pe'),
        'forward_pe': numeric_sort_key('forward_pe'),
        'price_to_sales': numeric_sort_key('price_to_sales'),
        'price_to_book': numeric_sort_key('price_to_book'),
        'ev_to_revenue': numeric_sort_key('ev_to_revenue'),
        'ev_to_ebitda': numeric_sort_key('ev_to_ebitda'),
        # Short interest fields
        'si_shares': numeric_sort_key('si_shares'),
        'si_percent_float': numeric_sort_key('si_percent_float'),
        'si_percent_outstanding': numeric_sort_key('si_percent_outstanding'),
        'si_days_to_cover': numeric_sort_key('si_days_to_cover'),
    }
    sort_key = sort_key_map.get(sort_col, sort_key_map['ticker'])
    result.sort(key=sort_key, reverse=reverse)

    return result


@app.route('/api/dashboard')
def get_dashboard_data():
    """
    Get comprehensive dashboard data for all tickers in workspace.
    Supports pagination via query parameters:
      - limit: max results per page (default 50, max 500)
      - offset: starting index (default 0)
      - sort: column to sort by (default 'ticker')
      - sortDir: 'asc' or 'desc' (default 'asc')
      - filter: filter tickers/names containing this string
    Returns: { data: [...], total: N, limit: N, offset: N }
    """
    try:
        # Pagination parameters
        limit = min(int(request.args.get('limit', 50)), 500)
        offset = int(request.args.get('offset', 0))
        sort_col = request.args.get('sort', 'ticker')
        sort_dir = request.args.get('sortDir', 'asc')
        filter_text = request.args.get('filter', '').strip()

        # Build all rows using shared helper
        result = _build_dashboard_rows(filter_text, sort_col, sort_dir)

        # Calculate total before pagination
        total = len(result)

        # Apply pagination
        paginated = result[offset:offset + limit]

        app.logger.info(f"/api/dashboard: Returned {len(paginated)}/{total} tickers (offset={offset}, limit={limit})")
        return jsonify({
            'data': paginated,
            'total': total,
            'limit': limit,
            'offset': offset
        })

    except Exception as e:
        app.logger.error(f"/api/dashboard: Error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


@app.route('/api/dashboard/export')
def export_dashboard_data():
    """
    Export all filtered dashboard data as CSV or TSV.
    Query parameters:
      - format: 'csv' or 'tsv' (default 'tsv')
      - filter: filter tickers/names/pages containing this string
      - sort: column to sort by (default 'ticker')
      - sortDir: 'asc' or 'desc' (default 'asc')
      - limit: max rows to export (default 5000, max 5000)
    Returns: Streaming CSV/TSV file with Content-Disposition header.
    Sets X-Export-Truncated: 1 header if result was capped.
    """
    try:
        export_format = request.args.get('format', 'tsv').lower()
        filter_text = request.args.get('filter', '').strip()
        sort_col = request.args.get('sort', 'ticker')
        sort_dir = request.args.get('sortDir', 'asc')
        limit = min(int(request.args.get('limit', 5000)), 5000)

        # Build all rows using shared helper
        result = _build_dashboard_rows(filter_text, sort_col, sort_dir)
        total = len(result)

        # Apply limit
        truncated = total > limit
        result = result[:limit]

        # Define columns for export
        columns = [
            ('ticker', 'Ticker'),
            ('name', 'Name'),
            ('latest_price', 'Price'),
            ('daily_change', 'Day %'),
            ('weekly_change', 'Week %'),
            ('monthly_change', 'Month %'),
            ('yearly_change', 'Year %'),
            ('high_52w', '52w High'),
            ('low_52w', '52w Low'),
            ('data_points', 'Data Pts'),
            ('pages', 'Pages'),
        ]

        # Set up CSV writer
        delimiter = '\t' if export_format == 'tsv' else ','
        file_ext = 'tsv' if export_format == 'tsv' else 'csv'
        mime_type = 'text/tab-separated-values; charset=utf-8' if export_format == 'tsv' else 'text/csv; charset=utf-8'

        def sanitize_cell(value):
            """Prevent formula injection in Excel/Sheets by prefixing dangerous characters."""
            if isinstance(value, str) and value and value[0] in ('=', '+', '-', '@'):
                return "'" + value
            return value

        def generate():
            output = io.StringIO()
            writer = csv.writer(output, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL)

            # Write header row
            writer.writerow([col[1] for col in columns])
            yield output.getvalue()
            output.seek(0)
            output.truncate(0)

            # Write data rows
            for row in result:
                row_data = []
                for col_key, _ in columns:
                    value = row.get(col_key)
                    if col_key == 'pages':
                        # Join page names for export
                        if value and isinstance(value, list):
                            value = ', '.join(p.get('page_name', '') for p in value)
                        else:
                            value = ''
                    elif value is None:
                        value = ''
                    elif isinstance(value, float):
                        value = f'{value:.2f}'
                    # Sanitize string values to prevent formula injection
                    row_data.append(sanitize_cell(value))
                writer.writerow(row_data)
                yield output.getvalue()
                output.seek(0)
                output.truncate(0)

        # Create response with streaming
        response = Response(generate(), mimetype=mime_type)
        response.headers['Content-Disposition'] = f'attachment; filename="dashboard_export_{datetime.now().strftime("%Y%m%d")}.{file_ext}"'
        if truncated:
            response.headers['X-Export-Truncated'] = '1'
            response.headers['X-Export-Total'] = str(total)

        app.logger.info(f"/api/dashboard/export: Exported {len(result)}/{total} tickers (truncated={truncated})")
        return response

    except Exception as e:
        app.logger.error(f"/api/dashboard/export: Error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


@app.route('/api/macro-dashboard')
def get_macro_dashboard():
    """
    Get macro/FRED dashboard data.
    Returns: Array of FRED indicator data with values and changes.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Get column names from stock_prices_daily
        columns = get_table_columns('stock_prices_daily', conn)
        valid_indicators = [t for t in FRED_INDICATORS if t in columns]

        if not valid_indicators:
            conn.close()
            return jsonify([])

        # Get metadata for names
        placeholders = ','.join(['?' for _ in valid_indicators])
        cursor.execute(f"SELECT ticker, name FROM ticker_metadata WHERE ticker IN ({placeholders})", valid_indicators)
        metadata = {row['ticker']: row['name'] for row in cursor.fetchall()}

        # Get price data
        indicator_cols = ', '.join([f'"{t}"' for t in valid_indicators])
        query = f'''
            SELECT Date, {indicator_cols}
            FROM stock_prices_daily
            ORDER BY Date DESC
            LIMIT 252
        '''
        cursor.execute(query)
        rows = cursor.fetchall()

        result = []
        for indicator in valid_indicators:
            idx = valid_indicators.index(indicator) + 1  # +1 for Date column

            # Find latest value and changes
            latest_value = None
            latest_date = None
            prev_value = None
            week_ago_value = None
            month_ago_value = None
            year_ago_value = None
            high_52w = None
            low_52w = None

            for i, row in enumerate(rows):
                value = row[idx]
                if value is not None:
                    if latest_value is None:
                        latest_value = value
                        latest_date = row[0]
                        high_52w = value
                        low_52w = value
                    elif prev_value is None:
                        prev_value = value
                    if i >= 4 and week_ago_value is None and value is not None:
                        week_ago_value = value
                    if i >= 20 and month_ago_value is None and value is not None:
                        month_ago_value = value
                    if i >= 250 and year_ago_value is None and value is not None:
                        year_ago_value = value
                    # Track 52-week high/low
                    if high_52w is not None and value > high_52w:
                        high_52w = value
                    if low_52w is not None and value < low_52w:
                        low_52w = value

            # Calculate changes (absolute for rates/indices, not percentage)
            daily_change = None
            weekly_change = None
            monthly_change = None
            yearly_change = None

            if latest_value is not None:
                if prev_value is not None:
                    daily_change = latest_value - prev_value
                if week_ago_value is not None:
                    weekly_change = latest_value - week_ago_value
                if month_ago_value is not None:
                    monthly_change = latest_value - month_ago_value
                if year_ago_value is not None:
                    yearly_change = latest_value - year_ago_value

            # Categorize the indicator
            category = 'Other'
            if indicator in ['DGS2', 'DGS10', 'DGS30', 'FEDFUNDS', 'EFFR', 'SOFR', 'T10Y2Y', 'T10Y3M']:
                category = 'Interest Rates'
            elif indicator in ['CPIAUCSL', 'CPILFESL', 'PCEPI', 'PCE', 'T5YIE', 'T10YIE', 'T5YIFR']:
                category = 'Inflation'
            elif indicator in ['UNRATE', 'PAYEMS', 'ICSA', 'CCSA', 'JTSJOL']:
                category = 'Labor Market'
            elif indicator in ['GDP', 'GDPC1', 'INDPRO', 'UMCSENT', 'RSXFS', 'HOUST', 'PERMIT']:
                category = 'Economic Activity'
            elif indicator in ['M2SL', 'WALCL', 'RRPONTSYD']:
                category = 'Money Supply'
            elif indicator in ['MORTGAGE30US', 'BAMLH0A0HYM2', 'BAMLC0A0CM']:
                category = 'Credit Spreads'
            elif indicator in ['DTWEXBGS', 'DEXUSEU', 'DEXJPUS', 'DEXCHUS']:
                category = 'Currencies'
            elif indicator in ['WTI', 'DCOILWTICO', 'GASREGW']:
                category = 'Energy'

            result.append({
                'ticker': indicator,
                'name': metadata.get(indicator, indicator),
                'category': category,
                'latest_value': round(latest_value, 4) if latest_value else None,
                'latest_date': latest_date,
                'daily_change': round(daily_change, 4) if daily_change is not None else None,
                'weekly_change': round(weekly_change, 4) if weekly_change is not None else None,
                'monthly_change': round(monthly_change, 4) if monthly_change is not None else None,
                'yearly_change': round(yearly_change, 4) if yearly_change is not None else None,
                'high_52w': round(high_52w, 4) if high_52w else None,
                'low_52w': round(low_52w, 4) if low_52w else None
            })

        conn.close()

        # Sort by category then ticker
        result.sort(key=lambda x: (x['category'], x['ticker']))

        app.logger.info(f"/api/macro-dashboard: Returned {len(result)} indicators")
        return jsonify(result)

    except Exception as e:
        app.logger.error(f"/api/macro-dashboard: Error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


# --- Dashboard Sparklines endpoint ---
@app.route('/api/dashboard/sparklines')
def dashboard_sparklines():
    """Get sparkline data for dashboard - rebased to 100 for comparability.

    Query params:
        tickers: comma-separated list of ticker symbols (required, max 50)
        days: number of days of history (default: 30, max: 90)

    Response: { TICKER: [{time, value}, ...], ... }
    Values are rebased so first value = 100, subsequent values show % change.
    """
    tickers_str = request.args.get('tickers')
    if not tickers_str:
        return jsonify({'error': 'tickers parameter required'}), HTTP_BAD_REQUEST

    # Parse and limit tickers
    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    MAX_TICKERS = 50
    if len(tickers) > MAX_TICKERS:
        tickers = tickers[:MAX_TICKERS]
        app.logger.warning(f"/api/dashboard/sparklines: truncated to {MAX_TICKERS} tickers")

    if not tickers:
        return jsonify({}), HTTP_OK

    # Parse and limit days
    try:
        days = min(int(request.args.get('days', 30)), 730)  # Max 2 years for sparklines
    except ValueError:
        days = 30

    # Calculate date cutoff
    from datetime import timedelta
    cutoff_date = datetime.now() - timedelta(days=days)
    cutoff_str = cutoff_date.strftime('%Y-%m-%d')

    conn = get_db_connection()
    result = {}

    try:
        # Get available columns from stock_prices_daily
        stock_cols = get_table_columns('stock_prices_daily', conn)

        # Filter to valid tickers
        valid_tickers = [t for t in tickers if t in stock_cols]

        if not valid_tickers:
            conn.close()
            return jsonify({}), HTTP_OK

        # Fetch data for all valid tickers in one query
        # Use date() to normalize mixed date formats and filter nulls
        cols_str = ', '.join([f'MAX("{t}") as "{t}"' for t in valid_tickers])
        query = f"""
            SELECT date(Date) as Date, {cols_str}
            FROM stock_prices_daily
            WHERE date(Date) >= ?
            GROUP BY date(Date)
            ORDER BY date(Date) ASC
        """

        df = pd.read_sql_query(query, conn, params=[cutoff_str], parse_dates=['Date'])

        if df.empty:
            conn.close()
            return jsonify({}), HTTP_OK

        # Process each ticker
        for ticker in valid_tickers:
            if ticker not in df.columns:
                continue

            series = df[['Date', ticker]].dropna()
            if series.empty or len(series) < 2:
                continue

            # Get values and rebase to 100
            values = series[ticker].values
            first_val = values[0]
            if first_val == 0 or pd.isna(first_val):
                continue

            rebased = (values / first_val) * 100

            # Convert to output format
            times = (series['Date'].astype('int64') // 10**9).astype(int).values
            result[ticker] = [
                {'time': int(t), 'value': round(float(v), 2)}
                for t, v in zip(times, rebased)
            ]

        conn.close()

        # Add ETag for caching
        import hashlib
        etag = hashlib.md5(json.dumps(result, sort_keys=True).encode()).hexdigest()[:16]

        response = jsonify(result)
        response.headers['ETag'] = f'"{etag}"'
        response.headers['Cache-Control'] = 'public, max-age=300'  # 5 min cache

        app.logger.info(f"/api/dashboard/sparklines: returned {len(result)} tickers, {days} days")
        return response

    except Exception as e:
        conn.close()
        app.logger.error(f"/api/dashboard/sparklines: Error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


# --- Chart Image Export Endpoint ---
@app.route('/api/chart/image')
def get_chart_image():
    """Generate a chart image (PNG) for given ticker(s).

    Query params:
        ticker: Stock ticker (required), e.g., AAPL
        start: Start date (optional), e.g., 2024-01-01
        end: End date (optional), e.g., 2025-01-01
        title: Chart title (optional)
        width: Image width in inches (optional, default 10)
        height: Image height in inches (optional, default 6)

    Returns: PNG image
    """
    ticker = request.args.get('ticker', '').strip().upper()
    if not ticker:
        return jsonify({'error': 'ticker parameter required'}), HTTP_BAD_REQUEST

    # Resolve alias
    ticker = resolve_ticker_alias(ticker)

    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    title = request.args.get('title', ticker)
    width = float(request.args.get('width', 10))
    height = float(request.args.get('height', 6))

    try:
        conn = get_db_connection()

        # Wide format table: Date column + ticker columns
        # Check if ticker column exists
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(stock_prices_daily)")
        columns = [row[1] for row in cursor.fetchall()]

        if ticker not in columns:
            conn.close()
            return jsonify({'error': f'Ticker {ticker} not found in database'}), HTTP_NOT_FOUND

        # Build query for wide format
        query = f'SELECT Date, "{ticker}" FROM stock_prices_daily WHERE "{ticker}" IS NOT NULL'
        params = []

        if start_date:
            query += " AND Date >= ?"
            params.append(start_date)
        if end_date:
            query += " AND Date <= ?"
            params.append(end_date)

        query += " ORDER BY Date"

        df = pd.read_sql_query(query, conn, params=params)
        conn.close()

        if df.empty:
            return jsonify({'error': f'No data found for {ticker}'}), HTTP_NOT_FOUND

        # Rename columns
        df.columns = ['Date', 'Close']
        df['Date'] = pd.to_datetime(df['Date'])
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        df = df.dropna()

        # Create chart
        fig, ax = plt.subplots(figsize=(width, height))
        ax.plot(df['Date'], df['Close'], linewidth=1.5, color='#2962FF')

        # Style
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_xlabel('')
        ax.set_ylabel('Price', fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        fig.autofmt_xdate()

        # Add price annotation
        last_price = df['Close'].iloc[-1]
        last_date = df['Date'].iloc[-1]
        ax.annotate(f'${last_price:.2f}', xy=(last_date, last_price),
                   xytext=(10, 0), textcoords='offset points',
                   fontsize=10, fontweight='bold', color='#2962FF')

        plt.tight_layout()

        # Save to buffer
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=150, bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        buf.seek(0)
        plt.close(fig)

        return Response(buf.getvalue(), mimetype='image/png')

    except Exception as e:
        app.logger.error(f"Chart image error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


# --- Lightweight Charts Image Export Endpoint ---
# Requires: pip install playwright && playwright install chromium

# _check_playwright() now imported from helpers.py


@app.route('/api/chart/lw')
def get_chart_lw():
    """Generate a chart image using Lightweight Charts (same style as dashboard).

    Query params:
        tickers: Comma-separated tickers (required), e.g., AAPL,MSFT
        start: Start date (optional), e.g., 2024-01-01
        end: End date (optional), e.g., 2025-01-01
        title: Chart title (optional)
        width: Image width in pixels (optional, default 1200)
        height: Image height in pixels (optional, default 600)
        show_title: Show title on chart (optional, default true)
        show_last_date: Show last data date in bottom-left (optional, default true)
        normalize: Rebase all tickers to 0% at start (optional, default false)
        metrics: Fundamentals metrics to chart instead of price (optional)
                 Options: revenue, netIncome, eps, fcf, operatingIncome, ebitda, grossProfit
        forecast_start: Date to begin dotted forecast line (optional), e.g., 2026-01-01
        labels: Custom legend labels (optional), e.g., SMH_1_44X:SMH 1.44x Lev,NVDA:NVIDIA
        sort_by_last: Sort series by last value, high to low (optional, default false)
        primary: Primary ticker to assign first color (optional), e.g., AAPL

    Returns: PNG image
    """
    if not _check_playwright():
        return jsonify({
            'error': 'Playwright not installed. Run: pip install playwright && playwright install chromium'
        }), HTTP_INTERNAL_ERROR

    from playwright.sync_api import sync_playwright

    tickers_param = request.args.get('tickers', '').strip().upper()
    product_param_early = request.args.get('product', '').strip()  # Check early for product mode

    # tickers required unless in product mode
    if not tickers_param and not product_param_early:
        return jsonify({'error': 'tickers parameter required (or use product parameter)'}), HTTP_BAD_REQUEST

    # Parse and resolve tickers (may be empty for product mode)
    tickers = [resolve_ticker_alias(t.strip()) for t in tickers_param.split(',') if t.strip()] if tickers_param else []

    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    title = request.args.get('title', ', '.join(tickers) if tickers else product_param_early or 'Chart')
    width = int(request.args.get('width', 1200))
    height = int(request.args.get('height', 800))
    show_title = request.args.get('show_title', 'false').lower() == 'true'
    show_last_date = request.args.get('show_last_date', 'true').lower() != 'false'
    normalize = request.args.get('normalize', 'false').lower() == 'true'

    # Default to 8 years for normalized charts if no start date specified
    if normalize and not start_date:
        from datetime import datetime, timedelta
        start_date = (datetime.now() - timedelta(days=8*365)).strftime('%Y-%m-%d')
    forecast_start = request.args.get('forecast_start', '').strip()  # Date to start dotted forecast line
    labels_param = request.args.get('labels', '').strip()  # Custom legend labels: TICKER:Label,TICKER2:Label2
    show_last_value = request.args.get('show_last_value', 'false').lower() == 'true'  # Show last price label on chart
    sort_by_last = request.args.get('sort_by_last', 'false').lower() == 'true'  # Sort series by last value (high to low)
    primary_ticker = request.args.get('primary', '').strip().upper()  # Primary ticker gets first color (index 0)

    # Parse custom labels
    labels = {}
    if labels_param:
        for pair in labels_param.split(','):
            if ':' in pair:
                key, val = pair.split(':', 1)
                labels[key.strip().upper()] = val.strip()

    metrics_param = request.args.get('metrics', '').strip().lower()
    combine_panes = request.args.get('combine', 'false').lower() == 'true'  # Combine multiple metrics into single pane
    product_param = product_param_early  # Already parsed above
    product_metrics_param = request.args.get('product_metrics', '').strip().lower()  # e.g., global_mau,revenue

    # Product metrics mapping
    product_metric_map = {
        'global_mau': ('Global MAU', 'M'),
        'us_mau': ('US MAU', 'M'),
        'revenue': ('Revenue', 'B'),
        'dau': ('DAU', 'M'),
        'memory_gb': ('Memory', 'GB'),
        'bandwidth_tb': ('Bandwidth', 'TB/s'),
    }

    # Handle product metrics (e.g., TikTok MAU/DAU/Revenue)
    if product_param and product_metrics_param:
        prod_metrics = [m.strip() for m in product_metrics_param.split(',') if m.strip() in product_metric_map]
        if not prod_metrics:
            return jsonify({'error': f'No valid product metrics. Options: {", ".join(product_metric_map.keys())}'}), HTTP_BAD_REQUEST

        try:
            conn = get_db_connection()
            chart_data = {}

            for metric in prod_metrics:
                label, unit = product_metric_map[metric]
                series_name = f"{product_param} {label}"

                query = """
                    SELECT date, value
                    FROM product_metrics
                    WHERE product = ? AND metric = ?
                """
                params = [product_param, metric]
                if start_date:
                    query += " AND date >= ?"
                    params.append(start_date)
                if end_date:
                    query += " AND date <= ?"
                    params.append(end_date)
                query += " ORDER BY date ASC"

                df = pd.read_sql(query, conn, params=params)

                if not df.empty:
                    data_points = []
                    for _, row in df.iterrows():
                        try:
                            date_str = pd.to_datetime(row['date']).strftime('%Y-%m-%d')
                            value = row['value']
                            if pd.notna(value):
                                data_points.append({'time': date_str, 'value': float(value)})
                        except Exception:
                            continue
                    if data_points:
                        chart_data[series_name] = data_points

            conn.close()

            if not chart_data:
                return jsonify({'error': f'No product metrics data found for {product_param}'}), HTTP_NOT_FOUND

            # Build pane groups for multi-metric charts
            pane_groups = {}
            if len(prod_metrics) > 1:
                for metric in prod_metrics:
                    label, _ = product_metric_map[metric]
                    matching_series = [s for s in chart_data.keys() if label in s]
                    if matching_series:
                        pane_groups[label] = matching_series

            # Update title if not custom
            if title == ', '.join(tickers):
                metric_labels = [product_metric_map[m][0] for m in prod_metrics]
                title = f"{product_param} — {', '.join(metric_labels)}"

            chart_config = {
                'data': chart_data,
                'title': title,
                'width': width,
                'height': height,
                'showTitle': show_title,
                'showLastDate': show_last_date,
                'showLastValue': show_last_value,
                'normalize': normalize,
                'isFundamentals': True,  # Use bar chart style
                'forecastStart': forecast_start if forecast_start else None,
                'labels': labels if labels else None,
                'separatePanes': len(prod_metrics) > 1,
                'paneGroups': pane_groups if pane_groups else None
            }

            # Render with Playwright
            from playwright.sync_api import sync_playwright
            template_path = os.path.join(basedir, 'templates', 'chart_render.html')

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page(viewport={'width': width, 'height': height})
                page.goto(f'file://{template_path}')
                page.evaluate(f'''
                    window.CHART_CONFIG = {json.dumps(chart_config)};
                    renderChart(window.CHART_CONFIG);
                ''')
                page.wait_for_function('window.chartReady === true', timeout=10000)
                page.wait_for_timeout(200)
                screenshot_bytes = page.screenshot(type='png')
                browser.close()

            return Response(screenshot_bytes, mimetype='image/png')

        except Exception as e:
            app.logger.error(f"Product metrics chart error: {e}")
            traceback.print_exc()
            return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR

    # Fundamentals metric mapping
    metric_map = {
        'revenue': ('income_statement_quarterly', 'total_revenue', 'Revenue'),
        'netincome': ('income_statement_quarterly', 'net_income', 'Net Income'),
        'eps': ('earnings_quarterly', 'reported_eps', 'EPS'),
        'fcf': ('cash_flow_quarterly', 'free_cash_flow', 'Free Cash Flow'),
        'ocf': ('cash_flow_quarterly', 'operating_cashflow', 'Operating CF'),
        'operatingincome': ('income_statement_quarterly', 'operating_income', 'Op Income'),
        'ebitda': ('income_statement_quarterly', 'ebitda', 'EBITDA'),
        'grossprofit': ('income_statement_quarterly', 'gross_profit', 'Gross Profit'),
        'capex': ('cash_flow_quarterly', 'capital_expenditures', 'CapEx'),
        'dividends': ('cash_flow_quarterly', 'dividend_payout', 'Dividends'),
        'buybacks': ('cash_flow_quarterly', 'share_repurchases', 'Buybacks'),
        'cash': ('balance_sheet_quarterly', 'IFNULL(cash_and_equivalents,0) + IFNULL(short_term_investments,0)', 'Cash Position'),
        'employees': ('employee_count', 'employees', 'Employees'),
    }

    # If metrics specified, fetch fundamentals instead of price
    if metrics_param:
        metrics = [m.strip() for m in metrics_param.split(',') if m.strip() in metric_map]
        if not metrics:
            return jsonify({'error': f'No valid metrics. Options: {", ".join(metric_map.keys())}'}), HTTP_BAD_REQUEST

        try:
            conn = get_db_connection()
            chart_data = {}

            for ticker in tickers:
                for metric in metrics:
                    table, column, label = metric_map[metric]
                    series_name = f"{ticker} {label}" if len(tickers) > 1 or len(metrics) > 1 else label

                    # Build query with optional date filters (alias column as 'metric_value' for expressions)
                    # Skip date('now') filter if forecast_start is provided (allows future forecast data)
                    query = f"""
                        SELECT fiscal_date_ending, ({column}) as metric_value
                        FROM {table}
                        WHERE ticker = ?
                    """
                    if not forecast_start:
                        query += " AND fiscal_date_ending <= date('now')"
                    params = [ticker]
                    if start_date:
                        query += " AND fiscal_date_ending >= ?"
                        params.append(start_date)
                    if end_date:
                        query += " AND fiscal_date_ending <= ?"
                        params.append(end_date)
                    query += " ORDER BY fiscal_date_ending ASC"
                    df = pd.read_sql(query, conn, params=params)

                    if not df.empty:
                        data_points = []
                        for _, row in df.iterrows():
                            try:
                                date_str = fiscal_to_calendar_quarter(row['fiscal_date_ending'])
                                value = row['metric_value']
                                if pd.notna(value) and value != 0:
                                    data_points.append({'time': date_str, 'value': float(value)})
                            except Exception:
                                continue
                        if data_points:
                            chart_data[series_name] = data_points

            conn.close()

            if not chart_data:
                return jsonify({'error': 'No fundamentals data found'}), HTTP_NOT_FOUND

            # Sort series by last value (high to low) if requested
            if sort_by_last and chart_data:
                def get_last_value(series_name):
                    points = chart_data.get(series_name, [])
                    if not points:
                        return float('-inf')
                    return points[-1]['value'] if points else float('-inf')

                sorted_names = sorted(chart_data.keys(), key=get_last_value, reverse=True)
                chart_data = {n: chart_data[n] for n in sorted_names}

            # Ensure primary ticker series are first (gets color index 0)
            # For fundamentals, series names include metric (e.g., "AAPL Revenue")
            if primary_ticker and chart_data:
                primary_series = [n for n in chart_data.keys() if n.startswith(primary_ticker)]
                other_series = [n for n in chart_data.keys() if not n.startswith(primary_ticker)]
                if primary_series:
                    chart_data = {**{n: chart_data[n] for n in primary_series},
                                  **{n: chart_data[n] for n in other_series}}

            # Update title if not custom
            if title == ', '.join(tickers):
                metric_labels = [metric_map[m][2] for m in metrics]
                title = f"{', '.join(tickers)} — {', '.join(metric_labels)}"

            # Build pane groups for multi-metric charts (separate panes for each metric)
            pane_groups = {}
            if len(metrics) > 1:
                for metric in metrics:
                    label = metric_map[metric][2]
                    # Find all series for this metric
                    matching_series = [s for s in chart_data.keys() if label in s]
                    if matching_series:
                        pane_groups[label] = matching_series

            chart_config = {
                'data': chart_data,
                'title': title,
                'width': width,
                'height': height,
                'showTitle': show_title,
                'showLastDate': show_last_date,
                'showLastValue': show_last_value,
                'normalize': normalize,
                'isFundamentals': True,
                'forecastStart': forecast_start if forecast_start else None,
                'labels': labels if labels else None,
                'separatePanes': len(metrics) > 1 and not combine_panes,
                'paneGroups': pane_groups if (pane_groups and not combine_panes) else None
            }

            # Render with Playwright
            from playwright.sync_api import sync_playwright
            template_path = os.path.join(basedir, 'templates', 'chart_render.html')

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page(viewport={'width': width, 'height': height})
                page.goto(f'file://{template_path}')
                page.evaluate(f'''
                    window.CHART_CONFIG = {json.dumps(chart_config)};
                    renderChart(window.CHART_CONFIG);
                ''')
                page.wait_for_function('window.chartReady === true', timeout=10000)
                page.wait_for_timeout(200)
                screenshot_bytes = page.screenshot(type='png')
                browser.close()

            return Response(screenshot_bytes, mimetype='image/png')

        except Exception as e:
            app.logger.error(f"Fundamentals chart error: {e}")
            traceback.print_exc()
            return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Get available columns
        cursor.execute("PRAGMA table_info(stock_prices_daily)")
        available_columns = [row[1] for row in cursor.fetchall()]

        # Filter to tickers that exist in database
        valid_tickers = [t for t in tickers if t in available_columns]
        if not valid_tickers:
            conn.close()
            return jsonify({'error': f'No valid tickers found. Requested: {tickers}'}), HTTP_NOT_FOUND

        # Build query for all tickers
        columns_sql = ', '.join([f'"{t}"' for t in valid_tickers])
        query = f'SELECT Date, {columns_sql} FROM stock_prices_daily WHERE 1=1'
        params = []

        if start_date:
            query += " AND Date >= ?"
            params.append(start_date)
        if end_date:
            query += " AND Date <= ?"
            params.append(end_date)

        query += " ORDER BY Date"

        df = pd.read_sql_query(query, conn, params=params)
        conn.close()

        if df.empty:
            return jsonify({'error': 'No data found for specified tickers/date range'}), HTTP_NOT_FOUND

        # Convert to chart data format: { AAPL: [{time, value}, ...], MSFT: [...] }
        # Use date strings (YYYY-MM-DD) which Lightweight Charts handles well
        chart_data = {}
        seen_dates = set()  # Track dates to skip duplicates
        for ticker in valid_tickers:
            ticker_df = df[['Date', ticker]].dropna()
            if not ticker_df.empty:
                ticker_points = []
                for _, row in ticker_df.iterrows():
                    # Convert to date string, skip duplicates
                    date_str = pd.to_datetime(row['Date']).strftime('%Y-%m-%d')
                    date_key = (ticker, date_str)
                    if date_key not in seen_dates:
                        seen_dates.add(date_key)
                        ticker_points.append({
                            'time': date_str,
                            'value': float(row[ticker])
                        })
                if ticker_points:
                    chart_data[ticker] = ticker_points

        if not chart_data:
            return jsonify({'error': 'No valid data after processing'}), HTTP_NOT_FOUND

        # Sort series by last value (high to low) if requested
        if sort_by_last and chart_data:
            # For normalized charts, find common start date (latest start across all tickers)
            # This matches the JavaScript normalization logic in chart_render.html
            common_start = None
            if normalize:
                start_dates = []
                for ticker, points in chart_data.items():
                    if points:
                        start_dates.append(points[0]['time'])
                if start_dates:
                    common_start = max(start_dates)  # Latest start = common start

            def get_sort_value(ticker):
                points = chart_data.get(ticker, [])
                if not points or len(points) < 2:
                    return float('-inf')
                if normalize and common_start:
                    # Find value at common start date (first point >= common_start)
                    base_val = None
                    for p in points:
                        if p['time'] >= common_start:
                            base_val = p['value']
                            break
                    last_val = points[-1]['value']
                    if base_val and base_val != 0:
                        return ((last_val - base_val) / base_val) * 100
                    return float('-inf')
                else:
                    # For raw charts, sort by last value
                    return points[-1]['value']

            sorted_tickers = sorted(chart_data.keys(), key=get_sort_value, reverse=True)
            chart_data = {t: chart_data[t] for t in sorted_tickers}

        # Ensure primary ticker is first (gets color index 0)
        if primary_ticker and primary_ticker in chart_data:
            chart_data = {primary_ticker: chart_data[primary_ticker],
                          **{t: v for t, v in chart_data.items() if t != primary_ticker}}

        # Prepare config for the HTML template
        chart_config = {
            'data': chart_data,
            'title': title,
            'width': width,
            'height': height,
            'showTitle': show_title,
            'showLastDate': show_last_date,
            'showLastValue': show_last_value,
            'normalize': normalize,
            'forecastStart': forecast_start if forecast_start else None,
            'labels': labels if labels else None
        }
        # Get the HTML template path
        template_path = os.path.join(basedir, 'templates', 'chart_render.html')
        if not os.path.exists(template_path):
            return jsonify({'error': 'Chart template not found'}), HTTP_INTERNAL_ERROR

        # Render with Playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': width, 'height': height})

            # Load the HTML template
            page.goto(f'file://{template_path}')

            # Inject the chart configuration and render
            page.evaluate(f'''
                window.CHART_CONFIG = {json.dumps(chart_config)};
                renderChart(window.CHART_CONFIG);
            ''')

            # Wait for chart to render
            page.wait_for_function('window.chartReady === true', timeout=10000)

            # Small delay for any animations to complete
            page.wait_for_timeout(200)

            # Take screenshot
            screenshot_bytes = page.screenshot(type='png')

            browser.close()

        return Response(screenshot_bytes, mimetype='image/png')

    except Exception as e:
        app.logger.error(f"Lightweight Charts image error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


@app.route('/api/chart/segment')
def get_chart_segment():
    """Generate segment-level charts from segment_quarterly table.

    Query params:
        ticker: Ticker symbol (required), e.g., GOOGL
        segments: Comma-separated segments (required), e.g., cloud,services
        metric: Metric to chart (required): revenue, operating_income, margin
        width: Image width (optional, default 1200)
        height: Image height (optional, default 600)
        title: Chart title (optional)
        chart_type: line or bar (optional, default line)

    Returns: PNG image
    """
    if not _check_playwright():
        return jsonify({
            'error': 'Playwright not installed. Run: pip install playwright && playwright install chromium'
        }), HTTP_INTERNAL_ERROR

    from playwright.sync_api import sync_playwright

    ticker = request.args.get('ticker', '').strip().upper()
    if not ticker:
        return jsonify({'error': 'ticker parameter required'}), HTTP_BAD_REQUEST

    segments_param = request.args.get('segments', '').strip().lower()
    if not segments_param:
        return jsonify({'error': 'segments parameter required'}), HTTP_BAD_REQUEST

    metric = request.args.get('metric', '').strip().lower()
    if not metric:
        return jsonify({'error': 'metric parameter required (revenue, operating_income, margin)'}), HTTP_BAD_REQUEST

    segments = [s.strip() for s in segments_param.split(',') if s.strip()]
    width = int(request.args.get('width', 1200))
    height = int(request.args.get('height', 600))
    title = request.args.get('title', '')
    chart_type = request.args.get('chart_type', 'line').lower()

    # Metric labels
    metric_labels = {
        'revenue': 'Revenue ($B)',
        'operating_income': 'Operating Income ($B)',
        'margin': 'Margin (%)',
    }

    try:
        conn = get_db_connection()
        chart_data = {}

        for segment in segments:
            display_name = segment.replace('_', ' ').title()

            query = """
                SELECT fiscal_date_ending, value
                FROM segment_quarterly
                WHERE ticker = ? AND segment = ? AND metric = ?
                ORDER BY fiscal_date_ending ASC
            """
            df = pd.read_sql(query, conn, params=[ticker, segment, metric])

            if not df.empty:
                data_points = []
                for _, row in df.iterrows():
                    try:
                        date_str = pd.to_datetime(row['fiscal_date_ending']).strftime('%Y-%m-%d')
                        value = row['value']
                        if pd.notna(value):
                            data_points.append({'time': date_str, 'value': float(value)})
                    except Exception:
                        continue
                if data_points:
                    chart_data[display_name] = data_points

        conn.close()

        if not chart_data:
            return jsonify({'error': f'No segment data found for {ticker}'}), HTTP_NOT_FOUND

        # Build title if not provided
        if not title:
            metric_label = metric_labels.get(metric, metric.title())
            title = f"{ticker} — {metric_label}"

        chart_config = {
            'data': chart_data,
            'title': title,
            'width': width,
            'height': height,
            'showTitle': False,
            'showLastDate': True,
            'showLastValue': False,
            'normalize': False,
            'isFundamentals': chart_type == 'bar',
            'forecastStart': None,
            'labels': None,
        }

        # Render with Playwright
        template_path = os.path.join(basedir, 'templates', 'chart_render.html')

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': width, 'height': height})
            page.goto(f'file://{template_path}')
            page.evaluate(f'''
                window.CHART_CONFIG = {json.dumps(chart_config)};
                renderChart(window.CHART_CONFIG);
            ''')
            page.wait_for_function('window.chartReady === true', timeout=10000)
            page.wait_for_timeout(200)
            screenshot_bytes = page.screenshot(type='png')
            browser.close()

        return Response(screenshot_bytes, mimetype='image/png')

    except Exception as e:
        app.logger.error(f"Segment chart error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


# Register fundamentals routes
try:
    from fundamentals_routes import fundamentals_bp
    app.register_blueprint(fundamentals_bp)
    app.logger.info("Fundamentals routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Fundamentals routes not available: {e}")

# Register data routes
try:
    from data_routes import data_bp
    app.register_blueprint(data_bp)
    app.logger.info("Data routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Data routes not available: {e}")

# Register diag routes
try:
    from diag_routes import diag_bp
    app.register_blueprint(diag_bp)
    app.logger.info("Diag routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Diag routes not available: {e}")

# Register short interest routes
try:
    from short_interest_routes import short_interest_bp
    app.register_blueprint(short_interest_bp)
    app.logger.info("Short interest routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Short interest routes not available: {e}")

# Register IV routes
try:
    from iv_routes import iv_bp
    app.register_blueprint(iv_bp)
    app.logger.info("IV routes registered successfully")
except ImportError as e:
    app.logger.warning(f"IV routes not available: {e}")

# Register content routes
try:
    from content_routes import content_bp
    app.register_blueprint(content_bp)
    app.logger.info("Content routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Content routes not available: {e}")

# Register portfolio routes
try:
    from portfolio_routes import portfolio_bp
    app.register_blueprint(portfolio_bp)
    app.logger.info("Portfolio routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Portfolio routes not available: {e}")

# Register thesis routes
try:
    from thesis_routes import thesis_bp
    app.register_blueprint(thesis_bp)
    app.logger.info("Thesis routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Thesis routes not available: {e}")

if __name__ == '__main__':
    app.run(debug=True, port=DEFAULT_PORT)
