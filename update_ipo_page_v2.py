#!/usr/bin/env python3
"""
Update IPO page (page 33) - Version 2 with additional IPOs

Adds newly discovered 2020-2024 IPOs to the Recent IPOs page.
"""

import json
import sys
from pathlib import Path

def update_ipo_page():
    workspace_path = Path('charting_app/workspace.json')

    if not workspace_path.exists():
        print(f"Error: {workspace_path} not found")
        return False

    # Load workspace
    with open(workspace_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Configuration
    PAGE_NUM = 33
    PAGE_NAME = "Recent IPOs"

    # Update page name
    data['pages']['names'][str(PAGE_NUM)] = PAGE_NAME

    # Remove all existing charts for this page
    data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(PAGE_NUM)]

    # Chart 1: 2024 IPOs
    chart1 = {
        "page": str(PAGE_NUM),
        "tickers": ["RDDT", "RBRK", "GEV"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"RDDT": 1, "RBRK": 1, "GEV": 1},
        "hidden": [],
        "range": {
            "from": 1704067200,  # 2024-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "2024 IPOs (Reddit, Rubrik, GE Vernova)",
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
            "RDDT": "#FF4500",   # Reddit orange
            "RBRK": "#00A4EF",   # Rubrik blue
            "GEV": "#005EB8"     # GE blue
        },
        "priceScaleAssignments": {}
    }

    # Chart 2: 2023 IPOs
    chart2 = {
        "page": str(PAGE_NUM),
        "tickers": ["ARM", "KVUE", "CAVA", "BIRK", "CART"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"ARM": 1, "KVUE": 1, "CAVA": 1, "BIRK": 1, "CART": 1},
        "hidden": [],
        "range": {
            "from": 1672531200,  # 2023-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "2023 IPOs (Arm, Kenvue, CAVA, Birkenstock, Instacart)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 500, "height": 140},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "ARM": "#0091BD",
            "KVUE": "#DC143C",
            "CAVA": "#D4AF37",
            "BIRK": "#8B4513",
            "CART": "#50C878"
        },
        "priceScaleAssignments": {}
    }

    # Chart 3: 2022 IPOs
    chart3 = {
        "page": str(PAGE_NUM),
        "tickers": ["TPG"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"TPG": 1},
        "hidden": [],
        "range": {
            "from": 1640995200,  # 2022-01-01
            "to": 1763424000
        },
        "useRaw": False,
        "title": "2022 IPOs (TPG Capital)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 400, "height": 80},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "TPG": "#1E3A8A"
        },
        "priceScaleAssignments": {}
    }

    # Chart 4: 2021 IPOs - Tech/SaaS
    chart4 = {
        "page": str(PAGE_NUM),
        "tickers": ["GTLB", "FRSH", "BRZE", "TOST", "SRAD", "WEAV"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"GTLB": 1, "FRSH": 1, "BRZE": 1, "TOST": 1, "SRAD": 1, "WEAV": 1},
        "hidden": [],
        "range": {
            "from": 1609459200,  # 2021-01-01
            "to": 1763424000
        },
        "useRaw": False,
        "title": "2021 IPOs - Tech/SaaS (GitLab, Freshworks, Braze, Toast, Sportradar, Weave)",
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
            "GTLB": "#FC6D26",
            "FRSH": "#00D4B5",
            "BRZE": "#6B46C1",
            "TOST": "#E85D04",
            "SRAD": "#0EA5E9",
            "WEAV": "#059669"
        },
        "priceScaleAssignments": {}
    }

    # Chart 5: 2021 IPOs - Other (EVs, Biotech, Other)
    chart5 = {
        "page": str(PAGE_NUM),
        "tickers": ["IONQ", "RIVN", "LCID", "RXRX", "OCS"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"IONQ": 1, "RIVN": 1, "LCID": 1, "RXRX": 1, "OCS": 1},
        "hidden": [],
        "range": {
            "from": 1609459200,  # 2021-01-01
            "to": 1763424000
        },
        "useRaw": False,
        "title": "2021 IPOs - Other (IonQ, Rivian, Lucid, Recursion, Oculis)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 540, "height": 140},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "IONQ": "#4A90E2",
            "RIVN": "#0E6BA8",
            "LCID": "#000000",
            "RXRX": "#7C3AED",
            "OCS": "#10B981"
        },
        "priceScaleAssignments": {}
    }

    # Chart 6: 2020-2021 IPOs - Major Tech
    chart6 = {
        "page": str(PAGE_NUM),
        "tickers": ["SNOW", "PLTR", "DASH", "ABNB", "COIN", "HOOD", "MNSO", "LEGN", "KROS"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"SNOW": 1, "PLTR": 1, "DASH": 1, "ABNB": 1, "COIN": 1, "HOOD": 1, "MNSO": 1, "LEGN": 1, "KROS": 1},
        "hidden": [],
        "range": {
            "from": 1577836800,  # 2020-01-01
            "to": 1763424000
        },
        "useRaw": False,
        "title": "2020 IPOs (Snowflake, Palantir, DoorDash, Airbnb, Coinbase, Robinhood, MINISO, Legend, Keros)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 680, "height": 200},
        "height": 500,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "SNOW": "#29B5E8",
            "PLTR": "#101820",
            "DASH": "#FF3008",
            "ABNB": "#FF5A5F",
            "COIN": "#0052FF",
            "HOOD": "#00C805",
            "MNSO": "#FF6B9D",
            "LEGN": "#A855F7",
            "KROS": "#14B8A6"
        },
        "priceScaleAssignments": {}
    }

    # Chart 7: 2019 IPOs
    chart7 = {
        "page": str(PAGE_NUM),
        "tickers": ["HIMS", "CRWD", "ASTS"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"HIMS": 1, "CRWD": 1, "ASTS": 1},
        "hidden": [],
        "range": {
            "from": 1546300800,  # 2019-01-01
            "to": 1763424000
        },
        "useRaw": False,
        "title": "2019 IPOs (Hims & Hers, CrowdStrike, AST SpaceMobile)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 480, "height": 120},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "HIMS": "#00C2A8",
            "CRWD": "#E01F3D",
            "ASTS": "#0066CC"
        },
        "priceScaleAssignments": {}
    }

    # Add charts to workspace
    data['cards'].extend([chart1, chart2, chart3, chart4, chart5, chart6, chart7])

    # Save workspace
    with open(workspace_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("=" * 70)
    print(f"{PAGE_NAME} Page Updated Successfully")
    print("=" * 70)
    print()
    print(f"Page Number: {PAGE_NUM}")
    print(f"Page Name: {PAGE_NAME}")
    print(f"Charts: 7 (grouped by IPO year)")
    print()
    print("Chart 1: 2024 IPOs (3 tickers)")
    print("  RDDT, RBRK, GEV")
    print()
    print("Chart 2: 2023 IPOs (5 tickers)")
    print("  ARM, KVUE, CAVA, BIRK, CART")
    print()
    print("Chart 3: 2022 IPOs (1 ticker)")
    print("  TPG")
    print()
    print("Chart 4: 2021 IPOs - Tech/SaaS (6 tickers)")
    print("  GTLB, FRSH, BRZE, TOST, SRAD, WEAV")
    print()
    print("Chart 5: 2021 IPOs - Other (5 tickers)")
    print("  IONQ, RIVN, LCID, RXRX, OCS")
    print()
    print("Chart 6: 2020 IPOs (9 tickers)")
    print("  SNOW, PLTR, DASH, ABNB, COIN, HOOD, MNSO, LEGN, KROS")
    print()
    print("Chart 7: 2019 IPOs (3 tickers)")
    print("  HIMS, CRWD, ASTS")
    print()
    print("=" * 70)
    print(f"Total: 32 IPO tickers (up from 20)")
    print("New additions: GEV, TPG, BRZE, TOST, SRAD, WEAV, RXRX, OCS,")
    print("               MNSO, LEGN, KROS, ASTS")
    print("=" * 70)

    return True

if __name__ == '__main__':
    success = update_ipo_page()
    sys.exit(0 if success else 1)
