# Adding New Tickers to Database

This guide explains how to add new tickers to your financial charts database.

## Quick Start

Use the standardized `scripts/add_ticker.py` script:

```bash
# Add single ticker
python scripts/add_ticker.py TSLA

# Add multiple tickers
python scripts/add_ticker.py CRWD MDB LYFT

# Add Brazilian stocks (B3)
python scripts/add_ticker.py FICT3.SA REAG3.SA

# Add any valid Yahoo Finance ticker
python scripts/add_ticker.py BTC-USD ETH-USD
```

## What the Script Does

The script performs 4 automated steps:

### 1. **Download Historical Price Data**
- Downloads full historical data from Yahoo Finance (`period='max'`)
- Handles timezone conversion to match database format
- Supports all Yahoo Finance tickers (stocks, ETFs, crypto, futures, FX, indices)

### 2. **Update Price Database**
- Adds new columns to `stock_prices_daily` table (wide-table format)
- Uses atomic table swap for safe updates
- Preserves all existing data

### 3. **Update Metadata**
- Fetches company name from Yahoo Finance
- **Automatically cleans corporate suffixes:**
  - `Inc.`, `Inc`, `Corporation`, `Corp.`, `Corp`
  - `Ltd.`, `Ltd`, `Limited`, `LLC`, `L.L.C.`
  - `S.A.`, `S.A`, `PLC`, `plc`, `N.V.`, `AG`
  - `Holdings`, `Hldgs.`, `Hldgs`, `Group`, `Company`, `Co.`
  - `Technologies`, `Industries`, `International`
- Stores cleaned name in `ticker_metadata` table
- Records date range and data point count

### 4. **Verification**
- Verifies price data was written correctly
- Confirms metadata is complete
- Shows latest price and total data points

## Output Example

```
============================================================
Add Tickers to Database
============================================================

Tickers to add: FICT3.SA, REAG3.SA
Database: market_data.db

Step 1: Downloading historical price data...
------------------------------------------------------------

Step 2: Updating stock_prices_daily table...
------------------------------------------------------------
FICT3.SA     - 6,368 data points
  Range: 2000-07-05 to 2025-11-18
  Latest: $3.00

REAG3.SA     - 1,128 data points
  Range: 2021-05-18 to 2025-11-18
  Latest: $1.65

Writing to staging table...
[OK] Price data updated

Step 3: Updating ticker_metadata table...
------------------------------------------------------------
Added FICT3.SA
  Name: Fictor Alimentos
  (Original: Fictor Alimentos S.A.)
  Range: 2000-07-05 to 2025-11-18
  Points: 6,228

Added REAG3.SA
  Name: REAG Investimentos
  (Original: REAG Investimentos S.A.)
  Range: 2021-05-18 to 2025-11-18
  Points: 1,128

[OK] Metadata updated

Step 4: Final Verification
------------------------------------------------------------
FICT3.SA     - Fictor Alimentos
  Latest: 2025-11-18 - $3.00
  Total: 6,228 data points

REAG3.SA     - REAG Investimentos
  Latest: 2025-11-18 - $1.65
  Total: 1,128 data points

============================================================
TICKERS ADDED SUCCESSFULLY
============================================================
```

## Supported Ticker Types

The script supports all Yahoo Finance ticker formats:

### US Stocks
```bash
python scripts/add_ticker.py AAPL MSFT GOOGL
```

### Brazilian Stocks (B3)
```bash
# Suffix: .SA (São Paulo Stock Exchange)
python scripts/add_ticker.py PETR4.SA VALE3.SA ITUB4.SA
```

### International Stocks
```bash
# London: .L
# Tokyo: .T
# Hong Kong: .HK
python scripts/add_ticker.py BP.L 7203.T 0700.HK
```

### Cryptocurrencies
```bash
python scripts/add_ticker.py BTC-USD ETH-USD SOL-USD
```

### Forex
```bash
python scripts/add_ticker.py EURUSD=X GBPUSD=X USDJPY=X
```

### Indices
```bash
python scripts/add_ticker.py ^GSPC ^DJI ^IXIC  # S&P 500, Dow, Nasdaq
python scripts/add_ticker.py ^VIX ^VXN ^VXD    # Volatility indices
```

### ETFs
```bash
python scripts/add_ticker.py SPY QQQ VOO VTI
```

### Futures
```bash
python scripts/add_ticker.py ES=F NQ=F GC=F CL=F
```

## Name Cleaning Examples

The script automatically cleans company names:

| Original Name | Cleaned Name |
|--------------|--------------|
| `CrowdStrike Holdings, Inc.` | `CrowdStrike` |
| `MongoDB, Inc.` | `MongoDB` |
| `Fictor Alimentos S.A.` | `Fictor Alimentos` |
| `Block, Inc.` | `Block` |
| `HSBC Hldgs plc` | `HSBC` |
| `Arm Hldgs plc` | `Arm` |
| `Johnson Controls International plc` | `Johnson Controls International` |
| `Packaging Corporation of America` | `Packaging of America` |

## Error Handling

The script handles common errors gracefully:

- **Ticker not found**: Shows "NO DATA AVAILABLE"
- **Network errors**: Displays download error message
- **Database errors**: Rolls back changes, preserves original data
- **Invalid tickers**: Shows error message, continues with valid tickers

## Manual Alternative

If you prefer to add tickers manually:

```python
import yfinance as yf
import pandas as pd
import sqlite3

# Download data
ticker = "TSLA"
stock = yf.Ticker(ticker)
hist = stock.history(period='max')

# Remove timezone
hist.index = hist.index.tz_localize(None)

# Update database
conn = sqlite3.connect('market_data.db')
existing = pd.read_sql('SELECT * FROM stock_prices_daily', conn, index_col='Date')
existing[ticker] = hist['Close']
existing.to_sql('stock_prices_daily', conn, if_exists='replace')
```

## Database Structure

### Wide Table Format

The database uses a **wide-table** structure where:
- Each ticker is a **column** (not a row)
- Each date is a **row**
- This enables fast multi-ticker queries

Example:
```
Date         | AAPL   | MSFT   | TSLA   | FICT3.SA
-------------|--------|--------|--------|----------
2025-11-18   | 267.44 | 493.79 | 401.25 | 3.00
2025-11-17   | 265.12 | 490.33 | 395.80 | 3.15
```

### Metadata Table

`ticker_metadata` stores:
- `ticker` - Ticker symbol (e.g., "AAPL", "FICT3.SA")
- `name` - **Cleaned** company name (e.g., "Apple", "Fictor Alimentos")
- `table_name` - Always "stock_prices_daily"
- `data_type` - Always "stock"
- `first_date` - First available date
- `last_date` - Last available date
- `data_points` - Total number of data points

## Troubleshooting

### "No data found" error
- Check ticker symbol is correct (case-sensitive)
- Try searching on [Yahoo Finance](https://finance.yahoo.com/)
- Some tickers may be delisted or unavailable

### Database locked error
- Make sure Flask app (`app.py`) is not running
- Close any database browser tools
- Check no other scripts are accessing the database

### Unicode encoding errors (Windows)
- This has been fixed in the script
- Previously caused issues with checkmarks (✓) in output

## Future Improvements

Planned enhancements:
- Bulk ticker import from CSV file
- Automatic detection of ticker type (stock/crypto/FX/etc.)
- Volume data import alongside price data
- Sector/industry classification
- Integration with regular `update_market_data.py` script

## Related Scripts

- `update_market_data.py` - Daily price updates for existing tickers
- `download_all_assets.py` - Bulk download for predefined ticker lists
- `scripts/extract_demo_data.py` - Extract subset for demo deployment
