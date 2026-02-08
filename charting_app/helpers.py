"""
Shared utilities used by multiple blueprint modules.
"""
import sqlite3
import time
import os
import sys
import logging

import pandas as pd

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import (DB_PATH, get_db_connection, SCHEMA_CACHE_TTL)

logger = logging.getLogger(__name__)

# Get the absolute path of the directory containing this script (charting_app)
basedir = os.path.abspath(os.path.dirname(__file__))

# --- DuckDB support ---
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

# --- Schema cache ---
_schema_cache = {}
_schema_cache_time = 0


def get_table_columns(table_name, conn=None, force_refresh=False):
    """Get column names for a table with caching."""
    global _schema_cache, _schema_cache_time

    # Check if cache needs refresh
    if force_refresh or time.time() - _schema_cache_time > SCHEMA_CACHE_TTL:
        _schema_cache = {}
        _schema_cache_time = time.time()
        logger.info(f"Schema cache refreshed")

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
        logger.info(f"Cached schema for table {table_name}: {len(columns)} columns")
        return columns
    except sqlite3.OperationalError:
        _schema_cache[table_name] = set()
        return set()
    finally:
        if close_conn:
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
            logger.warning(f"Slow query ({query_time:.2f}s): {table_name} for {len(valid_tickers)} tickers")

        # Split into per-ticker DataFrames
        for ticker in valid_tickers:
            if ticker in df.columns:
                result[ticker] = df[[ticker]].dropna()

    except Exception as e:
        logger.error(f"Error fetching from {table_name}: {e}")
    finally:
        if close_conn:
            conn.close()

    return result


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


# --- Playwright availability check ---
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
