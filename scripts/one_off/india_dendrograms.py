"""
india_dendrograms.py - Generate India market hierarchical clustering dendrograms
Vertical layout with company names on the left side.
Generates for Full History, 2024, and 2025 time periods.
"""

import sqlite3
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import os
import shutil

# India ticker to name mapping (ticker + company name)
INDIA_NAMES = {
    # Tech/IT Services
    'INFY.NS': 'INFY Infosys',
    'TCS.NS': 'TCS Tata Consultancy',
    'WIPRO.NS': 'WIPRO Wipro',
    'HCLTECH.NS': 'HCLTECH HCL Technologies',
    'TECHM.NS': 'TECHM Tech Mahindra',
    'LTIM.NS': 'LTIM LTIMindtree',
    'MPHASIS.NS': 'MPHASIS Mphasis',
    'COFORGE.NS': 'COFORGE Coforge',
    'TATAELXSI.NS': 'TATAELXSI Tata Elxsi',
    'TATACOMM.NS': 'TATACOMM Tata Communications',
    # Banks & Finance
    'HDFCBANK.NS': 'HDFCBANK HDFC Bank',
    'ICICIBANK.NS': 'ICICIBANK ICICI Bank',
    'SBIN.NS': 'SBIN State Bank India',
    'KOTAKBANK.NS': 'KOTAKBANK Kotak Mahindra',
    'AXISBANK.NS': 'AXISBANK Axis Bank',
    'INDUSINDBK.NS': 'INDUSINDBK IndusInd Bank',
    'BAJFINANCE.NS': 'BAJFINANCE Bajaj Finance',
    'BAJAJFINSV.NS': 'BAJAJFINSV Bajaj Finserv',
    'HDFCLIFE.NS': 'HDFCLIFE HDFC Life',
    'SBILIFE.NS': 'SBILIFE SBI Life',
    # Conglomerates/Industrial
    'RELIANCE.NS': 'RELIANCE Reliance Industries',
    'TATAMOTORS.NS': 'TATAMOTORS Tata Motors',
    'TATASTEEL.NS': 'TATASTEEL Tata Steel',
    'TATAPOWER.NS': 'TATAPOWER Tata Power',
    'ADANIENT.NS': 'ADANIENT Adani Enterprises',
    'ADANIPORTS.NS': 'ADANIPORTS Adani Ports',
    'ADANIGREEN.NS': 'ADANIGREEN Adani Green',
    'LT.NS': 'LT Larsen & Toubro',
    'HINDALCO.NS': 'HINDALCO Hindalco',
    'JSWSTEEL.NS': 'JSWSTEEL JSW Steel',
    # Consumer/Retail
    'HINDUNILVR.NS': 'HINDUNILVR Hindustan Unilever',
    'ITC.NS': 'ITC ITC Limited',
    'NESTLEIND.NS': 'NESTLEIND Nestle India',
    'BRITANNIA.NS': 'BRITANNIA Britannia',
    'TITAN.NS': 'TITAN Titan Company',
    'ASIANPAINT.NS': 'ASIANPAINT Asian Paints',
    'DMART.NS': 'DMART Avenue Supermarts',
    'TRENT.NS': 'TRENT Trent Limited',
    'PIDILITIND.NS': 'PIDILITIND Pidilite Industries',
    # Pharma/Healthcare
    'SUNPHARMA.NS': 'SUNPHARMA Sun Pharma',
    'DRREDDY.NS': 'DRREDDY Dr Reddys Labs',
    'CIPLA.NS': 'CIPLA Cipla',
    'DIVISLAB.NS': 'DIVISLAB Divis Laboratories',
    'APOLLOHOSP.NS': 'APOLLOHOSP Apollo Hospitals',
    'MAXHEALTH.NS': 'MAXHEALTH Max Healthcare',
    'BIOCON.NS': 'BIOCON Biocon',
    # Auto
    'MARUTI.NS': 'MARUTI Maruti Suzuki',
    'M&M.NS': 'M&M Mahindra & Mahindra',
    'BAJAJ-AUTO.NS': 'BAJAJ-AUTO Bajaj Auto',
    'HEROMOTOCO.NS': 'HEROMOTOCO Hero MotoCorp',
    'EICHERMOT.NS': 'EICHERMOT Eicher Motors',
    'TVSMOTOR.NS': 'TVSMOTOR TVS Motor',
    # Telecom
    'BHARTIARTL.NS': 'BHARTIARTL Bharti Airtel',
    'IDEA.NS': 'IDEA Vodafone Idea',
    'ZEEL.NS': 'ZEEL Zee Entertainment',
    # Energy/Utilities
    'ONGC.NS': 'ONGC Oil & Natural Gas',
    'NTPC.NS': 'NTPC NTPC Limited',
    'POWERGRID.NS': 'POWERGRID Power Grid Corp',
    'COALINDIA.NS': 'COALINDIA Coal India',
    'IOC.NS': 'IOC Indian Oil',
    'BPCL.NS': 'BPCL Bharat Petroleum',
    'GAIL.NS': 'GAIL GAIL India',
    # New Economy
    'PAYTM.NS': 'PAYTM Paytm',
    'NYKAA.NS': 'NYKAA FSN E-Commerce',
    'POLICYBZR.NS': 'POLICYBZR PB Fintech',
    # Electronics
    'DIXON.NS': 'DIXON Dixon Technologies',
    'VEDL.NS': 'VEDL Vedanta',
    'KAYNES.NS': 'KAYNES Kaynes Technology',
    # Defense
    'HAL.NS': 'HAL Hindustan Aeronautics',
    'BDL.NS': 'BDL Bharat Dynamics',
}

