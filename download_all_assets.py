import yfinance as yf
import pandas as pd
import sqlite3
import os
from datetime import datetime, timedelta
import time

# Import constants
from constants import (DB_PATH, get_db_connection, DEFAULT_START_DATE, BATCH_SIZE,
                      RETRY_LIMIT, RETRY_DELAY, TICKER_CATEGORIES,
                      FUTURES_SYMBOLS)

# DuckDB support - imports USE_DUCKDB from constants (set via USE_DUCKDB=1 env var)
from constants import USE_DUCKDB, duckdb_available
if USE_DUCKDB:
    try:
        from duckdb_writer import write_stock_prices
        DUCKDB_AVAILABLE = duckdb_available()
    except ImportError:
        DUCKDB_AVAILABLE = False
else:
    DUCKDB_AVAILABLE = False

# --- CONFIG ---
# Include data starting from December 30th, 2022
START_DATE = DEFAULT_START_DATE
# Use tomorrow's date as end to ensure today's data is included (yfinance treats end date as exclusive)
END_DATE = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

# These lists should be maintained separately as they're not static
# For now we'll keep them here but could move to a config file later
ADR_TICKERS = [
    "BABA", "TSM", "JD", "PDD", "NIO", "MELI", "TM", "SONY", "SAP", "ASML", "BP", "SHEL", "RIO", "TTE", "AZN", "VWAGY",
    "VALE", "PBR", "ITUB", "SHOP", "BNS", "BIDU", "NTES", "SE", "QFIN", "MUFG", "SKM", "KB",
    "INFY", "WIT", "IBN", "HDB", "ABEV", "UL", "HSBC", "NVS", "RHHBY", "UBS", "NXPI", "PHG", "DB", "SIEGY", "NSRGY", "FIG",
    # Canadian banks, Pharma ADRs, Mining
    "RY", "TD", "NVO", "SNY", "DEO", "BHP",
    # Robotics/Industrial ADRs
    "ABB", "FANUY", "ABBNY",
    # Chinese EV/Auto ADRs & HK Stocks
    "GELYF",    # Geely Automobile Holdings (OTC, owns Volvo, Polestar, Lotus)
    "0175.HK"   # Geely Automobile Holdings (Hong Kong Stock Exchange)
]

ETF_TICKERS = [
    # Core U.S. market benchmarks
    "SPY", "RSP", "SPLG", "VTI", "QQQ", "DIA", "IWM",  # added SPLG for ALLW
    # U.S. style / factor ETFs
    "MDY", "IJR", "MTUM", "VLUE", "QUAL", "SPLV",
    # Sector ETFs (GICS)
    "XLK", "XLF", "XLE", "XLV", "XLY", "XLB", "XLI", "XLC", "XLP", "XLRE", "XLU",
    # Additional Energy ETFs
    "OIH", "XOP", "VDE",
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
    # Single-stock volatility indices
    "^VXAPL", "^VXAZN", "^VXGOG", "^VXGS", "^VXIBM",
    # Treasury yield index symbols (yields, not prices)
    "^IRX", "^FVX", "^TNX", "^TYX",
    # Major market indices (US and International)
    "^GSPC", "^DJI", "^IXIC", "^RUT",  # US: S&P 500, Dow, Nasdaq, Russell 2000
    "^N225", "^FTSE", "^GDAXI", "^FCHI", "^STOXX50E", "^IBEX", "^AEX",  # Asia/Europe
    "^BVSP", "^MXX", "^GSPTSE",  # Americas
    "^AXJO", "^HSI", "^NSEI", "^BSESN", "^KS11", "^TWII", "^STI",  # Asia-Pacific
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
    # Robotics & Automation ETFs
    "BOTZ", "ROBO", "IRBO", "ROBT",
    # Electric Vehicle & Autonomous Driving ETFs
    "DRIV", "IDRV", "KARS",
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
    "ABNB","COIN","DDOG","DOCU","HOOD","NET","OKTA","PLTR","RBLX","SHOP","SNOW","SOFI","SPOT","SQ","UBER","ZM",
    "BYND","CELH","CPNG","DASH","LCID","MSTR","NU","RIVN","TOST","U","UPST", "CRWV", "FIG", "PSKY",
    # Data Centers
    "AJBU", "DBRG", "CONE", "QTS", "DTCR", "SRVR", "GDS", "GIGA",
    # Crypto / Blockchain
    "CRCL", "CRON",
]

# Electric Vehicle (EV) stocks
EV_STOCKS = [
    # Pure EV companies (already in OTHER_HIGH_PROFILE_STOCKS: TSLA, LCID, RIVN)
    "BYDDY",   # BYD Company (Chinese EV giant - ADR)
    "LI",      # Li Auto (Chinese EV)
    "XPEV",    # XPeng (Chinese EV)
    "VFS",     # VinFast (Vietnamese EV maker)
    "PSNY",    # Polestar (Volvo/Geely EV brand)
    "GOEV",    # Canoo
    "WKHS",    # Workhorse (EV delivery vans)
    "HYLN",    # Hyliion (electric powertrains for trucks)
    # Traditional automakers with major EV push (F, GM already in S&P 500)
    "HMC",     # Honda Motor Company
    "STLA",    # Stellantis (Chrysler, Jeep, Peugeot, Fiat)
    "POAHY",   # Porsche
    "RACE",    # Ferrari (entering EV market)
    # EV Charging infrastructure
    "CHPT",    # ChargePoint (largest charging network)
    "BLNK",    # Blink Charging
    "EVGO",    # EVgo (fast charging)
    # Delisted/unavailable: FSR (Fisker), LEV, NKLA (Nikola), MULN, RIDE (Lordstown), BMWYY (BMW ADR), FFIE (Faraday Future), ARVL (Arrival)
]

