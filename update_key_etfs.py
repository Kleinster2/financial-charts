#!/usr/bin/env python
"""
Update key ETFs with full historical data from 2000-2025.
"""

import sys
import time
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from constants import DB_PATH, get_db_connection

# Key ETFs to update with full history
KEY_ETFS = [
    'SPY', 'QQQ', 'DIA', 'IWM',  # Major indices
    'VTI', 'VOO', 'VEA', 'VWO',  # Vanguard
    'EEM', 'EFA', 'IVV', 'IJH',  # iShares
    'AGG', 'BND', 'TLT', 'IEF',  # Bonds
    'GLD', 'SLV', 'USO', 'UNG',  # Commodities
    'XLF', 'XLK', 'XLE', 'XLV',  # Sectors
    'XLI', 'XLY', 'XLP', 'XLB',  # More sectors
    'XLU', 'XLRE', 'XLC'         # Remaining sectors
]

def update_key_etfs():
    """Download and update key ETFs with full historical data."""
    print(f"Updating {len(KEY_ETFS)} key ETFs with full historical data...")
    print(f"Date range: 2000-01-01 to {datetime.today().strftime('%Y-%m-%d')}")
    print("="*60)

    # Download data
    start_date = "2000-01-01"
    end_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    all_data = {}
    failed = []

    for i, ticker in enumerate(KEY_ETFS, 1):
        print(f"[{i}/{len(KEY_ETFS)}] Downloading {ticker}...", end=" ")
        try:
            data = yf.download(
                ticker,
                start=start_date,
                end=end_date,
                auto_adjust=True,
                progress=False,
                timeout=10
            )

            if not data.empty and 'Close' in data.columns:
                if not data['Close'].isna().all():
                    all_data[ticker] = data
                    print(f"OK ({len(data)} days)")
                else:
                    failed.append(ticker)
                    print("FAIL (no data)")
            else:
                failed.append(ticker)
                print("FAIL (empty)")
        except Exception as e:
            failed.append(ticker)
            print(f"FAIL ({str(e)[:30]})")

        time.sleep(0.2)  # Brief pause to avoid rate limiting

    print("\n" + "="*60)
    print(f"Downloaded: {len(all_data)}/{len(KEY_ETFS)} ETFs")

    if not all_data:
        print("No data to save!")
        return False

    # Process data for database
    print("\nProcessing data for database update...")
    processed_dfs = []

    for ticker, data in all_data.items():
        if 'Close' in data.columns:
            close_series = data[['Close']].rename(columns={'Close': ticker})
            processed_dfs.append(close_series)

    # Combine all data
    new_data_df = pd.concat(processed_dfs, axis=1)
    new_data_df.index = pd.to_datetime(new_data_df.index)

    print(f"Date range in data: {new_data_df.index[0].strftime('%Y-%m-%d')} to {new_data_df.index[-1].strftime('%Y-%m-%d')}")

    # Update database
    conn = get_db_connection(row_factory=None)
    try:
        # Load existing data
        existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
        if not existing_df.empty and 'Date' in existing_df.columns:
            existing_df['Date'] = pd.to_datetime(existing_df['Date'])
            existing_df.set_index('Date', inplace=True)

        print(f"Merging with existing data ({len(existing_df)} rows)...")

        # Update only the ETF columns we downloaded
        for ticker in all_data.keys():
            if ticker not in existing_df.columns:
                existing_df[ticker] = pd.NA

            # Replace the entire column with new data
            for date in new_data_df.index:
                if pd.notna(new_data_df.loc[date, ticker]):
                    existing_df.loc[date, ticker] = new_data_df.loc[date, ticker]

        # Sort by date
        existing_df = existing_df.sort_index()

        # Save back to database
        print("Saving to database...")
        existing_df.astype(float).to_sql(
            'stock_prices_daily',
            conn,
            if_exists='replace',
            index=True,
            index_label='Date'
        )

        print("SUCCESS: Database updated successfully!")

        # Verify the update
        cursor = conn.cursor()
        for ticker in ['SPY', 'QQQ', 'DIA', 'IWM']:
            cursor.execute(f'''
                SELECT COUNT("{ticker}") as count,
                       MIN(CASE WHEN "{ticker}" IS NOT NULL THEN Date END) as first,
                       MAX(CASE WHEN "{ticker}" IS NOT NULL THEN Date END) as last
                FROM stock_prices_daily
                WHERE "{ticker}" IS NOT NULL
            ''')
            result = cursor.fetchone()
            if result[0] > 0:
                print(f"  {ticker}: {result[0]} days, from {result[1][:10]} to {result[2][:10]}")

        return True

    except Exception as e:
        print(f"ERROR: Database update failed: {e}")
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    success = update_key_etfs()
    sys.exit(0 if success else 1)