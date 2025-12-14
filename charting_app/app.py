import sqlite3
import time
import json
import os
import sys
import logging
import traceback
from flask import Flask, jsonify, request, Response, redirect, send_from_directory
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

    # Use DuckDB if enabled
    if USE_DUCKDB and DUCKDB_AVAILABLE:
        chart_data = get_price_data(tickers)

        # Apply interval resampling if needed
        if interval in ('weekly', 'monthly'):
            for ticker in chart_data:
                if not chart_data[ticker]:
                    continue
                # Convert to DataFrame for resampling
                df = pd.DataFrame(chart_data[ticker])
                df['Date'] = pd.to_datetime(df['time'], unit='s')
                df = df.set_index('Date')

                if interval == 'weekly':
                    df = df.resample('W-FRI')['value'].last().dropna().reset_index()
                else:  # monthly
                    df = df.resample('M')['value'].last().dropna().reset_index()

                df['time'] = (df['Date'].astype('int64') // 10**9).astype(int)
                chart_data[ticker] = df[['time', 'value']].to_dict(orient='records')

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
    chart_data = {}
    for ticker in tickers:
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
        'operatingcashflow': ('cash_flow_quarterly', 'operating_cashflow', 'Operating Cash Flow')
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


@app.route('/api/dashboard')
def get_dashboard_data():
    """
    Get comprehensive dashboard data for all tickers in workspace.
    Returns: Array of ticker data with prices, changes, metadata, and page info.
    """
    try:
        conn = get_db_connection()
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

        # Get column names from stock_prices_daily
        columns = get_table_columns('stock_prices_daily', conn)
        # Exclude FRED indicators - they go in the Macro Dashboard
        valid_tickers = [t for t in all_tickers if t in columns and t not in FRED_INDICATORS]

        if not valid_tickers:
            conn.close()
            return jsonify([])

        # Get latest prices and previous day prices for all tickers
        # Build dynamic SQL for selected tickers
        ticker_cols = ', '.join([f'"{t}"' for t in valid_tickers])

        # Get last 2 rows for each ticker to calculate daily change
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
                    # Convert to float if it's a string
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

            # Get 52-week high/low from the data we have
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
                'pages': pages
            })

        conn.close()

        # Sort by ticker
        result.sort(key=lambda x: x['ticker'])

        app.logger.info(f"/api/dashboard: Returned {len(result)} tickers")
        return jsonify(result)

    except Exception as e:
        app.logger.error(f"/api/dashboard: Error: {e}")
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
