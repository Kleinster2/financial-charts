#!/usr/bin/env python3
"""
Migrate wide-format tables to narrow (long) format in SQLite.

Creates:
  - prices_long (Date, Ticker, Close) from stock_prices_daily
  - volumes_long (Date, Ticker, Volume) from stock_volumes_daily
  - futures_prices_long from futures_prices_daily
  - futures_volumes_long from futures_volumes_daily

Safe to re-run: uses INSERT OR REPLACE.
"""

import os
import sys
import sqlite3
import time
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from constants import DB_PATH

CHUNK_SIZE = 2000  # rows per read chunk


def create_narrow_tables(conn):
    """Create narrow tables and indexes if they don't exist."""
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS prices_long (
            Date TEXT NOT NULL,
            Ticker TEXT NOT NULL,
            Close REAL,
            PRIMARY KEY (Date, Ticker)
        );
        CREATE INDEX IF NOT EXISTS idx_prices_long_ticker ON prices_long(Ticker);
        CREATE INDEX IF NOT EXISTS idx_prices_long_date ON prices_long(Date);

        CREATE TABLE IF NOT EXISTS volumes_long (
            Date TEXT NOT NULL,
            Ticker TEXT NOT NULL,
            Volume REAL,
            PRIMARY KEY (Date, Ticker)
        );
        CREATE INDEX IF NOT EXISTS idx_volumes_long_ticker ON volumes_long(Ticker);
        CREATE INDEX IF NOT EXISTS idx_volumes_long_date ON volumes_long(Date);

        CREATE TABLE IF NOT EXISTS futures_prices_long (
            Date TEXT NOT NULL,
            Ticker TEXT NOT NULL,
            Close REAL,
            PRIMARY KEY (Date, Ticker)
        );
        CREATE INDEX IF NOT EXISTS idx_futures_prices_long_ticker ON futures_prices_long(Ticker);
        CREATE INDEX IF NOT EXISTS idx_futures_prices_long_date ON futures_prices_long(Date);

        CREATE TABLE IF NOT EXISTS futures_volumes_long (
            Date TEXT NOT NULL,
            Ticker TEXT NOT NULL,
            Volume REAL,
            PRIMARY KEY (Date, Ticker)
        );
        CREATE INDEX IF NOT EXISTS idx_futures_volumes_long_ticker ON futures_volumes_long(Ticker);
        CREATE INDEX IF NOT EXISTS idx_futures_volumes_long_date ON futures_volumes_long(Date);
    """)


def migrate_table(conn, wide_table, narrow_table, value_col, verbose=True):
    """Melt a wide table into its narrow counterpart."""
    # Check if wide table exists
    cur = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
        (wide_table,)
    )
    if not cur.fetchone():
        if verbose:
            print(f"  Skipping {wide_table} — table does not exist")
        return 0

    # Get column info
    pragma = conn.execute(f"PRAGMA table_info({wide_table})").fetchall()
    ticker_cols = [row[1] for row in pragma if row[1] != 'Date']

    if not ticker_cols:
        if verbose:
            print(f"  Skipping {wide_table} — no ticker columns")
        return 0

    total_rows = conn.execute(f"SELECT COUNT(*) FROM {wide_table}").fetchone()[0]
    if verbose:
        print(f"\n  Migrating {wide_table} -> {narrow_table}")
        print(f"    Wide: {total_rows} rows x {len(ticker_cols)} tickers")

    total_inserted = 0
    t0 = time.time()

    # Read in chunks to control memory
    for offset in range(0, total_rows, CHUNK_SIZE):
        # Quote ticker columns to handle dots, special chars
        cols_str = ', '.join([f'"{c}"' for c in ticker_cols])
        query = f'SELECT Date, {cols_str} FROM {wide_table} LIMIT {CHUNK_SIZE} OFFSET {offset}'
        df = pd.read_sql(query, conn)

        # Melt to long format
        df_long = df.melt(id_vars=['Date'], var_name='Ticker', value_name=value_col)
        df_long = df_long.dropna(subset=[value_col])

        if df_long.empty:
            continue

        rows = list(zip(df_long['Date'], df_long['Ticker'], df_long[value_col]))
        conn.executemany(
            f'INSERT OR REPLACE INTO {narrow_table} (Date, Ticker, {value_col}) VALUES (?, ?, ?)',
            rows
        )
        total_inserted += len(rows)

        if verbose and (offset + CHUNK_SIZE) % 10000 == 0:
            elapsed = time.time() - t0
            print(f"    {offset + CHUNK_SIZE}/{total_rows} rows processed ({elapsed:.1f}s)")

    conn.commit()
    elapsed = time.time() - t0

    if verbose:
        final_count = conn.execute(f"SELECT COUNT(*) FROM {narrow_table}").fetchone()[0]
        distinct_tickers = conn.execute(f"SELECT COUNT(DISTINCT Ticker) FROM {narrow_table}").fetchone()[0]
        print(f"    Inserted: {total_inserted:,} rows in {elapsed:.1f}s")
        print(f"    {narrow_table}: {final_count:,} rows, {distinct_tickers} tickers")

    return total_inserted


def verify_migration(conn, verbose=True):
    """Spot-check a few tickers across wide and narrow tables."""
    checks = [
        ('AAPL', 'stock_prices_daily', 'prices_long', 'Close'),
        ('SPY', 'stock_prices_daily', 'prices_long', 'Close'),
        ('MSFT', 'stock_prices_daily', 'prices_long', 'Close'),
    ]

    if verbose:
        print("\n  Verification (spot checks):")

    all_ok = True
    for ticker, wide, narrow, val_col in checks:
        # Check if ticker exists in wide table
        pragma = conn.execute(f"PRAGMA table_info({wide})").fetchall()
        col_names = [r[1] for r in pragma]
        if ticker not in col_names:
            if verbose:
                print(f"    {ticker}: not in {wide} — skipping")
            continue

        # Get a sample row from wide
        row = conn.execute(
            f'SELECT Date, "{ticker}" FROM {wide} WHERE "{ticker}" IS NOT NULL ORDER BY Date DESC LIMIT 1'
        ).fetchone()
        if not row:
            continue

        date_val, wide_val = row

        # Check narrow
        narrow_row = conn.execute(
            f'SELECT {val_col} FROM {narrow} WHERE Ticker = ? AND Date = ?',
            (ticker, date_val)
        ).fetchone()

        if narrow_row is None:
            if verbose:
                print(f"    {ticker} @ {date_val}: MISSING in {narrow}")
            all_ok = False
        else:
            match = abs(float(narrow_row[0]) - float(wide_val)) < 0.01
            if verbose:
                status = "OK" if match else "MISMATCH"
                print(f"    {ticker} @ {date_val}: wide={wide_val}, narrow={narrow_row[0]} [{status}]")
            if not match:
                all_ok = False

    return all_ok


def main():
    print(f"Database: {DB_PATH}")
    print(f"File size: {os.path.getsize(DB_PATH) / 1024 / 1024:.1f} MB")

    conn = sqlite3.connect(DB_PATH)
    # Use WAL mode for better write performance
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")

    try:
        print("\nCreating narrow tables...")
        create_narrow_tables(conn)

        migrations = [
            ('stock_prices_daily', 'prices_long', 'Close'),
            ('stock_volumes_daily', 'volumes_long', 'Volume'),
            ('futures_prices_daily', 'futures_prices_long', 'Close'),
            ('futures_volumes_daily', 'futures_volumes_long', 'Volume'),
        ]

        total = 0
        for wide, narrow, val_col in migrations:
            total += migrate_table(conn, wide, narrow, val_col)

        print(f"\n  Total rows inserted: {total:,}")

        verify_migration(conn)

        # Final stats
        print("\n  Final table sizes:")
        for _, narrow, _ in migrations:
            try:
                count = conn.execute(f"SELECT COUNT(*) FROM {narrow}").fetchone()[0]
                tickers = conn.execute(f"SELECT COUNT(DISTINCT Ticker) FROM {narrow}").fetchone()[0]
                print(f"    {narrow}: {count:,} rows, {tickers} tickers")
            except sqlite3.OperationalError:
                pass

        new_size = os.path.getsize(DB_PATH) / 1024 / 1024
        print(f"\n  DB size after migration: {new_size:.1f} MB")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
