"""
hierarchical_analysis.py - Hierarchical Clustering with Dendrograms
Uses Ward's method to cluster stocks by correlation distance
Generates analysis for multiple time periods: Full history, 2024, 2025

DENDROGRAM FORMAT STANDARDS
===========================
All dendrograms should follow these conventions:

1. ORIENTATION: Vertical (orientation='right')
   - Labels appear on the LEFT side
   - Distance axis on the BOTTOM

2. LABELS: Use company names/metadata, not raw tickers
   - Format: "TICKER CompanyName" (e.g., "INFY Infosys")
   - Create a name_map dictionary: ticker -> display_name
   - Pass name_map to generate_sector_dendrogram()

3. FILE NAMING: dendrogram_{market}_{sector}{suffix}.png
   - Market: india, china, brazil, korea, canada, etc.
   - Sector: tech, banks, consumer, energy, etc.
   - Suffix: '' (full history), '_2024', '_2025'
   - Examples:
     - dendrogram_india_tech.png
     - dendrogram_india_banks_2024.png
     - dendrogram_china_consumer_2025.png

4. TIME PERIODS: Generate for each period:
   - Full History (no suffix)
   - 2024 (_2024 suffix)
   - 2025 (_2025 suffix)
   - Quarters: _2024_Q1, _2024_Q2, etc.
   - Months: _2024_01, _2024_02, etc.

5. FIGURE SIZE: Scale with number of tickers
   - Height: max(8, num_tickers * 0.25)
   - Width: 14 (standard)

6. OUTPUT DIRECTORY: charting_sandbox/dendrograms/

See india_dendrograms.py for a complete example implementation.
"""

import sqlite3
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
from constants import DB_PATH, get_db_connection
from pathlib import Path

# Output directory for all generated images
OUTPUT_DIR = Path("charting_sandbox/dendrograms")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print(f"Using database: {DB_PATH}")

# --- CONFIG ---
MIN_DATA_POINTS = 50   # Minimum data points required (lowered for yearly analysis)
MAX_TICKERS_FULL = 100  # Max tickers for full dendrogram (readable)
N_CLUSTERS = 15        # Number of clusters to extract

# Sector definitions
TECH_TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'META', 'AMZN', 'NVDA', 'AMD', 'INTC', 'TSM',
                'AVGO', 'QCOM', 'CRM', 'ORCL', 'ADBE', 'NOW', 'PLTR', 'SNOW', 'NET',
                'CRWD', 'PANW', 'DDOG', 'MDB', 'ARM', 'SMCI', 'APP', 'COIN', 'HOOD']

FIN_TICKERS = ['JPM', 'BAC', 'WFC', 'GS', 'MS', 'C', 'USB', 'PNC', 'TFC', 'SCHW',
               'BLK', 'BX', 'KKR', 'AXP', 'V', 'MA', 'PYPL', 'SQ', 'SOFI', 'COIN',
               'COF', 'DFS', 'SYF', 'ALLY']

ENERGY_TICKERS = ['XOM', 'CVX', 'COP', 'EOG', 'SLB', 'OXY', 'PSX', 'VLO', 'MPC',
                  'DVN', 'FANG', 'HAL', 'BKR', 'OKE', 'WMB', 'KMI', 'TRGP']

AI_TICKERS = ['NVDA', 'AMD', 'SMCI', 'AVGO', 'MRVL', 'ARM', 'TSM', 'INTC',
              'MSFT', 'GOOGL', 'META', 'AMZN', 'PLTR', 'SNOW', 'AI', 'BBAI', 'SOUN',
              'IREN', 'CORZ', 'CLSK', 'CIFR', 'WULF', 'VST', 'CEG', 'NRG']

CRYPTO_TICKERS = ['COIN', 'HOOD', 'MSTR', 'MARA', 'RIOT', 'CLSK', 'IREN', 'CORZ',
                  'CIFR', 'WULF', 'BITF', 'HUT', 'HIVE']