# Mining and rare earth elements equities
MINING_RARE_EARTH_STOCKS = [
    "TMC",    # The Metals Company
    "UAMY",   # United States Antimony Corporation
    "USAR",   # American Resources Corporation
    "NB",     # NioCorp Developments
    "IDR",    # Idaho Strategic Resources
    "MP",     # MP Materials (rare earths)
    "UUUU",   # Energy Fuels (uranium & rare earths)
    "CRML",   # Critical Metals Corp
    "TMQ",    # Trilogy Metals
    "AREC",   # American Resources Corporation
    "TMRC",   # Tectonic Metals
    "REEMF",  # Rare Element Resources
    "ERO",    # Ero Copper
    "PPTA",   # Perpetua Resources
    "LEU",    # Centrus Energy (uranium enrichment)
    "DNN",    # Denison Mines (uranium)
    "GROY",   # Gold Royalty Corp
    "NOVRF",  # NovaTech
    "UROY",   # Uranium Royalty Corp
    "LYC.AX", # Lynas Rare Earths (Australia)
    "ILU.AX", # Iluka Resources (Australia - rare earths & mineral sands)
    "ARU.AX", # Arafura Resources (Australia - rare earths)
    "ARA.TO", # Aclara Resources (Canada - rare earths, Brazil project, Hochschild spin-off)
]

# Battery and energy storage equities
BATTERY_ENERGY_STORAGE_STOCKS = [
    # Battery manufacturers & materials
    "ALB",    # Albemarle (lithium)
    "SQM",    # Sociedad Quimica y Minera (lithium)
    "LAC",    # Lithium Americas
    "LTHM",   # Livent (lithium)
    "STLHF",  # Standard Lithium
    "PLL",    # Piedmont Lithium
    "LTBR",   # Lightbridge Corp
    "QS",     # QuantumScape (solid-state batteries)
    "CBAT",   # CBAK Energy Technology
    "ABML",   # American Battery Technology
    "FREYR",  # FREYR Battery
    # Energy storage systems
    "SEDG",   # SolarEdge Technologies
    "ENPH",   # Enphase Energy
    "STEM",   # Stem Inc
    "FLNC",   # Fluence Energy
    "ENVX",   # Enovix (battery tech)
    "EOSE",   # Eos Energy Enterprises
    "RUN",    # Sunrun (residential solar)
    "NOVA",   # Sunnova Energy (residential solar)
    # Graphite & battery materials
    "NOVRF",  # Nouveau Monde Graphite
    "SYAAF",  # Syrah Resources (graphite)
    "GPH",    # Graphite One
]

# Nuclear energy and uranium equities
NUCLEAR_ENERGY_STOCKS = [
    # Uranium miners
    "CCJ",    # Cameco Corporation
    "UUUU",   # Energy Fuels (also rare earths)
    "DNN",    # Denison Mines
    "URG",    # Ur-Energy
    "UEC",    # Uranium Energy Corp
    "UROY",   # Uranium Royalty Corp
    "LEU",    # Centrus Energy (enrichment)
    "PALAF",  # Paladin Energy
    "BQSSF",  # Boss Energy
    "EU",     # enCore Energy
    # Nuclear technology & SMRs
    "SMR",    # NuScale Power (small modular reactors)
    "OKLO",   # Oklo Inc (advanced nuclear)
    "NNE",    # Nano Nuclear Energy
    "BWXT",   # BWX Technologies
    "GE",     # General Electric (nuclear division)
    "LTBR",   # Lightbridge Corp (nuclear fuel)
]

# Artificial Intelligence and semiconductor equities (beyond mega caps)
AI_SEMICONDUCTOR_STOCKS = [
    "ARM",    # ARM Holdings
    "AVGO",   # Broadcom (already in S&P probably)
    "MRVL",   # Marvell Technology
    "INTC",   # Intel
    "AMD",    # AMD (already in S&P probably)
    "QCOM",   # Qualcomm
    "TSM",    # Taiwan Semiconductor (ADR)
    "ASML",   # ASML Holding (ADR)
    "AMAT",   # Applied Materials
    "LRCX",   # Lam Research
    "KLAC",   # KLA Corporation
    "NVDA",   # NVIDIA (already in S&P)
    "SMCI",   # Super Micro Computer
    "DELL",   # Dell Technologies
    "HPE",    # Hewlett Packard Enterprise
    "SOUN",   # SoundHound AI
    "AI",     # C3.ai
    "BBAI",   # BigBear.ai
    "PATH",   # UiPath
    "SNOW",   # Snowflake
]

# Space and aerospace equities
SPACE_AEROSPACE_STOCKS = [
    "RKLB",   # Rocket Lab
    "ASTS",   # AST SpaceMobile
    "PL",     # Planet Labs
    "SPIR",   # Spire Global
    "BKSY",   # BlackSky Technology
    "LUNR",   # Intuitive Machines
    "VORB",   # Virgin Orbit (if still trading)
    "AJRD",   # Aerojet Rocketdyne (now part of L3Harris)
    "LHX",    # L3Harris Technologies
    "HEI",    # HEICO Corporation
    "TDG",    # TransDigm Group
    "SATS",   # EchoStar Corporation (satellite services)
]

