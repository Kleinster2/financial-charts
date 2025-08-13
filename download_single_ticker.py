"""Download and save a single ticker to the database.

Example usage:
    python download_single_ticker.py MSTR
"""

import sys
import sqlite3
import pandas as pd
import yfinance as yf
from datetime import datetime

def download_and_save_ticker(ticker: str, start_date: str = "2019-12-31") -> None:
    """Download a single ticker and save it to the database."""
    print(f"Downloading {ticker} data from {start_date} to {datetime.today().strftime('%Y-%m-%d')}...")
    
    # Download full history via single-ticker endpoint (Approach B)
    ticker_obj = yf.Ticker(ticker)
    data = ticker_obj.history(period="max", interval="1d", auto_adjust=True)
    if data.empty:
        print(f"No data found for {ticker}")
        return
    # Trim to start_date (handle timezone-aware index)
    idx = data.index
    if idx.tz is not None:
        idx = idx.tz_convert(None)
    data = data.loc[idx >= pd.to_datetime(start_date)]
    
    # Connect to the database
    conn = sqlite3.connect("sp500_data.db")
    
    try:
        # Prepare data for database
        data = data[['Close']].copy()  # We only need Close for prices
        data.columns = [ticker]  # Rename column to ticker
        data.index.name = 'Date'
        data = data.reset_index()
        
        cursor = conn.cursor()
        # Ensure base table exists
        cursor.execute("CREATE TABLE IF NOT EXISTS stock_prices_daily (Date TEXT PRIMARY KEY)")
        # Ensure ticker column exists
        try:
            cursor.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{ticker}" REAL')
        except sqlite3.OperationalError:
            # Column already exists
            pass
        
        # Insert or replace data
        data.to_sql('temp_table', conn, if_exists='replace', index=False)
        
        # Merge with existing data
        cursor.execute(f"""
            INSERT OR REPLACE INTO stock_prices_daily (Date, "{ticker}")
            SELECT Date, "{ticker}" FROM temp_table
        """)
        
        conn.commit()
        print(f"Successfully updated {ticker} with {len(data)} data points")
        
    except Exception as e:
        print(f"Error saving {ticker} to database: {e}")
        conn.rollback()
    finally:
        # Clean up
        cursor.execute("DROP TABLE IF EXISTS temp_table")
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_single_ticker.py TICKER")
        sys.exit(1)
        
    ticker = sys.argv[1].upper()
    download_and_save_ticker(ticker)
