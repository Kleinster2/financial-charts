# Financial Charts Workflow Checklist

## When Checking Data Availability

**ALWAYS check yfinance first, not just the database!**

### Quick Reference:

1. **yfinance** = Source of truth (Yahoo Finance API)
   - Shows what data is ACTUALLY available
   - Query: `yf.Ticker("SPY").history(period="5d")`

2. **Database** = Local cache
   - Shows what HAS BEEN downloaded
   - Query: `sqlite3 market_data.db "SELECT MAX(Date) FROM stock_prices_daily;"`
   - May lag behind yfinance by hours or days

### Standard Check Pattern:

```python
# Check yfinance availability
import yfinance as yf
data = yf.Ticker("AAPL").history(period="5d")
yf_latest = data.index[-1]

# Then check database
# sqlite3 query for comparison
```

### Common Questions:
- "Do we have today's prices?" → **Check yfinance, not database**
- "What's the latest data?" → **Check yfinance first**
- "Is data up to date?" → **Compare yfinance vs database**

## Adding New Tickers

**Three scripts for different use cases:**

### 1. `download_single_ticker.py TICKER` - Add Individual Tickers (FASTEST: ~5 seconds)

**Use this when:** Adding 1-10 new tickers

```bash
# Single ticker
python download_single_ticker.py VFS

# Multiple tickers (loop)
for ticker in VFS CHPT BLNK EVGO RACE; do
    python download_single_ticker.py $ticker
done
```

**Features:**
- Downloads maximum available history for ONE ticker
- Supports Cboe indices with direct CSV downloads
- Has data quality overrides for known bad data points
- Proper upsert logic (won't overwrite other tickers)

### 2. `update_market_data.py` - Daily Updates (FAST: ~3 minutes)

**Use this when:** Getting latest prices for existing tickers

```bash
python update_market_data.py --verbose
```

**What it does:**
- Updates ALL existing tickers with new dates only
- Adds futures contracts
- Auto-updates metadata
- Typical daily workflow

### 3. `download_all_assets.py` - Full Rebuild (SLOW: ~3 minutes)

**Use this when:** Initial setup or major configuration changes

```bash
python download_all_assets.py --verbose
```

**What it does:**
- Downloads ALL configured tickers from 2022-12-30 to today
- Re-downloads everything (inefficient for adding single tickers)
- Good for fresh database or bulk changes

### Recommended Workflow for Adding Tickers:

1. Edit `download_all_assets.py` to add ticker to appropriate list (EV_STOCKS, ETF_TICKERS, etc.)
2. Run `python download_single_ticker.py TICKER` to download just that ticker (5 seconds)
3. Commit changes to `download_all_assets.py`

**Why this matters:**
- `download_single_ticker.py TICKER` = 5 seconds for 1 ticker
- `download_all_assets.py` = 3 minutes for all 1,247 tickers
- **180x faster** when adding individual tickers!

## Reference Documents:
- **DATA_SOURCES.md** - Detailed explanation of data sources
- **REFACTORING_STATUS.md** - Code refactoring history
- **COMPLETION_GUIDE.md** - Implementation guides

## Database Info:
- Location: `C:\Users\klein\financial-charts\market_data.db`
- Tables: `stock_prices_daily`, `futures_prices_daily`
- Format: Wide (each ticker is a column)
