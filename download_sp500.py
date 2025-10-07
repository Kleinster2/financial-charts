import yfinance as yf
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import time
import requests
from bs4 import BeautifulSoup

# Import constants
from constants import (DB_PATH, get_db_connection, DEFAULT_START_DATE, BATCH_SIZE, 
                      RETRY_LIMIT, RETRY_DELAY, TICKER_CATEGORIES,
                      FUTURES_SYMBOLS)

# --- CONFIG ---
# Include data starting from December 30th, 2022
START_DATE = DEFAULT_START_DATE
END_DATE = datetime.today().strftime("%Y-%m-%d")

# These lists should be maintained separately as they're not static
# For now we'll keep them here but could move to a config file later
ADR_TICKERS = [
    "BABA", "TSM", "JD", "PDD", "NIO", "MELI", "TM", "SONY", "SAP", "ASML", "BP", "SHEL", "RIO", "TTE", "AZN", "VWAGY",
    "VALE", "PBR", "ITUB", "SHOP", "BNS", "BIDU", "NTES", "SE", "QFIN", "MUFG", "SKM", "KB",
    "INFY", "WIT", "IBN", "HDB", "ABEV", "UL", "HSBC", "NVS", "RHHBY", "UBS", "NXPI", "PHG", "DB", "SIEGY", "NSRGY", "FIG"
]

ETF_TICKERS = [
    # Core U.S. market benchmarks
    "SPY", "RSP", "SPLG", "VTI", "QQQ", "DIA", "IWM",  # added SPLG for ALLW
    # U.S. style / factor ETFs
    "MDY", "IJR", "MTUM", "VLUE", "QUAL", "SPLV",
    # Sector ETFs (GICS)
    "XLK", "XLF", "XLE", "XLV", "XLY", "XLB", "XLI", "XLC", "XLP", "XLRE", "XLU",
    # Broad international equity baskets
    "EFA", "EEM", "IEFA", "VWO", "SPEM",  # added SPEM for ALLW
    # Single-country developed market ETFs
    "EWZ", "EWW", "EWJ", "EWU", "EWG", "EWQ", "EWC", "EWA", "EWL", "EWS", "EWI", "EWP", "EWN", "EWD", "EWO", "EWH", "EWK", "EWM", "EDEN", "EFNL", "EIRL", "EIS", "ENZL", "ENOR",
    # Single-country emerging market ETFs
    "EWZ", "EWT", "EWY", "EWW", "EZA", "TUR", "THD", "EPOL", "EIDO", "FM", "FXI", "GXC",  # added GXC for ALLW
    # Fixed income & alternative asset ETFs
    "TLT", "HYG", "TIP", "LQD", "VNQ", "BIL", "AGG", "BND", "IEF", "IEI", "SHY", "SHV", "EMB", "JNK", "BNDX",
    # Multi-asset / risk parity ETFs
    "ALLW", "RPAR", "AOR", "AOM", "NTSX", "UPAR", "PARR",
    # Commodities, currencies & volatility
    "GLD","SLV", "USO", "DBA", "UUP", "UDN", "FXE", "FXB", "FXY", "FXA", "CYB", "FXC", "FXF", "DBC", "GSG", "COMB", "PDBC", "BNO", "UNG", "UGA", "KOLD", "BOIL", "IAU", "CPER", "PPLT", "PALL", "WEAT", "CORN", "SOYB", "CANE", "COCO", "COW", "PICK", "XME", "GDX", "GDXJ", "SIL", "RINF", "COMT",
    # Volatility indices (Yahoo '^' symbols) and ETNs
    "^VIX", "^VIX9D", "^VIX1D", "^VIX3M", "^VIX6M", "^VXV", "^VXD", "^VOLQ", "^VVIX", "^SKEW", "VXX", "UVXY", "SVXY", "^VXN", "^RVX", "^VXO", "^GVZ", "^OVX", "^EVZ", "^VXEFA", "^VXEWZ",
    # Treasury yield index symbols (yields, not prices)
    "^IRX", "^FVX", "^TNX", "^TYX",  # added comma after TYX
    # Additional Vanguard ETFs
    "VIG", "VUG", "VTV", "VYM", "VGT", "VNQ", "VB", "VBR", "VOO", "IVV",
    "VEA", "VXUS", "VT", "VEU", "SCZ", "DXJ", "HEDJ",
    "ASHR", "VGK", "VPL", "VNQI", "VIGI", "VSS", "IEMG", "EMQQ",
    "EEMV", "DGS", "DGRO", "DTD", "DVY", "NOBL", "PFF", "IGSB", "IGIB",
    "EMLC", "GOVT", "IAGG", "MUB",
    # iShares ETFs
    "IWF", "IWD", "IWO", "IWN",
    # ARK ETFs
    "ARKG", "ARKK", "ARKW", "ARKQ", "ARKF",
    # Clean energy ETFs
    "ICLN", "TAN", "LIT", "QCLN", "PBW", "FAN",
    # Technology ETFs
    "SOXX", "SMH", "PAVE", "MJ", "QTUM",
    # International ETFs
    "RSX", "INDA",
    # Leveraged ETFs
    "QLD", "SSO", "UPRO", "TQQQ", "SOXL", "SPXL", "TMF",
    "TNA", "FAS", "ERX", "LABU", "NUGT", "JNUG", "UGAZ", "UCO", "BOIL",
    # Inverse ETFs
    "PSQ", "SH", "SDS", "SPXU", "SPXS", "SQQQ", "SDOW", "SRTY", "TZA", "FAZ",
    "ERY", "LABD", "DRIP", "DUST", "JDST", "DGAZ", "SCO", "VIXY",
    # Crypto ETFs (spot, futures, blockchain)
    # -- Bitcoin spot ETFs
    "IBIT", "FBTC", "ARKB", "BITB", "HODL", "BTCO", "EZBC", "BRRR", "GBTC",
    # -- Bitcoin futures/inverse ETFs
    "BITO", "BTF", "XBTF", "BITI",
    # -- Blockchain/crypto industry ETFs
    "BLOK", "DAPP", "BKCH", "BITQ"
]

