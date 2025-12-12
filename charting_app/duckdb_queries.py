"""
DuckDB query helpers for the charting app.
Provides functions that return data in the same format as the SQLite queries,
using PIVOT to convert from long format back to wide format for API compatibility.
"""

import os
import sys
import duckdb
import pandas as pd
from typing import List, Dict, Optional, Set

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import DUCKDB_PATH, get_duckdb_connection as _get_duckdb_connection, duckdb_available

# Connection pool (DuckDB handles this well)
_conn = None


def get_duckdb_connection(read_only: bool = True):
    """Get a DuckDB connection."""
    global _conn
    if _conn is None or not read_only:
        _conn = _get_duckdb_connection(read_only=read_only)
    return _conn


def get_available_tickers() -> Set[str]:
    """Get all available tickers from the prices table."""
    conn = get_duckdb_connection()
    result = conn.execute("SELECT DISTINCT Ticker FROM prices").fetchall()
    return {row[0] for row in result}


def get_futures_tickers() -> Set[str]:
    """Get all available futures tickers."""
    conn = get_duckdb_connection()
    try:
        result = conn.execute("SELECT DISTINCT Ticker FROM futures_prices").fetchall()
        return {row[0] for row in result}
    except Exception:
        return set()


def get_bond_tickers() -> Set[str]:
    """Get all available bond tickers."""
    conn = get_duckdb_connection()
    try:
        result = conn.execute("SELECT DISTINCT Ticker FROM bond_prices").fetchall()
        return {row[0] for row in result}
    except Exception:
        return set()


def get_volume_tickers() -> Set[str]:
    """Get all available volume tickers."""
    conn = get_duckdb_connection()
    try:
        result = conn.execute("SELECT DISTINCT Ticker FROM volumes").fetchall()
        return {row[0] for row in result}
    except Exception:
        return set()


