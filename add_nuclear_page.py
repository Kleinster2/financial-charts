#!/usr/bin/env python3
"""
Add Nuclear Energy page to workspace.json

Creates page 47 with dedicated nuclear energy focus, separating traditional
uranium miners from next-generation nuclear technology companies.

Nuclear Renaissance: AI data centers, climate goals, energy security driving
renewed interest in nuclear power and small modular reactors (SMRs).
"""

import json
import sys
from pathlib import Path

def add_nuclear_page():
    workspace_path = Path('charting_app/workspace.json')

    if not workspace_path.exists():
        print(f"Error: {workspace_path} not found")
        return False

    # Load workspace
    with open(workspace_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Configuration
    PAGE_NUM = 47
    PAGE_NAME = "Nuclear Energy"

    # Add page to pages list
    if PAGE_NUM not in data['pages']['pages']:
        data['pages']['pages'].append(PAGE_NUM)
        data['pages']['pages'].sort()

    # Add page name
    data['pages']['names'][str(PAGE_NUM)] = PAGE_NAME

    # Remove any existing charts for this page
    data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(PAGE_NUM)]

    # Chart 1: Uranium Miners & ETF
    chart1 = {
        "page": str(PAGE_NUM),
        "tickers": ["URA", "CCJ", "DNN", "UEC", "UUUU", "UROY"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {
            "URA": 1,
            "CCJ": 1,
            "DNN": 1,
            "UEC": 1,
            "UUUU": 1,
            "UROY": 1
        },
        "hidden": [],
        "range": {
            "from": 1420070400,  # 2015-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "Uranium Miners (Global X ETF, Cameco, Denison, Energy Fuels, Uranium Royalty)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 600, "height": 140},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "URA": "#FFD700",     # Gold (ETF)
            "CCJ": "#00A86B",     # Jade green (Cameco - largest)
            "DNN": "#4169E1",     # Royal blue
            "UEC": "#FF6347",     # Tomato red
            "UUUU": "#9370DB",    # Medium purple
            "UROY": "#FF8C00"     # Dark orange
        },
        "priceScaleAssignments": {}
    }

    # Chart 2: Next-Gen Nuclear Technology (SMRs & Advanced Reactors)
    chart2 = {
        "page": str(PAGE_NUM),
        "tickers": ["SMR", "OKLO", "NNE", "LEU"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {
            "SMR": 1,
            "OKLO": 1,
            "NNE": 1,
            "LEU": 1
        },
        "hidden": [],
        "range": {
            "from": 1640995200,  # 2022-01-01 (newer companies)
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "Next-Gen Nuclear Tech (NuScale SMR, Oklo, NANO Nuclear, Centrus)",
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
            "SMR": "#00CED1",     # Dark turquoise (NuScale)
            "OKLO": "#32CD32",    # Lime green (Oklo)
            "NNE": "#FF1493",     # Deep pink (NANO Nuclear)
            "LEU": "#FF4500"      # Orange red (Centrus)
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
    print("Chart 1: Uranium Miners & ETF")
    print("  Tickers: URA, CCJ, DNN, UEC, UUUU, UROY")
    print("  Focus: Commodity-driven uranium producers")
    print("  Correlation: Spot uranium prices, mining costs")
    print()
    print("Chart 2: Next-Gen Nuclear Technology")
    print("  Tickers: SMR, OKLO, NNE, LEU")
    print("  Focus: Small Modular Reactors (SMRs), advanced fission")
    print("  Correlation: Tech innovation, AI data center power demand")
    print()
    print("=" * 70)
    print("Nuclear Energy - Key Drivers:")
    print("  - AI/data center power demand (24/7 clean baseload)")
    print("  - Climate goals (zero-emission baseload power)")
    print("  - Energy security (domestic fuel supply)")
    print("  - SMR technology (safer, scalable, factory-built)")
    print("  - Uranium supply deficit (production < demand)")
    print("  - Policy support (US, EU, Asia nuclear expansion)")
    print()
    print("Correlation Separation:")
    print("  - Miners: Follow uranium spot price (~$80/lb)")
    print("  - Tech: Follow growth/innovation narrative (like AI stocks)")
    print("=" * 70)

    return True

if __name__ == '__main__':
    success = add_nuclear_page()
    sys.exit(0 if success else 1)