# Core indices with the ^prefix
core_indices = TICKER_CATEGORIES['CORE_INDICES']
# Volatility indices
volatility_indices = TICKER_CATEGORIES['VOLATILITY_INDICES']
# Other indices and rates
other_indices = TICKER_CATEGORIES['TREASURY_YIELDS']

# Additional FX tickers (extra crosses, indices)
ADDITIONAL_FX_TICKERS = [
    # Extra USD crosses
    "USDSGD=X", "USDSEK=X", "USDNOK=X", "USDISK=X", "USDTWD=X", "USDARS=X", "USDSAR=X", "USDAED=X",
    "USDKZT=X", "USDVND=X", "USDKWD=X",
    # Non-USD major crosses
    "AUDJPY=X", "CADJPY=X", "CHFJPY=X", "EURCAD=X", "EURAUD=X", "EURNOK=X", "EURNZD=X", "EURSEK=X", "GBPCAD=X", "GBPAUD=X",
    # Currency indices
    "DX-Y.NYB", "^BXY"
]

# Stablecoins
STABLECOIN_TICKERS = ["USDT-USD", "USDC-USD", "DAI-USD"]

# Top-crypto tickers
CRYPTO_TICKERS = [
    "BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "SOL-USD", "ADA-USD", "DOGE-USD", "TON-USD",
    "TRX-USD", "AVAX-USD", "SHIB-USD", "DOT-USD", "MATIC-USD", "LINK-USD", "ATOM-USD", "LTC-USD", "BCH-USD", "UNI-USD",
    "XLM-USD", "ETC-USD", "FIL-USD", "ICP-USD", "APT-USD", "HBAR-USD", "ARB-USD", "MKR-USD", "VET-USD", "NEAR-USD",
    "OP-USD", "IMX-USD", "KAS-USD", "RNDR-USD", "AAVE-USD", "LDO-USD", "ALGO-USD", "QNT-USD", "EGLD-USD", "SAND-USD",
    "AXS-USD", "XTZ-USD", "THETA-USD", "MANA-USD", "GRT-USD", "CHZ-USD", "FLOW-USD", "XEC-USD", "DASH-USD", "HYPE-USD"
]

