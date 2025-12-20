# FRED Economic Indicators Guide

## Overview

Your database now includes **13 essential economic indicators** from FRED (Federal Reserve Economic Data) to provide macro context for market analysis. These complement your 1,277+ stocks, ETFs, and indices with key economic data.

## Current Indicators (Tier 1)

### Treasury Yields (Daily Updates)

| Code | Description | History | Latest |
|------|-------------|---------|--------|
| **DGS2** | 2-Year Treasury Constant Maturity Rate | 49 years (1976-) | 2025-11-19 |
| **DGS10** | 10-Year Treasury Constant Maturity Rate | 63 years (1962-) | 2025-11-19 |
| **DGS30** | 30-Year Treasury Constant Maturity Rate | 48 years (1977-) | 2025-11-19 |
| **T10Y2Y** | 10-Year minus 2-Year Spread | 49 years (1976-) | 2025-11-20 |

**Why these matter:**
- Track interest rate environment
- T10Y2Y inversion (negative spread) predicts recessions (2007, 2019, 2022)
- Affects discount rates for equity valuation

### Fed Policy (Daily/Monthly Updates)

| Code | Description | History | Latest |
|------|-------------|---------|--------|
| **FEDFUNDS** | Effective Federal Funds Rate | 71 years (1954-) | 2025-10-01 |
| **DFEDTARU** | Fed Funds Target Rate - Upper Limit | 17 years (2008-) | 2025-11-20 |
| **DFEDTARL** | Fed Funds Target Rate - Lower Limit | 17 years (2008-) | 2025-11-20 |

**Why these matter:**
- Primary monetary policy tool
- Affects borrowing costs, currency strength, asset prices
- FEDFUNDS is monthly (1 month lag), target rates are daily

### Inflation Measures

| Code | Description | History | Latest |
|------|-------------|---------|--------|
| **CPIAUCSL** | Consumer Price Index (All Items) | 78 years (1947-) | 2025-09-01 |
| **CPILFESL** | Core CPI (Less Food & Energy) | 68 years (1957-) | 2025-09-01 |
| **T5YIE** | 5-Year Breakeven Inflation Rate | 22 years (2003-) | 2025-11-20 |
| **T10YIE** | 10-Year Breakeven Inflation Rate | 22 years (2003-) | 2025-11-20 |

**Why these matter:**
- CPI is Fed's official inflation gauge (target: 2%)
- Monthly data (1-2 month lag for official releases)
- Breakeven rates show market's real-time inflation expectations

### Credit Spreads (Daily Updates)

| Code | Description | History | Latest |
|------|-------------|---------|--------|
| **BAMLH0A0HYM2** | ICE BofA High Yield Spread | 30 years (1996-) | 2025-11-19 |
| **BAMLC0A0CM** | ICE BofA Corporate Spread | 30 years (1996-) | 2025-11-19 |

**Why these matter:**
- Credit stress indicator (widens during crises)
- High yield spread >1000bp = severe stress (2008, 2020)
- Corporate spread shows investment-grade credit risk

## Usage Examples

### Cross-Asset Analysis

Compare stock volatility with macro factors:
```python
import sqlite3
import pandas as pd
from constants import DB_PATH

conn = sqlite3.connect(DB_PATH)

# Load data
df = pd.read_sql("""
    SELECT Date, "^VIX", DGS10, T10Y2Y, BAMLH0A0HYM2, FEDFUNDS
    FROM stock_prices_daily
    WHERE Date >= '2020-01-01'
    ORDER BY Date
""", conn)

# Analysis
print(df.corr())  # Correlation matrix
```

### Recession Signals

Classic indicators:
1. **Yield curve inversion**: T10Y2Y < 0
2. **Credit stress**: BAMLH0A0HYM2 > 1000
3. **Rising unemployment**: UNRATE trending up (if you added Tier 2)

### Chart Overlays

In your charting app, overlay macro context:
- ^VIX (stock volatility) + BAMLH0A0HYM2 (credit stress)
- ^GSPC (S&P 500) + T10Y2Y (yield curve)
- Gold vs T10YIE (inflation expectations)

## Scripts Reference

### 1. `download_fred_indicators.py`
**Initial setup - download historical data**

```bash
# Download Tier 1 essentials (13 indicators)
python download_fred_indicators.py --tier 1

# Download all indicators (Tier 1 + Tier 2 = 39 total)
python download_fred_indicators.py --tier 2

# Download specific categories
python download_fred_indicators.py --tier custom --categories treasury_yields labor
```

**Run once to populate historical data.**

### 2. `update_fred_indicators.py`
**Ongoing updates - keep data current**

```bash
# Update all FRED indicators in database (default: last 60 days)
python update_fred_indicators.py

# Update with custom lookback
python update_fred_indicators.py --lookback 90
```

**Run daily/weekly to maintain freshness.**

## Daily Update Workflow

### Recommended: Single Unified Command

