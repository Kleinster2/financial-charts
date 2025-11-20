#!/usr/bin/env python3
"""
Alternative Data Sources for Japanese Government Bond (JGB) Yields
Beyond Yahoo Finance integration options
"""

import json
from typing import Dict, List, Any
from datetime import datetime, timedelta
import pandas as pd

# ============================================================================
# DATA SOURCE CONFIGURATIONS
# ============================================================================

DATA_SOURCES = {
    "FRED": {
        "description": "Federal Reserve Economic Data - Free with API key",
        "api_endpoint": "https://api.stlouisfed.org/fred/series/observations",
        "series_codes": {
            "JGB_10Y": "INTGSBJPM193N",  # 10-Year JGB Yield
            "JGB_LONG": "IRLTLT01JPM156N",  # Long-term government bond yields
        },
        "python_library": "fredapi",
        "install": "pip install fredapi",
        "example_code": """
from fredapi import Fred
fred = Fred(api_key='YOUR_API_KEY')
jgb_10y = fred.get_series('INTGSBJPM193N')
""",
        "update_frequency": "Monthly",
        "cost": "Free",
        "pros": ["Official Fed data", "Reliable", "Free API"],
        "cons": ["Monthly updates only", "Not real-time"]
    },

    "BOJ": {
        "description": "Bank of Japan - Official source",
        "api_endpoint": "https://www.stat-search.boj.or.jp/api/en/",
        "data_available": [
            "JGB yield curves (1-40 year)",
            "BOJ policy rates",
            "Money market rates"
        ],
        "formats": ["JSON", "CSV", "Excel"],
        "example_url": "https://www.boj.or.jp/en/statistics/market/bonds/yieldcurve/index.htm",
        "update_frequency": "Daily",
        "cost": "Free",
        "pros": ["Official source", "Complete yield curve", "Daily updates"],
        "cons": ["May need parsing", "Documentation in Japanese"]
    },

    "QUANDL": {
        "description": "Nasdaq Data Link (formerly Quandl)",
        "api_endpoint": "https://data.nasdaq.com/api/v3/",
        "datasets": {
            "MOF_JAPAN": "MOFJ/INTEREST_RATE_JAPAN",
            "JGB_YIELDS": "Various premium datasets"
        },
        "python_library": "quandl",
        "install": "pip install quandl",
        "example_code": """
import quandl
quandl.ApiConfig.api_key = 'YOUR_KEY'
jgb_data = quandl.get('MOFJ/INTEREST_RATE_JAPAN')
""",
        "update_frequency": "Daily",
        "cost": "Free tier + Premium options",
        "pros": ["Easy Python integration", "Historical data"],
        "cons": ["Best data is premium", "Rate limits on free tier"]
    },

    "INVESTING_COM": {
        "description": "Investing.com - Real-time market data",
        "method": "Web scraping or unofficial API",
        "bond_ids": {
            "JGB_2Y": 29228,
            "JGB_5Y": 29229,
            "JGB_10Y": 29230,
            "JGB_30Y": 29231,
            "JGB_40Y": 371349
        },
        "python_library": "investpy (unofficial)",
        "install": "pip install investpy",
        "update_frequency": "Real-time",
        "cost": "Free",
        "pros": ["Real-time data", "All maturities", "Free"],
        "cons": ["Scraping may break", "Not official API"]
    },

    "BLOOMBERG": {
        "description": "Bloomberg Terminal/API - Professional grade",
        "tickers": {
            "JGB_10Y": "JGB10 Index",
            "JGB_30Y": "JGBS30 Index",
            "GENERIC_10Y": "GJGB10 Index"
        },
        "python_library": "blpapi",
        "cost": "~$24,000/year per terminal",
        "pros": ["Real-time", "Most comprehensive", "Professional support"],
        "cons": ["Very expensive", "Requires terminal"]
    },

    "REFINITIV": {
        "description": "Refinitiv Eikon - Professional data",
        "rics": {
            "JGB_10Y": "JP10YT=RR",
            "JGB_30Y": "JP30YT=RR",
            "JGB_5Y": "JP5YT=RR"
        },
        "python_library": "eikon",
        "example_code": """
import eikon as ek
ek.set_app_key('YOUR_APP_KEY')
df = ek.get_timeseries('JP10YT=RR')
""",
        "cost": "~$1,800/month",
        "pros": ["Real-time", "Good API", "Historical data"],
        "cons": ["Expensive", "Requires subscription"]
    }
}

