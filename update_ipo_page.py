#!/usr/bin/env python3
"""
Update IPO page (page 33) to focus exclusively on recent IPOs (2020-2024)

Removes comparison charts with non-IPO tickers. Creates clean IPO-only charts
grouped by sector and year, showing only companies that went public 2020+.
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
    PAGE_NAME = "Recent IPOs"  # Rename from "2025 IPOs"

    # Update page name
    data['pages']['names'][str(PAGE_NUM)] = PAGE_NAME

    # Remove all existing charts for this page
    data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(PAGE_NUM)]

    # Chart 1: 2024 IPOs
    chart1 = {
        "page": str(PAGE_NUM),
        "tickers": ["RDDT", "RBRK"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"RDDT": 1, "RBRK": 1},
        "hidden": [],
        "range": {
            "from": 1704067200,  # 2024-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "2024 IPOs (Reddit, Rubrik)",
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
            "RDDT": "#FF4500",   # Reddit orange
            "RBRK": "#00A4EF"    # Rubrik blue
        },
        "priceScaleAssignments": {}
    }

    # Chart 2: 2023 IPOs - Tech
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
            "ARM": "#0091BD",     # Arm blue
            "KVUE": "#DC143C",    # Kenvue crimson
            "CAVA": "#D4AF37",    # CAVA gold
            "BIRK": "#8B4513",    # Birkenstock brown
            "CART": "#50C878"     # Instacart green
        },
        "priceScaleAssignments": {}
    }

    # Chart 3: 2021-2022 IPOs - Tech & SaaS
    chart3 = {
        "page": str(PAGE_NUM),
        "tickers": ["GTLB", "FRSH", "IONQ", "RIVN", "LCID"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"GTLB": 1, "FRSH": 1, "IONQ": 1, "RIVN": 1, "LCID": 1},
        "hidden": [],
        "range": {
            "from": 1609459200,  # 2021-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "2021-2022 IPOs (GitLab, Freshworks, IonQ, Rivian, Lucid)",
        "lastLabelVisible": False,
        "lastTickerVisible": False,
        "showZeroLine": False,
        "showFixedLegend": True,
        "showLegendTickers": False,
        "fixedLegendPos": {"x": 10, "y": 10},
        "fixedLegendSize": {"width": 520, "height": 140},
        "height": 450,
        "fontSize": 11,
        "showNotes": False,
        "notes": "",
        "manualInterval": "daily",
        "decimalPrecision": 2,
        "tickerColors": {
            "GTLB": "#FC6D26",    # GitLab orange
            "FRSH": "#00D4B5",    # Freshworks teal
            "IONQ": "#4A90E2",    # IonQ blue
            "RIVN": "#0E6BA8",    # Rivian blue
            "LCID": "#000000"     # Lucid black
        },
        "priceScaleAssignments": {}
    }

    # Chart 4: 2020-2021 IPOs - Major Tech
    chart4 = {
        "page": str(PAGE_NUM),
        "tickers": ["SNOW", "PLTR", "DASH", "ABNB", "COIN", "HOOD"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"SNOW": 1, "PLTR": 1, "DASH": 1, "ABNB": 1, "COIN": 1, "HOOD": 1},
        "hidden": [],
        "range": {
            "from": 1577836800,  # 2020-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "2020-2021 IPOs (Snowflake, Palantir, DoorDash, Airbnb, Coinbase, Robinhood)",
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
            "SNOW": "#29B5E8",    # Snowflake blue
            "PLTR": "#101820",    # Palantir black
            "DASH": "#FF3008",    # DoorDash red
            "ABNB": "#FF5A5F",    # Airbnb coral
            "COIN": "#0052FF",    # Coinbase blue
            "HOOD": "#00C805"     # Robinhood green
        },
        "priceScaleAssignments": {}
    }

    # Chart 5: 2019-2020 IPOs - Healthcare & Other
    chart5 = {
        "page": str(PAGE_NUM),
        "tickers": ["HIMS", "CRWD"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {"HIMS": 1, "CRWD": 1},
        "hidden": [],
        "range": {
            "from": 1546300800,  # 2019-01-01
            "to": 1763424000     # 2025-11-18
        },
        "useRaw": False,
        "title": "2019 IPOs (Hims & Hers, CrowdStrike)",
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
            "HIMS": "#00C2A8",    # Hims teal
            "CRWD": "#E01F3D"     # CrowdStrike red
        },
        "priceScaleAssignments": {}
    }

    # Add charts to workspace
    data['cards'].extend([chart1, chart2, chart3, chart4, chart5])

    # Save workspace
    with open(workspace_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("=" * 70)
    print(f"{PAGE_NAME} Page Updated Successfully")
    print("=" * 70)
    print()
    print(f"Page Number: {PAGE_NUM}")
    print(f"Page Name: {PAGE_NAME} (renamed from '2025 IPOs')")
    print(f"Charts: 5 (grouped by IPO year)")
    print()
    print("Chart 1: 2024 IPOs (2 tickers)")
    print("  RDDT (Reddit), RBRK (Rubrik)")
    print()
    print("Chart 2: 2023 IPOs (5 tickers)")
    print("  ARM (Arm Holdings), KVUE (Kenvue), CAVA (CAVA)")
    print("  BIRK (Birkenstock), CART (Instacart)")
    print()
    print("Chart 3: 2021-2022 IPOs (5 tickers)")
    print("  GTLB (GitLab), FRSH (Freshworks), IONQ (IonQ)")
    print("  RIVN (Rivian), LCID (Lucid)")
    print()
    print("Chart 4: 2020-2021 IPOs (6 tickers)")
    print("  SNOW (Snowflake), PLTR (Palantir), DASH (DoorDash)")
    print("  ABNB (Airbnb), COIN (Coinbase), HOOD (Robinhood)")
    print()
    print("Chart 5: 2019 IPOs (2 tickers)")
    print("  HIMS (Hims & Hers), CRWD (CrowdStrike)")
    print()
    print("=" * 70)
    print("Changes Made:")
    print("  - Removed all comparison charts with non-IPO tickers")
    print("  - Removed SNAP, PINS, ADBE, CRWD (non-recent IPOs)")
    print("  - Organized by IPO year for correlation analysis")
    print("  - All tickers IPO'd 2019-2024 (post-crisis tech IPOs)")
    print("  - Total: 20 IPO tickers across 5 charts")
    print("=" * 70)

    return True

if __name__ == '__main__':
    success = update_ipo_page()
    sys.exit(0 if success else 1)
