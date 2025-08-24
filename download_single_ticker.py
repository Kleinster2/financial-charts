"""Download and save a single ticker to the database.

Example usage:
    python download_single_ticker.py MSTR [START_DATE]
"""

import sys
import sqlite3
import pandas as pd
import yfinance as yf
from datetime import datetime
import os

# Allow importing constants from repo root when run from anywhere
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from constants import DB_PATH, get_db_connection

# Known Cboe index CSV endpoints (symbol -> URL)
CBOE_INDEX_URLS = {
    '^BXY': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/BXY_History.csv',
}

def download_and_save_ticker(ticker: str, start_date: str = "2019-12-31") -> None:
    """Download a single ticker and save it to the database."""
    print(f"Downloading {ticker} data from {start_date} to {datetime.today().strftime('%Y-%m-%d')}...")
    
    # 1) Try Cboe direct CSV for supported indices (e.g., ^BXY)
    data = pd.DataFrame()
    if ticker in CBOE_INDEX_URLS:
        url = CBOE_INDEX_URLS[ticker]
        try:
            print(f"Fetching from Cboe CSV: {url}")
            cboe = pd.read_csv(url)
            # Expect columns: DATE, <INDEX>
            if {'DATE'}.issubset(cboe.columns):
                # Identify value column (use the second column if present)
                value_col = [c for c in cboe.columns if c != 'DATE'][0]
                cboe.rename(columns={'DATE': 'Date', value_col: ticker}, inplace=True)
                cboe['Date'] = pd.to_datetime(cboe['Date'], format='%m/%d/%Y', errors='coerce')
                cboe = cboe.dropna(subset=['Date'])
                cboe = cboe.sort_values('Date')
                # Filter by start_date
                cboe = cboe[cboe['Date'] >= pd.to_datetime(start_date)]
                # Standardize date format
                cboe['Date'] = cboe['Date'].dt.strftime('%Y-%m-%d')
                data = cboe[['Date', ticker]].copy()
        except Exception as e:
            print(f"Cboe fetch failed for {ticker}: {e}")

    # 2) If Cboe not available or failed, try yfinance
    if data.empty:
        # Prefer yf.download for broader compatibility
        ticker_obj = yf.Ticker(ticker)
        data_dl = yf.download(ticker, start=start_date, interval="1d", auto_adjust=True, progress=False)
        if data_dl is None or data_dl.empty:
            # Fallback to Ticker.history for tickers where download fails
            try:
                data_dl = ticker_obj.history(period="max", interval="1d", auto_adjust=True)
            except Exception as e:
                print(f"yfinance history error for {ticker}: {e}")
                data_dl = pd.DataFrame()
        if data_dl.empty:
            print(f"No data found for {ticker}")
            return
        # Normalize to Date + ticker columns
        data = data_dl[['Close']].copy()
        data.columns = [ticker]
        data.index.name = 'Date'
        data = data.reset_index()
        data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
    # Data already filtered by start_date via CSV filter or yf.download(start=...)
    
    # Connect to the database in the project root
    print(f"Using database: {DB_PATH}")
    conn = get_db_connection(row_factory=None)
    
    try:
        # Data is already shaped as ['Date', ticker]
        
        cursor = conn.cursor()
        # Ensure base table exists
        cursor.execute("CREATE TABLE IF NOT EXISTS stock_prices_daily (Date TEXT PRIMARY KEY)")
        # Ensure ticker column exists
        try:
            cursor.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{ticker}" REAL')
        except sqlite3.OperationalError:
            # Column already exists
            pass
        
        # Stage incoming data into a temp table
        data.to_sql('temp_table', conn, if_exists='replace', index=False)

        # Portable upsert without clobbering other tickers' columns
        # 1) UPDATE existing dates
        cursor.execute(f"""
            UPDATE stock_prices_daily
            SET "{ticker}" = (
                SELECT t."{ticker}" FROM temp_table t WHERE t.Date = stock_prices_daily.Date
            )
            WHERE EXISTS (
                SELECT 1 FROM temp_table t WHERE t.Date = stock_prices_daily.Date
            )
        """)

        # 2) INSERT rows that don't exist yet
        cursor.execute(f"""
            INSERT INTO stock_prices_daily (Date, "{ticker}")
            SELECT t.Date, t."{ticker}"
            FROM temp_table t
            WHERE NOT EXISTS (
                SELECT 1 FROM stock_prices_daily s WHERE s.Date = t.Date
            )
        """)

        conn.commit()
        # Verify range for this ticker in DB
        mn, mx, cnt = cursor.execute(
            f'SELECT date(min(Date)), date(max(Date)), COUNT(1) FROM stock_prices_daily WHERE "{ticker}" IS NOT NULL'
        ).fetchone()
        print(f"Successfully updated {ticker}: rows={len(data)}, db_range={mn} -> {mx}, non_null_rows={cnt}")
        
    except Exception as e:
        print(f"Error saving {ticker} to database: {e}")
        conn.rollback()
    finally:
        # Clean up
        cursor.execute("DROP TABLE IF EXISTS temp_table")
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Usage: python download_single_ticker.py TICKER [START_DATE]")
        sys.exit(1)

    ticker = sys.argv[1].upper()
    start_date = sys.argv[2] if len(sys.argv) == 3 else "2019-12-31"
    download_and_save_ticker(ticker, start_date)
