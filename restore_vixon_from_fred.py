#!/usr/bin/env python
"""
Download VIXON single-stock volatility indices from FRED (Federal Reserve Economic Data).
Yahoo Finance API restricts these to 1d/5d only, but FRED has full history from 2010.
"""

import sys
import pandas as pd
from datetime import datetime
from constants import DB_PATH, get_db_connection
from fred_utils import download_from_fred

# Mapping of Yahoo Finance tickers to FRED series codes
FRED_VIXON_MAPPING = {
    '^VXAPL': 'VXAPLCLS',   # CBOE Equity VIX on Apple
    '^VXAZN': 'VXAZNCLS',   # CBOE Equity VIX on Amazon
    '^VXGOG': 'VXGOGCLS',   # CBOE Equity VIX on Google
    '^VXGS': 'VXGSCLS',     # CBOE Equity VIX on Goldman Sachs
    '^VXIBM': 'VXIBMCLS'    # CBOE Equity VIX on IBM
}

def restore_vixon_indices():
    """Download and restore VIXON indices from FRED."""
    print("Restoring VIXON Single-Stock Volatility Indices from FRED")
    print("="*60)
    print("Source: Federal Reserve Economic Data (FRED)")
    print("Date range: 2010-06-01 to present")
    print()

    all_data = {}
    failed = []

    for i, (ticker, fred_code) in enumerate(FRED_VIXON_MAPPING.items(), 1):
        print(f"[{i}/{len(FRED_VIXON_MAPPING)}] Downloading {ticker} ({fred_code})...", end=" ")

        data = download_from_fred(fred_code)

        if data is not None and not data.empty:
            all_data[ticker] = data
            first_date = data.index[0].strftime('%Y-%m-%d')
            last_date = data.index[-1].strftime('%Y-%m-%d')
            print(f"OK ({len(data)} days, {first_date} to {last_date})")
        else:
            failed.append(ticker)
            print("FAIL")

    print("\n" + "="*60)
    print(f"Downloaded: {len(all_data)}/{len(FRED_VIXON_MAPPING)} indices")
    if failed:
        print(f"Failed: {', '.join(failed)}")

    if not all_data:
        print("No data to save!")
        return False

    # Combine all data
    print("\nProcessing data for database update...")
    new_data_df = pd.concat([data for data in all_data.values()], axis=1)
    new_data_df.columns = list(all_data.keys())
    new_data_df.index = pd.to_datetime(new_data_df.index)

    print(f"Date range: {new_data_df.index[0].strftime('%Y-%m-%d')} to {new_data_df.index[-1].strftime('%Y-%m-%d')}")

    # Update database
    conn = get_db_connection(row_factory=None)
    try:
        # Load existing data
        print("Loading existing database...")
        existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
        if not existing_df.empty and 'Date' in existing_df.columns:
            existing_df['Date'] = pd.to_datetime(existing_df['Date'])
            existing_df.set_index('Date', inplace=True)

        print(f"Merging with existing data ({len(existing_df)} rows)...")

        # Ensure columns exist
        for ticker in all_data.keys():
            if ticker not in existing_df.columns:
                existing_df[ticker] = pd.NA

        # Vectorized update (fast!)
        combined_df = existing_df.copy()
        combined_df.update(new_data_df)

        # Add any new dates
        new_dates = new_data_df.index.difference(combined_df.index)
        if len(new_dates) > 0:
            combined_df = pd.concat([combined_df, new_data_df.loc[new_dates]])
            combined_df = combined_df.sort_index()

        # Save back to database
        print("Saving to database...")

        # Clean up staging tables and indices
        cursor = conn.cursor()
        cursor.execute("DROP INDEX IF EXISTS ix_stock_prices_daily_staging_Date")
        cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_staging")
        cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_old")
        conn.commit()

        # Convert pd.NA to None for SQLite compatibility
        combined_df = combined_df.fillna(value=pd.NA).replace({pd.NA: None})

        # Save to staging table
        combined_df.to_sql(
            'stock_prices_daily_staging',
            conn,
            if_exists='replace',
            index=True,
            index_label='Date',
            dtype='REAL'
        )

        # Atomic swap
        cursor.execute("ALTER TABLE stock_prices_daily RENAME TO stock_prices_daily_old")
        cursor.execute("ALTER TABLE stock_prices_daily_staging RENAME TO stock_prices_daily")
        cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_old")
        conn.commit()

        print("SUCCESS: Database updated successfully!")

        # Verify the update
        print("\nVerification:")
        for ticker in all_data.keys():
            cursor.execute(f'''
                SELECT COUNT(\"{ticker}\") as count,
                       MIN(CASE WHEN \"{ticker}\" IS NOT NULL THEN Date END) as first,
                       MAX(CASE WHEN \"{ticker}\" IS NOT NULL THEN Date END) as last
                FROM stock_prices_daily
                WHERE \"{ticker}\" IS NOT NULL
            ''')
            result = cursor.fetchone()
            if result[0] > 0:
                years = result[0] / 251
                print(f"  {ticker:12} {result[0]:5} days ({years:4.1f} yrs), from {result[1][:10]} to {result[2][:10]}")

        return True

    except Exception as e:
        print(f"ERROR: Database update failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    success = restore_vixon_indices()
    sys.exit(0 if success else 1)
