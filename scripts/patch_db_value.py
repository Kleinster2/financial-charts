#!/usr/bin/env python3
"""
Patch a single value in the SQLite time-series table `stock_prices_daily`.

Usage examples:
  python scripts/patch_db_value.py --ticker ^VXD --date 2021-07-13 --value 15.19
  python scripts/patch_db_value.py --ticker ^VXD --date 2021-07-13 --interpolate

Options:
  --ticker        Ticker symbol, e.g. ^VXD
  --date          Date in YYYY-MM-DD
  --value         Explicit float value to set
  --interpolate   Compute value as the average of previous and next non-null values
  --dry-run       Show intended change without writing

The script uses DB path from constants.get_db_connection().
"""
from __future__ import annotations

import argparse
import sqlite3
from typing import Optional, Tuple

from constants import get_db_connection, DB_PATH


def get_neighbor_values(conn: sqlite3.Connection, ticker: str, date: str) -> Tuple[Optional[float], Optional[float]]:
    cur = conn.cursor()
    prev_row = cur.execute(
        f'SELECT "{ticker}" FROM stock_prices_daily WHERE Date < ? AND "{ticker}" IS NOT NULL ORDER BY Date DESC LIMIT 1',
        (date,)
    ).fetchone()
    next_row = cur.execute(
        f'SELECT "{ticker}" FROM stock_prices_daily WHERE Date > ? AND "{ticker}" IS NOT NULL ORDER BY Date ASC LIMIT 1',
        (date,)
    ).fetchone()
    prev_val = prev_row[0] if prev_row else None
    next_val = next_row[0] if next_row else None
    return prev_val, next_val


def ensure_row_and_column(conn: sqlite3.Connection, ticker: str, date: str) -> None:
    cur = conn.cursor()
    # Ensure base table exists
    cur.execute("CREATE TABLE IF NOT EXISTS stock_prices_daily (Date TEXT PRIMARY KEY)")
    # Ensure ticker column exists
    try:
        cur.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{ticker}" REAL')
    except sqlite3.OperationalError:
        pass
    # Ensure the date row exists
    cur.execute("INSERT OR IGNORE INTO stock_prices_daily (Date) VALUES (?)", (date,))


def main():
    ap = argparse.ArgumentParser(description="Patch a single value in stock_prices_daily")
    ap.add_argument('--ticker', required=True, help='Ticker symbol, e.g. ^VXD')
    ap.add_argument('--date', required=True, help='YYYY-MM-DD')
    ap.add_argument('--value', type=float, default=None, help='Explicit value to set')
    ap.add_argument('--interpolate', action='store_true', help='Average of previous and next non-null values')
    ap.add_argument('--dry-run', action='store_true', help='Show intended change without writing')
    args = ap.parse_args()

    ticker = args.ticker.upper()
    date = args.date

    if args.value is None and not args.interpolate:
        ap.error('Specify --value or --interpolate')

    print(f"Using database: {DB_PATH}")
    conn = get_db_connection(row_factory=None)
    try:
        cur = conn.cursor()
        # Current value
        row = cur.execute(f'SELECT "{ticker}" FROM stock_prices_daily WHERE Date = ?', (date,)).fetchone()
        current = row[0] if row else None
        print(f"Current {ticker} @ {date}: {current}")

        if args.interpolate and args.value is None:
            prev_val, next_val = get_neighbor_values(conn, ticker, date)
            print(f"Neighbor values -> prev: {prev_val}, next: {next_val}")
            if prev_val is None or next_val is None:
                raise SystemExit('Cannot interpolate: missing neighbor values')
            new_val = (prev_val + next_val) / 2.0
        else:
            new_val = float(args.value)

        print(f"New value -> {ticker} @ {date}: {new_val}")

        if args.dry_run:
            print('Dry run only. No changes written.')
            return

        ensure_row_and_column(conn, ticker, date)
        cur.execute(f'UPDATE stock_prices_daily SET "{ticker}" = ? WHERE Date = ?', (new_val, date))
        conn.commit()

        row2 = cur.execute(f'SELECT "{ticker}" FROM stock_prices_daily WHERE Date = ?', (date,)).fetchone()
        print(f"Updated {ticker} @ {date}: {row2[0] if row2 else None}")
    finally:
        conn.close()


if __name__ == '__main__':
    main()
