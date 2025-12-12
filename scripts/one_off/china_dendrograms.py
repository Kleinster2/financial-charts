import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))
"""
china_dendrograms.py - Generate China A-Shares dendrograms using company names
Uses Ward's method to cluster stocks by correlation distance
"""

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import seaborn as sns
from constants import DB_PATH, get_db_connection
import os
import shutil

print(f"Using database: {DB_PATH}")

# --- CONFIG ---
MIN_DATA_POINTS = 50
OUTPUT_DIR = 'charting_sandbox/dendrograms'

# China A-Shares ticker to name mapping
CHINA_NAMES = {
    # Financial Services
    "601318.SS": "Ping An Insurance",
    "600036.SS": "China Merchants Bank",
    "601166.SS": "Industrial Bank",
    "600000.SS": "Shanghai Pudong Bank",
    "601398.SS": "ICBC",
    "601939.SS": "China Construction Bank",
    "600016.SS": "Minsheng Bank",
    "601328.SS": "Bank of Communications",
    "601288.SS": "Agricultural Bank",
    "601601.SS": "China Pacific Insurance",
    # Consumer/Baijiu
    "600519.SS": "Kweichow Moutai",
    "000858.SZ": "Wuliangye",
    "000568.SZ": "Luzhou Laojiao",
    "600809.SS": "Shanxi Fenjiu",
    "000596.SZ": "Gujing Distillery",
    "603369.SS": "King's Luck Brewery",
    "002304.SZ": "Yanghe Brewery",
    "600887.SS": "Inner Mongolia Yili",
    "000895.SZ": "Henan Shuanghui",
    "603288.SS": "Foshan Haitian",
    # Technology
    "000725.SZ": "BOE Technology",
    "002415.SZ": "Hikvision",
    "000063.SZ": "ZTE Corporation",
    "600703.SS": "SenseTime",
    "002230.SZ": "iFlytek",
    # EV/Batteries/Solar
    "300750.SZ": "CATL",
    "002594.SZ": "BYD",
    "002460.SZ": "Ganfeng Lithium",
    "002466.SZ": "Tianqi Lithium",
    "300014.SZ": "EVE Energy",
    "601012.SS": "LONGi Green Energy",
    "600438.SS": "Tongwei",
    # Semiconductors & AI Chips
    "688012.SS": "AMEC",
    "688981.SS": "SMIC",
    "002371.SZ": "Naura Technology",
    "300223.SZ": "Beijing Huafeng Test",
    "688256.SS": "Cambricon",
    "688041.SS": "Hygon Information",
    "300474.SZ": "Jingjia Micro",
    "688368.SS": "Fullhan Microelectronics",
    "603986.SS": "GigaDevice",
    "688521.SS": "VeriSilicon",
    "688095.SS": "Empyrean Technology",
    "600584.SS": "JCET Group",
    # Healthcare
    "600276.SS": "Jiangsu Hengrui",
    "000538.SZ": "Yunnan Baiyao",
    "300122.SZ": "Zhifei Biological",
    "300015.SZ": "Aier Eye Hospital",
    "002007.SZ": "Hualan Biological",
    # Energy
    "601857.SS": "PetroChina",
    "600028.SS": "Sinopec",
    "601088.SS": "China Shenhua Energy",
    "601899.SS": "Zijin Mining",
    "600547.SS": "Shandong Gold",
    "600900.SS": "Yangtze Power",
    # Industrials
    "600031.SS": "Sany Heavy Industry",
    "000333.SZ": "Midea Group",
    "000651.SZ": "Gree Electric",
    "600690.SS": "Haier Smart Home",
    # Real Estate/Infrastructure
    "600048.SS": "Poly Developments",
    "001979.SZ": "Merchants Shekou",
    "000002.SZ": "China Vanke",
    "601669.SS": "Power Construction",
    # ETFs
    "510300.SS": "CSI 300 ETF",
    "510050.SS": "SSE 50 ETF",
}

