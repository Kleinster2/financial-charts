---
name: earnings
description: "Full earnings ingestion pipeline for a ticker: check income_statement_quarterly/annual in market_data.db, find the latest quarterly results (SEC filings, press releases, StockAnalysis), INSERT the data with correct field conventions (GAAP diluted EPS, EBITDA as OI+D&A, all 15 columns), regenerate fundamentals/sankey/waterfall charts, and update actor + daily notes. Use this skill whenever the user mentions earnings, quarterly results, income statement data, inserting fundamentals, fixing EPS or financial data in the DB, or asks if a ticker's earnings are current. Also triggers on /earnings TICKER."
---

# Earnings Processing

Process earnings data for a ticker. Usage: `/earnings TICKER`

## Phase 1: Check Current State

1. Check what's already in the database:
   ```sql
   SELECT fiscal_date_ending, total_revenue/1e9 AS rev_bn, net_income/1e9 AS ni_bn
   FROM income_statement_quarterly WHERE ticker='TICKER'
   ORDER BY fiscal_date_ending DESC LIMIT 6;
   ```
2. Compare the latest `fiscal_date_ending` to the company's most recent earnings release
3. If the database is current, tell the user and stop — no work needed

### Understand existing field conventions

Before inserting anything, query the most recent row in full to understand how derived fields are mapped for this specific ticker. Different companies have different income statement structures, and the DB may store fields in non-obvious ways.

```sql
SELECT * FROM income_statement_quarterly WHERE ticker='TICKER'
ORDER BY fiscal_date_ending DESC LIMIT 1;
```

Check these specifically — they vary by company:
- **`operating_expenses`**: Does it store *total* OpEx or *below-gross-profit* OpEx (total minus COGS)? Compare against the source filing to understand the convention.
- **`selling_general_administrative`**: Does it store only G&A, or full SGA (Sales & Marketing + G&A)? Cross-check against the prior quarter's filing.
- **`eps`**: Is it populated or always 0.0? If 0.0, that's an Alpha Vantage gap — insert the real GAAP diluted EPS. Always use GAAP diluted EPS, never adjusted/non-GAAP EPS — adjusted figures vary by company and break comparability.
- **`ebitda`**: Always derive as Operating Income + D&A for the quarter being inserted. Never derive by subtracting other quarters' stored EBITDA from an annual total — the stored values may use different derivation methods, contaminating the result.

This step prevents silent data corruption. Inserting total OpEx ($11.7B) when the DB convention is below-GP OpEx ($5.6B) breaks the entire data series for that ticker.

### Check existing data quality

While analyzing the existing rows, scan for anomalies — unexpected jumps, sign changes, or values that don't reconcile with the annual total. If you spot inconsistencies, flag them in the output. This doesn't block the insert but the user needs to know.

## Phase 2: Find Latest Numbers

1. Search for the earnings release: `"TICKER earnings Q[N] [year]"`, `"TICKER quarterly results"`
2. Check SEC filings if needed: `python scripts/parse_sec_filing.py TICKER --save /tmp/ticker.txt`
   - Use a Task agent to extract revenue, net income, EPS, segment data from the filing
3. Capture:
   - Total revenue
   - Net income
   - EPS — **GAAP diluted** (not adjusted/non-GAAP). Adjusted EPS varies by company and breaks cross-ticker comparability.
   - Segment breakdown (revenue and operating income per segment)
   - Geographic breakdown if material
   - Forward guidance if provided
   - **All sub-line items**: R&D, SGA (or its components), D&A, interest expense, income tax expense. Press releases often have quarterly breakdowns that 10-K annual filings don't split per-quarter — use whichever source gives the most granular data.
   - **D&A sourcing priority**: Quarterly D&A often isn't in the 10-K. Check these sources in order: (1) earnings press release cash flow section, (2) earnings supplement, (3) derive from 10-Q comparisons (e.g., 9-month D&A minus 6-month D&A = Q3 D&A). Leaving D&A as NULL when it's findable is a quality failure.
4. **Verify currency** — match the reporting currency already in the database for that ticker

## Phase 3: Insert Data

1. Use `INSERT INTO` (plain INSERT) with correct schema and `YYYY-MM-DD` date format
2. If the data is from a press release (not final 10-Q/10-K), note it as preliminary
3. **Fill all 15 columns** — not just revenue and net income. Extract R&D, SGA, D&A, interest expense, income tax, and depreciation from the filing or press release. NULL fields that could have been populated are a quality failure.
4. Cross-verify every derived field against the prior quarter's DB value and its source filing to confirm the mapping is consistent
5. **EBITDA derivation**: Compute EBITDA as `operating_income + depreciation_amortization` for the quarter being inserted. Do NOT derive by subtracting stored quarterly EBITDA values from an annual total — stored values may use inconsistent derivation methods, producing wrong results

### Q4 special handling

When processing Q4 of a fiscal year:
- **Also insert the annual row** into `income_statement_annual` using full-year figures from the 10-K
- **Cross-verify Q4** by calculating `Q4 = Annual - (Q1 + Q2 + Q3)` from the DB. If all line items match the press release figures exactly, both the annual data and the existing quarterly data are confirmed correct. If they don't match, investigate before inserting.
- Check if the annual table already has the row before inserting

### Interest income vs expense

Some companies (e.g., Palantir, Berkshire) have net interest *income*, not expense. If the income statement shows interest income with no interest expense line, set `interest_expense` to 0 in the INSERT — don't store interest income as a negative expense.

## Phase 4: Regenerate Charts

1. Start the charting app: `cd /c/Users/klein/financial-charts && python charting_app/app.py`
   - On Windows/Git Bash, background `&` doesn't work. Run in foreground or use `app.test_client()` for verification.
2. Update price data: `python update_market_data.py --lookback 10 --assets stocks`
3. Regenerate the fundamentals chart:
   ```bash
   curl "http://localhost:5000/api/chart/lw?tickers=TICKER&metrics=revenue,netincome" \
     -o investing/attachments/ticker-fundamentals.png
   ```
4. Read the generated image to verify it looks correct
5. If a peer comparison chart exists for this ticker, regenerate that too

## Phase 5: Update Notes

1. **Actor note** (`investing/Actors/`):
   - Add earnings data under a `## Financials` or `## Recent earnings` section
   - Include key metrics, segment breakdown, guidance
   - Mark preliminary data so it can be replaced later
   - Add italicized interpretation below any charts
2. **Daily note** (`investing/Daily/YYYY-MM-DD.md`):
   - Add summary entry with key metrics and stock reaction
   - Create the daily note if it doesn't exist
3. **Entity linking**: wikilink every entity mentioned
4. **Compliance**: run `python scripts/check_note_compliance.py` on modified notes

## Rules

- **Never DELETE, UPDATE, or INSERT OR REPLACE** — use plain `INSERT INTO` only. `INSERT OR REPLACE` silently deletes the existing row first, which can mask duplicates and lose the `last_updated` timestamp. If a row already exists for that fiscal_date_ending, investigate why before inserting.
- **Verify currency** before inserting — mismatched currencies corrupt the dataset
- **Preliminary data is fine** — `fetch_fundamentals.py` will overwrite with final data later
- **Always extract segment data** — top-level numbers alone are insufficient
- **Charts must have data tables** — reader should see the numbers, not just the visualization
- **Cross-verify derived fields** — every calculated value (COGS, OpEx, SGA, EBITDA) must be checked against the existing DB convention for that ticker before inserting
