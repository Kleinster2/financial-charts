# Creating Pages - Standard Procedure

Complete guide for adding new themed pages to the financial charts application.

## Overview

Pages are organizational units that group related charts together. Each page has:
- **Page Number** - Unique identifier (e.g., 1, 2, 3, 43)
- **Page Name** - Display name (e.g., "Main", "Brazil", "Israel")
- **Charts** - One or more chart cards with tickers

## Current Pages (43 total)

1. Main
2. Correlation Pairs
3. Brazil
4. Crypto
5. China Stocks
6. Cboe
7. Quantum
8. Ark
9. Semis
10. PAVE
11. Clean
12. RiskPar
13. Metals
14. STAR
15. Drugs
17. Portfolios
19. ALLW
20. Global Markets
21. NatSec
22. Argentina
25. Gaming & iGaming
27. Market Indicators
28. Tech Benchmarks
29. US Rates
30. Global Rates
31. Energy
32. Robotics
33. 2025 IPOs
34. Futures
35. Currencies
36. Cars
37. Banks
38. Critical Metals & Mining
39. Healthcare & Biotech
40. Real Estate & REITs
41. Bonds & Credit
42. Implied Volatility
43. Israel

## Standard Page Creation Procedure

### Step 1: Identify Tickers

Before creating a page, ensure all required tickers are in the database.

**Check if ticker exists:**
```bash
sqlite3 market_data.db "SELECT ticker, name FROM ticker_metadata WHERE ticker='AAPL'"
```

**Add missing tickers:**
```bash
python scripts/add_ticker.py TICKER1 TICKER2 TICKER3
```

### Step 2: Determine Page Number

Find the next available page number:

```bash
cd charting_app
python -c "import json; data=json.load(open('workspace.json')); print('Next page:', max(data['pages']['pages']) + 1)"
```

### Step 3: Create Page Script

Create a Python script to add your page (follow the template below).

**Template: `add_[name]_page.py`**

```python
#!/usr/bin/env python3
"""
Add [Name] page to workspace.json

Description of what this page tracks.
"""

import json
import sys
from pathlib import Path

def add_page():
    workspace_path = Path('charting_app/workspace.json')

    if not workspace_path.exists():
        print(f"Error: {workspace_path} not found")
        return False

    # Load workspace
    with open(workspace_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Configuration
    PAGE_NUM = 44  # Change this to next available number
    PAGE_NAME = "Your Page Name"

    # Add page to pages list
    if PAGE_NUM not in data['pages']['pages']:
        data['pages']['pages'].append(PAGE_NUM)
        data['pages']['pages'].sort()

    # Add page name
    data['pages']['names'][str(PAGE_NUM)] = PAGE_NAME

    # Remove any existing charts for this page
    data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(PAGE_NUM)]

    # Chart 1: Your First Chart
    chart1 = {
        "page": str(PAGE_NUM),
        "tickers": ["TICKER1", "TICKER2", "TICKER3"],
        "showDiff": False,
        "showAvg": False,
        "showVol": False,
        "showVolume": False,
        "showRevenue": False,
        "showFundamentalsPane": False,
        "fundamentalsMetrics": ["revenue", "netincome"],
        "multipliers": {
            "TICKER1": 1,
            "TICKER2": 1,
            "TICKER3": 1
        },
        "hidden": [],
        "range": {
            "from": 1420070400,  # 2015-01-01 (Unix timestamp)
            "to": 1763424000     # 2025-11-18 (Unix timestamp)
        },
        "useRaw": False,
        "title": "Your Chart Title",
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
            "TICKER1": "#FF6B6B",
            "TICKER2": "#4ECDC4",
            "TICKER3": "#45B7D1"
        },
        "priceScaleAssignments": {}
    }

    # Add more charts as needed
    # chart2 = { ... }

    # Add charts to workspace
    data['cards'].append(chart1)
    # data['cards'].append(chart2)

    # Save workspace
    with open(workspace_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("=" * 60)
    print(f"{PAGE_NAME} Page Added Successfully")
    print("=" * 60)
    print()
    print(f"Page Number: {PAGE_NUM}")
    print(f"Page Name: {PAGE_NAME}")
    print(f"Charts Added: 1")  # Update count
    print()
    print("=" * 60)

    return True

if __name__ == '__main__':
    success = add_page()
    sys.exit(0 if success else 1)
```