```bash
# Update everything including FRED indicators
python update_market_data.py --assets all --lookback 10

# Or check data freshness first
python update_market_data.py --status
```

**Total time:** ~5 minutes for all 1,290+ series

## Available Tier 2 Indicators

If you want to expand beyond Tier 1, run:
```bash
python download_fred_indicators.py --tier 2
```

This adds:

**Labor Market (4 indicators):**
- UNRATE - Unemployment Rate
- PAYEMS - Nonfarm Payrolls
- CIVPART - Labor Force Participation
- U6RATE - Underemployment Rate

**Economic Activity (4 indicators):**
- GDP - Gross Domestic Product
- GDPC1 - Real GDP
- UMCSENT - Consumer Sentiment
- RSXFS - Retail Sales

**Liquidity (3 indicators):**
- WALCL - Fed Balance Sheet
- RRPONTSYD - Reverse Repo
- WTREGEN - Treasury General Account

**Financial Stress (2 indicators):**
- STLFSI4 - Financial Stress Index
- TEDRATE - TED Spread

**Commodities (3 indicators):**
- DCOILWTICO - WTI Crude Oil
- GOLDAMGBD228NLBM - Gold Price
- DCOILBRENTEU - Brent Crude

**Forex (3 indicators):**
- DEXCHUS - China/US Exchange Rate
- DEXJPUS - Japan/US Exchange Rate
- DEXUSEU - US/Euro Exchange Rate

## Data Characteristics

### Update Frequencies

| Type | Frequency | Lag | Example |
|------|-----------|-----|---------|
| Treasury Yields | Daily | 1 day | DGS10 |
| Credit Spreads | Daily | 1 day | BAMLH0A0HYM2 |
| Fed Target Rates | Daily | Real-time | DFEDTARU |
| Fed Funds (Actual) | Monthly | 1 month | FEDFUNDS |
| CPI | Monthly | 2 weeks | CPIAUCSL |
| Nonfarm Payrolls | Monthly | 1 week | PAYEMS |
| GDP | Quarterly | 1 month | GDP |

### Data Quality

- **Source**: St. Louis Federal Reserve (FRED)
- **Reliability**: 99.9%+ uptime, rarely has outages
- **No API key required** for basic CSV downloads
- **Historical depth**: Many series go back 50+ years
- **No rate limits** on CSV endpoint

## Troubleshooting

### If update fails:

1. **Check internet connection**
   ```bash
   curl https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
   ```

2. **Verify indicator is in database**
   ```bash
   python -c "
   import sqlite3
   from constants import DB_PATH
   conn = sqlite3.connect(DB_PATH)
   cursor = conn.cursor()
   cursor.execute('PRAGMA table_info(stock_prices_daily)')
   cols = [row[1] for row in cursor.fetchall()]
   fred_cols = [c for c in cols if c in ['DGS10', 'FEDFUNDS', 'CPIAUCSL']]
   print('FRED columns:', fred_cols)
   "
   ```

3. **Check FRED series status**
   - Visit: https://fred.stlouisfed.org/series/[CODE]
   - Example: https://fred.stlouisfed.org/series/DGS10

### Monthly data won't update daily

This is expected. CPI, FEDFUNDS, PAYEMS only update monthly:
- **CPI**: Mid-month release (15th ±2 days)
- **FEDFUNDS**: First week of month
- **PAYEMS**: First Friday of month

Use `--lookback 60` to catch monthly releases.

## Integration with Charting App

The FRED indicators are stored as regular columns in `stock_prices_daily` table, so they work with all existing chart features:

```javascript
// In charting_app, these work like any ticker:
chartManager.addSeries('DGS10', {
    name: '10-Year Treasury',
    color: '#FF6B6B',
    priceScaleId: 'left'
});

chartManager.addSeries('^VIX', {
    name: 'VIX',
    color: '#4ECDC4',
    priceScaleId: 'right'
});
```

No code changes needed - FRED indicators are first-class citizens in your database!

## Performance Notes

**Download times:**
- Tier 1 (13 indicators): ~15-30 seconds
- Tier 2 (39 indicators): ~60-90 seconds
- Daily update: ~5-10 seconds

**Database impact:**
- Tier 1 adds ~18,000 rows (date range expansion)
- Tier 2 adds ~25,000 rows total
- Negligible size increase (<1 MB)

## Future Expansion

Want to add more FRED series? Edit `download_fred_indicators.py` and add to `FRED_INDICATORS` dict:

```python
'your_category': {
    'FRED_CODE': 'Description',
    'DEXUSUK': 'USD/GBP Exchange Rate',
}
```

Browse 841,000+ series at https://fred.stlouisfed.org/

---

**Last Updated:** 2025-11-21
**Database:** market_data.db
**Total FRED Indicators:** 13 (Tier 1) / 39 (Tier 1 + Tier 2 available)
**Oldest Data:** 1947 (CPIAUCSL)
**Update Source:** https://fred.stlouisfed.org/
