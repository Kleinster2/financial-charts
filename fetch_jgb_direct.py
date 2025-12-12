#!/usr/bin/env python3
"""
Direct fetch of JGB yield data from FRED without API key
Uses FRED's public CSV download endpoints
"""

import pandas as pd
import sqlite3
import requests
from datetime import datetime
import sys
from constants import DB_PATH

def fetch_jgb_yields_direct():
    """
    Fetch JGB yields directly from FRED's public CSV endpoints
    No API key required for basic CSV downloads
    """

    # FRED public CSV URLs for JGB data
    urls = {
        'jgb_10y': 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=INTGSBJPM193N',
        'jgb_long': 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=IRLTLT01JPM156N'
    }

    print("=" * 70)
    print("FETCHING JGB YIELD DATA FROM FRED (Direct CSV)")
    print("=" * 70)

    all_data = None

    for name, url in urls.items():
        print(f"\nFetching {name}...")
        try:
            # Download CSV directly - handle the format more carefully
            df = pd.read_csv(url)

            # Check what columns we have
            if 'DATE' in df.columns:
                df['DATE'] = pd.to_datetime(df['DATE'])
                df.set_index('DATE', inplace=True)
            else:
                # Try first column as date
                df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
                df.set_index(df.columns[0], inplace=True)

            # Rename the value column to our naming convention
            if len(df.columns) > 0:
                df.rename(columns={df.columns[0]: name}, inplace=True)

            # Merge with existing data
            if all_data is None:
                all_data = df[[name]]  # Only keep the column we want
            else:
                all_data = all_data.join(df[[name]], how='outer')

            print(f"  [OK] Retrieved {len(df)} data points")
            print(f"  Date range: {df.index.min().date()} to {df.index.max().date()}")

        except Exception as e:
            print(f"  [ERROR] Error fetching {name}: {e}")
            continue

    if all_data is None:
        print("\nNo data retrieved")
        return None

    # Reset index to have date as column
    all_data.reset_index(inplace=True)

    # The index name might be DATE or something else, rename it to 'date'
    if 'DATE' in all_data.columns:
        all_data.rename(columns={'DATE': 'date'}, inplace=True)
    elif all_data.columns[0] != 'date':
        # Rename first column (which should be the date from the index) to 'date'
        all_data.rename(columns={all_data.columns[0]: 'date'}, inplace=True)

    # Add source
    all_data['source'] = 'FRED'

    # Filter to recent data (2020 onwards)
    all_data = all_data[all_data['date'] >= pd.to_datetime('2020-01-01')]

    print(f"\nTotal rows fetched: {len(all_data)}")
    print("\nMost recent data:")
    print(all_data.tail(5).to_string())

    return all_data


def store_in_database(yield_data):
    """Store JGB yields in SQLite database"""

    if yield_data is None or yield_data.empty:
        print("No data to store")
        return False

    try:
        conn = sqlite3.connect(DB_PATH)
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

        stored = 0
        updated = 0

        for _, row in yield_data.iterrows():
            try:
                cursor.execute('''
                    INSERT INTO jgb_yields (date, jgb_10y, jgb_long, source)
                    VALUES (?, ?, ?, ?)
                ''', (
                    row['date'].strftime('%Y-%m-%d'),
                    row.get('jgb_10y'),
                    row.get('jgb_long'),
                    row['source']
                ))
                stored += 1
            except sqlite3.IntegrityError:
                cursor.execute('''
                    UPDATE jgb_yields
                    SET jgb_10y = ?, jgb_long = ?, source = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE date = ?
                ''', (
                    row.get('jgb_10y'),
                    row.get('jgb_long'),
                    row['source'],
                    row['date'].strftime('%Y-%m-%d')
                ))
                updated += 1

        conn.commit()

        # Get summary
        cursor.execute('SELECT COUNT(*), MIN(date), MAX(date) FROM jgb_yields WHERE jgb_10y IS NOT NULL')
        count, min_date, max_date = cursor.fetchone()

        conn.close()

        print("\n" + "=" * 70)
        print("DATABASE UPDATE COMPLETE")
        print("=" * 70)
        print(f"New rows: {stored}")
        print(f"Updated rows: {updated}")
        print(f"Total rows in database: {count}")
        print(f"Date range: {min_date} to {max_date}")
        print("=" * 70)

        return True

    except Exception as e:
        print(f"Error storing in database: {e}")
        return False


def display_recent_comparison():
    """Show recent JGB yields vs bond ETF prices"""

    try:
        conn = sqlite3.connect(DB_PATH)

        # Recent JGB yields
        query_yields = '''
            SELECT date, jgb_10y, jgb_long
            FROM jgb_yields
            WHERE jgb_10y IS NOT NULL
            ORDER BY date DESC
            LIMIT 10
        '''
        yields = pd.read_sql_query(query_yields, conn)

        # Recent JPGB ETF prices
        query_jpgb = '''
            SELECT Date, JPGB, IGOV, BWX
            FROM stock_prices_daily
            WHERE Date >= date('now', '-30 days')
            AND JPGB IS NOT NULL
            ORDER BY Date DESC
            LIMIT 10
        '''
        etfs = pd.read_sql_query(query_jpgb, conn)

        conn.close()

        print("\n" + "=" * 70)
        print("JGB YIELDS vs BOND ETF PRICES")
        print("=" * 70)

        if not yields.empty:
            print("\nLatest JGB Yields (%, monthly data from FRED):")
            print("-" * 40)
            for _, row in yields.head(5).iterrows():
                date_str = row['date']
                y10 = f"{row['jgb_10y']:.3f}" if pd.notna(row['jgb_10y']) else 'N/A'
                ylong = f"{row['jgb_long']:.3f}" if pd.notna(row['jgb_long']) else 'N/A'
                print(f"{date_str}  10Y: {y10:>6}%  Long: {ylong:>6}%")

        if not etfs.empty:
            print("\nLatest Bond ETF Prices (daily from Yahoo):")
            print("-" * 50)
            for _, row in etfs.head(5).iterrows():
                jpgb = f"${row['JPGB']:.2f}" if pd.notna(row['JPGB']) else 'N/A'
                igov = f"${row['IGOV']:.2f}" if pd.notna(row['IGOV']) else 'N/A'
                bwx = f"${row['BWX']:.2f}" if pd.notna(row['BWX']) else 'N/A'
                print(f"{row['Date']}  JPGB: {jpgb:>7}  IGOV: {igov:>7}  BWX: {bwx:>7}")

        print("\n" + "=" * 70)
        print("KEY INSIGHTS:")
        print("- JGB yields are updated monthly (FRED data lag)")
        print("- Bond ETF prices update daily (real-time proxy)")
        print("- When yields ↑ (bond rout), ETF prices ↓")
        print("- Current tracking: Both actual yields + ETF proxies")
        print("=" * 70)

    except Exception as e:
        print(f"Error in comparison: {e}")


def main():
    """Main function"""

    # Fetch data
    yield_data = fetch_jgb_yields_direct()

    if yield_data is not None:
        # Store in database
        success = store_in_database(yield_data)

        if success:
            # Show comparison
            display_recent_comparison()

            print("\n[SUCCESS] JGB yield data successfully integrated!")
            print("  You now have both actual yields AND ETF proxies")
            return 0

    return 1


if __name__ == '__main__':
    sys.exit(main())