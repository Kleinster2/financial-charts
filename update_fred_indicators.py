#!/usr/bin/env python
"""
Update economic indicators from FRED.
Run this after the main market data update to keep macro indicators current.
"""

import os
import sys
import pandas as pd
from datetime import datetime, timedelta
from constants import DB_PATH, get_db_connection

# Narrow-format dual-write
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'charting_app'))
try:
    from sqlite_queries import sync_wide_to_narrow, check_narrow_available
    NARROW_SYNC = check_narrow_available()
except ImportError:
    NARROW_SYNC = False
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
    # TODO (post-narrow-FRED migration): seed DFF, SOFR, IORB. Blocked by
    # wide-table column limit — see download_fred_indicators.py fed_policy.

    # Inflation (monthly)
    'CPIAUCSL': 'CPI All Items',
    'CPILFESL': 'Core CPI',
    'T5YIE': '5Y Breakeven Inflation',
    'T10YIE': '10Y Breakeven Inflation',

    # Credit spreads (daily)
    'BAMLH0A0HYM2': 'High Yield Spread',
    'BAMLC0A0CM': 'Corporate Spread',
}

# FRED series stored only in prices_long. stock_prices_daily is at SQLite's
# 2000-column limit, so new macro series should enter through the narrow table.
NARROW_ONLY_FRED_INDICATORS = {
    'DGS5': '5-Year Treasury',
    'DFII5': '5-Year TIPS Real Yield',
    'DFII10': '10-Year TIPS Real Yield',
    'DFII30': '30-Year TIPS Real Yield',
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

def get_latest_narrow_date(conn, ticker):
    """Return latest date for a ticker in prices_long, or None if absent."""
    try:
        row = conn.execute(
            """
            SELECT MAX(Date)
            FROM prices_long
            WHERE Ticker = ? AND Close IS NOT NULL
            """,
            (ticker,),
        ).fetchone()
        return row[0] if row else None
    except Exception:
        return None

def refresh_fred_metadata(codes, descriptions):
    """Refresh ticker_metadata for FRED series present in prices_long."""
    if not codes:
        return

    conn = get_db_connection(row_factory=None)
    try:
        for code in codes:
            row = conn.execute(
                """
                SELECT MIN(Date), MAX(Date), COUNT(*)
                FROM prices_long
                WHERE Ticker = ? AND Close IS NOT NULL
                """,
                (code,),
            ).fetchone()
            if not row or not row[0]:
                continue

            conn.execute(
                """
                INSERT INTO ticker_metadata
                    (ticker, name, table_name, data_type, first_date, last_date, data_points)
                VALUES (?, ?, 'prices_long', 'macro', ?, ?, ?)
                ON CONFLICT(ticker) DO UPDATE SET
                    name = excluded.name,
                    table_name = excluded.table_name,
                    data_type = excluded.data_type,
                    first_date = excluded.first_date,
                    last_date = excluded.last_date,
                    data_points = excluded.data_points
                """,
                (code, descriptions.get(code, code), row[0], row[1], row[2]),
            )
        conn.commit()
    finally:
        conn.close()

def sync_fred_narrow_only(narrow_updates):
    """Write narrow-only FRED series to prices_long and ticker_metadata."""
    if not narrow_updates:
        return True

    if not NARROW_SYNC:
        print("  [Narrow] prices_long unavailable; skipped narrow-only FRED series")
        return False

    narrow_df = pd.concat(
        [data['Close'].rename(code) for code, data in narrow_updates.items()],
        axis=1,
    ).sort_index()

    try:
        sync_wide_to_narrow(narrow_df, table='prices_long', value_col='Close', verbose=True)
        refresh_fred_metadata(narrow_updates.keys(), NARROW_ONLY_FRED_INDICATORS)

        return True
    except Exception as e:
        print(f"  [Narrow] ERROR syncing narrow-only FRED series: {e}")
        return False

def update_fred_indicators(lookback_days=60, codes=None):
    """
    Update FRED economic indicators.

    Args:
        lookback_days: How many days back to check/update (default 60 for monthly data)
        codes: Optional iterable of FRED codes to update.
    """
    print("Updating FRED Economic Indicators")
    print("="*60)
    print(f"Looking back {lookback_days} days for updates")
    print()

    selected_codes = {code.upper() for code in codes} if codes else None

    cutoff_date = datetime.now() - timedelta(days=lookback_days)

    # Check which indicators exist in database
    conn = get_db_connection(row_factory=None)
    try:
        existing_indicators = get_existing_indicators(conn)
        conn.close()
    except Exception as e:
        print(f"ERROR checking database: {e}")
        return False

    if selected_codes:
        existing_indicators = {
            code: description
            for code, description in existing_indicators.items()
            if code in selected_codes
        }

    if not existing_indicators:
        if selected_codes:
            print("No selected wide FRED indicators found in stock_prices_daily.")
        else:
            print("No FRED indicators found in database.")
            print("Run 'python download_fred_indicators.py' first to add indicators.")
            return False

    print(f"Found {len(existing_indicators)} FRED indicators in database")
    print()

    wide_updates = {}
    narrow_updates = {}

    for i, (code, description) in enumerate(existing_indicators.items(), 1):
        print(f"[{i}/{len(existing_indicators)}] {code:20} {description:25}...", end=" ")

        data = download_from_fred(code)

        if data is not None and not data.empty:
            # Filter to recent data only
            recent_data = data[data.index >= cutoff_date]

            if not recent_data.empty:
                wide_updates[code] = recent_data
                print(f"OK ({len(recent_data):3} new points, latest {recent_data.index[-1].strftime('%Y-%m-%d')})")
            else:
                print("OK (no new data)")
        else:
            print("FAIL")

    print()
    narrow_indicators = {
        code: description
        for code, description in NARROW_ONLY_FRED_INDICATORS.items()
        if selected_codes is None or code in selected_codes
    }

    print(f"Checking {len(narrow_indicators)} narrow-only FRED indicators")
    conn = get_db_connection(row_factory=None)
    try:
        narrow_latest = {
            code: get_latest_narrow_date(conn, code)
            for code in narrow_indicators
        }
    finally:
        conn.close()

    for i, (code, description) in enumerate(narrow_indicators.items(), 1):
        latest = narrow_latest.get(code)
        filter_cutoff = datetime(1900, 1, 1) if latest is None else cutoff_date
        seed_note = "seed" if latest is None else "update"
        print(f"[{i}/{len(narrow_indicators)}] {code:20} {description:25} ({seed_note})...", end=" ")

        data = download_from_fred(code)

        if data is not None and not data.empty:
            recent_data = data[data.index >= filter_cutoff]
            if not recent_data.empty:
                narrow_updates[code] = recent_data
                print(f"OK ({len(recent_data):3} points, latest {recent_data.index[-1].strftime('%Y-%m-%d')})")
            else:
                print("OK (no new data)")
        else:
            print("FAIL")

    if not wide_updates and not narrow_updates:
        print("\nNo updates needed - all indicators are current")
        return True

    narrow_success = True
    if narrow_updates:
        print(f"\nUpdating prices_long with {len(narrow_updates)} narrow-only indicators...")
        narrow_success = sync_fred_narrow_only(narrow_updates)

        print("\nNarrow-only verification:")
        conn = get_db_connection(row_factory=None)
        try:
            for code in narrow_updates:
                row = conn.execute(
                    """
                    SELECT MIN(Date), MAX(Date), COUNT(*)
                    FROM prices_long
                    WHERE Ticker = ? AND Close IS NOT NULL
                    """,
                    (code,),
                ).fetchone()
                if row and row[0]:
                    print(f"  {code:20} {row[2]:5} rows, {row[0][:10]} to {row[1][:10]}")
        finally:
            conn.close()

    if not wide_updates:
        return narrow_success

    # Update database
    print(f"\nUpdating stock_prices_daily with {len(wide_updates)} wide indicators...")

    conn = get_db_connection(row_factory=None)
    try:
        existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
        existing_df['Date'] = pd.to_datetime(existing_df['Date'])
        existing_df.set_index('Date', inplace=True)

        # Update each indicator
        combined_df = existing_df.copy()

        for code, data in wide_updates.items():
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

        # Sync to narrow-format table
        if NARROW_SYNC:
            try:
                sync_wide_to_narrow(
                    combined_df[list(wide_updates.keys())],
                    table='prices_long',
                    value_col='Close',
                    verbose=True,
                )
                refresh_fred_metadata(wide_updates.keys(), existing_indicators)
            except Exception as e:
                print(f"  [Narrow] Warning: sync failed: {e}")

        # Verify
        print("\nVerification:")
        for code in wide_updates.keys():
            cursor.execute(f'''
                SELECT MAX(Date)
                FROM stock_prices_daily
                WHERE "{code}" IS NOT NULL
            ''')
            latest = cursor.fetchone()[0]
            if latest:
                print(f"  {code:20} latest: {latest[:10]}")

        conn.close()
        return narrow_success

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
    parser.add_argument('--codes', nargs='+',
                       help='Optional FRED codes to update, e.g. DGS5 DFII5 DFII10 DFII30')
    parser.add_argument('--skip-b3', action='store_true',
                       help='Skip B3 yield curve update')

    args = parser.parse_args()

    success = update_fred_indicators(lookback_days=args.lookback, codes=args.codes)

    # Also update B3 yield curve (daily data, shorter lookback)
    if not args.skip_b3:
        b3_success = update_b3_yield_curve(lookback_days=min(args.lookback, 10))
        success = success and b3_success

    sys.exit(0 if success else 1)