### Step 4: Configure Chart Details

#### Required Fields

- **`page`** - Page number as string (e.g., "43")
- **`tickers`** - List of ticker symbols (e.g., ["AAPL", "MSFT"])
- **`title`** - Chart title displayed in UI
- **`tickerColors`** - Color mapping for each ticker

#### Optional Fields (with defaults)

- **`showDiff`** - Show difference from first ticker (default: false)
- **`showAvg`** - Show moving average (default: false)
- **`showVol`** - Show volatility (default: false)
- **`showVolume`** - Show volume bars (default: false)
- **`showRevenue`** - Show revenue overlay (default: false)
- **`multipliers`** - Scaling factors for each ticker (default: 1)
- **`hidden`** - List of initially hidden tickers (default: [])
- **`range`** - Time range {from: timestamp, to: timestamp}
- **`height`** - Chart height in pixels (default: 450)
- **`fontSize`** - Legend font size (default: 11)
- **`manualInterval`** - "daily", "weekly", or "monthly" (default: "daily")
- **`decimalPrecision`** - Price decimal places (default: 2)

#### Date Range Timestamps

Use Unix timestamps (seconds since 1970-01-01):

```python
import datetime

# 2015-01-01
datetime.datetime(2015, 1, 1).timestamp()  # 1420070400

# 2025-11-18
datetime.datetime(2025, 11, 18).timestamp()  # 1763424000

# Or use online converter: https://www.unixtimestamp.com/
```

#### Color Palette Recommendations

**Standard Colors:**
```python
"#FF6B6B"  # Red
"#4ECDC4"  # Teal
"#45B7D1"  # Light Blue
"#FFA07A"  # Light Salmon
"#98D8C8"  # Mint
"#F7B731"  # Yellow
"#5F27CD"  # Purple
"#00D2D3"  # Cyan
"#1DD1A1"  # Green
"#FF9FF3"  # Pink
```

**Country-Themed Colors:**
- Israel: `#0038b8` (flag blue)
- Brazil: `#009B3A` (flag green), `#FEDD00` (flag yellow)
- Argentina: `#74ACDF` (flag blue)
- USA: `#B22234` (red), `#3C3B6E` (blue)

### Step 5: Run the Script

```bash
cd /c/Users/klein/financial-charts
python scripts/one_off/add_your_page.py
```

### Step 6: Verify

Check that the page was added correctly:

```bash
cd charting_app
python -c "import json; data=json.load(open('workspace.json')); \
    print('Page 44 exists:', 44 in data['pages']['pages']); \
    print('Page name:', data['pages']['names'].get('44')); \
    charts=[c for c in data['cards'] if c.get('page')=='44']; \
    print(f'Charts: {len(charts)}'); \
    [print(f'  - {c[\"title\"]}') for c in charts]"
```

### Step 7: View in Browser

1. If Flask app is running, it will auto-reload
2. If not running: `python charting_app/app.py`
3. Open http://localhost:5000
4. Click on your new page tab

## Real-World Examples

### Example 1: Simple Country Page (Israel)

```python
PAGE_NUM = 43
PAGE_NAME = "Israel"

chart1 = {
    "page": "43",
    "tickers": ["TEVA", "CHKP", "NICE", "EIS"],
    "title": "Israeli Tech Giants",
    "tickerColors": {
        "TEVA": "#0038b8",
        "CHKP": "#FF6B6B",
        "NICE": "#4ECDC4",
        "EIS": "#95E1D3"
    },
    # ... other standard fields
}
```

### Example 2: Sector Page (Electric Vehicles)

```python
PAGE_NUM = 45
PAGE_NAME = "Electric Vehicles"

chart1 = {
    "page": "45",
    "tickers": ["TSLA", "RIVN", "LCID", "NIO", "XPEV"],
    "title": "EV Manufacturers",
    "tickerColors": {
        "TSLA": "#E31937",  # Tesla red
        "RIVN": "#00D4FF",  # Rivian blue
        "LCID": "#4A90E2",  # Lucid blue
        "NIO": "#00A0E3",   # NIO blue
        "XPEV": "#FF6B35"   # XPeng orange
    },
    # ... other fields
}
```

