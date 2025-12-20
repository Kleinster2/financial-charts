"""
Global Constants and Configuration
Centralizes magic numbers and configuration values for the entire project
"""

import os
import logging
import sqlite3

# Date Constants
DEFAULT_START_DATE = "2019-12-31"
TRADING_DAYS_PER_YEAR = 252

# Database Configuration
DB_FILENAME = "market_data.db"
SAMPLE_DB_FILENAME = "sample_data.db"
DUCKDB_FILENAME = "market_data.duckdb"
SCHEMA_CACHE_TTL = 3600  # 1 hour in seconds

# Demo mode - set DEMO_MODE=1 to use sample database (for demos/testing without full DB)
DEMO_MODE = os.environ.get('DEMO_MODE', '0') == '1'

# DuckDB toggle - set USE_DUCKDB=1 environment variable to enable
USE_DUCKDB = os.environ.get('USE_DUCKDB', '0') == '1'

# API Configuration
DEFAULT_PORT = 5000
CACHE_CONTROL_MAX_AGE = 0  # No caching for API responses

# Data Processing
VOLUME_WINDOW = 100  # Number of days for volume calculation
PRICE_PRECISION = 2
VOLUME_PRECISION = 1

# File Paths
WORKSPACE_FILENAME = "workspace.json"
WORKSPACE_TEMP_SUFFIX = ".tmp"

# HTTP Status Codes (for clarity)
HTTP_OK = 200
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_ERROR = 500

# Logging Configuration
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Market Categories (for organizing tickers)
TICKER_CATEGORIES = {
    'CORE_INDICES': ['^GSPC', '^DJI', '^IXIC', '^RUT'],
    
    'VOLATILITY_INDICES': [
        '^VIX', '^VIX9D', '^VIX1D', '^VIX3M', '^VIX6M', '^VXV', 
        '^VXD', '^VOLQ', '^VVIX', '^SKEW', '^VXN', '^RVX', '^GVZ', '^OVX'
    ],
    
    'TREASURY_YIELDS': [
        '^IRX',  # 3-month
        '^FVX',  # 5-year
        '^TNX',  # 10-year
        '^TYX'   # 30-year
    ],
    
    'MAJOR_CURRENCIES': [
        'USD', 'EUR', 'JPY', 'GBP', 'CHF', 'AUD', 'NZD', 'CAD'
    ],
    
    'EMERGING_CURRENCIES': [
        'BRL', 'MXN', 'ZAR', 'TRY', 'INR', 'IDR', 'CNY', 'HKD', 
        'KRW', 'RUB', 'COP', 'CLP', 'PHP', 'THB', 'PLN', 'HUF', 
        'CZK', 'RON', 'ILS'
    ],
    
    'PRECIOUS_METALS': [
        'XAUUSD=X', 'XAGUSD=X', 'XPTUSD=X', 'XPDUSD=X'
    ]
}

# Futures Symbols
FUTURES_SYMBOLS = {
    # Energy
    'CRUDE_OIL': 'CL=F',
    'BRENT_OIL': 'BZ=F',
    'NATURAL_GAS': 'NG=F',
    'HEATING_OIL': 'HO=F',
    'GASOLINE': 'RB=F',
    
    # Metals
    'GOLD': 'GC=F',
    'SILVER': 'SI=F',
    'COPPER': 'HG=F',
    'PLATINUM': 'PL=F',
    'PALLADIUM': 'PA=F',
    
    # Grains
    'CORN': 'ZC=F',
    'WHEAT': 'ZW=F',
    'SOYBEANS': 'ZS=F',
    
    # Currencies
    'EURO_FX': '6E=F',
    'JAPANESE_YEN': '6J=F',
    'BRITISH_POUND': '6B=F',
    'SWISS_FRANC': '6S=F',
    'CANADIAN_DOLLAR': '6C=F',
    'AUSTRALIAN_DOLLAR': '6A=F',
    
    # Indices
    'SP500_EMINI': 'ES=F',
    'NASDAQ_EMINI': 'NQ=F',
    'DOW_EMINI': 'YM=F',
    'RUSSELL_EMINI': 'RTY=F',
    'VIX': 'VX=F',
    
    # Bonds
    'US_10Y': 'ZN=F',
    'US_30Y': 'ZB=F',
    'US_5Y': 'ZF=F',
    'US_2Y': 'ZT=F'
}

# Data Quality Thresholds
MIN_DATA_POINTS = 10  # Minimum data points to consider valid
MAX_MISSING_RATIO = 0.5  # Maximum ratio of missing data allowed

# Batch Processing
BATCH_SIZE = 50  # Number of tickers to process at once
RETRY_LIMIT = 3
RETRY_DELAY = 1  # seconds

