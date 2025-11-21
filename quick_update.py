#!/usr/bin/env python
"""Quick update script to get November 20, 2025 closing prices for key tickers."""

import yfinance as yf
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
from constants import DB_PATH, get_db_connection

# Key tickers to update
KEY_TICKERS = ["SPY", "QQQ", "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "BRK-B"]

def main():
    print("Quick Update - Fetching Nov 20, 2025 closing prices")
    print("="*60)

    # Date range - just the last few days
    START_DATE = "2025-11-18"
    END_DATE = "2025-11-21"

    print(f"Downloading data for {len(KEY_TICKERS)} key tickers...")
    print(f"Date range: {START_DATE} to {END_DATE}")
    print()

    # Download data
    data = yf.download(KEY_TICKERS, start=START_DATE, end=END_DATE, auto_adjust=True, group_by='ticker')

    if data.empty:
        print("ERROR: No data returned")
        return

    # Process data
    processed_dfs = []
    for ticker in KEY_TICKERS:
        if ticker in data:
            ticker_data = data[ticker] if len(KEY_TICKERS) > 1 else data
            close_series = ticker_data[['Close']].rename(columns={'Close': ticker})
            processed_dfs.append(close_series)
            latest_close = close_series.iloc[-1][ticker]
            latest_date = close_series.index[-1].strftime('%Y-%m-%d')
            print(f"{ticker:10} Latest: {latest_date} Close: ${latest_close:.2f}")

    if not processed_dfs:
        print("No data to update")
        return

    # Combine data
    new_data_df = pd.concat(processed_dfs, axis=1)
    new_data_df.index = pd.to_datetime(new_data_df.index)

    print()
    print(f"Latest market date in data: {new_data_df.index[-1].strftime('%Y-%m-%d')}")

    # Update database
    print("\nUpdating database...")
    conn = get_db_connection(row_factory=None)

    try:
        cursor = conn.cursor()

        # Load existing data
        existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
        if not existing_df.empty and 'Date' in existing_df.columns:
            existing_df['Date'] = pd.to_datetime(existing_df['Date'])
            existing_df.set_index('Date', inplace=True)

        print(f"Existing data: {len(existing_df)} rows")

        # Merge with new data
        for ticker in KEY_TICKERS:
            if ticker in new_data_df.columns:
                for date in new_data_df.index:
                    if ticker in existing_df.columns:
                        existing_df.loc[date, ticker] = new_data_df.loc[date, ticker]

        # Sort by date
        existing_df = existing_df.sort_index()

        # Save back to database
        staging_table = "stock_prices_daily_staging"
        existing_df.astype(float).to_sql(staging_table, conn, if_exists="replace", index=True, index_label='Date')

        # Atomic swap
        cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_old")
        cursor.execute("ALTER TABLE stock_prices_daily RENAME TO stock_prices_daily_old")
        cursor.execute(f"ALTER TABLE {staging_table} RENAME TO stock_prices_daily")
        conn.commit()

        # Verify
        cursor.execute("SELECT Date FROM stock_prices_daily ORDER BY Date DESC LIMIT 1")
        latest_db_date = cursor.fetchone()[0]
        print(f"SUCCESS: Database updated. Latest date: {latest_db_date}")

        # Check a few tickers
        cursor.execute("SELECT SPY, AAPL, MSFT FROM stock_prices_daily ORDER BY Date DESC LIMIT 1")
        latest_prices = cursor.fetchone()
        print(f"Latest prices - SPY: ${latest_prices[0]:.2f}, AAPL: ${latest_prices[1]:.2f}, MSFT: ${latest_prices[2]:.2f}")

    finally:
        conn.close()

    print("\nUpdate complete!")

if __name__ == "__main__":
    main()