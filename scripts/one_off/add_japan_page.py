#!/usr/bin/env python3
"""
Add Japan page to workspace.json

Creates page 46 with Japanese market ETFs and major Japanese companies (ADRs).

Japan: World's 3rd largest economy, technology and automotive leader,
aging population, major exporter.
"""

import json
import sys
from pathlib import Path

def add_japan_page():
    workspace_path = Path('charting_app/workspace.json')

    if not workspace_path.exists():
        print(f"Error: {workspace_path} not found")
        return False

    # Load workspace
    with open(workspace_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Configuration
    PAGE_NUM = 46
    PAGE_NAME = "Japan"

    # Add page to pages list
    if PAGE_NUM not in data['pages']['pages']:
        data['pages']['pages'].append(PAGE_NUM)
        data['pages']['pages'].sort()

    # Add page name
    data['pages']['names'][str(PAGE_NUM)] = PAGE_NAME

    # Remove any existing charts for this page
    data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(PAGE_NUM)]

    # Chart 1: Japan Market ETFs
    chart1 = {
        "page": str(PAGE_NUM),
        "tickers": ["EWJ", "DXJ", "JPXN", "DBJP"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {
            "EWJ": 1,
            "DXJ": 1,
            "JPXN": 1,
            "DBJP": 1
        },
        "hidden": [],
        "range": {
            "from": 1262304000,  # 2010-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "Japan Market ETFs (iShares MSCI, WisdomTree Hedged, JPX-Nikkei 400, Xtrackers)",
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
            "EWJ": "#BC002D",     # Japanese flag red
            "DXJ": "#FF6B6B",     # Light red
            "JPXN": "#DC143C",    # Crimson
            "DBJP": "#B22222"     # Fire brick
        },
        "priceScaleAssignments": {}
    }

    # Chart 2: Japanese Blue Chips (Automotive, Tech, Finance)
    chart2 = {
        "page": str(PAGE_NUM),
        "tickers": ["TM", "HMC", "SONY", "NMR", "MUFG"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {
            "TM": 1,
            "HMC": 1,
            "SONY": 1,
            "NMR": 1,
            "MUFG": 1
        },
        "hidden": [],
        "range": {
            "from": 1262304000,  # 2010-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "Japanese Blue Chips (Toyota, Honda, Sony, Nomura, MUFG)",
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
            "TM": "#BC002D",      # Red (Toyota)
            "HMC": "#4A90E2",     # Blue (Honda)
            "SONY": "#000000",    # Black (Sony)
            "NMR": "#FFD700",     # Gold (Nomura)
            "MUFG": "#DC143C"     # Crimson (MUFG)
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
    print("Chart 1: Japan Market ETFs")
    print("  Tickers: EWJ, DXJ, JPXN, DBJP")
    print("  Focus: MSCI Japan, Hedged, JPX-Nikkei 400")
    print()
    print("Chart 2: Japanese Blue Chips")
    print("  Tickers: TM, HMC, SONY, NMR, MUFG")
    print("  Sectors: Automotive (2), Tech (1), Finance (2)")
    print()
    print("=" * 70)
    print("Japan - Key Facts:")
    print("  - World's 3rd largest economy (GDP)")
    print("  - Major technology exporter (electronics, robotics)")
    print("  - Automotive leader (Toyota, Honda, Nissan)")
    print("  - Aging population (28% over 65)")
    print("  - Tokyo Stock Exchange - 3rd largest by market cap")
    print("  - Innovation hub (AI, robotics, semiconductors)")
    print("=" * 70)

    return True

if __name__ == '__main__':
    success = add_japan_page()
    sys.exit(0 if success else 1)
