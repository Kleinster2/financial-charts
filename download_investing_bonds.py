"""
Scraper for Investing.com corporate bond historical data
Downloads individual corporate bond prices for big tech companies
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

# Bond URLs from Investing.com
TECH_BONDS = {
    'AAPL 4.45% 2044': 'https://www.investing.com/rates-bonds/aapl-4.45-06-may-2044-historical-data',
    'AAPL 3.85% 2043': 'https://www.investing.com/rates-bonds/aapl-3.85-04-may-2043-historical-data',
    'AAPL 3.00% 2027': 'https://www.investing.com/rates-bonds/aapl-3-20-jun-2027-historical-data',
    'MSFT 5.30% 2041': 'https://www.investing.com/rates-bonds/msft-5.3-08-feb-2041-historical-data',
    # Add more bonds as needed
}

def download_bond_data(bond_name, url, start_date='01/01/2020', end_date=None):
    """
    Download historical bond data from Investing.com

    Note: This is a basic template. Investing.com may require:
    - Headers to mimic browser requests
    - Handling of JavaScript/dynamic content (may need Selenium)
    - Rate limiting to avoid blocking

    Parameters:
    - bond_name: str, name of the bond
    - url: str, URL to the bond's historical data page
    - start_date: str, format MM/DD/YYYY
    - end_date: str, format MM/DD/YYYY (default: today)

    Returns:
    - DataFrame with historical prices
    """

    if end_date is None:
        end_date = datetime.now().strftime('%m/%d/%Y')

    print(f"Attempting to download {bond_name}...")

    # Set headers to mimic browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the historical data table
        # NOTE: This is a placeholder - actual parsing depends on Investing.com's HTML structure
        table = soup.find('table', {'class': 'historical-data-table'})

        if table:
            # Extract data (this is a simplified example)
            df = pd.read_html(str(table))[0]
            df['Bond'] = bond_name
            return df
        else:
            print(f"  Could not find data table for {bond_name}")
            return None

    except Exception as e:
        print(f"  Error downloading {bond_name}: {e}")
        return None

def main():
    """
    Main function to download all tech company bonds
    """

    print("=" * 60)
    print("Investing.com Corporate Bond Data Downloader")
    print("=" * 60)
    print()

    all_data = []

    for bond_name, url in TECH_BONDS.items():
        data = download_bond_data(bond_name, url)

        if data is not None:
            all_data.append(data)
            print(f"  ✓ Downloaded {len(data)} records for {bond_name}")

        # Rate limiting - be polite
        time.sleep(2)

    if all_data:
        # Combine all data
        combined_df = pd.concat(all_data, ignore_index=True)

        # Save to CSV
        output_file = 'corporate_bonds_data.csv'
        combined_df.to_csv(output_file, index=False)
        print(f"\n✓ Saved {len(combined_df)} total records to {output_file}")
    else:
        print("\n⚠ No data was downloaded")
        print("\nNOTE: Investing.com likely requires more sophisticated scraping:")
        print("  - May need Selenium for JavaScript rendering")
        print("  - May have anti-bot protection")
        print("  - Alternative: Use EODHD API or manually download CSVs")

if __name__ == '__main__':
    main()

    print("\n" + "=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    print("1. If this script doesn't work, we can:")
    print("   a) Use Selenium to automate browser clicking 'Download'")
    print("   b) Sign up for EODHD API free trial")
    print("   c) Manually download CSVs and I'll process them")
    print()
    print("2. For reliable automated access, consider:")
    print("   - EODHD API ($59.99/month)")
    print("   - Interactive Brokers API (free but needs account)")
    print("=" * 60)
