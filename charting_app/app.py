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

def fiscal_to_calendar_quarter(date):
    """Map a fiscal quarter end date to the nearest calendar quarter end.

    Jan-Mar → Mar 31 (Q1)
    Apr-Jun → Jun 30 (Q2)
    Jul-Sep → Sep 30 (Q3)
    Oct-Dec → Dec 31 (Q4)
    """
    if isinstance(date, str):
        date = pd.to_datetime(date)
    month = date.month
    year = date.year
    if month <= 3:
        return f"{year}-03-31"
    elif month <= 6:
        return f"{year}-06-30"
    elif month <= 9:
        return f"{year}-09-30"
    else:
        return f"{year}-12-31"

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import (DB_PATH, get_db_connection, SCHEMA_CACHE_TTL, DEFAULT_PORT,
                      CACHE_CONTROL_MAX_AGE, WORKSPACE_FILENAME,
                      WORKSPACE_TEMP_SUFFIX, HTTP_OK, HTTP_BAD_REQUEST,
                      HTTP_NOT_FOUND, HTTP_INTERNAL_ERROR,
                      resolve_ticker_alias, TICKER_ALIASES)

# DuckDB support - imports USE_DUCKDB from constants (set via USE_DUCKDB=1 env var)
from constants import USE_DUCKDB
if USE_DUCKDB:
    try:
        from duckdb_queries import (
            check_duckdb_available, get_price_data, get_volume_data,
            get_all_tickers_list, get_available_tickers, get_futures_tickers,
            get_bond_tickers, get_metadata, get_dashboard_prices
        )
        DUCKDB_AVAILABLE = check_duckdb_available()
    except ImportError:
        DUCKDB_AVAILABLE = False
else:
    DUCKDB_AVAILABLE = False

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

# Get the absolute path of the directory containing this script (charting_app)
basedir = os.path.abspath(os.path.dirname(__file__))
# Using centralized DB_PATH and get_db_connection() from constants.py
# DB_PATH comes from constants.resolve_db_path(), which prefers market_data.db and falls back to sp500_data.db.

# Schema cache for performance
_schema_cache = {}
_schema_cache_time = 0

# --- Start of Diagnostic Logging ---
app.logger.info(f"SCRIPT_DIR: {basedir}")
app.logger.info(f"DB_PATH: {DB_PATH}")
app.logger.info(f"USE_DUCKDB: {USE_DUCKDB}, DUCKDB_AVAILABLE: {DUCKDB_AVAILABLE}")
if not os.path.exists(DB_PATH):
    app.logger.error("FATAL: DATABASE NOT FOUND AT THE CALCULATED PATH!")
else:
    app.logger.info("SUCCESS: Database file was found at the path.")
# --- End of Diagnostic Logging ---

# --- Helper Functions ---
def get_table_columns(table_name, conn=None, force_refresh=False):
    """Get column names for a table with caching."""
    global _schema_cache, _schema_cache_time
    
    # Check if cache needs refresh
    if force_refresh or time.time() - _schema_cache_time > SCHEMA_CACHE_TTL:
        _schema_cache = {}
        _schema_cache_time = time.time()
        app.logger.info(f"Schema cache refreshed")
    
    # Return cached result if available
    if table_name in _schema_cache:
        return _schema_cache[table_name]
    
    # Fetch and cache column names
    close_conn = False
    if conn is None:
        conn = get_db_connection()
        close_conn = True
    
    try:
        cursor = conn.execute(f"PRAGMA table_info({table_name})")
        # PRAGMA returns tuples: (cid, name, type, notnull, dflt_value, pk)
        columns = {row[1] for row in cursor.fetchall()}
        _schema_cache[table_name] = columns
        app.logger.info(f"Cached schema for table {table_name}: {len(columns)} columns")
        return columns
    except sqlite3.OperationalError:
        _schema_cache[table_name] = set()
        return set()
    finally:
        if close_conn:
            conn.close()


# --- Short Interest Synthetic Ticker Support ---
# Patterns: AAPL_SI_PCT -> short_percent_float, AAPL_SI_DAYS -> days_to_cover
SI_PATTERNS = {
    '_SI_PCT': 'short_percent_float',
    '_SI_DAYS': 'days_to_cover',
}


def parse_si_ticker(ticker):
    """Parse a synthetic SI ticker into (base_ticker, column) or (None, None) if not SI."""
    for suffix, column in SI_PATTERNS.items():
        if ticker.endswith(suffix):
            return ticker[:-len(suffix)], column
    return None, None


def get_si_tickers_with_data():
    """Get list of base tickers that have short interest data."""
    conn = get_db_connection()
    try:
        cursor = conn.execute("SELECT DISTINCT ticker FROM short_interest")
        return [row[0] for row in cursor.fetchall()]
    except sqlite3.OperationalError:
        return []
    finally:
        conn.close()


def get_si_timeseries(base_ticker, column, start_date=None, end_date=None):
    """
    Get short interest time series with forward-fill to trading dates.

    SI data is published bi-monthly on settlement dates. This function:
    1. Fetches SI settlement data for the ticker
    2. Gets all trading dates from stock_prices_daily
    3. Forward-fills SI values to each trading date

    Returns: list of {time: unix_seconds, value: float}
    """
    conn = get_db_connection()
    try:
        # Resolve ticker alias
        db_ticker = resolve_ticker_alias(base_ticker)

        # Build date filters
        date_filter = ""
        if start_date:
            date_filter += f" AND settlement_date >= '{start_date}'"
        if end_date:
            date_filter += f" AND settlement_date <= '{end_date}'"

        # Get SI settlement data
        si_query = f"""
            SELECT settlement_date, {column}
            FROM short_interest
            WHERE ticker = ? {date_filter}
            ORDER BY settlement_date ASC
        """
        cursor = conn.execute(si_query, (db_ticker,))
        si_data = cursor.fetchall()

        if not si_data:
            return []

        # Get all trading dates from stock_prices_daily
        # Use Date column presence to get trading days
        dates_query = """
            SELECT DISTINCT date(Date) as d
            FROM stock_prices_daily
            WHERE Date IS NOT NULL
        """
        if start_date:
            dates_query += f" AND date(Date) >= '{start_date}'"
        if end_date:
            dates_query += f" AND date(Date) <= '{end_date}'"
        dates_query += " ORDER BY d ASC"

        cursor = conn.execute(dates_query)
        trading_dates = [row[0] for row in cursor.fetchall()]

        if not trading_dates:
            return []

        # Forward-fill SI values to each trading date
        result = []
        si_idx = 0
        current_value = None

        for date_str in trading_dates:
            # Advance SI index while settlement_date <= current date
            while si_idx < len(si_data) and si_data[si_idx][0] <= date_str:
                current_value = si_data[si_idx][1]
                si_idx += 1

            if current_value is not None:
                # Convert date to unix timestamp
                try:
                    dt = pd.to_datetime(date_str)
                    unix_time = int(dt.timestamp())
                    result.append({'time': unix_time, 'value': float(current_value)})
                except (ValueError, TypeError):
                    continue

        return result
    except sqlite3.OperationalError as e:
        app.logger.warning(f"SI query failed for {base_ticker}: {e}")
        return []
    finally:
        conn.close()


