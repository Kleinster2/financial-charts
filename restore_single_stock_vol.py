#!/usr/bin/env python
"""
Restore single-stock volatility indices.
"""

import sys
import time
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from constants import DB_PATH, get_db_connection

# Single-stock volatility indices
SINGLE_STOCK_VOL_INDICES = [
    '^VXAPL',   # Apple volatility
    '^VXAZN',   # Amazon volatility
    '^VXGOG',   # Google volatility
    '^VXGS',    # Goldman Sachs volatility
    '^VXIBM'    # IBM volatility
]

def restore_single_stock_vol():
    """Download and restore single-stock volatility indices."""
    print(f"Restoring {len(SINGLE_STOCK_VOL_INDICES)} single-stock volatility indices...")
    print(f"Date range: 2010-01-01 to {datetime.today().strftime('%Y-%m-%d')}")
    print("="*60)

    # Download data (start from 2010 as these are likely newer indices)
    start_date = "2010-01-01"
    end_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    all_data = {}
    failed = []

    for i, ticker in enumerate(SINGLE_STOCK_VOL_INDICES, 1):
        print(f"[{i}/{len(SINGLE_STOCK_VOL_INDICES)}] Downloading {ticker}...", end=" ")
        try:
            data = yf.download(
                ticker,
                start=start_date,
                end=end_date,
                auto_adjust=True,
                progress=False,
                timeout=15
            )

            if isinstance(data, pd.DataFrame) and not data.empty:
                # Handle MultiIndex columns from yfinance
                if isinstance(data.columns, pd.MultiIndex):
                    # Flatten MultiIndex columns
                    data.columns = data.columns.get_level_values(0)

                if 'Close' in data.columns:
                    close_col = data['Close']
                    if not close_col.isna().all():
                        all_data[ticker] = data
                        first_date = data.index[0].strftime('%Y-%m-%d')
                        last_date = data.index[-1].strftime('%Y-%m-%d')
                        print(f"OK ({len(data)} days, {first_date} to {last_date})")
                    else:
                        failed.append(ticker)
                        print("FAIL (no data)")
                else:
                    failed.append(ticker)
                    print("FAIL (no Close column)")
            else:
                failed.append(ticker)
                print("FAIL (empty)")
        except Exception as e:
            failed.append(ticker)
            print(f"FAIL ({str(e)[:50]})")

        time.sleep(0.3)  # Brief pause to avoid rate limiting

    print("\n" + "="*60)
    print(f"Downloaded: {len(all_data)}/{len(SINGLE_STOCK_VOL_INDICES)} indices")
    if failed:
        print(f"Failed: {', '.join(failed)}")

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
                print(f"  {ticker:12} {result[0]:5} days, from {result[1][:10]} to {result[2][:10]}")

        return True

    except Exception as e:
        print(f"ERROR: Database update failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    success = restore_single_stock_vol()
    sys.exit(0 if success else 1)
