#!/usr/bin/env python
"""
Update economic indicators from FRED.
Run this after the main market data update to keep macro indicators current.
"""

import sys
import pandas as pd
from datetime import datetime, timedelta
from constants import DB_PATH, get_db_connection
from fred_utils import download_from_fred

# FRED economic indicators currently in database
FRED_INDICATORS = {
    # Treasury yields (daily)
    'DGS2': '2-Year Treasury',
    'DGS10': '10-Year Treasury',
    'DGS30': '30-Year Treasury',
    'T10Y2Y': '10Y-2Y Spread',

    # Fed policy (monthly/daily)
    'FEDFUNDS': 'Fed Funds Rate',
    'DFEDTARU': 'Fed Target Upper',
    'DFEDTARL': 'Fed Target Lower',

    # Inflation (monthly)
    'CPIAUCSL': 'CPI All Items',
    'CPILFESL': 'Core CPI',
    'T5YIE': '5Y Breakeven Inflation',
    'T10YIE': '10Y Breakeven Inflation',

    # Credit spreads (daily)
    'BAMLH0A0HYM2': 'High Yield Spread',
    'BAMLC0A0CM': 'Corporate Spread',
}

# Add Tier 2 indicators if they've been downloaded
TIER2_INDICATORS = {
    # Labor (monthly)
    'UNRATE': 'Unemployment Rate',
    'PAYEMS': 'Nonfarm Payrolls',
    'CIVPART': 'Labor Force Participation',
    'U6RATE': 'U6 Unemployment',

    # Economic activity
    'GDP': 'GDP',
    'GDPC1': 'Real GDP',
    'UMCSENT': 'Consumer Sentiment',
    'RSXFS': 'Retail Sales',

    # Liquidity
    'WALCL': 'Fed Balance Sheet',
    'RRPONTSYD': 'Reverse Repo',
    'WTREGEN': 'Treasury General Account',

    # Financial stress
    'STLFSI4': 'Financial Stress Index',
    'TEDRATE': 'TED Spread',

    # Commodities (daily)
    'DCOILWTICO': 'WTI Crude Oil',
    'GOLDAMGBD228NLBM': 'Gold Price',
    'DCOILBRENTEU': 'Brent Crude',

    # Forex (daily)
    'DEXCHUS': 'CNY/USD',
    'DEXJPUS': 'JPY/USD',
    'DEXUSEU': 'USD/EUR',

    # Brazil interest rates (monthly)
    'INTDSRBRM193N': 'Brazil SELIC Rate',
    'IRSTCI01BRM156N': 'Brazil CDI Rate',
    'INTGSTBRM193N': 'Brazil T-Bill Rate',

    # ECB/Euro rates (daily)
    'ECBDFR': 'ECB Deposit Rate',
    'ECBESTRVOLWGTTRMDMNRT': 'Euro STR (overnight)',
    'ECBMRRFR': 'ECB Main Refi Rate',
    'ECBMLFR': 'ECB Marginal Lending Rate',
}

def get_existing_indicators(conn):
    """Check which FRED indicators are already in the database."""
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(stock_prices_daily)")
    columns = [row[1] for row in cursor.fetchall()]

    existing = {}
    for code in list(FRED_INDICATORS.keys()) + list(TIER2_INDICATORS.keys()):
        if code in columns:
            existing[code] = FRED_INDICATORS.get(code) or TIER2_INDICATORS.get(code)

    return existing

def update_fred_indicators(lookback_days=60):
    """
    Update FRED economic indicators.

    Args:
        lookback_days: How many days back to check/update (default 60 for monthly data)
    """
    print("Updating FRED Economic Indicators")
    print("="*60)
    print(f"Looking back {lookback_days} days for updates")
    print()

    cutoff_date = datetime.now() - timedelta(days=lookback_days)

    # Check which indicators exist in database
    conn = get_db_connection(row_factory=None)
    try:
        existing_indicators = get_existing_indicators(conn)
        conn.close()
    except Exception as e:
        print(f"ERROR checking database: {e}")
        return False

    if not existing_indicators:
        print("No FRED indicators found in database.")
        print("Run 'python download_fred_indicators.py' first to add indicators.")
        return False

    print(f"Found {len(existing_indicators)} FRED indicators in database")
    print()

    all_updates = {}

    for i, (code, description) in enumerate(existing_indicators.items(), 1):
        print(f"[{i}/{len(existing_indicators)}] {code:20} {description:25}...", end=" ")

        data = download_from_fred(code)

        if data is not None and not data.empty:
            # Filter to recent data only
            recent_data = data[data.index >= cutoff_date]

            if not recent_data.empty:
                all_updates[code] = recent_data
                print(f"OK ({len(recent_data):3} new points, latest {recent_data.index[-1].strftime('%Y-%m-%d')})")
            else:
                print("OK (no new data)")
        else:
            print("FAIL")

    if not all_updates:
        print("\nNo updates needed - all indicators are current")
        return True

    # Update database
    print(f"\nUpdating database with {len(all_updates)} indicators...")

    conn = get_db_connection(row_factory=None)
    try:
        existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
        existing_df['Date'] = pd.to_datetime(existing_df['Date'])
        existing_df.set_index('Date', inplace=True)

        # Update each indicator
        combined_df = existing_df.copy()

        for code, data in all_updates.items():
            if code not in combined_df.columns:
                combined_df[code] = pd.NA

            # Update with new data
            for date in data.index:
                combined_df.loc[date, code] = data.loc[date, 'Close']

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
        for code in all_updates.keys():
            cursor.execute(f'''
                SELECT MAX(Date)
                FROM stock_prices_daily
                WHERE "{code}" IS NOT NULL
            ''')
            latest = cursor.fetchone()[0]
            if latest:
                print(f"  {code:20} latest: {latest[:10]}")

        conn.close()
        return True

    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        conn.close()
        return False

def update_b3_yield_curve(lookback_days=10):
    """Update B3 DI yield curve data (incremental)."""
    try:
        from fetch_b3_yield_curve import fetch_historical_curves, update_database
        from datetime import datetime, timedelta

        print("\nUpdating B3 DI Yield Curve")
        print("="*60)

        end_date = datetime.now()
        start_date = end_date - timedelta(days=lookback_days)

        df = fetch_historical_curves(start_date, end_date, verbose=True)

        if not df.empty:
            update_database(df, verbose=True)
            return True
        else:
            print("No new B3 data available")
            return True
    except ImportError:
        print("B3 yield curve module not available (fetch_b3_yield_curve.py)")
        return True
    except Exception as e:
        print(f"ERROR updating B3: {e}")
        return False


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Update FRED economic indicators')
    parser.add_argument('--lookback', type=int, default=60,
                       help='Days to look back for updates (default: 60 for monthly data)')
    parser.add_argument('--skip-b3', action='store_true',
                       help='Skip B3 yield curve update')

    args = parser.parse_args()

    success = update_fred_indicators(lookback_days=args.lookback)

    # Also update B3 yield curve (daily data, shorter lookback)
    if not args.skip_b3:
        b3_success = update_b3_yield_curve(lookback_days=min(args.lookback, 10))
        success = success and b3_success

    sys.exit(0 if success else 1)