CONSUMER_TICKERS = ['AMZN', 'WMT', 'COST', 'TGT', 'HD', 'LOW', 'NKE', 'SBUX', 'MCD',
                    'CMG', 'DPZ', 'YUM', 'LULU', 'RH', 'ULTA', 'DG', 'DLTR']

# Defense/Aerospace (traditional defense, space, drones, defense tech)
DEFENSE_TICKERS = [
    # Prime contractors
    'LMT',   # Lockheed Martin
    'RTX',   # RTX (Raytheon)
    'NOC',   # Northrop Grumman
    'GD',    # General Dynamics
    'BA',    # Boeing
    'LHX',   # L3Harris
    'HII',   # Huntington Ingalls
    # Aerospace suppliers
    'TDG',   # TransDigm
    'HWM',   # Howmet Aerospace
    'TXT',   # Textron
    'AJRD',  # Aerojet Rocketdyne
    # Defense IT/Services
    'LDOS',  # Leidos
    'PLTR',  # Palantir
    'KTOS',  # Kratos Defense
    'BWXT',  # BWX Technologies
    'AXON',  # Axon Enterprise
    'AVAV',  # AeroVironment (drones)
    # Space
    'RKLB',  # Rocket Lab
    'LUNR',  # Intuitive Machines
    'RDW',   # Redwire
    'ASTS',  # AST SpaceMobile
    # eVTOL/Air Mobility
    'JOBY',  # Joby Aviation
    'ACHR',  # Archer Aviation
]

# REITs by property type
REIT_TICKERS = [
    # Data Centers & Towers
    'EQIX',  # Equinix
    'DLR',   # Digital Realty
    'AMT',   # American Tower
    'CCI',   # Crown Castle
    'SBAC',  # SBA Communications
    # Industrial/Logistics
    'PLD',   # Prologis
    # Residential/Apartments
    'EQR',   # Equity Residential
    'AVB',   # AvalonBay
    'MAA',   # Mid-America Apartment
    'UDR',   # UDR Inc
    'CPT',   # Camden Property
    'ESS',   # Essex Property
    'INVH',  # Invitation Homes (SFR)
    # Retail
    'SPG',   # Simon Property (Malls)
    'O',     # Realty Income
    'REG',   # Regency Centers
    'KIM',   # Kimco Realty
    'FRT',   # Federal Realty
    # Office
    'BXP',   # Boston Properties
    'CBRE',  # CBRE Group
    # Healthcare
    'WELL',  # Welltower
    'VTR',   # Ventas
    'PEAK',  # Healthpeak
    # Hotels
    'HST',   # Host Hotels
    # Storage
    'PSA',   # Public Storage
    'EXR',   # Extra Space Storage
    # Specialty
    'VICI',  # VICI Properties (Gaming)
    'IRM',   # Iron Mountain
]

BRAZIL_TICKERS = [
    'ABEV3.SA', 'AZUL4.SA', 'B3SA3.SA', 'BBAS3.SA', 'BBDC3.SA', 'BBDC4.SA', 'BBSE3.SA',
    'BEEF3.SA', 'BPAC11.SA', 'BRAP4.SA', 'BRFS3.SA', 'BRKM5.SA', 'BRML3.SA', 'CCRO3.SA',
    'CIEL3.SA', 'CMIG4.SA', 'COGN3.SA', 'CPFE3.SA', 'CPLE6.SA', 'CSAN3.SA', 'CSNA3.SA',
    'CVCB3.SA', 'CYRE3.SA', 'EGIE3.SA', 'ELET3.SA', 'ELET6.SA', 'EMBR3.SA', 'ENBR3.SA',
    'ENEV3.SA', 'ENGI11.SA', 'EQTL3.SA', 'FLRY3.SA', 'GGBR4.SA', 'GOAU4.SA', 'HAPV3.SA',
    'HYPE3.SA', 'IGTI11.SA', 'IRBR3.SA', 'ITSA4.SA', 'ITUB4.SA', 'JHSF3.SA', 'KLBN11.SA',
    'LREN3.SA', 'MGLU3.SA', 'MRFG3.SA', 'MRVE3.SA', 'MULT3.SA', 'NEOE3.SA', 'PETR3.SA',
    'PETR4.SA', 'PRIO3.SA', 'QUAL3.SA', 'RAIL3.SA', 'RENT3.SA', 'SANB11.SA', 'SBSP3.SA',
    'SUZB3.SA', 'TAEE11.SA', 'TOTS3.SA', 'UGPA3.SA', 'USIM5.SA', 'VALE3.SA', 'VIVT3.SA',
    'WEGE3.SA', 'YDUQ3.SA'
]

