#!/usr/bin/env python3
"""
Fetch JGB (Japanese Government Bond) yield data from FRED
Federal Reserve Economic Data - St. Louis Fed

This script fetches official JGB yield data and stores it in the database.
FRED provides monthly data with a slight lag but it's official and reliable.
"""

import sqlite3
import sys
from datetime import datetime, timedelta
import pandas as pd
from fredapi import Fred
import os

# FRED API Configuration
# You need to get a free API key from: https://fred.stlouisfed.org/docs/api/api_key.html
# Then set it as an environment variable: set FRED_API_KEY=your_key_here
# Or directly in the script (less secure): FRED_API_KEY = "your_key_here"

FRED_API_KEY = os.environ.get('FRED_API_KEY', 'YOUR_API_KEY_HERE')

# FRED Series IDs for Japanese bond yields
JGB_SERIES = {
    'jgb_10y': 'INTGSBJPM193N',  # 10-Year Japanese Government Bond Yield
    'jgb_long': 'IRLTLT01JPM156N'  # Long-term government bond yields for Japan
}

def fetch_fred_data(api_key=None, start_date='2020-01-01'):
    """
    Fetch JGB yield data from FRED API

    Args:
        api_key: FRED API key (if None, uses environment variable)
        start_date: Start date for data retrieval (YYYY-MM-DD format)

    Returns:
        DataFrame with JGB yield data
    """
    if api_key is None:
        api_key = FRED_API_KEY

    if api_key == 'YOUR_API_KEY_HERE':
        print("=" * 70)
        print("ERROR: FRED API key not configured!")
        print("=" * 70)
        print("\nTo use this script, you need a free FRED API key:")
        print("1. Go to: https://fred.stlouisfed.org/docs/api/api_key.html")
        print("2. Click 'Request API Key' and create a free account")
        print("3. You'll receive your API key immediately")
        print("\nThen set it as an environment variable:")
        print("  Windows: set FRED_API_KEY=your_key_here")
        print("  Linux/Mac: export FRED_API_KEY=your_key_here")
        print("\nOr edit this script and replace 'YOUR_API_KEY_HERE' with your actual key")
        print("=" * 70)
        return None

    try:
        print(f"Connecting to FRED API...")
        fred = Fred(api_key=api_key)

        # Create a DataFrame to store all yield data
        yield_data = pd.DataFrame()

        # Fetch each series
        for column_name, series_id in JGB_SERIES.items():
            print(f"Fetching {column_name} (Series: {series_id})...")
            try:
                series_data = fred.get_series(
                    series_id,
                    observation_start=start_date
                )

                if yield_data.empty:
                    yield_data = pd.DataFrame(index=series_data.index)

                yield_data[column_name] = series_data
                print(f"  Retrieved {len(series_data)} data points")

            except Exception as e:
                print(f"  Warning: Could not fetch {series_id}: {e}")
                continue

        if yield_data.empty:
            print("No data retrieved from FRED")
            return None

        # Reset index to have date as a column
        yield_data.reset_index(inplace=True)
        yield_data.rename(columns={'index': 'date'}, inplace=True)

        # Add source column
        yield_data['source'] = 'FRED'

        print(f"\nSuccessfully fetched {len(yield_data)} rows of JGB yield data")
        print(f"Date range: {yield_data['date'].min()} to {yield_data['date'].max()}")

        # Show recent data
        print("\nMost recent JGB yields:")
        print(yield_data.tail(5).to_string())

        return yield_data

    except Exception as e:
        print(f"Error fetching FRED data: {e}")
        return None