# India All Tickers
INDIA_ALL_TICKERS = list(INDIA_NAMES.keys())

# Sector groupings
INDIA_TECH = [
    'INFY.NS', 'TCS.NS', 'WIPRO.NS', 'HCLTECH.NS', 'TECHM.NS',
    'LTIM.NS', 'MPHASIS.NS', 'COFORGE.NS', 'TATAELXSI.NS', 'TATACOMM.NS'
]

INDIA_BANKS = [
    'HDFCBANK.NS', 'ICICIBANK.NS', 'SBIN.NS', 'KOTAKBANK.NS', 'AXISBANK.NS',
    'INDUSINDBK.NS', 'BAJFINANCE.NS', 'BAJAJFINSV.NS', 'HDFCLIFE.NS', 'SBILIFE.NS'
]

INDIA_INDUSTRIAL = [
    'RELIANCE.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TATAPOWER.NS',
    'ADANIENT.NS', 'ADANIPORTS.NS', 'ADANIGREEN.NS', 'LT.NS', 'HINDALCO.NS', 'JSWSTEEL.NS'
]

INDIA_CONSUMER = [
    'HINDUNILVR.NS', 'ITC.NS', 'NESTLEIND.NS', 'BRITANNIA.NS', 'TITAN.NS',
    'ASIANPAINT.NS', 'DMART.NS', 'TRENT.NS', 'PIDILITIND.NS', 'MARUTI.NS', 'M&M.NS'
]

INDIA_PHARMA = [
    'SUNPHARMA.NS', 'DRREDDY.NS', 'CIPLA.NS', 'DIVISLAB.NS',
    'APOLLOHOSP.NS', 'MAXHEALTH.NS', 'BIOCON.NS'
]

INDIA_AUTO = [
    'MARUTI.NS', 'M&M.NS', 'TATAMOTORS.NS',
    'BAJAJ-AUTO.NS', 'HEROMOTOCO.NS', 'EICHERMOT.NS', 'TVSMOTOR.NS'
]

