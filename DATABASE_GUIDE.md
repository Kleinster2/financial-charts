# Database Guide

## Overview

The `market_data.db` SQLite database (~400 MB) contains all market data. This guide documents what data exists, what's critical, and how to protect it.

## Data Classification

### CRITICAL - Irreplaceable Data (NEEDS BACKUP)

These tables contain cleaned, curated, or user-generated data that **cannot be re-downloaded**:

| Table | Rows | Description | Why Critical |
|-------|------|-------------|--------------|
| `B3_DI_*` columns | 5,445 days | Brazil DI yield curve (1M-10Y) | **Manually cleaned** historical data back to 2003. Raw B3 data has errors/gaps that were fixed. |
| `bond_prices_daily` | ~2,400 | Corporate bond prices | Scraped/manual - no bulk API |
| `credit_spreads_daily` | ~340 | Calculated credit spreads | Derived from cleaned bond data |
| `portfolios` | varies | User portfolio definitions | User-created |
| `portfolio_transactions` | varies | Trade history | User-created |
| `investment_theses` | varies | Research notes | User-created |
| `jgb_yields` | ~70 | Japan govt bond yields | FRED, but cleaned |

### RE-DOWNLOADABLE - Can Recover from APIs

These can be fully reconstructed by running update scripts:

| Table | Source | Recovery Command |
|-------|--------|------------------|
| `stock_prices_daily` | yfinance | `python update_market_data.py --assets stocks etfs` |
| `stock_volumes_daily` | yfinance | Same as above |
| `futures_prices_daily` | yfinance | `python update_market_data.py --assets futures` |
| `cboe_indices_daily` | CBOE | `python update_market_data.py --assets iv` |
| `implied_volatility_daily` | CBOE | Same as above |
| `ticker_metadata` | yfinance | Auto-generated during updates |
| `company_overview` | Alpha Vantage | `python fetch_fundamentals.py` |
| `earnings_*` | Alpha Vantage | Same as above |
| `income_statement_*` | Alpha Vantage | Same as above |
| `balance_sheet_*` | Alpha Vantage | Same as above |
| `cash_flow_*` | Alpha Vantage | Same as above |

### SPECIAL: B3 DI Yield Curve Data

The `stock_prices_daily` table contains these columns with **cleaned Brazilian interest rate data**:

- `B3_DI_1M` - 1 month DI rate
- `B3_DI_3M` - 3 month DI rate
- `B3_DI_6M` - 6 month DI rate
- `B3_DI_1Y` - 1 year DI rate
- `B3_DI_2Y` - 2 year DI rate
- `B3_DI_5Y` - 5 year DI rate
- `B3_DI_10Y` - 10 year DI rate
- `BCB_CDI` - Central bank CDI rate

**History:** 5,445 trading days from 2003-08-08 to present.

**CRITICAL:** This data was manually cleaned to fix:
- Missing data points
- Outliers and data entry errors
- Format inconsistencies
- Holiday/weekend handling

While `fetch_b3_yield_curve.py` can download recent data, the historical cleaning work would be lost if this data is overwritten.

## Backup Strategy

### In-Database Backups (Automatic)

The update scripts create versioned backups before each write:
- `stock_prices_daily_backup_YYYYMMDD_HHMMSS`
- Last 3 backups retained

### External Backups (Recommended)

For critical data, export to CSV periodically:

```bash
# Export B3 DI data
python -c "
import sqlite3
import pandas as pd
conn = sqlite3.connect('market_data.db')
df = pd.read_sql('''
    SELECT Date, B3_DI_1M, B3_DI_3M, B3_DI_6M, B3_DI_1Y,
           B3_DI_2Y, B3_DI_5Y, B3_DI_10Y, BCB_CDI
    FROM stock_prices_daily
    WHERE B3_DI_1Y IS NOT NULL
''', conn)
df.to_csv('backups/b3_di_curves_backup.csv', index=False)
print(f'Exported {len(df)} rows')
"
```

### Recovery from Corruption

1. Check available backups:
```sql
SELECT name FROM sqlite_master WHERE name LIKE '%backup%';
```

2. Restore from backup:
```sql
DROP TABLE stock_prices_daily;
ALTER TABLE stock_prices_daily_backup_YYYYMMDD_HHMMSS
  RENAME TO stock_prices_daily;
```

## Update Safety

The update scripts include integrity checks that:
1. Verify historical SPY data points before writing
2. Abort if cleaned data would be overwritten with NULLs
3. Create timestamped backups before each write

To safely update:
```bash
# Use incremental mode (recommended)
python update_market_data.py  # Select option 1: Incremental (10 days)

# Or via CLI
python update_market_data.py --lookback 10
```

## Schema Notes

### Wide-Column Format