# High-profile non-S&P 500 U.S. stocks to track
OTHER_HIGH_PROFILE_STOCKS = [
    "ABNB","COIN","DDOG","DOCU","HOOD","NET","OKTA","PLTR","RBLX","SHOP","SNOW","SOFI","SQ","UBER","ZM",
    "BYND","CELH","CPNG","DASH","LCID","MSTR","NU","RIVN","TOST","U","UPST", "CRWV", "FIG", "PSKY",
    # Data Centers
    "AJBU", "DBRG", "CONE", "QTS", "DTCR", "SRVR", "GDS", "GIGA",
    # Crypto / Blockchain
    "CRCL", "CRON",
]

# Crypto-exposed equities (miners, exchanges, infrastructure)
CRYPTO_STOCKS = [
    # Miners
    "RIOT", "MARA", "HUT", "HIVE", "BITF", "CIFR", "CORZ", "IREN", "WULF", "CLSK", "BTBT", "SDIG", "CAN",
    # Platforms / infra
    "BKKT",
]

# Quantum computing and quantum tech-related equities
QUANTUM_STOCKS = [
    "IONQ", "RGTI", "QBTS", "ARQQ", "QUBT"
]

# Adtech / app monetization / measurement and programmatic advertising equities
ADTECH_STOCKS = [
    "APP",   # AppLovin
    "TTD",   # The Trade Desk
    "MGNI",  # Magnite
    "PUBM",  # PubMatic
    "IAS",   # Integral Ad Science
    "DV",    # DoubleVerify
    "PERI",  # Perion Network
    "APPS",  # Digital Turbine
    "RAMP",  # LiveRamp
    "CRTO",  # Criteo
    "ZETA",  # Zeta Global
    "TBLA",  # Taboola
    "SSTK",  # Shutterstock
    "ROKU"   # Roku (CTV ad platform)
]

# Biotech, pharmaceutical, and life sciences equities
BIOTECH_STOCKS = [
    # Vaccine & COVID-related
    "NVAX", "BNTX", "VXRT", "INO", "MRNA",
    # Established large pharma/biotech  
    "GILD", "BIIB", "AMGN", "REGN", "VRTX", "ILMN",
    # Specialty pharmaceutical
    "BMRN", "ALNY", "TECH", "SRPT", "RARE",
    # Gene editing & cell therapy
    "CRSP", "EDIT", "NTLA", "BEAM",
    # Biotech tools & diagnostics
    "EXAS", "PACB", "TWST", "CDNA",
    # Emerging biotech
    "ZLAB", "HALO", "FOLD", "AGEN", "SAVA", "AXSM", "JAZZ", "PTCT"
]

# Tickers that consistently fail to download (excluded from universe)
EXCLUDED_TICKERS = [
    "JBSS3.SA",  # No Yahoo data
    "GOLL4.SA",  # No Yahoo data
    "SULA11.SA", # No Yahoo data
    "OB",        # Removed from static lists
    "FSR",       # Removed from static lists
]

# Foreign exchange tickers (major + EM pairs)
MAJOR_CCY = ["USD","EUR","JPY","GBP","CHF","AUD","NZD","CAD"]
EM_CCY = [
    "BRL","MXN","ZAR","TRY","INR","IDR","CNY","HKD","KRW","RUB",
    "COP","CLP","PHP","THB","PLN","HUF","CZK","RON","ILS",
]

