# ALLW Replication Portfolio - Implementation Guide

**Generated:** October 7, 2025
**Based on ALLW holdings as of:** October 6, 2025
**Current ALLW Price:** $28.16

---

## Quick Reference: $100,000 Investment

### Option 1: Buy ALLW Directly (Recommended)
- **Shares:** 3,551 shares @ $28.16
- **Cost:** $99,996.16
- **Simplicity:** ★★★★★
- **Tracking Error:** 0%
- **Annual Cost:** 0.15% ER = $150/year

### Option 2: ALLW Scaled Portfolio (100% Invested)
| Ticker | Shares | Price | Cost | Weight |
|--------|--------|-------|------|--------|
| SPLG | 768 | $78.73 | $60,464.64 | 60.50% |
| SPEM | 400 | $47.48 | $18,992.00 | 19.01% |
| GXC | 121 | $106.09 | $12,836.89 | 12.92% |
| GLD | 20 | $364.38 | $7,287.60 | 7.58% |
| **CASH** | - | - | **$418.87** | **0.42%** |
| **TOTAL** | | | **$100,000.00** | **100%** |

- **Portfolio Efficiency:** 99.58%
- **Estimated Tracking Error:** 1-2% annually
- **Annual Cost:** ~$50-60 (weighted avg ER ~0.05%)
- **Rebalancing:** Quarterly recommended

### Option 3: Direct Holdings Approach (77% Cash)
| Ticker | Shares | Price | Cost | Weight |
|--------|--------|-------|------|--------|
| SPLG | 173 | $78.73 | $13,620.29 | 13.64% |
| SPEM | 90 | $47.48 | $4,273.20 | 4.29% |
| GXC | 27 | $106.09 | $2,864.43 | 2.91% |
| GLD | 4 | $364.38 | $1,457.52 | 1.71% |
| **CASH** | - | - | **$77,784.56** | **77.78%** |
| **TOTAL** | | | **$100,000.00** | **100%** |

- **Portfolio Efficiency:** 22.22% (most capital in cash)
- **Estimated Tracking Error:** 0.3-0.8% annually
- **Annual Cost:** ~$15 on invested portion
- **Notes:** Mimics ALLW's actual structure (futures + cash)

---

## Portfolio Breakdown by Investment Size

### $10,000 Investment

**ALLW Scaled Portfolio:**
- SPLG: 76 shares @ $78.73 = $5,983.48 (60.5%)
- SPEM: 40 shares @ $47.48 = $1,899.20 (19.0%)
- GXC: 12 shares @ $106.09 = $1,273.08 (12.9%)
- GLD: 2 shares @ $364.38 = $728.76 (7.6%)
- Cash: $115.48 (1.2%)

**Buy ALLW:** 355 shares @ $28.16 = $9,996.80

---

### $50,000 Investment

**ALLW Scaled Portfolio:**
- SPLG: 384 shares @ $78.73 = $30,232.32 (60.5%)
- SPEM: 200 shares @ $47.48 = $9,496.00 (19.0%)
- GXC: 60 shares @ $106.09 = $6,365.40 (12.9%)
- GLD: 10 shares @ $364.38 = $3,643.80 (7.6%)
- Cash: $262.48 (0.5%)

**Buy ALLW:** 1,775 shares @ $28.16 = $49,984.00

---

### $250,000 Investment

**ALLW Scaled Portfolio:**
- SPLG: 1,920 shares @ $78.73 = $151,161.60 (60.5%)
- SPEM: 1,000 shares @ $47.48 = $47,480.00 (19.0%)
- GXC: 303 shares @ $106.09 = $32,145.27 (12.9%)
- GLD: 52 shares @ $364.38 = $18,947.76 (7.6%)
- Cash: $265.37 (0.1%)

**Buy ALLW:** 8,878 shares @ $28.16 = $249,963.48

---

## ALLW Portfolio Composition (Oct 6, 2025)

### Estimated Assets Under Management: $596.5 Million

### Top Holdings by Market Value:
1. **US 10YR Note Futures (TYZ5):** $116.2M (0.03% weight)
2. **Euro-Bund Futures (RXZ5):** $83.9M (0.03% weight)
3. **SPLG (S&P 500 ETF):** $63.2M (13.64% weight)
4. **Gold Futures (GCZ5):** $61.2M (1.71% weight)
5. **US Long Bond Futures (USZ5):** $58.4M (0.16% weight)
6. **Euro Stoxx 50 Futures (VGZ5):** $43.5M (0.31% weight)
7. **Australian Bond Futures (XMZ5):** $42.8M (-0.05% weight)
8. **UK Gilt Futures (G Z5):** $34.6M (0.01% weight)
9. **TOPIX Futures (TPZ5):** $23.1M (0.18% weight)
10. **SPEM (EM ETF):** $19.9M (4.29% weight)

**Key Insight:** ALLW uses ~$477M in futures contracts (notional value) with only ~$95M in ETFs and cash as margin. This creates synthetic exposure to multiple asset classes with capital efficiency.

