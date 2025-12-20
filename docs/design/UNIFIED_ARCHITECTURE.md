# Unified Ticker Architecture ✅

## Core Principle: All Tickers Are Just Tickers

**No special configuration needed.** The system automatically knows how to handle any ticker.

## How It Works

### Workspace Configuration
```json
{
  "page": "42",
  "title": "Apple Price vs Volatility Comparison",
  "tickers": ["AAPL", "^VXAPL"]
}
```

**That's it!** No `dataType`, no `ivMetric`, no special flags. Just list the tickers you want.

### Single Table Architecture

**All tickers live in `stock_prices_daily` table as columns:**
- Stock prices: `AAPL`, `MSFT`, `GOOGL` (in dollars)
- CBOE IV indices: `^VXAPL`, `^VIX`, `^VXN` (in percentage)
- Futures, bonds, FX: All other tickers

**One table, one query, one API endpoint.**

### Frontend Implementation

**data-fetcher.js:**
```javascript
async getData(tickers, days = 5475, interval = 'daily', options = {}) {
    // ALL tickers go to the same endpoint (/api/data).
    // Returns uniform format: {ticker: [{time, value}, ...]}
    // (days param unused; fromDate/toDate passed as null to getPriceData)
    const { signal } = options;
    return await this.getPriceData(tickers, null, null, interval, { signal });
}
```

**chart-card-plot.js (ChartCardPlot):**
```javascript
const data = await DataFetcher.getData(tickerList, 5475, interval, { signal });

// Series setup is uniform (no per-ticker routing)
ChartSeriesManager.setupPriceSeries(chart, tickerList, data, /* ... */);
```

## Available Tickers

### CBOE Volatility Indices (15 years of historical data)

**Market Indices:**
- `^VIX` - S&P 500 Volatility Index (use as proxy for SPY, broad market)
- `^VXN` - Nasdaq-100 Volatility Index (use as proxy for QQQ, tech stocks)
- `^VXD` - Dow Jones Volatility Index (use as proxy for DIA, blue chips)
- `^RVX` - Russell 2000 Volatility Index (use as proxy for IWM, small caps)

**Stock-Specific Indices:**
- `^VXAPL` - Apple VIX Index
- `^VXAZN` - Amazon VIX Index
- `^VXGOG` - Google VIX Index
- `^VXGS` - Goldman Sachs VIX Index
- `^VXIBM` - IBM VIX Index

### Using CBOE Indices as Proxies

For stocks without dedicated CBOE indices, use sector/market proxies:

- **Tech stocks** (MSFT, NVDA, AMD, META, TSLA) → Use `^VXN` (Nasdaq-100 volatility)
- **Financial stocks** (JPM, BAC, WFC, C) → Use `^VIX` (market volatility)
- **Any S&P 500 stock** → Use `^VIX` (market volatility)

**Why proxies?** CBOE indices provide 15 years of professional-grade data immediately, representing sector-wide volatility.

### Any Stock Price Ticker
- `AAPL`, `GOOGL`, `AMZN`, `NFLX`, `MSFT`, etc.
- Any ticker in your `stock_prices_daily` table

## Example Configurations

**Compare price vs volatility:**
```json
{
  "title": "Apple: Price vs Implied Volatility",
  "tickers": ["AAPL", "^VXAPL"]
}
```

**Multiple IV indices:**
```json
{
  "title": "Tech Volatility Comparison",
  "tickers": ["^VXAPL", "^VXAZN", "^VXGOG", "^VXN"]
}
```

**Tech stock with sector proxy:**
```json
{
  "title": "Microsoft: Price vs Nasdaq Volatility",
  "tickers": ["MSFT", "^VXN"]
}
```

**Market overview:**
```json
{
  "title": "Market Overview",
  "tickers": ["SPY", "^VIX", "QQQ", "^VXN"]
}
```

## Architecture Benefits

✅ **Single Source of Truth**: One table (`stock_prices_daily`) for all ticker data
✅ **Simple**: Just list tickers, no configuration
✅ **Fast**: Single query fetches all tickers simultaneously
✅ **Maintainable**: One code path for all data types
✅ **Extensible**: Easy to add new tickers (just add column)
✅ **Consistent**: All data in same format (date + value columns)