INDIA_ENERGY = [
    'ONGC.NS', 'NTPC.NS', 'POWERGRID.NS', 'COALINDIA.NS',
    'IOC.NS', 'BPCL.NS', 'GAIL.NS', 'TATAPOWER.NS', 'RELIANCE.NS'
]

INDIA_TELECOM_NEWECO = [
    'BHARTIARTL.NS', 'IDEA.NS', 'ZEEL.NS',
    'PAYTM.NS', 'NYKAA.NS', 'POLICYBZR.NS',
    'DIXON.NS', 'TATAELXSI.NS', 'KAYNES.NS'
]

MIN_DATA_POINTS = 50

def generate_dendrogram(tickers, title, filename, corr_matrix, name_map, date_range):
    """Generate a vertical dendrogram with company names on the left."""
    valid_tickers = [t for t in tickers if t in corr_matrix.columns]
    if len(valid_tickers) < 3:
        print(f"  Skipping {title} - only {len(valid_tickers)} valid tickers")
        return False

    # Use name_map for labels
    labels = [name_map.get(t, t.replace('.NS', '')) for t in valid_tickers]

    corr_sub = corr_matrix.loc[valid_tickers, valid_tickers]
    dist_sub = 1 - corr_sub
    np.fill_diagonal(dist_sub.values, 0)
    dist_cond = squareform(dist_sub.values)
    Z_sub = linkage(dist_cond, method='ward')

    # Vertical layout with labels on left
    fig_height = max(8, len(valid_tickers) * 0.25)
    plt.figure(figsize=(14, fig_height))
    dendrogram(
        Z_sub,
        labels=labels,
        orientation='right',  # Vertical with labels on left
        leaf_font_size=10
    )
    plt.title(f'{title} Dendrogram\n{date_range}', fontsize=12, fontweight='bold')
    plt.xlabel('Distance (1 - Correlation)')
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    return True


