# Chart API Reference

**ALWAYS use the charting app API. NEVER use matplotlib or other tools.**

## Critical Warning

> **NEVER overwrite existing chart files without asking first.**
>
> Before touching ANY existing chart:
> 1. **READ the existing image** to see what's there
> 2. **ASK the user** before making changes
>
> Existing charts may have levered benchmarks (e.g., SMH_1_44X), custom date ranges, or other carefully chosen parameters that are NOT obvious from the filename.

## Quick Start

```bash
# Start the app
cd /c/Users/klein/financial-charts && python charting_app/app.py

# Price comparison (normalized)
curl "http://localhost:5000/api/chart/lw?tickers=AAPL,QQQ&start=2020-01-01&normalize=true" \
  -o investing/attachments/aapl-vs-qqq.png

# Fundamentals (revenue + net income in separate panes)
curl "http://localhost:5000/api/chart/lw?tickers=AAPL&metrics=revenue,netincome" \
  -o investing/attachments/aapl-fundamentals.png
```

## API Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `tickers` | required | Comma-separated tickers |
| `start` | | Start date (YYYY-MM-DD) |
| `end` | | End date |
| `normalize` | false | Normalize to 100 at start |
| `primary` | | Actor ticker — always gets blue (#2962FF) |
| `metrics` | | Fundamentals: revenue, netincome, eps, fcf, operatingincome, ebitda, grossprofit |
| `forecast_start` | | Date to begin dotted forecast line |
| `labels` | | Custom legend labels (e.g., `SMH_1_44X:SMH%201.44x%20Lev`) |
| `sort_by_last` | false | Sort legend by final value, high→low |
| `show_title` | false | Don't use — legend suffices |
| `width` | 1200 | Image width |
| `height` | 800 | Image height |

## Product Metrics

For #product notes, use `product` and `product_metrics` instead of `tickers`:

```bash
curl "http://localhost:5000/api/chart/lw?product=TikTok&product_metrics=global_mau,revenue" \
  -o investing/attachments/tiktok-usage.png
```

Available: `global_mau`, `us_mau`, `dau`, `revenue`. Data must exist in `product_metrics` table.

## Chart Best Practices

**Prefer peer comparisons** — single-ticker charts waste the comparison opportunity. Include 2-4 relevant peers with `normalize=true`.

**No titles needed** — legend already shows tickers. Leave `show_title=false`.

**Naming convention:** `aapl-price-chart.png`, `tsmc-vs-samsung-foundry.png`, `nvda-2024-rally.png`

**Chart links:** Every embed needs an italicized line linking to *other* tickers shown:

```markdown
# On Apple note, showing AAPL vs QQQ:
![[aapl-vs-qqq.png]]
*vs [[Nasdaq|QQQ]]*
```

**Chart notes:** Add 1-2 sentence interpretation below charts (peaks, catalysts, current context).

---

## Before Creating Charts

### 1. Check if price data exists

```bash
sqlite3 market_data.db "PRAGMA table_info(stock_prices_daily);" | findstr /i "TICKER"
```

### 2. If missing, add it

```python
import yfinance as yf
import sqlite3
conn = sqlite3.connect('market_data.db')
ticker = 'TICKER'
t = yf.Ticker(ticker)
hist = t.history(period='max')

try:
    conn.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{ticker}" REAL')
except: pass

for date, row in hist.iterrows():
    date_str = date.strftime('%Y-%m-%d') + ' 00:00:00'
    conn.execute(f'UPDATE stock_prices_daily SET "{ticker}" = ? WHERE Date = ?',
                (row['Close'], date_str))
conn.commit()
```

### 3. Check if financials exist

```bash
sqlite3 market_data.db "SELECT COUNT(*) FROM income_statement_quarterly WHERE ticker='TICKER';"
```

### 4. If missing, fetch them

**Option A: fetch_fundamentals.py (US stocks)**
```bash
python fetch_fundamentals.py TICKER
```

**Option B: Manual backfill (international)**
```python
import sqlite3
conn = sqlite3.connect('market_data.db')
data = [('TICKER', '2024-12-31', 10000000000, 1000000000)]
for row in data:
    conn.execute('''INSERT OR REPLACE INTO income_statement_quarterly
        (ticker, fiscal_date_ending, total_revenue, net_income) VALUES (?, ?, ?, ?)''', row)
conn.commit()
```

### 5. Verify output

After generating, READ the image to confirm all tickers appear with visible data lines.

---

## Handling Losses in Fundamentals

Quarterly losses distort scale. NULL them out and note below chart:

```sql
UPDATE income_statement_quarterly SET net_income = NULL WHERE ticker = 'MSFT' AND net_income < 0;
```

```markdown
*Q2 2012 loss (-$492M, aQuantive writedown) excluded from chart.*
```

---

## Adding Forecasts

> **NEVER use WebFetch on Yahoo Finance analysis pages** — crashes session.
> Use Chrome browser automation tools (`mcp__claude-in-chrome__*`).

### Process

1. **Get estimates** from Yahoo Finance `/quote/TICKER/analysis/`:
   - Quarterly EPS (current + next quarter)
   - Annual revenue & EPS (current + next year)

2. **Yahoo fiscal year convention:** Labels by calendar year the FY ends in.
   - NVDA (FY ends Jan): "Next Year (2027)" = FY27 (Feb 2026 - Jan 2027)
   - AAPL (FY ends Sep): "Next Year (2026)" = FY26 (Oct 2025 - Sep 2026)

3. **Get shares outstanding:**
   ```sql
   sqlite3 market_data.db "SELECT shares_outstanding FROM company_overview WHERE ticker='AAPL';"
   ```

4. **Calculate net income from EPS:**
   - US stocks: `Net Income = EPS × shares_outstanding`
   - ADRs: `Net Income = (ADR_EPS / ADR_ratio) × FX_rate × shares_outstanding`

5. **Extrapolate quarters** using YoY growth (preserves seasonality):
   ```
   Q1_next = Q1_current × (FY_next / FY_current)
   ```

6. **Insert forecasts:**
   ```sql
   INSERT OR REPLACE INTO income_statement_quarterly
     (ticker, fiscal_date_ending, total_revenue, net_income)
   VALUES ('AAPL', '2026-12-31', 147400000000, 43200000000);
   ```

7. **Generate with forecast line:**
   ```bash
   curl "http://localhost:5000/api/chart/lw?tickers=AAPL&metrics=revenue,netincome&forecast_start=2025-10-01" \
     -o investing/attachments/aapl-fundamentals.png
   ```

   `forecast_start` = day after last actual quarter.

---

## Segment Charts

For granular segment-level data (Cloud margin, product mix, etc.), use the segment endpoint:

```bash
# Cloud margin trajectory
curl "http://localhost:5000/api/chart/segment?ticker=GOOGL&segments=cloud&metric=margin" \
  -o investing/attachments/goog-cloud-margin.png

# Cloud vs Services operating income
curl "http://localhost:5000/api/chart/segment?ticker=GOOGL&segments=cloud,services&metric=operating_income&chart_type=bar" \
  -o investing/attachments/goog-cloud-vs-services-opex.png

# Services product revenue mix
curl "http://localhost:5000/api/chart/segment?ticker=GOOGL&segments=search,youtube,network,subs&metric=revenue" \
  -o investing/attachments/goog-services-product-mix.png
```

| Parameter | Description |
|-----------|-------------|
| `ticker` | Required. Ticker symbol (e.g., GOOGL) |
| `segments` | Required. Comma-separated segments (e.g., cloud,services) |
| `metric` | Required. `revenue`, `operating_income`, or `margin` |
| `chart_type` | Optional. `line` (default) or `bar` |
| `width`, `height` | Optional. Image dimensions |

### Adding Segment Data

Data lives in `segment_quarterly` table (normalized format):

```sql
-- Schema
CREATE TABLE segment_quarterly (
    ticker TEXT,
    fiscal_date_ending TEXT,  -- YYYY-MM-DD
    segment TEXT,             -- cloud, services, search, youtube, etc.
    metric TEXT,              -- revenue, operating_income, margin
    value REAL,
    PRIMARY KEY (ticker, fiscal_date_ending, segment, metric)
);

-- Insert example
INSERT INTO segment_quarterly VALUES
('GOOGL', '2025-09-30', 'cloud', 'margin', 23.7),
('GOOGL', '2025-09-30', 'cloud', 'revenue', 15.2),
('GOOGL', '2025-09-30', 'cloud', 'operating_income', 3.6);
```

### Workflow

1. **Extract from 10-Q** using SEC filing script + Task agent
2. **Insert to database** using SQL inserts
3. **Generate charts** using segment endpoint
4. **Embed in notes** with interpretation captions
