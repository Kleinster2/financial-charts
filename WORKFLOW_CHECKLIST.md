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

## Reference Documents:
- **DATA_SOURCES.md** - Detailed explanation of data sources
- **REFACTORING_STATUS.md** - Code refactoring history
- **COMPLETION_GUIDE.md** - Implementation guides

## Database Info:
- Location: `C:\Users\klein\financial-charts\market_data.db`
- Tables: `stock_prices_daily`, `futures_prices_daily`
- Format: Wide (each ticker is a column)