## Key Files

- **`charting_sandbox/data-fetcher.js`**: `DataFetcher.getData()` - unified fetching
- **`charting_sandbox/chart-card-plot.js`**: `ChartCardPlot.plot()` calls `DataFetcher.getData()` for all tickers
- **`charting_app/app.py`**: `/api/data` endpoint - queries `stock_prices_daily`
- **`charting_app/workspace.json`**: Clean ticker-only configuration
- **`cboe_iv_fetcher.py`**: Updates `stock_prices_daily` IV columns

## Database Schema

### Single Table: `stock_prices_daily`

**Structure:** Wide format (1000+ columns)
```sql
CREATE TABLE stock_prices_daily (
    Date TIMESTAMP PRIMARY KEY,
    "AAPL" REAL,      -- Stock price ($267.46)
    "MSFT" REAL,      -- Stock price ($492.82)
    "^VXAPL" REAL,    -- IV index (26.65%)
    "^VIX" REAL,      -- IV index (15.42%)
    "^VXN" REAL,      -- IV index (18.23%)
    ... (1000+ more columns)
)
```

**Benefits:**
- Single query returns multiple tickers
- Fast column-based access
- Natural time-series alignment (all data shares same dates)

**Trade-offs:**
- Many columns (1000+), but SQLite handles this efficiently
- Adding new tickers requires ALTER TABLE (but rare operation)
- Some NULL values for dates before ticker existed (expected)

### Legacy Table: `cboe_indices_daily`

Still maintained for historical compatibility:
```sql
CREATE TABLE cboe_indices_daily (
    date TEXT NOT NULL,
    symbol TEXT NOT NULL,
    value REAL NOT NULL,
    description TEXT,
    PRIMARY KEY (date, symbol)
)
```

Daily updates write to BOTH tables, but frontend only uses `stock_prices_daily`.

## Backend API

### `/api/data` - Universal Data Endpoint

**Request:**
```
GET /api/data?tickers=AAPL,^VXAPL,MSFT,^VXN
```

**Response:**
```json
{
  "AAPL": [
    {"time": 1700179200, "value": 267.46},
    {"time": 1700265600, "value": 272.41},
    ...
  ],
  "^VXAPL": [
    {"time": 1700179200, "value": 26.65},
    {"time": 1700265600, "value": 25.38},
    ...
  ],
  "MSFT": [...],
  "^VXN": [...]
}
```

**Implementation:**
- Queries `stock_prices_daily` table
- `SELECT Date, "AAPL", "^VXAPL", "MSFT", "^VXN" FROM stock_prices_daily`
- Returns uniform `{time, value}` format for all tickers
- Handles weekly/monthly aggregation if requested

## Daily Updates

Run this to collect new data:
```bash
cd /c/Users/klein/financial-charts
python update_market_data.py  # Updates ALL data (prices + CBOE indices)
```

Or specifically:
```bash
python update_market_data.py --assets iv      # Just CBOE indices
python update_market_data.py --assets stocks  # Just price data
```

**Update Process:**
1. Stock prices update via `download_all_assets.py` → adds new date rows
2. IV indices update via `cboe_iv_fetcher.py` → updates IV columns for existing dates
3. All data ends up in `stock_prices_daily` table

**Note:** IV updates write directly to stock_prices_daily columns. No separate IV table needed.

---

## Migration Complete

**Status:** ✅ Fully implemented single-table architecture

**Changes Made:**
1. ✅ Migrated 18,670 IV records to `stock_prices_daily` columns
2. ✅ Updated `cboe_iv_fetcher.py` to write to wide table
3. ✅ Simplified `data-fetcher.js` - removed IV routing logic
4. ✅ Flask `/api/data` already worked - no changes needed!
5. ✅ Documentation updated

**Result:** All tickers work uniformly. Just list them - the system handles everything automatically.

**Test:** Navigate to Page 42, hard refresh (Ctrl+Shift+R), see AAPL price + ^VXAPL IV charted together from single query.