def get_price_data(tickers: List[str], start_date: Optional[str] = None) -> Dict[str, List[dict]]:
    """
    Get price data for tickers, returning in chart-ready format.

    Args:
        tickers: List of ticker symbols
        start_date: Optional start date filter (YYYY-MM-DD)

    Returns:
        Dict mapping ticker -> list of {time: unix_seconds, value: price}
    """
    conn = get_duckdb_connection()

    # Determine which table each ticker belongs to
    stock_tickers = get_available_tickers()
    futures_tickers = get_futures_tickers()
    bond_tickers = get_bond_tickers()

    result = {}

    for ticker in tickers:
        if ticker in stock_tickers:
            table = 'prices'
        elif ticker in futures_tickers:
            table = 'futures_prices'
        elif ticker in bond_tickers:
            table = 'bond_prices'
        else:
            result[ticker] = []
            continue

        # Query for this ticker
        date_filter = f"AND Date >= '{start_date}'" if start_date else ""

        query = f"""
            SELECT Date, Close as value
            FROM {table}
            WHERE Ticker = ? {date_filter}
            ORDER BY Date ASC
        """

        df = conn.execute(query, [ticker]).fetchdf()

        if df.empty:
            result[ticker] = []
            continue

        # Convert to chart format
        df['time'] = (pd.to_datetime(df['Date']).astype('int64') // 10**9).astype(int)
        result[ticker] = df[['time', 'value']].to_dict(orient='records')

    return result


def get_price_data_wide(tickers: List[str], start_date: Optional[str] = None) -> pd.DataFrame:
    """
    Get price data in wide format (Date as index, tickers as columns).
    Uses DuckDB PIVOT for efficient conversion.

    Args:
        tickers: List of ticker symbols
        start_date: Optional start date filter

    Returns:
        DataFrame with Date index and ticker columns
    """
    conn = get_duckdb_connection()

    if not tickers:
        return pd.DataFrame()

    # Filter to valid tickers
    stock_tickers = get_available_tickers()
    valid_tickers = [t for t in tickers if t in stock_tickers]

    if not valid_tickers:
        return pd.DataFrame()

    # Build ticker list for SQL
    ticker_list = "', '".join(valid_tickers)
    date_filter = f"AND Date >= '{start_date}'" if start_date else ""

    # Use PIVOT to convert long to wide
    query = f"""
        PIVOT (
            SELECT Date, Ticker, Close
            FROM prices
            WHERE Ticker IN ('{ticker_list}') {date_filter}
        )
        ON Ticker
        USING first(Close)
        GROUP BY Date
        ORDER BY Date
    """

    df = conn.execute(query).fetchdf()

    if not df.empty:
        df = df.set_index('Date')

    return df


def get_volume_data(tickers: List[str]) -> Dict[str, List[dict]]:
    """
    Get volume data for tickers.

    Returns:
        Dict mapping ticker -> list of {time: unix_seconds, value: volume}
    """
    conn = get_duckdb_connection()
    volume_tickers = get_volume_tickers()

    result = {}

    for ticker in tickers:
        if ticker not in volume_tickers:
            result[ticker] = []
            continue

        query = """
            SELECT Date, Volume as value
            FROM volumes
            WHERE Ticker = ?
            ORDER BY Date ASC
        """

        df = conn.execute(query, [ticker]).fetchdf()

        if df.empty:
            result[ticker] = []
            continue

        df['time'] = (pd.to_datetime(df['Date']).astype('int64') // 10**9).astype(int)
        # Replace NaN with None for JSON serialization
        df['value'] = df['value'].where(pd.notna(df['value']), None)
        result[ticker] = df[['time', 'value']].to_dict(orient='records')

    return result


def get_dashboard_prices(tickers: List[str], lookback_days: int = 252) -> pd.DataFrame:
    """
    Get recent prices for dashboard calculations.

    Args:
        tickers: List of ticker symbols
        lookback_days: Number of days to look back

    Returns:
        DataFrame with Date, Ticker, Close columns (long format)
    """
    conn = get_duckdb_connection()

    if not tickers:
        return pd.DataFrame()

    ticker_list = "', '".join(tickers)

    query = f"""
        SELECT Date, Ticker, Close
        FROM prices
        WHERE Ticker IN ('{ticker_list}')
        ORDER BY Date DESC
        LIMIT {lookback_days * len(tickers)}
    """

    return conn.execute(query).fetchdf()


def get_all_tickers_list() -> List[str]:
    """Get sorted list of all available tickers across all tables."""
    tickers = set()
    tickers.update(get_available_tickers())
    tickers.update(get_futures_tickers())
    tickers.update(get_bond_tickers())
    return sorted(tickers)


def get_metadata(tickers: List[str]) -> Dict[str, dict]:
    """Get metadata for tickers."""
    conn = get_duckdb_connection()

    if not tickers:
        return {}

    ticker_list = "', '".join(tickers)

    query = f"""
        SELECT ticker, name, first_date, last_date, data_points
        FROM ticker_metadata
        WHERE ticker IN ('{ticker_list}')
    """

    try:
        df = conn.execute(query).fetchdf()
        result = {}
        for _, row in df.iterrows():
            result[row['ticker']] = {
                'name': row['name'],
                'first_date': row['first_date'],
                'last_date': row['last_date'],
                'data_points': row['data_points']
            }
        return result
    except Exception:
        return {}


def check_duckdb_available() -> bool:
    """Check if DuckDB database exists and is accessible."""
    if not duckdb_available():
        return False

    try:
        conn = get_duckdb_connection(read_only=True)
        conn.execute("SELECT 1 FROM prices LIMIT 1").fetchone()
        return True
    except Exception:
        return False


# Test function
if __name__ == "__main__":
    print(f"DuckDB path: {DUCKDB_PATH}")
    print(f"Available: {check_duckdb_available()}")

    if check_duckdb_available():
        print(f"\nStock tickers: {len(get_available_tickers())}")
        print(f"Futures tickers: {len(get_futures_tickers())}")
        print(f"Volume tickers: {len(get_volume_tickers())}")

        # Test price query
        data = get_price_data(['AAPL', 'MSFT'], start_date='2025-01-01')
        for ticker, points in data.items():
            print(f"\n{ticker}: {len(points)} data points")
            if points:
                print(f"  First: {points[0]}")
                print(f"  Last: {points[-1]}")
