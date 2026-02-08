"""
Dashboard API routes.
Routes: /api/dashboard, /api/dashboard/export, /api/dashboard/sparklines, /api/macro-dashboard
"""
import csv
import io
import json
import hashlib
import logging
import traceback
import sys
import os
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request, Response
import pandas as pd
from constants import (get_db_connection, WORKSPACE_FILENAME,
                      HTTP_OK, HTTP_BAD_REQUEST, HTTP_INTERNAL_ERROR)
from helpers import basedir, get_table_columns, FRED_INDICATORS

logger = logging.getLogger(__name__)

dashboard_bp = Blueprint('dashboard', __name__)


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
            logger.warning(f"Could not load short interest: {e}")

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
            logger.warning(f"Could not load fundamentals: {e}")

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


@dashboard_bp.route('/api/dashboard')
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

        logger.info(f"/api/dashboard: Returned {len(paginated)}/{total} tickers (offset={offset}, limit={limit})")
        return jsonify({
            'data': paginated,
            'total': total,
            'limit': limit,
            'offset': offset
        })

    except Exception as e:
        logger.error(f"/api/dashboard: Error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


@dashboard_bp.route('/api/dashboard/export')
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

        logger.info(f"/api/dashboard/export: Exported {len(result)}/{total} tickers (truncated={truncated})")
        return response

    except Exception as e:
        logger.error(f"/api/dashboard/export: Error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


@dashboard_bp.route('/api/macro-dashboard')
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

        logger.info(f"/api/macro-dashboard: Returned {len(result)} indicators")
        return jsonify(result)

    except Exception as e:
        logger.error(f"/api/macro-dashboard: Error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR


# --- Dashboard Sparklines endpoint ---
@dashboard_bp.route('/api/dashboard/sparklines')
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
        logger.warning(f"/api/dashboard/sparklines: truncated to {MAX_TICKERS} tickers")

    if not tickers:
        return jsonify({}), HTTP_OK

    # Parse and limit days
    try:
        days = min(int(request.args.get('days', 30)), 730)  # Max 2 years for sparklines
    except ValueError:
        days = 30

    # Calculate date cutoff
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
        etag = hashlib.md5(json.dumps(result, sort_keys=True).encode()).hexdigest()[:16]

        response = jsonify(result)
        response.headers['ETag'] = f'"{etag}"'
        response.headers['Cache-Control'] = 'public, max-age=300'  # 5 min cache

        logger.info(f"/api/dashboard/sparklines: returned {len(result)} tickers, {days} days")
        return response

    except Exception as e:
        conn.close()
        logger.error(f"/api/dashboard/sparklines: Error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), HTTP_INTERNAL_ERROR