# Diagnostic: run the same transform as /api/data for a single ticker
@app.route('/api/diag_reduce')
def diag_reduce():
    ticker = (request.args.get('ticker') or '^VXD').strip().upper()
    conn = get_db_connection()
    try:
        # Detect table
        try:
            stock_cols = {row['name'] for row in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            stock_cols = set()
        try:
            fut_cols = {row['name'] for row in conn.execute("PRAGMA table_info(futures_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            fut_cols = set()
        # Check futures table first for =F tickers (has more recent data)
        if ticker in fut_cols and ticker.endswith('=F'):
            table = 'futures_prices_daily'
        elif ticker in stock_cols:
            table = 'stock_prices_daily'
        elif ticker in fut_cols:
            table = 'futures_prices_daily'
        else:
            return jsonify({'error': 'ticker not found', 'db_path': DB_PATH}), 404
        q = (
            f'SELECT date(Date) AS Date, MAX("{ticker}") as value '
            f'FROM {table} '
            f'WHERE "{ticker}" IS NOT NULL '
            f'GROUP BY date(Date) '
            f'ORDER BY date(Date) ASC'
        )
        df = pd.read_sql_query(q, conn, parse_dates=['Date'])
        if df.empty:
            return jsonify({'ticker': ticker, 'records': []})
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date', 'value'])
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        df = df.dropna(subset=['value'])
        df = df.sort_values('Date')
        day = df['Date'].dt.normalize()
        df = df.assign(Date=day).groupby('Date', as_index=False)['value'].median()
        df['time'] = (df['Date'].astype('int64') // 10**9).astype(int)
        records = df[['time', 'value']].to_dict(orient='records')
        return jsonify({'ticker': ticker, 'records': records, 'db_path': DB_PATH})
    finally:
        conn.close()

def fetch_ticker_data(table_name, tickers, date_column='Date', value_columns=None, conn=None):
    """Fetch ticker data from any table with consistent interface.
    
    Args:
        table_name: Name of the table to query
        tickers: List of ticker symbols
        date_column: Name of the date column (default: 'Date')
        value_columns: List of columns to fetch (defaults to tickers)
        conn: Database connection (will create if None)
    
    Returns:
        dict: {ticker: DataFrame} mapping
    """
    close_conn = False
    if conn is None:
        conn = get_db_connection()
        close_conn = True
    
    if value_columns is None:
        value_columns = tickers
    
    result = {}
    try:
        # Get available columns
        table_cols = get_table_columns(table_name, conn)
        valid_tickers = [t for t in value_columns if t in table_cols]
        
        if not valid_tickers:
            return result
        
        # Build query
        columns_str = f"{date_column}, " + ", ".join([f'"{t}"' for t in valid_tickers])
        query = f"SELECT {columns_str} FROM {table_name} ORDER BY {date_column}"
        
        # Log slow queries
        start_time = time.time()
        df = pd.read_sql(query, conn, parse_dates=[date_column], index_col=date_column)
        query_time = time.time() - start_time
        
        if query_time > 1.0:  # Log queries taking more than 1 second
            app.logger.warning(f"Slow query ({query_time:.2f}s): {table_name} for {len(valid_tickers)} tickers")
        
        # Split into per-ticker DataFrames
        for ticker in valid_tickers:
            if ticker in df.columns:
                result[ticker] = df[[ticker]].dropna()
    
    except Exception as e:
        app.logger.error(f"Error fetching from {table_name}: {e}")
    finally:
        if close_conn:
            conn.close()
    
    return result

@app.route('/')
def index():
    """Redirect root to sandbox UI"""
    return redirect('/sandbox/')

@app.route('/api/health')
def health():
    """Health check endpoint for monitoring."""
    try:
        # Test database connection
        conn = get_db_connection()
        cursor = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
        table_count = cursor.fetchone()[0]
        conn.close()
        
        return jsonify({
            'status': 'healthy',
            'timestamp': time.time(),
            'database': 'connected',
            'table_count': table_count,
            'cache_size': len(_schema_cache),
            'cache_age': time.time() - _schema_cache_time if _schema_cache_time > 0 else None
        }), 200
    except Exception as e:
        app.logger.error(f"Health check failed: {e}")
        return jsonify({
            'status': 'unhealthy',
            'timestamp': time.time(),
            'error': str(e)
        }), 503

# --- Diagnostic endpoint to inspect active DB and a specific ticker/date ---
@app.route('/api/diag')
def diag():
    """Return DB path and the server-observed value for a given ticker/date.
    Query params:
        ticker: symbol (default '^VXD')
        date: YYYY-MM-DD (default '2021-07-13')
    """
    ticker = (request.args.get('ticker') or '^VXD').strip().upper()
    date = (request.args.get('date') or '2021-07-13').strip()

    conn = None
    try:
        conn = get_db_connection()
        # Column presence
        try:
            stock_cols = {row['name'] for row in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            stock_cols = set()
        try:
            futures_cols = {row['name'] for row in conn.execute("PRAGMA table_info(futures_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            futures_cols = set()

        table = None
        # Check futures table first for =F tickers (has more recent data)
        if ticker in futures_cols and ticker.endswith('=F'):
            table = 'futures_prices_daily'
        elif ticker in stock_cols:
            table = 'stock_prices_daily'
        elif ticker in futures_cols:
            table = 'futures_prices_daily'

        value = None
        row_count = None
        all_vals = []
        if table:
            row = conn.execute(f'SELECT "{ticker}" FROM {table} WHERE Date = ?', (date,)).fetchone()
            value = row[0] if row else None
            try:
                row_count = conn.execute(f'SELECT COUNT(1) FROM {table} WHERE Date = ?', (date,)).fetchone()[0]
                all_vals = [r[0] for r in conn.execute(f'SELECT "{ticker}" FROM {table} WHERE Date = ?', (date,)).fetchall()]
            except Exception:
                pass

        return jsonify({
            'db_path': DB_PATH,
            'ticker': ticker,
            'date': date,
            'table': table,
            'stock_has_col': ticker in stock_cols,
            'futures_has_col': ticker in futures_cols,
            'value': value,
            'row_count_for_date': row_count,
            'all_values_for_date': all_vals
        }), 200
    except Exception as e:
        return jsonify({'error': str(e), 'db_path': DB_PATH}), 500
    finally:
        if conn is not None:
            conn.close()

# Sandbox static serving
@app.route('/sandbox/')
@app.route('/sandbox/<path:filename>')
def sandbox_static(filename='index.html'):
    sandbox_dir = os.path.abspath(os.path.join(basedir, '..', 'charting_sandbox'))
    return send_from_directory(sandbox_dir, filename)

@app.route('/api/tickers')
def get_tickers():
    """Provides a sorted list of all available tickers from the database."""
    app.logger.info("Request received for /api/tickers")
    try:
        # Use DuckDB if enabled
        if USE_DUCKDB and DUCKDB_AVAILABLE:
            tickers = get_all_tickers_list()
            # Add portfolios from SQLite (portfolio data not migrated yet)
            conn = get_db_connection()
            try:
                cursor = conn.execute("SELECT portfolio_id FROM portfolios ORDER BY portfolio_id")
                for row in cursor.fetchall():
                    tickers.append(f"PORTFOLIO_{row[0]}")
            except sqlite3.OperationalError:
                pass
            # Add SI synthetic tickers
            try:
                cursor = conn.execute("SELECT DISTINCT ticker FROM short_interest")
                for row in cursor.fetchall():
                    base = row[0]
                    for suffix in SI_PATTERNS.keys():
                        tickers.append(f"{base}{suffix}")
            except sqlite3.OperationalError:
                pass
            conn.close()
            tickers = sorted(set(tickers))
            app.logger.info(f"[DuckDB] Found {len(tickers)} tickers")
            return jsonify(tickers)

        # SQLite fallback
        conn = get_db_connection()
        tickers_set = set()

        # Collect columns from stock table
        try:
            cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
            # PRAGMA returns tuples: (cid, name, type, notnull, dflt_value, pk)
            tickers_set.update(row[1] for row in cursor.fetchall() if row[1] != 'Date')
        except sqlite3.OperationalError:
            app.logger.warning("Table 'stock_prices_daily' not found.")

        # Collect columns from futures table
        try:
            cursor = conn.execute("PRAGMA table_info(futures_prices_daily)")
            # PRAGMA returns tuples: (cid, name, type, notnull, dflt_value, pk)
            tickers_set.update(row[1] for row in cursor.fetchall() if row[1] != 'Date')
        except sqlite3.OperationalError:
            app.logger.warning("Table 'futures_prices_daily' not found.")

        # Collect columns from bonds table
        try:
            cursor = conn.execute("PRAGMA table_info(bond_prices_daily)")
            # PRAGMA returns tuples: (cid, name, type, notnull, dflt_value, pk)
            tickers_set.update(row[1] for row in cursor.fetchall() if row[1] != 'Date')
        except sqlite3.OperationalError:
            app.logger.warning("Table 'bond_prices_daily' not found.")

        # Collect columns from FRED series table
        try:
            cursor = conn.execute("PRAGMA table_info(fred_series)")
            tickers_set.update(row[1] for row in cursor.fetchall() if row[1] != 'Date')
        except sqlite3.OperationalError:
            app.logger.warning("Table 'fred_series' not found.")

        # Add portfolios
        try:
            cursor = conn.execute("SELECT portfolio_id, name FROM portfolios ORDER BY portfolio_id")
            for row in cursor.fetchall():
                portfolio_id = row[0]
                tickers_set.add(f"PORTFOLIO_{portfolio_id}")
        except sqlite3.OperationalError:
            app.logger.info("Table 'portfolios' not found - portfolio feature not available.")

        # Add SI synthetic tickers
        try:
            cursor = conn.execute("SELECT DISTINCT ticker FROM short_interest")
            for row in cursor.fetchall():
                base = row[0]
                for suffix in SI_PATTERNS.keys():
                    tickers_set.add(f"{base}{suffix}")
        except sqlite3.OperationalError:
            app.logger.info("Table 'short_interest' not found - SI synthetic tickers not available.")

        conn.close()
        tickers = sorted(tickers_set)
        app.logger.info(f"Found {len(tickers)} tickers across stock, futures, bonds, and portfolio tables.")
        if not tickers:
            app.logger.warning("WARNING: Ticker list is empty. Check if table 'stock_prices_daily' exists and is populated.")
        return jsonify(sorted(tickers))
    except Exception as e:
        app.logger.error(f"An error occurred in get_tickers: {e}")
        return jsonify([]), 500

@app.route('/api/metadata')
def get_metadata():
    """Return a mapping of ticker -> display name for provided tickers.
    Priority: ticker_metadata.name → stock_metadata.name → futures_metadata → ticker itself.
    Special: ?tickers=ALL returns all available metadata.
    """
    tickers_str = request.args.get('tickers', '')

    # Handle special "ALL" case
    if tickers_str.strip().upper() == 'ALL':
        try:
            conn = get_db_connection()
            names = {}

            # Get all from ticker_metadata
            try:
                df = pd.read_sql("SELECT ticker, name FROM ticker_metadata WHERE name IS NOT NULL AND name != ''", conn)
                for _, row in df.iterrows():
                    names[row['ticker']] = row['name'].strip()
                app.logger.info(f"/api/metadata: ALL mode returned {len(names)} entries")
            except Exception as e:
                app.logger.warning(f"/api/metadata: ALL mode failed: {e}")

            conn.close()
            return jsonify(names)
        except Exception as e:
            app.logger.error(f"/api/metadata ALL error: {e}")
            return jsonify({}), 500

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    # Empty query → empty JSON
    if not tickers:
        return jsonify({})

    try:
        conn = get_db_connection()
        placeholders = ','.join(['?'] * len(tickers))
        names = {}

        # 1) Try unified ticker_metadata first (if present)
        try:
            q1 = f"SELECT ticker, name FROM ticker_metadata WHERE ticker IN ({placeholders})"
            df1 = pd.read_sql(q1, conn, params=tickers)
            for _, row in df1.iterrows():
                n = (row['name'] or '').strip()
                if n:
                    names[row['ticker']] = n
            app.logger.info(f"/api/metadata: ticker_metadata hits={len(names)}")
        except Exception as e:
            app.logger.warning(f"/api/metadata: ticker_metadata lookup skipped/failed: {e}")

        # 2) Fallback to legacy stock_metadata for any missing
        missing = [t for t in tickers if t not in names]
        if missing:
            try:
                ph = ','.join(['?'] * len(missing))
                q2 = f"SELECT ticker, name FROM stock_metadata WHERE ticker IN ({ph})"
                df2 = pd.read_sql(q2, conn, params=missing)
                add = 0
                for _, row in df2.iterrows():
                    n = (row['name'] or '').strip()
                    if n and row['ticker'] not in names:
                        names[row['ticker']] = n
                        add += 1
                app.logger.info(f"/api/metadata: stock_metadata hits={add}")
            except Exception as e:
                app.logger.warning(f"/api/metadata: stock_metadata lookup failed: {e}")

        # 3) Check for futures metadata for any remaining missing
        missing = [t for t in tickers if t not in names]
        if missing:
            # Futures metadata hardcoded from download_futures.py
            futures_metadata = {
                "ES=F": "S&P 500 E-Mini",
                "NQ=F": "Nasdaq-100 E-Mini", 
                "YM=F": "Dow Jones 30 E-Mini",
                "RTY=F": "Russell 2000 E-Mini",
                "CL=F": "WTI Crude Oil",
                "BZ=F": "Brent Crude Oil", 
                "NG=F": "Natural Gas",
                "RB=F": "RBOB Gasoline",
                "GC=F": "Gold",
                "SI=F": "Silver",
                "HG=F": "Copper", 
                "PL=F": "Platinum",
                "PA=F": "Palladium",
                "TIO=F": "Iron Ore 62%, CFR China (TSI)",
                "AL=F": "Aluminum",
                "ZI=F": "Zinc",
                "NI=F": "Nickel", 
                "HRN00": "HRC Steel (Hot-Rolled Coil) Futures",
                "HRC00": "HRC Steel (Hot-Rolled Coil) Futures",
                "HRE00": "HRC Steel (Hot-Rolled Coil) Futures",
                "DBB": "Invesco DB Base Metals Fund",
                "ZB=F": "30-Year Bond",
                "ZN=F": "10-Year Note", 
                "ZF=F": "5-Year Note",
                "ZT=F": "2-Year Note",
                "FGBL=F": "Euro-Bund (Germany 10Y)",
                "DX=F": "US Dollar Index Futures (ICE)",
                "ZC=F": "Corn",
                "ZS=F": "Soybeans",
                "ZW=F": "Wheat (Chicago)", 
                "KE=F": "Wheat (Kansas City)",
                "SB=F": "Sugar #11",
                "KC=F": "Coffee",
                "CC=F": "Cocoa",
                "CT=F": "Cotton",
                "OJ=F": "Orange Juice",
            }
            
            futures_hits = 0
            for ticker in missing:
                if ticker in futures_metadata:
                    names[ticker] = futures_metadata[ticker]
                    futures_hits += 1
            
            app.logger.info(f"/api/metadata: futures_metadata hits={futures_hits}")

        conn.close()

        # 4) Final mapping: fallback to ticker itself for any missing
        mapping = {t: names.get(t, t) for t in tickers}
        resolved = sum(1 for t in tickers if mapping[t] != t)
        app.logger.info(f"/api/metadata: requested={len(tickers)} resolved={resolved} missing={len(tickers)-resolved}")
        return jsonify(mapping)
    except Exception as e:
        app.logger.error(f"/api/metadata error: {e}")
        return jsonify({}), 500


@app.route('/api/ticker-aliases')
def get_ticker_aliases():
    """
    Return the ticker alias mapping.
    Used for fundamentals where share classes have identical financials.
    Response: { "GOOGL": "GOOG", "BRK-B": "BRK-A", ... }
    """
    return jsonify(TICKER_ALIASES)


@app.route('/api/data')
def get_data():
    """Provides raw historical price data for a list of tickers.

    Query params:
        tickers: comma-separated list of ticker symbols (required)
        interval: 'daily' (default), 'weekly', or 'monthly' (optional)
    """
    tickers_str = request.args.get('tickers')
    if not tickers_str:
        return jsonify({'error': 'At least one ticker is required'}), 400

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    interval = request.args.get('interval', 'daily').lower()
    start_date = request.args.get('start')
    end_date = request.args.get('end')

    # --- Handle SI synthetic tickers ---
    chart_data = {}
    regular_tickers = []

    for ticker in tickers:
        base_ticker, si_column = parse_si_ticker(ticker)
        if base_ticker:
            # This is an SI synthetic ticker
            si_data = get_si_timeseries(base_ticker, si_column, start_date, end_date)
            # Apply interval resampling if needed
            if si_data and interval in ('weekly', 'monthly'):
                df = pd.DataFrame(si_data)
                df['Date'] = pd.to_datetime(df['time'], unit='s')
                df = df.set_index('Date')
                if interval == 'weekly':
                    df = df.resample('W-FRI')['value'].last().dropna().reset_index()
                else:
                    df = df.resample('M')['value'].last().dropna().reset_index()
                df['time'] = (df['Date'].astype('int64') // 10**9).astype(int)
                si_data = df[['time', 'value']].to_dict(orient='records')
            chart_data[ticker] = si_data
        else:
            regular_tickers.append(ticker)

    # If no regular tickers, return SI data only
    if not regular_tickers:
        app.logger.info(f"/api/data: returned {len(chart_data)} SI tickers")
        return jsonify(chart_data)

    # Use DuckDB if enabled
    if USE_DUCKDB and DUCKDB_AVAILABLE:
        price_data = get_price_data(regular_tickers)

        # Apply interval resampling if needed
        if interval in ('weekly', 'monthly'):
            for ticker in price_data:
                if not price_data[ticker]:
                    continue
                # Convert to DataFrame for resampling
                df = pd.DataFrame(price_data[ticker])
                df['Date'] = pd.to_datetime(df['time'], unit='s')
                df = df.set_index('Date')

                if interval == 'weekly':
                    df = df.resample('W-FRI')['value'].last().dropna().reset_index()
                else:  # monthly
                    df = df.resample('M')['value'].last().dropna().reset_index()

                df['time'] = (df['Date'].astype('int64') // 10**9).astype(int)
                price_data[ticker] = df[['time', 'value']].to_dict(orient='records')

        # Merge SI data with price data
        chart_data.update(price_data)
        app.logger.info(f"[DuckDB] /api/data: returned {len(chart_data)} tickers")
        return jsonify(chart_data)

    # SQLite fallback
    conn = get_db_connection()

        # --- Determine which tickers belong to which table ---
    stock_cols, futures_cols, bond_cols, fred_cols = set(), set(), set(), set()
    try:
        cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
        stock_cols = {row['name'] for row in cursor.fetchall()}
    except sqlite3.OperationalError:
        pass
    try:
        cursor = conn.execute("PRAGMA table_info(futures_prices_daily)")
        futures_cols = {row['name'] for row in cursor.fetchall()}
    except sqlite3.OperationalError:
        pass
    try:
        cursor = conn.execute("PRAGMA table_info(bond_prices_daily)")
        bond_cols = {row['name'] for row in cursor.fetchall()}
    except sqlite3.OperationalError:
        pass
    try:
        cursor = conn.execute("PRAGMA table_info(fred_series)")
        fred_cols = {row['name'] for row in cursor.fetchall()}
    except sqlite3.OperationalError:
        pass

    # Assign each requested ticker to *exactly one* source table to prevent
    # duplicate column names that break pd.concat (InvalidIndexError).
    # Build chart_data per ticker to avoid column duplication issues entirely
    # (SI synthetic tickers already added to chart_data above)
    for ticker in regular_tickers:
        # Check futures table first for =F tickers (has more recent data)
        if ticker in futures_cols and ticker.endswith('=F'):
            table = 'futures_prices_daily'
        elif ticker in stock_cols:
            table = 'stock_prices_daily'
        elif ticker in futures_cols:
            table = 'futures_prices_daily'
        elif ticker in bond_cols:
            table = 'bond_prices_daily'
        elif ticker in fred_cols:
            table = 'fred_series'
        else:
            chart_data[ticker] = []
            continue

        q = (
            f'SELECT date(Date) AS Date, MAX("{ticker}") as value '
            f'FROM {table} '
            f'WHERE "{ticker}" IS NOT NULL '
            f'GROUP BY date(Date) '
            f'ORDER BY date(Date) ASC'
        )
        df = pd.read_sql_query(q, conn, parse_dates=['Date'])
        if df.empty:
            chart_data[ticker] = []
            continue
        # Coerce any invalid dates to NaT and drop rows with invalid date or value
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        before = len(df)
        df = df.dropna(subset=['Date', 'value'])
        # Coerce 'value' to numeric in case of mixed types from SQLite/pandas parsing
        try:
            df['value'] = pd.to_numeric(df['value'], errors='coerce')
        except Exception as e:
            app.logger.warning(f"/api/data: to_numeric failed for {ticker}: {e}")
        df = df.dropna(subset=['value'])
        dropped = before - len(df)
        if dropped:
            app.logger.warning(f"/api/data: dropped {dropped} invalid rows for {ticker} due to NaT/NaN")
        # Ensure sorted by date
        df = df.sort_values('Date')
        # Normalize to calendar day and collapse by median for each day (always)
        # This protects against mixed 'YYYY-MM-DD' vs 'YYYY-MM-DD 00:00:00' rows
        # and duplicated ingests for the same day.
        day = df['Date'].dt.normalize()
        before_rows = len(df)
        df = df.assign(Date=day).groupby('Date', as_index=False)['value'].median()
        after_rows = len(df)
        dropped_dup = before_rows - after_rows
        if dropped_dup:
            app.logger.warning(f"/api/data: collapsed duplicate day rows for {ticker}: {dropped_dup} rows dropped")
        # Apply interval aggregation if requested
        if interval == 'weekly':
            # Resample to week-end (Friday) closing prices
            df = df.set_index('Date')
            df = df.resample('W-FRI')['value'].last().dropna().reset_index()
            app.logger.info(f"/api/data: resampled {ticker} to weekly, rows={len(df)}")
        elif interval == 'monthly':
            # Resample to month-end closing prices
            df = df.set_index('Date')
            df = df.resample('M')['value'].last().dropna().reset_index()
            app.logger.info(f"/api/data: resampled {ticker} to monthly, rows={len(df)}")

        # Compute unix seconds; guard against negative epochs from NaT
        df['time'] = (df['Date'].astype('int64') // 10**9).astype(int)
        neg = int((df['time'] < 0).sum())
        if neg:
            app.logger.warning(f"/api/data: filtered {neg} rows with negative epoch for {ticker}")
        df = df[df['time'] >= 0]
        chart_data[ticker] = df[['time', 'value']].to_dict(orient='records')

    conn.close()

    return jsonify(chart_data)



# Diagnostic: return raw rows for a single ticker between dates using same SQL as /api/data
@app.route('/api/diag_series')
def diag_series():
    ticker = (request.args.get('ticker') or '^VXD').strip().upper()
    frm = (request.args.get('from') or '2021-07-09').strip()
    to = (request.args.get('to') or '2021-07-16').strip()

    conn = get_db_connection()
    try:
        # Detect table
        try:
            stock_cols = {row['name'] for row in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            stock_cols = set()
        try:
            fut_cols = {row['name'] for row in conn.execute("PRAGMA table_info(futures_prices_daily)").fetchall()}
        except sqlite3.OperationalError:
            fut_cols = set()

        # Check futures table first for =F tickers (has more recent data)
        if ticker in fut_cols and ticker.endswith('=F'):
            table = 'futures_prices_daily'
        elif ticker in stock_cols:
            table = 'stock_prices_daily'
        elif ticker in fut_cols:
            table = 'futures_prices_daily'
        else:
            return jsonify({'error': 'ticker not found in DB', 'db_path': DB_PATH}), 404

        q = f'SELECT Date, "{ticker}" as value FROM {table} WHERE "{ticker}" IS NOT NULL ORDER BY Date ASC'
        df = pd.read_sql_query(q, conn, parse_dates=['Date'])
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date'])
        mask = (df['Date'] >= pd.to_datetime(frm)) & (df['Date'] <= pd.to_datetime(to))
        sub = df.loc[mask].copy()
        # Return all rows as strings for Date
        sub['Date'] = sub['Date'].dt.strftime('%Y-%m-%d')
        return jsonify({
            'db_path': DB_PATH,
            'ticker': ticker,
            'table': table,
            'from': frm,
            'to': to,
            'rows': sub.to_dict(orient='records'),
            'row_count': int(len(sub))
        })
    finally:
        conn.close()


@app.route('/api/volume')
def get_volume():
    """Provides raw historical volume data for a list of tickers.
    Query params:
        tickers: comma-separated symbols (required)
    """
    tickers_str = request.args.get('tickers')
    if not tickers_str:
        return jsonify({'error': 'At least one ticker is required'}), 400

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]

    # Use DuckDB if enabled
    if USE_DUCKDB and DUCKDB_AVAILABLE:
        out = get_volume_data(tickers)
        app.logger.info(f"[DuckDB] /api/volume: returned {len(out)} tickers")
        return jsonify(out)

    # SQLite fallback
    conn = get_db_connection()

    # Determine which requested tickers are present in the stock and futures volume tables
    try:
        stock_cols = {row['name'] for row in conn.execute("PRAGMA table_info(stock_volumes_daily)").fetchall()}
    except sqlite3.OperationalError:
        stock_cols = set()
    try:
        fut_cols = {row['name'] for row in conn.execute("PRAGMA table_info(futures_volumes_daily)").fetchall()}
    except sqlite3.OperationalError:
        fut_cols = set()

    selected_stock = [t for t in tickers if t in stock_cols]
    selected_fut = [t for t in tickers if t in fut_cols]

    # Initialize default empty arrays for all requested tickers
    out = {t: [] for t in tickers}

    if selected_stock:
        safe_cols = '\", \"'.join(selected_stock)
        q = f'SELECT Date, "{safe_cols}" FROM stock_volumes_daily ORDER BY Date ASC'
        df = pd.read_sql_query(q, conn, parse_dates=['Date']).set_index('Date')
        # Convert index to unix seconds
        df['time'] = (df.index.astype('int64') // 10**9).astype(int)
        for t in selected_stock:
            tmp = df[['time', t]].copy()
            tmp.rename(columns={t: 'value'}, inplace=True)
            tmp['value'] = tmp['value'].replace({np.nan: None})
            out[t] = tmp.to_dict(orient='records')

    if selected_fut:
        safe_cols = '\", \"'.join(selected_fut)
        q = f'SELECT Date, "{safe_cols}" FROM futures_volumes_daily ORDER BY Date ASC'
        df = pd.read_sql_query(q, conn, parse_dates=['Date']).set_index('Date')
        df['time'] = (df.index.astype('int64') // 10**9).astype(int)
        for t in selected_fut:
            tmp = df[['time', t]].copy()
            tmp.rename(columns={t: 'value'}, inplace=True)
            tmp['value'] = tmp['value'].replace({np.nan: None})
            out[t] = tmp.to_dict(orient='records')

    conn.close()
    return jsonify(out)


def trigger_workspace_backup():
    """Trigger automatic workspace backup via backup_workspace.py script"""
    try:
        backup_script = Path(__file__).parent.parent / 'backup_workspace.py'
        if not backup_script.exists():
            app.logger.warning(f"Backup script not found at {backup_script}")
            return False

        result = subprocess.run(
            [sys.executable, str(backup_script), 'backup'],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            app.logger.info(f"Automatic backup completed: {result.stdout.strip()}")
            return True
        else:
            app.logger.warning(f"Backup script returned error: {result.stderr.strip()}")
            return False
    except subprocess.TimeoutExpired:
        app.logger.error("Backup script timed out")
        return False
    except Exception as e:
        app.logger.error(f"Failed to trigger backup: {e}")
        return False


# --- Workspace Persistence API ---
@app.route('/api/workspace', methods=['GET', 'POST'])
def workspace():
    """Persist or retrieve the multi-chart workspace layout.
    The workspace is stored as JSON in a file so it survives server restarts
    and is shared across browser origins/ports.
    """
    workspace_path = os.path.join(basedir, WORKSPACE_FILENAME)

    if request.method == 'POST':
        try:
            state = request.get_json(force=True) or []
            # Determine schema and counts
            if isinstance(state, dict) and 'cards' in state:
                items = len(state.get('cards') or [])
                schema = 'object'
            else:
                # Legacy: array of cards
                items = len(state) if isinstance(state, list) else 0
                schema = 'array'
            app.logger.info(f"/api/workspace POST schema={schema} items={items}")

            # Write atomically by first dumping to a temp file
            temp_file = WORKSPACE_FILENAME + WORKSPACE_TEMP_SUFFIX
            with open(temp_file, 'w', encoding='utf-8') as fh:
                json.dump(state, fh)
            os.replace(temp_file, workspace_path)

            # Trigger automatic backup after successful save
            trigger_workspace_backup()

            return jsonify({'status': 'saved', 'items': items, 'schema': schema}), 200
        except Exception as e:
            app.logger.error(f"Failed to save workspace: {e}")
            return jsonify({'error': 'failed to save'}), 500

    # GET
    if os.path.exists(workspace_path):
        try:
            with open(workspace_path, 'r', encoding='utf-8') as fh:
                state = json.load(fh)
        except Exception as e:
            app.logger.error(f"Failed to read workspace file: {e}")
            state = []
    else:
        state = []
    return jsonify(state)


# --- Lightweight commentary endpoint ---
@app.route('/api/commentary')
def commentary():
    """Return rule-based text summary for each requested ticker.
    Query params:
        tickers: comma-separated symbols
        from, to: unix seconds (optional)
    """
    tickers_param = request.args.get('tickers', '')
    if not tickers_param:
        return jsonify({}), 400

    tickers = [t.strip().upper() for t in tickers_param.split(',') if t.strip()]
    try:
        t_from = int(request.args.get('from', 0))
    except ValueError:
        t_from = 0
    try:
        t_to = int(request.args.get('to', 10**12))
    except ValueError:
        t_to = 10**12

    conn = get_db_connection()
    safe_cols = '"' + '", "'.join(tickers) + '"'
    query = f'SELECT Date, {safe_cols} FROM stock_prices_daily ORDER BY Date ASC'
    df = pd.read_sql_query(query, conn, parse_dates=['Date'])
    conn.close()

    # Limit range
    ts = (df['Date'].astype('int64') // 10**9)
    df = df[(ts >= t_from) & (ts <= t_to)].set_index('Date')

    out = {}
    for t in tickers:
        series = df[t].dropna()
        if series.empty:
            out[t] = 'No data for selected period.'
            continue
        start, end = series.iloc[[0, -1]]
        pct = (end / start - 1) * 100
        peak_date = series.idxmax().date()
        trough_date = series.idxmin().date()
        direction = 'rose' if pct > 0 else 'fell'
        out[t] = (f'From {series.index[0].date()} to {series.index[-1].date()}, '
                  f'{t} {direction} {pct:+.1f} %. Peak on {peak_date}, low on {trough_date}.')
    return jsonify(out)


# --- ETF series endpoint (Option A) ---
@app.route('/api/etf/series')
def etf_series():
    """Return derived ETF series like portfolio value and shares outstanding.
    Query params:
        etf: e.g., 'ALLW' (required)
        metrics: comma-separated subset of ['value','shares'] (default 'value,shares')
        from: ISO date YYYY-MM-DD (optional)
        to: ISO date YYYY-MM-DD (optional)
    Response JSON keys present only for requested metrics.
    Each series is a list of {time: <unix_sec>, value: <number>}.
    """
    try:
        etf = (request.args.get('etf', '') or '').strip().upper()
        if not etf:
            return jsonify({'error': 'etf is required'}), 400

        metrics_param = request.args.get('metrics', 'value,shares')
        allowed = {'value', 'shares'}
        metrics = {m.strip().lower() for m in metrics_param.split(',') if m.strip().lower() in allowed}
        if not metrics:
            metrics = {'value'}

        from_str = request.args.get('from')
        to_str = request.args.get('to')

        conn = get_db_connection()

        # Aggregate portfolio value by snapshot_date
        q_hold = (
            "SELECT snapshot_date as Date, SUM(market_value) as total_value "
            "FROM etf_holdings_daily "
            "WHERE etf = ? "
            "GROUP BY snapshot_date "
            "ORDER BY snapshot_date ASC"
        )
        df_hold = pd.read_sql_query(q_hold, conn, params=[etf], parse_dates=['Date'])

        # Filter by date range if provided
        if not df_hold.empty and (from_str or to_str):
            if from_str:
                try:
                    start_ts = pd.to_datetime(from_str)
                    df_hold = df_hold[df_hold['Date'] >= start_ts]
                except Exception:
                    pass
            if to_str:
                try:
                    end_ts = pd.to_datetime(to_str)
                    df_hold = df_hold[df_hold['Date'] <= end_ts]
                except Exception:
                    pass

        result = {}

        # Metric: portfolio value over time
        if 'value' in metrics:
            if df_hold.empty:
                result['value'] = []
            else:
                tmp = df_hold.copy()
                tmp['time'] = (tmp['Date'].astype('int64') // 10**9).astype(int)
                result['value'] = (
                    tmp[['time', 'total_value']]
                    .rename(columns={'total_value': 'value'})
                    .to_dict(orient='records')
                )

        # Metric: shares outstanding = total_value / price
        if 'shares' in metrics:
            shares_series = []
            if not df_hold.empty:
                # Check price column exists for ETF
                try:
                    cols = {row['name'] for row in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall()}
                except sqlite3.OperationalError:
                    cols = set()
                app.logger.info(f"/api/etf/series shares: df_hold rows={len(df_hold)}; price_col_exists={etf in cols}")
                if etf in cols:
                    q_price = f'SELECT Date, "{etf}" as price FROM stock_prices_daily ORDER BY Date ASC'
                    df_price = pd.read_sql_query(q_price, conn, parse_dates=['Date'])
                    app.logger.info(f"/api/etf/series shares: df_price rows={len(df_price)}")
                    if not df_price.empty:
                        if from_str or to_str:
                            if from_str:
                                try:
                                    start_ts = pd.to_datetime(from_str)
                                    df_price = df_price[df_price['Date'] >= start_ts]
                                except Exception:
                                    pass
                            if to_str:
                                try:
                                    end_ts = pd.to_datetime(to_str)
                                    df_price = df_price[df_price['Date'] <= end_ts]
                                except Exception:
                                    pass
                        # Use asof merge to tolerate non-trading-day snapshots; align to previous available price (up to 5 days back)
                        df_hold_sorted = df_hold[['Date', 'total_value']].sort_values('Date')
                        df_price_sorted = df_price[['Date', 'price']].sort_values('Date')
                        try:
                            df_m = pd.merge_asof(
                                df_hold_sorted,
                                df_price_sorted,
                                on='Date',
                                direction='backward',
                                tolerance=pd.Timedelta('5D')
                            )
                        except Exception as me:
                            app.logger.warning(f"/api/etf/series shares: merge_asof failed ({me}); falling back to inner merge")
                            df_m = pd.merge(df_hold_sorted, df_price_sorted, on='Date', how='inner')
                        df_m = df_m[df_m['price'].notna()]
                        app.logger.info(f"/api/etf/series shares: merged rows={len(df_m)}")
                        if not df_m.empty:
                            df_m['shares'] = df_m['total_value'] / df_m['price']
                            df_m['time'] = (df_m['Date'].astype('int64') // 10**9).astype(int)
                            shares_series = (
                                df_m[['time', 'shares']]
                                .rename(columns={'shares': 'value'})
                                .to_dict(orient='records')
                            )
                            app.logger.info(f"/api/etf/series shares: output points={len(shares_series)}")
            result['shares'] = shares_series

        conn.close()
        return jsonify(result)
    except Exception as e:
        app.logger.error(f"/api/etf/series error: {e}")
        return jsonify({'error': 'failed to compute series'}), 500

@app.route('/api/revenue')
def api_revenue():
    """
    Fetch quarterly revenue data for requested tickers.
    Query params: ?tickers=AAPL,MSFT,TSLA
    Returns: { "AAPL": [{time: unix_ts, value: revenue}, ...], "MSFT": [...], ... }

    DB-first: queries income_statement_quarterly.total_revenue.
    Falls back to Alpha Vantage (if API key available), then yfinance if DB is empty.
    """
    import yfinance as yf
    from datetime import datetime
    import os

    ticker_param = request.args.get('tickers', '')
    if not ticker_param:
        return jsonify({'error': 'No tickers provided'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in ticker_param.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG for fundamentals)
    # Keep mapping to return data under original requested ticker
    alias_map = {}  # original -> canonical
    canonical_tickers = []
    for t in tickers:
        canonical = resolve_ticker_alias(t)
        if canonical != t:
            alias_map[t] = canonical
            app.logger.info(f"/api/revenue: aliased {t} -> {canonical}")
        canonical_tickers.append(canonical)

    # Dedupe canonical tickers (e.g., if user requests both GOOG and GOOGL)
    unique_canonical = list(dict.fromkeys(canonical_tickers))

    app.logger.info(f"/api/revenue: requested tickers={tickers}, canonical={unique_canonical}")

    # Check for Alpha Vantage API key (accept both env var names, prefer ALPHA_VANTAGE_API_KEY)
    alpha_vantage_key = os.environ.get('ALPHA_VANTAGE_API_KEY') or os.environ.get('ALPHAVANTAGE_API_KEY')
    use_alpha_vantage = alpha_vantage_key is not None

    result = {}

    def fetch_all_from_db(symbols):
        """Batch fetch quarterly revenue from local database for all tickers at once"""
        db_results = {s: None for s in symbols}
        try:
            conn = get_db_connection()
            placeholders = ','.join('?' * len(symbols))
            query = f"""
                SELECT ticker, fiscal_date_ending, total_revenue
                FROM income_statement_quarterly
                WHERE ticker IN ({placeholders})
                ORDER BY ticker, fiscal_date_ending ASC
            """
            df = pd.read_sql(query, conn, params=symbols)
            conn.close()

            if df.empty:
                return db_results

            # Group by ticker
            for ticker in symbols:
                ticker_df = df[df['ticker'] == ticker]
                if ticker_df.empty:
                    continue

                data_points = []
                for _, row in ticker_df.iterrows():
                    try:
                        date = pd.to_datetime(row['fiscal_date_ending'])
                        unix_ts = int(date.timestamp())
                        value = row['total_revenue']
                        if pd.notna(value) and value != 0:
                            data_points.append({'time': unix_ts, 'value': float(value)})
                    except Exception as e:
                        app.logger.warning(f"/api/revenue: Error parsing DB row for {ticker}: {e}")
                        continue

                if data_points:
                    db_results[ticker] = data_points
                    app.logger.info(f"/api/revenue: {ticker} returned {len(data_points)} quarters from DB")

            return db_results

        except Exception as e:
            app.logger.error(f"/api/revenue: DB batch error: {e}")
            return db_results

    # Lazy-initialize Alpha Vantage client (reuses hardened client with proper rate limiting)
    av_client = None
    if use_alpha_vantage:
        try:
            from alpha_vantage_fetcher import AlphaVantageClient
            av_client = AlphaVantageClient(api_key=alpha_vantage_key)
        except Exception as e:
            app.logger.warning(f"/api/revenue: Could not initialize AlphaVantageClient: {e}")

    def fetch_from_alpha_vantage(symbol):
        """Fetch quarterly revenue from Alpha Vantage using hardened client (12s rate limit + retry)"""
        if not av_client:
            return None

        try:
            # Use the hardened client which handles rate limiting and retries
            data = av_client.get_income_statement(symbol)

            if not data:
                app.logger.warning(f"/api/revenue: No data from Alpha Vantage for {symbol}")
                return None

            quarterly_reports = data.get('quarterlyReports', [])
            if not quarterly_reports:
                app.logger.warning(f"/api/revenue: No quarterly reports from Alpha Vantage for {symbol}")
                return None

            data_points = []
            for report in quarterly_reports:
                try:
                    fiscal_date = report.get('fiscalDateEnding')  # YYYY-MM-DD string
                    total_revenue = report.get('totalRevenue')

                    if not fiscal_date or not total_revenue:
                        continue

                    # Parse date string (YYYY-MM-DD)
                    date_obj = datetime.strptime(fiscal_date, '%Y-%m-%d')
                    unix_ts = int(date_obj.timestamp())
                    revenue_val = float(total_revenue)

                    # Include original date string for DB persistence (avoids timezone edge cases)
                    data_points.append({'time': unix_ts, 'value': revenue_val, 'date': fiscal_date})
                except (ValueError, TypeError) as e:
                    app.logger.warning(f"/api/revenue: Error parsing Alpha Vantage data for {symbol}: {e}")
                    continue

            # Sort by time (oldest first)
            data_points.sort(key=lambda x: x['time'])
            app.logger.info(f"/api/revenue: {symbol} returned {len(data_points)} quarters from Alpha Vantage")
            return data_points

        except Exception as e:
            app.logger.error(f"/api/revenue: Alpha Vantage error for {symbol}: {e}")
            return None

    def fetch_from_yfinance(symbol):
        """Fetch quarterly revenue from yfinance (last 5 quarters only)"""
        try:
            ticker = yf.Ticker(symbol)
            quarterly = ticker.quarterly_financials

            if quarterly is None or quarterly.empty:
                app.logger.warning(f"/api/revenue: No financials from yfinance for {symbol}")
                return []

            if 'Total Revenue' not in quarterly.index:
                app.logger.warning(f"/api/revenue: No Total Revenue from yfinance for {symbol}")
                return []

            revenue_series = quarterly.loc['Total Revenue']

            # Convert to list of {time, value} dicts
            data_points = []
            for date, value in revenue_series.items():
                try:
                    # Convert pandas timestamp to unix timestamp
                    unix_ts = int(date.timestamp())
                    # Extract date string (YYYY-MM-DD) for DB persistence
                    date_str = date.strftime('%Y-%m-%d')
                    # Convert value to float, handle None/NaN
                    revenue_val = float(value) if pd.notna(value) else None
                    if revenue_val is not None:
                        data_points.append({'time': unix_ts, 'value': revenue_val, 'date': date_str})
                except Exception as e:
                    app.logger.warning(f"/api/revenue: Error processing yfinance data for {symbol}: {e}")
                    continue

            # Sort by time (oldest first)
            data_points.sort(key=lambda x: x['time'])
            app.logger.info(f"/api/revenue: {symbol} returned {len(data_points)} quarters from yfinance")
            return data_points

        except Exception as e:
            app.logger.error(f"/api/revenue: yfinance error for {symbol}: {e}")
            return []

    # Batch fetch from DB first (single query for canonical tickers)
    db_data = fetch_all_from_db(unique_canonical)

    # Identify which canonical tickers need external API fallback
    missing_canonical = [t for t in unique_canonical if db_data.get(t) is None]

    if missing_canonical:
        app.logger.info(f"/api/revenue: DB hits={len(unique_canonical) - len(missing_canonical)}, misses={len(missing_canonical)}: {missing_canonical}")
    else:
        app.logger.info(f"/api/revenue: All {len(unique_canonical)} canonical tickers found in DB")

    def persist_revenue_to_db(symbol, data_points):
        """Persist fetched revenue data to income_statement_quarterly for future DB hits"""
        if not data_points:
            return
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            inserted = 0
            for point in data_points:
                try:
                    # Use original date string if available (avoids timezone edge cases)
                    # Fall back to UTC conversion from timestamp if not present
                    fiscal_date = point.get('date') or datetime.utcfromtimestamp(point['time']).strftime('%Y-%m-%d')
                    # INSERT OR IGNORE to avoid duplicates (UNIQUE constraint on ticker, fiscal_date_ending)
                    cursor.execute('''
                        INSERT OR IGNORE INTO income_statement_quarterly
                        (ticker, fiscal_date_ending, total_revenue)
                        VALUES (?, ?, ?)
                    ''', (symbol, fiscal_date, point['value']))
                    if cursor.rowcount > 0:
                        inserted += 1
                except Exception as e:
                    app.logger.warning(f"/api/revenue: Error persisting row for {symbol}: {e}")
            conn.commit()
            conn.close()
            if inserted > 0:
                app.logger.info(f"/api/revenue: Persisted {inserted} new quarters for {symbol} to DB")
        except Exception as e:
            app.logger.error(f"/api/revenue: Error persisting {symbol} to DB: {e}")

    # Fallback to external APIs only for missing canonical tickers
    for symbol in missing_canonical:
        data = None

        # Try Alpha Vantage if client available (handles its own 12s rate limiting)
        if av_client:
            data = fetch_from_alpha_vantage(symbol)

        # Fall back to yfinance if still no data
        if data is None or len(data) == 0:
            app.logger.info(f"/api/revenue: Falling back to yfinance for {symbol}")
            data = fetch_from_yfinance(symbol)

        # Persist successful fetches to DB for future cache hits
        if data and len(data) > 0:
            persist_revenue_to_db(symbol, data)

        db_data[symbol] = data if data else []

    # Build final result (strip internal 'date' field, return only {time, value})
    # Map canonical data back to original requested tickers
    for i, original_ticker in enumerate(tickers):
        canonical = canonical_tickers[i]
        raw_data = db_data.get(canonical) or []
        result[original_ticker] = [{'time': p['time'], 'value': p['value']} for p in raw_data]

    return jsonify(result)


@app.route('/api/fundamentals/overview')
def get_fundamental_overview():
    """
    Get company overview / fundamental metrics for one or more tickers.
    Query params: ?tickers=AAPL,MSFT,TSLA
    Returns: {AAPL: {...}, MSFT: {...}, ...}
    """
    tickers_str = request.args.get('tickers', '')
    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    conn = get_db_connection()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            app.logger.info(f"/api/fundamentals/overview: aliased {ticker} -> {db_ticker}")

        try:
            query = "SELECT * FROM company_overview WHERE ticker = ?"
            df = pd.read_sql(query, conn, params=(db_ticker,))

            if df.empty:
                app.logger.warning(f"/api/fundamentals/overview: No data for {db_ticker}")
                result[ticker] = None
            else:
                # Convert to dict, excluding last_updated
                data = df.iloc[0].to_dict()
                if 'last_updated' in data:
                    del data['last_updated']
                result[ticker] = data

        except Exception as e:
            app.logger.error(f"/api/fundamentals/overview: Error for {db_ticker}: {e}")
            result[ticker] = None

    conn.close()
    return jsonify(result)


@app.route('/api/fundamentals/earnings')
def get_fundamental_earnings():
    """
    Get quarterly earnings data for one or more tickers.
    Query params: ?tickers=AAPL,MSFT&period=quarterly (or annual)
    Returns: {AAPL: [{fiscalDateEnding, reportedEPS, estimatedEPS, ...}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    period = request.args.get('period', 'quarterly').lower()

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    if period not in ['quarterly', 'annual']:
        return jsonify({'error': 'Period must be quarterly or annual'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    table_name = f'earnings_{period}'
    conn = get_db_connection()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            app.logger.info(f"/api/fundamentals/earnings: aliased {ticker} -> {db_ticker}")

        try:
            query = f"SELECT * FROM {table_name} WHERE ticker = ? ORDER BY fiscal_date_ending DESC"
            df = pd.read_sql(query, conn, params=(db_ticker,))

            if df.empty:
                app.logger.warning(f"/api/fundamentals/earnings: No {period} data for {db_ticker}")
                result[ticker] = []
            else:
                # Convert to list of dicts
                data = df.to_dict('records')
                # Remove id and last_updated fields
                for row in data:
                    row.pop('id', None)
                    row.pop('last_updated', None)
                result[ticker] = data

        except Exception as e:
            app.logger.error(f"/api/fundamentals/earnings: Error for {db_ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@app.route('/api/fundamentals/income')
def get_fundamental_income():
    """
    Get income statement data for one or more tickers.
    Query params: ?tickers=AAPL,MSFT&period=quarterly (or annual)
    Returns: {AAPL: [{fiscalDateEnding, totalRevenue, netIncome, ...}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    period = request.args.get('period', 'quarterly').lower()

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    if period not in ['quarterly', 'annual']:
        return jsonify({'error': 'Period must be quarterly or annual'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    table_name = f'income_statement_{period}'
    conn = get_db_connection()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            app.logger.info(f"/api/fundamentals/income: aliased {ticker} -> {db_ticker}")

        try:
            query = f"SELECT * FROM {table_name} WHERE ticker = ? ORDER BY fiscal_date_ending DESC"
            df = pd.read_sql(query, conn, params=(db_ticker,))

            if df.empty:
                app.logger.warning(f"/api/fundamentals/income: No {period} data for {db_ticker}")
                result[ticker] = []
            else:
                data = df.to_dict('records')
                for row in data:
                    row.pop('id', None)
                    row.pop('last_updated', None)
                result[ticker] = data

        except Exception as e:
            app.logger.error(f"/api/fundamentals/income: Error for {db_ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@app.route('/api/fundamentals/balance')
def get_fundamental_balance():
    """
    Get balance sheet data for one or more tickers.
    Query params: ?tickers=AAPL,MSFT&period=quarterly (or annual)
    Returns: {AAPL: [{fiscalDateEnding, totalAssets, totalLiabilities, ...}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    period = request.args.get('period', 'quarterly').lower()

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    if period not in ['quarterly', 'annual']:
        return jsonify({'error': 'Period must be quarterly or annual'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    table_name = f'balance_sheet_{period}'
    conn = get_db_connection()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            app.logger.info(f"/api/fundamentals/balance: aliased {ticker} -> {db_ticker}")
        try:
            query = f"SELECT * FROM {table_name} WHERE ticker = ? ORDER BY fiscal_date_ending DESC"
            df = pd.read_sql(query, conn, params=(db_ticker,))

            if df.empty:
                app.logger.warning(f"/api/fundamentals/balance: No {period} data for {db_ticker}")
                result[ticker] = []
            else:
                data = df.to_dict('records')
                for row in data:
                    row.pop('id', None)
                    row.pop('last_updated', None)
                result[ticker] = data

        except Exception as e:
            app.logger.error(f"/api/fundamentals/balance: Error for {db_ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@app.route('/api/fundamentals/cashflow')
def get_fundamental_cashflow():
    """
    Get cash flow data for one or more tickers.
    Query params: ?tickers=AAPL,MSFT&period=quarterly (or annual)
    Returns: {AAPL: [{fiscalDateEnding, operatingCashflow, freeCashFlow, ...}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    period = request.args.get('period', 'quarterly').lower()

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    if period not in ['quarterly', 'annual']:
        return jsonify({'error': 'Period must be quarterly or annual'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    table_name = f'cash_flow_{period}'
    conn = get_db_connection()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            app.logger.info(f"/api/fundamentals/cashflow: aliased {ticker} -> {db_ticker}")
        try:
            query = f"SELECT * FROM {table_name} WHERE ticker = ? ORDER BY fiscal_date_ending DESC"
            df = pd.read_sql(query, conn, params=(db_ticker,))

            if df.empty:
                app.logger.warning(f"/api/fundamentals/cashflow: No {period} data for {db_ticker}")
                result[ticker] = []
            else:
                data = df.to_dict('records')
                for row in data:
                    row.pop('id', None)
                    row.pop('last_updated', None)
                result[ticker] = data

        except Exception as e:
            app.logger.error(f"/api/fundamentals/cashflow: Error for {db_ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@app.route('/api/fundamentals/chart')
def get_fundamentals_chart_data():
    """
    Get fundamental metrics formatted for charting (quarterly time series).
    Query params: ?tickers=AAPL,MSFT&metrics=revenue,netIncome,eps,fcf
    Returns: {AAPL: {revenue: [{time, value}, ...], netIncome: [...], ...}, ...}
    """
    tickers_str = request.args.get('tickers', '')
    metrics_str = request.args.get('metrics', 'revenue,netIncome,eps,fcf')

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    metrics = [m.strip().lower() for m in metrics_str.split(',') if m.strip()]

    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases (e.g., GOOGL -> GOOG)
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    conn = get_db_connection()
    result = {}

    # Metric mapping: metric_name -> (table, column, label)
    metric_map = {
        'revenue': ('income_statement_quarterly', 'total_revenue', 'Revenue'),
        'netincome': ('income_statement_quarterly', 'net_income', 'Net Income'),
        'eps': ('earnings_quarterly', 'reported_eps', 'EPS'),
        'fcf': ('cash_flow_quarterly', 'free_cash_flow', 'Free Cash Flow'),
        'operatingincome': ('income_statement_quarterly', 'operating_income', 'Operating Income'),
        'ebitda': ('income_statement_quarterly', 'ebitda', 'EBITDA'),
        'grossprofit': ('income_statement_quarterly', 'gross_profit', 'Gross Profit'),
        'operatingcashflow': ('cash_flow_quarterly', 'operating_cashflow', 'Operating Cash Flow'),
        'capex': ('cash_flow_quarterly', 'capital_expenditures', 'Capital Expenditures')
    }

    for ticker in tickers:
        # Use canonical ticker for DB query
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            app.logger.info(f"/api/fundamentals/chart: aliased {ticker} -> {db_ticker}")
        ticker_data = {}

        for metric in metrics:
            if metric not in metric_map:
                app.logger.warning(f"/api/fundamentals/chart: Unknown metric '{metric}'")
                continue

            table, column, label = metric_map[metric]

            try:
                query = f"""
                    SELECT fiscal_date_ending, {column}
                    FROM {table}
                    WHERE ticker = ?
                    ORDER BY fiscal_date_ending ASC
                """
                df = pd.read_sql(query, conn, params=(db_ticker,))

                if df.empty:
                    ticker_data[metric] = []
                else:
                    # Convert to chart format: [{time: unix_timestamp, value: number}, ...]
                    data_points = []
                    for _, row in df.iterrows():
                        try:
                            # Parse date and convert to unix timestamp
                            date = pd.to_datetime(row['fiscal_date_ending'])
                            unix_ts = int(date.timestamp())

                            value = row[column]
                            if pd.notna(value) and value != 0:
                                data_points.append({
                                    'time': unix_ts,
                                    'value': float(value)
                                })
                        except Exception as e:
                            app.logger.warning(f"/api/fundamentals/chart: Error parsing row for {ticker} {metric}: {e}")
                            continue

                    ticker_data[metric] = data_points
                    app.logger.info(f"/api/fundamentals/chart: {ticker} {metric} returned {len(data_points)} quarters")

            except Exception as e:
                app.logger.error(f"/api/fundamentals/chart: Error for {ticker} {metric}: {e}")
                ticker_data[metric] = []

        result[ticker] = ticker_data

    conn.close()
    return jsonify(result)


# --- Short Interest Endpoints ---

@app.route('/api/short-interest')
def get_short_interest():
    """
    Get short interest data for one or more tickers.
    Query params: ?tickers=AAPL,MSFT&limit=10
    Returns: {AAPL: [{settlement_date, short_percent_float, days_to_cover, ...}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    limit = request.args.get('limit', '10')

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    try:
        limit = int(limit)
    except ValueError:
        return jsonify({'error': 'Invalid limit parameter'}), HTTP_BAD_REQUEST

    # Resolve ticker aliases
    canonical_map = {t: resolve_ticker_alias(t) for t in tickers}

    conn = get_db_connection()
    cursor = conn.cursor()
    result = {}

    for ticker in tickers:
        db_ticker = canonical_map[ticker]
        if db_ticker != ticker:
            app.logger.info(f"/api/short-interest: aliased {ticker} -> {db_ticker}")

        try:
            cursor.execute('''
                SELECT settlement_date, short_interest, shares_outstanding,
                       short_percent_float, short_percent_outstanding,
                       days_to_cover, avg_daily_volume, source
                FROM short_interest
                WHERE ticker = ?
                ORDER BY settlement_date DESC
                LIMIT ?
            ''', (db_ticker, limit))

            rows = cursor.fetchall()
            data_points = []

            for row in rows:
                data_points.append({
                    'settlementDate': row[0],
                    'shortInterest': row[1],
                    'sharesOutstanding': row[2],
                    'shortPercentFloat': row[3],
                    'shortPercentOutstanding': row[4],
                    'daysToCover': row[5],
                    'avgDailyVolume': row[6],
                    'source': row[7]
                })

            # Reverse to chronological order for charting
            data_points.reverse()
            result[ticker] = data_points

        except Exception as e:
            app.logger.error(f"/api/short-interest: Error for {db_ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@app.route('/api/short-interest/latest')
def get_short_interest_latest():
    """
    Get latest short interest data for multiple tickers (for dashboard/overview).
    Query params: ?tickers=AAPL,MSFT or no params for all
    Returns: [{ticker, settlementDate, shortPercentFloat, daysToCover, ...}, ...]
    """
    tickers_str = request.args.get('tickers', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    if tickers_str:
        tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
        placeholders = ','.join('?' * len(tickers))
        query = f'''
            SELECT si.ticker, si.settlement_date, si.short_interest,
                   si.shares_outstanding, si.short_percent_float,
                   si.short_percent_outstanding, si.days_to_cover,
                   si.avg_daily_volume, si.source
            FROM short_interest si
            INNER JOIN (
                SELECT ticker, MAX(settlement_date) as max_date
                FROM short_interest
                WHERE ticker IN ({placeholders})
                GROUP BY ticker
            ) latest ON si.ticker = latest.ticker AND si.settlement_date = latest.max_date
            ORDER BY si.short_percent_float DESC
        '''
        cursor.execute(query, tickers)
    else:
        # Get all tickers with SI data
        cursor.execute('''
            SELECT si.ticker, si.settlement_date, si.short_interest,
                   si.shares_outstanding, si.short_percent_float,
                   si.short_percent_outstanding, si.days_to_cover,
                   si.avg_daily_volume, si.source
            FROM short_interest si
            INNER JOIN (
                SELECT ticker, MAX(settlement_date) as max_date
                FROM short_interest
                GROUP BY ticker
            ) latest ON si.ticker = latest.ticker AND si.settlement_date = latest.max_date
            ORDER BY si.short_percent_float DESC
        ''')

    rows = cursor.fetchall()
    result = []

    for row in rows:
        result.append({
            'ticker': row[0],
            'settlementDate': row[1],
            'shortInterest': row[2],
            'sharesOutstanding': row[3],
            'shortPercentFloat': row[4],
            'shortPercentOutstanding': row[5],
            'daysToCover': row[6],
            'avgDailyVolume': row[7],
            'source': row[8]
        })

    conn.close()
    return jsonify(result)


@app.route('/api/iv/stock')
def get_stock_implied_volatility():
    """
    Get implied volatility data for stocks.
    Query params: ?tickers=AAPL,MSFT&days=30
    Returns: {AAPL: [{date, call_iv, put_iv, average_iv, current_price}, ...], ...}
    """
    tickers_str = request.args.get('tickers', '')
    days = request.args.get('days', '30')

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]

    try:
        days = int(days)
    except ValueError:
        return jsonify({'error': 'Invalid days parameter'}), HTTP_BAD_REQUEST

    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    conn = get_db_connection()
    cursor = conn.cursor()
    result = {}

    from datetime import datetime, timedelta
    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

    for ticker in tickers:
        try:
            cursor.execute('''
                SELECT date, call_iv, put_iv, average_iv, current_price, expiration
                FROM implied_volatility_daily
                WHERE ticker = ? AND date >= ?
                ORDER BY date ASC
            ''', (ticker, start_date))

            rows = cursor.fetchall()
            data_points = []

            for row in rows:
                # Convert date to unix timestamp for charting
                date_obj = datetime.strptime(row[0], '%Y-%m-%d')
                timestamp = int(date_obj.timestamp())

                data_points.append({
                    'time': timestamp,
                    'date': row[0],
                    'call_iv': row[1],
                    'put_iv': row[2],
                    'average_iv': row[3],
                    'current_price': row[4],
                    'expiration': row[5]
                })

            result[ticker] = data_points
            app.logger.info(f"/api/iv/stock: {ticker} returned {len(data_points)} data points")

        except Exception as e:
            app.logger.error(f"/api/iv/stock: Error for {ticker}: {e}")
            result[ticker] = []

    conn.close()
    return jsonify(result)


@app.route('/api/iv/cboe')
def get_cboe_indices():
    """
    Get CBOE volatility indices (VIX, VXN, VXD).
    Query params: ?symbols=^VIX,^VXN&days=30
    Returns: {^VIX: [{date, value}, ...], ^VXN: [{date, value}, ...], ...}
    """
    symbols_str = request.args.get('symbols', '^VIX,^VXN,^VXD')
    days = request.args.get('days', '30')

    symbols = [s.strip() for s in symbols_str.split(',') if s.strip()]

    try:
        days = int(days)
    except ValueError:
        return jsonify({'error': 'Invalid days parameter'}), HTTP_BAD_REQUEST

    if not symbols:
        return jsonify({'error': 'No valid symbols provided'}), HTTP_BAD_REQUEST

    conn = get_db_connection()
    cursor = conn.cursor()
    result = {}

    from datetime import datetime, timedelta
    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

    for symbol in symbols:
        try:
            cursor.execute('''
                SELECT date, value, description
                FROM cboe_indices_daily
                WHERE symbol = ? AND date >= ?
                ORDER BY date ASC
            ''', (symbol, start_date))

            rows = cursor.fetchall()
            data_points = []

            for row in rows:
                # Convert date to unix timestamp for charting
                date_obj = datetime.strptime(row[0], '%Y-%m-%d')
                timestamp = int(date_obj.timestamp())

                data_points.append({
                    'time': timestamp,
                    'date': row[0],
                    'value': row[1],
                    'description': row[2]
                })

            result[symbol] = data_points
            app.logger.info(f"/api/iv/cboe: {symbol} returned {len(data_points)} data points")

        except Exception as e:
            app.logger.error(f"/api/iv/cboe: Error for {symbol}: {e}")
            result[symbol] = []

    conn.close()
    return jsonify(result)


@app.route('/api/iv/latest')
def get_latest_iv():
    """
    Get latest implied volatility values for tickers.
    Query params: ?tickers=AAPL,MSFT
    Returns: {AAPL: {date, call_iv, put_iv, average_iv, current_price}, ...}
    """
    tickers_str = request.args.get('tickers', '')

    if not tickers_str:
        return jsonify({'error': 'Missing tickers parameter'}), HTTP_BAD_REQUEST

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]

    if not tickers:
        return jsonify({'error': 'No valid tickers provided'}), HTTP_BAD_REQUEST

    conn = get_db_connection()
    cursor = conn.cursor()
    result = {}

    for ticker in tickers:
        try:
            cursor.execute('''
                SELECT date, call_iv, put_iv, average_iv, current_price, expiration
                FROM implied_volatility_daily
                WHERE ticker = ?
                ORDER BY date DESC
                LIMIT 1
            ''', (ticker,))

            row = cursor.fetchone()

            if row:
                result[ticker] = {
                    'date': row[0],
                    'call_iv': row[1],
                    'put_iv': row[2],
                    'average_iv': row[3],
                    'current_price': row[4],
                    'expiration': row[5]
                }
            else:
                result[ticker] = None

            app.logger.info(f"/api/iv/latest: {ticker} returned {('data' if row else 'no data')}")

        except Exception as e:
            app.logger.error(f"/api/iv/latest: Error for {ticker}: {e}")
            result[ticker] = None

    conn.close()
    return jsonify(result)


import csv
import io

# FRED/Macro indicators list - all-caps series from FRED
# Used by both /api/dashboard (to exclude) and /api/macro-dashboard (to include)
FRED_INDICATORS = [
    'DGS2', 'DGS10', 'DGS30', 'FEDFUNDS', 'EFFR', 'SOFR',
    'CPIAUCSL', 'CPILFESL', 'PCEPI', 'PCE',
    'T5YIE', 'T10YIE', 'T5YIFR',
    'UNRATE', 'PAYEMS', 'ICSA', 'CCSA', 'JTSJOL',
    'GDP', 'GDPC1', 'INDPRO',
    'UMCSENT', 'RSXFS', 'HOUST', 'PERMIT',
    'M2SL', 'WALCL', 'RRPONTSYD',
    'MORTGAGE30US', 'BAMLH0A0HYM2', 'BAMLC0A0CM',
    'DTWEXBGS', 'DEXUSEU', 'DEXJPUS', 'DEXCHUS',
    'WTI', 'DCOILWTICO', 'GASREGW',
    'T10Y2Y', 'T10Y3M'
]


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

# Lazy-load playwright to avoid import errors if not installed
_playwright_available = None

def _check_playwright():
    """Check if playwright is available (lazy import)."""
    global _playwright_available
    if _playwright_available is None:
        try:
            from playwright.sync_api import sync_playwright
            _playwright_available = True
        except ImportError:
            _playwright_available = False
    return _playwright_available


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
                    query = f"""
                        SELECT fiscal_date_ending, ({column}) as metric_value
                        FROM {table}
                        WHERE ticker = ?
                    """
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
            def get_sort_value(ticker):
                points = chart_data.get(ticker, [])
                if not points or len(points) < 2:
                    return float('-inf')
                if normalize:
                    # For normalized charts, sort by % change from first to last
                    first_val = points[0]['value']
                    last_val = points[-1]['value']
                    if first_val and first_val != 0:
                        return ((last_val - first_val) / first_val) * 100
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
