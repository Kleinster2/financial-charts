"""
DuckDB writer for market data - writes data in long format.
Used by download_all_assets.py to maintain DuckDB alongside SQLite.
"""

import os
import duckdb
import pandas as pd
from datetime import datetime

from constants import DUCKDB_PATH, get_duckdb_connection as _get_duckdb_conn, duckdb_available


def get_duckdb_connection(read_only: bool = False):
    """Get a DuckDB connection."""
    return _get_duckdb_conn(read_only=read_only)


def ensure_tables_exist(conn):
    """Create tables if they don't exist."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            Date DATE,
            Ticker VARCHAR,
            Close DOUBLE,
            PRIMARY KEY (Date, Ticker)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS volumes (
            Date DATE,
            Ticker VARCHAR,
            Volume DOUBLE,
            PRIMARY KEY (Date, Ticker)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS futures_prices (
            Date DATE,
            Ticker VARCHAR,
            Close DOUBLE,
            PRIMARY KEY (Date, Ticker)
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS futures_volumes (
            Date DATE,
            Ticker VARCHAR,
            Volume DOUBLE,
            PRIMARY KEY (Date, Ticker)
        )
    """)

    # Create indexes if not exist
    try:
        conn.execute("CREATE INDEX IF NOT EXISTS idx_prices_ticker ON prices(Ticker)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_prices_date ON prices(Date)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_volumes_ticker ON volumes(Ticker)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_volumes_date ON volumes(Date)")
    except Exception:
        pass  # Indexes may already exist


def write_prices_long(df_wide: pd.DataFrame, table: str = "prices", value_col: str = "Close", verbose: bool = True):
    """
    Write price data from wide format DataFrame to DuckDB long format.

    Args:
        df_wide: DataFrame with Date index and ticker columns
        table: Target table name ('prices', 'futures_prices', 'volumes', etc.)
        value_col: Name for the value column in long format
        verbose: Print progress info
    """
    if df_wide.empty:
        if verbose:
            print(f"  [DuckDB] Skipping {table} - empty DataFrame")
        return

    conn = get_duckdb_connection(read_only=False)
    ensure_tables_exist(conn)

    # Melt wide to long format
    df_wide = df_wide.reset_index()
    if 'index' in df_wide.columns:
        df_wide = df_wide.rename(columns={'index': 'Date'})

    df_long = df_wide.melt(
        id_vars=['Date'],
        var_name='Ticker',
        value_name=value_col
    )

    # Drop nulls
    df_long = df_long.dropna(subset=[value_col])

    if df_long.empty:
        if verbose:
            print(f"  [DuckDB] Skipping {table} - no valid data after melt")
        conn.close()
        return

    if verbose:
        print(f"  [DuckDB] Writing {len(df_long):,} rows to {table}")

    # Use INSERT OR REPLACE pattern with staging
    staging_table = f"{table}_staging"

    # Create staging table
    conn.execute(f"DROP TABLE IF EXISTS {staging_table}")
    conn.execute(f"""
        CREATE TABLE {staging_table} (
            Date DATE,
            Ticker VARCHAR,
            {value_col} DOUBLE,
            PRIMARY KEY (Date, Ticker)
        )
    """)

    # Insert new data into staging
    conn.execute(f"""
        INSERT INTO {staging_table} (Date, Ticker, {value_col})
        SELECT Date, Ticker, {value_col} FROM df_long
    """)

    # Merge staging into main table (upsert)
    # Delete existing rows that will be updated, then insert all from staging
    conn.execute(f"""
        DELETE FROM {table}
        WHERE (Date, Ticker) IN (SELECT Date, Ticker FROM {staging_table})
    """)

    conn.execute(f"""
        INSERT INTO {table}
        SELECT * FROM {staging_table}
    """)

    # Drop staging
    conn.execute(f"DROP TABLE {staging_table}")

    # Get final count
    count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]

    if verbose:
        print(f"  [DuckDB] {table} now has {count:,} total rows")

    conn.close()


def write_stock_prices(df_prices: pd.DataFrame, df_volumes: pd.DataFrame = None, verbose: bool = True):
    """
    Write stock prices and volumes to DuckDB.

    Args:
        df_prices: Wide format DataFrame with Date index, ticker columns, Close prices
        df_volumes: Wide format DataFrame with Date index, ticker columns, Volume values
        verbose: Print progress
    """
    if verbose:
        print("\n  [DuckDB] Writing stock data...")

    write_prices_long(df_prices, table="prices", value_col="Close", verbose=verbose)

    if df_volumes is not None and not df_volumes.empty:
        write_prices_long(df_volumes, table="volumes", value_col="Volume", verbose=verbose)


def write_futures_prices(df_prices: pd.DataFrame, df_volumes: pd.DataFrame = None, verbose: bool = True):
    """
    Write futures prices and volumes to DuckDB.

    Args:
        df_prices: Wide format DataFrame with Date index, ticker columns
        df_volumes: Wide format DataFrame with Date index, ticker columns
        verbose: Print progress
    """
    if verbose:
        print("\n  [DuckDB] Writing futures data...")

    write_prices_long(df_prices, table="futures_prices", value_col="Close", verbose=verbose)

    if df_volumes is not None and not df_volumes.empty:
        write_prices_long(df_volumes, table="futures_volumes", value_col="Volume", verbose=verbose)


def check_duckdb_exists() -> bool:
    """Check if DuckDB database exists."""
    return duckdb_available()


def get_duckdb_stats() -> dict:
    """Get statistics about the DuckDB database."""
    if not check_duckdb_exists():
        return {'exists': False}

    conn = get_duckdb_connection(read_only=True)

    stats = {'exists': True}

    tables = ['prices', 'volumes', 'futures_prices', 'futures_volumes']
    for table in tables:
        try:
            count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            ticker_count = conn.execute(f"SELECT COUNT(DISTINCT Ticker) FROM {table}").fetchone()[0]
            stats[table] = {'rows': count, 'tickers': ticker_count}
        except Exception:
            stats[table] = {'rows': 0, 'tickers': 0}

    conn.close()
    return stats


# Test
if __name__ == "__main__":
    print(f"DuckDB path: {DUCKDB_PATH}")
    print(f"Exists: {check_duckdb_exists()}")

    if check_duckdb_exists():
        stats = get_duckdb_stats()
        print("\nDatabase stats:")
        for key, val in stats.items():
            if key != 'exists':
                print(f"  {key}: {val}")
