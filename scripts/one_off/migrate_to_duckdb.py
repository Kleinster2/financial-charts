#!/usr/bin/env python3
"""
migrate_to_duckdb.py - Migrate SQLite wide tables to DuckDB long format

Phase 1 of the DuckDB migration:
- Reads existing market_data.db (SQLite)
- Melts wide tables (stock_prices_daily, stock_volumes_daily, futures_prices_daily, etc.) to long format
- Saves to market_data.duckdb

Schema:
    prices: (Date DATE, Ticker VARCHAR, Close DOUBLE, PRIMARY KEY (Date, Ticker))
    volumes: (Date DATE, Ticker VARCHAR, Volume DOUBLE, PRIMARY KEY (Date, Ticker))
"""

import os
import sqlite3
import duckdb
import pandas as pd
from datetime import datetime

# Paths
SQLITE_PATH = os.path.join(os.path.dirname(__file__), "market_data.db")
DUCKDB_PATH = os.path.join(os.path.dirname(__file__), "market_data.duckdb")


def get_sqlite_tables(sqlite_conn):
    """Get list of tables in SQLite database."""
    cursor = sqlite_conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    )
    return [row[0] for row in cursor.fetchall()]


def melt_wide_table(df, value_name="value"):
    """Convert wide DataFrame (Date as index, tickers as columns) to long format."""
    # Reset index to get Date as a column
    df = df.reset_index()

    # Melt: Date stays, all other columns become Ticker/value pairs
    df_long = df.melt(
        id_vars=["Date"],
        var_name="Ticker",
        value_name=value_name
    )

    # Drop nulls (sparse data)
    df_long = df_long.dropna(subset=[value_name])

    return df_long


