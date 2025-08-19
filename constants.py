"""
Global Constants and Configuration
Centralizes magic numbers and configuration values for the entire project
"""

# Date Constants
DEFAULT_START_DATE = "2019-12-31"
TRADING_DAYS_PER_YEAR = 252

# Database Configuration
DB_FILENAME = "sp500_data.db"
SCHEMA_CACHE_TTL = 3600  # 1 hour in seconds

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
        '^VXMT', '^VXD', '^VOLQ', '^VVIX', '^SKEW', '^VXST'
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