### Example 3: Multi-Chart Page (Commodities)

```python
PAGE_NUM = 46
PAGE_NAME = "Commodities"

# Gold & Precious Metals
chart1 = {
    "page": "46",
    "tickers": ["GLD", "SLV", "PALL", "PPLT"],
    "title": "Precious Metals ETFs",
    # ...
}

# Energy
chart2 = {
    "page": "46",
    "tickers": ["USO", "UNG", "BNO", "DBO"],
    "title": "Energy Commodities",
    # ...
}

# Agriculture
chart3 = {
    "page": "46",
    "tickers": ["CORN", "WEAT", "SOYB", "CANE"],
    "title": "Agricultural Commodities",
    # ...
}
```

## Page Naming Conventions

### Geographic Pages
- Country name: "Brazil", "Israel", "Argentina", "China Stocks"
- Region: "Global Markets", "Latin America"

### Sector Pages
- Industry: "Semis", "Energy", "Healthcare & Biotech"
- Theme: "Clean", "Robotics", "Quantum"

### Asset Class Pages
- Type: "Crypto", "Futures", "Currencies", "Bonds & Credit"
- Specific: "US Rates", "Global Rates"

### Strategy Pages
- Investment style: "Portfolios", "RiskPar", "ALLW"
- Fund: "Ark", "PAVE"

### Market Data Pages
- Indicators: "Market Indicators", "Implied Volatility"
- Benchmarks: "Tech Benchmarks", "Cboe"

## Chart Naming Conventions

**Format:** `[Category] ([Key Tickers])`

**Examples:**
- "Israeli Tech Giants (Teva, Check Point, NICE, iShares Israel ETF)"
- "Brazil Blue Chips (Vale, Petrobras, Banks)"
- "EV Manufacturers (Tesla, Rivian, Lucid)"
- "Precious Metals ETFs (Gold, Silver, Palladium, Platinum)"

**Guidelines:**
- Start with category/theme
- Include 2-4 key tickers in parentheses
- Use company names, not symbols (readable by non-experts)
- Keep under 80 characters

## Best Practices

### 1. Ticker Selection
- **3-5 tickers per chart** - Optimal for readability
- **Related tickers** - Same sector, country, or theme
- **Liquid tickers** - Prefer actively traded securities
- **Data availability** - Ensure historical data exists

### 2. Chart Organization
- **1-3 charts per page** - Don't overcrowd
- **Logical grouping** - Related themes together
- **Clear titles** - Descriptive and specific

### 3. Date Ranges
- **Long-term comparison** - Use 5-10 year range
- **Recent trends** - Use 1-2 year range
- **IPO tracking** - Start from listing date

### 4. Colors
- **Distinct colors** - Easy to differentiate
- **Consistent themes** - Use palette matching page theme
- **Accessibility** - Avoid red/green only (colorblind-friendly)

### 5. Testing
- **Load page** - Verify charts render
- **Check data** - Ensure prices load correctly
- **Test interactions** - Volume, averages, export
- **Refresh** - Confirm persistence works

## Troubleshooting

### Page Not Appearing
```bash
# Check if page was added
cd charting_app
python -c "import json; data=json.load(open('workspace.json')); \
    print(data['pages']['names'].get('43'))"

# Restart Flask app
# Ctrl+C to stop, then:
python charting_app/app.py
```

### Charts Not Rendering
```bash
# Verify tickers exist in database
sqlite3 market_data.db "SELECT ticker FROM ticker_metadata WHERE ticker IN ('AAPL', 'MSFT')"

# Check for JSON syntax errors
cd charting_app
python -c "import json; json.load(open('workspace.json')); print('Valid JSON')"
```

### Colors Not Showing
- Ensure `tickerColors` has entries for ALL tickers
- Use valid hex colors (e.g., "#FF6B6B", not "red")
- Check for typos in ticker symbols

### Page Number Conflicts
```bash
# Find used page numbers
cd charting_app
python -c "import json; data=json.load(open('workspace.json')); \
    print('Used pages:', sorted(data['pages']['pages']))"
```

## Maintenance

### Updating Existing Pages

