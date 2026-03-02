#!/usr/bin/env python3
"""
Fill today's futures row with live/delayed quotes from yfinance.

These are provisional prices that get overwritten by the next
update_market_data.py run with official closing prices.

Usage:
    python scripts/fill_live_futures.py          # fill today
    python scripts/fill_live_futures.py --dry-run # show quotes without writing
"""
import argparse
import sqlite3
import os
import sys
from datetime import datetime, timezone

import yfinance as yf

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "market_data.db")
TABLE = "futures_prices_daily"


def get_futures_tickers(conn):
    """Get all ticker columns from the futures table."""
    cursor = conn.execute(f"PRAGMA table_info({TABLE})")
    return [row[1] for row in cursor.fetchall() if row[1] != "Date"]


def fetch_live_quotes(tickers):
    """Fetch last price for each ticker via yf.Ticker.fast_info."""
    quotes = {}
    for t in tickers:
        try:
            fi = yf.Ticker(t).fast_info
            price = fi.get("lastPrice") or fi.get("last_price")
            if price and price > 0:
                quotes[t] = float(price)
        except Exception:
            pass
    return quotes


def fill_row(conn, quotes, date_str, dry_run=False):
    """Insert or update today's row with live quotes."""
    # Check if row exists
    row = conn.execute(f"SELECT * FROM {TABLE} WHERE Date = ?", (date_str,)).fetchone()

    if row:
        # Update existing row — only fill NULLs or update all
        cols = [desc[0] for desc in conn.execute(f"SELECT * FROM {TABLE} LIMIT 0").description]
        col_idx = {name: i for i, name in enumerate(cols)}

        updates = []
        values = []
        for ticker, price in quotes.items():
            if ticker in col_idx:
                existing = row[col_idx[ticker]]
                if existing is None or existing != price:
                    updates.append(f'"{ticker}" = ?')
                    values.append(price)

        if updates and not dry_run:
            values.append(date_str)
            sql = f"UPDATE {TABLE} SET {', '.join(updates)} WHERE Date = ?"
            conn.execute(sql, values)
            conn.commit()
        return len(updates), "updated"
    else:
        # Insert new row
        if not dry_run:
            col_names = ', '.join(f'"{t}"' for t in quotes.keys())
            placeholders = ', '.join('?' for _ in quotes)
            sql = f'INSERT INTO {TABLE} (Date, {col_names}) VALUES (?, {placeholders})'
            conn.execute(sql, [date_str] + list(quotes.values()))
            conn.commit()
        return len(quotes), "inserted"


def main():
    parser = argparse.ArgumentParser(description="Fill live futures quotes into today's row")
    parser.add_argument("--dry-run", action="store_true", help="Show quotes without writing to DB")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)

    # Use YYYY-MM-DD HH:MM:SS format to match existing convention
    now_utc = datetime.now(timezone.utc)
    date_str = now_utc.strftime("%Y-%m-%d") + " 00:00:00"

    tickers = get_futures_tickers(conn)
    print(f"Fetching live quotes for {len(tickers)} futures contracts...")
    quotes = fetch_live_quotes(tickers)
    print(f"Got {len(quotes)} live quotes")

    if args.dry_run:
        for t, p in sorted(quotes.items()):
            print(f"  {t:8s}  {p:>12.2f}")
        print(f"\nWould write to date: {date_str}")
    else:
        count, action = fill_row(conn, quotes, date_str)
        print(f"{action.capitalize()} {count} prices for {date_str}")

    conn.close()


if __name__ == "__main__":
    main()