# Commentary Thresholds
COMMENTARY_THRESHOLDS = {
    'STRONG_UP': 0.03,    # 3% daily gain
    'MODERATE_UP': 0.01,  # 1% daily gain
    'STRONG_DOWN': -0.03, # 3% daily loss
    'MODERATE_DOWN': -0.01 # 1% daily loss
}

# Ticker Aliases - maps alternative tickers to canonical DB tickers
# Used for fundamentals/revenue endpoints where share classes have identical financials
TICKER_ALIASES = {
    # Google: GOOGL (Class A) -> GOOG (Class C) - same financials
    'GOOGL': 'GOOG',
    # Berkshire Hathaway: B shares -> A shares (same financials, different price)
    'BRK-B': 'BRK-A',
    'BRK.B': 'BRK-A',
    # News Corp: Class B -> Class A
    'NWS': 'NWSA',
    # Fox Corporation: Class B -> Class A
    'FOX': 'FOXA',
    # Zillow: Class C -> Class A
    'Z': 'ZG',
    # Under Armour: Class C -> Class A
    'UA': 'UAA',
    # Discovery (now Warner Bros Discovery): Class B/C -> Class A
    'DISCB': 'DISCA',
    'DISCK': 'DISCA',
    # Lionsgate: Class B -> Class A
    'LGF.B': 'LGF.A',
    'LGF-B': 'LGF-A',
}

def resolve_ticker_alias(ticker: str) -> str:
    """Resolve ticker to canonical form for fundamentals lookups."""
    return TICKER_ALIASES.get(ticker.upper(), ticker.upper())

def resolve_ticker_aliases(tickers: list) -> dict:
    """
    Resolve a list of tickers to canonical forms.
    Returns dict mapping original -> canonical (only for those that changed).
    """
    mapping = {}
    for t in tickers:
        canonical = resolve_ticker_alias(t)
        if canonical != t.upper():
            mapping[t.upper()] = canonical
    return mapping

# --- Database Path Resolver -------------------------------------------------
_logger = logging.getLogger(__name__)

def resolve_db_path() -> str:
    """Resolve absolute SQLite database path with demo mode and legacy fallback.

    Order of precedence:
    1) If DEMO_MODE=1: sample_data.db in project root (for demos without full DB)
    2) market_data.db (current, from DB_FILENAME) in project root
    3) sp500_data.db (legacy) in project root, with a deprecation warning
    4) return path to market_data.db even if missing (callers can create it)
    """
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Demo mode: use sample database if available
    if DEMO_MODE:
        sample_db = os.path.join(basedir, SAMPLE_DB_FILENAME)
        if os.path.exists(sample_db):
            _logger.info("DEMO_MODE: Using sample database 'sample_data.db'")
            return sample_db
        _logger.warning(
            "DEMO_MODE enabled but sample_data.db not found. "
            "Run 'python scripts/create_sample_db.py' to create it."
        )

    default_db = os.path.join(basedir, DB_FILENAME)
    legacy_db = os.path.join(basedir, 'sp500_data.db')

    if os.path.exists(default_db):
        return default_db
    if os.path.exists(legacy_db):
        _logger.warning(
            "Using legacy database 'sp500_data.db'. Please migrate to 'market_data.db'."
        )
        return legacy_db
    # Prefer default path even if not present; callers may create the DB
    return default_db

# Absolute path to the active database file
DB_PATH = resolve_db_path()

# Centralized database connection helper
def get_db_connection(row_factory=sqlite3.Row):
    """Return a sqlite3 connection to the active DB.

    Args:
        row_factory: Optional sqlite3 row factory (defaults to sqlite3.Row). Set to None to skip.
    """
    conn = sqlite3.connect(DB_PATH)
    if row_factory is not None:
        conn.row_factory = row_factory
    return conn


# --- DuckDB Path and Connection (Shadow Phase) --------------------------------
def resolve_duckdb_path() -> str:
    """Resolve absolute DuckDB database path.

    Returns path to market_data.duckdb in project root.
    """
    basedir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(basedir, DUCKDB_FILENAME)


# Absolute path to the DuckDB database file
DUCKDB_PATH = resolve_duckdb_path()


def get_duckdb_connection(read_only: bool = True):
    """Return a DuckDB connection.

    Args:
        read_only: If True, open in read-only mode (default for queries).
                   Set to False for write operations.

    Returns:
        duckdb.DuckDBPyConnection

    Raises:
        ImportError: If duckdb is not installed
        FileNotFoundError: If database doesn't exist and read_only=True
    """
    import duckdb

    if read_only and not os.path.exists(DUCKDB_PATH):
        raise FileNotFoundError(f"DuckDB database not found: {DUCKDB_PATH}")

    return duckdb.connect(DUCKDB_PATH, read_only=read_only)


def duckdb_available() -> bool:
    """Check if DuckDB is available and the database exists."""
    try:
        import duckdb
        return os.path.exists(DUCKDB_PATH)
    except ImportError:
        return False