# Brazil ticker to short name mapping (ticker + company)
BRAZIL_NAMES = {
    'ABEV3.SA': 'ABEV3 Ambev',
    'AZUL4.SA': 'AZUL4 Azul Airlines',
    'B3SA3.SA': 'B3SA3 B3 Exchange',
    'BBAS3.SA': 'BBAS3 Banco Brasil',
    'BBDC3.SA': 'BBDC3 Bradesco',
    'BBDC4.SA': 'BBDC4 Bradesco PN',
    'BBSE3.SA': 'BBSE3 BB Seguridade',
    'BEEF3.SA': 'BEEF3 Minerva Foods',
    'BPAC11.SA': 'BPAC11 BTG Pactual',
    'BRAP4.SA': 'BRAP4 Bradespar',
    'BRFS3.SA': 'BRFS3 BRF Foods',
    'BRKM5.SA': 'BRKM5 Braskem',
    'BRML3.SA': 'BRML3 BR Malls',
    'CCRO3.SA': 'CCRO3 CCR',
    'CIEL3.SA': 'CIEL3 Cielo',
    'CMIG4.SA': 'CMIG4 Cemig',
    'COGN3.SA': 'COGN3 Cogna Educ',
    'CPFE3.SA': 'CPFE3 CPFL Energia',
    'CPLE6.SA': 'CPLE6 Copel',
    'CSAN3.SA': 'CSAN3 Cosan',
    'CSNA3.SA': 'CSNA3 CSN Steel',
    'CVCB3.SA': 'CVCB3 CVC Brasil',
    'CYRE3.SA': 'CYRE3 Cyrela',
    'EGIE3.SA': 'EGIE3 Engie Brasil',
    'ELET3.SA': 'ELET3 Eletrobras',
    'ELET6.SA': 'ELET6 Eletrobras PNB',
    'EMBR3.SA': 'EMBR3 Embraer',
    'ENBR3.SA': 'ENBR3 Energias BR',
    'ENEV3.SA': 'ENEV3 Eneva',
    'ENGI11.SA': 'ENGI11 Energisa',
    'EQTL3.SA': 'EQTL3 Equatorial',
    'FLRY3.SA': 'FLRY3 Fleury',
    'GGBR4.SA': 'GGBR4 Gerdau',
    'GOAU4.SA': 'GOAU4 Gerdau Met',
    'HAPV3.SA': 'HAPV3 Hapvida',
    'HYPE3.SA': 'HYPE3 Hypera',
    'IGTI11.SA': 'IGTI11 Iguatemi',
    'IRBR3.SA': 'IRBR3 IRB Brasil',
    'ITSA4.SA': 'ITSA4 Itausa',
    'ITUB4.SA': 'ITUB4 Itau Unibanco',
    'JHSF3.SA': 'JHSF3 JHSF',
    'KLBN11.SA': 'KLBN11 Klabin',
    'LREN3.SA': 'LREN3 Lojas Renner',
    'MGLU3.SA': 'MGLU3 Magazine Luiza',
    'MRFG3.SA': 'MRFG3 Marfrig',
    'MRVE3.SA': 'MRVE3 MRV Engen',
    'MULT3.SA': 'MULT3 Multiplan',
    'NEOE3.SA': 'NEOE3 Neoenergia',
    'PETR3.SA': 'PETR3 Petrobras',
    'PETR4.SA': 'PETR4 Petrobras PN',
    'PRIO3.SA': 'PRIO3 PetroRio',
    'QUAL3.SA': 'QUAL3 Qualicorp',
    'RAIL3.SA': 'RAIL3 Rumo',
    'RENT3.SA': 'RENT3 Localiza',
    'SANB11.SA': 'SANB11 Santander BR',
    'SBSP3.SA': 'SBSP3 Sabesp',
    'SUZB3.SA': 'SUZB3 Suzano',
    'TAEE11.SA': 'TAEE11 Taesa',
    'TOTS3.SA': 'TOTS3 Totvs',
    'UGPA3.SA': 'UGPA3 Ultrapar',
    'USIM5.SA': 'USIM5 Usiminas',
    'VALE3.SA': 'VALE3 Vale',
    'VIVT3.SA': 'VIVT3 Telefonica BR',
    'WEGE3.SA': 'WEGE3 WEG',
    'YDUQ3.SA': 'YDUQ3 Yduqs',
}

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
    "688981.SS": "Zhongwang Technology",
    # EV/Batteries/Solar
    "300750.SZ": "CATL",
    "002594.SZ": "BYD",
    "002460.SZ": "Ganfeng Lithium",
    "002466.SZ": "Tianqi Lithium",
    "300014.SZ": "EVE Energy",
    "601012.SS": "LONGi Green Energy",
    "600438.SS": "Tongwei",
    # Semiconductors
    "688012.SS": "SMIC",
    "002371.SZ": "Naura Technology",
    "300223.SZ": "Beijing Huafeng Test",
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

