"""
SQLite narrow-format query helpers for the charting app.
Mirrors duckdb_queries.py function signatures but reads from
prices_long / volumes_long tables in market_data.db.
"""

import os
import sys
import sqlite3
import pandas as pd
from typing import List, Dict, Optional, Set

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import DB_PATH, get_db_connection


# ---------------------------------------------------------------------------
# Ticker discovery
# ---------------------------------------------------------------------------

def get_available_tickers() -> Set[str]:
    """Get all tickers in prices_long."""
    conn = get_db_connection(row_factory=None)
    try:
        rows = conn.execute("SELECT DISTINCT Ticker FROM prices_long").fetchall()
        return {r[0] for r in rows}
    finally:
        conn.close()


def get_futures_tickers() -> Set[str]:
    """Get all tickers in futures_prices_long."""
    conn = get_db_connection(row_factory=None)
    try:
        rows = conn.execute("SELECT DISTINCT Ticker FROM futures_prices_long").fetchall()
        return {r[0] for r in rows}
    except sqlite3.OperationalError:
        return set()
    finally:
        conn.close()


def get_bond_tickers() -> Set[str]:
    """Get all tickers in bond_prices_daily (unchanged — already narrow-ish)."""
    conn = get_db_connection(row_factory=None)
    try:
        cols = conn.execute("PRAGMA table_info(bond_prices_daily)").fetchall()
        return {c[1] for c in cols if c[1] != 'Date'}
    except sqlite3.OperationalError:
        return set()
    finally:
        conn.close()


def get_volume_tickers() -> Set[str]:
    """Get all tickers in volumes_long."""
    conn = get_db_connection(row_factory=None)
    try:
        rows = conn.execute("SELECT DISTINCT Ticker FROM volumes_long").fetchall()
        return {r[0] for r in rows}
    except sqlite3.OperationalError:
        return set()
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Chart-ready data (long format → {ticker: [{time, value}]})
# ---------------------------------------------------------------------------

