"""
EODHD Corporate Bond Data Downloader
Fetches individual corporate bond historical prices using CUSIP/ISIN lookup

Free tier: 20 API calls per day
Paid tier: $59.99/month for unlimited fundamentals access
"""

import requests
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import time
from constants import DB_PATH

# EODHD API Configuration
API_TOKEN = "6919787a7f5c78.39425766"  # EODHD API token
BASE_URL = "https://eodhd.com/api"

# Major Tech Company Bonds to Track
TECH_BONDS = {
    # Apple bonds (CUSIP)
    'AAPL_3.25_2029': '037833CR9',
    'AAPL_3.85_2043': '037833EN6',
    'AAPL_4.65_2046': '037833CK5',
    'AAPL_2.65_2050': '037833DL4',
    'AAPL_3.00_2027': '037833DC4',

    # Microsoft bonds
    'MSFT_3.70_2042': '594918BW3',
    'MSFT_4.50_2050': '594918BV5',
    'MSFT_2.40_2050': '594918BN1',
    'MSFT_3.45_2045': '594918BS0',

    # Amazon bonds
    'AMZN_3.95_2052': '023135BW5',
    'AMZN_4.80_2047': '023135106',
    'AMZN_2.70_2050': '023135BK0',
    'AMZN_3.25_2050': '023135BM6',

    # Alphabet/Google bonds
    'GOOGL_1.10_2027': '02079K107',
    'GOOGL_2.25_2060': '02079K305',
    'GOOGL_1.90_2040': '02079K396',
    'GOOGL_3.38_2024': '02079K248',

    # Oracle bonds
    'ORCL_5.5_2064': '68389XCV5',
    'ORCL_6.15_2029': '68389XCH6',
    'ORCL_3.6_2050': '68389XCK9',
    'ORCL_3.85_2060': '68389XCL7',
}

def get_bond_fundamentals(cusip, bond_name):
    """
    Fetch bond fundamentals data from EODHD

    Parameters:
    - cusip: str, 9-character CUSIP identifier
    - bond_name: str, descriptive name for the bond

    Returns:
    - dict with bond data or None if error
    """

    url = f"{BASE_URL}/bond-fundamentals/{cusip}"
    params = {
        'api_token': API_TOKEN,
        'fmt': 'json'
    }

    try:
        print(f"Fetching {bond_name} (CUSIP: {cusip})...")
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data:
            print(f"  ✓ Retrieved {bond_name}")
            return data
        else:
            print(f"  ✗ No data for {bond_name}")
            return None

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"  ✗ Bond not found: {bond_name}")
        elif e.response.status_code == 403:
            print(f"  ✗ API limit reached or invalid token")
        else:
            print(f"  ✗ HTTP Error {e.response.status_code}: {bond_name}")
        return None
    except Exception as e:
        print(f"  ✗ Error fetching {bond_name}: {e}")
        return None

def get_bond_historical_data(cusip, bond_name, from_date='2020-01-01'):
    """
    Fetch historical EOD prices for a bond

    Parameters:
    - cusip: str, 9-character CUSIP
    - bond_name: str, descriptive name
    - from_date: str, format YYYY-MM-DD

    Returns:
    - DataFrame with historical prices or None
    """

    # Format: CUSIP.BOND for historical data endpoint
    symbol = f"{cusip}.BOND"

    url = f"{BASE_URL}/eod/{symbol}"
    params = {
        'api_token': API_TOKEN,
        'fmt': 'json',
        'from': from_date
    }

    try:
        print(f"Fetching historical data for {bond_name}...")
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data and len(data) > 0:
            df = pd.DataFrame(data)
            df['date'] = pd.to_datetime(df['date'])
            df['bond_name'] = bond_name
            df['cusip'] = cusip
            print(f"  ✓ Retrieved {len(df)} days for {bond_name}")
            return df
        else:
            print(f"  ✗ No historical data for {bond_name}")
            return None

    except Exception as e:
        print(f"  ✗ Error fetching historical data for {bond_name}: {e}")
        return None