def build_fx_tickers():
    fx = []
    # All major crosses, both directions (excludes self-crosses automatically)
    fx += make_pairs(MAJOR_CCY, MAJOR_CCY)
    # USD-EM pairs, both directions
    fx += make_pairs(["USD"], EM_CCY)
    fx += make_pairs(EM_CCY, ["USD"])
    # Precious metals as currencies
    fx += ["XAUUSD=X", "XAGUSD=X", "XPTUSD=X", "XPDUSD=X"]
    return unique_preserve(fx)

def make_pairs(bases, quotes, suffix="=X"):
    """Generate Yahoo FX tickers like 'EURUSD=X' for all base-quote combos where base != quote."""
    return [f"{b}{q}{suffix}" for b in bases for q in quotes if b != q]

def unique_preserve(seq):
    seen = set()
    out = []
    for s in seq:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out

def get_sp500_tickers():
    """Return a list of S&P 500 constituent tickers.
    Tries to scrape the Wikipedia S&P 500 page; if that fails, falls back to a static list.
    """
    try:
        tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
        sp500 = tables[0]
        sp500['Symbol'] = sp500['Symbol'].str.replace('.', '-', regex=False)
        tickers = sp500['Symbol'].tolist()
        if tickers:
            return tickers, sp500
    except Exception as e:
        print(f"Warning: Could not scrape S&P 500 constituents: {e}. Falling back to static list.")
    
    # Static fallback list (S&P 500 August 2025 + Recent IPOs)
    tickers = [
        "MMM", "AOS", "ABT", "ABBV", "ACN", "ADBE", "AMD", "AAP", "AES", "AFL", "A", "APD", "AKAM", "ALK", "ALB", "ARE", "ALGN", "ALLE", "LNT", "ALL", "GOOGL", "GOOG", "MO", "AMZN", "AMCR", "AEE", "AAL", "AEP", "AXP", "AIG", "AMT", "AWK", "AMP", "ABC", "AME", "AMGN", "APH", "ADI", "ANSS", "AON", "APA", "AAPL", "AMAT", "APTV", "ACGL", "ADM", "ANET", "AJG", "AIZ", "T", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "AXON", "BKR", "BALL", "BAC", "BBWI", "BAX", "BDX", "BRK-B", "BBY", "BIO", "TECH", "BIIB", "BLK", "BK", "BA", "BKNG", "BWA", "BXP", "BSX", "BMY", "AVGO", "BR", "BRO", "BF-B", "BLDR", "BG", "CDNS", "CZR", "CPT", "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CTLT", "CAT", "CBOE", "CBRE", "CDW", "CE", "CNC", "CNP", "CDAY", "CF", "CRL", "SCHW", "CHTR", "CVX", "CMG", "CB", "CHD", "CI", "CINF", "CTAS", "CSCO", "C", "CFG", "CLX", "CME", "CMS", "KO", "CTSH", "CL", "CMCSA", "CMA", "CAG", "COP", "ED", "STZ", "CEG", "COO", "CPRT", "GLW", "CTVA", "CSGP", "COST", "CTRA", "CCI", "CSX", "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DAL", "XRAY", "DVN", "DXCM", "FANG", "DLR", "DFS", "DIS", "DG", "DLTR", "D", "DPZ", "DOV", "DOW", "DTE", "DUK", "DD", "EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "ELV", "LLY", "EMR", "ENPH", "ETR", "EOG", "EPAM", "EQT", "EFX", "EQIX", "EQR", "ESS", "EL", "ETSY", "EG", "EVRG", "ES", "EXC", "EXPE", "EXPD", "EXR", "XOM", "FFIV", "FDS", "FICO", "FAST", "FRT", "FDX", "FITB", "FSLR", "FE", "FIS", "FISV", "FLT", "FMC", "F", "FTNT", "FTV", "FOXA", "FOX", "BEN", "FCX", "GRMN", "IT", "GEHC", "GEN", "GNRC", "GD", "GE", "GIS", "GM", "GPC", "GILD", "GL", "GPN", "GS", "HAL", "HIG", "HAS", "HCA", "PEAK", "HSIC", "HSY", "HES", "HPE", "HLT", "HOLX", "HD", "HON", "HRL", "HST", "HWM", "HPQ", "HUBB", "HUM", "HBAN", "HII", "IBM", "IEX", "IDXX", "ITW", "ILMN", "INCY", "IR", "PODD", "INTC", "ICE", "IFF", "IP", "IPG", "INTU", "ISRG", "IVZ", "INVH", "IQV", "IRM", "JBHT", "JKHY", "J", "JNJ", "JCI", "JPM", "JNPR", "K", "KDP", "KEY", "KEYS", "KMB", "KIM", "KMI", "KLAC", "KHC", "KR", "LHX", "LH", "LRCX", "LW", "LVS", "LDOS", "LEN", "LIN", "LYV", "LKQ", "LMT", "L", "LOW", "LULU", "LYB", "MTB", "MRO", "MPC", "MKTX", "MAR", "MMC", "MLM", "MAS", "MA", "MTCH", "MKC", "MCD", "MCK", "MDT", "MRK", "META", "MET", "MTD", "MGM", "MCHP", "MU", "MSFT", "MAA", "MRNA", "MHK", "MOH", "TAP", "MDLZ", "MPWR", "MNST", "MCO", "MS", "MOS", "MSI", "MSCI", "NDAQ", "NTAP", "NFLX", "NWL", "NEM", "NWSA", "NWS", "NEE", "NKE", "NI", "NDSN", "NSC", "NTRS", "NOC", "NCLH", "NRG", "NUE", "NVDA", "NVR", "NXPI", "ORLY", "OXY", "ODFL", "OMC", "ON", "OKE", "ORCL", "OGN", "OTIS", "PCAR", "PKG", "PARA", "PH", "PAYX", "PAYC", "PYPL", "PNR", "PEP", "PKI", "PFE", "PCG", "PM", "PSX", "PNW", "PXD", "PNC", "POOL", "PPG", "PPL", "PFG", "PG", "PGR", "PLD", "PRU", "PEG", "PTC", "PSA", "PHM", "QRVO", "PWR", "QCOM", "DGX", "RL", "RJF", "RTX", "O", "REG", "REGN", "RF", "RSG", "RMD", "RVTY", "RHI", "ROK", "ROL", "ROP", "ROST", "RCL", "SPGI", "CRM", "SBAC", "SLB", "STX", "SEE", "SRE", "NOW", "SHW", "SPG", "SWKS", "SJM", "SNA", "SEDG", "SO", "LUV", "SWK", "SBUX", "STT", "STLD", "STE", "SYK", "SYF", "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR", "TRGP", "TGT", "TEL", "TDY", "TFX", "TER", "TSLA", "TXN", "TXT", "TMO", "TJX", "TSCO", "TT", "TDG", "TRV", "TRMB", "TFC", "TYL", "TSN", "USB", "UDR", "ULTA", "UNP", "UAL", "UPS", "URI", "UNH", "UHS", "VLO", "VTR", "VRSN", "VRSK", "VZ", "VRTX", "VTRS", "VICI", "V", "VMC", "WAB", "WBA", "WMT", "WBD", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC", "WRK", "WY", "WHR", "WMB", "WTW", "GWW", "WYNN", "XEL", "XYL", "YUM", "ZBRA", "ZBH", "ZION", "ZTS", 
        # Recent IPOs added October 2025
        "NTSK", "STUB", "KLAR", "ALH", "FRMI", "APACU", "CBK", "AGRZ", "NP", "KNRX", "KDK", "MGN", "BTQ"
    ]
    
    # Create a minimal DataFrame with just the tickers
    sp500 = pd.DataFrame({
        'ticker': tickers,
        'name': [f"Company {i}" for i in range(len(tickers))],  # Placeholder names
        'sector': ["Unknown" for _ in range(len(tickers))]  # Placeholder sectors
    })
    
    return tickers, sp500

