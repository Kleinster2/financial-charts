#!/usr/bin/env python3
"""
Summarize DB coverage for given tickers in stock_prices_daily.

Usage:
  python scripts/db_summary.py --tickers ^BXMD,^PUT,^VVIX
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
import os
from typing import List

# Allow importing constants from repo root when run from anywhere
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)
from constants import DB_PATH  # type: ignore


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Summarize DB ranges for tickers")
    p.add_argument("--tickers", type=str, required=True, help="Comma-separated list of tickers")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    tickers: List[str] = [t.strip() for t in args.tickers.split(",") if t.strip()]

    print(f"DB: {DB_PATH}")
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    # Ensure table exists
    cur.execute("CREATE TABLE IF NOT EXISTS stock_prices_daily (Date TEXT PRIMARY KEY)")

    for s in tickers:
        try:
            # Ensure column exists (no-op if present)
            try:
                cur.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{s}" REAL')
            except sqlite3.OperationalError:
                pass
            q = f'SELECT date(min(Date)), date(max(Date)), COUNT(1) FROM stock_prices_daily WHERE "{s}" IS NOT NULL'
            mn, mx, cnt = cur.execute(q).fetchone()
            print(f"{s}: {mn} -> {mx}, rows={cnt}")
        except Exception as e:
            print(f"{s}: ERROR: {e}")

    con.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