# China A-Shares - All tickers for full dendrogram
CHINA_ALL_TICKERS = [
    # Financial Services
    "601318.SS", "600036.SS", "601166.SS", "600000.SS", "601398.SS",
    "601939.SS", "600016.SS", "601328.SS", "601288.SS", "601601.SS",
    # Consumer/Baijiu
    "600519.SS", "000858.SZ", "000568.SZ", "600809.SS", "000596.SZ",
    "603369.SS", "002304.SZ", "600887.SS", "000895.SZ", "603288.SS",
    # Technology
    "000725.SZ", "002415.SZ", "000063.SZ", "600703.SS", "002230.SZ", "688981.SS",
    # EV/Batteries
    "300750.SZ", "002594.SZ", "002460.SZ", "002466.SZ", "300014.SZ",
    # Semiconductors
    "688012.SS", "002371.SZ", "300223.SZ",
    # Healthcare
    "600276.SS", "000538.SZ", "300122.SZ", "300015.SZ", "002007.SZ",
    # Energy
    "601857.SS", "600028.SS", "601088.SS", "601899.SS", "600547.SS",
    # Industrials
    "600031.SS", "000333.SZ", "000651.SZ", "600690.SS", "601012.SS", "600438.SS",
    # Real Estate
    "600048.SS", "001979.SZ", "000002.SZ",
    # Utilities
    "600900.SS", "601669.SS",
    # ETFs
    "510300.SS", "510050.SS",
]

# China A-Shares by sector
CHINA_FINANCIALS = [
    "601318.SS",  # Ping An Insurance
    "600036.SS",  # China Merchants Bank
    "601166.SS",  # Industrial Bank
    "600000.SS",  # Shanghai Pudong Development Bank
    "601398.SS",  # ICBC
    "601939.SS",  # China Construction Bank
    "600016.SS",  # Minsheng Bank
    "601328.SS",  # Bank of Communications
    "601288.SS",  # Agricultural Bank of China
    "601601.SS",  # China Pacific Insurance
]

CHINA_CONSUMER = [
    "600519.SS",  # Kweichow Moutai
    "000858.SZ",  # Wuliangye
    "000568.SZ",  # Luzhou Laojiao
    "600809.SS",  # Shanxi Fenjiu
    "000596.SZ",  # Gujing Distillery
    "603369.SS",  # King's Luck Brewery
    "002304.SZ",  # Yanghe Brewery
    "600887.SS",  # Inner Mongolia Yili
    "000895.SZ",  # Henan Shuanghui
    "603288.SS",  # Foshan Haitian
]

