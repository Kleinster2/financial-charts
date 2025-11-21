"""
Add implied volatility charts to the workspace.
Adds charts to page 6 (Cboe) and creates a new page 42 (Implied Volatility).
"""

import json
import os

WORKSPACE_PATH = 'charting_app/workspace.json'

# Load existing workspace
with open(WORKSPACE_PATH, 'r') as f:
    workspace = json.load(f)

# Add page 42 for Implied Volatility
if 'pages' not in workspace:
    workspace['pages'] = {}

workspace['pages']['names']['42'] = 'Implied Volatility'
if 42 not in workspace['pages']['pages']:
    workspace['pages']['pages'].append(42)

# Define IV chart configurations
iv_charts = [
    # Page 6 - Cboe - Add VIX and volatility indices
    {
        "page": "6",
        "tickers": ["^VIX", "^VXN", "^VXD"],
        "title": "CBOE Volatility Indices",
        "notes": "VIX (S&P 500), VXN (Nasdaq), VXD (DJIA) implied volatility",
        "height": 500,
        "useRaw": True,  # Use raw values, not percentage
        "tickerColors": {
            "^VIX": "#FF4444",
            "^VXN": "#4444FF",
            "^VXD": "#44AA44"
        }
    },
    # Page 42 - Implied Volatility - Stock IV comparison
    {
        "page": "42",
        "tickers": ["AAPL", "MSFT", "GOOGL", "AMZN"],
        "title": "Tech Giants - Implied Volatility",
        "notes": "ATM implied volatility comparison for mega-cap tech",
        "height": 500,
        "useRaw": True,
        "dataType": "iv",  # New: use IV data instead of price
        "tickerColors": {
            "AAPL": "#4E79A7",
            "MSFT": "#E15759",
            "GOOGL": "#59A14F",
            "AMZN": "#F28E2B"
        }
    },
    {
        "page": "42",
        "tickers": ["TSLA", "NVDA", "AMD", "META"],
        "title": "High Volatility Tech - Implied Volatility",
        "notes": "IV for volatile tech stocks - typically >40%",
        "height": 500,
        "useRaw": True,
        "dataType": "iv",
        "tickerColors": {
            "TSLA": "#E15759",
            "NVDA": "#76B7B2",
            "AMD": "#B07AA1",
            "META": "#4E79A7"
        }
    },
    {
        "page": "42",
        "tickers": ["SPY", "QQQ", "IWM", "DIA"],
        "title": "Index ETFs - Implied Volatility",
        "notes": "ETF implied volatility (typically lower than individual stocks)",
        "height": 500,
        "useRaw": True,
        "dataType": "iv",
        "tickerColors": {
            "SPY": "#4E79A7",
            "QQQ": "#E15759",
            "IWM": "#76B7B2",
            "DIA": "#59A14F"
        }
    },
    {
        "page": "42",
        "tickers": ["^VIX"],
        "title": "VIX - Market Fear Gauge",
        "notes": "S&P 500 30-day implied volatility. >30 = high fear, <15 = complacency",
        "height": 500,
        "useRaw": True,
        "showZeroLine": True,
        "tickerColors": {
            "^VIX": "#FF4444"
        }
    },
    {
        "page": "42",
        "tickers": ["JPM", "BAC", "WFC", "C"],
        "title": "Big Banks - Implied Volatility",
        "notes": "Financial sector IV - sensitive to market stress",
        "height": 500,
        "useRaw": True,
        "dataType": "iv",
        "tickerColors": {
            "JPM": "#4E79A7",
            "BAC": "#E15759",
            "WFC": "#76B7B2",
            "C": "#F28E2B"
        }
    }
]

# Default card properties
default_card = {
    "showDiff": False,
    "showAvg": False,
    "showVol": False,
    "showVolume": False,
    "showRevenue": False,
    "showFundamentalsPane": False,
    "fundamentalsMetrics": ["revenue", "netincome"],
    "multipliers": {},
    "hidden": [],
    "range": {"from": 1609459200, "to": 1763337600},  # 2021-01-01 to 2025-11-18
    "lastLabelVisible": False,
    "lastTickerVisible": False,
    "showZeroLine": False,
    "showFixedLegend": True,
    "showLegendTickers": False,
    "fixedLegendPos": {"x": 10, "y": 10},
    "fixedLegendSize": None,
    "fontSize": 11,
    "showNotes": False,
    "manualInterval": "daily",
    "decimalPrecision": 4  # Show 4 decimals for IV (e.g., 0.3456)
}

# Add IV charts to workspace
for chart_config in iv_charts:
    # Create full card config by merging defaults with specific config
    card = {**default_card, **chart_config}

    # Set multipliers for all tickers
    for ticker in card['tickers']:
        if ticker not in card['multipliers']:
            card['multipliers'][ticker] = 1

    # Add card to workspace
    workspace['cards'].append(card)

    print(f"Added chart: {card['title']} (Page {card['page']})")

# Save updated workspace
with open(WORKSPACE_PATH, 'w') as f:
    json.dump(workspace, f, indent=2)

print(f"\n[OK] Successfully added {len(iv_charts)} implied volatility charts!")
print(f"[OK] Created page 42: 'Implied Volatility'")
print(f"[OK] Added VIX charts to page 6: 'Cboe'")
print("\nNext steps:")
print("1. Restart Flask server or refresh browser")
print("2. Navigate to page 6 (Cboe) or page 42 (Implied Volatility)")
print("3. Charts will show once IV data is available in the database")
print("\nNote: These charts use 'dataType: iv' which needs frontend support.")
print("For now, they will display using the standard price API.")
print("See IMPLIED_VOLATILITY_GUIDE.md for frontend integration details.")