def store_in_database(yield_data, db_path='market_data.db'):
    """
    Store JGB yield data in SQLite database

    Args:
        yield_data: DataFrame with yield data
        db_path: Path to SQLite database

    Returns:
        Boolean indicating success
    """
    if yield_data is None or yield_data.empty:
        print("No data to store")
        return False

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Ensure table exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jgb_yields (
                date DATE PRIMARY KEY,
                jgb_10y REAL,
                jgb_long REAL,
                source TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Prepare data for insertion
        stored_count = 0
        updated_count = 0

        for _, row in yield_data.iterrows():
            try:
                # Try to insert new row
                cursor.execute('''
                    INSERT INTO jgb_yields (date, jgb_10y, jgb_long, source)
                    VALUES (?, ?, ?, ?)
                ''', (
                    row['date'].strftime('%Y-%m-%d'),
                    row.get('jgb_10y'),
                    row.get('jgb_long'),
                    row.get('source', 'FRED')
                ))
                stored_count += 1

            except sqlite3.IntegrityError:
                # Row exists, update it
                cursor.execute('''
                    UPDATE jgb_yields
                    SET jgb_10y = ?, jgb_long = ?, source = ?,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE date = ?
                ''', (
                    row.get('jgb_10y'),
                    row.get('jgb_long'),
                    row.get('source', 'FRED'),
                    row['date'].strftime('%Y-%m-%d')
                ))
                updated_count += 1

        conn.commit()

        # Get summary statistics
        cursor.execute('SELECT COUNT(*) FROM jgb_yields')
        total_rows = cursor.fetchone()[0]

        cursor.execute('''
            SELECT MIN(date), MAX(date)
            FROM jgb_yields
            WHERE jgb_10y IS NOT NULL
        ''')
        date_range = cursor.fetchone()

        conn.close()

        print("\n" + "=" * 70)
        print("DATABASE UPDATE COMPLETE")
        print("=" * 70)
        print(f"New rows added: {stored_count}")
        print(f"Existing rows updated: {updated_count}")
        print(f"Total rows in database: {total_rows}")
        if date_range[0]:
            print(f"Date range in database: {date_range[0]} to {date_range[1]}")
        print("=" * 70)

        return True

    except Exception as e:
        print(f"Error storing data in database: {e}")
        return False


def display_comparison():
    """
    Display comparison between JGB yields and bond ETF prices
    """
    try:
        conn = sqlite3.connect('market_data.db')

        # Get recent JGB yields
        yields_query = '''
            SELECT date, jgb_10y, jgb_long
            FROM jgb_yields
            WHERE date >= date('now', '-6 months')
            ORDER BY date DESC
            LIMIT 10
        '''
        yields_df = pd.read_sql_query(yields_query, conn)

        # Get recent JPGB ETF prices (proxy for bond prices)
        jpgb_query = '''
            SELECT Date, JPGB
            FROM stock_prices_daily
            WHERE Date >= date('now', '-1 month')
            AND JPGB IS NOT NULL
            ORDER BY Date DESC
            LIMIT 10
        '''
        jpgb_df = pd.read_sql_query(jpgb_query, conn)

        conn.close()

        print("\n" + "=" * 70)
        print("COMPARISON: JGB YIELDS vs BOND ETF PRICES")
        print("=" * 70)

        if not yields_df.empty:
            print("\nRecent JGB Yields (from FRED):")
            print("Date         10Y Yield  Long Yield")
            print("-" * 35)
            for _, row in yields_df.head(5).iterrows():
                print(f"{row['date']}   {row['jgb_10y']:6.3f}%    {row['jgb_long']:6.3f}%")

        if not jpgb_df.empty:
            print("\nRecent JPGB ETF Prices (from Yahoo Finance):")
            print("Date         JPGB Price")
            print("-" * 25)
            for _, row in jpgb_df.head(5).iterrows():
                print(f"{row['Date']}   ${row['JPGB']:.2f}")

            print("\nNote: Bond prices move inversely to yields")
            print("When yields rise (bond rout), ETF prices fall")

        print("=" * 70)

    except Exception as e:
        print(f"Error displaying comparison: {e}")


def main():
    """
    Main function to fetch and store JGB yield data
    """
    print("=" * 70)
    print("JGB YIELD DATA FETCHER - FRED Integration")
    print("=" * 70)

    # Check if API key is configured
    api_key = os.environ.get('FRED_API_KEY', FRED_API_KEY)

    if api_key == 'YOUR_API_KEY_HERE':
        # Try to use a demo/test fetch
        print("\nNo API key configured. Showing demo of what this script does...")
        print("\nThis script will fetch:")
        print("1. 10-Year JGB Yields (Series: INTGSBJPM193N)")
        print("2. Long-term JGB Yields (Series: IRLTLT01JPM156N)")
        print("\nData is updated monthly by FRED (Federal Reserve Economic Data)")
        print("\nTo actually fetch data, get a free API key from FRED (see instructions above)")
        return

    # Fetch data from FRED
    print(f"\nFetching JGB yield data from FRED...")
    yield_data = fetch_fred_data(api_key, start_date='2020-01-01')

    if yield_data is not None:
        # Store in database
        success = store_in_database(yield_data)

        if success:
            # Display comparison with ETF data
            display_comparison()

            print("\n✓ JGB yield data successfully integrated!")
            print("You can now create charts combining actual yields with ETF proxies")
    else:
        print("\nFailed to fetch JGB yield data")
        print("Please check your API key and internet connection")
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())