**Edit page name:**
```python
import json
data = json.load(open('charting_app/workspace.json'))
data['pages']['names']['43'] = 'New Israel Name'
json.dump(data, open('charting_app/workspace.json', 'w'), indent=2)
```

**Add chart to existing page:**
```python
# Use the same script template, but append instead of replace:
# Don't remove existing charts:
# data['cards'] = [c for c in data.get('cards', []) if c.get('page') != str(PAGE_NUM)]
```

### Deleting Pages

```python
import json
data = json.load(open('charting_app/workspace.json'))

# Remove page
data['pages']['pages'].remove(43)
del data['pages']['names']['43']

# Remove all charts from page
data['cards'] = [c for c in data['cards'] if c.get('page') != '43']

json.dump(data, open('charting_app/workspace.json', 'w'), indent=2)
```

## Related Documentation

- [ADDING_TICKERS.md](./ADDING_TICKERS.md) - How to add tickers to database
- [README.md](./README.md) - Project overview
- [CODEMAP.md](./CODEMAP.md) - Codebase structure
- [charting_app/workspace.json](./charting_app/workspace.json) - Workspace configuration

## Quick Reference

### Page Numbers In Use
1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 17, 19, 20, 21, 22, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43

### Next Available Page Number
**44**

### Total Pages
**43 pages**

### workspace.json Structure
```json
{
  "pages": {
    "active": 3,
    "names": {
      "1": "Main",
      "43": "Israel"
    },
    "pages": [1, 2, 3, ..., 43]
  },
  "cards": [
    {
      "page": "43",
      "tickers": ["TEVA", "CHKP"],
      "title": "Chart Title",
      "tickerColors": {...}
    }
  ]
}
```

## Page Categories (Dropdown Menus)

Pages are organized into dropdown menus in the navigation bar. These categories are defined in `workspace.json` under `pages.categories`.

### Available Categories

| Category | Description | Example Pages |
|----------|-------------|---------------|
| **Portfolios** | Investment portfolios and strategies | Main, Portfolios, RiskPar, ALLW, STAR |
| **Sectors** | Industry and thematic pages | Semis, Tech Benchmarks, Quantum, Energy, AI |
| **Countries** | Geographic/country-specific pages | Brazil, China, Israel, Argentina |
| **Macro** | Macroeconomic and rates pages | US Rates, Global Rates, Market Indicators |
| **Assets** | Asset class pages | Crypto, Futures, Currencies, Metals |

### workspace.json Categories Structure

```json
{
  "pages": {
    "categories": {
      "Portfolios": [1, 2, 17, 19, 12, 8, 14, 33, 6],
      "Sectors": [28, 9, 54, 7, 15, 55, 21, 25, 31, 32, 36, 37, 39, 40, 11, 64],
      "Countries": [3, 5, 22, 43, 44, 45, 46],
      "Macro": [27, 49, 50, 51, 52, 53, 29, 30, 41, 48, 58],
      "Assets": [4, 13, 38, 34, 35, 42, 20]
    }
  }
}
```

### Assigning a Page to a Category

After creating a page, add its page number to the appropriate category array:

```python
import json

# Load workspace
with open('charting_app/workspace.json', 'r') as f:
    ws = json.load(f)

# Add page 65 to Sectors category
ws['pages']['categories']['Sectors'].append(65)

# Save
with open('charting_app/workspace.json', 'w') as f:
    json.dump(ws, f, indent=2)
```

### Important Notes

- A page **must** be assigned to a category to appear in the dropdown menus
- Pages can only belong to **one** category
- If a page exists but doesn't appear in any dropdown, check `pages.categories`
- The order of pages in the array determines their order in the dropdown

## Summary

Creating a new page involves:
1. ✅ Ensure tickers are in database (`scripts/add_ticker.py`)
2. ✅ Find next page number (currently 44)
3. ✅ Create script from template (`scripts/one_off/add_[name]_page.py`)
4. ✅ Configure charts (tickers, titles, colors)
5. ✅ Run script to update `workspace.json`
6. ✅ Verify page appears in app
7. ✅ Test charts render correctly

**Standard Template:** Use `scripts/one_off/add_israel_page.py` as reference

**Time Required:** 10-15 minutes per page

**Last Updated:** 2025-11-19
