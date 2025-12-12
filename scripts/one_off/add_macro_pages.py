#!/usr/bin/env python3
"""
Add FRED macro indicator pages to workspace.json

Creates 5 pages (49-53) with economic indicators:
- Page 49: Macro Dashboard (yields, Fed policy, inflation, credit)
- Page 50: Labor Market (unemployment, payrolls, participation)
- Page 51: Economic Activity (GDP, sentiment, retail sales)
- Page 52: Fed Policy & Liquidity (balance sheet, reverse repo, rates)
- Page 53: Financial Stress & Risk (stress index, credit spreads, VIX)
"""

import json
import sys
from pathlib import Path

def add_macro_pages():
    workspace_path = Path('charting_app/workspace.json')

    if not workspace_path.exists():
        print(f"Error: {workspace_path} not found")
        return False

    # Load workspace
    with open(workspace_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Page definitions
    pages_config = [
        {
            'num': 49,
            'name': 'Macro Dashboard',
            'charts': [
                {
                    'title': 'Treasury Yield Curve (2Y, 10Y, 30Y)',
                    'tickers': ['DGS2', 'DGS10', 'DGS30'],
                    'colors': {
                        'DGS2': '#FF6B6B',     # Red (short-term)
                        'DGS10': '#4ECDC4',    # Teal (mid-term)
                        'DGS30': '#45B7D1'     # Blue (long-term)
                    },
                    'height': 350
                },
                {
                    'title': 'Yield Curve Spread (10Y - 2Y) - Recession Predictor',
                    'tickers': ['T10Y2Y'],
                    'colors': {'T10Y2Y': '#9B59B6'},  # Purple
                    'height': 300
                },
                {
                    'title': 'Inflation Measures (CPI, Core CPI, 5Y Breakeven)',
                    'tickers': ['CPIAUCSL', 'CPILFESL', 'T5YIE'],
                    'colors': {
                        'CPIAUCSL': '#E74C3C',    # Red (headline CPI)
                        'CPILFESL': '#F39C12',    # Orange (core CPI)
                        'T5YIE': '#3498DB'        # Blue (expectations)
                    },
                    'height': 350
                },
                {
                    'title': 'Credit Spreads (High Yield & Corporate)',
                    'tickers': ['BAMLH0A0HYM2', 'BAMLC0A0CM'],
                    'colors': {
                        'BAMLH0A0HYM2': '#E67E22',  # Dark orange (HY)
                        'BAMLC0A0CM': '#16A085'      # Teal (IG)
                    },
                    'height': 350
                }
            ]
        },
        {
            'num': 50,
            'name': 'Labor Market',
            'charts': [
                {
                    'title': 'Unemployment Rates (U3 & U6)',
                    'tickers': ['UNRATE', 'U6RATE'],
                    'colors': {
                        'UNRATE': '#E74C3C',      # Red (U3 - headline)
                        'U6RATE': '#9B59B6'       # Purple (U6 - underemployment)
                    },
                    'height': 400
                },
                {
                    'title': 'Nonfarm Payrolls (Thousands)',
                    'tickers': ['PAYEMS'],
                    'colors': {'PAYEMS': '#27AE60'},  # Green
                    'height': 400
                },
                {
                    'title': 'Labor Force Participation Rate',
                    'tickers': ['CIVPART'],
                    'colors': {'CIVPART': '#3498DB'},  # Blue
                    'height': 400
                }
            ]
        },
        {
            'num': 51,
            'name': 'Economic Activity',
            'charts': [
                {
                    'title': 'GDP & Real GDP',
                    'tickers': ['GDP', 'GDPC1'],
                    'colors': {
                        'GDP': '#2ECC71',         # Green (nominal)
                        'GDPC1': '#27AE60'        # Dark green (real)
                    },
                    'height': 400
                },
                {
                    'title': 'Consumer Sentiment (University of Michigan)',
                    'tickers': ['UMCSENT'],
                    'colors': {'UMCSENT': '#F39C12'},  # Orange
                    'height': 400
                },
                {
                    'title': 'Retail Sales (Millions)',
                    'tickers': ['RSXFS'],
                    'colors': {'RSXFS': '#9B59B6'},  # Purple
                    'height': 400
                }
            ]
        },
        {
            'num': 52,
            'name': 'Fed Policy',
            'charts': [
                {
                    'title': 'Federal Funds Rate (Effective & Targets)',
                    'tickers': ['FEDFUNDS', 'DFEDTARU', 'DFEDTARL'],
                    'colors': {
                        'FEDFUNDS': '#E74C3C',    # Red (effective)
                        'DFEDTARU': '#95A5A6',    # Gray (upper target)
                        'DFEDTARL': '#7F8C8D'     # Dark gray (lower target)
                    },
                    'height': 400
                },
                {
                    'title': 'Fed Balance Sheet (Trillions)',
                    'tickers': ['WALCL'],
                    'colors': {'WALCL': '#3498DB'},  # Blue
                    'height': 400
                },
                {
                    'title': 'Overnight Reverse Repo (Billions)',
                    'tickers': ['RRPONTSYD'],
                    'colors': {'RRPONTSYD': '#9B59B6'},  # Purple
                    'height': 400
                },
                {
                    'title': 'Treasury General Account (Billions)',
                    'tickers': ['WTREGEN'],
                    'colors': {'WTREGEN': '#27AE60'},  # Green
                    'height': 350
                }
            ]
        },
        {
            'num': 53,
            'name': 'Financial Stress',
            'charts': [
                {
                    'title': 'St. Louis Fed Financial Stress Index',
                    'tickers': ['STLFSI4'],
                    'colors': {'STLFSI4': '#E74C3C'},  # Red
                    'height': 400
                },
                {
                    'title': 'Credit Spreads (High Yield & Corporate)',
                    'tickers': ['BAMLH0A0HYM2', 'BAMLC0A0CM'],
                    'colors': {
                        'BAMLH0A0HYM2': '#E67E22',  # Dark orange
                        'BAMLC0A0CM': '#16A085'      # Teal
                    },
                    'height': 400
                },
                {
                    'title': 'Market Volatility (VIX) vs Financial Stress',
                    'tickers': ['^VIX', 'STLFSI4'],
                    'colors': {
                        '^VIX': '#9B59B6',        # Purple (VIX)
                        'STLFSI4': '#E74C3C'      # Red (stress)
                    },
                    'priceScaleAssignments': {
                        '^VIX': 'left',
                        'STLFSI4': 'right'
                    },
                    'height': 400
                },
                {
                    'title': 'TED Spread (LIBOR - T-Bill) [Discontinued 2022]',
                    'tickers': ['TEDRATE'],
                    'colors': {'TEDRATE': '#F39C12'},  # Orange
                    'height': 300
                }
            ]
        }
    ]

    # Add pages and charts
    for page_config in pages_config:
        page_num = page_config['num']
        page_name = page_config['name']

        # Add page to pages list
        if page_num not in data['pages']['pages']:
            data['pages']['pages'].append(page_num)
            data['pages']['pages'].sort()

        # Add page name
        data['pages']['names'][str(page_num)] = page_name

        # Remove any existing charts for this page
        data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(page_num)]

        # Add charts for this page
        for chart_config in page_config['charts']:
            chart = {
                "page": str(page_num),
                "tickers": chart_config['tickers'],
                "showDiff": False,
                "showAvg": False,
                "showVol": False,
                "showVolume": False,
                "showRevenue": False,
                "showFundamentalsPane": False,
                "fundamentalsMetrics": ["revenue", "netincome"],
                "multipliers": {ticker: 1 for ticker in chart_config['tickers']},
                "hidden": [],
                "range": {
                    "from": 946684800,   # 2000-01-01
                    "to": 1763424000     # 2025-11-18
                },
                "useRaw": False,
                "title": chart_config['title'],
                "lastLabelVisible": False,
                "lastTickerVisible": False,
                "showZeroLine": True,
                "showFixedLegend": True,
                "showLegendTickers": False,
                "fixedLegendPos": {"x": 10, "y": 10},
                "fixedLegendSize": {"width": 600, "height": 80 + len(chart_config['tickers']) * 25},
                "height": chart_config.get('height', 400),
                "fontSize": 11,
                "showNotes": False,
                "notes": "",
                "manualInterval": "daily",
                "decimalPrecision": 2,
                "tickerColors": chart_config['colors'],
                "priceScaleAssignments": chart_config.get('priceScaleAssignments', {})
            }
            data['cards'].append(chart)

    # Save workspace
    with open(workspace_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Print summary
    print("=" * 70)
    print("FRED Macro Indicator Pages Added Successfully")
    print("=" * 70)
    print()

    for page_config in pages_config:
        print(f"Page {page_config['num']}: {page_config['name']}")
        print(f"  Charts: {len(page_config['charts'])}")
        for i, chart in enumerate(page_config['charts'], 1):
            print(f"  {i}. {chart['title']}")
            print(f"     Tickers: {', '.join(chart['tickers'])}")
        print()

    print("=" * 70)
    print("Key Features:")
    print("  - Recession indicators: T10Y2Y inversion, STLFSI4 spikes")
    print("  - Fed policy tracking: WALCL (QE/QT), FEDFUNDS (rates)")
    print("  - Labor market health: UNRATE, PAYEMS, CIVPART")
    print("  - Economic growth: GDP, UMCSENT, RSXFS")
    print("  - Credit stress: High yield spreads, TED spread")
    print("  - All charts with dual y-axis support")
    print("  - Color-coded for easy interpretation")
    print("=" * 70)
    print()
    print("Total pages added: 5 (Pages 49-53)")
    print("Total charts added:", sum(len(p['charts']) for p in pages_config))
    print("=" * 70)

    return True

if __name__ == '__main__':
    success = add_macro_pages()
    sys.exit(0 if success else 1)