Price/volume tables use wide format: one row per date, one column per ticker.
- Pros: Fast queries for single-ticker time series
- Cons: Adding tickers requires ALTER TABLE

### Date Format

Dates are stored as strings: `YYYY-MM-DD` or `YYYY-MM-DD HH:MM:SS`
- Normalize on read: `pd.to_datetime(df['Date'])`

---

## Bug History and Fixes (December 2025)

### Incident: Database Wiped by Partial Asset Update

**Date:** December 11, 2025
**Impact:** Complete loss of stock_prices_daily table (8,700+ rows wiped)
**Root Cause:** Multiple bugs in `download_all_assets.py`

#### Bug 1: Merge Logic Corrupted Non-Downloaded Columns

**Location:** `download_all_assets.py` lines 874-877 (before fix)

**The Bug:**
```python
# OLD BUGGY CODE
combined_df = pd.concat([combined_df, new_data_df])
combined_df = combined_df[~combined_df.index.duplicated(keep='last')]
```

**Problem:** When running `--assets china` (or any partial update):
1. `new_data_df` only contained Chinese ticker columns (~80 columns)
2. `pd.concat` + `keep='last'` replaced entire rows for overlapping dates
3. For those dates, ALL non-Chinese columns became NaN
4. B3 DI data, US stocks, ETFs, etc. were silently corrupted

**The Fix:**
```python
# NEW SAFE CODE
# Only update specific columns that were downloaded
for col in new_data_df.columns:
    for date in new_data_df.index:
        if date in combined_df.index:
            combined_df.loc[date, col] = new_data_df.loc[date, col]
```

#### Bug 2: No Safety Check When existing_df Was Empty

**Location:** `download_all_assets.py` line 884-885 (before fix)

**The Bug:**
```python
else:
    combined_df = new_data_df  # DANGEROUS: Replaces entire table!
```

**Problem:** If `existing_df` was empty for ANY reason (database lock, read failure, date parsing issue), the entire table would be replaced with just the newly downloaded data.

**The Fix:**
```python
# CRITICAL SAFETY CHECK: If table exists but we couldn't read data, ABORT
if table_exists and existing_df.empty and existing_row_count_before_parse > 0:
    vprint("CRITICAL ERROR: Table exists but existing_df is empty!")
    vprint("ABORTING to prevent complete data loss.")
    return
```

#### Bug 3: No Database Lock Handling

**Location:** `download_all_assets.py` line 800 (before fix)

**The Bug:**
```python
existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
# No try-except, no retry logic
```

**Problem:** If database was locked by another process (Flask app, concurrent update), `read_sql` could fail or return incomplete data, leading to Bug 2.

**The Fix:**
```python
# Read with retry logic for database locks
max_retries = 3
retry_delay = 2
for attempt in range(max_retries):
    try:
        existing_df = pd.read_sql("SELECT * FROM stock_prices_daily", conn)
        break
    except Exception as e:
        if "locked" in str(e).lower() and attempt < max_retries - 1:
            time.sleep(retry_delay)
            retry_delay *= 2  # Exponential backoff
        else:
            vprint(f"ERROR: Failed to read existing data. ABORTING.")
            return
```

#### Bug 4: Sanity Checks Only Warned, Didn't Abort

**Location:** `download_all_assets.py` lines 945-947 (before fix)

**The Bug:**
```python
if existing_rows > 0 and new_rows < existing_rows * 0.5:
    vprint("WARNING: New row count is less than 50% of existing")
    vprint("Proceeding with caution...")  # <-- Didn't abort!
```

**The Fix:**
```python
if existing_rows > 0 and new_rows < existing_rows * 0.5:
    vprint("CRITICAL ERROR: New row count is less than 50% of existing")
    vprint("ABORTING to prevent data loss.")
    return  # <-- Now aborts
```

### Prevention Measures Now in Place

1. **Database lock retry:** 3 attempts with exponential backoff
2. **Date parsing validation:** Abort if >10% of rows fail to parse
3. **Empty DataFrame check:** Abort if table exists but can't be read
4. **Safe merge logic:** Only update downloaded columns, never replace rows
5. **Row count validation:** Abort if new data is <50% of existing
6. **Column count validation:** Abort if columns drop by >90%
7. **Integrity checks:** Sample historical SPY values before write

### Recovery Procedure Used

1. Identified latest valid backup: `stock_prices_daily_backup_20251211_012442`
2. Restored table from backup:
   ```sql
   ALTER TABLE stock_prices_daily RENAME TO stock_prices_daily_corrupted;
   ALTER TABLE stock_prices_daily_backup_20251211_012442 RENAME TO stock_prices_daily;
   ```
3. Verified B3 DI data was intact
4. Applied fixes to prevent recurrence