CHINA_TECH = [
    "000725.SZ",  # BOE Technology
    "002415.SZ",  # Hikvision
    "000063.SZ",  # ZTE Corporation
    "600703.SS",  # SenseTime
    "002230.SZ",  # iFlytek
    "688981.SS",  # Zhongwang Technology
]

CHINA_EV_BATTERY = [
    "300750.SZ",  # CATL
    "002594.SZ",  # BYD (A-share)
    "002460.SZ",  # Ganfeng Lithium
    "002466.SZ",  # Tianqi Lithium
    "300014.SZ",  # EVE Energy
    "601012.SS",  # LONGi Green Energy (solar, correlates with EV/battery)
    "600438.SS",  # Tongwei (solar, correlates with EV/battery)
]

CHINA_SEMICONDUCTORS = [
    "688012.SS",  # SMIC
    "002371.SZ",  # Naura Technology
    "300223.SZ",  # Beijing Huafeng Test
]

CHINA_HEALTHCARE = [
    "600276.SS",  # Jiangsu Hengrui Medicine
    "000538.SZ",  # Yunnan Baiyao
    "300122.SZ",  # Zhifei Biological
    "300015.SZ",  # Aier Eye Hospital
    "002007.SZ",  # Hualan Biological
]

CHINA_ENERGY = [
    "601857.SS",  # PetroChina
    "600028.SS",  # Sinopec
    "601088.SS",  # China Shenhua Energy
    "601899.SS",  # Zijin Mining
    "600547.SS",  # Shandong Gold
    "600900.SS",  # China Yangtze Power (hydroelectric utility)
]

CHINA_INDUSTRIALS = [
    "600031.SS",  # Sany Heavy Industry
    "000333.SZ",  # Midea Group
    "000651.SZ",  # Gree Electric
    "600690.SS",  # Haier Smart Home
]

CHINA_REAL_ESTATE = [
    "600048.SS",  # Poly Developments
    "001979.SZ",  # Merchants Shekou
    "000002.SZ",  # China Vanke
    "601669.SS",  # China Power Construction
]

# Country/Regional ETFs (iShares MSCI series)
COUNTRY_INDEX_TICKERS = [
    'EDEN',  # Denmark
    'EFNL',  # Finland
    'EIDO',  # Indonesia
    'EIRL',  # Ireland
    'EIS',   # Israel
    'ENOR',  # Norway
    'ENZL',  # New Zealand
    'EPOL',  # Poland
    'EWA',   # Australia
    'EWC',   # Canada
    'EWD',   # Sweden
    'EWG',   # Germany
    'EWH',   # Hong Kong
    'EWI',   # Italy
    'EWJ',   # Japan
    'EWK',   # Belgium
    'EWL',   # Switzerland
    'EWM',   # Malaysia
    'EWN',   # Netherlands
    'EWO',   # Austria
    'EWP',   # Spain
    'EWQ',   # France
    'EWS',   # Singapore
    'EWT',   # Taiwan
    'EWU',   # United Kingdom
    'EWW',   # Mexico
    'EWY',   # South Korea
    'EWZ',   # Brazil
    'FXI',   # China Large Cap
    'INDA',  # India
    'MCHI',  # China
    'THD',   # Thailand
]

# 1. Load all price data
print("Loading price data...")
df_prices_all = pd.read_sql(
    "SELECT * FROM stock_prices_daily ORDER BY Date",
    get_db_connection(row_factory=None),
    parse_dates=["Date"],
).set_index("Date")

# Convert to numeric
df_prices_all = df_prices_all.apply(pd.to_numeric, errors='coerce')


