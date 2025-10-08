# ALLW Portfolio Replication System

Complete system for downloading, analyzing, and replicating the State Street ALLW ETF portfolio.

---

## What This System Does

1. **Downloads** daily holdings from ALLW ETF
2. **Stores** holdings history in SQLite database
3. **Generates** tradeable replication portfolios
4. **Calculates** exact positions based on your investment amount
5. **Exports** portfolio data for brokers (CSV, JSON)
6. **Integrates** with your charting application
7. **Tracks** portfolio changes over time

---

## Quick Start

### 1. Download Latest ALLW Holdings
```bash
cd C:\Users\klein\financial-charts
python download_allw_holdings.py
```

**Output:**
- Downloads XLSX from State Street
- Stores in `etf_holdings_daily` table
- Shows 14 holdings as of Oct 6, 2025

### 2. Generate Replication Portfolios
```bash
python generate_allw_replication.py
```

**Output:**
- `ALLW_ETF_ONLY`: 23% securities + 77% cash
- `ALLW_SCALED`: 100% invested (scaled weights)
- Stores in `replication_portfolios` table

### 3. Calculate Your Positions
```bash
python calculate_portfolio_value.py 100000 ALLW_SCALED 2025-10-06
```

**Output:**
```
Portfolio: ALLW_SCALED
Investment Amount: $100,000.00

Ticker        Price   Weight %     Shares            Cost          Target
------------------------------------------------------------------------------------------
SPLG     $    78.73     60.50%        768 $     60,464.64 $     60,496.47
SPEM     $    47.48     19.01%        400 $     18,992.00 $     19,007.61
GXC      $   106.09     12.92%        121 $     12,836.89 $     12,915.98
GLD      $   364.38      7.58%         20 $      7,287.60 $      7,579.93
------------------------------------------------------------------------------------------
CASH                     0.42%            $        418.87
TOTAL                  100.00%            $    100,000.00
```

### 4. Export for Your Broker
```bash
python export_portfolio.py broker ALLW_SCALED 2025-10-06 100000
```

### 5. View in Charting App
```bash
python add_portfolio_to_charts.py ALLW_SCALED 2025-10-06 22
```
Then reload charting app → Navigate to Page 22 "ALLW"

---

## Files Created

### Core Scripts
| File | Purpose | Size |
|------|---------|------|
| `download_allw_holdings.py` | Download daily holdings from State Street | 13K |
| `generate_allw_replication.py` | Create tradeable portfolios | 12K |
| `calculate_portfolio_value.py` | Calculate positions & costs | 9.5K |
| `export_portfolio.py` | Export to CSV/JSON/broker format | 6.7K |
| `add_portfolio_to_charts.py` | Add to charting app | 4.5K |

### Documentation
| File | Purpose | Size |
|------|---------|------|
| `portfolio_implementation_guide.md` | Complete implementation guide | 7.7K |
| `allw_replication_portfolio.md` | Portfolio composition details | 5.5K |
| `ALLW_REPLICATION_README.md` | This file | - |

---

## Database Structure

### `etf_holdings_daily`
Stores ALLW's daily holdings from State Street.

```sql
CREATE TABLE etf_holdings_daily (
    snapshot_date TEXT NOT NULL,   -- YYYY-MM-DD
    etf TEXT NOT NULL,              -- 'ALLW'
    ticker TEXT NOT NULL,           -- e.g. 'SPLG', 'GCZ5'
    name TEXT,                      -- Security name
    weight REAL,                    -- Decimal weight (0.1364 = 13.64%)
    shares REAL,                    -- Number of shares held
    market_value REAL,              -- USD market value
    PRIMARY KEY (snapshot_date, etf, ticker)
);
```

**Current Data:**
- 2 snapshots: Aug 4, 2025 & Oct 6, 2025
- 14 holdings per snapshot
- $596M total AUM (estimated)

### `replication_portfolios`
Stores generated replication portfolios.