def analyze_india_period(df_prices, period_name, suffix, min_data_points=MIN_DATA_POINTS):
    """Generate India dendrograms for a specific time period."""
    print(f"\n{'='*60}")
    print(f"India Dendrograms: {period_name}")
    print(f"{'='*60}")

    # Get India tickers in the data
    india_cols = [c for c in df_prices.columns if c.endswith('.NS')]
    if not india_cols:
        print("  No India tickers found in data")
        return

    df_india = df_prices[india_cols].copy()

    # Filter columns with sufficient data
    valid_cols = df_india.columns[df_india.notna().sum() >= min_data_points]
    df_india = df_india[valid_cols]

    if len(df_india.columns) < 5:
        print(f"  Not enough tickers with data ({len(df_india.columns)})")
        return

    # Convert to numeric
    df_india = df_india.apply(pd.to_numeric, errors='coerce')

    # Find valid date range
    data_density = df_india.notna().sum(axis=1)
    threshold = max(5, int(0.1 * len(df_india.columns)))
    valid_rows = data_density >= threshold
    if valid_rows.any():
        first_valid = valid_rows.idxmax()
        df_india = df_india.loc[first_valid:]

    if len(df_india) < min_data_points:
        print(f"  Not enough data ({len(df_india)} days)")
        return

    print(f"  Data range: {df_india.index.min().date()} to {df_india.index.max().date()}")
    print(f"  Tickers: {len(df_india.columns)}, Days: {len(df_india)}")

    # Calculate returns
    df_india = df_india.replace(0, np.nan)
    returns = np.log(df_india).diff()
    returns = returns.dropna(axis=1, thresh=int(0.3 * len(returns)))
    returns = returns.dropna(axis=0, thresh=int(0.5 * len(returns.columns)))
    returns = returns.fillna(0)

    if len(returns.columns) < 5:
        print(f"  Not enough valid columns after filtering ({len(returns.columns)})")
        return

    # Correlation matrix
    corr_matrix = returns.corr().fillna(0)
    date_range = f"{returns.index.min().strftime('%b %Y')} - {returns.index.max().strftime('%b %Y')}"

    # Generate dendrograms
    output_dir = 'charting_sandbox/dendrograms'
    os.makedirs(output_dir, exist_ok=True)

    # All India
    if generate_dendrogram(INDIA_ALL_TICKERS, 'India (All Stocks)',
                          f'{output_dir}/dendrogram_india{suffix}.png',
                          corr_matrix, INDIA_NAMES, date_range):
        print(f"  Created dendrogram_india{suffix}.png")

    # Tech
    if generate_dendrogram(INDIA_TECH, 'India Tech/IT Services',
                          f'{output_dir}/dendrogram_india_tech{suffix}.png',
                          corr_matrix, INDIA_NAMES, date_range):
        print(f"  Created dendrogram_india_tech{suffix}.png")

    # Banks
    if generate_dendrogram(INDIA_BANKS, 'India Banks & Finance',
                          f'{output_dir}/dendrogram_india_banks{suffix}.png',
                          corr_matrix, INDIA_NAMES, date_range):
        print(f"  Created dendrogram_india_banks{suffix}.png")

    # Industrial
    if generate_dendrogram(INDIA_INDUSTRIAL, 'India Industrial/Conglomerates',
                          f'{output_dir}/dendrogram_india_industrial{suffix}.png',
                          corr_matrix, INDIA_NAMES, date_range):
        print(f"  Created dendrogram_india_industrial{suffix}.png")

    # Consumer
    if generate_dendrogram(INDIA_CONSUMER, 'India Consumer/Retail',
                          f'{output_dir}/dendrogram_india_consumer{suffix}.png',
                          corr_matrix, INDIA_NAMES, date_range):
        print(f"  Created dendrogram_india_consumer{suffix}.png")

    # Pharma
    if generate_dendrogram(INDIA_PHARMA, 'India Pharma/Healthcare',
                          f'{output_dir}/dendrogram_india_pharma{suffix}.png',
                          corr_matrix, INDIA_NAMES, date_range):
        print(f"  Created dendrogram_india_pharma{suffix}.png")

    # Auto
    if generate_dendrogram(INDIA_AUTO, 'India Auto',
                          f'{output_dir}/dendrogram_india_auto{suffix}.png',
                          corr_matrix, INDIA_NAMES, date_range):
        print(f"  Created dendrogram_india_auto{suffix}.png")

    # Energy
    if generate_dendrogram(INDIA_ENERGY, 'India Energy/Utilities',
                          f'{output_dir}/dendrogram_india_energy{suffix}.png',
                          corr_matrix, INDIA_NAMES, date_range):
        print(f"  Created dendrogram_india_energy{suffix}.png")

    # Telecom & New Economy
    if generate_dendrogram(INDIA_TELECOM_NEWECO, 'India Telecom & New Economy',
                          f'{output_dir}/dendrogram_india_neweco{suffix}.png',
                          corr_matrix, INDIA_NAMES, date_range):
        print(f"  Created dendrogram_india_neweco{suffix}.png")


def main():
    print("Loading price data...")
    conn = sqlite3.connect('market_data.db')
    df_prices = pd.read_sql(
        "SELECT * FROM stock_prices_daily ORDER BY Date",
        conn,
        parse_dates=["Date"],
    ).set_index("Date")
    conn.close()

    # Convert to numeric
    df_prices = df_prices.apply(pd.to_numeric, errors='coerce')

    # Time periods
    periods = [
        ("Full History", "", df_prices),
        ("2024", "_2024", df_prices[(df_prices.index >= '2024-01-01') & (df_prices.index < '2025-01-01')]),
        ("2025", "_2025", df_prices[df_prices.index >= '2025-01-01']),
    ]

    for period_name, suffix, df_period in periods:
        if len(df_period) > 0:
            analyze_india_period(df_period, period_name, suffix)

    print("\n" + "=" * 60)
    print("India dendrograms complete!")
    print("=" * 60)


if __name__ == '__main__':
    main()
