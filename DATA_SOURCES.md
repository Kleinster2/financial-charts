# Data Sources and Availability

## Important Distinction: Database vs. API

### Database (`market_data.db`)
- **What it is**: Local SQLite database storing historical price data
- **Location**: `C:\Users\klein\financial-charts\market_data.db`
- **Update mechanism**: Scheduled job/script that fetches from yfinance
- **Status**: Shows what HAS BEEN downloaded and stored locally

**Key tables:**
- `stock_prices_daily` - Stock closing prices (wide format: each ticker is a column)
- `futures_prices_daily` - Futures contract prices (wide format)
- `stock_volumes_daily` - Trading volumes
- `futures_volumes_daily` - Futures volumes

### yfinance API
- **What it is**: Python library that fetches data from Yahoo Finance API
- **Source of truth**: Yahoo Finance maintains the actual market data
- **Availability**: May have MORE recent data than the local database
- **Update timing**: Yahoo Finance typically updates shortly after market close

## Data Freshness Check

To check what data is **available from yfinance** (not just what's in the database):

```python
import yfinance as yf

# Check latest available data for a ticker
ticker = yf.Ticker("AAPL")
data = ticker.history(period="5d")
latest_date = data.index[-1]
latest_price = data['Close'].iloc[-1]

print(f"Latest data: {latest_date}")
print(f"Close: ${latest_price:.2f}")
```

To check what's **in the database**:

```sql
SELECT Date, AAPL FROM stock_prices_daily
ORDER BY Date DESC LIMIT 1;
```

## Common Scenario

**Database lag:**
- Market closes: 4:00 PM ET
- Yahoo Finance updates: ~4:15-5:00 PM ET (data available via yfinance)
- Database update runs: (whenever the scheduled job executes)
- **Gap period**: yfinance has new data, but database hasn't been updated yet

**When checking data availability:**
1. ✓ Check yfinance to see what Yahoo Finance has
2. ✓ Check database to see what's been downloaded locally
3. ⚠️ Don't assume database is current - it may lag behind yfinance

## Database Schema Notes

**Wide format structure:**
- Each ticker is a **column**, not a row
- Date is the only temporal column
- Price values stored as REAL (floating point)

Example:
```
Date                 | AAPL   | MSFT   | GOOGL  | ...
---------------------|--------|--------|--------|-----
2025-11-11 00:00:00  | 275.25 | 508.68 | 291.31 | ...
2025-11-10 00:00:00  | 269.43 | 506.00 | 290.10 | ...
```

## Quick Reference Commands

**Check database latest date:**
```bash
sqlite3 market_data.db "SELECT MAX(Date) FROM stock_prices_daily;"
```

**Check yfinance availability:**
```bash
python -c "import yfinance as yf; print(yf.Ticker('SPY').history(period='1d'))"
```

**Update priority:**
1. Always check yfinance for actual data availability
2. Database shows historical record, not real-time availability
3. If database is stale, trigger update job (if available)
