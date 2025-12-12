import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))
"""
korea_dendrograms.py - Generate South Korea dendrograms using company names
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

# Korea stocks ticker to name mapping
KOREA_NAMES = {
    # Semiconductors & Electronics
    "005930.KS": "Samsung Electronics",
    "000660.KS": "SK Hynix",
    "009150.KS": "Samsung Electro-Mechanics",
    "034730.KS": "SK Inc",
    "066570.KS": "LG Electronics",
    "003550.KS": "LG Corp",
    # Internet & Tech
    "035420.KS": "NAVER",
    "035720.KS": "Kakao",
    "259960.KS": "Krafton",
    "263750.KS": "Pearl Abyss",
    "251270.KS": "Netmarble",
    "036570.KS": "NCsoft",
    # Batteries & EV
    "006400.KS": "Samsung SDI",
    "051910.KS": "LG Chem",
    "373220.KS": "LG Energy Solution",
    "096770.KS": "SK Innovation",
    # Automotive
    "005380.KS": "Hyundai Motor",
    "000270.KS": "Kia",
    "012330.KS": "Hyundai Mobis",
    "011210.KS": "Hyundai Wia",
    # Biotech & Pharma
    "068270.KS": "Celltrion",
    "207940.KS": "Samsung Biologics",
    "128940.KS": "Hanmi Pharm",
    "326030.KS": "SK Biopharmaceuticals",
    # Financial Services
    "105560.KS": "KB Financial",
    "055550.KS": "Shinhan Financial",
    "086790.KS": "Hana Financial",
    "316140.KS": "Woori Financial",
    "000810.KS": "Samsung Fire & Marine",
    # Telecom
    "017670.KS": "SK Telecom",
    "030200.KS": "KT Corp",
    "032640.KS": "LG Uplus",
    # Steel & Chemicals
    "005490.KS": "POSCO Holdings",
    "010130.KS": "Korea Zinc",
    "051900.KS": "LG H&H",
    # Shipbuilding & Heavy Industry
    "009540.KS": "Hyundai Heavy Industries",
    "010140.KS": "Samsung Heavy Industries",
    "042660.KS": "Daewoo Shipbuilding",
    # Trading & Conglomerates
    "028260.KS": "Samsung C&T",
    "000100.KS": "Yuhan Corp",
    "018260.KS": "Samsung SDS",
    # Index ETF
    "069500.KS": "KODEX 200 ETF",
}

# Korea sector groups
KOREA_GROUPS = {
    'korea': {
        'title': 'South Korea (All)',
        'tickers': list(KOREA_NAMES.keys()),
    },
    'korea_tech': {
        'title': 'Korea Technology',
        'tickers': ["005930.KS", "000660.KS", "009150.KS", "066570.KS", "003550.KS",
                    "035420.KS", "035720.KS", "259960.KS", "263750.KS", "251270.KS",
                    "036570.KS", "018260.KS"],
    },
    'korea_battery': {
        'title': 'Korea Battery & EV',
        'tickers': ["006400.KS", "051910.KS", "373220.KS", "096770.KS",
                    "005380.KS", "000270.KS", "012330.KS", "011210.KS"],
    },
    'korea_financials': {
        'title': 'Korea Financials',
        'tickers': ["105560.KS", "055550.KS", "086790.KS", "316140.KS", "000810.KS"],
    },
    'korea_biotech': {
        'title': 'Korea Biotech',
        'tickers': ["068270.KS", "207940.KS", "128940.KS", "326030.KS", "000100.KS"],
    },
    'korea_industrial': {
        'title': 'Korea Industrial',
        'tickers': ["005490.KS", "010130.KS", "009540.KS", "010140.KS", "042660.KS",
                    "017670.KS", "030200.KS", "032640.KS"],
    },
}

def get_display_name(ticker):
    """Get display name for ticker (company name or ticker if not found)."""
    return KOREA_NAMES.get(ticker, ticker)

# Load price data
print("Loading price data...")
df_prices_all = pd.read_sql(
    "SELECT * FROM stock_prices_daily ORDER BY Date",
    get_db_connection(row_factory=None),
    parse_dates=["Date"],
).set_index("Date")
df_prices_all = df_prices_all.apply(pd.to_numeric, errors='coerce')


def generate_korea_dendrograms(df_prices, period_name, suffix, min_data_points=MIN_DATA_POINTS):
    """Generate dendrograms for all Korea groups."""
    print(f"\n{'='*60}")
    print(f"Generating Korea dendrograms: {period_name}")
    print(f"{'='*60}")

    # Get all Korea tickers that have data
    korea_tickers = list(KOREA_NAMES.keys())
    available = [t for t in korea_tickers if t in df_prices.columns]

    if len(available) < 5:
        print(f"  Not enough Korea tickers with data ({len(available)}). Skipping.")
        return

    # Filter to Korea tickers only
    df_korea = df_prices[available].copy()

    # Filter columns with sufficient data
    valid_cols = df_korea.columns[df_korea.notna().sum() >= min_data_points]
    df_korea = df_korea[valid_cols].copy()

    if len(df_korea.columns) < 5:
        print(f"  Not enough valid tickers after filtering. Skipping.")
        return

    # For Full History, filter to rows where Korea data exists
    # Find the first date where we have Korea data
    first_valid_idx = df_korea.notna().any(axis=1).idxmax()
    df_korea = df_korea.loc[first_valid_idx:]
    print(f"  Data range: {df_korea.index.min().date()} to {df_korea.index.max().date()} ({len(df_korea)} days)")

    if len(df_korea) < min_data_points:
        print(f"  Not enough data ({len(df_korea)} days). Skipping.")
        return

    # Calculate log returns
    df_korea = df_korea.replace(0, np.nan)
    returns = np.log(df_korea).diff()

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
    for group_key, group_info in KOREA_GROUPS.items():
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


# Define time periods
periods = [
    ("Full History", "", df_prices_all),
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
    generate_korea_dendrograms(df_period, period_name, suffix)

# Copy Korea files to sandbox folder
print("\n" + "=" * 60)
print("Copying Korea files to charting_sandbox/dendrograms...")
os.makedirs(OUTPUT_DIR, exist_ok=True)

for f in os.listdir('.'):
    if (f.startswith(('dendrogram_korea', 'clustermap_korea')) and f.endswith('.png')):
        shutil.copy(f, os.path.join(OUTPUT_DIR, f))
        print(f"  Copied {f}")

print("\n" + "=" * 60)
print("Korea dendrograms complete!")
