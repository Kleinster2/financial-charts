#!/usr/bin/env python3
"""
Expanded Japan Bond Rout Tracking - Version 2
Page 46: Comprehensive tracking across 8 dimensions
"""

import json
import sys
from pathlib import Path

def update_japan_page():
    workspace_path = Path('charting_app/workspace.json')

    if not workspace_path.exists():
        print(f"Error: {workspace_path} not found")
        return False

    with open(workspace_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    PAGE_NUM = 46
    PAGE_NAME = "Japan - Bond Rout"

    data['pages']['names'][str(PAGE_NUM)] = PAGE_NAME
    data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(PAGE_NUM)]

    # Chart 1: Bond ETFs Falling (Primary Indicator)
    chart1 = {
        "page": str(PAGE_NUM),
        "tickers": ["JPGB", "IGOV", "BWX", "ISHG"],
        "showDiff": False, "showAvg": False, "showVol": False, "showVolume": False,
        "showRevenue": False, "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"JPGB": 1, "IGOV": 1, "BWX": 1, "ISHG": 1},
        "hidden": [],
        "range": {"from": 1704067200, "to": 1763424000},
        "useRaw": False,
        "title": "1. Bond Rout - Prices Falling (JPGB, Int'l Treasury ETFs)",
        "lastLabelVisible": False, "lastTickerVisible": False, "showZeroLine": False,
        "showFixedLegend": True, "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 600, "height": 120},
        "height": 450, "fontSize": 11, "showNotes": False, "notes": "",
        "manualInterval": "daily", "decimalPrecision": 2,
        "tickerColors": {
            "JPGB": "#E01F3D", "IGOV": "#FF9933",
            "BWX": "#4A90E2", "ISHG": "#00C805"
        },
        "priceScaleAssignments": {}
    }

    # Chart 2: Inverse Bond ETFs (Traders Profiting from Rout)
    chart2 = {
        "page": str(PAGE_NUM),
        "tickers": ["TBT", "TBF", "PST"],
        "showDiff": False, "showAvg": False, "showVol": False, "showVolume": False,
        "showRevenue": False, "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"TBT": 1, "TBF": 1, "PST": 1},
        "hidden": [],
        "range": {"from": 1704067200, "to": 1763424000},
        "useRaw": False,
        "title": "2. Inverse Bond ETFs Rising (Traders profiting: TBT 2x, TBF, PST 2x)",
        "lastLabelVisible": False, "lastTickerVisible": False, "showZeroLine": False,
        "showFixedLegend": True, "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 600, "height": 120},
        "height": 450, "fontSize": 11, "showNotes": False, "notes": "",
        "manualInterval": "daily", "decimalPrecision": 2,
        "tickerColors": {
            "TBT": "#E01F3D",    # Red (2x inverse 20Y)
            "TBF": "#FF9933",    # Orange (1x inverse 20Y)
            "PST": "#9D4EDD"     # Purple (2x inverse 7-10Y)
        },
        "priceScaleAssignments": {}
    }

    # Chart 3: US Yields (Comparison - Global or Japan-specific?)
    chart3 = {
        "page": str(PAGE_NUM),
        "tickers": ["^TNX", "^TYX", "TLT", "IEF"],
        "showDiff": False, "showAvg": False, "showVol": False, "showVolume": False,
        "showRevenue": False, "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"^TNX": 1, "^TYX": 1, "TLT": 1, "IEF": 1},
        "hidden": [],
        "range": {"from": 1704067200, "to": 1763424000},
        "useRaw": False,
        "title": "3. US Treasuries (Yields rising, Bonds falling - Global stress or Japan only?)",
        "lastLabelVisible": False, "lastTickerVisible": False, "showZeroLine": False,
        "showFixedLegend": True, "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 560, "height": 120},
        "height": 450, "fontSize": 11, "showNotes": False, "notes": "",
        "manualInterval": "daily", "decimalPrecision": 2,
        "tickerColors": {
            "^TNX": "#4A90E2",    # Blue (10Y yield)
            "^TYX": "#E01F3D",    # Red (30Y yield)
            "TLT": "#FF9933",     # Orange (20Y bond ETF)
            "IEF": "#00C805"      # Green (7-10Y bond ETF)
        },
        "priceScaleAssignments": {}
    }

    # Chart 4: JPY Weakness (Currency Stress)
    chart4 = {
        "page": str(PAGE_NUM),
        "tickers": ["JPY=X", "USDJPY=X", "FXY", "YCS"],
        "showDiff": False, "showAvg": False, "showVol": False, "showVolume": False,
        "showRevenue": False, "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"JPY=X": 1, "USDJPY=X": 1, "FXY": 1, "YCS": 1},
        "hidden": [],
        "range": {"from": 1704067200, "to": 1763424000},
        "useRaw": False,
        "title": "4. JPY Weakness (USD/JPY rising, Yen ETF falling, Short Yen rising)",
        "lastLabelVisible": False, "lastTickerVisible": False, "showZeroLine": False,
        "showFixedLegend": True, "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 620, "height": 120},
        "height": 450, "fontSize": 11, "showNotes": False, "notes": "",
        "manualInterval": "daily", "decimalPrecision": 2,
        "tickerColors": {
            "JPY=X": "#E01F3D",       # Red
            "USDJPY=X": "#DC143C",    # Crimson
            "FXY": "#00C805",         # Green
            "YCS": "#FF9933"          # Orange
        },
        "priceScaleAssignments": {}
    }

    # Chart 5: Asian Contagion Risk
    chart5 = {
        "page": str(PAGE_NUM),
        "tickers": ["AAXJ", "AIA", "BBAX", "CNY=X", "KRW=X"],
        "showDiff": False, "showAvg": False, "showVol": False, "showVolume": False,
        "showRevenue": False, "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"AAXJ": 1, "AIA": 1, "BBAX": 1, "CNY=X": 1, "KRW=X": 1},
        "hidden": [],
        "range": {"from": 1704067200, "to": 1763424000},
        "useRaw": False,
        "title": "5. Asian Contagion Risk (Asia ex-Japan stocks, China/Korea currency stress)",
        "lastLabelVisible": False, "lastTickerVisible": False, "showZeroLine": False,
        "showFixedLegend": True, "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 660, "height": 140},
        "height": 450, "fontSize": 11, "showNotes": False, "notes": "",
        "manualInterval": "daily", "decimalPrecision": 2,
        "tickerColors": {
            "AAXJ": "#E01F3D",     # Red (Asia ex-Japan)
            "AIA": "#FF9933",      # Orange (Asia 50)
            "BBAX": "#9D4EDD",     # Purple (Asia Pacific ex-Japan)
            "CNY=X": "#4A90E2",    # Blue (USD/CNY)
            "KRW=X": "#00C805"     # Green (USD/KRW)
        },
        "priceScaleAssignments": {}
    }

    # Chart 6: Safe Haven Flows
    chart6 = {
        "page": str(PAGE_NUM),
        "tickers": ["GLD", "^VIX", "VXX"],
        "showDiff": False, "showAvg": False, "showVol": False, "showVolume": False,
        "showRevenue": False, "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"GLD": 1, "^VIX": 1, "VXX": 1},
        "hidden": [],
        "range": {"from": 1704067200, "to": 1763424000},
        "useRaw": False,
        "title": "6. Safe Haven & Risk (Gold rising, VIX spiking = Fear)",
        "lastLabelVisible": False, "lastTickerVisible": False, "showZeroLine": False,
        "showFixedLegend": True, "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 560, "height": 120},
        "height": 450, "fontSize": 11, "showNotes": False, "notes": "",
        "manualInterval": "daily", "decimalPrecision": 2,
        "tickerColors": {
            "GLD": "#FFD700",      # Gold
            "^VIX": "#E01F3D",     # Red (fear gauge)
            "VXX": "#DC143C"       # Crimson (VIX ETF)
        },
        "priceScaleAssignments": {}
    }

    # Chart 7: Japanese Banks - Direct Tokyo Listings (Ground Zero)
    chart7 = {
        "page": str(PAGE_NUM),
        "tickers": ["8306.T", "8604.T", "8316.T", "MUFG", "NMR"],
        "showDiff": False, "showAvg": False, "showVol": False, "showVolume": False,
        "showRevenue": False, "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"8306.T": 1, "8604.T": 1, "8316.T": 1, "MUFG": 1, "NMR": 1},
        "hidden": [],
        "range": {"from": 1704067200, "to": 1763424000},
        "useRaw": False,
        "title": "7. Japanese Banks - Ground Zero (Tokyo: MUFG, Nomura, SMFG + ADRs)",
        "lastLabelVisible": False, "lastTickerVisible": False, "showZeroLine": False,
        "showFixedLegend": True, "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 640, "height": 140},
        "height": 450, "fontSize": 11, "showNotes": False, "notes": "",
        "manualInterval": "daily", "decimalPrecision": 2,
        "tickerColors": {
            "8306.T": "#E01F3D",    # Red (MUFG Tokyo)
            "8604.T": "#DC143C",    # Crimson (Nomura Tokyo)
            "8316.T": "#B22222",    # Fire brick (SMFG Tokyo)
            "MUFG": "#FFD700",      # Gold (MUFG ADR)
            "NMR": "#FF9933"        # Orange (Nomura ADR)
        },
        "priceScaleAssignments": {}
    }

    # Chart 8: Japan Equities (Exporters vs Overall Market)
    chart8 = {
        "page": str(PAGE_NUM),
        "tickers": ["EWJ", "^N225", "TM", "SONY", "HMC"],
        "showDiff": False, "showAvg": False, "showVol": False, "showVolume": False,
        "showRevenue": False, "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"EWJ": 1, "^N225": 1, "TM": 1, "SONY": 1, "HMC": 1},
        "hidden": [],
        "range": {"from": 1704067200, "to": 1763424000},
        "useRaw": False,
        "title": "8. Japan Equities (ETF, Nikkei, Exporters benefit from weak yen)",
        "lastLabelVisible": False, "lastTickerVisible": False, "showZeroLine": False,
        "showFixedLegend": True, "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 640, "height": 140},
        "height": 450, "fontSize": 11, "showNotes": False, "notes": "",
        "manualInterval": "daily", "decimalPrecision": 2,
        "tickerColors": {
            "EWJ": "#BC002D",      # Red (Japan ETF)
            "^N225": "#FF6B6B",    # Light red (Nikkei)
            "TM": "#4A90E2",       # Blue (Toyota)
            "SONY": "#9370DB",     # Purple (Sony)
            "HMC": "#00C805"       # Green (Honda)
        },
        "priceScaleAssignments": {}
    }

    data['cards'].extend([chart1, chart2, chart3, chart4, chart5, chart6, chart7, chart8])

    with open(workspace_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("=" * 70)
    print(f"{PAGE_NAME} Page Updated - EXPANDED VERSION")
    print("=" * 70)
    print(f"\nPage {PAGE_NUM}: {PAGE_NAME} - Now with 8 comprehensive charts:\n")
    print("1. Bond Rout - Prices Falling (JPGB, IGOV, BWX, ISHG)")
    print("2. Inverse Bond ETFs Rising (TBT, TBF, PST - traders profiting)")
    print("3. US Treasuries (Compare: Global or Japan-specific?)")
    print("4. JPY Weakness (Currency stress from bond sales)")
    print("5. Asian Contagion Risk (Regional spillover to Asia)")
    print("6. Safe Haven & Risk (Gold, VIX - fear indicators)")
    print("7. Japanese Banks - Ground Zero (Tokyo listings + ADRs)")
    print("8. Japan Equities (Exporters benefit, market impact)")
    print("\n" + "=" * 70)
    print("Total tickers tracked: 31 across 8 dimensions")
    print("=" * 70)

    return True

if __name__ == '__main__':
    success = update_japan_page()
    sys.exit(0 if success else 1)
