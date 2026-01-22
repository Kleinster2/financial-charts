#!/usr/bin/env python
"""
Download economic indicators from FRED (Federal Reserve Economic Data).
Adds macro context to market data: yields, inflation, Fed policy, employment, etc.
"""

import sys
import pandas as pd
from datetime import datetime
from constants import DB_PATH, get_db_connection
from fred_utils import download_from_fred

# FRED series organized by category
FRED_INDICATORS = {
    # TIER 1: Essential Market Context
    'treasury_yields': {
        'DGS2': '2-Year Treasury Constant Maturity Rate',
        'DGS10': '10-Year Treasury Constant Maturity Rate',
        'DGS30': '30-Year Treasury Constant Maturity Rate',
        'T10Y2Y': '10-Year minus 2-Year Treasury Spread',
    },
    'fed_policy': {
        'FEDFUNDS': 'Effective Federal Funds Rate',
        'DFEDTARU': 'Federal Funds Target Rate - Upper Limit',
        'DFEDTARL': 'Federal Funds Target Rate - Lower Limit',
    },
    'inflation': {
        'CPIAUCSL': 'Consumer Price Index for All Urban Consumers',
        'CPILFESL': 'Consumer Price Index - Core (Less Food & Energy)',
        'T5YIE': '5-Year Breakeven Inflation Rate',
        'T10YIE': '10-Year Breakeven Inflation Rate',
    },
    'credit_spreads': {
        'BAMLH0A0HYM2': 'ICE BofA US High Yield Option-Adjusted Spread',
        'BAMLC0A0CM': 'ICE BofA US Corporate Option-Adjusted Spread',
    },

    # TIER 2: Advanced Indicators
    'labor': {
        'UNRATE': 'Unemployment Rate',
        'PAYEMS': 'All Employees, Total Nonfarm',
        'CIVPART': 'Labor Force Participation Rate',
        'U6RATE': 'Total Unemployed + Marginally Attached + Part-Time',
    },
    'economic_activity': {
        'GDP': 'Gross Domestic Product',
        'GDPC1': 'Real Gross Domestic Product',
        'UMCSENT': 'University of Michigan Consumer Sentiment',
        'RSXFS': 'Advance Retail Sales',
    },
    'liquidity': {
        'WALCL': 'Federal Reserve Total Assets (Balance Sheet)',
        'RRPONTSYD': 'Overnight Reverse Repurchase Agreements',
        'WTREGEN': 'Treasury General Account',
    },
    'financial_stress': {
        'STLFSI4': 'St. Louis Fed Financial Stress Index',
        'TEDRATE': 'TED Spread (3-Month LIBOR - 3-Month T-Bill)',
    },
    'commodities': {
        'DCOILWTICO': 'Crude Oil Prices: West Texas Intermediate (WTI)',
        'GOLDAMGBD228NLBM': 'Gold Fixing Price (London, USD)',
        'DCOILBRENTEU': 'Crude Oil Prices: Brent - Europe',
    },
    'forex': {
        'DEXCHUS': 'China / U.S. Foreign Exchange Rate',
        'DEXJPUS': 'Japan / U.S. Foreign Exchange Rate',
        'DEXUSEU': 'U.S. / Euro Foreign Exchange Rate',
    },
}

# Tier 1 essentials (recommended for all users)
TIER1_CATEGORIES = ['treasury_yields', 'fed_policy', 'inflation', 'credit_spreads']

