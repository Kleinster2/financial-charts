# Index Update Strategy

## Overview

Your database has **49 index tickers** (^ prefix) tracking market volatility, international markets, and treasury yields. These require a **hybrid update approach** using both Yahoo Finance and FRED data sources.

## Update Strategy

### Primary Source: Yahoo Finance (44 of 49 indices)

**Works for:**
- All major US indices (^GSPC, ^DJI, ^IXIC, ^RUT)
- All international indices (^N225, ^FTSE, ^GDAXI, etc.)
- Most volatility indices (^VIX, ^VXN, ^VXD, etc.)
- **Single-stock volatility indices** (^VXAPL, ^VXAZN, ^VXGOG, ^VXGS, ^VXIBM)
- Treasury yields (^IRX, ^FVX, ^TNX, ^TYX)

**Script:** `python update_market_data.py --assets etfs --lookback 10`

### Secondary Source: FRED (5 of 49 indices)

**Need FRED for:**
1. **^RVX** - Russell 2000 Volatility Index (active, but Yahoo blocks API access)
2. **^VOLQ** - Nasdaq-100 Volatility (discontinued Sept 2023)
3. **^VXO** - VXO Index (discontinued Sept 2021)
4. **^VXV** - 3-Month VIX (discontinued July 2020)
5. **^EVZ** - Euro Currency Volatility (last updated March 2025)

**Script:** `python update_market_data.py --assets fredindices --lookback 30`

## Daily Update Workflow

### Recommended: Single Unified Command

```bash
# Update everything: stocks, ETFs, futures, FRED indices, FRED indicators (~5 min)
python update_market_data.py --assets all --lookback 10

# Or check data freshness first
python update_market_data.py --status
```

**Total time:** ~5 minutes for complete update (1,290+ series)

### Alternative: ETFs Only

If you only want to update indices and ETFs (not stocks):

```bash
python update_market_data.py --assets etfs fredindices --lookback 10
```

## Why This Hybrid Approach?

### Yahoo Finance Restrictions

**Single-Stock Volatility Indices (^VXAPL, etc.):**
- ✓ Work for **daily updates** (period='5d')
- ✗ Blocked for **historical downloads** (period='max')
- **Solution:** Downloaded 15-year history from FRED initially, now use Yahoo for daily updates

**^RVX (Russell 2000 Volatility):**
- ✗ Completely blocked by Yahoo Finance ("delisted" error)
- ✓ Available on FRED with full history since 2004
- **Solution:** Always use FRED for ^RVX

**Discontinued Indices (^VOLQ, ^VXO, ^VXV, ^EVZ):**
- ✗ Yahoo returns "delisted" errors
- ✓ FRED has historical data through discontinuation dates
- **Solution:** FRED for any historical gaps; no new data expected

## FRED Index Mappings

| Yahoo Ticker | FRED Code | Status |
|--------------|-----------|--------|
| ^RVX | RVXCLS | Active - update daily |
| ^VXAPL | VXAPLCLS | Active - Yahoo works |
| ^VXAZN | VXAZNCLS | Active - Yahoo works |
| ^VXGOG | VXGOGCLS | Active - Yahoo works |
| ^VXGS | VXGSCLS | Active - Yahoo works |
| ^VXIBM | VXIBMCLS | Active - Yahoo works |
| ^VOLQ | VOLQCLS | Discontinued 2023-09-29 |
| ^VXO | VXOCLS | Discontinued 2021-09-23 |
| ^VXV | VXVCLS | Discontinued 2020-07-09 |
| ^EVZ | EVZCLS | Discontinued 2025-03-05 |

## Scripts Reference

### 1. `update_market_data.py` (Unified Script)
**Single command for all data updates**
- Supports 19 asset types: stocks, etfs, futures, fredindices, fred, fredbonds, fundamentals, etc.
- `--status` flag for data freshness dashboard
- `--lookback N` for incremental updates (recommended: 10 days)
- Interactive mode when run without arguments

```bash
python update_market_data.py --assets all --lookback 10  # Daily update
python update_market_data.py --status                     # Check freshness
```

### 2. `scripts/one_off/restore_international_indices.py`
**One-time restoration script**
- Restored 21 international indices with 25-year history
- Already run - don't need to run again
- Downloaded full history from Yahoo Finance

### 4. `scripts/one_off/restore_vixon_from_fred.py`
**One-time restoration script**
- Restored 5 single-stock vol indices with 15-year history
- Already run - don't need to run again
- Downloaded full history from FRED

## Performance Notes

**Update Times:**
- Yahoo Finance batch (1,200+ tickers): ~3-5 minutes
- FRED updates (5 indices): ~5-10 seconds
- Total daily update: ~3-5 minutes

**Data Freshness:**
- Yahoo Finance: Real-time to 15-minute delay
- FRED: End-of-day updates (usually by market close + 1 hour)

## Monitoring

Check update success with:

```bash
python scripts/diagnostics/check_nov20_final.py
```

Or query latest dates for FRED indices:

```bash
python -c "
import sqlite3
from constants import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

for ticker in ['^RVX', '^VXAPL', '^VXAZN', '^VXGOG', '^VXGS', '^VXIBM']:
    cursor.execute(f'SELECT MAX(Date) FROM stock_prices_daily WHERE \"{ticker}\" IS NOT NULL')
    latest = cursor.fetchone()[0]
    print(f'{ticker}: {latest}')

conn.close()
"
```

## Troubleshooting

**If Yahoo Finance fails for single-stock vol:**
- They still work for daily updates (period='5d')
- Fall back to FRED if needed (add to `update_indices_from_fred.py`)

**If ^RVX updates stop:**
- Check FRED status: https://fred.stlouisfed.org/series/RVXCLS
- FRED rarely has outages; usually updates by 4 PM ET

**If FRED script fails:**
- Check internet connection
- FRED doesn't require API key for basic access
- CSV download endpoint is very reliable

## Future Maintenance

**When adding new indices:**
1. Add to `ETF_TICKERS` in `download_all_assets.py`
2. Test with Yahoo Finance first
3. If blocked, add to `FRED_INDICES` in `update_indices_from_fred.py`

**Data Quality:**
- All 49 indices now have complete historical data
- Ranges from 2.6 to 26 years depending on index launch date
- Daily updates maintain completeness

## FRED Economic Indicators (NEW!)

**Added:** 13 essential macro indicators for market context

**What's included:**
- **Treasury Yields**: DGS2, DGS10, DGS30, T10Y2Y (recession predictor)
- **Fed Policy**: FEDFUNDS, DFEDTARU, DFEDTARL
- **Inflation**: CPIAUCSL, CPILFESL, T5YIE, T10YIE
- **Credit Spreads**: BAMLH0A0HYM2 (high yield), BAMLC0A0CM (corporate)

**Scripts:**
- `download_fred_indicators.py` - Initial setup (already run)
- `update_fred_indicators.py` - Daily updates (add to workflow)

**Why these matter:**
- Cross-asset analysis (overlay VIX with credit spreads)
- Recession signals (T10Y2Y inversion, credit stress)
- Fed policy context (rate changes affect all assets)
- Inflation environment (real vs nominal returns)

**See:** `FRED_INDICATORS_GUIDE.md` for full documentation

---

**Last Updated:** 2025-11-21
**Database:** market_data.db
**Total Series:** 1,290+ (49 indices + 1,228 stocks/ETFs/FX/crypto + 13 FRED indicators)