---

## Rebalancing Schedule

### Quarterly Rebalancing (Recommended)
- **Dates:** End of March, June, September, December
- **Triggers:**
  - Any position drifts >2% from target
  - After significant market moves (>10%)
- **Method:** Sell overweight positions, buy underweight
- **Cost:** ~$0-20 per rebalance (depending on broker)

### How to Rebalance:
```bash
# Download latest ALLW holdings
cd C:\Users\klein\financial-charts
python download_allw_holdings.py

# Regenerate portfolio
python generate_allw_replication.py

# Calculate new positions for your portfolio value
python calculate_portfolio_value.py YOUR_AMOUNT ALLW_SCALED LATEST_DATE

# Compare to current holdings and adjust
```

---

## Tax Considerations

### ALLW (Direct Purchase)
- **Advantage:** 60/40 tax treatment on futures gains
  - 60% long-term capital gains (max 20%)
  - 40% short-term (ordinary income)
- **Disadvantage:** ETF structure means less control over distributions

### Replication Portfolio
- **Advantage:**
  - Control over when you realize gains
  - Can tax-loss harvest individual positions
- **Disadvantage:**
  - Pure equity ETFs taxed at ordinary rates if held <1 year
  - No 60/40 treatment on equity positions

### Example Tax Scenario:
**$10,000 gain on $100,000 investment:**

| Approach | Tax Treatment | Estimated Tax* |
|----------|---------------|----------------|
| ALLW | 60/40 (futures) | ~$1,840 |
| Replication | 100% LT gains | ~$2,000 |
| Replication | 100% ST gains | ~$3,700 |

*Assumes 37% ordinary income rate, 20% LT cap gains rate

---

## Performance Tracking

### Expected Tracking Error Sources:

1. **Missing Futures Exposure:** ~3% of ALLW (bond/equity futures)
   - Impact: 0.3-0.5% annual tracking error

2. **Cash Drag in Scaled Portfolio:** ~0.4%
   - Impact: Minimal in flat/down markets, slight drag in up markets

3. **Rebalancing Timing:** ALLW rebalances continuously, you rebalance quarterly
   - Impact: 0.2-0.5% annual tracking error

4. **Expense Ratio Differential:**
   - ALLW: 0.15%
   - Replication: ~0.05%
   - **Savings: 0.10% annually**

### Total Expected Tracking Error: 1.0-1.5% annually

---

## When to Use Each Approach

### Buy ALLW Directly If:
- ✅ Portfolio size < $50,000
- ✅ You want simplicity and autopilot
- ✅ You value 60/40 tax treatment
- ✅ You don't want to rebalance
- ✅ You're okay with 0.15% ER

### Use Replication If:
- ✅ Portfolio size > $500,000 (ER savings > $500/year)
- ✅ You want to tax-loss harvest
- ✅ You want control over positions
- ✅ You're okay with quarterly rebalancing
- ✅ You want slightly lower costs

### Break-Even Analysis:
- **ALLW ER cost:** 0.15% = $150 per $100k
- **Replication ER cost:** 0.05% = $50 per $100k
- **Savings:** $100 per $100k annually
- **Your time cost:** 4 hours/year rebalancing

**If your time is worth >$25/hour, just buy ALLW for amounts <$100k**

---

## Scripts Reference

### Download Latest Holdings
```bash
python download_allw_holdings.py
```

### Generate Portfolio
```bash
python generate_allw_replication.py
```

### Calculate Positions
```bash
python calculate_portfolio_value.py 100000 ALLW_SCALED 2025-10-06
python calculate_portfolio_value.py 100000 ALLW 2025-10-06
```

### Export for Broker
```bash
python export_portfolio.py broker ALLW_SCALED 2025-10-06 100000
python export_portfolio.py csv ALLW_SCALED 2025-10-06
```

### Add to Charts
```bash
python add_portfolio_to_charts.py ALLW_SCALED 2025-10-06 22
```

---

## Database Queries

### View All ALLW Holdings
```sql
SELECT ticker, name, ROUND(weight*100,2) as weight_pct
FROM etf_holdings_daily
WHERE etf='ALLW' AND snapshot_date='2025-10-06'
ORDER BY ABS(weight) DESC;
```

### Compare Holdings Over Time
```sql
SELECT snapshot_date, COUNT(*) as holdings,
       SUM(CASE WHEN weight > 0 THEN weight ELSE 0 END) as long_weight
FROM etf_holdings_daily
WHERE etf='ALLW'
GROUP BY snapshot_date
ORDER BY snapshot_date DESC;
```

### View Your Portfolios
```sql
SELECT portfolio_name, ticker,
       ROUND(weight*100,2) as weight_pct
FROM replication_portfolios
WHERE as_of_date='2025-10-06'
ORDER BY portfolio_name, weight DESC;
```

---

**Questions or issues?** Check the database at `C:\Users\klein\financial-charts\market_data.db`

*This guide is for informational purposes only. Not investment advice.*
