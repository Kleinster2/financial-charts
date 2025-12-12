import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))
"""
brazil_dendrograms.py - Generate Brazil (Ibovespa) dendrograms using company names
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

# Brazil stocks ticker to name mapping
BRAZIL_NAMES = {
    # Banks & Financial Services
    "ITUB4.SA": "Itaú Unibanco",
    "BBDC4.SA": "Bradesco PN",
    "BBDC3.SA": "Bradesco ON",
    "BBAS3.SA": "Banco do Brasil",
    "SANB11.SA": "Santander Brasil",
    "ITSA4.SA": "Itaúsa",
    "B3SA3.SA": "B3 (Exchange)",
    "BPAC11.SA": "BTG Pactual",
    "BBSE3.SA": "BB Seguridade",
    "IRBR3.SA": "IRB Brasil RE",
    # Oil & Gas / Energy
    "PETR4.SA": "Petrobras PN",
    "PETR3.SA": "Petrobras ON",
    "PRIO3.SA": "PetroRio",
    "UGPA3.SA": "Ultrapar",
    "CSAN3.SA": "Cosan",
    # Mining & Steel
    "VALE3.SA": "Vale",
    "GGBR4.SA": "Gerdau",
    "GOAU4.SA": "Metalúrgica Gerdau",
    "CSNA3.SA": "CSN",
    "USIM5.SA": "Usiminas",
    "BRAP4.SA": "Bradespar",
    # Utilities (Electric)
    "ELET3.SA": "Eletrobras ON",
    "ELET6.SA": "Eletrobras PNB",
    "EQTL3.SA": "Equatorial",
    "EGIE3.SA": "Engie Brasil",
    "CPFE3.SA": "CPFL Energia",
    "CMIG4.SA": "Cemig",
    "CPLE6.SA": "Copel",
    "NEOE3.SA": "Neoenergia",
    "ENGI11.SA": "Energisa",
    "TAEE11.SA": "Taesa",
    "ENEV3.SA": "Eneva",
    "SBSP3.SA": "Sabesp",
    # Consumer / Retail
    "LREN3.SA": "Lojas Renner",
    "MGLU3.SA": "Magazine Luiza",
    "CYRE3.SA": "Cyrela",
    "MRVE3.SA": "MRV",
    "MULT3.SA": "Multiplan",
    "IGTI11.SA": "Iguatemi",
    "JHSF3.SA": "JHSF",
    "YDUQ3.SA": "Yduqs",
    "COGN3.SA": "Cogna",
    # Food & Beverage
    "ABEV3.SA": "Ambev",
    "JBSS3.SA": "JBS",
    "BRFS3.SA": "BRF",
    "MRFG3.SA": "Marfrig",
    "BEEF3.SA": "Minerva Foods",
    # Healthcare
    "HAPV3.SA": "Hapvida",
    "QUAL3.SA": "Qualicorp",
    "FLRY3.SA": "Fleury",
    "HYPE3.SA": "Hypera Pharma",
    # Industrials / Transport
    "WEGE3.SA": "WEG",
    "EMBR3.SA": "Embraer",
    "RAIL3.SA": "Rumo",
    "AZUL4.SA": "Azul",
    "RENT3.SA": "Localiza",
    "CCRO3.SA": "CCR",
    "GOLL4.SA": "GOL",
    # Pulp & Paper
    "SUZB3.SA": "Suzano",
    "KLBN11.SA": "Klabin",
    # Telecom & Tech
    "VIVT3.SA": "Telefônica Vivo",
    "TOTS3.SA": "Totvs",
    "TIMP3.SA": "TIM",
    # Chemicals / Materials
    "BRKM5.SA": "Braskem",
    # Others
    "CVCB3.SA": "CVC Brasil",
    "HGTX3.SA": "Cia Hering",
    "BRML3.SA": "BR Malls",
    "CIEL3.SA": "Cielo",
    "SULA11.SA": "SulAmérica",
    "ENBR3.SA": "Energias BR",
}

# Brazil sector groups
BRAZIL_GROUPS = {
    'brazil': {
        'title': 'Brazil (All)',
        'tickers': list(BRAZIL_NAMES.keys()),
    },
    'brazil_financials': {
        'title': 'Brazil Financials',
        'tickers': ["ITUB4.SA", "BBDC4.SA", "BBDC3.SA", "BBAS3.SA", "SANB11.SA",
                    "ITSA4.SA", "B3SA3.SA", "BPAC11.SA", "BBSE3.SA", "IRBR3.SA"],
    },
    'brazil_energy': {
        'title': 'Brazil Oil & Gas',
        'tickers': ["PETR4.SA", "PETR3.SA", "PRIO3.SA", "UGPA3.SA", "CSAN3.SA"],
    },
    'brazil_mining': {
        'title': 'Brazil Mining & Steel',
        'tickers': ["VALE3.SA", "GGBR4.SA", "GOAU4.SA", "CSNA3.SA", "USIM5.SA", "BRAP4.SA"],
    },
    'brazil_utilities': {
        'title': 'Brazil Utilities',
        'tickers': ["ELET3.SA", "ELET6.SA", "EQTL3.SA", "EGIE3.SA", "CPFE3.SA",
                    "CMIG4.SA", "CPLE6.SA", "NEOE3.SA", "ENGI11.SA", "TAEE11.SA",
                    "ENEV3.SA", "SBSP3.SA"],
    },
    'brazil_consumer': {
        'title': 'Brazil Consumer',
        'tickers': ["LREN3.SA", "MGLU3.SA", "CYRE3.SA", "MRVE3.SA", "MULT3.SA",
                    "IGTI11.SA", "JHSF3.SA", "YDUQ3.SA", "COGN3.SA", "ABEV3.SA",
                    "BEEF3.SA"],
    },
    'brazil_industrial': {
        'title': 'Brazil Industrial',
        'tickers': ["WEGE3.SA", "EMBR3.SA", "RAIL3.SA", "AZUL4.SA", "RENT3.SA",
                    "SUZB3.SA", "KLBN11.SA"],
    },
}

def get_display_name(ticker):
    """Get display name for ticker (company name or ticker if not found)."""
    return BRAZIL_NAMES.get(ticker, ticker)

# Load price data
print("Loading price data...")
df_prices_all = pd.read_sql(
    "SELECT * FROM stock_prices_daily ORDER BY Date",
    get_db_connection(row_factory=None),
    parse_dates=["Date"],
).set_index("Date")
df_prices_all = df_prices_all.apply(pd.to_numeric, errors='coerce')


def generate_brazil_dendrograms(df_prices, period_name, suffix, min_data_points=MIN_DATA_POINTS):
    """Generate dendrograms for all Brazil groups."""
    print(f"\n{'='*60}")
    print(f"Generating Brazil dendrograms: {period_name}")
    print(f"{'='*60}")

    # Get all Brazil tickers that have data
    brazil_tickers = list(BRAZIL_NAMES.keys())
    available = [t for t in brazil_tickers if t in df_prices.columns]

    if len(available) < 5:
        print(f"  Not enough Brazil tickers with data ({len(available)}). Skipping.")
        return

    # Filter to Brazil tickers only
    df_brazil = df_prices[available].copy()

    # Filter columns with sufficient data
    valid_cols = df_brazil.columns[df_brazil.notna().sum() >= min_data_points]
    df_brazil = df_brazil[valid_cols].copy()

    if len(df_brazil.columns) < 5:
        print(f"  Not enough valid tickers after filtering. Skipping.")
        return

    # For Full History, filter to rows where Brazil data exists
    first_valid_idx = df_brazil.notna().any(axis=1).idxmax()
    df_brazil = df_brazil.loc[first_valid_idx:]
    print(f"  Data range: {df_brazil.index.min().date()} to {df_brazil.index.max().date()} ({len(df_brazil)} days)")

    if len(df_brazil) < min_data_points:
        print(f"  Not enough data ({len(df_brazil)} days). Skipping.")
        return

    # Calculate log returns
    df_brazil = df_brazil.replace(0, np.nan)
    returns = np.log(df_brazil).diff()

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
    for group_key, group_info in BRAZIL_GROUPS.items():
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
    generate_brazil_dendrograms(df_period, period_name, suffix)

# Copy Brazil files to sandbox folder
print("\n" + "=" * 60)
print("Copying Brazil files to charting_sandbox/dendrograms...")
os.makedirs(OUTPUT_DIR, exist_ok=True)

for f in os.listdir('.'):
    if (f.startswith(('dendrogram_brazil', 'clustermap_brazil')) and f.endswith('.png')):
        shutil.copy(f, os.path.join(OUTPUT_DIR, f))
        print(f"  Copied {f}")

print("\n" + "=" * 60)
print("Brazil dendrograms complete!")