def get_ibovespa_tickers():
    """Return a list of Ibovespa constituent tickers formatted for Yahoo Finance (ending with '.SA').
    Tries to scrape the Wikipedia Ibovespa page; if that fails, falls back to a static list captured July 2025.
    """
    try:
        tables = pd.read_html("https://en.wikipedia.org/wiki/Ibovespa")
        for tbl in tables:
            # The column may be named either 'Ticker' or 'Code' depending on Wiki revision
            candidate_cols = [col for col in tbl.columns if str(col).lower() in ("ticker", "code")]
            if candidate_cols:
                col = candidate_cols[0]
                tickers = (
                    tbl[col]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                    .str.replace(r"\\.B3$", "", regex=True)
                    + ".SA"
                )
                # Filter out invalid entries such as nan or ''
                tickers = [t for t in tickers.unique().tolist() if t and t != "NAN.SA"]
                if tickers:
                    return tickers
    except Exception as e:
        print(f"Warning: Could not scrape Ibovespa constituents: {e}. Falling back to static list.")

    # Static fallback list (Ibovespa July 2025)
    return [
        "ABEV3.SA","AZUL4.SA","B3SA3.SA","BBAS3.SA","BBDC3.SA","BBDC4.SA","BBSE3.SA","BEEF3.SA","BPAC11.SA",
        "BRAP4.SA","BRFS3.SA","BRKM5.SA","BRML3.SA","CCRO3.SA","CIEL3.SA","CMIG4.SA","COGN3.SA","CPFE3.SA",
        "CPLE6.SA","CSAN3.SA","CSNA3.SA","CVCB3.SA","CYRE3.SA","EGIE3.SA","ELET3.SA","ELET6.SA","EMBR3.SA",
        "ENBR3.SA","ENEV3.SA","ENGI11.SA","EQTL3.SA","FLRY3.SA","GGBR4.SA","GOAU4.SA","GOLL4.SA","HAPV3.SA",
        "HGTX3.SA","HYPE3.SA","IGTI11.SA","IRBR3.SA","ITSA4.SA","ITUB4.SA","JBSS3.SA","JHSF3.SA","KLBN11.SA",
        "LREN3.SA","MGLU3.SA","MRFG3.SA","MRVE3.SA","MULT3.SA","NEOE3.SA","PETR3.SA","PETR4.SA","PRIO3.SA",
        "QUAL3.SA","RAIL3.SA","RENT3.SA","SANB11.SA","SBSP3.SA","SULA11.SA","SUZB3.SA","TAEE11.SA","TIMP3.SA",
        "TOTS3.SA","UGPA3.SA","USIM5.SA","VALE3.SA","VIVT3.SA","WEGE3.SA","YDUQ3.SA",
    ]

