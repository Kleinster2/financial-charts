#!/usr/bin/env python
"""
fetch_b3_yield_curve.py - Fetch Brazil DI yield curve from B3

Downloads the PRE (DI x pre-fixed) yield curve from B3's public-data hub.
Historical data available from April 22, 2002.

Usage:
    python fetch_b3_yield_curve.py                  # Fetch last 30 days
    python fetch_b3_yield_curve.py --days 365      # Fetch last year
    python fetch_b3_yield_curve.py --start 2024-01-01 --end 2024-12-31
"""

import os
import sys
from io import BytesIO
from zipfile import BadZipFile, ZipFile
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import time
import argparse
import requests
from constants import DB_PATH
from brazil_rate_series_registry import B3_DI_SERIES

# Narrow-format dual-write
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'charting_app'))
try:
    from sqlite_queries import upsert_prices_long, check_narrow_available
    NARROW_SYNC = check_narrow_available()
except ImportError:
    NARROW_SYNC = False
from http_utils import FetchError
B3_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}
B3_TAXASWAP_URL = "https://www.b3.com.br/pesquisapregao/download"
B3_TAXASWAP_CURVE_CODE = "T1PRE"  # DIxPRE, replacement for the legacy PRE curve.
B3_COLUMNS = list(B3_DI_SERIES.keys())


def _fetch_binary_with_retry(url, params=None, retries=3, backoff=2.0, timeout=30.0, headers=None):
    """Fetch binary content with the same retry semantics used by http_utils."""
    last_exc = None
    last_status = None
    last_kind = "unknown"

    for attempt in range(retries + 1):
        try:
            resp = requests.get(url, params=params, headers=headers, timeout=timeout)
            last_status = resp.status_code

            if 200 <= resp.status_code < 300:
                return resp.content

            if resp.status_code == 404:
                return b""

            if resp.status_code == 429 or resp.status_code >= 500:
                last_kind = "server"
                raise requests.HTTPError(f"HTTP {resp.status_code}", response=resp)

            last_kind = "client"
            resp.raise_for_status()

        except requests.Timeout as e:
            last_kind, last_exc = "timeout", e
        except requests.HTTPError as e:
            last_exc = e
        except requests.RequestException as e:
            last_kind, last_exc = "network", e

        if attempt < retries:
            time.sleep(backoff**attempt)

    raise FetchError(url, params=params, kind=last_kind, status_code=last_status, last_exc=last_exc)


def _zip_members_from_payload(data):
    """Yield (name, bytes) from a zip archive, including PKSFX-style embedded zips."""
    offset = 0
    while True:
        pos = data.find(b"PK\x03\x04", offset)
        if pos < 0:
            return

        try:
            with ZipFile(BytesIO(data[pos:])) as zf:
                for name in zf.namelist():
                    yield name, zf.read(name)
                return
        except BadZipFile:
            offset = pos + 4


def extract_taxaswap_text(payload):
    """Extract TaxaSwap.txt from B3's nested zip/self-extracting payload."""
    queue = [payload]

    for _ in range(4):
        next_queue = []
        for item in queue:
            for name, member in _zip_members_from_payload(item):
                if name.lower().endswith(".txt"):
                    return member.decode("latin1")
                next_queue.append(member)
        queue = next_queue

    return None


def parse_taxaswap_rates(text, curve_code=B3_TAXASWAP_CURVE_CODE):
    """Parse B3 TaxaSwap fixed-width rows into {business_days: annual_rate_pct}."""
    rates = {}

    for line in text.splitlines():
        if len(line) < 72:
            continue

        code = line[19:24].strip()
        if code != curve_code:
            continue

        try:
            business_days = int(line[46:51])
            sign = -1 if line[51] == "-" else 1
            rate = sign * int(line[52:66]) / 10_000_000
        except ValueError:
            continue

        rates[business_days] = rate

    return rates