def analyze_period(df_prices, period_name, suffix, min_data_points=MIN_DATA_POINTS):
    """
    Run full hierarchical analysis for a given time period.
    """
    print(f"\n{'='*60}")
    print(f"Analyzing period: {period_name}")
    print(f"{'='*60}")

    # Filter columns with sufficient data
    valid_cols = df_prices.columns[df_prices.notna().sum() >= min_data_points]
    df_period = df_prices[valid_cols].copy()

    if len(df_period.columns) < 10:
        print(f"  Not enough tickers with data for {period_name}. Skipping.")
        return None

    # For Full History, trim to where most data actually exists
    # Find where at least 10% of columns have data
    data_density = df_period.notna().sum(axis=1)
    threshold = max(10, int(0.1 * len(df_period.columns)))
    valid_rows = data_density >= threshold
    if valid_rows.any():
        first_valid = valid_rows.idxmax()
        df_period = df_period.loc[first_valid:]
        print(f"  Data range: {df_period.index.min().date()} to {df_period.index.max().date()} ({len(df_period)} days)")

    if len(df_period) < min_data_points:
        print(f"  Not enough data for {period_name} ({len(df_period)} days). Skipping.")
        return None

    # Calculate log returns
    df_period = df_period.replace(0, np.nan)
    returns = np.log(df_period).diff()

    # Drop columns with too many NaNs - use reasonable threshold based on actual data
    col_thresh = max(min_data_points, int(0.3 * len(returns)))
    returns = returns.dropna(axis=1, thresh=col_thresh)

    if len(returns.columns) < 10:
        print(f"  Not enough valid columns after filtering ({len(returns.columns)}). Skipping.")
        return None

    row_thresh = int(0.5 * len(returns.columns))
    returns = returns.dropna(axis=0, thresh=row_thresh)
    returns = returns.fillna(0)

    if len(returns.columns) < 10:
        print(f"  Not enough valid tickers after filtering. Skipping.")
        return None

    print(f"  Analyzing {len(returns.columns)} tickers with {len(returns)} days of data")
    print(f"  Period: {returns.index.min().date()} to {returns.index.max().date()}")

    # Calculate correlation matrix
    corr_matrix = returns.corr().fillna(0)

    # Convert to distance
    dist_matrix = 1 - corr_matrix
    dist_matrix = (dist_matrix + dist_matrix.T) / 2
    np.fill_diagonal(dist_matrix.values, 0)
    dist_matrix = dist_matrix.clip(lower=0, upper=2)

    dist_condensed = squareform(dist_matrix.values, checks=False)

    # Hierarchical clustering
    Z = linkage(dist_condensed, method='ward')

    # Extract clusters
    clusters = fcluster(Z, t=N_CLUSTERS, criterion='maxclust')
    cluster_df = pd.DataFrame({
        'ticker': corr_matrix.columns,
        'cluster': clusters
    })

    # Get top connected stocks
    avg_corr = corr_matrix.abs().mean()
    top_tickers = avg_corr.nlargest(min(MAX_TICKERS_FULL, len(avg_corr))).index.tolist()

    # Generate outputs
    date_range = f"{returns.index.min().strftime('%b %Y')} - {returns.index.max().strftime('%b %Y')}"

    # --- Truncated Dendrogram ---
    print(f"  Generating truncated dendrogram...")
    fig_height = max(15, 50 * 0.3)
    fig, ax = plt.subplots(figsize=(16, fig_height))
    dendrogram(
        Z,
        labels=corr_matrix.columns.tolist(),
        orientation='right',
        leaf_font_size=7,
        truncate_mode='lastp',
        p=50,
        show_contracted=True,
        ax=ax
    )
    ax.set_title(f'Stock Dendrogram - {period_name} ({len(returns.columns)} stocks)\n{date_range}')
    ax.set_xlabel('Distance (1 - Correlation)')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f'dendrogram_truncated{suffix}.png', dpi=150, bbox_inches='tight')
    plt.close()

    # --- Detailed Dendrogram ---
    print(f"  Generating detailed dendrogram...")
    if len(top_tickers) >= 10:
        corr_subset = corr_matrix.loc[top_tickers, top_tickers]
        dist_subset = 1 - corr_subset
        np.fill_diagonal(dist_subset.values, 0)
        dist_condensed_subset = squareform(dist_subset.values)
        Z_subset = linkage(dist_condensed_subset, method='ward')

        fig_height = max(12, len(top_tickers) * 0.15)
        plt.figure(figsize=(12, fig_height))
        dendrogram(
            Z_subset,
            labels=top_tickers,
            orientation='right',
            leaf_font_size=9,
            color_threshold=0.7 * max(Z_subset[:, 2])
        )
        plt.title(f'Stock Dendrogram - Top {len(top_tickers)} Most Connected - {period_name}\n{date_range}')
        plt.xlabel('Distance (1 - Correlation) - Log Scale')
        plt.xscale('log')
        ax = plt.gca()
        xlim = ax.get_xlim()
        ax.set_xlim(max(0.01, xlim[0]), xlim[1])
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'dendrogram_detailed{suffix}.png', dpi=150)
        plt.close()

    # --- Sector Dendrograms ---
    def generate_sector_dendrogram(tickers, title, filename, name_map=None):
        valid_tickers = [t for t in tickers if t in corr_matrix.columns]
        if len(valid_tickers) < 3:
            return

        # Use name_map for labels if provided, otherwise use tickers
        labels = [name_map.get(t, t) for t in valid_tickers] if name_map else valid_tickers

        corr_sub = corr_matrix.loc[valid_tickers, valid_tickers]
        dist_sub = 1 - corr_sub
        np.fill_diagonal(dist_sub.values, 0)
        dist_cond = squareform(dist_sub.values)
        Z_sub = linkage(dist_cond, method='ward')

        fig_height = max(6, len(valid_tickers) * 0.15)
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
        plt.savefig(OUTPUT_DIR / filename, dpi=150)
        plt.close()

    print(f"  Generating sector dendrograms...")
    generate_sector_dendrogram(TECH_TICKERS, 'Technology', f'dendrogram_tech{suffix}.png')
    generate_sector_dendrogram(FIN_TICKERS, 'Financials', f'dendrogram_financials{suffix}.png')
    generate_sector_dendrogram(ENERGY_TICKERS, 'Energy', f'dendrogram_energy{suffix}.png')
    generate_sector_dendrogram(AI_TICKERS, 'AI & Data Centers', f'dendrogram_ai{suffix}.png')
    generate_sector_dendrogram(CRYPTO_TICKERS, 'Crypto & Mining', f'dendrogram_crypto{suffix}.png')
    generate_sector_dendrogram(CONSUMER_TICKERS, 'Consumer', f'dendrogram_consumer{suffix}.png')
    generate_sector_dendrogram(DEFENSE_TICKERS, 'Defense & Aerospace', f'dendrogram_defense{suffix}.png')
    generate_sector_dendrogram(REIT_TICKERS, 'REITs', f'dendrogram_reits{suffix}.png')
    generate_sector_dendrogram(BRAZIL_TICKERS, 'Brazil', f'dendrogram_brazil{suffix}.png', name_map=BRAZIL_NAMES)
    generate_sector_dendrogram(COUNTRY_INDEX_TICKERS, 'Country Indexes', f'dendrogram_countries{suffix}.png')
    # China A-Shares
    generate_sector_dendrogram(CHINA_ALL_TICKERS, 'China A-Shares (All)', f'dendrogram_china{suffix}.png', name_map=CHINA_NAMES)
    generate_sector_dendrogram(CHINA_FINANCIALS, 'China Financials', f'dendrogram_china_financials{suffix}.png', name_map=CHINA_NAMES)
    generate_sector_dendrogram(CHINA_CONSUMER, 'China Consumer/Baijiu', f'dendrogram_china_consumer{suffix}.png', name_map=CHINA_NAMES)
    generate_sector_dendrogram(CHINA_TECH, 'China Technology', f'dendrogram_china_tech{suffix}.png', name_map=CHINA_NAMES)
    generate_sector_dendrogram(CHINA_EV_BATTERY, 'China EV & Battery', f'dendrogram_china_ev{suffix}.png', name_map=CHINA_NAMES)
    generate_sector_dendrogram(CHINA_HEALTHCARE, 'China Healthcare', f'dendrogram_china_healthcare{suffix}.png', name_map=CHINA_NAMES)
    generate_sector_dendrogram(CHINA_ENERGY, 'China Energy', f'dendrogram_china_energy{suffix}.png', name_map=CHINA_NAMES)
    generate_sector_dendrogram(CHINA_INDUSTRIALS, 'China Industrials', f'dendrogram_china_industrials{suffix}.png', name_map=CHINA_NAMES)
    generate_sector_dendrogram(CHINA_REAL_ESTATE, 'China Real Estate', f'dendrogram_china_realestate{suffix}.png', name_map=CHINA_NAMES)

    print(f"  Completed {period_name} analysis")
    return corr_matrix