# China sector groups
CHINA_GROUPS = {
    'china': {
        'title': 'China A-Shares (All)',
        'tickers': list(CHINA_NAMES.keys()),
    },
    'china_financials': {
        'title': 'China Financials',
        'tickers': ["601318.SS", "600036.SS", "601166.SS", "600000.SS", "601398.SS",
                    "601939.SS", "600016.SS", "601328.SS", "601288.SS", "601601.SS"],
    },
    'china_consumer': {
        'title': 'China Consumer/Baijiu',
        'tickers': ["600519.SS", "000858.SZ", "000568.SZ", "600809.SS", "000596.SZ",
                    "603369.SS", "002304.SZ", "600887.SS", "000895.SZ", "603288.SS"],
    },
    'china_tech': {
        'title': 'China Technology',
        'tickers': ["000725.SZ", "002415.SZ", "000063.SZ", "600703.SS", "002230.SZ",
                    "688256.SS", "688041.SS", "300474.SZ", "688368.SS", "603986.SS",
                    "688521.SS", "688095.SS", "600584.SS", "688012.SS", "688981.SS",
                    "002371.SZ", "300223.SZ"],
    },
    'china_semis': {
        'title': 'China Semiconductors & AI',
        'tickers': ["688012.SS", "688981.SS", "002371.SZ", "300223.SZ", "688256.SS",
                    "688041.SS", "300474.SZ", "688368.SS", "603986.SS", "688521.SS",
                    "688095.SS", "600584.SS"],
    },
    'china_ev': {
        'title': 'China EV & Battery',
        'tickers': ["300750.SZ", "002594.SZ", "002460.SZ", "002466.SZ", "300014.SZ",
                    "601012.SS", "600438.SS"],
    },
    'china_healthcare': {
        'title': 'China Healthcare',
        'tickers': ["600276.SS", "000538.SZ", "300122.SZ", "300015.SZ", "002007.SZ"],
    },
    'china_energy': {
        'title': 'China Energy',
        'tickers': ["601857.SS", "600028.SS", "601088.SS", "601899.SS", "600547.SS", "600900.SS"],
    },
    'china_industrials': {
        'title': 'China Industrials',
        'tickers': ["600031.SS", "000333.SZ", "000651.SZ", "600690.SS"],
    },
    'china_realestate': {
        'title': 'China Real Estate',
        'tickers': ["600048.SS", "001979.SZ", "000002.SZ", "601669.SS"],
    },
}

def get_display_name(ticker):
    """Get display name for ticker (company name or ticker if not found)."""
    return CHINA_NAMES.get(ticker, ticker)

# Load price data
print("Loading price data...")
df_prices_all = pd.read_sql(
    "SELECT * FROM stock_prices_daily ORDER BY Date",
    get_db_connection(row_factory=None),
    parse_dates=["Date"],
).set_index("Date")
df_prices_all = df_prices_all.apply(pd.to_numeric, errors='coerce')


def generate_china_dendrograms(df_prices, period_name, suffix, min_data_points=MIN_DATA_POINTS):
    """Generate dendrograms for all China groups."""
    print(f"\n{'='*60}")
    print(f"Generating China dendrograms: {period_name}")
    print(f"{'='*60}")

    # Get all China tickers that have data
    china_tickers = list(CHINA_NAMES.keys())
    available = [t for t in china_tickers if t in df_prices.columns]

    if len(available) < 5:
        print(f"  Not enough China tickers with data ({len(available)}). Skipping.")
        return

    # Filter to China tickers only
    df_china = df_prices[available].copy()

    # Filter columns with sufficient data
    valid_cols = df_china.columns[df_china.notna().sum() >= min_data_points]
    df_china = df_china[valid_cols].copy()

    if len(df_china.columns) < 5:
        print(f"  Not enough valid tickers after filtering. Skipping.")
        return

    # For Full History, filter to rows where China data exists
    # Find the first date where we have China data
    first_valid_idx = df_china.notna().any(axis=1).idxmax()
    df_china = df_china.loc[first_valid_idx:]
    print(f"  Data range: {df_china.index.min().date()} to {df_china.index.max().date()} ({len(df_china)} days)")

    if len(df_china) < min_data_points:
        print(f"  Not enough data ({len(df_china)} days). Skipping.")
        return

    # Calculate log returns
    df_china = df_china.replace(0, np.nan)
    returns = np.log(df_china).diff()

    # Use reasonable thresholds based on actual data length
    col_thresh = max(min_data_points, int(0.3 * len(returns)))
    returns = returns.dropna(axis=1, thresh=col_thresh)

    if len(returns.columns) < 5:
        print(f"  Not enough valid columns after filtering ({len(returns.columns)}). Skipping.")
        return

    row_thresh = int(0.5 * len(returns.columns))
    returns = returns.dropna(axis=0, thresh=row_thresh)
    returns = returns.fillna(0)

    if len(returns.columns) < 5:
        print(f"  Not enough valid tickers after return calculation. Skipping.")
        return

    print(f"  Analyzing {len(returns.columns)} tickers with {len(returns)} days of data")
    print(f"  Period: {returns.index.min().date()} to {returns.index.max().date()}")

    # Calculate correlation matrix
    corr_matrix = returns.corr().fillna(0)
    date_range = f"{returns.index.min().strftime('%b %Y')} - {returns.index.max().strftime('%b %Y')}"

    # Generate dendrograms for each group
    for group_key, group_info in CHINA_GROUPS.items():
        title = group_info['title']
        tickers = group_info['tickers']

        # Filter to available tickers in this group
        valid_tickers = [t for t in tickers if t in corr_matrix.columns]
        if len(valid_tickers) < 3:
            print(f"  Skipping {title} (only {len(valid_tickers)} tickers available)")
            continue

        # Get company names for labels
        labels = [get_display_name(t) for t in valid_tickers]

        # Calculate correlation submatrix
        corr_sub = corr_matrix.loc[valid_tickers, valid_tickers]
        dist_sub = 1 - corr_sub
        np.fill_diagonal(dist_sub.values, 0)
        dist_cond = squareform(dist_sub.values)
        Z_sub = linkage(dist_cond, method='ward')

        # Generate dendrogram
        fig_height = max(6, len(valid_tickers) * 0.2)
        plt.figure(figsize=(12, fig_height))
        dendrogram(
            Z_sub,
            labels=labels,
            orientation='right',
            leaf_font_size=9
        )
        plt.title(f'{title} Dendrogram - {period_name}\n{date_range}')
        plt.xlabel('Distance (1 - Correlation)')
        plt.tight_layout()
        filename = f'dendrogram_{group_key}{suffix}.png'
        plt.savefig(filename, dpi=150)
        plt.close()

        # Generate clustermap
        fig_size = max(8, len(valid_tickers) * 0.4)

        # Rename columns/index to company names for the clustermap
        corr_named = corr_sub.copy()
        corr_named.columns = labels
        corr_named.index = labels

        g = sns.clustermap(
            corr_named,
            method='ward',
            cmap='RdYlGn',
            center=0,
            vmin=-1,
            vmax=1,
            figsize=(fig_size, fig_size),
            dendrogram_ratio=0.15,
            cbar_pos=(0.02, 0.8, 0.03, 0.15),
            annot=len(valid_tickers) <= 15,
            fmt='.2f' if len(valid_tickers) <= 15 else None,
            annot_kws={'size': 7} if len(valid_tickers) <= 15 else None
        )
        g.ax_heatmap.set_title(f'{title} Correlation - {period_name}\n{date_range}', pad=20)
        plt.tight_layout()
        filename = f'clustermap_{group_key}{suffix}.png'
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()

        print(f"  Generated {title}: {len(valid_tickers)} stocks")

    print(f"  Completed {period_name}")


