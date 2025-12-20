# Implied Volatility Guide

Track CBOE implied volatility for individual stocks using real-time options data.

## Quick Start

```bash
# 1. Fetch IV data for sample stocks
python cboe_iv_fetcher.py

# 2. Start Flask server
python charting_app/app.py

# 3. Test API
curl "http://localhost:5000/api/iv/latest?tickers=AAPL,MSFT,TSLA"
```

**Sample Output:**
```json
{
  "AAPL": {"average_iv": 0.33, "call_iv": 0.40, "put_iv": 0.26, "current_price": 266.20},
  "TSLA": {"average_iv": 0.64, "call_iv": 0.53, "put_iv": 0.75, "current_price": 398.92}
}
```

## Features

- **Stock Implied Volatility**: At-the-money (ATM) call and put IV
- **CBOE Indices**: VIX, VXN, VXD tracking
- **Stock VIX Indices**: ^VXAPL, ^VXAZN, ^VXGOG, ^VXIBM, ^VXGS
- **Historical Storage**: SQLite database for trend analysis
- **REST API**: Easy integration with frontend

## Data Sources

### CBOE Benchmark Indices (^VIX, ^VXN, ^VXD)
- **Source**: Yahoo Finance (yfinance)
- **History**: Full history available via `period='max'`

### Individual Stock VIX Indices (^VXAPL, ^VXAZN, ^VXGOG, ^VXIBM, ^VXGS)
- **Primary Source**: CBOE CSV files (recommended)
- **Fallback**: Yahoo Finance (only 1 day available)

**Why CBOE CSV?** Yahoo Finance only provides 1-5 days for individual stock VIX indices. CBOE provides full history since 2011.

| Index | Stock | CBOE CSV URL |
|-------|-------|--------------|
| ^VXAPL | Apple | `https://cdn.cboe.com/api/global/us_indices/daily_prices/VXAPL_History.csv` |
| ^VXAZN | Amazon | `https://cdn.cboe.com/api/global/us_indices/daily_prices/VXAZN_History.csv` |
| ^VXGOG | Google | `https://cdn.cboe.com/api/global/us_indices/daily_prices/VXGOG_History.csv` |
| ^VXIBM | IBM | `https://cdn.cboe.com/api/global/us_indices/daily_prices/VXIBM_History.csv` |
| ^VXGS | Goldman Sachs | `https://cdn.cboe.com/api/global/us_indices/daily_prices/VXGS_History.csv` |

The `cboe_iv_fetcher.py` automatically uses CBOE CSV for these indices via `update_stock_vix_from_cboe()`.

## API Endpoints

### `/api/iv/stock`
Historical implied volatility for stocks.

```
GET /api/iv/stock?tickers=AAPL,MSFT&days=30
```

**Response:**
```json
{
  "AAPL": [
    {"time": 1763442000, "date": "2025-11-18", "call_iv": 0.40, "put_iv": 0.26, "average_iv": 0.33}
  ]
}
```

### `/api/iv/cboe`
CBOE volatility indices (VIX, VXN, VXD).

```
GET /api/iv/cboe?symbols=^VIX,^VXN&days=30
```

### `/api/iv/latest`
Latest IV values for quick lookups.

```
GET /api/iv/latest?tickers=AAPL,MSFT,TSLA
```

## Database Schema

### `implied_volatility_daily`

| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | YYYY-MM-DD format |
| ticker | TEXT | Stock symbol |
| call_iv | REAL | ATM call implied volatility |
| put_iv | REAL | ATM put implied volatility |
| average_iv | REAL | Average of call and put IV |
| current_price | REAL | Stock price at capture |

### `cboe_indices_daily`

| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | YYYY-MM-DD format |
| symbol | TEXT | Index symbol (^VIX) |
| value | REAL | Index value |

## Python Usage

