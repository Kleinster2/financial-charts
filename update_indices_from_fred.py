#!/usr/bin/env python
"""
Supplemental update script for indices that don't work with Yahoo Finance.
Run this after the main update to fill in gaps from FRED.
"""

import sys
import pandas as pd
from datetime import datetime, timedelta
from constants import DB_PATH, get_db_connection
from fred_utils import download_from_fred

# Indices that need FRED (Yahoo Finance doesn't work for these)
FRED_INDICES = {
    '^RVX': 'RVXCLS',      # Russell 2000 Volatility (active, Yahoo blocks it)
    '^VXV': 'VXVCLS',      # VIX 3-Month (active, Yahoo blocks it)
    # These are discontinued but FRED has historical data through their end dates:
    '^VXO': 'VXOCLS',      # Discontinued Sept 2021
    '^EVZ': 'EVZCLS',      # Discontinued March 2025
    # ^VOLQ removed - FRED series no longer exists (404)
}

def update_indices_from_fred(lookback_days=30):
    """
    Update indices from FRED.

    Args:
        lookback_days: How many days back to check/update (default 30)
    """
    print("Updating Indices from FRED")
    print("="*60)
    print(f"Looking back {lookback_days} days for updates")
    print()

    cutoff_date = datetime.now() - timedelta(days=lookback_days)

    all_updates = {}

    for ticker, fred_code in FRED_INDICES.items():
        print(f"Checking {ticker} ({fred_code})...", end=" ")

        data = download_from_fred(fred_code)

        if data is not None and not data.empty:
            # Filter to recent data only
            recent_data = data[data.index >= cutoff_date]

            if not recent_data.empty:
                all_updates[ticker] = recent_data
                print(f"OK ({len(recent_data)} new days, latest {recent_data.index[-1].strftime('%Y-%m-%d')})")
            else:
                print("OK (no new data)")
        else:
            print("FAIL")

    if not all_updates:
        print("\nNo updates needed - all indices are current")
        return True

    # Update database
    print(f"\nUpdating database with {len(all_updates)} indices...")

    conn = get_db_connection(row_factory=None)
    try:
        existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
        existing_df['Date'] = pd.to_datetime(existing_df['Date'])
        existing_df.set_index('Date', inplace=True)

        # Update each ticker
        combined_df = existing_df.copy()

        for ticker, data in all_updates.items():
            if ticker not in combined_df.columns:
                combined_df[ticker] = pd.NA

            # Update with new data
            for date in data.index:
                combined_df.loc[date, ticker] = data.loc[date, 'Close']

        # Sort and save
        combined_df = combined_df.sort_index()
        combined_df = combined_df.fillna(value=pd.NA).replace({pd.NA: None})

        # Atomic update
        cursor = conn.cursor()
        cursor.execute("DROP INDEX IF EXISTS ix_stock_prices_daily_staging_Date")
        cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_staging")
        cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_old")
        conn.commit()

        combined_df.to_sql('stock_prices_daily_staging', conn,
                          if_exists='replace', index=True,
                          index_label='Date', dtype='REAL')

        cursor.execute("ALTER TABLE stock_prices_daily RENAME TO stock_prices_daily_old")
        cursor.execute("ALTER TABLE stock_prices_daily_staging RENAME TO stock_prices_daily")
        cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_old")
        conn.commit()

        print("SUCCESS: Database updated")

        # Verify
        print("\nVerification:")
        for ticker in all_updates.keys():
            cursor.execute(f'''
                SELECT MAX(Date)
                FROM stock_prices_daily
                WHERE "{ticker}" IS NOT NULL
            ''')
            latest = cursor.fetchone()[0]
            if latest:
                print(f"  {ticker:12} latest: {latest[:10]}")

        conn.close()
        return True

    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        conn.close()
        return False

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Update indices from FRED')
    parser.add_argument('--lookback', type=int, default=30,
                       help='Days to look back for updates (default: 30)')

    args = parser.parse_args()

    success = update_indices_from_fred(lookback_days=args.lookback)
    sys.exit(0 if success else 1)
