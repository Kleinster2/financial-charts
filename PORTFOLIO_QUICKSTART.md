# Portfolio Quickstart Guide

## Getting Started with Portfolios

### Step 1: Initialize the Database

Run this once to create the portfolio tables:

```bash
cd C:\Users\klein\financial-charts
python -c "from portfolio_manager import PortfolioManager; PortfolioManager()"
```

### Step 2: Run the Demo

See a complete example with transactions and valuations:

```bash
python example_portfolio.py
```

This creates a sample "My Tech Portfolio" with AAPL and MSFT trades.

## Creating Your Own Portfolio

### Option A: Using Python

```python
from portfolio_manager import PortfolioManager
from portfolio_valuation import PortfolioValuation

pm = PortfolioManager()
pv = PortfolioValuation()

# 1. Create portfolio
portfolio_id = pm.create_portfolio(
    name="My Investment Portfolio",
    description="Long-term investments",
    initial_cash=100000.0
)

# 2. Buy some stocks
pm.add_transaction(
    portfolio_id=portfolio_id,
    transaction_date="2025-01-15",
    transaction_type="BUY",
    ticker="AAPL",
    quantity=100,
    price=180.50,
    fees=5.00
)

pm.add_transaction(
    portfolio_id=portfolio_id,
    transaction_date="2025-01-20",
    transaction_type="BUY",
    ticker="MSFT",
    quantity=50,
    price=375.00,
    fees=5.00
)

# 3. Calculate valuations
pv.backfill_valuations(
    portfolio_id=portfolio_id,
    start_date="2025-01-15"
)

# 4. View current holdings
holdings = pm.get_holdings(portfolio_id)
for h in holdings:
    print(f"{h['ticker']}: {h['quantity']} shares @ ${h['avg_cost']:.2f}")

# 5. Check performance
valuations = pv.get_valuation_history(portfolio_id)
latest = valuations[-1]
print(f"Total Value: ${latest['total_value']:,.2f}")
print(f"Return: {latest['cumulative_return']*100:.2f}%")
```

### Option B: Using the API

**Create Portfolio:**
```bash
curl -X POST http://localhost:5000/api/portfolio/create \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My Portfolio",
    "initial_cash": 100000
  }'
```

**Add Buy Transaction:**
```bash
curl -X POST http://localhost:5000/api/portfolio/1/transaction \
  -H "Content-Type: application/json" \
  -d '{
    "transaction_date": "2025-01-15",
    "transaction_type": "BUY",
    "ticker": "AAPL",
    "quantity": 100,
    "price": 180.50,
    "fees": 5.00
  }'
```

**Get Holdings:**
```bash
curl http://localhost:5000/api/portfolio/1/holdings
```

**Get Valuation Chart Data:**
```bash
curl http://localhost:5000/api/portfolio/1/valuations
```

## Common Operations

### Selling Shares

```python
pm.add_transaction(
    portfolio_id=portfolio_id,
    transaction_date="2025-03-01",
    transaction_type="SELL",
    ticker="AAPL",
    quantity=50,  # Sell 50 shares
    price=195.00,
    fees=5.00
)
```

### Adding Cash (Deposit)

```python
pm.add_transaction(
    portfolio_id=portfolio_id,
    transaction_date="2025-04-01",
    transaction_type="DEPOSIT",
    amount=10000.00,  # Add $10,000
    notes="Additional investment"
)
```

### Withdrawing Cash

```python
pm.add_transaction(
    portfolio_id=portfolio_id,
    transaction_date="2025-05-01",
    transaction_type="WITHDRAWAL",
    amount=5000.00,  # Withdraw $5,000
    notes="Living expenses"
)
```

### Recording Dividends

```python
pm.add_transaction(
    portfolio_id=portfolio_id,
    transaction_date="2025-06-01",
    transaction_type="DIVIDEND",
    ticker="AAPL",
    amount=150.00,  # Received $150 dividend
    notes="Quarterly dividend"
)
```

## Viewing Portfolio Data

### List All Portfolios

```python
portfolios = pm.list_portfolios()
for p in portfolios:
    print(f"{p['portfolio_id']}: {p['name']}")
```

### Get Transaction History

```python
transactions = pm.get_transactions(
    portfolio_id=1,
    start_date="2025-01-01",
    end_date="2025-12-31"
)

for t in transactions:
    print(f"{t['transaction_date']}: {t['transaction_type']} {t['ticker']} {t['quantity']}")
```

