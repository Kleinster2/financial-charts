#!/usr/bin/env python3
"""
Add Saudi Arabia & GCC page to workspace.json

Creates page 44 with Saudi Arabia and Gulf Cooperation Council (GCC) market ETFs.

GCC Members: Saudi Arabia, UAE, Qatar, Kuwait, Bahrain, Oman
"""

import json
import sys
from pathlib import Path

def add_saudi_gcc_page():
    workspace_path = Path('charting_app/workspace.json')

    if not workspace_path.exists():
        print(f"Error: {workspace_path} not found")
        return False

    # Load workspace
    with open(workspace_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Configuration
    PAGE_NUM = 44
    PAGE_NAME = "Saudi & GCC"

    # Add page to pages list
    if PAGE_NUM not in data['pages']['pages']:
        data['pages']['pages'].append(PAGE_NUM)
        data['pages']['pages'].sort()

    # Add page name
    data['pages']['names'][str(PAGE_NUM)] = PAGE_NAME

    # Remove any existing charts for this page
    data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(PAGE_NUM)]

    # Chart 1: Saudi Arabia Market
    chart1 = {
        "page": str(PAGE_NUM),
        "tickers": ["KSA", "FLSA"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {
            "KSA": 1,
            "FLSA": 1
        },
        "hidden": [],
        "range": {
            "from": 1420070400,  # 2015-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "Saudi Arabia Market (iShares MSCI, Franklin FTSE)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 400, "height": 100},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "KSA": "#006C35",     # Saudi flag green
            "FLSA": "#165C2C"     # Dark green
        },
        "priceScaleAssignments": {}
    }

    # Chart 2: GCC Countries (Qatar, UAE)
    chart2 = {
        "page": str(PAGE_NUM),
        "tickers": ["QAT", "UAE", "GULF"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {
            "QAT": 1,
            "UAE": 1,
            "GULF": 1
        },
        "hidden": [],
        "range": {
            "from": 1388534400,  # 2014-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "GCC Markets (Qatar, UAE, Middle East Dividend)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 400, "height": 120},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "QAT": "#8D1B3D",     # Qatar maroon
            "UAE": "#00732F",     # UAE green
            "GULF": "#C09300"     # Gold
        },
        "priceScaleAssignments": {}
    }

    # Add charts to workspace
    data['cards'].append(chart1)
    data['cards'].append(chart2)

    # Save workspace
    with open(workspace_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("=" * 70)
    print(f"{PAGE_NAME} Page Added Successfully")
    print("=" * 70)
    print()
    print(f"Page Number: {PAGE_NUM}")
    print(f"Page Name: {PAGE_NAME}")
    print(f"Charts Added: 2")
    print()
    print("Chart 1: Saudi Arabia Market")
    print("  Tickers: KSA, FLSA")
    print("  Title: Saudi Arabia Market (iShares MSCI, Franklin FTSE)")
    print()
    print("Chart 2: GCC Markets")
    print("  Tickers: QAT, UAE, GULF")
    print("  Title: GCC Markets (Qatar, UAE, Middle East Dividend)")
    print()
    print("=" * 70)
    print("Gulf Cooperation Council (GCC) Members:")
    print("  - Saudi Arabia (largest economy)")
    print("  - UAE (Dubai, Abu Dhabi)")
    print("  - Qatar (LNG powerhouse)")
    print("  - Kuwait")
    print("  - Bahrain")
    print("  - Oman")
    print("=" * 70)

    return True

if __name__ == '__main__':
    success = add_saudi_gcc_page()
    sys.exit(0 if success else 1)