def download_fred_indicators(tier='1', categories=None):
    """
    Download FRED economic indicators.

    Args:
        tier: '1' for essentials only, '2' for all indicators, 'custom' for specific categories
        categories: List of category names if tier='custom'
    """
    print("Downloading FRED Economic Indicators")
    print("="*60)

    # Determine which categories to download
    if tier == '1':
        selected_cats = TIER1_CATEGORIES
        print("Tier 1: Essential Market Context")
    elif tier == '2':
        selected_cats = list(FRED_INDICATORS.keys())
        print("Tier 2: All Indicators")
    elif tier == 'custom' and categories:
        selected_cats = categories
        print(f"Custom selection: {', '.join(categories)}")
    else:
        selected_cats = TIER1_CATEGORIES
        print("Defaulting to Tier 1: Essential Market Context")

    print()

    # Download data
    all_data = {}
    failed = []
    total_indicators = sum(len(FRED_INDICATORS[cat]) for cat in selected_cats if cat in FRED_INDICATORS)
    current = 0

    for category in selected_cats:
        if category not in FRED_INDICATORS:
            print(f"Warning: Unknown category '{category}', skipping")
            continue

        print(f"\n{category.upper().replace('_', ' ')}:")
        print("-" * 60)

        for fred_code, description in FRED_INDICATORS[category].items():
            current += 1
            print(f"[{current}/{total_indicators}] {fred_code:20} {description[:35]:35}...", end=" ")

            data = download_from_fred(fred_code)

            if data is not None and not data.empty:
                all_data[fred_code] = data
                first_date = data.index[0].strftime('%Y-%m-%d')
                last_date = data.index[-1].strftime('%Y-%m-%d')
                years = len(data) / 251  # Approximate trading days per year
                print(f"OK ({len(data):5} days, {years:4.1f}y, {first_date} to {last_date})")
            else:
                failed.append(fred_code)
                print("FAIL")

    print("\n" + "="*60)
    print(f"Downloaded: {len(all_data)}/{total_indicators} indicators")
    if failed:
        print(f"Failed: {', '.join(failed)}")

    if not all_data:
        print("No data to save!")
        return False

    # Combine all data
    print("\nProcessing data for database update...")
    new_data_df = pd.concat([data for data in all_data.values()], axis=1)
    new_data_df.columns = list(all_data.keys())
    new_data_df.index = pd.to_datetime(new_data_df.index)

    print(f"Date range: {new_data_df.index[0].strftime('%Y-%m-%d')} to {new_data_df.index[-1].strftime('%Y-%m-%d')}")
    print(f"Total rows: {len(new_data_df)}")

    # Update database
    conn = get_db_connection(row_factory=None)
    try:
        # Load existing data
        print("\nLoading existing database...")
        existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
        if not existing_df.empty and 'Date' in existing_df.columns:
            existing_df['Date'] = pd.to_datetime(existing_df['Date'], format='mixed')
            existing_df.set_index('Date', inplace=True)

        print(f"Merging with existing data ({len(existing_df)} rows)...")

        # Ensure columns exist
        for ticker in all_data.keys():
            if ticker not in existing_df.columns:
                existing_df[ticker] = pd.NA

        # Vectorized update
        combined_df = existing_df.copy()
        combined_df.update(new_data_df)

        # Add any new dates
        new_dates = new_data_df.index.difference(combined_df.index)
        if len(new_dates) > 0:
            combined_df = pd.concat([combined_df, new_data_df.loc[new_dates]])
            combined_df = combined_df.sort_index()

        # Save to database
        print("Saving to database...")

        # Clean up staging tables
        cursor = conn.cursor()
        cursor.execute("DROP INDEX IF EXISTS ix_stock_prices_daily_staging_Date")
        cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_staging")
        cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_old")
        conn.commit()

        # Convert pd.NA to None for SQLite
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

        # Verify
        print("\nVerification:")
        for fred_code in sorted(all_data.keys()):
            cursor.execute(f'''
                SELECT COUNT("{fred_code}") as count,
                       MIN(CASE WHEN "{fred_code}" IS NOT NULL THEN Date END) as first,
                       MAX(CASE WHEN "{fred_code}" IS NOT NULL THEN Date END) as last
                FROM stock_prices_daily
                WHERE "{fred_code}" IS NOT NULL
            ''')
            result = cursor.fetchone()
            if result[0] > 0:
                years = result[0] / 251
                print(f"  {fred_code:20} {result[0]:5} days ({years:4.1f} yrs), {result[1][:10]} to {result[2][:10]}")

        conn.close()
        return True

    except Exception as e:
        print(f"ERROR: Database update failed: {e}")
        import traceback
        traceback.print_exc()
        conn.close()
        return False

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Download FRED economic indicators',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Download Tier 1 essentials (yields, Fed policy, inflation, credit spreads)
  python download_fred_indicators.py

  # Download all indicators (Tier 1 + Tier 2)
  python download_fred_indicators.py --tier 2

  # Download specific categories
  python download_fred_indicators.py --tier custom --categories treasury_yields labor commodities

Available categories:
  Tier 1: treasury_yields, fed_policy, inflation, credit_spreads
  Tier 2: labor, economic_activity, liquidity, financial_stress, commodities, forex
        """
    )

    parser.add_argument('--tier', type=str, default='1', choices=['1', '2', 'custom'],
                       help='Tier level: 1=essentials, 2=all, custom=specific categories')
    parser.add_argument('--categories', nargs='+',
                       help='Category names (required if --tier custom)')

    args = parser.parse_args()

    if args.tier == 'custom' and not args.categories:
        parser.error("--categories required when --tier custom")

    success = download_fred_indicators(tier=args.tier, categories=args.categories)
    sys.exit(0 if success else 1)