### Get Performance Metrics

```python
import requests

response = requests.get('http://localhost:5000/api/portfolio/1/performance')
metrics = response.json()

print(f"Current Value: ${metrics['current_value']:,.2f}")
print(f"Total Return: {metrics['total_return']:.2f}%")
print(f"Volatility: {metrics['volatility']:.2f}%")
```

## Plotting Portfolios on Charts

Your portfolio valuations can be plotted alongside stocks!

### Method 1: Direct API Call

The valuations endpoint returns data in the same format as stock prices:

```javascript
// In your JavaScript code
fetch('http://localhost:5000/api/portfolio/1/valuations')
  .then(r => r.json())
  .then(data => {
    // data.time and data.value arrays ready for charting
    series.setData(data.time.map((t, i) => ({
      time: t,
      value: data.value[i]
    })));
  });
```

### Method 2: Add to Your Ticker System

You could extend your data-fetcher.js to recognize portfolio IDs:

```javascript
// If ticker starts with "PORTFOLIO_", fetch from portfolio API
if (ticker.startsWith('PORTFOLIO_')) {
  const id = ticker.replace('PORTFOLIO_', '');
  const response = await fetch(`/api/portfolio/${id}/valuations`);
  return await response.json();
}
```

## Recalculating Valuations

If you bulk-import transactions or fix errors:

```python
# Recalculate all valuations
pv.backfill_valuations(portfolio_id=1)

# Or via API
curl -X POST http://localhost:5000/api/portfolio/1/recalculate \
  -H "Content-Type: application/json" \
  -d '{}'
```

## Important Notes

### Transaction Dates
- Must be valid trading days (weekends/holidays will use previous close)
- Transactions are processed in chronological order
- Adding past transactions automatically recalculates from that date forward

### Cost Basis
- **Buys**: Weighted average cost basis
- **Sells**: Average cost doesn't change, realizes P&L
- Example:
  - Buy 100 shares @ $100 = avg cost $100
  - Buy 50 shares @ $110 = avg cost $103.33
  - Sell 75 shares @ $120 = realized P&L = $1,250.25, avg cost still $103.33

### Cash Balance
- Starts with `initial_cash`
- Decreases on: BUY (price × qty + fees), WITHDRAWAL
- Increases on: SELL (price × qty - fees), DEPOSIT, DIVIDEND

### Valuations
- Calculated using closing prices from `stock_prices_daily`
- Total Value = Cash + (Sum of all positions at market price)
- Daily Return = (Today Value - Yesterday Value) / Yesterday Value
- Cumulative Return = (Current Value - Initial Cash) / Initial Cash

## Troubleshooting

### "No price for ticker on date"
- Ensure market data is updated: `python update_market_data.py`
- Check ticker exists: `SELECT * FROM stock_prices_daily LIMIT 1`

### "Cannot sell X shares, only Y available"
- Check current holdings: `pm.get_holdings(portfolio_id)`
- Verify transaction dates are in correct order

### Valuations not updating
- Run: `pv.backfill_valuations(portfolio_id)`
- Or via API: `POST /api/portfolio/<id>/recalculate`

## Advanced Usage

### Bulk Import from CSV

```python
import pandas as pd

# Read transactions from CSV
df = pd.read_csv('transactions.csv')
# Columns: date, type, ticker, quantity, price, fees

for _, row in df.iterrows():
    pm.add_transaction(
        portfolio_id=1,
        transaction_date=row['date'],
        transaction_type=row['type'],
        ticker=row['ticker'],
        quantity=row['quantity'],
        price=row['price'],
        fees=row['fees']
    )

# Recalculate all valuations
pv.backfill_valuations(portfolio_id=1)
```

### Compare Portfolio vs Benchmark

```python
# Get portfolio valuations
port_vals = pv.get_valuation_history(1)

# Get SPY (S&P 500) prices
import sqlite3
conn = sqlite3.connect('market_data.db')
cursor = conn.execute('SELECT date, SPY FROM stock_prices_daily ORDER BY date')
spy_data = cursor.fetchall()

# Compare returns
# ... analysis code ...
```

## Next Steps

1. **Try the demo**: `python example_portfolio.py`
2. **Create your portfolio**: Use Python or API examples above
3. **Import your trades**: Bulk import from brokerage statements
4. **Visualize**: Plot portfolio value alongside individual stocks
5. **Analyze**: Compare performance vs benchmarks

For detailed API documentation, see `PORTFOLIO_README.md`.
