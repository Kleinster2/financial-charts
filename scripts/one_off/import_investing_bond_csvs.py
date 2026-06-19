"""
Import Corporate Bond CSV files downloaded from Investing.com
Processes multiple CSV files and adds them to your database

HOW TO USE:
1. Visit Investing.com bond pages and download CSV files:
   - Apple 4.45% 2044: https://www.investing.com/rates-bonds/aapl-4.45-06-may-2044-historical-data
   - Apple 3.85% 2043: https://www.investing.com/rates-bonds/aapl-3.85-04-may-2043-historical-data
   - Microsoft 5.3% 2041: https://www.investing.com/rates-bonds/msft-5.3-08-feb-2041-historical-data
   - etc.

2. For each bond:
   - Set date range (max available)
   - Click "Download" button
   - Save CSV file to: C:\\Users\\klein\\financial-charts\\bond_csvs\\

3. Run this script: python import_investing_bond_csvs.py

The script will:
- Read all CSV files from bond_csvs folder
- Parse bond name from filename
- Import into bond_prices_daily table
- Create bond_metadata table
"""

import pandas as pd
import sqlite3
import os
from pathlib import Path
import re

# Directory containing downloaded CSV files
CSV_DIR = Path(__file__).parent / 'bond_csvs'
DB_PATH = 'market_data.db'

# Bond name mapping (filename pattern -> ticker name)
BOND_NAME_PATTERNS = {
    r'aapl.*4\.45.*2044': 'AAPL_4.45_2044',
    r'aapl.*3\.85.*2043': 'AAPL_3.85_2043',
    r'aapl.*3\.0.*2027': 'AAPL_3.00_2027',
    r'aapl.*2\.65.*2050': 'AAPL_2.65_2050',
    r'msft.*5\.3.*2041': 'MSFT_5.30_2041',
    r'msft.*4\.5.*2050': 'MSFT_4.50_2050',
    r'msft.*3\.7.*2042': 'MSFT_3.70_2042',
    r'amzn.*3\.95.*2052': 'AMZN_3.95_2052',
    r'amzn.*4\.8.*2047': 'AMZN_4.80_2047',
    r'googl.*1\.1.*2027': 'GOOGL_1.10_2027',
    r'googl.*2\.25.*2060': 'GOOGL_2.25_2060',
}

def parse_bond_name(filename):
    """Extract bond ticker from filename"""
    filename_lower = filename.lower()

    for pattern, ticker in BOND_NAME_PATTERNS.items():
        if re.search(pattern, filename_lower):
            return ticker

    # Fallback: use filename
    return Path(filename).stem.replace(' ', '_')

def parse_investing_csv(filepath):
    """
    Parse Investing.com bond CSV file

    Expected format:
    Date,Price,Open,High,Low,Change %
    Nov 17, 2025,93.647,93.500,93.800,93.400,+0.25%
    """
    try:
        df = pd.read_csv(filepath)

        # Check if this is an Investing.com format
        if 'Price' in df.columns or 'Close' in df.columns:
            # Rename columns
            df = df.rename(columns={
                'Price': 'close',
                'Close': 'close',
                'Date': 'date'
            })

            # Parse date (Investing.com uses formats like "Nov 17, 2025")
            df['date'] = pd.to_datetime(df['date'], format='mixed')

            # Keep only date and close price
            df = df[['date', 'close']]

            # Remove any NaN values
            df = df.dropna()

            return df
        else:
            print(f"  Warning: Unexpected CSV format in {filepath.name}")
            return None

    except Exception as e:
        print(f"  Error parsing {filepath.name}: {e}")
        return None

def import_bonds_to_database(bonds_data):
    """
    Import bond data into database
    Creates/updates bond_prices_daily table
    """
    if not bonds_data:
        print("No bond data to import")
        return

    conn = sqlite3.connect(DB_PATH)

    # Combine all bonds into wide format
    all_dfs = []
    for bond_name, df in bonds_data.items():
        if df is not None and not df.empty:
            bond_series = df.set_index('date')[['close']].rename(columns={'close': bond_name})
            all_dfs.append(bond_series)
            print(f"  Prepared {bond_name}: {len(df)} days")

    if all_dfs:
        # Combine all bonds
        combined_df = pd.concat(all_dfs, axis=1, join='outer')
        combined_df.index.name = 'Date'

        # Check if table exists
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bond_prices_daily'")
        table_exists = cursor.fetchone() is not None

        if table_exists:
            # Load existing data
            existing_df = pd.read_sql('SELECT * FROM bond_prices_daily', conn)
            existing_df['Date'] = pd.to_datetime(existing_df['Date'])
            existing_df.set_index('Date', inplace=True)

            # Merge with new data (new data takes precedence)
            combined_df = combined_df.combine_first(existing_df)
            print(f"\n  Merged with existing bond_prices_daily table")

        # Save to database
        combined_df.to_sql('bond_prices_daily', conn, if_exists='replace', index=True)

        print(f"\n✓ Saved to database:")
        print(f"  Table: bond_prices_daily")
        print(f"  Rows: {len(combined_df)}")
        print(f"  Columns: Date + {len(combined_df.columns)} bonds")
        print(f"  Bonds: {', '.join(combined_df.columns[:5])}{'...' if len(combined_df.columns) > 5 else ''}")

    conn.close()

def main():
    print("=" * 70)
    print("Investing.com Bond CSV Importer")
    print("=" * 70)
    print()

    # Create CSV directory if it doesn't exist
    CSV_DIR.mkdir(exist_ok=True)

    # Find all CSV files
    csv_files = list(CSV_DIR.glob('*.csv'))

    if not csv_files:
        print(f"No CSV files found in: {CSV_DIR}")
        print()
        print("HOW TO DOWNLOAD:")
        print("1. Visit bond pages on Investing.com:")
        print("   https://www.investing.com/rates-bonds/aapl-4.45-06-may-2044-historical-data")
        print("   https://www.investing.com/rates-bonds/msft-5.3-08-feb-2041-historical-data")
        print()
        print("2. Click 'Download' button on each page")
        print(f"3. Save CSV files to: {CSV_DIR.absolute()}")
        print()
        print("4. Run this script again")
        return

    print(f"Found {len(csv_files)} CSV file(s) in {CSV_DIR}:")
    for f in csv_files:
        print(f"  - {f.name}")
    print()

    # Parse each CSV
    bonds_data = {}
    for csv_file in csv_files:
        bond_name = parse_bond_name(csv_file.name)
        print(f"Processing: {csv_file.name} -> {bond_name}")

        df = parse_investing_csv(csv_file)
        if df is not None:
            bonds_data[bond_name] = df

    # Import to database
    if bonds_data:
        print(f"\n{'='*70}")
        print("Importing to database...")
        print("=" * 70)
        import_bonds_to_database(bonds_data)

        print("\n" + "=" * 70)
        print("COMPLETE")
        print("=" * 70)
        print()
        print("Next steps:")
        print("1. Check bond_prices_daily table: sqlite3 market_data.db \"SELECT * FROM bond_prices_daily LIMIT 5;\"")
        print("2. Add bonds to your charting workspace")
    else:
        print("\nNo valid bond data found in CSV files")

if __name__ == '__main__':
    main()
