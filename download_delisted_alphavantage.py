#!/usr/bin/env python3
"""
Download historical data for delisted EV companies using Alpha Vantage API.
Requires Alpha Vantage API key (free tier available).

Get your free API key at: https://www.alphavantage.co/support/#api-key
"""
import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

import os
import sqlite3
import pandas as pd
from datetime import datetime
import time
import json
from constants import DB_PATH
CONFIG_FILE = '.alphavantage_config.json'

# Delisted EV tickers to download
DELISTED_TICKERS = {
    'FFIE': 'Faraday Future',
    'FSR': 'Fisker',
    'MULN': 'Mullen Automotive',
    'NKLA': 'Nikola',
    'RIDE': 'Lordstown Motors'
}

def get_api_key():
    """Get Alpha Vantage API key from env or config file."""
    # Try environment variable first (accept both names, prefer ALPHA_VANTAGE_API_KEY)
    api_key = os.environ.get('ALPHA_VANTAGE_API_KEY') or os.environ.get('ALPHAVANTAGE_API_KEY')
    if api_key:
        return api_key

    # Try config file
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                return config.get('api_key')
        except:
            pass

    # Prompt user
    print("\n" + "="*70)
    print("Alpha Vantage API Key Required")
    print("="*70)
    print("\nTo download delisted stock data, you need a free Alpha Vantage API key.")
    print("\nSteps:")
    print("1. Visit: https://www.alphavantage.co/support/#api-key")
    print("2. Enter your email to get a free API key")
    print("3. Copy the API key and paste it below\n")

    api_key = input("Enter your Alpha Vantage API key (or 'skip' to cancel): ").strip()

    if api_key.lower() == 'skip':
        return None

    # Save to config file
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump({'api_key': api_key}, f)
        print(f"\n✓ API key saved to {CONFIG_FILE}")
    except:
        print("\n⚠ Could not save API key to file, but will use it this session")

    return api_key

def download_alphavantage_data(ticker, api_key):
    """Download historical data from Alpha Vantage."""
    try:
        import requests

        url = f'https://www.alphavantage.co/query'
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': ticker,
            'outputsize': 'full',  # Get all available data
            'apikey': api_key
        }

        print(f'  Fetching from Alpha Vantage...')
        response = requests.get(url, params=params)
        data = response.json()

        # Check for errors
        if 'Error Message' in data:
            print(f'  ✗ Error: {data["Error Message"]}')
            return None

        if 'Note' in data:
            print(f'  ✗ Rate limit: {data["Note"]}')
            return None

        # Extract time series data
        time_series_key = 'Time Series (Daily)'
        if time_series_key not in data:
            print(f'  ✗ No data available')
            print(f'  Response keys: {list(data.keys())}')
            return None

        time_series = data[time_series_key]

        # Convert to DataFrame
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()

        # Rename columns (Alpha Vantage uses different names)
        df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

        # Convert to float
        df = df.astype(float)

        print(f'  ✓ Downloaded {len(df)} days')
        print(f'    Range: {df.index.min().date()} to {df.index.max().date()}')

        return df

    except ImportError:
        print(f'  ✗ Error: requests library not installed')
        print(f'    Install with: pip install requests')
        return None
    except Exception as e:
        print(f'  ✗ Error: {e}')
        return None

def save_to_database(ticker, df):
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

        if ticker not in columns:
            print(f'  Adding column {ticker}...')
            cursor.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{ticker}" REAL')
            conn.commit()

        # Insert/update data
        for date, row in df.iterrows():
            value = row['Close']
            date_str = str(date.date())

            # Try UPDATE first
            cursor.execute(f'''
                UPDATE stock_prices_daily
                SET "{ticker}" = ?
                WHERE DATE(Date) = ?
            ''', (value, date_str))

            if cursor.rowcount > 0:
                rows_updated += 1
            else:
                # INSERT new row
                cursor.execute(f'''
                    INSERT INTO stock_prices_daily (Date, "{ticker}")
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

def update_metadata(ticker, df, company_name):
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
        ''', (ticker, company_name, first_date, last_date, data_points))

        conn.commit()
        print(f'  ✓ Metadata updated')

    except sqlite3.Error as e:
        print(f'  ✗ Metadata error: {e}')
        conn.rollback()
    finally:
        conn.close()

def main():
    print("="*70)
    print("Alpha Vantage: Delisted EV Companies Data Download")
    print("="*70)

    # Get API key
    api_key = get_api_key()

    if not api_key:
        print("\n✗ No API key provided. Exiting.")
        print("\nGet a free API key at: https://www.alphavantage.co/support/#api-key")
        return

    print(f"\nDatabase: {DB_PATH}")
    print(f"Companies to download: {len(DELISTED_TICKERS)}\n")
    print("⚠ Note: Free API tier is limited to 5 requests/minute, 500/day")
    print("        This will take a few minutes...\n")

    total_rows = 0
    successful = 0

    for ticker, company_name in DELISTED_TICKERS.items():
        print(f"\n{ticker} ({company_name}):")

        # Download data
        df = download_alphavantage_data(ticker, api_key)

        if df is not None:
            # Save to database
            rows = save_to_database(ticker, df)
            total_rows += rows

            # Update metadata
            update_metadata(ticker, df, company_name)

            successful += 1

            # Wait to respect rate limit (5 requests/minute)
            if successful < len(DELISTED_TICKERS):
                print(f"\n  ⏳ Waiting 15 seconds (API rate limit)...")
                time.sleep(15)

    print("\n" + "="*70)
    print("Download Summary")
    print("="*70)
    print(f"\nSuccessful: {successful}/{len(DELISTED_TICKERS)} companies")
    print(f"Total rows: {total_rows}")

    if successful > 0:
        print("\n✓ Download complete!")
    else:
        print("\n✗ No data could be downloaded")

if __name__ == '__main__':
    main()
