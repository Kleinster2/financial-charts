"""
update_fx_ny_close.py - Update FX prices to use 4pm EST (NY market close) instead of daily bars

This script downloads hourly FX data and extracts the 21:00 UTC (4pm EST) close price,
which aligns with the NY stock market close time for proper comparison.
"""

import yfinance as yf
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import pytz
from constants import DB_PATH


def get_fx_tickers_from_db(db_path=None, include_crypto=True):
    """Get list of FX tickers (=X suffix) and optionally crypto (-USD) from the database."""
    db_path = db_path or DB_PATH
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM pragma_table_info("stock_prices_daily")')
    cols = [r[0] for r in cursor.fetchall()]
    conn.close()

    # Filter to FX tickers (ending with =X)
    fx_tickers = [c for c in cols if c.endswith('=X')]

    # Optionally include crypto tickers (ending with -USD)
    if include_crypto:
        crypto_tickers = [c for c in cols if c.endswith('-USD')]
        fx_tickers.extend(crypto_tickers)

    return fx_tickers


def download_fx_at_ny_close(fx_tickers, period='5d', verbose=True):
    """
    Download FX data using hourly candles and extract the 4pm EST (21:00 UTC) close.

    Args:
        fx_tickers: List of FX tickers (e.g., ['USDBRL=X', 'EURUSD=X'])
        period: Period for historical data (default: '5d' for recent data, use '1mo' for more)
        verbose: Print progress messages

    Returns:
        DataFrame with Date index and FX ticker columns containing 4pm EST close prices
    """
    if not fx_tickers:
        return pd.DataFrame()

    if verbose:
        print(f"Downloading FX at NY close (4pm EST) for {len(fx_tickers)} pairs (period={period})...")

    all_results = {}

    # Download in batches to avoid API limits
    batch_size = 20
    for i in range(0, len(fx_tickers), batch_size):
        batch = fx_tickers[i:i+batch_size]
        if verbose:
            print(f"  Batch {i//batch_size + 1}: {batch[:3]}...")

        try:
            # Download hourly data - use period instead of start date for recent data
            data = yf.download(batch, period=period, interval='1h',
                             auto_adjust=True, group_by='ticker', progress=False)

            if data.empty:
                continue

            # Extract 21:00 UTC (4pm EST) candle for each ticker
            for ticker in batch:
                try:
                    if len(batch) == 1:
                        ticker_data = data
                    elif ticker in data.columns.get_level_values(0):
                        ticker_data = data[ticker]
                    else:
                        continue

                    if ticker_data.empty or 'Close' not in ticker_data.columns:
                        continue

                    closes = ticker_data['Close'].copy()
                    closes.index = pd.to_datetime(closes.index)

                    # Group by date and get the 21:00 or 20:00 UTC value
                    # 4pm EST = 21:00 UTC (standard time) or 20:00 UTC (DST)
                    daily_closes = {}
                    for dt, price in closes.items():
                        date = dt.date()
                        hour = dt.hour
                        # Prefer 21:00 UTC, but accept 20:00 (DST) or 22:00 (backup)
                        if hour in [20, 21, 22]:
                            if date not in daily_closes or hour == 21:
                                daily_closes[date] = price

                    if daily_closes:
                        all_results[ticker] = pd.Series(daily_closes, name=ticker)

                except Exception as e:
                    if verbose:
                        print(f"    Warning: Failed to process {ticker}: {e}")

        except Exception as e:
            if verbose:
                print(f"    Warning: Batch download failed: {e}")

    if not all_results:
        return pd.DataFrame()

    # Combine all tickers into a single DataFrame
    result_df = pd.DataFrame(all_results)
    result_df.index = pd.to_datetime(result_df.index)
    result_df.index.name = 'Date'

    # Filter out future dates - only include dates where 4pm EST has passed
    # Get current time in NY (EST/EDT)
    from datetime import timezone
    import pytz
    ny_tz = pytz.timezone('America/New_York')
    now_ny = datetime.now(ny_tz)

    # Only include a date if it's before today, OR if it's today and past 4pm
    today_ny = now_ny.date()
    cutoff_hour = 16  # 4pm

    if now_ny.hour < cutoff_hour:
        # Before 4pm NY time - exclude today
        max_date = today_ny - timedelta(days=1)
    else:
        # After 4pm NY time - can include today
        max_date = today_ny

    result_df = result_df[result_df.index.date <= max_date]

    if verbose:
        print(f"Downloaded {len(result_df.columns)} FX pairs, {len(result_df)} days (cutoff: {max_date})")

    return result_df


def update_database(fx_df, db_path=None, verbose=True):
    """Update the database with NY close FX prices."""
    db_path = db_path or DB_PATH
    if fx_df.empty:
        print("No FX data to update.")
        return

    conn = sqlite3.connect(db_path)

    # Read existing data
    existing = pd.read_sql('SELECT * FROM stock_prices_daily', conn,
                          index_col='Date', parse_dates=['Date'])

    if verbose:
        print(f"Existing data: {existing.shape}")

    # Safety check: don't proceed if existing data appears corrupted/empty
    if existing.empty or len(existing) < 1000:
        print("ERROR: Existing stock_prices_daily table appears empty or corrupted. Aborting FX update.")
        conn.close()
        return

    # Update FX columns with new NY close data
    updated_count = 0
    for ticker in fx_df.columns:
        if ticker in existing.columns:
            for date in fx_df.index:
                if date in existing.index and pd.notna(fx_df.loc[date, ticker]):
                    old_val = existing.loc[date, ticker]
                    new_val = fx_df.loc[date, ticker]
                    # Ensure scalar values (handle potential duplicate indices)
                    if isinstance(old_val, pd.Series):
                        old_val = old_val.iloc[0]
                    if isinstance(new_val, pd.Series):
                        new_val = new_val.iloc[0]
                    if pd.isna(old_val) or abs(old_val - new_val) > 0.0001:
                        existing.loc[date, ticker] = new_val
                        updated_count += 1

    # Save back - drop orphaned index first if exists
    try:
        conn.execute("DROP INDEX IF EXISTS ix_stock_prices_daily_Date")
    except Exception:
        pass
    existing.to_sql('stock_prices_daily', conn, if_exists='replace', index=True)
    conn.close()

    if verbose:
        print(f"Updated {updated_count} FX values in database")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Update FX prices to NY close')
    parser.add_argument('--period', type=str, default='5d',
                       help='Period to download (default: 5d, options: 1d,5d,1mo,3mo)')
    parser.add_argument('--tickers', nargs='+',
                       help='Specific tickers to update (default: all FX)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Download and show data without updating database')
    args = parser.parse_args()

    # Get tickers
    if args.tickers:
        fx_tickers = args.tickers
    else:
        fx_tickers = get_fx_tickers_from_db()

    print(f"Processing {len(fx_tickers)} FX tickers")

    # Download FX at NY close
    fx_df = download_fx_at_ny_close(fx_tickers, period=args.period)

    if fx_df.empty:
        print("No data downloaded")
    else:
        print(f"\nSample data (last 5 days):")
        print(fx_df.tail())

        if not args.dry_run:
            update_database(fx_df)
            print("\nDatabase updated with NY close FX prices.")
        else:
            print("\nDry run - database not updated.")
