import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))
"""
canada_dendrograms.py - Generate Canadian stocks dendrograms using company names
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

# Canadian ticker to name mapping
CANADA_NAMES = {
    # Banks (Big Six)
    "RY.TO": "Royal Bank",
    "TD.TO": "TD Bank",
    "BNS.TO": "Scotiabank",
    "BMO.TO": "Bank of Montreal",
    "CM.TO": "CIBC",
    "NA.TO": "National Bank",
    # Insurance & Diversified Financials
    "MFC.TO": "Manulife",
    "SLF.TO": "Sun Life",
    "IFC.TO": "Intact Financial",
    "GWO.TO": "Great-West Lifeco",
    "POW.TO": "Power Corp",
    "FFH.TO": "Fairfax Financial",
    "BN.TO": "Brookfield Corp",
    "BAM.TO": "Brookfield AM",
    "BIP-UN.TO": "Brookfield Infra",
    "BEP-UN.TO": "Brookfield Renewable",
    # Energy - Oil & Gas
    "CNQ.TO": "Canadian Natural",
    "SU.TO": "Suncor",
    "IMO.TO": "Imperial Oil",
    "CVE.TO": "Cenovus",
    "TOU.TO": "Tourmaline Oil",
    "ARX.TO": "ARC Resources",
    "OVV.TO": "Ovintiv",
    "MEG.TO": "MEG Energy",
    "WCP.TO": "Whitecap Resources",
    "TVE.TO": "Tamarack Valley",
    # Energy - Pipelines & Midstream
    "ENB.TO": "Enbridge",
    "TRP.TO": "TC Energy",
    "PPL.TO": "Pembina Pipeline",
    "KEY.TO": "Keyera",
    "IPL.TO": "Inter Pipeline",
    # Mining - Gold
    "ABX.TO": "Barrick Gold",
    "NEM.TO": "Newmont",
    "AEM.TO": "Agnico Eagle",
    "K.TO": "Kinross Gold",
    "ELD.TO": "Eldorado Gold",
    "YRI.TO": "Yamana Gold",
    "WPM.TO": "Wheaton PM",
    "FNV.TO": "Franco-Nevada",
    # Mining - Base Metals & Diversified
    "FM.TO": "First Quantum",
    "TECK-B.TO": "Teck Resources",
    "LUN.TO": "Lundin Mining",
    "HBM.TO": "Hudbay Minerals",
    "IVN.TO": "Ivanhoe Mines",
    "CS.TO": "Capstone Copper",
    # Mining - Uranium & Rare Earths
    "CCO.TO": "Cameco",
    "NXE.TO": "NexGen Energy",
    "DML.TO": "Denison Mines",
    "U.TO": "Sprott Uranium",
    "ARA.TO": "Aclara Resources",
    # Materials - Fertilizers
    "NTR.TO": "Nutrien",
    "MOS.TO": "Mosaic",
    # Telecom
    "BCE.TO": "BCE (Bell)",
    "T.TO": "TELUS",
    "RCI-B.TO": "Rogers",
    "QBR-B.TO": "Quebecor",
    # Technology
    "SHOP.TO": "Shopify",
    "CSU.TO": "Constellation SW",
    "OTEX.TO": "Open Text",
    "DCBO.TO": "Docebo",
    "LSPD.TO": "Lightspeed",
    "NVEI.TO": "Nuvei",
    "KXS.TO": "Kinaxis",
    "DSG.TO": "Descartes",
    "TOI.TO": "Topicus",
    # Industrials - Rail & Transportation
    "CNR.TO": "CN Rail",
    "CP.TO": "CP Kansas City",
    "AC.TO": "Air Canada",
    "TFI.TO": "TFI International",
    # Industrials - Diversified
    "CAE.TO": "CAE Inc",
    "WSP.TO": "WSP Global",
    "STN.TO": "Stantec",
    "NFI.TO": "NFI Group",
    "TFII.TO": "TFI Int'l",
    # Consumer & Retail
    "ATD.TO": "Couche-Tard",
    "L.TO": "Loblaw",
    "MRU.TO": "Metro Inc",
    "DOL.TO": "Dollarama",
    "EMP-A.TO": "Empire (Sobeys)",
    "CTC-A.TO": "Canadian Tire",
    "GIL.TO": "Gildan",
    "GOOS.TO": "Canada Goose",
    "QSR.TO": "Restaurant Brands",
    # Cannabis
    "WEED.TO": "Canopy Growth",
    "ACB.TO": "Aurora Cannabis",
    "TLRY.TO": "Tilray",
    "CRON.TO": "Cronos Group",
    # Real Estate (REITs)
    "REI-UN.TO": "RioCan REIT",
    "HR-UN.TO": "H&R REIT",
    "CAR-UN.TO": "CAPREIT",
    "AP-UN.TO": "Allied Properties",
    "GRT-UN.TO": "Granite REIT",
    "DIR-UN.TO": "Dream Industrial",
    # Healthcare
    "BHC.TO": "Bausch Health",
    "WELL.TO": "WELL Health",
    "DOC.TO": "CloudMD",
    # Utilities
    "FTS.TO": "Fortis",
    "EMA.TO": "Emera",
    "H.TO": "Hydro One",
    "AQN.TO": "Algonquin Power",
    "CPX.TO": "Capital Power",
    "TA.TO": "TransAlta",
    "NPI.TO": "Northland Power",
    # ETFs
    "XIU.TO": "iShares TSX 60",
    "XIC.TO": "iShares TSX Comp",
    "ZCN.TO": "BMO TSX Comp",
}

# Canadian sector groups
CANADA_GROUPS = {
    'canada': {
        'title': 'Canada TSX (All)',
        'tickers': list(CANADA_NAMES.keys()),
    },
    'canada_banks': {
        'title': 'Canada Banks',
        'tickers': ["RY.TO", "TD.TO", "BNS.TO", "BMO.TO", "CM.TO", "NA.TO"],
    },
    'canada_financials': {
        'title': 'Canada Financials',
        'tickers': ["RY.TO", "TD.TO", "BNS.TO", "BMO.TO", "CM.TO", "NA.TO",
                    "MFC.TO", "SLF.TO", "IFC.TO", "GWO.TO", "POW.TO", "FFH.TO",
                    "BN.TO", "BAM.TO", "BIP-UN.TO", "BEP-UN.TO"],
    },
    'canada_energy': {
        'title': 'Canada Energy',
        'tickers': ["CNQ.TO", "SU.TO", "IMO.TO", "CVE.TO", "TOU.TO", "ARX.TO",
                    "OVV.TO", "MEG.TO", "WCP.TO", "TVE.TO", "ENB.TO", "TRP.TO",
                    "PPL.TO", "KEY.TO", "IPL.TO"],
    },
    'canada_oil': {
        'title': 'Canada Oil & Gas',
        'tickers': ["CNQ.TO", "SU.TO", "IMO.TO", "CVE.TO", "TOU.TO", "ARX.TO",
                    "OVV.TO", "MEG.TO", "WCP.TO", "TVE.TO"],
    },
    'canada_pipelines': {
        'title': 'Canada Pipelines',
        'tickers': ["ENB.TO", "TRP.TO", "PPL.TO", "KEY.TO", "IPL.TO"],
    },
    'canada_mining': {
        'title': 'Canada Mining (All)',
        'tickers': ["ABX.TO", "NEM.TO", "AEM.TO", "K.TO", "ELD.TO", "YRI.TO",
                    "WPM.TO", "FNV.TO", "FM.TO", "TECK-B.TO", "LUN.TO", "HBM.TO",
                    "IVN.TO", "CS.TO", "CCO.TO", "NXE.TO", "DML.TO", "U.TO", "ARA.TO"],
    },
    'canada_gold': {
        'title': 'Canada Gold Miners',
        'tickers': ["ABX.TO", "NEM.TO", "AEM.TO", "K.TO", "ELD.TO", "YRI.TO",
                    "WPM.TO", "FNV.TO"],
    },
    'canada_uranium': {
        'title': 'Canada Uranium & Rare Earths',
        'tickers': ["CCO.TO", "NXE.TO", "DML.TO", "U.TO", "ARA.TO"],
    },
    'canada_tech': {
        'title': 'Canada Technology',
        'tickers': ["SHOP.TO", "CSU.TO", "OTEX.TO", "DCBO.TO", "LSPD.TO",
                    "NVEI.TO", "KXS.TO", "DSG.TO", "TOI.TO"],
    },
    'canada_telecom': {
        'title': 'Canada Telecom',
        'tickers': ["BCE.TO", "T.TO", "RCI-B.TO", "QBR-B.TO"],
    },
    'canada_rail': {
        'title': 'Canada Rail & Transport',
        'tickers': ["CNR.TO", "CP.TO", "AC.TO", "TFI.TO"],
    },
    'canada_consumer': {
        'title': 'Canada Consumer & Retail',
        'tickers': ["ATD.TO", "L.TO", "MRU.TO", "DOL.TO", "EMP-A.TO",
                    "CTC-A.TO", "GIL.TO", "GOOS.TO", "QSR.TO"],
    },
    'canada_cannabis': {
        'title': 'Canada Cannabis',
        'tickers': ["WEED.TO", "ACB.TO", "TLRY.TO", "CRON.TO"],
    },
    'canada_reits': {
        'title': 'Canada REITs',
        'tickers': ["REI-UN.TO", "HR-UN.TO", "CAR-UN.TO", "AP-UN.TO",
                    "GRT-UN.TO", "DIR-UN.TO"],
    },
    'canada_utilities': {
        'title': 'Canada Utilities',
        'tickers': ["FTS.TO", "EMA.TO", "H.TO", "AQN.TO", "CPX.TO", "TA.TO", "NPI.TO"],
    },
}

def get_display_name(ticker):
    """Get display name for ticker (company name or ticker if not found)."""
    return CANADA_NAMES.get(ticker, ticker)

# Load price data
print("Loading price data...")
df_prices_all = pd.read_sql(
    "SELECT * FROM stock_prices_daily ORDER BY Date",
    get_db_connection(row_factory=None),
    parse_dates=["Date"],
).set_index("Date")
df_prices_all = df_prices_all.apply(pd.to_numeric, errors='coerce')


def generate_canada_dendrograms(df_prices, period_name, suffix, min_data_points=MIN_DATA_POINTS):
    """Generate dendrograms for all Canada groups."""
    print(f"\n{'='*60}")
    print(f"Generating Canada dendrograms: {period_name}")
    print(f"{'='*60}")

    # Get all Canada tickers that have data
    canada_tickers = list(CANADA_NAMES.keys())
    available = [t for t in canada_tickers if t in df_prices.columns]

    if len(available) < 5:
        print(f"  Not enough Canada tickers with data ({len(available)}). Skipping.")
        return

    # Filter to Canada tickers only
    df_canada = df_prices[available].copy()

    # Filter columns with sufficient data
    valid_cols = df_canada.columns[df_canada.notna().sum() >= min_data_points]
    df_canada = df_canada[valid_cols].copy()

    if len(df_canada.columns) < 5:
        print(f"  Not enough valid tickers after filtering. Skipping.")
        return

    # For Full History, filter to rows where Canada data exists
    first_valid_idx = df_canada.notna().any(axis=1).idxmax()
    df_canada = df_canada.loc[first_valid_idx:]
    print(f"  Data range: {df_canada.index.min().date()} to {df_canada.index.max().date()} ({len(df_canada)} days)")

    if len(df_canada) < min_data_points:
        print(f"  Not enough data ({len(df_canada)} days). Skipping.")
        return

    # Calculate log returns
    df_canada = df_canada.replace(0, np.nan)
    returns = np.log(df_canada).diff()

    # Use reasonable thresholds - for quarterly data, use lower threshold
    # Require at least 30% of data or 30 days, whichever is lower
    col_thresh = min(max(30, int(0.3 * len(returns))), int(0.5 * len(returns)))
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
    for group_key, group_info in CANADA_GROUPS.items():
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
        print(f"  Saved {filename}")

    print(f"\nCanada dendrograms complete for {period_name}")


# Define time periods - calendar based to match UI
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

# Run analysis
print("\n" + "="*60)
print("CANADA STOCKS DENDROGRAM ANALYSIS")
print("="*60)

for period_name, suffix, df_period in periods:
    generate_canada_dendrograms(df_period, period_name, suffix)

# Copy dendrograms to output directory
print(f"\nCopying dendrograms to {OUTPUT_DIR}...")
os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir('.'):
    if filename.startswith('dendrogram_canada') and filename.endswith('.png'):
        src = filename
        dst = os.path.join(OUTPUT_DIR, filename)
        shutil.copy2(src, dst)
        print(f"  Copied {filename}")

print("\nDone!")