def fetch_b3_yield_curve(date):
    """
    Fetch B3 PRE yield curve for a specific date.

    Args:
        date: datetime object or string (YYYY-MM-DD)

    Returns:
        dict mapping days to rates, or None if no data
    """
    if isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d')

    date_str = date.strftime('%d/%m/%Y')
    file_name = f"TS{date:%y%m%d}.ex_"

    try:
        payload = _fetch_binary_with_retry(
            B3_TAXASWAP_URL,
            params={"filelist": file_name},
            retries=3,
            backoff=2.0,
            timeout=30.0,
            headers=B3_HEADERS,
        )

        if not payload or len(payload) <= 22:
            return None

        taxaswap_text = extract_taxaswap_text(payload)
        if not taxaswap_text:
            print(f"  Parse failed {date_str}: {file_name} had no TaxaSwap.txt payload")
            return None

        rates = parse_taxaswap_rates(taxaswap_text)
        if not rates:
            print(f"  Parse failed {date_str}: TaxaSwap.txt had no {B3_TAXASWAP_CURVE_CODE} rows")
            return None

        return rates

    except FetchError as e:
        print(f"  FetchError {date_str}: {e.kind} - {str(e)[:80]}")
        return None
    except Exception as e:
        print(f"  Error fetching {date_str}: {e}")
        return None


def get_tenor_rate(rates, target_days):
    """Get rate for closest available tenor."""
    if not rates:
        return None
    closest = min(rates.keys(), key=lambda x: abs(x - target_days))
    # Only accept if within 10% of target
    if abs(closest - target_days) / target_days < 0.1:
        return rates[closest]
    return None


