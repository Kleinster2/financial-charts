# Portfolio Management System

A comprehensive portfolio tracking system with transaction history and daily mark-to-market valuations.

## Features

### Core Capabilities
- **Multiple Portfolios**: Create and manage multiple independent portfolios
- **Transaction Tracking**: Record buys, sells, deposits, withdrawals, and dividends
- **Position Management**: Automatic position tracking with average cost basis
- **Daily Mark-to-Market**: Calculate daily portfolio valuations using actual market prices
- **Historical Reconstruction**: Backfill valuations for any historical date range
- **Performance Metrics**: Track daily returns, cumulative returns, and volatility

### Transaction Types
- **BUY**: Purchase securities (decreases cash, increases position)
- **SELL**: Sell securities (increases cash, decreases position)
- **DEPOSIT**: Add cash to portfolio
- **WITHDRAWAL**: Remove cash from portfolio
- **DIVIDEND**: Record dividend income

## Database Schema

### Tables
1. **portfolios**: Portfolio master records
2. **portfolio_transactions**: Complete transaction log
3. **portfolio_holdings**: Current positions (materialized view)
4. **portfolio_valuations_daily**: Daily portfolio values and returns
5. **portfolio_holdings_daily**: Daily snapshot of all positions

## API Endpoints

All endpoints are under `/api/portfolio/`

### List Portfolios
```
GET /api/portfolio/list
```
Returns array of all portfolios.

### Create Portfolio
```
POST /api/portfolio/create
Body: {
  "name": "My Portfolio",
  "description": "Optional description",
  "initial_cash": 100000.0,
  "currency": "USD"
}
```
Returns: `{"portfolio_id": 1, "success": true}`

### Get Holdings
```
GET /api/portfolio/<portfolio_id>/holdings
```
Returns current positions and cash balance.

### Add Transaction
```
POST /api/portfolio/<portfolio_id>/transaction
Body: {
  "transaction_date": "2025-01-15",
  "transaction_type": "BUY",
  "ticker": "AAPL",
  "quantity": 100,
  "price": 180.50,
  "fees": 5.00,
  "notes": "Optional notes"
}
```
Automatically recalculates valuations from transaction date forward.

### Get Transactions
```
GET /api/portfolio/<portfolio_id>/transactions?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
```
Returns transaction history.

### Get Valuations
```
GET /api/portfolio/<portfolio_id>/valuations?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
```
Returns time series data formatted for charting:
```json
{
  "time": [timestamp1, timestamp2, ...],
  "value": [value1, value2, ...],
  "raw_data": [...]
}
```

### Get Performance Metrics
```
GET /api/portfolio/<portfolio_id>/performance
```
Returns:
- Current value
- Cash balance
- Securities value
- Total return (% and $)
- Annualized volatility
- Start/end dates

### Recalculate Valuations
```
POST /api/portfolio/<portfolio_id>/recalculate
Body: {
  "start_date": "2025-01-01",  // optional
  "end_date": "2025-03-31"     // optional
}
```
Useful after bulk transaction imports or data corrections.

## Python Usage

### Basic Example

```python
from portfolio_manager import PortfolioManager
from portfolio_valuation import PortfolioValuation

pm = PortfolioManager()
pv = PortfolioValuation()

# Create portfolio
portfolio_id = pm.create_portfolio(
    name="Tech Portfolio",
    initial_cash=100000.0
)

# Buy stock
pm.add_transaction(
    portfolio_id=portfolio_id,
    transaction_date="2025-01-02",
    transaction_type="BUY",
    ticker="AAPL",
    quantity=100,
    price=180.50,
    fees=5.00
)

# Calculate valuations
pv.backfill_valuations(
    portfolio_id=portfolio_id,
    start_date="2025-01-02",
    end_date="2025-03-31"
)

# Get current holdings
holdings = pm.get_holdings(portfolio_id)
cash = pm.get_cash_balance(portfolio_id)

# Get valuation history
valuations = pv.get_valuation_history(portfolio_id)
```

### Running the Example

```bash
cd C:\Users\klein\financial-charts
python example_portfolio.py
```

This creates a demo portfolio with sample transactions and calculates valuations.

## How It Works

### Transaction Processing
1. When you add a BUY/SELL transaction:
   - Transaction is logged in `portfolio_transactions`
   - Cash balance is updated (transaction amount)
   - Holdings are updated in `portfolio_holdings`
   - Average cost basis is recalculated for buys

### Daily Valuation Calculation
1. For each trading day:
   - Reconstruct holdings from transaction history up to that date
   - Fetch closing prices for all holdings
   - Calculate market value = quantity × price
   - Calculate unrealized P&L = market value - cost basis
   - Sum all positions + cash = total portfolio value
   - Calculate daily return = (today - yesterday) / yesterday
   - Calculate cumulative return = (current - initial) / initial

### Cost Basis Tracking
- **Buys**: Weighted average cost
  - New avg = (old_qty × old_avg + new_qty × new_price) / total_qty
- **Sells**: Average cost remains unchanged
  - Realized P&L = (sale_price - avg_cost) × quantity

## Integration with Charts

Portfolio valuations can be plotted alongside individual stocks:

1. Fetch portfolio data via `/api/portfolio/<id>/valuations`
2. Data is returned in same format as stock prices
3. Add to chart using existing ticker infrastructure
4. Portfolio appears as "PORTFOLIO_<name>" in ticker list

## Performance Considerations

- **Valuations are cached**: Daily valuations are stored, not recalculated on every request
- **Incremental updates**: New transactions only recalculate from transaction date forward
- **Efficient queries**: Indices on portfolio_id and date columns
- **Lazy recalculation**: Valuations only update when transactions are added

## Limitations

- Only supports long positions (no short selling)
- Price data must exist in `stock_prices_daily` table
- No intraday tracking (daily close prices only)
- No options, bonds, or other derivatives
- Single currency per portfolio

## Future Enhancements

Potential additions:
- Short positions
- Options and derivatives
- Multiple currencies with FX conversion
- Intraday tracking
- Dividend reinvestment automation
- Tax lot tracking for FIFO/LIFO
- Benchmark comparison (vs S&P 500, etc.)
- Sharpe ratio and other risk metrics
- Portfolio rebalancing suggestions

## Files

- `portfolio_schema.sql` - Database schema
- `portfolio_manager.py` - Core portfolio operations
- `portfolio_valuation.py` - Daily mark-to-market engine
- `portfolio_routes.py` - Flask API endpoints
- `example_portfolio.py` - Demo script
- `PORTFOLIO_README.md` - This file