# --- Main function to orchestrate the download ---
def update_sp500_data(verbose: bool = True, assets=None):
    """Update daily market data for selected asset groups.
    assets: list like ['stocks','etfs','adrs','fx','crypto'] or None for all.
    """
    # 1. Get S&P 500 list and combine with ETFs
    def vprint(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)

    vprint("Fetching US large-cap index constituents...")
    try:
        # Get S&P 500 tickers with fallback to static list
        sp500_tickers, sp500 = get_sp500_tickers()
        vprint(f"Fetched {len(sp500_tickers)} S&P 500 tickers.")
        
        # 1b. Get Ibovespa tickers (Brazil)
        ibov_tickers = get_ibovespa_tickers()
        vprint(f"Fetched {len(ibov_tickers)} Ibovespa tickers.")
        
        # Generate FX tickers
        FX_TICKERS = build_fx_tickers()
        vprint(f"FX tickers generated: {len(FX_TICKERS)}; additional FX-like: {len(ADDITIONAL_FX_TICKERS)}")
        
        # Build asset groups
        groups = {
            'stocks': [t for t in sorted(list(set(
                sp500_tickers + ibov_tickers + OTHER_HIGH_PROFILE_STOCKS + CRYPTO_STOCKS + QUANTUM_STOCKS + ADTECH_STOCKS + BIOTECH_STOCKS
            ))) if t not in EXCLUDED_TICKERS],
            'etfs': ETF_TICKERS,
            'adrs': ADR_TICKERS,
            'fx': sorted(list(set(FX_TICKERS + ADDITIONAL_FX_TICKERS))),
            'crypto': CRYPTO_TICKERS,
        }
        selected = list(groups.keys()) if not assets else [a.lower() for a in assets]
        unknown = [a for a in selected if a not in groups]
        if unknown:
            vprint(f"Warning: ignoring unknown asset groups: {', '.join(unknown)}")
            selected = [a for a in selected if a in groups]
        if not selected:
            selected = list(groups.keys())
            vprint("No valid asset groups selected; defaulting to all groups.")
        vprint(f"Selected asset groups: {', '.join(selected)}")
        # Expand tickers based on selection
        all_tickers = sorted(list(set(sum((groups[a] for a in selected), []))))
    except Exception as e:
        raise SystemExit(f"Failed to fetch US large-cap list: {e}")

    # 2. Determine what needs to be downloaded
    vprint(f"Using database: {DB_PATH}")
    conn = get_db_connection(row_factory=None)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_prices_daily';")
        table_exists = cursor.fetchone() is not None
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_volumes_daily';")
        vol_table_exists = cursor.fetchone() is not None

        # Load existing data (if any) from the daily prices table
        existing_df = pd.DataFrame()
        existing_vol_df = pd.DataFrame()
        if table_exists:
            # Read without date parsing first so that an empty table doesn’t raise a KeyError
            existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
            if not existing_df.empty and 'Date' in existing_df.columns:
                # Robust date parsing to handle mixed formats (e.g., "YYYY-MM-DD" and locale-specific)
                def _safe_parse(s):
                    try:
                        return pd.to_datetime(s, format="%Y-%m-%d", errors="raise")
                    except Exception:
                        # Fallback: let pandas infer or treat dayfirst as needed; coerce invalid to NaT
                        return pd.to_datetime(s, errors="coerce", dayfirst=False)
                existing_df['Date'] = existing_df['Date'].apply(_safe_parse)
                existing_df.dropna(subset=['Date'], inplace=True)
                existing_df.set_index('Date', inplace=True)
        if vol_table_exists:
            existing_vol_df = pd.read_sql("SELECT * FROM stock_volumes_daily", conn)
            if not existing_vol_df.empty and 'Date' in existing_vol_df.columns:
                existing_vol_df['Date'] = pd.to_datetime(existing_vol_df['Date'])
                existing_vol_df.set_index('Date', inplace=True)

        # 3. Download data in a fault-tolerant way
        vprint(f"Downloading/updating data for {len(all_tickers)} securities...")
        # Use yfinance's grouping to handle failed downloads gracefully
        data = yf.download(all_tickers, start=START_DATE, end=END_DATE, auto_adjust=True, group_by='ticker')

        if data.empty:
            print("No data returned from Yahoo Finance.")
            return

        # 4. Process downloaded data ticker by ticker
        processed_dfs = []
        processed_vol_dfs = []
        for ticker in all_tickers:
            if ticker in data and not data[ticker].empty:
                # Extract just the 'Close' price and rename the series to the ticker
                close_series = data[ticker][['Close']].rename(columns={'Close': ticker})
                processed_dfs.append(close_series)
                # Extract 'Volume' where available
                if 'Volume' in data[ticker].columns:
                    vol_series = data[ticker][['Volume']].rename(columns={'Volume': ticker})
                    processed_vol_dfs.append(vol_series)
            else:
                print(f"- Warning: Could not download data for {ticker}. It will be skipped.")

        if not processed_dfs:
            print("Data processing failed for all tickers.")
            return

        # 5. Combine all processed dataframes into one (prices)
        new_data_df = pd.concat(processed_dfs, axis=1)
        new_data_df.index = pd.to_datetime(new_data_df.index)
        # 5b. Combine volumes (if any)
        new_vol_df = pd.DataFrame()
        if processed_vol_dfs:
            new_vol_df = pd.concat(processed_vol_dfs, axis=1)
            new_vol_df.index = pd.to_datetime(new_vol_df.index)

        # 6. Merge with existing data, giving precedence to new data (prices)
        if not existing_df.empty:
            # Align columns to ensure safe combination
            existing_cols = existing_df.columns
            new_cols = new_data_df.columns
            combined_cols = sorted(list(set(existing_cols) | set(new_cols)))
            
            existing_df = existing_df.reindex(columns=combined_cols)
            new_data_df = new_data_df.reindex(columns=combined_cols)
            
            combined_df = new_data_df.combine_first(existing_df)
        else:
            combined_df = new_data_df

        # 6b. Restrict to current ticker universe only if we're running a full refresh
        # For partial asset updates, preserve existing columns to avoid dropping data.
        all_groups = {'stocks','etfs','adrs','fx','crypto'}
        selected_set = set(selected)
        if selected_set == all_groups:
            combined_df = combined_df.reindex(columns=all_tickers)

        # 6c. Merge volumes with existing (if available), giving precedence to new volume data
        combined_vol_df = pd.DataFrame()
        if not new_vol_df.empty or not existing_vol_df.empty:
            if new_vol_df.empty:
                combined_vol_df = existing_vol_df.copy()
            elif existing_vol_df.empty:
                combined_vol_df = new_vol_df.copy()
            else:
                existing_vol_cols = existing_vol_df.columns
                new_vol_cols = new_vol_df.columns
                combined_vol_cols = sorted(list(set(existing_vol_cols) | set(new_vol_cols)))
                existing_vol_df = existing_vol_df.reindex(columns=combined_vol_cols)
                new_vol_df = new_vol_df.reindex(columns=combined_vol_cols)
                combined_vol_df = new_vol_df.combine_first(existing_vol_df)
            # Restrict to current ticker universe only for full refresh
            if selected_set == all_groups:
                combined_vol_df = combined_vol_df.reindex(columns=all_tickers)

        # 7. Save to database
        vprint("Saving data to database...")
        # Ensure index name for proper DB column naming
        index_label = combined_df.index.name or 'Date'
        combined_df.astype(float).to_sql("stock_prices_daily", conn, if_exists="replace", index=True, index_label=index_label)
        if not combined_vol_df.empty:
            combined_vol_df.astype(float).to_sql("stock_volumes_daily", conn, if_exists="replace", index=True, index_label=index_label)
        if 'stocks' in selected_set:
            sp500.to_sql("stock_metadata", conn, if_exists="replace", index=False)
        else:
            vprint("Skipping stock_metadata update (stocks not selected).")
        vprint(f"Database updated. Now contains {combined_df.shape[1]} securities with {combined_df.shape[0]} daily prices.")

    finally:
        conn.close()

def update_market_data(verbose: bool = True, assets=None):
    """Compatibility alias for broader project scope."""
    return update_sp500_data(verbose=verbose, assets=assets)

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    verbose = True
    if any(a in ("--quiet", "-q") for a in argv):
        verbose = False
    if any(a in ("--verbose", "-v") for a in argv):
        verbose = True
    update_market_data(verbose=verbose)
