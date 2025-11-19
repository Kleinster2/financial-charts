#!/usr/bin/env python3
"""
Add Ticker to Database

Standardized script for adding new tickers to the database with:
- Full historical price data download
- Metadata with cleaned company names (no corporate suffixes)
- Proper error handling and verification

Usage:
    python scripts/add_ticker.py AAPL MSFT GOOGL
    python scripts/add_ticker.py FICT3.SA REAG3.SA
"""

import sys
import sqlite3
import yfinance as yf
import pandas as pd
import re
from datetime import datetime


def clean_company_name(name):
    """Remove corporate suffixes from company name"""
    if not name:
        return name

    # Define suffixes to remove (case-insensitive)
    suffixes = [
        r'\s+S\.A\.',
        r'\s+S\.A$',
        r'\s+Inc\.',
        r'\s+Inc$',
        r'\s+Ltd\.',
        r'\s+Ltd$',
        r'\s+LLC',
        r'\s+L\.L\.C\.',
        r'\s+Corp\.',
        r'\s+Corp$',
        r'\s+Corporation',
        r'\s+Company',
        r'\s+Co\.',
        r'\s+Holdings',
        r'\s+Hldgs\.',
        r'\s+Hldgs$',
        r'\s+Group',
        r'\s+Limited',
        r'\s+PLC',
        r'\s+plc',
        r'\s+N\.V\.',
        r'\s+AG$',
        r',\s+Inc\.',
        r',\s+Inc$',
    ]

    cleaned = name

    # Remove suffixes
    for suffix in suffixes:
        cleaned = re.sub(suffix, '', cleaned, flags=re.IGNORECASE)

    # Clean up extra spaces and trailing commas
    cleaned = ' '.join(cleaned.split())
    cleaned = cleaned.rstrip(',').strip()

    # Remove standalone "Hldgs" if still present
    if cleaned.endswith('Hldgs'):
        cleaned = cleaned[:-5].strip()

    return cleaned