# Define time periods
periods = [
    ("Full History (2+ years)", "", df_prices_all),
    ("2024", "_2024", df_prices_all[(df_prices_all.index >= '2024-01-01') & (df_prices_all.index < '2025-01-01')]),
    ("2025", "_2025", df_prices_all[df_prices_all.index >= '2025-01-01']),
    # 2024 Quarters
    ("2024 Q1", "_2024_Q1", df_prices_all[(df_prices_all.index >= '2024-01-01') & (df_prices_all.index < '2024-04-01')]),
    ("2024 Q2", "_2024_Q2", df_prices_all[(df_prices_all.index >= '2024-04-01') & (df_prices_all.index < '2024-07-01')]),
    ("2024 Q3", "_2024_Q3", df_prices_all[(df_prices_all.index >= '2024-07-01') & (df_prices_all.index < '2024-10-01')]),
    ("2024 Q4", "_2024_Q4", df_prices_all[(df_prices_all.index >= '2024-10-01') & (df_prices_all.index < '2025-01-01')]),
    # 2025 Quarters
    ("2025 Q1", "_2025_Q1", df_prices_all[(df_prices_all.index >= '2025-01-01') & (df_prices_all.index < '2025-04-01')]),
    ("2025 Q2", "_2025_Q2", df_prices_all[(df_prices_all.index >= '2025-04-01') & (df_prices_all.index < '2025-07-01')]),
    ("2025 Q3", "_2025_Q3", df_prices_all[(df_prices_all.index >= '2025-07-01') & (df_prices_all.index < '2025-10-01')]),
]