```python
from cboe_iv_fetcher import CBOEImpliedVolatilityFetcher

fetcher = CBOEImpliedVolatilityFetcher()
fetcher.init_database()

# Fetch IV for stocks
stocks = ['AAPL', 'MSFT', 'TSLA', 'SPY', 'QQQ']
fetcher.fetch_and_store_stock_iv(stocks)

# Fetch CBOE indices
fetcher.fetch_and_store_cboe_indices()

# Get historical data
history = fetcher.get_iv_history('AAPL', days=30)
```

### Daily Update Script

```python
# update_iv_daily.py
from cboe_iv_fetcher import CBOEImpliedVolatilityFetcher

fetcher = CBOEImpliedVolatilityFetcher()

stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'META', 'SPY', 'QQQ']
fetcher.fetch_and_store_stock_iv(stocks)
fetcher.fetch_and_store_cboe_indices()
```

## Interpreting IV Values

### Stock IV Levels
| Range | Interpretation | Examples |
|-------|---------------|----------|
| < 0.25 | Low volatility | Utilities, stable large-caps |
| 0.25-0.40 | Moderate | Most large-cap stocks |
| 0.40-0.60 | High | Growth stocks, tech |
| > 0.60 | Very high | Speculative, meme stocks |

### VIX (Fear Gauge)
| Range | Market Condition |
|-------|-----------------|
| < 15 | Complacent, calm |
| 15-25 | Normal |
| 25-35 | Elevated uncertainty |
| > 35 | High fear, panic |

### Example IV Values

| Ticker | Average IV | Volatility Level |
|--------|-----------|------------------|
| AAPL | 0.30 | Moderate |
| MSFT | 0.37 | Moderate |
| TSLA | 0.63 | High |
| NVDA | 0.93 | Very high |
| SPY | 0.19 | Low (ETF) |

## Frontend Integration

### Fetching IV Data

```javascript
async function fetchImpliedVolatility(tickers, days = 365) {
  const response = await fetch(`/api/iv/stock?tickers=${tickers.join(',')}&days=${days}`);
  const data = await response.json();

  // Convert to chart format
  const result = {};
  for (const [ticker, ivData] of Object.entries(data)) {
    result[ticker] = ivData.map(d => ({
      time: d.time,
      value: d.average_iv
    }));
  }
  return result;
}
```

### Charts Available

**Page 6 (Cboe):** VIX, VXN, VXD indices - works immediately

**Page 42 (Implied Volatility):**
- Tech Giants IV (AAPL, MSFT, GOOGL, AMZN)
- High Volatility Tech IV (TSLA, NVDA, AMD, META)
- Index ETFs IV (SPY, QQQ, IWM, DIA)
- Big Banks IV (JPM, BAC, WFC, C)

## Troubleshooting

### No Data for a Stock
```python
# Check if options are available
import yfinance as yf
ticker = yf.Ticker('SYMBOL')
print(ticker.options)  # Should return expiration dates
```

**Possible causes:**
- Stock doesn't have options
- Options are too illiquid
- yfinance data unavailable

### API Returns Empty Arrays
1. Run the fetcher to populate data
2. Check with `days=365` for wider range
3. Verify data exists:
```bash
sqlite3 market_data.db "SELECT * FROM implied_volatility_daily LIMIT 5;"
```

### Database Errors
```python
# Initialize tables if missing
fetcher = CBOEImpliedVolatilityFetcher()
fetcher.init_database()
```

## Limitations

- **Options Availability**: Only works for optionable stocks
- **Market Hours**: Data updates during market hours only
- **No Historical Options**: yfinance provides current IV only (build history by daily fetching)
- **ATM Definition**: Uses closest strike to current price
- **Liquidity**: ATM detection requires liquid options

## Files

| File | Purpose |
|------|---------|
| `cboe_iv_fetcher.py` | Main fetcher module |
| `implied_volatility_fetcher.py` | Alpha Vantage alternative (not recommended) |
| `populate_iv_data.py` | Populate data for all chart stocks |

## Resources

- [CBOE VIX Methodology](https://www.cboe.com/tradable_products/vix/)
- [Options Volatility Explained](https://www.investopedia.com/terms/i/iv.asp)
- [yfinance Documentation](https://pypi.org/project/yfinance/)
