# Portfolio Management Guide

Comprehensive portfolio tracking with transaction history, daily valuations, and ALLW ETF replication.

## Quick Start

```bash
# Initialize database tables
python -c "from portfolio_manager import PortfolioManager; PortfolioManager()"

# Run demo
python example_portfolio.py
```

## Features

- **Multiple Portfolios**: Create and manage independent portfolios
- **Transaction Tracking**: Buys, sells, deposits, withdrawals, dividends
- **Daily Mark-to-Market**: Automatic valuations using market prices
- **ALLW Replication**: Replicate State Street's ALLW ETF

## Creating a Portfolio

### Python API

```python
from portfolio_manager import PortfolioManager
from portfolio_valuation import PortfolioValuation

pm = PortfolioManager()
pv = PortfolioValuation()

# Create portfolio
portfolio_id = pm.create_portfolio(
    name="My Portfolio",
    initial_cash=100000.0
)

# Buy stocks
pm.add_transaction(
    portfolio_id=portfolio_id,
    transaction_date="2025-01-15",
    transaction_type="BUY",
    ticker="AAPL",
    quantity=100,
    price=180.50,
    fees=5.00
)

# Calculate valuations
pv.backfill_valuations(portfolio_id=portfolio_id, start_date="2025-01-15")

# View holdings
holdings = pm.get_holdings(portfolio_id)
```

### REST API

**Create Portfolio:**
```bash
curl -X POST http://localhost:5000/api/portfolio/create \
  -H "Content-Type: application/json" \
  -d '{"name": "My Portfolio", "initial_cash": 100000}'
```

**Add Transaction:**
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

**Get Valuations (for charting):**
```bash
curl http://localhost:5000/api/portfolio/1/valuations
```

## Transaction Types

| Type | Effect |
|------|--------|
| **BUY** | Decrease cash, increase position |
| **SELL** | Increase cash, decrease position |
| **DEPOSIT** | Add cash to portfolio |
| **WITHDRAWAL** | Remove cash from portfolio |
| **DIVIDEND** | Add dividend income as cash |

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/portfolio/list` | GET | List all portfolios |
| `/api/portfolio/create` | POST | Create new portfolio |
| `/api/portfolio/<id>/holdings` | GET | Current positions |
| `/api/portfolio/<id>/transaction` | POST | Add transaction |
| `/api/portfolio/<id>/transactions` | GET | Transaction history |
| `/api/portfolio/<id>/valuations` | GET | Daily values (chart format) |
| `/api/portfolio/<id>/performance` | GET | Performance metrics |
| `/api/portfolio/<id>/recalculate` | POST | Recalculate valuations |

## Database Schema

### Tables
- `portfolios` - Portfolio master records
- `portfolio_transactions` - Transaction log
- `portfolio_holdings` - Current positions
- `portfolio_valuations_daily` - Daily values
- `portfolio_holdings_daily` - Daily position snapshots

## Cost Basis

- **Buys**: Weighted average cost basis
- **Sells**: Average cost unchanged, realizes P&L

**Example:**
- Buy 100 @ $100 = avg cost $100
- Buy 50 @ $110 = avg cost $103.33
- Sell 75 @ $120 = P&L = $1,250, avg cost still $103.33

---

# ALLW ETF Replication

Replicate State Street's ALLW ETF with a simplified portfolio.

## Quick Start

```bash
# Download ALLW holdings
python download_allw_holdings.py

# Generate replication portfolios
python generate_allw_replication.py

# Calculate positions for $100,000
python calculate_portfolio_value.py 100000 ALLW_SCALED 2025-10-06
```

## ALLW Scaled Portfolio ($100,000)

| Ticker | Name | Shares | Cost | Weight |
|--------|------|--------|------|--------|
| SPLG | S&P 500 ETF | 768 | $60,465 | 60.5% |
| SPEM | Emerging Markets | 400 | $18,992 | 19.0% |
| GXC | China ETF | 121 | $12,837 | 12.9% |
| GLD | Gold Trust | 20 | $7,288 | 7.6% |
| **CASH** | | | $419 | 0.4% |

## Why ALLW Uses 77% Cash

ALLW holds ~23% in ETFs and ~77% cash as margin for futures:
- Bond futures (~$380M notional)
- Equity index futures (~$100M notional)
- Commodity futures (~$60M notional)

The **Scaled Portfolio** eliminates this cash drag by scaling up ETF weights to 100%.

## Portfolio Options

### Option 1: Buy ALLW Directly
- **Simplicity**: Easiest approach
- **Cost**: 0.15% expense ratio
- **Tracking Error**: 0%

### Option 2: ALLW Scaled (Recommended for Replication)
- **Simplicity**: 4 ETFs, quarterly rebalancing
- **Cost**: ~0.05% expense ratio
- **Tracking Error**: 1-2% annually

### Option 3: Direct Holdings (77% Cash)
- **Matches**: ALLW's actual structure
- **Cost**: ~0.05% on invested portion
- **Tracking Error**: 0.3-0.8%

## When to Use Each

| Approach | Best For |
|----------|----------|
| Buy ALLW | < $50k, want simplicity |
| Replication | > $100k, want lower costs, tax-loss harvesting |

**Break-even**: ~$100k (saves $100/year vs ALLW ER)

## Rebalancing

```bash
# Quarterly: Download latest, regenerate, recalculate
python download_allw_holdings.py
python generate_allw_replication.py
python calculate_portfolio_value.py YOUR_AMOUNT ALLW_SCALED LATEST_DATE
```

## Export for Broker

```bash
python export_portfolio.py broker ALLW_SCALED 2025-10-06 100000
python export_portfolio.py csv ALLW_SCALED 2025-10-06
```

## Database Tables

### `etf_holdings_daily`
Daily ALLW holdings from State Street.

```sql
SELECT ticker, name, ROUND(weight*100,2) as weight_pct
FROM etf_holdings_daily
WHERE etf='ALLW'
ORDER BY ABS(weight) DESC;
```

### `replication_portfolios`
Generated replication portfolios.

```sql
SELECT portfolio_name, ticker, ROUND(weight*100,2) as weight_pct
FROM replication_portfolios
WHERE as_of_date='2025-10-06'
ORDER BY weight DESC;
```

## Files

| File | Purpose |
|------|---------|
| `portfolio_manager.py` | Core portfolio operations |
| `portfolio_valuation.py` | Daily mark-to-market |
| `portfolio_routes.py` | Flask API endpoints |
| `download_allw_holdings.py` | Download ALLW holdings |
| `generate_allw_replication.py` | Create replication portfolios |
| `calculate_portfolio_value.py` | Calculate positions |
| `export_portfolio.py` | Export to CSV/JSON |

## Troubleshooting

### "No price for ticker on date"
```bash
python update_market_data_fixed.py --batch-size 20
```

### "Cannot sell X shares, only Y available"
Check holdings: `pm.get_holdings(portfolio_id)`

### Valuations not updating
```python
pv.backfill_valuations(portfolio_id)
```

### "No holdings found" (ALLW)
```bash
python download_allw_holdings.py
```

## Limitations

- Long positions only (no short selling)
- Daily close prices only (no intraday)
- Single currency per portfolio
- No options or derivatives

## Resources

- [ALLW Product Page](https://www.ssga.com/us/en/intermediary/etfs/funds/spdr-ssga-active-large-cap-etf-allw)
- [ALLW Daily Holdings](https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-allw.xlsx)