# ============================================================================
# FREE DATA SOURCE IMPLEMENTATION EXAMPLES
# ============================================================================

def fetch_fred_jgb_data(api_key: str, start_date: str = None) -> pd.DataFrame:
    """
    Fetch JGB yield data from FRED (Federal Reserve Economic Data)

    Args:
        api_key: FRED API key (get free at https://fred.stlouisfed.org/docs/api/api_key.html)
        start_date: Start date in YYYY-MM-DD format

    Returns:
        DataFrame with JGB yield data
    """
    try:
        from fredapi import Fred

        fred = Fred(api_key=api_key)

        # Fetch 10-year JGB yields
        jgb_10y = fred.get_series(
            'INTGSBJPM193N',
            observation_start=start_date
        )

        # Create DataFrame
        df = pd.DataFrame({
            'date': jgb_10y.index,
            'jgb_10y_yield': jgb_10y.values
        })

        return df

    except ImportError:
        print("Please install fredapi: pip install fredapi")
        return pd.DataFrame()


def fetch_boj_yield_curve() -> Dict[str, float]:
    """
    Fetch latest JGB yield curve from Bank of Japan
    Note: This is a simplified example - actual implementation would need proper parsing

    Returns:
        Dictionary of maturity: yield pairs
    """
    import requests

    # BOJ publishes yield curve data
    # This is a conceptual example - actual URL and parsing would differ
    url = "https://www.boj.or.jp/en/statistics/market/bonds/yieldcurve/index.htm"

    # In practice, you'd parse the HTML or access their data API
    # Returns example structure:
    return {
        "1Y": 0.005,
        "2Y": 0.010,
        "5Y": 0.025,
        "10Y": 0.065,
        "20Y": 0.450,
        "30Y": 0.650,
        "40Y": 0.750
    }


def fetch_quandl_jgb_data(api_key: str, dataset: str = "MOFJ/INTEREST_RATE_JAPAN") -> pd.DataFrame:
    """
    Fetch JGB data from Quandl/Nasdaq Data Link

    Args:
        api_key: Quandl API key
        dataset: Dataset code

    Returns:
        DataFrame with historical JGB data
    """
    try:
        import quandl

        quandl.ApiConfig.api_key = api_key

        # Fetch the dataset
        data = quandl.get(dataset)

        return data

    except ImportError:
        print("Please install quandl: pip install quandl")
        return pd.DataFrame()


# ============================================================================
# INTEGRATION STRATEGY FOR YOUR CHARTING SYSTEM
# ============================================================================