# Defense and military technology equities
DEFENSE_STOCKS = [
    "LMT",    # Lockheed Martin
    "RTX",    # Raytheon Technologies
    "NOC",    # Northrop Grumman
    "GD",     # General Dynamics
    "BA",     # Boeing
    "HII",    # Huntington Ingalls
    "LHX",    # L3Harris Technologies
    "TXT",    # Textron
    "PLTR",   # Palantir (defense AI)
    "AVAV",   # AeroVironment (drones)
    "KTOS",   # Kratos Defense
    "IRDM",   # Iridium Communications
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

# China A-Shares (Shanghai .SS and Shenzhen .SZ exchanges)
# Major constituents of CSI 300 and other key stocks
CHINA_A_SHARES = [
    # Financial Services (Banks, Insurance)
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
    # Consumer/Retail (Baijiu, Food, Beverages)
    "600519.SS",  # Kweichow Moutai (most valuable A-share)
    "000858.SZ",  # Wuliangye Yibin
    "000568.SZ",  # Luzhou Laojiao
    "600809.SS",  # Shanxi Fenjiu
    "000596.SZ",  # Gujing Distillery
    "603369.SS",  # Jiangsu King's Luck Brewery
    "002304.SZ",  # Yanghe Brewery
    "600887.SS",  # Inner Mongolia Yili
    "000895.SZ",  # Henan Shuanghui
    "603288.SS",  # Foshan Haitian
    # Technology/Electronics
    "000725.SZ",  # BOE Technology
    "002415.SZ",  # Hikvision
    "000063.SZ",  # ZTE Corporation
    "600703.SS",  # SenseTime
    "002230.SZ",  # iFlytek
    # Electric Vehicles & Batteries
    "300750.SZ",  # CATL (Contemporary Amperex)
    "002594.SZ",  # BYD (A-share)
    "002460.SZ",  # Ganfeng Lithium
    "002466.SZ",  # Tianqi Lithium
    "300014.SZ",  # EVE Energy
    # Semiconductors & AI Chips
    "688012.SS",  # AMEC (Advanced Micro-Fabrication Equipment)
    "688981.SS",  # SMIC (Semiconductor Manufacturing International)
    "002371.SZ",  # Naura Technology (semiconductor equipment)
    "300223.SZ",  # Beijing Huafeng Test
    "688256.SS",  # Cambricon Technologies (AI chips)
    "688041.SS",  # Hygon Information Technology (x86 CPUs)
    "300474.SZ",  # Jingjia Micro (GPU)
    "688439.SS",  # Moore Threads (GPU/AI chips - "China's Nvidia")
    "688368.SS",  # Shanghai Fullhan Microelectronics
    "603986.SS",  # GigaDevice Semiconductor (flash memory)
    "688521.SS",  # VeriSilicon (IP/design services)
    "688095.SS",  # Empyrean Technology (EDA software)
    "600584.SS",  # JCET Group (packaging/testing)
    # Healthcare/Pharma
    "600276.SS",  # Jiangsu Hengrui Medicine
    "000538.SZ",  # Yunnan Baiyao
    "300122.SZ",  # Zhifei Biological
    "300015.SZ",  # Aier Eye Hospital
    "002007.SZ",  # Hualan Biological
    # Energy & Resources
    "601857.SS",  # PetroChina
    "600028.SS",  # Sinopec
    "601088.SS",  # China Shenhua Energy
    "601899.SS",  # Zijin Mining
    "600547.SS",  # Shandong Gold
    # Industrials/Manufacturing
    "600031.SS",  # Sany Heavy Industry
    "000333.SZ",  # Midea Group
    "000651.SZ",  # Gree Electric
    "600690.SS",  # Haier Smart Home
    "601012.SS",  # LONGi Green Energy
    "600438.SS",  # Tongwei
    # Real Estate (major developers)
    "600048.SS",  # Poly Developments
    "001979.SZ",  # Merchants Shekou
    "000002.SZ",  # China Vanke
    # Infrastructure/Utilities
    "600900.SS",  # China Yangtze Power
    "601669.SS",  # China Power Construction
    # Index ETFs (for reference)
    "510300.SS",  # CSI 300 ETF
    "510050.SS",  # SSE 50 ETF
]

# South Korea (KRX - Korea Exchange, .KS suffix)
# Major constituents of KOSPI and key Korean companies
KOREA_STOCKS = [
    # Semiconductors & Electronics
    "005930.KS",  # Samsung Electronics
    "000660.KS",  # SK Hynix
    "009150.KS",  # Samsung Electro-Mechanics
    "034730.KS",  # SK Inc
    "066570.KS",  # LG Electronics
    "003550.KS",  # LG Corp
    # Internet & Tech
    "035420.KS",  # NAVER
    "035720.KS",  # Kakao
    "259960.KS",  # Krafton (gaming)
    "263750.KS",  # Pearl Abyss (gaming)
    "251270.KS",  # Netmarble (gaming)
    "036570.KS",  # NCsoft (gaming)
    # Batteries & EV
    "006400.KS",  # Samsung SDI
    "051910.KS",  # LG Chem
    "373220.KS",  # LG Energy Solution
    "096770.KS",  # SK Innovation
    # Automotive
    "005380.KS",  # Hyundai Motor
    "000270.KS",  # Kia
    "012330.KS",  # Hyundai Mobis
    "011210.KS",  # Hyundai Wia
    # Biotech & Pharma
    "068270.KS",  # Celltrion
    "207940.KS",  # Samsung Biologics
    "128940.KS",  # Hanmi Pharm
    "326030.KS",  # SK Biopharmaceuticals
    # Financial Services
    "105560.KS",  # KB Financial Group
    "055550.KS",  # Shinhan Financial
    "086790.KS",  # Hana Financial
    "316140.KS",  # Woori Financial
    "000810.KS",  # Samsung Fire & Marine
    # Telecom
    "017670.KS",  # SK Telecom
    "030200.KS",  # KT Corp
    "032640.KS",  # LG Uplus
    # Steel & Chemicals
    "005490.KS",  # POSCO Holdings
    "010130.KS",  # Korea Zinc
    "051900.KS",  # LG H&H (household/cosmetics)
    # Shipbuilding & Heavy Industry
    "009540.KS",  # Hyundai Heavy Industries
    "010140.KS",  # Samsung Heavy Industries
    "042660.KS",  # Daewoo Shipbuilding
    # Trading & Conglomerates
    "028260.KS",  # Samsung C&T
    "000100.KS",  # Yuhan Corp (pharma)
    "018260.KS",  # Samsung SDS
    # Index ETF
    "069500.KS",  # KODEX 200 (KOSPI 200 ETF)
]


# Canada (TSX - Toronto Stock Exchange, .TO suffix)
# Major constituents of S&P/TSX Composite and key Canadian companies
CANADA_STOCKS = [
    # Banks (Big Five + National Bank)
    "RY.TO",     # Royal Bank of Canada
    "TD.TO",     # Toronto-Dominion Bank
    "BNS.TO",    # Bank of Nova Scotia (Scotiabank)
    "BMO.TO",    # Bank of Montreal
    "CM.TO",     # Canadian Imperial Bank of Commerce (CIBC)
    "NA.TO",     # National Bank of Canada
    # Insurance & Diversified Financials
    "MFC.TO",    # Manulife Financial
    "SLF.TO",    # Sun Life Financial
    "IFC.TO",    # Intact Financial
    "GWO.TO",    # Great-West Lifeco
    "POW.TO",    # Power Corporation
    "FFH.TO",    # Fairfax Financial Holdings
    "BN.TO",     # Brookfield Corporation
    "BAM.TO",    # Brookfield Asset Management
    "BIP-UN.TO", # Brookfield Infrastructure Partners
    "BEP-UN.TO", # Brookfield Renewable Partners
    # Energy - Oil & Gas
    "CNQ.TO",    # Canadian Natural Resources
    "SU.TO",     # Suncor Energy
    "IMO.TO",    # Imperial Oil
    "CVE.TO",    # Cenovus Energy
    "TOU.TO",    # Tourmaline Oil
    "ARX.TO",    # ARC Resources
    "OVV.TO",    # Ovintiv
    "MEG.TO",    # MEG Energy
    "WCP.TO",    # Whitecap Resources
    "TVE.TO",    # Tamarack Valley Energy
    # Energy - Pipelines & Midstream
    "ENB.TO",    # Enbridge
    "TRP.TO",    # TC Energy
    "PPL.TO",    # Pembina Pipeline
    "KEY.TO",    # Keyera Corp
    "IPL.TO",    # Inter Pipeline (now Pembina)
    # Mining - Gold
    "ABX.TO",    # Barrick Gold
    "NEM.TO",    # Newmont (dual-listed)
    "AEM.TO",    # Agnico Eagle Mines
    "K.TO",      # Kinross Gold
    "ELD.TO",    # Eldorado Gold
    "YRI.TO",    # Yamana Gold (now Agnico)
    "WPM.TO",    # Wheaton Precious Metals
    "FNV.TO",    # Franco-Nevada
    # Mining - Base Metals & Diversified
    "FM.TO",     # First Quantum Minerals
    "TECK-B.TO", # Teck Resources
    "LUN.TO",    # Lundin Mining
    "HBM.TO",    # Hudbay Minerals
    "IVN.TO",    # Ivanhoe Mines
    "CS.TO",     # Capstone Copper
    # Mining - Uranium & Rare Earths
    "CCO.TO",    # Cameco (uranium)
    "NXE.TO",    # NexGen Energy (uranium)
    "DML.TO",    # Denison Mines (uranium)
    "U.TO",      # Sprott Physical Uranium Trust
    "ARA.TO",    # Aclara Resources (rare earths, Brazil)
    # Materials - Fertilizers & Chemicals
    "NTR.TO",    # Nutrien (potash/fertilizers)
    "MOS.TO",    # Mosaic (dual-listed)
    # Telecom
    "BCE.TO",    # BCE Inc (Bell Canada)
    "T.TO",      # TELUS
    "RCI-B.TO",  # Rogers Communications
    "QBR-B.TO",  # Quebecor
    # Technology
    "SHOP.TO",   # Shopify
    "CSU.TO",    # Constellation Software
    "OTEX.TO",   # Open Text
    "DCBO.TO",   # Docebo
    "LSPD.TO",   # Lightspeed Commerce
    "NVEI.TO",   # Nuvei Corporation
    "KXS.TO",    # Kinaxis
    "DSG.TO",    # Descartes Systems
    "TOI.TO",    # Topicus.com (Constellation spin-off)
    # Industrials - Rail & Transportation
    "CNR.TO",    # Canadian National Railway
    "CP.TO",     # Canadian Pacific Kansas City
    "WJA.TO",    # WestJet (if public)
    "AC.TO",     # Air Canada
    "TFI.TO",    # TFI International
    # Industrials - Diversified
    "CAE.TO",    # CAE Inc (flight simulators)
    "WSP.TO",    # WSP Global (engineering)
    "STN.TO",    # Stantec
    "NFI.TO",    # NFI Group (buses)
    "TFII.TO",   # TFI International (trucking)
    # Consumer & Retail
    "ATD.TO",    # Alimentation Couche-Tard
    "L.TO",      # Loblaw Companies
    "MRU.TO",    # Metro Inc
    "DOL.TO",    # Dollarama
    "EMP-A.TO",  # Empire Company (Sobeys)
    "CTC-A.TO",  # Canadian Tire
    "GIL.TO",    # Gildan Activewear
    "GOOS.TO",   # Canada Goose
    "QSR.TO",    # Restaurant Brands International
    # Cannabis (major players)
    "WEED.TO",   # Canopy Growth
    "ACB.TO",    # Aurora Cannabis
    "TLRY.TO",   # Tilray
    "CRON.TO",   # Cronos Group
    # Real Estate (REITs)
    "REI-UN.TO", # RioCan REIT
    "HR-UN.TO",  # H&R REIT
    "CAR-UN.TO", # Canadian Apartment Properties REIT
    "AP-UN.TO",  # Allied Properties REIT
    "GRT-UN.TO", # Granite REIT
    "DIR-UN.TO", # Dream Industrial REIT
    # Healthcare & Life Sciences
    "BHC.TO",    # Bausch Health
    "WELL.TO",   # WELL Health Technologies
    "DOC.TO",    # CloudMD Software
    # Utilities
    "FTS.TO",    # Fortis Inc
    "EMA.TO",    # Emera
    "H.TO",      # Hydro One
    "AQN.TO",    # Algonquin Power & Utilities
    "CPX.TO",    # Capital Power
    "TA.TO",     # TransAlta
    "NPI.TO",    # Northland Power
    # Index ETFs
    "XIU.TO",    # iShares S&P/TSX 60 ETF
    "XIC.TO",    # iShares Core S&P/TSX Capped Composite ETF
    "ZCN.TO",    # BMO S&P/TSX Capped Composite ETF
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

# Online gaming, iGaming, and gambling equities
GAMING_IGAMING_STOCKS = [
    # Social casino & online gaming
    "DDI",    # DoubleDown Interactive (South Korea - social casino games)
    "PLTK",   # Playtika (social casino & casual games)
    "ZNGA",   # Zynga (now part of Take-Two, but may still trade)
    # Online gambling & sports betting
    "DKNG",   # DraftKings (sports betting & iGaming)
    "PENN",   # Penn Entertainment (casinos & sports betting)
    "MGM",    # MGM Resorts (casinos & BetMGM)
    "CZR",    # Caesars Entertainment (casinos & sports betting)
    "LNW",    # Light & Wonder (gaming equipment & content)
    "FLUT",   # Flutter Entertainment (FanDuel parent)
    "BALY",   # Bally's Corporation
    "GENI",   # Genius Sports (sports data & betting tech)
    "FUBO",   # fuboTV (streaming with gambling integration)
    "RSI",    # Rush Street Interactive (online casino)
    # Video game publishers (related)
    "EA",     # Electronic Arts
    "TTWO",   # Take-Two Interactive
    "RBLX",   # Roblox
    "U",      # Unity Software
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
    Uses a static list (S&P 500 as of October 2025 + Recent IPOs).
    """
    # Static list (S&P 500 October 2025 + Recent IPOs)
    tickers = [
        "MMM", "AOS", "ABT", "ABBV", "ACN", "ADBE", "AMD", "AAP", "AES", "AFL", "A", "APD", "AKAM", "ALK", "ALB", "ARE", "ALGN", "ALLE", "LNT", "ALL", "GOOGL", "GOOG", "MO", "AMZN", "AMCR", "AEE", "AAL", "AEP", "AXP", "AIG", "AMT", "AWK", "AMP", "ABC", "AME", "AMGN", "APH", "ADI", "ANSS", "AON", "APA", "AAPL", "AMAT", "APTV", "ACGL", "ADM", "ANET", "AJG", "AIZ", "T", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "AXON", "BKR", "BALL", "BAC", "BBWI", "BAX", "BDX", "BRK-B", "BBY", "BIO", "TECH", "BIIB", "BLK", "BK", "BA", "BKNG", "BWA", "BXP", "BSX", "BMY", "AVGO", "BR", "BRO", "BF-B", "BLDR", "BG", "CDNS", "CZR", "CPT", "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CTLT", "CAT", "CBOE", "CBRE", "CDW", "CE", "CNC", "CNP", "CDAY", "CF", "CRL", "SCHW", "CHTR", "CVX", "CMG", "CB", "CHD", "CI", "CINF", "CTAS", "CSCO", "C", "CFG", "CLX", "CME", "CMS", "KO", "CTSH", "CL", "CMCSA", "CMA", "CAG", "COP", "ED", "STZ", "CEG", "COO", "CPRT", "GLW", "CTVA", "CSGP", "COST", "CTRA", "CCI", "CSX", "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DAL", "XRAY", "DVN", "DXCM", "FANG", "DLR", "DFS", "DIS", "DG", "DLTR", "D", "DPZ", "DOV", "DOW", "DTE", "DUK", "DD", "EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "ELV", "LLY", "EMR", "ENPH", "ETR", "EOG", "EPAM", "EQT", "EFX", "EQIX", "EQR", "ESS", "EL", "ETSY", "EG", "EVRG", "ES", "EXC", "EXPE", "EXPD", "EXR", "XOM", "FFIV", "FDS", "FICO", "FAST", "FRT", "FDX", "FITB", "FSLR", "FE", "FIS", "FISV", "FLT", "FMC", "F", "FTNT", "FTV", "FOXA", "FOX", "BEN", "FCX", "GRMN", "IT", "GEHC", "GEN", "GNRC", "GD", "GE", "GIS", "GM", "GPC", "GILD", "GL", "GPN", "GS", "HAL", "HIG", "HAS", "HCA", "PEAK", "HSIC", "HSY", "HES", "HPE", "HLT", "HOLX", "HD", "HON", "HRL", "HST", "HWM", "HPQ", "HUBB", "HUM", "HBAN", "HII", "IBM", "IEX", "IDXX", "ITW", "ILMN", "INCY", "IR", "PODD", "INTC", "ICE", "IFF", "IP", "IPG", "INTU", "ISRG", "IVZ", "INVH", "IQV", "IRM", "JBHT", "JKHY", "J", "JNJ", "JCI", "JPM", "JNPR", "K", "KDP", "KEY", "KEYS", "KMB", "KIM", "KMI", "KLAC", "KHC", "KR", "LHX", "LH", "LRCX", "LW", "LVS", "LDOS", "LEN", "LIN", "LYV", "LKQ", "LMT", "L", "LOW", "LULU", "LYB", "MTB", "MRO", "MPC", "MKTX", "MAR", "MMC", "MLM", "MAS", "MA", "MTCH", "MKC", "MCD", "MCK", "MDT", "MRK", "META", "MET", "MTD", "MGM", "MCHP", "MU", "MSFT", "MAA", "MRNA", "MHK", "MOH", "TAP", "MDLZ", "MPWR", "MNST", "MCO", "MS", "MOS", "MSI", "MSCI", "NDAQ", "NTAP", "NFLX", "NWL", "NEM", "NWSA", "NWS", "NEE", "NKE", "NI", "NDSN", "NSC", "NTRS", "NOC", "NCLH", "NRG", "NUE", "NVDA", "NVR", "NXPI", "ORLY", "OXY", "ODFL", "OMC", "ON", "OKE", "ORCL", "OGN", "OTIS", "PCAR", "PKG", "PARA", "PH", "PAYX", "PAYC", "PYPL", "PNR", "PEP", "PKI", "PFE", "PCG", "PM", "PSX", "PNW", "PXD", "PNC", "POOL", "PPG", "PPL", "PFG", "PG", "PGR", "PLD", "PRU", "PEG", "PTC", "PSA", "PHM", "QRVO", "PWR", "QCOM", "DGX", "RL", "RJF", "RTX", "O", "REG", "REGN", "RF", "RSG", "RMD", "RVTY", "RHI", "ROK", "ROL", "ROP", "ROST", "RCL", "SPGI", "CRM", "SBAC", "SLB", "STX", "SEE", "SRE", "NOW", "SHW", "SPG", "SWKS", "SJM", "SNA", "SEDG", "SO", "LUV", "SWK", "SBUX", "STT", "STLD", "STE", "SYK", "SYF", "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR", "TRGP", "TGT", "TEL", "TDY", "TFX", "TER", "TSLA", "TXN", "TXT", "TMO", "TJX", "TSCO", "TT", "TDG", "TRV", "TRMB", "TFC", "TYL", "TSN", "USB", "UDR", "ULTA", "UNP", "UAL", "UPS", "URI", "UNH", "UHS", "VLO", "VTR", "VRSN", "VRSK", "VZ", "VRTX", "VTRS", "VICI", "V", "VMC", "WAB", "WBA", "WMT", "WBD", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC", "WRK", "WY", "WHR", "WMB", "WTW", "GWW", "WYNN", "XEL", "XYL", "YUM", "ZBRA", "ZBH", "ZION", "ZTS", 
        # Recent IPOs added October 2025
        "NTSK", "STUB", "KLAR", "ALH", "FRMI", "APACU", "CBK", "AGRZ", "NP", "KNRX", "KDK", "MGN", "BTQ",
        # Social media
        "SNAP"
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
    Uses a static list (Ibovespa as of October 2025).
    """
    # Static list (Ibovespa October 2025)
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
def update_sp500_data(verbose: bool = True, assets=None, lookback_days: int = None):
    """Update daily market data for selected asset groups.
    assets: list like ['stocks','etfs','adrs','fx','crypto'] or None for all.
    lookback_days: If set, only download data from (today - lookback_days) instead of full history.
                   Use None or 0 for full history download. Default is full history for backward compat.
    """
    # 1. Get S&P 500 list and combine with ETFs
    def vprint(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)

    vprint("Loading index constituents...")
    try:
        # Get S&P 500 tickers from static list
        sp500_tickers, sp500 = get_sp500_tickers()
        vprint(f"Loaded {len(sp500_tickers)} S&P 500 tickers.")

        # 1b. Get Ibovespa tickers (Brazil)
        ibov_tickers = get_ibovespa_tickers()
        vprint(f"Loaded {len(ibov_tickers)} Ibovespa tickers.")
        
        # Generate FX tickers
        FX_TICKERS = build_fx_tickers()
        vprint(f"FX tickers generated: {len(FX_TICKERS)}; additional FX-like: {len(ADDITIONAL_FX_TICKERS)}")
        
        # Build asset groups
        groups = {
            'stocks': [t for t in sorted(list(set(
                sp500_tickers + ibov_tickers + OTHER_HIGH_PROFILE_STOCKS + EV_STOCKS + CRYPTO_STOCKS + QUANTUM_STOCKS +
                ADTECH_STOCKS + GAMING_IGAMING_STOCKS + BIOTECH_STOCKS + MINING_RARE_EARTH_STOCKS + BATTERY_ENERGY_STORAGE_STOCKS +
                NUCLEAR_ENERGY_STOCKS + AI_SEMICONDUCTOR_STOCKS + SPACE_AEROSPACE_STOCKS + DEFENSE_STOCKS
            ))) if t not in EXCLUDED_TICKERS],
            'etfs': ETF_TICKERS,
            'adrs': ADR_TICKERS,
            'fx': sorted(list(set(FX_TICKERS + ADDITIONAL_FX_TICKERS))),
            'crypto': CRYPTO_TICKERS,
            'china': CHINA_A_SHARES,  # Shanghai (.SS) and Shenzhen (.SZ) A-shares
            'korea': KOREA_STOCKS,  # Korea Exchange (.KS) stocks
            'canada': CANADA_STOCKS,  # Toronto Stock Exchange (.TO) stocks
            'brazil': get_ibovespa_tickers(),  # B3 exchange (.SA) stocks
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
                existing_vol_df['Date'] = pd.to_datetime(existing_vol_df['Date'], format='mixed')
                existing_vol_df.set_index('Date', inplace=True)

        # 3. Download data in a fault-tolerant way
        # Use lookback_days for incremental updates (e.g., --lookback 10 for daily updates)
        if lookback_days and lookback_days > 0:
            download_start = (datetime.today() - timedelta(days=lookback_days)).strftime('%Y-%m-%d')
            vprint(f"Incremental update: downloading last {lookback_days} days (from {download_start})")
        else:
            download_start = START_DATE
            vprint(f"Full history download from {START_DATE}")
        
        vprint(f"Downloading/updating data for {len(all_tickers)} securities...")
        # Use yfinance's grouping to handle failed downloads gracefully
        data = yf.download(all_tickers, start=download_start, end=END_DATE, auto_adjust=True, group_by='ticker')

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
            # FIXED: Only update columns that were actually downloaded
            # Previous bug: reindex() added NaN for all non-downloaded tickers, overwriting existing data
            combined_df = existing_df.copy()

            # Add any new columns from new_data_df
            for col in new_data_df.columns:
                if col not in combined_df.columns:
                    combined_df[col] = pd.NA

            # Combine the dataframes: use concat then drop duplicates, keeping new data
            # This handles both existing and new dates properly
            combined_df = pd.concat([combined_df, new_data_df])
            combined_df = combined_df[~combined_df.index.duplicated(keep='last')]
            combined_df = combined_df.sort_index()

            # Now update only the columns that were downloaded with their new values
            for col in new_data_df.columns:
                for date in new_data_df.index:
                    combined_df.loc[date, col] = new_data_df.loc[date, col]
        else:
            combined_df = new_data_df

        # 6b. SAFETY: Never delete columns to preserve historical/delisted ticker data
        # Previously, full refreshes would reindex(columns=all_tickers), deleting any
        # ticker not in current lists (e.g., delisted companies, manual additions).
        # This is now disabled to prevent irreversible data loss.
        all_groups = {'stocks','etfs','adrs','fx','crypto'}
        selected_set = set(selected)
        # if selected_set == all_groups:
        #     combined_df = combined_df.reindex(columns=all_tickers)  # ← DANGEROUS: Deletes unlisted tickers!

        # 6c. Merge volumes with existing (if available), giving precedence to new volume data
        combined_vol_df = pd.DataFrame()
        if not new_vol_df.empty or not existing_vol_df.empty:
            if new_vol_df.empty:
                combined_vol_df = existing_vol_df.copy()
            elif existing_vol_df.empty:
                combined_vol_df = new_vol_df.copy()
            else:
                # FIXED: Same bug as prices - only update columns that were downloaded
                combined_vol_df = existing_vol_df.copy()

                # Add any new columns
                for col in new_vol_df.columns:
                    if col not in combined_vol_df.columns:
                        combined_vol_df[col] = pd.NA

                # Combine and handle both existing and new dates
                combined_vol_df = pd.concat([combined_vol_df, new_vol_df])
                combined_vol_df = combined_vol_df[~combined_vol_df.index.duplicated(keep='last')]
                combined_vol_df = combined_vol_df.sort_index()

                # Update only downloaded columns
                for col in new_vol_df.columns:
                    for date in new_vol_df.index:
                        combined_vol_df.loc[date, col] = new_vol_df.loc[date, col]
            # SAFETY: Never delete volume columns (same reasoning as prices)
            # if selected_set == all_groups:
            #     combined_vol_df = combined_vol_df.reindex(columns=all_tickers)  # ← DANGEROUS: Deletes unlisted tickers!

        # 7. Save to database using STAGING TABLE pattern for safety
        vprint("Saving data to database...")

        # Pre-write validation
        if combined_df.empty:
            vprint("ERROR: Combined DataFrame is empty. Aborting write.")
            return

        index_label = combined_df.index.name or 'Date'

        # Get existing table info for comparison
        existing_rows = existing_df.shape[0] if not existing_df.empty else 0
        existing_cols = existing_df.shape[1] if not existing_df.empty else 0
        new_rows = combined_df.shape[0]
        new_cols = combined_df.shape[1]

        vprint(f"  Existing table: {existing_rows} rows × {existing_cols} columns")
        vprint(f"  New data:       {new_rows} rows × {new_cols} columns")

        # Sanity checks
        if existing_rows > 0 and new_rows < existing_rows * 0.5:
            vprint(f"  WARNING: New row count ({new_rows}) is less than 50% of existing ({existing_rows})")
            vprint(f"  This might indicate a download failure. Proceeding with caution...")

        if existing_cols > 0 and new_cols < existing_cols:
            vprint(f"  INFO: Column count decreased from {existing_cols} to {new_cols}")
            vprint(f"  This is expected when not all asset groups are selected.")
            vprint(f"  Missing columns will be preserved from existing data.")

        # Write to staging table first
        staging_table = "stock_prices_daily_staging"
        vprint(f"  Writing to staging table: {staging_table}")
        # Clean up any leftover staging artifacts (indexes from previous failed runs)
        cursor.execute(f"DROP TABLE IF EXISTS {staging_table}")
        cursor.execute(f"DROP INDEX IF EXISTS ix_{staging_table}_Date")
        conn.commit()
        combined_df.astype(float).to_sql(staging_table, conn, if_exists="replace", index=True, index_label=index_label)

        # Validate staging table
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {staging_table}")
        staging_row_count = cursor.fetchone()[0]

        if staging_row_count != new_rows:
            vprint(f"  ERROR: Staging table row count mismatch ({staging_row_count} != {new_rows}). Aborting.")
            cursor.execute(f"DROP TABLE IF EXISTS {staging_table}")
            conn.commit()
            return

        vprint(f"  [OK] Staging table validated ({staging_row_count} rows)")

        # Atomic swap: Rename staging -> main
        vprint("  Performing atomic table swap...")
        cursor.execute("DROP TABLE IF EXISTS stock_prices_daily_old")
        if table_exists:
            cursor.execute("ALTER TABLE stock_prices_daily RENAME TO stock_prices_daily_old")
        cursor.execute(f"ALTER TABLE {staging_table} RENAME TO stock_prices_daily")

        # Keep old table as backup for one write cycle (will be dropped on next run)
        if table_exists:
            vprint(f"  [OK] Old table preserved as 'stock_prices_daily_old' (backup)")

        conn.commit()
        vprint(f"  [OK] Prices table updated successfully")

        # Same pattern for volumes
        if not combined_vol_df.empty:
            staging_vol_table = "stock_volumes_daily_staging"
            vprint(f"  Writing volumes to staging table: {staging_vol_table}")
            # Clean up any leftover staging artifacts
            cursor.execute(f"DROP TABLE IF EXISTS {staging_vol_table}")
            cursor.execute(f"DROP INDEX IF EXISTS ix_{staging_vol_table}_Date")
            conn.commit()
            # Convert NA to NaN before astype to avoid TypeError
            vol_df_clean = combined_vol_df.fillna(pd.NA).infer_objects(copy=False)
            vol_df_clean = vol_df_clean.apply(pd.to_numeric, errors='coerce')
            vol_df_clean.to_sql(staging_vol_table, conn, if_exists="replace", index=True, index_label=index_label)

            cursor.execute(f"SELECT COUNT(*) FROM {staging_vol_table}")
            staging_vol_row_count = cursor.fetchone()[0]
            vprint(f"  [OK] Volume staging table validated ({staging_vol_row_count} rows)")

            cursor.execute("DROP TABLE IF EXISTS stock_volumes_daily_old")
            if vol_table_exists:
                cursor.execute("ALTER TABLE stock_volumes_daily RENAME TO stock_volumes_daily_old")
            cursor.execute(f"ALTER TABLE {staging_vol_table} RENAME TO stock_volumes_daily")
            conn.commit()
            vprint(f"  [OK] Volumes table updated successfully")
        if 'stocks' in selected_set:
            sp500.to_sql("stock_metadata", conn, if_exists="replace", index=False)
        else:
            vprint("Skipping stock_metadata update (stocks not selected).")
        vprint(f"Database updated. Now contains {combined_df.shape[1]} securities with {combined_df.shape[0]} daily prices.")

        # Write to DuckDB if enabled (Phase 1: shadow database)
        if USE_DUCKDB and DUCKDB_AVAILABLE:
            vprint("\n" + "="*60)
            vprint("[DuckDB] Writing to shadow database...")
            vprint("="*60)
            try:
                write_stock_prices(combined_df, combined_vol_df, verbose=verbose)
                vprint("[DuckDB] Shadow database updated successfully")
            except Exception as e:
                vprint(f"[DuckDB] Warning: Failed to write to DuckDB: {e}")

        # Auto-update ticker metadata for new tickers
        try:
            from metadata_utils import auto_update_new_tickers
            vprint("\n" + "="*60)
            vprint("Auto-updating metadata for new tickers...")
            vprint("="*60)
            stats = auto_update_new_tickers()
            if stats['successful'] > 0 or stats['failed'] > 0:
                vprint(f"Metadata update: {stats['successful']} added, {stats['failed']} failed, {stats['skipped']} skipped")
            else:
                vprint("All tickers already have metadata")
        except Exception as e:
            vprint(f"Warning: Could not auto-update metadata: {e}")

    finally:
        conn.close()

def update_market_data(verbose: bool = True, assets=None, lookback_days: int = None):
    """Compatibility alias for broader project scope."""
    return update_sp500_data(verbose=verbose, assets=assets, lookback_days=lookback_days)

if __name__ == "__main__":
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='Download/update market data from Yahoo Finance')
    parser.add_argument('-v', '--verbose', action='store_true', default=True, help='Verbose output')
    parser.add_argument('-q', '--quiet', action='store_true', help='Suppress output')
    parser.add_argument('--lookback', type=int, default=None,
                        help='Days to look back for incremental updates (default: full history). Use 10 for daily updates.')
    parser.add_argument('--full', action='store_true', help='Force full history download (ignore --lookback)')
    parser.add_argument('--assets', nargs='+', 
                        choices=['stocks', 'etfs', 'adrs', 'fx', 'crypto', 'china', 'korea', 'canada', 'brazil'],
                        help='Asset groups to update (default: all)')
    
    args = parser.parse_args()
    
    verbose = not args.quiet
    lookback = None if args.full else args.lookback
    
    update_market_data(verbose=verbose, assets=args.assets, lookback_days=lookback)