def add_tickers(tickers, database_path='market_data.db'):
    """Add tickers to database with price data and metadata"""

    if not tickers:
        print("Error: No tickers provided")
        return False

    print("=" * 60)
    print("Add Tickers to Database")
    print("=" * 60)
    print()
    print(f"Tickers to add: {', '.join(tickers)}")
    print(f"Database: {database_path}")
    print()

    # Connect to database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Step 1: Download price data
    print("Step 1: Downloading historical price data...")
    print("-" * 60)

    try:
        data = yf.download(tickers, period='max', progress=False)

        # Extract close prices
        if len(tickers) == 1:
            close_data = pd.DataFrame({tickers[0]: data['Close']})
        else:
            close_data = data['Close']

        # Remove timezone info to match database format
        close_data.index = close_data.index.tz_localize(None)

    except Exception as e:
        print(f"Error downloading data: {e}")
        return False

    # Step 2: Update price table
    print()
    print("Step 2: Updating stock_prices_daily table...")
    print("-" * 60)

    try:
        # Read existing table
        existing = pd.read_sql('SELECT * FROM stock_prices_daily', conn, index_col='Date', parse_dates=['Date'])

        # Add/update new tickers
        for ticker in tickers:
            if ticker in close_data.columns:
                existing[ticker] = close_data[ticker]
                count = close_data[ticker].notna().sum()

                if count > 0:
                    first_date = close_data[ticker].dropna().index[0].strftime('%Y-%m-%d')
                    last_date = close_data[ticker].dropna().index[-1].strftime('%Y-%m-%d')
                    latest = close_data[ticker].dropna().iloc[-1]

                    print(f"{ticker:12s} - {count:,} data points")
                    print(f"  Range: {first_date} to {last_date}")
                    print(f"  Latest: ${latest:.2f}")
                else:
                    print(f"{ticker:12s} - NO DATA AVAILABLE")

        # Write to staging table
        print()
        print("Writing to staging table...")
        cursor.execute('DROP TABLE IF EXISTS stock_prices_daily_staging')
        cursor.execute('DROP INDEX IF EXISTS ix_stock_prices_daily_staging_Date')
        conn.commit()

        existing.astype(float).to_sql('stock_prices_daily_staging', conn, if_exists='replace', index=True, index_label='Date')

        # Atomic swap
        cursor.execute('DROP TABLE IF EXISTS stock_prices_daily_old')
        cursor.execute('ALTER TABLE stock_prices_daily RENAME TO stock_prices_daily_old')
        cursor.execute('ALTER TABLE stock_prices_daily_staging RENAME TO stock_prices_daily')
        conn.commit()

        print("[OK] Price data updated")

    except Exception as e:
        print(f"Error updating price table: {e}")
        conn.rollback()
        return False

    # Step 3: Update metadata
    print()
    print("Step 3: Updating ticker_metadata table...")
    print("-" * 60)

    for ticker in tickers:
        try:
            # Get company name from Yahoo Finance
            stock = yf.Ticker(ticker)
            info = stock.info
            raw_name = info.get('longName', info.get('shortName', ticker))

            # Clean company name
            clean_name = clean_company_name(raw_name)

            # Get date range from database
            cursor.execute(f'SELECT MIN(Date), MAX(Date), COUNT(*) FROM stock_prices_daily WHERE "{ticker}" IS NOT NULL')
            first_date, last_date, data_points = cursor.fetchone()

            if not first_date:
                print(f"{ticker:12s} - SKIPPED (no price data)")
                continue

            # Check if metadata already exists
            cursor.execute('SELECT ticker FROM ticker_metadata WHERE ticker = ?', (ticker,))
            exists = cursor.fetchone()

            if exists:
                cursor.execute('''
                    UPDATE ticker_metadata
                    SET name = ?,
                        table_name = 'stock_prices_daily',
                        data_type = 'stock',
                        first_date = ?,
                        last_date = ?,
                        data_points = ?
                    WHERE ticker = ?
                ''', (clean_name, first_date, last_date, data_points, ticker))
                action = 'Updated'
            else:
                cursor.execute('''
                    INSERT INTO ticker_metadata (ticker, name, table_name, data_type, first_date, last_date, data_points)
                    VALUES (?, ?, 'stock_prices_daily', 'stock', ?, ?, ?)
                ''', (ticker, clean_name, first_date, last_date, data_points))
                action = 'Added'

            print(f"{action} {ticker:12s}")
            print(f"  Name: {clean_name}")
            print(f"  (Original: {raw_name})")
            print(f"  Range: {first_date[:10]} to {last_date[:10]}")
            print(f"  Points: {data_points:,}")

        except Exception as e:
            print(f"{ticker:12s} - ERROR: {str(e)[:60]}")

    conn.commit()
    print()
    print("[OK] Metadata updated")

    # Step 4: Verification
    print()
    print("Step 4: Final Verification")
    print("-" * 60)

    for ticker in tickers:
        cursor.execute(f'SELECT Date, "{ticker}" FROM stock_prices_daily WHERE "{ticker}" IS NOT NULL ORDER BY Date DESC LIMIT 1')
        price_row = cursor.fetchone()

        cursor.execute('SELECT name, data_points FROM ticker_metadata WHERE ticker = ?', (ticker,))
        meta_row = cursor.fetchone()

        if price_row and meta_row:
            print(f"{ticker:12s} - {meta_row[0]}")
            print(f"  Latest: {price_row[0][:10]} - ${price_row[1]:.2f}")
            print(f"  Total: {meta_row[1]:,} data points")
        else:
            print(f"{ticker:12s} - VERIFICATION FAILED")

    conn.close()

    print()
    print("=" * 60)
    print("TICKERS ADDED SUCCESSFULLY")
    print("=" * 60)

    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    tickers = sys.argv[1:]
    success = add_tickers(tickers)

    sys.exit(0 if success else 1)