def migrate_price_table(sqlite_conn, duck_conn, sqlite_table, duck_table, value_col="Close"):
    """Migrate a wide price table to long format in DuckDB."""
    print(f"\n  Migrating {sqlite_table} -> {duck_table}...")

    # Read from SQLite
    df = pd.read_sql(
        f'SELECT * FROM "{sqlite_table}" ORDER BY Date',
        sqlite_conn,
        parse_dates=["Date"]
    )

    if df.empty:
        print(f"    Skipping {sqlite_table} - empty table")
        return 0

    df = df.set_index("Date")
    print(f"    Read {len(df)} rows, {len(df.columns)} tickers")

    # Convert to long format
    df_long = melt_wide_table(df, value_name=value_col)
    print(f"    Melted to {len(df_long)} rows")

    # Create table in DuckDB if not exists
    duck_conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {duck_table} (
            Date DATE,
            Ticker VARCHAR,
            {value_col} DOUBLE,
            PRIMARY KEY (Date, Ticker)
        )
    """)

    # Insert data
    duck_conn.execute(f"DELETE FROM {duck_table}")  # Clear existing
    duck_conn.execute(f"""
        INSERT INTO {duck_table} (Date, Ticker, {value_col})
        SELECT Date, Ticker, {value_col} FROM df_long
    """)

    count = duck_conn.execute(f"SELECT COUNT(*) FROM {duck_table}").fetchone()[0]
    print(f"    Inserted {count} rows into {duck_table}")
    return count


def migrate_metadata_table(sqlite_conn, duck_conn, table_name):
    """Copy a metadata table directly (not melted)."""
    print(f"\n  Copying metadata table {table_name}...")

    try:
        df = pd.read_sql(f'SELECT * FROM "{table_name}"', sqlite_conn)
    except Exception as e:
        print(f"    Skipping {table_name}: {e}")
        return 0

    if df.empty:
        print(f"    Skipping {table_name} - empty table")
        return 0

    # Drop and recreate in DuckDB
    duck_conn.execute(f"DROP TABLE IF EXISTS {table_name}")
    duck_conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")

    count = duck_conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
    print(f"    Copied {count} rows")
    return count


def main():
    print("=" * 70)
    print("DuckDB Migration - Phase 1: Shadow Database")
    print("=" * 70)
    print(f"\nSource: {SQLITE_PATH}")
    print(f"Target: {DUCKDB_PATH}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Check SQLite exists
    if not os.path.exists(SQLITE_PATH):
        print(f"\nERROR: SQLite database not found: {SQLITE_PATH}")
        return

    # Connect to databases
    sqlite_conn = sqlite3.connect(SQLITE_PATH)

    # Remove existing DuckDB file to start fresh
    if os.path.exists(DUCKDB_PATH):
        os.remove(DUCKDB_PATH)
        print(f"\nRemoved existing {DUCKDB_PATH}")

    duck_conn = duckdb.connect(DUCKDB_PATH)

    # Get SQLite tables
    tables = get_sqlite_tables(sqlite_conn)
    print(f"\nFound {len(tables)} tables in SQLite:")
    for t in tables:
        print(f"  - {t}")

    # Migrate price tables (wide -> long)
    print("\n" + "=" * 70)
    print("Migrating Price Tables (Wide -> Long)")
    print("=" * 70)

    price_tables = [
        ("stock_prices_daily", "prices", "Close"),
        ("futures_prices_daily", "futures_prices", "Close"),
        ("bond_prices_daily", "bond_prices", "Close"),
    ]

    for sqlite_table, duck_table, value_col in price_tables:
        if sqlite_table in tables:
            migrate_price_table(sqlite_conn, duck_conn, sqlite_table, duck_table, value_col)
        else:
            print(f"\n  Skipping {sqlite_table} - not found")

    # Migrate volume tables (wide -> long)
    print("\n" + "=" * 70)
    print("Migrating Volume Tables (Wide -> Long)")
    print("=" * 70)

    volume_tables = [
        ("stock_volumes_daily", "volumes", "Volume"),
        ("futures_volumes_daily", "futures_volumes", "Volume"),
    ]

    for sqlite_table, duck_table, value_col in volume_tables:
        if sqlite_table in tables:
            migrate_price_table(sqlite_conn, duck_conn, sqlite_table, duck_table, value_col)
        else:
            print(f"\n  Skipping {sqlite_table} - not found")

    # Migrate metadata tables (direct copy)
    print("\n" + "=" * 70)
    print("Copying Metadata Tables")
    print("=" * 70)

    metadata_tables = [
        "ticker_metadata",
        "stock_metadata",
        "company_overview",
        "investment_theses",
    ]

    for table in metadata_tables:
        if table in tables:
            migrate_metadata_table(sqlite_conn, duck_conn, table)

    # Migrate fundamental tables (direct copy - they're already normalized)
    print("\n" + "=" * 70)
    print("Copying Fundamental Tables")
    print("=" * 70)

    fundamental_tables = [
        "earnings_quarterly", "earnings_annual",
        "income_statement_quarterly", "income_statement_annual",
        "balance_sheet_quarterly", "balance_sheet_annual",
        "cash_flow_quarterly", "cash_flow_annual",
    ]

    for table in fundamental_tables:
        if table in tables:
            migrate_metadata_table(sqlite_conn, duck_conn, table)

    # Migrate other tables
    print("\n" + "=" * 70)
    print("Copying Other Tables")
    print("=" * 70)

    other_tables = [
        "cboe_indices_daily",
        "implied_volatility_daily",
        "etf_holdings_daily",
        "portfolios",
        "portfolio_transactions",
        "portfolio_holdings",
        "portfolio_valuations_daily",
        "portfolio_holdings_daily",
    ]

    for table in other_tables:
        if table in tables:
            migrate_metadata_table(sqlite_conn, duck_conn, table)

    # Create indexes
    print("\n" + "=" * 70)
    print("Creating Indexes")
    print("=" * 70)

    indexes = [
        ("idx_prices_ticker", "prices", "Ticker"),
        ("idx_prices_date", "prices", "Date"),
        ("idx_volumes_ticker", "volumes", "Ticker"),
        ("idx_volumes_date", "volumes", "Date"),
        ("idx_futures_prices_ticker", "futures_prices", "Ticker"),
        ("idx_futures_prices_date", "futures_prices", "Date"),
    ]

    for idx_name, table, column in indexes:
        try:
            duck_conn.execute(f"CREATE INDEX IF NOT EXISTS {idx_name} ON {table}({column})")
            print(f"  Created index {idx_name}")
        except Exception as e:
            print(f"  Skipping index {idx_name}: {e}")

    # Summary
    print("\n" + "=" * 70)
    print("Migration Summary")
    print("=" * 70)

    duck_tables = duck_conn.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema='main'"
    ).fetchall()

    print(f"\nDuckDB tables created: {len(duck_tables)}")
    for (t,) in duck_tables:
        count = duck_conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"  - {t}: {count:,} rows")

    # File sizes
    sqlite_size = os.path.getsize(SQLITE_PATH) / (1024 * 1024)
    duckdb_size = os.path.getsize(DUCKDB_PATH) / (1024 * 1024)
    print(f"\nFile sizes:")
    print(f"  SQLite: {sqlite_size:.1f} MB")
    print(f"  DuckDB: {duckdb_size:.1f} MB")
    print(f"  Ratio:  {duckdb_size/sqlite_size:.1%}")

    # Close connections
    sqlite_conn.close()
    duck_conn.close()

    print(f"\nCompleted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