# Add monthly periods for 2024 (with lower min_data_points for monthly)
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_periods = []
for month_idx in range(12):
    month_num = month_idx + 1
    start = f'2024-{month_num:02d}-01'
    if month_num == 12:
        end = '2025-01-01'
    else:
        end = f'2024-{month_num+1:02d}-01'
    monthly_periods.append((f"{MONTHS[month_idx]} 2024", f"_2024_{month_num:02d}",
                   df_prices_all[(df_prices_all.index >= start) & (df_prices_all.index < end)]))

# Add monthly periods for 2025 (Jan through Nov)
for month_idx in range(11):  # Jan through Nov 2025
    month_num = month_idx + 1
    start = f'2025-{month_num:02d}-01'
    end = f'2025-{month_num+1:02d}-01'
    monthly_periods.append((f"{MONTHS[month_idx]} 2025", f"_2025_{month_num:02d}",
                   df_prices_all[(df_prices_all.index >= start) & (df_prices_all.index < end)]))

# Run analysis for each period
for period_name, suffix, df_period in periods:
    analyze_period(df_period, period_name, suffix)

# Run monthly analysis with lower threshold (15 trading days minimum)
for period_name, suffix, df_period in monthly_periods:
    analyze_period(df_period, period_name, suffix, min_data_points=15)

print("\n" + "=" * 60)
print("Analysis complete!")
print(f"Generated dendrograms in: {OUTPUT_DIR}/")
print("  - Full History (no suffix)")
print("  - 2024 (_2024 suffix)")
print("  - 2025 (_2025 suffix)")
