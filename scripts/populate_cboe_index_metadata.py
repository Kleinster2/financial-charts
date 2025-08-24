#!/usr/bin/env python3
"""
Populate/refresh metadata for Cboe indices in ticker_metadata so the UI shows
friendly names instead of raw tickers.

Usage:
  python -u scripts/populate_cboe_index_metadata.py [--tickers ^BXMD,^PUT,...]

Notes:
- Only tickers that already exist as columns in stock_prices_daily are processed.
- Upserts into ticker_metadata with data_type='index' and table_name='stock_prices_daily'.
- Fills first_date, last_date, data_points from the prices table.
"""
from __future__ import annotations

import argparse
import os
import sqlite3
from typing import Dict, List

from constants import DB_PATH, get_db_connection

# Canonical names from Cboe dashboards
CBOE_INDEX_NAMES: Dict[str, str] = {
    "^BXM": "Cboe S&P 500 BuyWrite Index",
    "^BXY": "Cboe S&P 500 2% OTM BuyWrite Index",
    "^BXMD": "Cboe S&P 500 30-Delta BuyWrite Index",
    "^PUT": "Cboe S&P 500 PutWrite Index",
    "^PPUT": "Cboe S&P 500 5% OTM PutWrite Index",
    "^VVIX": "Cboe VVIX Index",
    "^VIX1D": "Cboe 1-Day Volatility Index",
    "^VIX3M": "Cboe 3-Month Volatility Index",
    "^VIX9D": "Cboe 9-Day Volatility Index",
    "^VIX6M": "Cboe 6-Month Volatility Index",
    "^VXN": "Cboe Nasdaq-100 Volatility Index",
    "^VXD": "Cboe DJIA Volatility Index",
    "^RVX": "Cboe Russell 2000 Volatility Index",
    "^SKEW": "Cboe SKEW Index",
}

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS ticker_metadata (
    ticker TEXT PRIMARY KEY,
    name TEXT,
    table_name TEXT NOT NULL,
    data_type TEXT NOT NULL,  -- e.g. 'stock', 'etf', 'future', 'fx', 'crypto', 'index'
    exchange TEXT,
    sector TEXT,
    industry TEXT,
    first_date DATE,
    last_date DATE,
    data_points INTEGER,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT 1,
    notes TEXT
)
"""


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Populate Cboe index metadata")
    p.add_argument(
        "--tickers",
        type=str,
        help="Comma-separated list of tickers to process; default uses known Cboe indices present in DB",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()

    print("=== Populating Cboe index metadata ===")
    print(f"Using database: {DB_PATH}")
    if not os.path.exists(DB_PATH):
        print(f"Database not found: {DB_PATH}")
        return 1

    conn = get_db_connection()
    cur = conn.cursor()

    # Ensure table exists
    cur.execute(CREATE_TABLE_SQL)
    conn.commit()

    # Discover which tickers exist in prices table
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_prices_daily'")
    if not cur.fetchone():
        print("stock_prices_daily not found; nothing to do.")
        conn.close()
        return 0

    cur.execute("PRAGMA table_info(stock_prices_daily)")
    price_columns = {row[1] for row in cur.fetchall()}
    price_columns.discard("Date")
    print(f"Found {len(price_columns)} price columns.")

    # Determine targets
    if args.tickers:
        requested: List[str] = [t.strip() for t in args.tickers.split(",") if t.strip()]
    else:
        requested = list(CBOE_INDEX_NAMES.keys())

    targets = [t for t in requested if t in price_columns]
    skipped_missing_price = [t for t in requested if t not in price_columns]

    print(f"Will process {len(targets)} tickers; skipping {len(skipped_missing_price)} not in prices table.")
    if skipped_missing_price:
        print("Skipped (not in stock_prices_daily):", ", ".join(sorted(skipped_missing_price)))

    inserted = 0
    updated = 0

    for ticker in sorted(targets):
        name = CBOE_INDEX_NAMES.get(ticker) or ticker

        # Range & count from prices table
        cur.execute(
            f"""
            SELECT MIN(Date) as first_date,
                   MAX(Date) as last_date,
                   COUNT(*) as data_points
            FROM stock_prices_daily
            WHERE "{ticker}" IS NOT NULL
            """
        )
        first_date, last_date, data_points = cur.fetchone()
        if not data_points or data_points <= 0:
            print(f"No data points for {ticker}; skipping.")
            continue

        # Upsert
        cur.execute("SELECT ticker FROM ticker_metadata WHERE ticker = ?", (ticker,))
        exists = cur.fetchone() is not None

        if not exists:
            cur.execute(
                """
                INSERT INTO ticker_metadata
                    (ticker, name, table_name, data_type, exchange, first_date, last_date, data_points, notes)
                VALUES (?, ?, 'stock_prices_daily', 'index', 'Cboe', ?, ?, ?, 'Source: Cboe CSV / index')
                """,
                (ticker, name, first_date, last_date, data_points),
            )
            inserted += 1
            print(f"Inserted {ticker}: {name}")
        else:
            cur.execute(
                """
                UPDATE ticker_metadata
                   SET name = ?,
                       table_name = 'stock_prices_daily',
                       data_type = 'index',
                       exchange = COALESCE(exchange, 'Cboe'),
                       first_date = ?,
                       last_date = ?,
                       data_points = ?,
                       active = 1
                 WHERE ticker = ?
                """,
                (name, first_date, last_date, data_points, ticker),
            )
            updated += 1
            print(f"Updated {ticker}: {name}")

    conn.commit()

    print("\n=== Summary ===")
    print(f"Inserted: {inserted}")
    print(f"Updated: {updated}")
    print(f"Total affected: {inserted + updated}")

    # Verify a small sample
    sample = sorted(targets)[:10]
    if sample:
        qmarks = ",".join(["?"] * len(sample))
        print("\nVerifying sample:")
        cur.execute(
            f"SELECT ticker, name, data_type, first_date, last_date, data_points FROM ticker_metadata WHERE ticker IN ({qmarks}) ORDER BY ticker",
            sample,
        )
        for t, n, dt, fd, ld, cnt in cur.fetchall():
            print(f"  {t}: {n}  [{dt}]  range={fd}..{ld} rows={cnt}")

    conn.close()
    print("\n✓ Cboe index metadata population complete!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