def save_bonds_to_database(bonds_data, db_path=None):
    """
    Save bond data to SQLite database

    Creates a new table: bond_prices_daily
    Columns: Date, AAPL_3.25_2029, AAPL_3.85_2043, etc.
    """
    db_path = db_path or DB_PATH

    if not bonds_data:
        print("No bond data to save")
        return

    conn = sqlite3.connect(db_path)

    # Combine all bond data into wide format
    all_dfs = []
    for bond_name, df in bonds_data.items():
        if df is not None and not df.empty:
            # Use 'close' price, rename column to bond name
            bond_series = df.set_index('date')[['close']].rename(columns={'close': bond_name})
            all_dfs.append(bond_series)

    if all_dfs:
        # Combine all bonds into one DataFrame
        combined_df = pd.concat(all_dfs, axis=1)
        combined_df.index.name = 'Date'

        # Save to database
        combined_df.to_sql('bond_prices_daily', conn, if_exists='replace', index=True)
        print(f"\n✓ Saved {len(combined_df)} days for {len(all_dfs)} bonds to database")
        print(f"  Table: bond_prices_daily")
        print(f"  Columns: Date, {', '.join([col for col in combined_df.columns[:5]])}...")
    else:
        print("No valid bond data to save")

    conn.close()

def save_bond_metadata(bonds_info, db_path=None):
    """
    Save bond metadata to database
    """
    db_path = db_path or DB_PATH

    if not bonds_info:
        return

    conn = sqlite3.connect(db_path)

    metadata = []
    for bond_name, info in bonds_info.items():
        if info:
            metadata.append({
                'bond_name': bond_name,
                'cusip': info.get('CUSIP', ''),
                'issuer': info.get('General', {}).get('Issuer', ''),
                'coupon': info.get('General', {}).get('Coupon', ''),
                'maturity': info.get('General', {}).get('MaturityDate', ''),
                'type': info.get('General', {}).get('Type', ''),
            })

    if metadata:
        df = pd.DataFrame(metadata)
        df.to_sql('bond_metadata', conn, if_exists='replace', index=False)
        print(f"✓ Saved metadata for {len(metadata)} bonds")

    conn.close()

def main():
    """
    Main function to download tech company bonds
    """

    print("=" * 70)
    print("EODHD Corporate Bond Data Downloader")
    print("=" * 70)
    print()

    # Check API token
    if API_TOKEN == "YOUR_API_TOKEN_HERE":
        print("⚠ ERROR: Please set your EODHD API token in this script")
        print()
        print("To get your API token:")
        print("1. Sign up at https://eodhd.com/register")
        print("2. Copy your API token from the dashboard")
        print("3. Replace 'YOUR_API_TOKEN_HERE' in this script")
        print()
        print("Free tier allows 20 API calls per day")
        return

    # Fetch bond fundamentals (uses API calls)
    print(f"Fetching fundamentals for {len(TECH_BONDS)} bonds...")
    print("(Free tier: 20 calls/day, this will use ~{} calls)".format(len(TECH_BONDS)))
    print()

    bonds_info = {}
    for bond_name, cusip in list(TECH_BONDS.items())[:20]:  # Limit to 20 for free tier
        info = get_bond_fundamentals(cusip, bond_name)
        if info:
            bonds_info[bond_name] = info
        time.sleep(1)  # Rate limiting

    # Save metadata
    if bonds_info:
        save_bond_metadata(bonds_info)

    # Fetch historical data (uses additional API calls)
    print("\n" + "=" * 70)
    print("Fetching historical prices...")
    print("=" * 70)
    print()

    bonds_historical = {}
    calls_made = len(bonds_info)

    for bond_name, cusip in TECH_BONDS.items():
        if calls_made >= 20:
            print(f"\n⚠ Reached free tier limit (20 calls/day)")
            print(f"  Fetched {len(bonds_historical)} bonds' historical data")
            break

        hist_df = get_bond_historical_data(cusip, bond_name, from_date='2023-01-01')
        if hist_df is not None:
            bonds_historical[bond_name] = hist_df

        calls_made += 1
        time.sleep(1)  # Rate limiting

    # Save to database
    if bonds_historical:
        save_bonds_to_database(bonds_historical)

    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)
    print(f"API calls used: ~{calls_made} / 20 (free tier daily limit)")
    print(f"Bonds with fundamentals: {len(bonds_info)}")
    print(f"Bonds with historical data: {len(bonds_historical)}")
    print()
    print("Next steps:")
    print("1. Check market_data.db for bond_prices_daily table")
    print("2. Add bonds to your charting workspace")
    print("3. Run this script daily to update (respects 20 call limit)")

if __name__ == '__main__':
    main()