def fetch_historical_curves(start_date, end_date, verbose=True):
    """
    Fetch historical yield curves for a date range.

    Args:
        start_date: Start date (datetime or string YYYY-MM-DD)
        end_date: End date (datetime or string YYYY-MM-DD)
        verbose: Print progress

    Returns:
        DataFrame with Date index and tenor columns
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Standard tenors (business days)
    tenors = {
        'B3_DI_1M': 21,
        'B3_DI_3M': 63,
        'B3_DI_6M': 126,
        'B3_DI_1Y': 252,
        'B3_DI_2Y': 504,
        'B3_DI_5Y': 1260,
        'B3_DI_10Y': 2520,
    }

    results = []
    current = start_date
    total_days = (end_date - start_date).days + 1
    fetched = 0

    if verbose:
        print(f"Fetching B3 yield curves from {start_date.date()} to {end_date.date()}...")

    while current <= end_date:
        # Skip weekends
        if current.weekday() < 5:
            rates = fetch_b3_yield_curve(current)

            if rates:
                row = {'Date': current.date()}
                for name, days in tenors.items():
                    row[name] = get_tenor_rate(rates, days)
                results.append(row)
                fetched += 1

                if verbose and fetched % 10 == 0:
                    print(f"  Fetched {fetched} days...")

            # Rate limit - be nice to B3's server
            time.sleep(0.5)

        current += timedelta(days=1)

    if not results:
        return pd.DataFrame()

    df = pd.DataFrame(results)
    df.set_index('Date', inplace=True)

    if verbose:
        print(f"  Total: {len(df)} trading days with data")

    return df


def update_database(df, verbose=True):
    """Update database with B3 yield curve data using safe SQL UPDATEs.

    SAFETY: This function uses individual UPDATE statements instead of
    replacing the entire table, preventing accidental data loss.
    """
    if df.empty:
        if verbose:
            print("No data to update.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if table exists and has data
    cursor.execute("SELECT COUNT(*) FROM stock_prices_daily")
    existing_count = cursor.fetchone()[0]
    if verbose:
        print(f"Existing data: {existing_count} rows")

    if existing_count == 0:
        if verbose:
            print("WARNING: Table is empty. Cannot update B3 columns without existing date rows.")
            print("Run stock price update first to populate date rows.")
        conn.close()
        return

    # Get existing columns
    cursor.execute("PRAGMA table_info(stock_prices_daily)")
    existing_cols = {row[1] for row in cursor.fetchall()}

    # Add B3 columns if they don't exist
    b3_columns = B3_COLUMNS + ['BCB_CDI']
    for col in b3_columns:
        if col not in existing_cols:
            cursor.execute(f"ALTER TABLE stock_prices_daily ADD COLUMN [{col}] REAL")
            if verbose:
                print(f"  Added column: {col}")

    conn.commit()

    # SAFETY: Only update data from the last 60 days to protect cleaned historical data
    # Historical B3 DI data (2003-present) has been manually cleaned and should not be overwritten
    cutoff_date = (datetime.now() - timedelta(days=60)).strftime('%Y-%m-%d')

    # Update B3 values using individual UPDATE statements
    updated_count = 0
    skipped_historical = 0
    for date_idx, row in df.iterrows():
        date_str = pd.Timestamp(date_idx).strftime('%Y-%m-%d')

        # Protect historical data - only update recent dates
        if date_str < cutoff_date:
            skipped_historical += 1
            continue

        for col in df.columns:
            if col in b3_columns and pd.notna(row[col]):
                value = float(row[col])
                # Update only if date exists in table
                # Handle both date formats: "2025-12-09" and "2025-12-09 00:00:00"
                cursor.execute(f'''
                    UPDATE stock_prices_daily
                    SET [{col}] = ?
                    WHERE (Date = ? OR Date = ? || ' 00:00:00')
                      AND ([{col}] IS NULL OR [{col}] != ?)
                ''', (value, date_str, date_str, value))
                if cursor.rowcount > 0:
                    updated_count += cursor.rowcount

    if skipped_historical > 0 and verbose:
        print(f"  Skipped {skipped_historical} historical dates (protected, older than 60 days)")

    conn.commit()

    # Sync B3 columns to narrow-format table
    if NARROW_SYNC:
        try:
            rows = []
            for date_idx, row in df.iterrows():
                date_str = pd.Timestamp(date_idx).strftime('%Y-%m-%d') + ' 00:00:00'
                for col in b3_columns:
                    if col in df.columns and pd.notna(row.get(col)):
                        rows.append({'Date': date_str, 'Ticker': col, 'Close': float(row[col])})
            if rows:
                upsert_prices_long(pd.DataFrame(rows), verbose=verbose)
                for ticker, name in B3_DI_SERIES.items():
                    meta_row = conn.execute(
                        """
                        SELECT MIN(Date), MAX(Date), COUNT(*)
                        FROM prices_long
                        WHERE Ticker = ? AND Close IS NOT NULL
                        """,
                        (ticker,),
                    ).fetchone()
                    if meta_row and meta_row[0]:
                        conn.execute(
                            """
                            INSERT INTO ticker_metadata
                                (ticker, name, table_name, data_type, first_date, last_date, data_points)
                            VALUES (?, ?, 'prices_long', 'macro', ?, ?, ?)
                            ON CONFLICT(ticker) DO UPDATE SET
                                name = excluded.name,
                                table_name = excluded.table_name,
                                data_type = excluded.data_type,
                                first_date = excluded.first_date,
                                last_date = excluded.last_date,
                                data_points = excluded.data_points
                            """,
                            (ticker, name, meta_row[0], meta_row[1], meta_row[2]),
                        )
                conn.commit()
        except Exception as e:
            if verbose:
                print(f"  [Narrow] Warning: sync failed: {e}")

    conn.close()

    if verbose:
        print(f"Updated {updated_count} values in database")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch B3 DI yield curve')
    parser.add_argument('--start', type=str, help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end', type=str, help='End date (YYYY-MM-DD)')
    parser.add_argument('--days', type=int, default=30, help='Days to look back (default: 30)')
    parser.add_argument('--dry-run', action='store_true', help='Show data without updating database')
    args = parser.parse_args()

    # Determine date range
    if args.start and args.end:
        start_date = args.start
        end_date = args.end
    else:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=args.days)

    # Fetch data
    df = fetch_historical_curves(start_date, end_date)

    if df.empty:
        print("No data fetched.")
    else:
        print(f"\nSample data (last 5 days):")
        print(df.tail().round(2))

        if not args.dry_run:
            update_database(df)
            print("\nDatabase updated with B3 yield curve data.")
        else:
            print("\nDry run - database not updated.")