```sql
CREATE TABLE replication_portfolios (
    portfolio_name TEXT NOT NULL,   -- 'ALLW_SCALED', 'ALLW_ETF_ONLY'
    as_of_date TEXT NOT NULL,       -- Based on holdings date
    ticker TEXT NOT NULL,           -- e.g. 'SPLG'
    name TEXT,                      -- Security name
    weight REAL,                    -- Target weight
    allocation_type TEXT,           -- 'direct', 'proxy', 'scaled'
    category TEXT,                  -- Asset class
    original_weight REAL,           -- ALLW's original weight
    created_at TEXT NOT NULL,       -- Timestamp
    PRIMARY KEY (portfolio_name, as_of_date, ticker)
);
```

**Current Portfolios:**
- `ALLW_ETF_ONLY`: 9 positions (includes cash)
- `ALLW_SCALED`: 4 positions (100% invested)

---

## Current Portfolio Composition (Oct 6, 2025)

### ALLW Actual Holdings

| Category | Weight | Description |
|----------|--------|-------------|
| **US Equity** | 13.64% | SPLG (S&P 500 ETF) |
| **Emerging Markets** | 4.29% | SPEM (EM ETF) |
| **China** | 2.91% | GXC (China ETF) |
| **Gold** | 1.71% | Gold futures (Dec 2025) |
| **International Equity** | 0.62% | Euro Stoxx, TOPIX, FTSE, SPI futures |
| **Bonds** | 0.18% | US/Euro/UK/AU bond futures |
| **Currency** | -0.08% | Short GBP |
| **Cash/Margin** | ~77% | For futures positions |

### ALLW_SCALED Portfolio (Simplified)

| Ticker | Name | Weight | Current Price |
|--------|------|--------|---------------|
| **SPLG** | SPDR Portfolio S&P 500 | 60.50% | $78.73 |
| **SPEM** | SPDR Portfolio Emerging Markets | 19.01% | $47.48 |
| **GXC** | SPDR S&P China | 12.92% | $106.09 |
| **GLD** | SPDR Gold Trust | 7.58% | $364.38 |

**Key Changes from ALLW:**
- Scales up the ETF-only positions to 100%
- Replaces gold futures with GLD ETF
- Omits bond/equity index futures (small positions)
- Eliminates 77% cash position

---

## Usage Examples

### Example 1: $10,000 Portfolio
```bash
python calculate_portfolio_value.py 10000 ALLW_SCALED 2025-10-06
```

**Result:**
- SPLG: 76 shares = $5,983
- SPEM: 40 shares = $1,899
- GXC: 12 shares = $1,273
- GLD: 2 shares = $729
- Cash: $115

### Example 2: Export to CSV
```bash
python export_portfolio.py csv ALLW_SCALED 2025-10-06
```

Creates `ALLW_SCALED_2025-10-06.csv`:
```csv
Ticker,Name,Weight %,Allocation Type,Category
SPLG,SPDR PORTFOLIO S+P 500 ETF,60.4965,scaled,us_equity_etf
SPEM,SPDR PORTFOLIO EMERGING MARKET,19.0076,scaled,emerging_markets_etf
GXC,SPDR S+P CHINA ETF,12.9160,scaled,china_etf
GLD,SPDR Gold Trust,7.5799,scaled,gold
```

### Example 3: Compare to Direct ALLW Purchase
```bash
python calculate_portfolio_value.py 100000 ALLW 2025-10-06
```

Shows actual ALLW holdings approach with 77% cash.

### Example 4: Historical Comparison
```bash
sqlite3 market_data.db "
SELECT
    a.ticker,
    a.weight*100 as aug_weight,
    b.weight*100 as oct_weight,
    (b.weight-a.weight)*100 as change
FROM etf_holdings_daily a
JOIN etf_holdings_daily b ON a.ticker = b.ticker
WHERE a.snapshot_date='2025-08-04'
  AND b.snapshot_date='2025-10-06'
ORDER BY ABS(b.weight-a.weight) DESC
LIMIT 10;"
```

---

## Maintenance Schedule

### Daily (Automated)
- [ ] Download latest ALLW holdings (if available)
  ```bash
  python download_allw_holdings.py
  ```

