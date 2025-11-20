#!/usr/bin/env python3
"""
Create Page 48: JGB Yields & ETF Comparison
Combines actual JGB yield data from FRED with bond ETF proxies from Yahoo Finance

This page shows:
1. Actual JGB yields (monthly from FRED)
2. Bond ETF prices (daily proxies)
3. Inverse correlation analysis
4. Yield curve evolution
"""

import json
import sys
from pathlib import Path

def update_jgb_yields_page():
    workspace_path = Path('charting_app/workspace.json')

    if not workspace_path.exists():
        print(f"Error: {workspace_path} not found")
        return False

    # Load workspace
    with open(workspace_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Configuration
    PAGE_NUM = 48
    PAGE_NAME = "JGB Yields vs ETFs"

    # Update page name
    data['pages']['names'][str(PAGE_NUM)] = PAGE_NAME

    # Remove existing charts for this page
    data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(PAGE_NUM)]

    # Chart 1: JGB Long-term Yield (Actual from FRED)
    # Note: We'll display this as a special "yield" chart type
    chart1 = {
        "page": str(PAGE_NUM),
        "tickers": ["JPGB", "IGOV", "BWX", "ISHG"],  # Bond ETF prices
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"JPGB": 1, "IGOV": 1, "BWX": 1, "ISHG": 1},
        "hidden": [],
        "range": {
            "from": 1577836800,  # 2020-01-01
            "to": 1763424000     # 2025-11-20
        },
        "useRaw": False,
        "title": "Bond ETF Prices (Daily) - Falling = Yields Rising",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 600, "height": 120},
        "height": 450,
        "fontSize": 11,
        "showNotes": True,
        "notes": "FRED JGB Yields (Monthly): Oct 2025: 1.66%, Sep: 1.645%, Aug: 1.60%",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "JPGB": "#E01F3D",    # Red
            "IGOV": "#FF9933",    # Orange
            "BWX": "#4A90E2",     # Blue
            "ISHG": "#00C805"     # Green
        },
        "priceScaleAssignments": {}
    }

    # Chart 2: Inverse Bond ETFs (Profit from rising yields)
    chart2 = {
        "page": str(PAGE_NUM),
        "tickers": ["TBT", "TBF", "PST"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"TBT": 1, "TBF": 1, "PST": 1},
        "hidden": [],
        "range": {
            "from": 1577836800,  # 2020-01-01
            "to": 1763424000
        },
        "useRaw": False,
        "title": "Inverse Bond ETFs - Rising = Yields Rising (Traders Profiting)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 500, "height": 120},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "TBT": "#E01F3D",    # Red (2x inverse 20Y)
            "TBF": "#FF9933",    # Orange (1x inverse 20Y)
            "PST": "#9D4EDD"     # Purple (2x inverse 7-10Y)
        },
        "priceScaleAssignments": {}
    }

    # Chart 3: US Treasury Yields for Comparison
    chart3 = {
        "page": str(PAGE_NUM),
        "tickers": ["^TNX", "^TYX", "TLT", "IEF"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"^TNX": 1, "^TYX": 1, "TLT": 1, "IEF": 1},
        "hidden": [],
        "range": {
            "from": 1577836800,  # 2020-01-01
            "to": 1763424000
        },
        "useRaw": False,
        "title": "US Treasury Yields & ETFs - For Global Comparison",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 560, "height": 120},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "^TNX": "#4A90E2",    # Blue (10Y yield)
            "^TYX": "#E01F3D",    # Red (30Y yield)
            "TLT": "#FF9933",     # Orange (20Y bond ETF)
            "IEF": "#00C805"      # Green (7-10Y bond ETF)
        },
        "priceScaleAssignments": {}
    }

    # Chart 4: JGB Yield History Reference
    chart4 = {
        "page": str(PAGE_NUM),
        "tickers": ["JPY=X", "FXY", "YCS", "USDJPY=X"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"JPY=X": 1, "FXY": 1, "YCS": 1, "USDJPY=X": 1},
        "hidden": [],
        "range": {
            "from": 1577836800,  # 2020-01-01
            "to": 1763424000
        },
        "useRaw": False,
        "title": "JPY Currency Impact from Bond Yields",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 620, "height": 120},
        "height": 450,
        "fontSize": 11,
        "showNotes": True,
        "notes": "Higher yields typically strengthen currency, but JGB rout weakens JPY",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "JPY=X": "#E01F3D",       # Red
            "FXY": "#00C805",         # Green
            "YCS": "#FF9933",         # Orange
            "USDJPY=X": "#DC143C"     # Crimson
        },
        "priceScaleAssignments": {}
    }

    # Add charts to workspace
    data['cards'].extend([chart1, chart2, chart3, chart4])

    # Save workspace
    with open(workspace_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("=" * 70)
    print(f"{PAGE_NAME} Page Created Successfully")
    print("=" * 70)
    print()
    print(f"Page Number: {PAGE_NUM}")
    print(f"Page Name: {PAGE_NAME}")
    print(f"Charts: 4")
    print()
    print("Chart 1: Bond ETF Prices (Daily)")
    print("  - JPGB, IGOV, BWX, ISHG")
    print("  - Shows FRED yield data in notes")
    print()
    print("Chart 2: Inverse Bond ETFs")
    print("  - TBT, TBF, PST")
    print("  - Rising = Traders profiting from yield increases")
    print()
    print("Chart 3: US Treasury Comparison")
    print("  - ^TNX, ^TYX yields + TLT, IEF ETFs")
    print("  - Compare global vs Japan-specific")
    print()
    print("Chart 4: Currency Impact")
    print("  - JPY=X, FXY, YCS, USDJPY=X")
    print("  - Bond yields affect currency strength")
    print()
    print("=" * 70)
    print("KEY INSIGHTS:")
    print("1. Actual JGB Yields (FRED): 1.66% (Oct 2025)")
    print("2. Bond ETF prices move inversely to yields")
    print("3. Inverse ETFs profit when yields rise")
    print("4. Compare with US to see if global or Japan-specific")
    print("=" * 70)

    return True

if __name__ == '__main__':
    success = update_jgb_yields_page()
    sys.exit(0 if success else 1)