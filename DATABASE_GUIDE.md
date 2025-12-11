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