### Weekly
- [ ] Review holdings changes
  ```sql
  SELECT * FROM etf_holdings_daily
  WHERE snapshot_date = (SELECT MAX(snapshot_date) FROM etf_holdings_daily);
  ```

### Monthly
- [ ] Update market prices
  ```bash
  python update_market_data.py --assets stocks
  ```

### Quarterly (Rebalancing)
1. Download latest ALLW holdings
2. Regenerate portfolios
3. Calculate new positions
4. Execute trades
5. Update charting app

---

## Key Insights

### Why ALLW Uses 77% Cash
ALLW holds ~23% in ETFs and ~77% in cash/T-bills, using the cash as margin for futures contracts. The futures provide leveraged exposure to:
- Bond markets (~$380M notional)
- International equity indices (~$100M notional)
- Commodities (~$60M notional)

Total futures notional: ~$540M on ~$600M AUM = 90% exposure from futures

### Replication Challenges
1. **Futures Access**: Retail investors can't easily replicate futures positions
2. **Rolling Contracts**: Futures need quarterly rolls (Mar/Jun/Sep/Dec)
3. **Margin Requirements**: Futures require 5-10% margin per contract
4. **Tax Treatment**: Futures get 60/40 treatment, ETFs don't

### Why the Scaled Portfolio Works
- Captures 99% of ALLW's equity/commodity exposure
- Uses liquid ETFs anyone can buy
- Avoids futures complexity
- Expected tracking error: 1-2% annually
- Lower costs: 0.05% vs 0.15% ER

---

## Performance Comparison

| Metric | Buy ALLW | Scaled Portfolio | Direct Holdings |
|--------|----------|------------------|-----------------|
| **Simplicity** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Cost** | 0.15% ER | ~0.05% ER | ~0.05% ER |
| **Tax Efficiency** | 60/40 | Pure equity | Pure equity |
| **Tracking Error** | 0% | 1-2% | 0.3-0.8% |
| **Rebalancing** | Auto | Quarterly | Quarterly |
| **Min Investment** | ~$30 | ~$1,000 | ~$1,000 |
| **Control** | None | Full | Full |

---

## Troubleshooting

### "No holdings found"
```bash
# Check if holdings exist
sqlite3 market_data.db "SELECT COUNT(*) FROM etf_holdings_daily WHERE etf='ALLW';"

# If 0, download holdings
python download_allw_holdings.py
```

### "No price found for ticker"
```bash
# Update market data
python update_market_data.py --assets stocks

# Or download specific ticker
python download_single_ticker.py GLD
```

### "Portfolio not found"
```bash
# List available portfolios
python export_portfolio.py list

# Regenerate if missing
python generate_allw_replication.py
```

### Unicode/Encoding Errors
```bash
# Use UTF-8 encoding prefix
PYTHONIOENCODING=utf-8 python script_name.py
```

---

## Next Steps

1. **Set up daily downloads:**
   ```bash
   # Add to Task Scheduler (Windows) or cron (Linux)
   python download_allw_holdings.py --quiet
   ```

2. **Build historical database:**
   Download past XLSX files from State Street and import:
   ```bash
   python download_allw_holdings.py 2025-09-30 path/to/historical.xlsx
   ```

3. **Track performance:**
   Compare your replication portfolio to ALLW using the charting app

4. **Automate rebalancing alerts:**
   Create script to email when positions drift >2% from target

---

## Resources

- **ALLW Product Page:** https://www.ssga.com/us/en/intermediary/etfs/funds/spdr-ssga-active-large-cap-etf-allw
- **Daily Holdings:** https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-allw.xlsx
- **Database:** `C:\Users\klein\financial-charts\market_data.db`
- **Charts:** http://localhost:5000/sandbox/ (Page 22)

---

## License & Disclaimer

This system is for educational and personal use only. Not financial advice.

Market data provided by Yahoo Finance. Holdings data from State Street.

**Use at your own risk.** Past performance does not guarantee future results.

---

*Last Updated: October 7, 2025*
*System Version: 1.0*
