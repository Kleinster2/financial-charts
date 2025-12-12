#!/usr/bin/env python3
"""
Download historical data for delisted EV companies.
Tries multiple ticker variants including OTC symbols.
"""
import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

import sqlite3
import yfinance as yf
import pandas as pd
from datetime import datetime
from constants import DB_PATH

# Map of desired ticker -> possible variants to try
DELISTED_EV_TICKERS = {
    'ARVL': ['ARVLF', 'ARVL'],  # Arrival - OTC
    'FFIE': ['FFIE', 'FFIEF'],  # Faraday Future
    'FSR': ['FSRN', 'FSR', 'FSRNF'],  # Fisker
    'MULN': ['MULN', 'MULNF'],  # Mullen
    'NKLA': ['NKLA'],  # Nikola (might still be active)
    'RIDE': ['RIDE', 'RIDEF']  # Lordstown Motors
}

def find_best_ticker(original, variants):
    """Try each variant and return the one with data."""
    for ticker in variants:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period='max')

            if not hist.empty:
                print(f'  ✓ Found data: {ticker} ({len(hist)} days)')
                return ticker, hist
        except Exception as e:
            pass

    print(f'  ✗ No data found')
    return None, None

def save_to_database(original_ticker, actual_ticker, df):
    """Save ticker data to stock_prices_daily table."""
    if df is None or df.empty:
        return 0

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    rows_updated = 0
    rows_inserted = 0

    try:
        # Check if column exists
        cursor.execute("PRAGMA table_info(stock_prices_daily)")
        columns = {row[1] for row in cursor.fetchall()}

        # Use original ticker as column name (ARVL not ARVLF)
        column_name = original_ticker

        if column_name not in columns:
            print(f'  Adding column {column_name}...')
            cursor.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{column_name}" REAL')
            conn.commit()

        # Insert/update data
        for date, row in df.iterrows():
            value = row['Close']
            date_str = str(date.date())

            # Try UPDATE first
            cursor.execute(f'''
                UPDATE stock_prices_daily
                SET "{column_name}" = ?
                WHERE DATE(Date) = ?
            ''', (value, date_str))

            if cursor.rowcount > 0:
                rows_updated += 1
            else:
                # INSERT new row
                cursor.execute(f'''
                    INSERT INTO stock_prices_daily (Date, "{column_name}")
                    VALUES (?, ?)
                ''', (date_str, value))
                rows_inserted += 1

        conn.commit()
        print(f'  ✓ Database: {rows_updated} updated, {rows_inserted} inserted')

        return rows_updated + rows_inserted

    except sqlite3.Error as e:
        print(f'  ✗ Database error: {e}')
        conn.rollback()
        return 0
    finally:
        conn.close()

def update_metadata(original_ticker, actual_ticker, df, company_name):
    """Update ticker_metadata table."""
    if df is None or df.empty:
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        first_date = str(df.index.min().date())
        last_date = str(df.index.max().date())
        data_points = len(df)

        cursor.execute('''
            INSERT OR REPLACE INTO ticker_metadata
            (ticker, name, table_name, data_type, first_date, last_date, data_points)
            VALUES (?, ?, 'stock_prices_daily', 'equity', ?, ?, ?)
        ''', (original_ticker, company_name, first_date, last_date, data_points))

        conn.commit()
        print(f'  ✓ Metadata updated')

    except sqlite3.Error as e:
        print(f'  ✗ Metadata error: {e}')
        conn.rollback()
    finally:
        conn.close()

def main():
    print("="*70)
    print("Delisted EV Companies Historical Data Download")
    print("="*70)
    print(f"\nDatabase: {DB_PATH}")
    print(f"Companies to download: {len(DELISTED_EV_TICKERS)}\n")

    company_names = {
        'ARVL': 'Arrival',
        'FFIE': 'Faraday Future',
        'FSR': 'Fisker',
        'MULN': 'Mullen Automotive',
        'NKLA': 'Nikola',
        'RIDE': 'Lordstown Motors'
    }

    total_rows = 0
    successful = 0

    for original, variants in DELISTED_EV_TICKERS.items():
        print(f"\n{original} ({company_names[original]}):")

        # Find working ticker
        actual_ticker, hist = find_best_ticker(original, variants)

        if hist is not None:
            print(f'  Range: {hist.index.min().date()} to {hist.index.max().date()}')
            print(f'  Last price: ${hist["Close"].iloc[-1]:.4f}')

            # Save to database using original ticker name
            rows = save_to_database(original, actual_ticker, hist[['Close']])
            total_rows += rows

            # Update metadata
            update_metadata(original, actual_ticker, hist, company_names[original])

            successful += 1

    print("\n" + "="*70)
    print("Download Summary")
    print("="*70)
    print(f"\nSuccessful: {successful}/{len(DELISTED_EV_TICKERS)} companies")
    print(f"Total rows: {total_rows}")

    if successful > 0:
        print("\n✓ Download complete!")
    else:
        print("\n✗ No data could be downloaded")

if __name__ == '__main__':
    main()