def get_price_data(tickers: List[str], start_date: Optional[str] = None) -> Dict[str, List[dict]]:
    """
    Get price data for tickers in lightweight-chart format.

    Returns:
        {ticker: [{time: unix_seconds, value: float}, ...]}
    """
    stock_tickers = get_available_tickers()
    futures_tickers = get_futures_tickers()

    result = {}
    conn = get_db_connection(row_factory=None)
    try:
        for ticker in tickers:
            if ticker in stock_tickers:
                table = 'prices_long'
            elif ticker in futures_tickers:
                table = 'futures_prices_long'
            else:
                result[ticker] = []
                continue

            date_filter = "AND Date >= ?" if start_date else ""
            query = f"""
                SELECT Date, Close AS value
                FROM {table}
                WHERE Ticker = ? {date_filter}
                ORDER BY Date ASC
            """
            params = [ticker]
            if start_date:
                params.append(start_date)

            df = pd.read_sql(query, conn, params=params)
            if df.empty:
                result[ticker] = []
                continue

            df['time'] = (pd.to_datetime(df['Date']).astype('int64') // 10**9).astype(int)
            result[ticker] = df[['time', 'value']].to_dict(orient='records')
    finally:
        conn.close()

    return result


def get_price_data_wide(tickers: List[str], start_date: Optional[str] = None) -> pd.DataFrame:
    """
    Get price data pivoted back to wide format (Date index, ticker columns).
    Bridge for existing scripts that expect a wide DataFrame.
    """
    if not tickers:
        return pd.DataFrame()

    stock_tickers = get_available_tickers()
    valid = [t for t in tickers if t in stock_tickers]
    if not valid:
        return pd.DataFrame()

    conn = get_db_connection(row_factory=None)
    try:
        placeholders = ','.join(['?'] * len(valid))
        date_filter = "AND Date >= ?" if start_date else ""
        query = f"""
            SELECT Date, Ticker, Close
            FROM prices_long
            WHERE Ticker IN ({placeholders}) {date_filter}
            ORDER BY Date
        """
        params = list(valid)
        if start_date:
            params.append(start_date)

        df = pd.read_sql(query, conn, params=params)
    finally:
        conn.close()

    if df.empty:
        return pd.DataFrame()

    wide = df.pivot(index='Date', columns='Ticker', values='Close')
    wide.index.name = 'Date'
    # Reorder columns to match requested order
    ordered = [t for t in tickers if t in wide.columns]
    return wide[ordered]


def get_volume_data(tickers: List[str]) -> Dict[str, List[dict]]:
    """
    Get volume data in chart-ready format.

    Returns:
        {ticker: [{time: unix_seconds, value: float}, ...]}
    """
    volume_tickers = get_volume_tickers()
    result = {}
    conn = get_db_connection(row_factory=None)
    try:
        for ticker in tickers:
            if ticker not in volume_tickers:
                result[ticker] = []
                continue

            query = """
                SELECT Date, Volume AS value
                FROM volumes_long
                WHERE Ticker = ?
                ORDER BY Date ASC
            """
            df = pd.read_sql(query, conn, params=[ticker])
            if df.empty:
                result[ticker] = []
                continue

            df['time'] = (pd.to_datetime(df['Date']).astype('int64') // 10**9).astype(int)
            df['value'] = df['value'].where(pd.notna(df['value']), None)
            result[ticker] = df[['time', 'value']].to_dict(orient='records')
    finally:
        conn.close()

    return result


def get_dashboard_prices(tickers: List[str], lookback_days: int = 252) -> pd.DataFrame:
    """
    Recent prices for dashboard calcs.

    Returns long-format DataFrame with Date, Ticker, Close columns.
    """
    if not tickers:
        return pd.DataFrame()

    conn = get_db_connection(row_factory=None)
    try:
        placeholders = ','.join(['?'] * len(tickers))
        query = f"""
            SELECT Date, Ticker, Close
            FROM prices_long
            WHERE Ticker IN ({placeholders})
            ORDER BY Date DESC
            LIMIT ?
        """
        params = list(tickers) + [lookback_days * len(tickers)]
        return pd.read_sql(query, conn, params=params)
    finally:
        conn.close()


def get_all_tickers_list() -> List[str]:
    """Sorted list of all tickers across all narrow tables."""
    tickers = set()
    tickers.update(get_available_tickers())
    tickers.update(get_futures_tickers())
    return sorted(tickers)


def get_metadata(tickers: List[str]) -> Dict[str, dict]:
    """Get metadata for tickers from ticker_metadata."""
    if not tickers:
        return {}

    conn = get_db_connection(row_factory=None)
    try:
        placeholders = ','.join(['?'] * len(tickers))
        query = f"""
            SELECT ticker, name, first_date, last_date, data_points
            FROM ticker_metadata
            WHERE ticker IN ({placeholders})
        """
        rows = conn.execute(query, tickers).fetchall()
        result = {}
        for r in rows:
            result[r[0]] = {
                'name': r[1],
                'first_date': r[2],
                'last_date': r[3],
                'data_points': r[4]
            }
        return result
    except sqlite3.OperationalError:
        return {}
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Write helpers (for dual-write / sync)
# ---------------------------------------------------------------------------

def upsert_prices_long(df_long: pd.DataFrame, table: str = 'prices_long',
                       value_col: str = 'Close', verbose: bool = True):
    """
    INSERT OR REPLACE rows into a narrow table.

    Args:
        df_long: DataFrame with columns [Date, Ticker, <value_col>]
        table: Target table name
        value_col: Name of the value column (Close or Volume)
        verbose: Print progress
    """
    if df_long.empty:
        return

    conn = sqlite3.connect(DB_PATH)
    try:
        rows = list(zip(df_long['Date'], df_long['Ticker'], df_long[value_col]))
        conn.executemany(
            f'INSERT OR REPLACE INTO {table} (Date, Ticker, {value_col}) VALUES (?, ?, ?)',
            rows
        )
        conn.commit()
        if verbose:
            print(f"  [Narrow] Upserted {len(rows):,} rows into {table}")
    finally:
        conn.close()


def _ensure_narrow_table(table: str, value_col: str):
    """Create narrow table with indexes if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(f'''CREATE TABLE IF NOT EXISTS {table} (
            Date TEXT NOT NULL,
            Ticker TEXT NOT NULL,
            {value_col} REAL,
            PRIMARY KEY (Date, Ticker)
        )''')
        conn.execute(f'CREATE INDEX IF NOT EXISTS idx_{table}_ticker ON {table}(Ticker)')
        conn.execute(f'CREATE INDEX IF NOT EXISTS idx_{table}_date ON {table}(Date)')
        conn.commit()
    finally:
        conn.close()


def sync_wide_to_narrow(df_wide: pd.DataFrame, table: str = 'prices_long',
                        value_col: str = 'Close', verbose: bool = True):
    """
    Melt a wide DataFrame (Date index, ticker columns) to long format
    and upsert into a narrow table.

    This is the canonical write entry point. Creates the table if needed.
    """
    if df_wide.empty:
        if verbose:
            print(f"  [Narrow] Skipping {table} — empty DataFrame")
        return

    _ensure_narrow_table(table, value_col)

    df = df_wide.reset_index()
    if 'index' in df.columns:
        df = df.rename(columns={'index': 'Date'})

    df_long = df.melt(id_vars=['Date'], var_name='Ticker', value_name=value_col)
    df_long = df_long.dropna(subset=[value_col])

    if df_long.empty:
        if verbose:
            print(f"  [Narrow] Skipping {table} — no non-null data after melt")
        return

    # Normalize dates to match DB format
    df_long['Date'] = pd.to_datetime(df_long['Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

    upsert_prices_long(df_long, table=table, value_col=value_col, verbose=verbose)


def check_narrow_available() -> bool:
    """Check if narrow tables exist and have data."""
    try:
        conn = get_db_connection(row_factory=None)
        count = conn.execute("SELECT COUNT(*) FROM prices_long").fetchone()[0]
        conn.close()
        return count > 0
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print(f"DB path: {DB_PATH}")
    print(f"Narrow tables available: {check_narrow_available()}")

    if check_narrow_available():
        stock = get_available_tickers()
        print(f"\nStock tickers: {len(stock)}")
        futures = get_futures_tickers()
        print(f"Futures tickers: {len(futures)}")
        vol = get_volume_tickers()
        print(f"Volume tickers: {len(vol)}")

        data = get_price_data(['AAPL', 'MSFT'], start_date='2025-01-01')
        for ticker, points in data.items():
            print(f"\n{ticker}: {len(points)} data points")
            if points:
                print(f"  First: {points[0]}")
                print(f"  Last: {points[-1]}")
