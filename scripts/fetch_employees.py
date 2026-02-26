#!/usr/bin/env python3
"""Fetch historical employee counts from StockAnalysis.com and store in market_data.db."""

import argparse
import os
import re
import sqlite3
import sys
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "market_data.db")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Tickers that need non-standard StockAnalysis URLs
# Format: db_ticker -> (url_path_prefix, url_ticker)
TICKER_URL_MAP = {
    "BRK-B": ("stocks", "brk.b"),
    "ACA.PA": ("quote/epa", "aca"),
}


def get_url(ticker):
    """Build StockAnalysis employee page URL for a given ticker."""
    if ticker in TICKER_URL_MAP:
        prefix, slug = TICKER_URL_MAP[ticker]
        return f"https://stockanalysis.com/{prefix}/{slug}/employees/"
    return f"https://stockanalysis.com/stocks/{ticker.lower()}/employees/"


def parse_date(date_str):
    """Parse date string like 'Sep 27, 2025' to 'YYYY-MM-DD HH:MM:SS'."""
    try:
        dt = datetime.strptime(date_str.strip(), "%b %d, %Y")
        return dt.strftime("%Y-%m-%d 00:00:00")
    except ValueError:
        return None


def parse_employees(text):
    """Parse employee count string like '166,000' to integer."""
    text = text.strip().replace(",", "")
    try:
        return int(text)
    except ValueError:
        return None


def fetch_employee_data(ticker, delay=1.0):
    """Fetch employee history for a single ticker. Returns list of (date, count) tuples."""
    url = get_url(ticker)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code == 404:
            return None, "page not found"
        resp.raise_for_status()
    except requests.RequestException as e:
        return None, str(e)

    soup = BeautifulSoup(resp.text, "html.parser")
    table = soup.find("table")
    if not table:
        return None, "no table found"

    rows = table.find_all("tr")
    results = []
    for row in rows[1:]:  # skip header
        cells = row.find_all("td")
        if len(cells) < 2:
            continue
        date_str = cells[0].text.strip()
        emp_str = cells[1].text.strip()
        date = parse_date(date_str)
        count = parse_employees(emp_str)
        if date and count:
            results.append((date, count))

    if delay > 0:
        time.sleep(delay)

    return results, None


def store_employee_data(conn, ticker, records):
    """Insert employee records, skipping duplicates."""
    inserted = 0
    for date, count in records:
        existing = conn.execute(
            "SELECT 1 FROM employee_count WHERE ticker = ? AND fiscal_date_ending = ?",
            (ticker, date),
        ).fetchone()
        if existing:
            continue
        conn.execute(
            "INSERT INTO employee_count (ticker, fiscal_date_ending, employees, last_updated) VALUES (?, ?, ?, ?)",
            (ticker, date, count, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        inserted += 1
    conn.commit()
    return inserted


def main():
    parser = argparse.ArgumentParser(description="Fetch employee counts from StockAnalysis.com")
    parser.add_argument("tickers", nargs="*", help="Tickers to fetch (default: all with fundamentals)")
    parser.add_argument("--all-fundamentals", action="store_true", help="Fetch for all tickers with fundamentals data")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between requests in seconds (default: 1.0)")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and display but don't store")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)

    if args.all_fundamentals:
        tickers = [
            r[0]
            for r in conn.execute(
                "SELECT DISTINCT ticker FROM income_statement_annual ORDER BY ticker"
            ).fetchall()
        ]
    elif args.tickers:
        tickers = args.tickers
    else:
        parser.error("Provide tickers or use --all-fundamentals")

    # Skip tickers that already have data
    existing = set()
    for row in conn.execute("SELECT DISTINCT ticker FROM employee_count").fetchall():
        existing.add(row[0])

    to_fetch = [t for t in tickers if t not in existing]
    already = [t for t in tickers if t in existing]

    if already:
        print(f"Skipping {len(already)} tickers with existing data: {', '.join(already)}")

    print(f"Fetching employee data for {len(to_fetch)} tickers...")
    print()

    success = 0
    failed = []
    for i, ticker in enumerate(to_fetch, 1):
        print(f"[{i}/{len(to_fetch)}] {ticker}...", end=" ", flush=True)
        records, error = fetch_employee_data(ticker, delay=args.delay)

        if error:
            print(f"FAILED ({error})")
            failed.append((ticker, error))
            continue

        if not records:
            print("no data")
            failed.append((ticker, "empty table"))
            continue

        if args.dry_run:
            print(f"{len(records)} records (dry run)")
            for date, count in records[:3]:
                print(f"  {date}: {count:,}")
            if len(records) > 3:
                print(f"  ... and {len(records) - 3} more")
        else:
            inserted = store_employee_data(conn, ticker, records)
            print(f"{len(records)} records ({inserted} new)")
            success += 1

    print()
    print(f"Done. {success} tickers populated, {len(failed)} failed.")
    if failed:
        print("Failed tickers:")
        for ticker, error in failed:
            print(f"  {ticker}: {error}")

    conn.close()


if __name__ == "__main__":
    main()
