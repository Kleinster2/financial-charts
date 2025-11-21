#!/usr/bin/env python3
"""
Add India page to workspace.json

Creates page 45 with Indian market ETFs and major Indian companies (ADRs).

India: World's 5th largest economy, fastest-growing major economy,
tech services hub, 1.4 billion population.
"""

import json
import sys
from pathlib import Path

def add_india_page():
    workspace_path = Path('charting_app/workspace.json')

    if not workspace_path.exists():
        print(f"Error: {workspace_path} not found")
        return False

    # Load workspace
    with open(workspace_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Configuration
    PAGE_NUM = 45
    PAGE_NAME = "India"

    # Add page to pages list
    if PAGE_NUM not in data['pages']['pages']:
        data['pages']['pages'].append(PAGE_NUM)
        data['pages']['pages'].sort()

    # Add page name
    data['pages']['names'][str(PAGE_NUM)] = PAGE_NAME

    # Remove any existing charts for this page
    data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(PAGE_NUM)]

    # Chart 1: India Market ETFs
    chart1 = {
        "page": str(PAGE_NUM),
        "tickers": ["INDA", "INDY", "EPI", "SMIN"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {
            "INDA": 1,
            "INDY": 1,
            "EPI": 1,
            "SMIN": 1
        },
        "hidden": [],
        "range": {
            "from": 1356998400,  # 2013-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "India Market ETFs (iShares MSCI, India 50, Earnings, Small-Cap)",
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
            "INDA": "#FF9933",    # Indian flag saffron
            "INDY": "#138808",    # Indian flag green
            "EPI": "#000080",     # Navy blue
            "SMIN": "#FF6B35"     # Orange
        },
        "priceScaleAssignments": {}
    }

    # Chart 2: Indian IT Services & Banks
    chart2 = {
        "page": str(PAGE_NUM),
        "tickers": ["INFY", "WIT", "HDB", "IBN", "RDY"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {
            "INFY": 1,
            "WIT": 1,
            "HDB": 1,
            "IBN": 1,
            "RDY": 1
        },
        "hidden": [],
        "range": {
            "from": 1262304000,  # 2010-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "Indian Blue Chips (Infosys, Wipro, HDFC, ICICI, Dr. Reddy's)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 500, "height": 150},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "INFY": "#FF9933",    # Saffron (Infosys)
            "WIT": "#4A90E2",     # Blue (Wipro)
            "HDB": "#138808",     # Green (HDFC Bank)
            "IBN": "#E85D04",     # Dark orange (ICICI Bank)
            "RDY": "#9D4EDD"      # Purple (Dr. Reddy's)
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
    print("Chart 1: India Market ETFs")
    print("  Tickers: INDA, INDY, EPI, SMIN")
    print("  Focus: Broad market, top 50, earnings, small-cap")
    print()
    print("Chart 2: Indian Blue Chips")
    print("  Tickers: INFY, WIT, HDB, IBN, RDY")
    print("  Sectors: IT Services (2), Banking (2), Pharma (1)")
    print()
    print("=" * 70)
    print("India - Key Facts:")
    print("  - World's 5th largest economy (GDP)")
    print("  - Fastest-growing major economy (~7% annual growth)")
    print("  - 1.4 billion population (world's most populous)")
    print("  - Global IT services hub (Bangalore = Silicon Valley of India)")
    print("  - Digital payments leader (UPI)")
    print("  - Manufacturing growth (PLI schemes)")
    print("=" * 70)

    return True

if __name__ == '__main__':
    success = add_india_page()
    sys.exit(0 if success else 1)
