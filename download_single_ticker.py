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
# Prefer explicit entries when known; will also try a dynamic fallback pattern.
CBOE_INDEX_URLS = {
    '^BXY': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/BXY_History.csv',
    '^BXM': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/BXM_History.csv',
    '^BXMD': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/BXMD_History.csv',
    '^PUT': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/PUT_History.csv',
    '^PPUT': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/PPUT_History.csv',
    '^BXD': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/BXD_History.csv',
    '^CLL': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/CLL_History.csv',
    '^CLLZ': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/CLLZ_History.csv',
    '^VVIX': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/VVIX_History.csv',
    '^SKEW': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv',
    '^VIX1D': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX1D_History.csv',
    '^VIX9D': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX9D_History.csv',
    '^VIX3M': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX3M_History.csv',
    '^VIX6M': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX6M_History.csv',
    '^RVX': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/RVX_History.csv',
    '^VXN': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/VXN_History.csv',
    '^VXD': 'https://cdn.cboe.com/api/global/us_indices/daily_prices/VXD_History.csv',
}

def _cboe_candidate_urls(ticker: str) -> list[str]:
    base = ticker.lstrip('^').upper()
    # Primary known pattern
    candidates = [
        CBOE_INDEX_URLS.get(ticker),
        f'https://cdn.cboe.com/api/global/us_indices/daily_prices/{base}_History.csv',
    ]
    return [u for u in candidates if u]

def _try_fetch_cboe_csv(ticker: str, start_date: str) -> pd.DataFrame:
    """Attempt to fetch Cboe CSV for the given ticker and return standardized DataFrame ['Date', ticker].
    Returns empty DataFrame on failure.
    """
    for url in _cboe_candidate_urls(ticker):
        try:
            print(f"Fetching from Cboe CSV: {url}")
            raw = pd.read_csv(url)
            # Normalize column names for robust parsing
            cols_norm = {c: c.strip() for c in raw.columns}
            raw = raw.rename(columns=cols_norm)
            # Find date column (case-insensitive)
            date_col = None
            for c in raw.columns:
                if c.lower() == 'date':
                    date_col = c
                    break
            if not date_col:
                print(f"Cboe CSV missing a 'Date' column: columns={list(raw.columns)}")
                continue
            # Choose value column: prefer exact base symbol, else common names
            base = ticker.lstrip('^').upper()
            value_col = None
            priority = [base, 'CLOSE', 'Close', 'Index Value', 'INDEX VALUE', 'VALUE']
            for c in priority:
                if c in raw.columns:
                    value_col = c
                    break
            if value_col is None:
                # Pick first non-date numeric-like column
                non_date = [c for c in raw.columns if c != date_col]
                if non_date:
                    value_col = non_date[0]
            if value_col is None:
                print(f"Could not identify value column for {ticker} in {url}; columns={list(raw.columns)}")
                continue

            df = raw[[date_col, value_col]].copy()
            df.rename(columns={date_col: 'Date', value_col: ticker}, inplace=True)
            # Parse dates; handle both m/d/Y and Y-m-d by coercion
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
            df = df.dropna(subset=['Date'])
            # Coerce numeric values
            df[ticker] = pd.to_numeric(df[ticker], errors='coerce')
            df = df.dropna(subset=[ticker])
            df = df.sort_values('Date')
            # Filter by start_date
            df = df[df['Date'] >= pd.to_datetime(start_date)]
            # Standardize date format
            df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
            print(f"Cboe CSV parsed for {ticker}: rows={len(df)}, cols={list(df.columns)}")
            return df[['Date', ticker]].copy()
        except Exception as e:
            print(f"Cboe fetch failed for {ticker} at {url}: {e}")
            continue
    return pd.DataFrame()

def download_and_save_ticker(ticker: str, start_date: str = "2019-12-31") -> None:
    """Download a single ticker and save it to the database."""
    print(f"Downloading {ticker} data from {start_date} to {datetime.today().strftime('%Y-%m-%d')}...")
    
    # 1) Try Cboe direct CSV for supported indices (e.g., ^BXY and others)
    data = _try_fetch_cboe_csv(ticker, start_date)

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
