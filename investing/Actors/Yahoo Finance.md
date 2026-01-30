#actor #fintech #data #usa

**Yahoo Finance** — Free financial data platform. Part of [[Yahoo]] (owned by [[Apollo]]).

---

## Why Yahoo Finance matters

Primary source for **price data** in this vault via `yfinance` Python library. Also used for:
- Analyst estimates and guidance
- Earnings calendars
- Options data

---

## Data in this project

```python
import yfinance as yf
ticker = yf.Ticker("AAPL")
hist = ticker.history(period="max")  # Price history
```

**Advantages over [[Alpha Vantage]] for prices:**
- No API key required
- Higher rate limits
- Better international coverage

---

## Related

- [[Alpha Vantage]] — alternative (used for fundamentals)
- [[Yahoo]] — parent company
- [[Apollo]] — Yahoo owner