# Define time periods - include Full History for China specifically
periods = [
    ("Full History", "", df_prices_all),  # China has data from 2019
    ("2024", "_2024", df_prices_all[(df_prices_all.index >= '2024-01-01') & (df_prices_all.index < '2025-01-01')]),
    ("2025", "_2025", df_prices_all[df_prices_all.index >= '2025-01-01']),
    # Quarters
    ("2024 Q1", "_2024_Q1", df_prices_all[(df_prices_all.index >= '2024-01-01') & (df_prices_all.index < '2024-04-01')]),
    ("2024 Q2", "_2024_Q2", df_prices_all[(df_prices_all.index >= '2024-04-01') & (df_prices_all.index < '2024-07-01')]),
    ("2024 Q3", "_2024_Q3", df_prices_all[(df_prices_all.index >= '2024-07-01') & (df_prices_all.index < '2024-10-01')]),
    ("2024 Q4", "_2024_Q4", df_prices_all[(df_prices_all.index >= '2024-10-01') & (df_prices_all.index < '2025-01-01')]),
    ("2025 Q1", "_2025_Q1", df_prices_all[(df_prices_all.index >= '2025-01-01') & (df_prices_all.index < '2025-04-01')]),
    ("2025 Q2", "_2025_Q2", df_prices_all[(df_prices_all.index >= '2025-04-01') & (df_prices_all.index < '2025-07-01')]),
    ("2025 Q3", "_2025_Q3", df_prices_all[(df_prices_all.index >= '2025-07-01') & (df_prices_all.index < '2025-10-01')]),
]

# Run analysis (yearly and quarterly only, no monthly)
for period_name, suffix, df_period in periods:
    generate_china_dendrograms(df_period, period_name, suffix)

# Copy China files to sandbox folder
print("\n" + "=" * 60)
print("Copying China files to charting_sandbox/dendrograms...")
os.makedirs(OUTPUT_DIR, exist_ok=True)

for f in os.listdir('.'):
    if (f.startswith(('dendrogram_china', 'clustermap_china')) and f.endswith('.png')):
        shutil.copy(f, os.path.join(OUTPUT_DIR, f))
        print(f"  Copied {f}")

print("\n" + "=" * 60)
print("China dendrograms complete!")
