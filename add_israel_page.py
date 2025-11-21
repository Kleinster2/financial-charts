#!/usr/bin/env python3
"""
Add Israel page to workspace.json

Creates page 43 with Israeli tech companies and market indices.
"""

import json
import sys
from pathlib import Path

def add_israel_page():
    workspace_path = Path('charting_app/workspace.json')

    if not workspace_path.exists():
        print(f"Error: {workspace_path} not found")
        return False

    # Load workspace
    with open(workspace_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Add page 43 to pages list
    if 43 not in data['pages']['pages']:
        data['pages']['pages'].append(43)
        data['pages']['pages'].sort()

    # Add Israel to page names
    data['pages']['names']['43'] = 'Israel'

    # Remove any existing Israel page charts
    data['cards'] = [c for c in data.get('cards', []) if c.get('page') != '43']

    # Chart 1: Israeli Tech Giants
    chart1 = {
        "page": "43",
        "tickers": ["TEVA", "CHKP", "NICE", "EIS"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {
            "TEVA": 1,
            "CHKP": 1,
            "NICE": 1,
            "EIS": 1
        },
        "hidden": [],
        "range": {
            "from": 1420070400,  # 2015-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "Israeli Tech Giants (Teva, Check Point, NICE, iShares Israel ETF)",
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
            "TEVA": "#0038b8",     # Israeli blue
            "CHKP": "#FF6B6B",     # Red
            "NICE": "#4ECDC4",     # Teal
            "EIS": "#95E1D3"       # Light teal
        },
        "priceScaleAssignments": {}
    }

    # Chart 2: Emerging Israeli Tech
    chart2 = {
        "page": "43",
        "tickers": ["WIX", "MNDY", "CYBR", "FVRR"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {
            "WIX": 1,
            "MNDY": 1,
            "CYBR": 1,
            "FVRR": 1
        },
        "hidden": [],
        "range": {
            "from": 1609459200,  # 2021-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "Emerging Israeli Tech (Wix, monday.com, CyberArk, Fiverr)",
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
            "WIX": "#A855F7",      # Purple
            "MNDY": "#F97316",     # Orange
            "CYBR": "#10B981",     # Green
            "FVRR": "#3B82F6"      # Blue
        },
        "priceScaleAssignments": {}
    }

    # Add charts to workspace
    data['cards'].append(chart1)
    data['cards'].append(chart2)

    # Save workspace
    with open(workspace_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("=" * 60)
    print("Israel Page Added Successfully")
    print("=" * 60)
    print()
    print(f"Page Number: 43")
    print(f"Page Name: Israel")
    print(f"Charts Added: 2")
    print()
    print("Chart 1: Israeli Tech Giants")
    print("  Tickers: TEVA, CHKP, NICE, EIS")
    print("  Title: Israeli Tech Giants (Teva, Check Point, NICE, iShares Israel ETF)")
    print()
    print("Chart 2: Emerging Israeli Tech")
    print("  Tickers: WIX, MNDY, CYBR, FVRR")
    print("  Title: Emerging Israeli Tech (Wix, monday.com, CyberArk, Fiverr)")
    print()
    print("=" * 60)
    print("Next Steps:")
    print("1. Restart Flask app: python charting_app/app.py")
    print("2. Open in browser: http://localhost:5000")
    print("3. Navigate to 'Israel' page (page 43)")
    print("=" * 60)

    return True

if __name__ == '__main__':
    success = add_israel_page()
    sys.exit(0 if success else 1)
