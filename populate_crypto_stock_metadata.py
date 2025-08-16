"""
Populate proper company names for crypto-exposed equities into ticker_metadata
so frontend chip tooltips show friendly names instead of raw tickers.

Usage:
    python -u populate_crypto_stock_metadata.py

Notes:
- This script updates/insert rows in ticker_metadata with data_type='stock'.
- It only processes tickers that already exist in stock_prices_daily.
- It preserves date ranges by querying stock_prices_daily for each ticker.
"""
from __future__ import annotations

import os
import sqlite3
from typing import Dict

DB_PATH = "sp500_data.db"

CRYPTO_STOCK_NAMES: Dict[str, str] = {
    # Exchanges / software
    "COIN": "Coinbase Global, Inc.",
    "MSTR": "MicroStrategy Incorporated",
    "BKKT": "Bakkt Holdings, Inc.",
    # Miners & infrastructure
    "RIOT": "Riot Platforms, Inc.",
    "MARA": "Marathon Digital Holdings, Inc.",
    "HUT": "Hut 8 Corp.",
    "HIVE": "HIVE Digital Technologies Ltd.",
    "BITF": "Bitfarms Ltd.",
    "CIFR": "Cipher Mining Inc.",
    "CORZ": "Core Scientific, Inc.",
    "IREN": "Iris Energy Limited",
    "WULF": "TeraWulf Inc.",
    "CLSK": "CleanSpark, Inc.",
    "BTBT": "Bit Digital, Inc.",
    "SDIG": "Stronghold Digital Mining, Inc.",
    "CAN": "Canaan Inc.",
}

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS ticker_metadata (
    ticker TEXT PRIMARY KEY,
    name TEXT,
    table_name TEXT NOT NULL,
    data_type TEXT NOT NULL,  -- 'stock', 'etf', 'future', 'fx', 'crypto'
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


def main() -> None:
    print("=== Populating crypto-exposed stock metadata ===")

    if not os.path.exists(DB_PATH):
        print(f"Database not found: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Ensure table exists (no-op if already created by optimizer)
    cur.execute(CREATE_TABLE_SQL)
    conn.commit()

    # Discover which tickers actually exist in prices table
    print("\n1) Inspecting stock_prices_daily columns…")
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_prices_daily'")
    if not cur.fetchone():
        print("stock_prices_daily not found; nothing to do.")
        conn.close()
        return

    cur.execute("PRAGMA table_info(stock_prices_daily)")
    price_columns = {row[1] for row in cur.fetchall()}  # set of column names
    price_columns.discard('Date')
    print(f"Found {len(price_columns)} price columns.")

    # Prepare run
    to_process = [t for t in CRYPTO_STOCK_NAMES.keys() if t in price_columns]
    skipped = [t for t in CRYPTO_STOCK_NAMES.keys() if t not in price_columns]

    print(f"\n2) Will process {len(to_process)} tickers present in DB; skipping {len(skipped)} not found in prices table.")
    if skipped:
        print("Skipped (not in stock_prices_daily):", ", ".join(sorted(skipped)))

    updated = 0
    inserted = 0

    for ticker in sorted(to_process):
        name = CRYPTO_STOCK_NAMES[ticker]

        # Check if metadata row exists
        cur.execute("SELECT ticker FROM ticker_metadata WHERE ticker = ?", (ticker,))
        exists = cur.fetchone() is not None

        # Gather date range & count from prices table for this ticker
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

        if not exists:
            if data_points and data_points > 0:
                cur.execute(
                    """
                    INSERT INTO ticker_metadata
                        (ticker, name, table_name, data_type, first_date, last_date, data_points)
                    VALUES (?, ?, 'stock_prices_daily', 'stock', ?, ?, ?)
                    """,
                    (ticker, name, first_date, last_date, data_points),
                )
                inserted += 1
                print(f"Inserted {ticker}: {name}")
            else:
                print(f"No data points for {ticker}; skipping insert.")
        else:
            # Update name (and mark as stock); keep existing range & counts intact
            cur.execute(
                """
                UPDATE ticker_metadata
                   SET name = ?, data_type = 'stock', table_name = 'stock_prices_daily'
                 WHERE ticker = ?
                """,
                (name, ticker),
            )
            updated += 1
            print(f"Updated {ticker}: {name}")

    conn.commit()

    print("\n=== Summary ===")
    print(f"Inserted: {inserted}")
    print(f"Updated: {updated}")
    print(f"Total affected: {inserted + updated}")

    # Verify a small sample
    sample = sorted(to_process)[:10]
    if sample:
        qmarks = ",".join(["?"] * len(sample))
        print("\n3) Verifying sample:")
        cur.execute(
            f"SELECT ticker, name, data_type FROM ticker_metadata WHERE ticker IN ({qmarks}) ORDER BY ticker",
            sample,
        )
        for t, n, dt in cur.fetchall():
            print(f"  {t}: {n}  [{dt}]")

    conn.close()
    print("\n✓ Crypto stock metadata population complete!")


if __name__ == "__main__":
    main()
