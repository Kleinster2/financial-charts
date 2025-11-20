#!/usr/bin/env python3
"""
Update Japan page (46) with Bond Rout Tracking Charts

Tracks the JGB rout through:
- International bond ETFs (falling prices = rising yields)
- US yields for comparison
- Currency weakness (JPY=X)
- Japanese equity impact
"""

import json
import sys
from pathlib import Path

def update_japan_page():
    workspace_path = Path('charting_app/workspace.json')

    if not workspace_path.exists():
        print(f"Error: {workspace_path} not found")
        return False

    # Load workspace
    with open(workspace_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Configuration
    PAGE_NUM = 46
    PAGE_NAME = "Japan - Bond Rout"

    # Update page name
    data['pages']['names'][str(PAGE_NUM)] = PAGE_NAME

    # Remove existing charts for this page
    data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(PAGE_NUM)]

    # Chart 1: International Bond ETFs (Japan included - falling = yields rising)
    chart1 = {
        "page": str(PAGE_NUM),
        "tickers": ["JPGB", "IGOV", "BWX", "ISHG"],
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
            "from": 1704067200,  # 2024-01-01 (capture recent rout)
            "to": 1763424000     # 2025-11-20
        },
        "useRaw": False,
        "title": "Japan Bond Rout - Bond ETFs Falling (JPGB, Int'l Treasury ETFs)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 600, "height": 120},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "JPGB": "#E01F3D",    # Red (Japan bond - falling = rout)
            "IGOV": "#FF9933",    # Orange (Int'l Treasury ETF)
            "BWX": "#4A90E2",     # Blue (SPDR Int'l Treasury)
            "ISHG": "#00C805"     # Green (1-3Y Int'l Treasury)
        },
        "priceScaleAssignments": {}
    }

    # Chart 2: US Yields for Comparison (rising = bond sell-off)
    chart2 = {
        "page": str(PAGE_NUM),
        "tickers": ["^TNX", "^TYX"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"^TNX": 1, "^TYX": 1},
        "hidden": [],
        "range": {
            "from": 1704067200,  # 2024-01-01
            "to": 1763424000     # 2025-11-20
        },
        "useRaw": False,
        "title": "US Treasury Yields (10Y, 30Y) - For Comparison",
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
            "^TNX": "#4A90E2",    # Blue (10Y)
            "^TYX": "#E01F3D"     # Red (30Y)
        },
        "priceScaleAssignments": {}
    }

    # Chart 3: JPY Weakness (currency stress from bond sell-off)
    chart3 = {
        "page": str(PAGE_NUM),
        "tickers": ["JPY=X", "FXY", "YCS"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"JPY=X": 1, "FXY": 1, "YCS": 1},
        "hidden": [],
        "range": {
            "from": 1704067200,  # 2024-01-01
            "to": 1763424000     # 2025-11-20
        },
        "useRaw": False,
        "title": "JPY Weakness from Bond Stress (USD/JPY rising, Yen ETF falling, Short Yen rising)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 620, "height": 120},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "JPY=X": "#E01F3D",    # Red (rising = yen weakening)
            "FXY": "#00C805",      # Green (falling = yen weakening)
            "YCS": "#FF9933"       # Orange (2x short yen - bet on weakness)
        },
        "priceScaleAssignments": {}
    }

    # Chart 4: Japan Equities (impact of bond rout)
    chart4 = {
        "page": str(PAGE_NUM),
        "tickers": ["EWJ", "^N225", "TM", "SONY", "MUFG", "NMR"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"EWJ": 1, "^N225": 1, "TM": 1, "SONY": 1, "MUFG": 1, "NMR": 1},
        "hidden": [],
        "range": {
            "from": 1704067200,  # 2024-01-01
            "to": 1763424000     # 2025-11-20
        },
        "useRaw": False,
        "title": "Japan Equities - Impact of Bond Rout (ETF, Nikkei, Exporters, Banks)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 640, "height": 140},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "EWJ": "#BC002D",      # Red (Japan ETF)
            "^N225": "#FF6B6B",    # Light red (Nikkei)
            "TM": "#4A90E2",       # Blue (Toyota - exporter benefits from weak yen)
            "SONY": "#9370DB",     # Purple (Sony - exporter)
            "MUFG": "#FFD700",     # Gold (Bank - stressed by bond rout)
            "NMR": "#DC143C"       # Crimson (Nomura - financial stress)
        },
        "priceScaleAssignments": {}
    }

    # Add charts to workspace
    data['cards'].extend([chart1, chart2, chart3, chart4])

    # Save workspace
    with open(workspace_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("=" * 70)
    print(f"{PAGE_NAME} Page Updated Successfully")
    print("=" * 70)
    print()
    print(f"Page Number: {PAGE_NUM}")
    print(f"Page Name: {PAGE_NAME}")
    print(f"Charts Added: 4")
    print()
    print("Chart 1: Bond ETFs Falling (Yields Rising)")
    print("  Tickers: JPGB, IGOV, BWX, ISHG")
    print("  Key: Falling prices = Rising yields = Bond rout")
    print()
    print("Chart 2: US Treasury Yields")
    print("  Tickers: ^TNX (10Y), ^TYX (30Y)")
    print("  Key: Compare US vs Japan - is this Japan-specific?")
    print()
    print("Chart 3: JPY Weakness")
    print("  Tickers: JPY=X, FXY, YCS")
    print("  Key: Bond stress causes currency weakness")
    print()
    print("Chart 4: Japan Equities")
    print("  Tickers: EWJ, ^N225, TM, SONY, MUFG, NMR")
    print("  Key: Exporters benefit, banks/financials stressed")
    print()
    print("=" * 70)
    print("JGB Rout Mechanics:")
    print("  1. Bond ETFs fall (JPGB, IGOV, BWX, ISHG down)")
    print("  2. Yields rise (inverse relationship)")
    print("  3. JPY weakens (JPY=X rises, FXY falls)")
    print("  4. Exporters benefit (TM, SONY up from weak yen)")
    print("  5. Banks stressed (MUFG, NMR - hold JGBs, mark-to-market losses)")
    print("=" * 70)

    return True

if __name__ == '__main__':
    success = update_japan_page()
    sys.exit(0 if success else 1)
