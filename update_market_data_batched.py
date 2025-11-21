#!/usr/bin/env python
"""Modified update script that downloads in smaller batches to avoid hanging."""

import sys
sys.path.append('.')

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time
from constants import DB_PATH, get_db_connection
from download_all_assets import *

# Date range
START_DATE = "2022-12-30"
END_DATE = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

def download_batch(tickers, batch_size=50):
    """Download tickers in smaller batches to avoid hanging."""
    all_data = {}
    total = len(tickers)

    for i in range(0, total, batch_size):
        batch = tickers[i:i+batch_size]
        batch_num = i // batch_size + 1
        total_batches = (total + batch_size - 1) // batch_size

        print(f"Downloading batch {batch_num}/{total_batches} ({len(batch)} tickers)...")
        print(f"  Tickers: {batch[0]} to {batch[-1]}")

        try:
            # Download with explicit timeout
            data = yf.download(
                batch,
                start=START_DATE,
                end=END_DATE,
                auto_adjust=True,
                group_by='ticker',
                progress=True,
                threads=True,  # Use multithreading
                timeout=30  # 30 second timeout per ticker
            )

            if not data.empty:
                # If single ticker, wrap in dict
                if len(batch) == 1:
                    all_data[batch[0]] = data
                else:
                    # Multi-ticker data
                    for ticker in batch:
                        if ticker in data.columns.get_level_values(0):
                            all_data[ticker] = data[ticker]

            # Small delay between batches to avoid rate limiting
            if i + batch_size < total:
                time.sleep(1)

        except Exception as e:
            print(f"  WARNING: Batch failed with error: {e}")
            print(f"  Trying tickers individually...")

            # Try each ticker individually if batch fails
            for ticker in batch:
                try:
                    single_data = yf.download(
                        ticker,
                        start=START_DATE,
                        end=END_DATE,
                        auto_adjust=True,
                        progress=False,
                        timeout=5
                    )
                    if not single_data.empty:
                        all_data[ticker] = single_data
                        print(f"    {ticker}: OK")
                    else:
                        print(f"    {ticker}: No data")
                except:
                    print(f"    {ticker}: Failed")

    return all_data

def main():
    print(f"Market Data Update - Batched Download")
    print(f"Date range: {START_DATE} to {END_DATE}")
    print("="*60)

    # Get all tickers (stocks only for now)
    sp500_tickers, _ = get_sp500_tickers()
    ibov_tickers = get_ibovespa_tickers()

    all_stocks = list(set(
        sp500_tickers + ibov_tickers + OTHER_HIGH_PROFILE_STOCKS + EV_STOCKS + CRYPTO_STOCKS + QUANTUM_STOCKS +
        ADTECH_STOCKS + GAMING_IGAMING_STOCKS + BIOTECH_STOCKS + MINING_RARE_EARTH_STOCKS + BATTERY_ENERGY_STORAGE_STOCKS +
        NUCLEAR_ENERGY_STOCKS + AI_SEMICONDUCTOR_STOCKS + SPACE_AEROSPACE_STOCKS + DEFENSE_STOCKS
    ))

    # Filter out excluded tickers and sort
    stocks = sorted([t for t in all_stocks if t not in EXCLUDED_TICKERS])

    print(f"Total tickers to download: {len(stocks)}")
    print()

    # Download in batches
    all_data = download_batch(stocks, batch_size=30)

    print()
    print(f"Successfully downloaded data for {len(all_data)} tickers")

    if not all_data:
        print("No data downloaded. Exiting.")
        return

    # Process and combine data
    print("\nProcessing data...")
    processed_dfs = []
    processed_vol_dfs = []

    for ticker, data in all_data.items():
        if 'Close' in data.columns:
            close_series = data[['Close']].rename(columns={'Close': ticker})
            processed_dfs.append(close_series)

        if 'Volume' in data.columns:
            vol_series = data[['Volume']].rename(columns={'Volume': ticker})
            processed_vol_dfs.append(vol_series)

    # Combine all data
    new_data_df = pd.concat(processed_dfs, axis=1) if processed_dfs else pd.DataFrame()
    new_vol_df = pd.concat(processed_vol_dfs, axis=1) if processed_vol_dfs else pd.DataFrame()

    if not new_data_df.empty:
        new_data_df.index = pd.to_datetime(new_data_df.index)
    if not new_vol_df.empty:
        new_vol_df.index = pd.to_datetime(new_vol_df.index)

    # Load existing data
    print("\nLoading existing database...")
    conn = get_db_connection(row_factory=None)

    try:
        cursor = conn.cursor()

        # Check if tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_prices_daily';")
        table_exists = cursor.fetchone() is not None

        existing_df = pd.DataFrame()
        if table_exists:
            existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
            if not existing_df.empty and 'Date' in existing_df.columns:
                existing_df['Date'] = pd.to_datetime(existing_df['Date'])
                existing_df.set_index('Date', inplace=True)

        # Merge with existing data
        print("\nMerging with existing data...")
        if not existing_df.empty:
            combined_df = existing_df.copy()

            # Add new columns
            for col in new_data_df.columns:
                if col not in combined_df.columns:
                    combined_df[col] = pd.NA

            # Combine and update
            combined_df = pd.concat([combined_df, new_data_df])
            combined_df = combined_df[~combined_df.index.duplicated(keep='last')]
            combined_df = combined_df.sort_index()

            # Update downloaded columns
            for col in new_data_df.columns:
                for date in new_data_df.index:
                    if pd.notna(new_data_df.loc[date, col]):
                        combined_df.loc[date, col] = new_data_df.loc[date, col]
        else:
            combined_df = new_data_df

        # Save to database
        print("\nSaving to database...")
        print(f"  Total rows: {len(combined_df)}")
        print(f"  Total columns: {len(combined_df.columns)}")

        # Use staging table for safety
        staging_table = "stock_prices_daily_staging"
        combined_df.astype(float).to_sql(staging_table, conn, if_exists="replace", index=True, index_label='Date')

        # Validate
        cursor.execute(f"SELECT COUNT(*) FROM {staging_table}")
        staging_count = cursor.fetchone()[0]

        if staging_count == len(combined_df):
            # Atomic swap
            cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_old")
            if table_exists:
                cursor.execute("ALTER TABLE stock_prices_daily RENAME TO stock_prices_daily_old")
            cursor.execute(f"ALTER TABLE {staging_table} RENAME TO stock_prices_daily")
            conn.commit()
            print(f"  SUCCESS: Database updated with {staging_count} rows")

            # Show latest data
            cursor.execute("SELECT Date FROM stock_prices_daily ORDER BY Date DESC LIMIT 1")
            latest_date = cursor.fetchone()[0]
            print(f"  Latest data: {latest_date}")
        else:
            print(f"  ERROR: Row count mismatch. Rolling back.")
            cursor.execute(f"DROP TABLE IF EXISTS {staging_table}")
            conn.commit()

    finally:
        conn.close()

    print("\nUpdate complete!")

if __name__ == "__main__":
    main()