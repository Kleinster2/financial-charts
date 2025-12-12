#!/usr/bin/env python3
"""
Download historical data for CBOE volatility indices.

Downloads historical close prices for major CBOE indices (^VIX, ^VXN, etc.)
and stores them in stock_prices_daily table.
"""

import sqlite3
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import sys

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from constants import DB_PATH

# CBOE indices to download
CBOE_INDICES = {
    '^VIX': 'CBOE Volatility Index',
    '^VXN': 'CBOE Nasdaq-100 Volatility Index',
    '^VXD': 'CBOE DJIA Volatility Index',
    '^RVX': 'CBOE Russell 2000 Volatility Index',
}


def download_cboe_index(symbol, description, start_date='2010-01-01'):
    """
    Download historical data for a CBOE index using yfinance.

    Args:
        symbol: CBOE symbol (e.g., '^VIX')
        description: Index description
        start_date: Start date for historical download (default: 2010-01-01)

    Returns:
        DataFrame with Date and Close columns, or None if download fails
    """
    print(f"\nDownloading {symbol} ({description})...")

    try:
        ticker = yf.Ticker(symbol)

        # Download historical data
        df = ticker.history(start=start_date, end=datetime.now().strftime('%Y-%m-%d'))

        if df.empty:
            print(f"  ✗ No data available")
            return None

        # Keep only Date (index) and Close columns
        df = df[['Close']].copy()
        df.index = pd.to_datetime(df.index).date  # Convert to date only
        df.index.name = 'Date'

        print(f"  ✓ Downloaded {len(df)} rows")
        print(f"    Range: {df.index.min()} to {df.index.max()}")
        print(f"    Latest value: {df['Close'].iloc[-1]:.2f}")

        return df

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None


def save_to_database(symbol, df):
    """
    Save CBOE index data to stock_prices_daily table.

    Args:
        symbol: CBOE symbol (e.g., '^VIX')
        df: DataFrame with Date index and Close column

    Returns:
        Number of rows updated/inserted
    """
    if df is None or df.empty:
        return 0

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    rows_updated = 0
    rows_inserted = 0

    try:
        # Check if column exists, add if needed
        cursor.execute("PRAGMA table_info(stock_prices_daily)")
        columns = {row[1] for row in cursor.fetchall()}

        if symbol not in columns:
            print(f"  Adding column {symbol} to stock_prices_daily...")
            cursor.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{symbol}" REAL')
            conn.commit()

        # Insert/update each row
        for date, row in df.iterrows():
            value = row['Close']

            # Try UPDATE first
            cursor.execute(f'''
                UPDATE stock_prices_daily
                SET "{symbol}" = ?
                WHERE DATE(Date) = ?
            ''', (value, str(date)))

            if cursor.rowcount > 0:
                rows_updated += 1
            else:
                # Date doesn't exist, INSERT new row
                cursor.execute(f'''
                    INSERT INTO stock_prices_daily (Date, "{symbol}")
                    VALUES (?, ?)
                ''', (str(date), value))
                rows_inserted += 1

        conn.commit()
        print(f"  ✓ Database: {rows_updated} updated, {rows_inserted} inserted")

        return rows_updated + rows_inserted

    except sqlite3.Error as e:
        print(f"  ✗ Database error: {e}")
        conn.rollback()
        return 0

    finally:
        conn.close()


def update_metadata(symbol, description, df):
    """
    Update ticker_metadata table with index information.

    Args:
        symbol: CBOE symbol
        description: Index description
        df: DataFrame with historical data
    """
    if df is None or df.empty:
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        first_date = str(df.index.min())
        last_date = str(df.index.max())
        data_points = len(df)

        cursor.execute('''
            INSERT OR REPLACE INTO ticker_metadata
            (ticker, name, table_name, data_type, first_date, last_date, data_points)
            VALUES (?, ?, 'stock_prices_daily', 'volatility_index', ?, ?, ?)
        ''', (symbol, description, first_date, last_date, data_points))

        conn.commit()
        print(f"  ✓ Metadata updated")

    except sqlite3.Error as e:
        print(f"  ✗ Metadata error: {e}")
        conn.rollback()

    finally:
        conn.close()


def main():
    print("="*70)
    print("CBOE Historical Data Download")
    print("="*70)
    print(f"\nDatabase: {DB_PATH}")
    print(f"Indices to download: {len(CBOE_INDICES)}")

    total_rows = 0
    successful = 0

    for symbol, description in CBOE_INDICES.items():
        # Download historical data
        df = download_cboe_index(symbol, description)

        if df is not None:
            # Save to database
            rows = save_to_database(symbol, df)
            total_rows += rows

            # Update metadata
            update_metadata(symbol, description, df)

            successful += 1

    print("\n" + "="*70)
    print("Download Summary")
    print("="*70)
    print(f"\nSuccessful: {successful}/{len(CBOE_INDICES)} indices")
    print(f"Total rows: {total_rows}")
    print("\n✓ Download complete!")


if __name__ == '__main__':
    main()