class JGBDataIntegration:
    """
    Strategy for integrating JGB yield data into your existing system
    """

    def __init__(self):
        self.sources_priority = [
            "FRED",      # Free, reliable, monthly
            "QUANDL",    # Free tier, daily possible
            "BOJ",       # Official, needs parsing
            "INVESTING"  # Real-time but unofficial
        ]

    def recommended_approach(self) -> Dict[str, Any]:
        """
        Recommended integration approach for your system
        """
        return {
            "primary_source": "FRED",
            "reason": "Free, official, reliable API with Python library",
            "backup_source": "BOJ direct",
            "implementation_steps": [
                "1. Get free FRED API key",
                "2. Install fredapi library",
                "3. Create jgb_yields table in SQLite",
                "4. Fetch monthly JGB yields from FRED",
                "5. Store in separate table from stock prices",
                "6. Create visualization combining yfinance ETFs + direct yields"
            ],
            "data_structure": {
                "table_name": "jgb_yields",
                "columns": [
                    "date DATE PRIMARY KEY",
                    "jgb_1y REAL",
                    "jgb_2y REAL",
                    "jgb_5y REAL",
                    "jgb_10y REAL",
                    "jgb_20y REAL",
                    "jgb_30y REAL",
                    "jgb_40y REAL",
                    "source TEXT",
                    "updated_at TIMESTAMP"
                ]
            },
            "update_schedule": "Monthly (FRED updates) or daily (BOJ scraping)",
            "visualization": {
                "chart_type": "Yield curve over time",
                "combine_with": "JPGB ETF prices for correlation analysis"
            }
        }

    def create_hybrid_solution(self) -> str:
        """
        Hybrid solution combining yfinance and external data
        """
        return """
        HYBRID JGB TRACKING SOLUTION:

        1. REAL-TIME PROXIES (via yfinance - already implemented):
           - Bond ETFs: JPGB, IGOV, BWX, ISHG (prices inverse to yields)
           - Inverse ETFs: TBT, TBF, PST (profit from rising yields)
           - Currency: JPY=X, FXY (yield impact on currency)

        2. ACTUAL YIELDS (new integration):
           - FRED API: Monthly official JGB yields (all maturities)
           - Store in separate SQLite table
           - Update monthly via cron/scheduler

        3. COMBINED VISUALIZATION:
           - Chart 1: ETF prices (daily from yfinance)
           - Chart 2: Actual JGB yields (monthly from FRED)
           - Chart 3: Correlation analysis (ETF vs actual yields)
           - Chart 4: Yield curve evolution over time

        4. IMPLEMENTATION PRIORITY:
           a. Keep current yfinance solution (works now)
           b. Add FRED integration for actual yields
           c. Create new page combining both data sources
           d. Optional: Add real-time scraping from Investing.com
        """


# ============================================================================
# QUICK START GUIDE
# ============================================================================

def quick_start_guide():
    """
    Quick start guide for adding JGB yield data
    """
    print("""
    ========================================================================
    QUICK START: Adding JGB Yield Data to Your System
    ========================================================================

    OPTION 1: FRED (Recommended for simplicity)
    --------------------------------------------
    1. Get API key: https://fred.stlouisfed.org/docs/api/api_key.html
    2. Install: pip install fredapi
    3. Add to your update script:

       from fredapi import Fred
       fred = Fred(api_key='YOUR_KEY')
       jgb_10y = fred.get_series('INTGSBJPM193N')

    OPTION 2: Quandl/Nasdaq Data Link
    ----------------------------------
    1. Get API key: https://data.nasdaq.com/sign-up
    2. Install: pip install quandl
    3. Add to your update script:

       import quandl
       quandl.ApiConfig.api_key = 'YOUR_KEY'
       jgb_data = quandl.get('MOFJ/INTEREST_RATE_JAPAN')

    OPTION 3: Direct BOJ Scraping
    -----------------------------
    1. No API key needed
    2. Parse BOJ yield curve page
    3. More complex but gives daily updates

    DATABASE INTEGRATION
    --------------------
    Create new table for yield data:

    CREATE TABLE jgb_yields (
        date DATE PRIMARY KEY,
        jgb_10y REAL,
        jgb_30y REAL,
        source TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    ========================================================================
    """)


if __name__ == "__main__":
    # Print quick start guide
    quick_start_guide()

    # Show available data sources
    print("\nAVAILABLE JGB DATA SOURCES:")
    print("=" * 80)

    for source, info in DATA_SOURCES.items():
        print(f"\n{source}:")
        print(f"  Description: {info['description']}")
        print(f"  Cost: {info.get('cost', 'Unknown')}")
        print(f"  Update Frequency: {info.get('update_frequency', 'Unknown')}")
        if 'pros' in info:
            print(f"  Pros: {', '.join(info['pros'])}")
        if 'cons' in info:
            print(f"  Cons: {', '.join(info['cons'])}")

    print("\n" + "=" * 80)
    print("RECOMMENDED: Start with FRED for free monthly data,")
    print("then optionally add BOJ scraping for daily updates.")
    print("=" * 80)