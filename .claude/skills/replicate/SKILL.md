---
name: replicate
description: Build ETF/fund replication analysis — map holdings to proxies, construct synthetic indices, generate comparison charts, update vault note
---

# ETF Replication Analysis

Build a replication of a multi-asset ETF or fund using tradeable proxies. Usage: `/replicate TICKER`

The goal is to decompose what an ETF actually holds and replicate its returns using liquid instruments the user could trade directly. This reveals hidden exposures, hedging gaps, and whether the fund's fee is justified.

## Phase 0: Reconnaissance

1. Check if a vault note exists for the ticker:
   ```bash
   python scripts/check_before_create.py "TICKER"
   ```
2. Read the existing note if found — look for: holdings data, allocation breakdowns, any prior replication work
3. Check what price data exists:
   ```sql
   SELECT COUNT(*), MIN(Date), MAX(Date) FROM stock_prices_daily WHERE "TICKER" IS NOT NULL;
   ```
   If missing, add it: `python scripts/add_ticker.py TICKER`
4. Search for holdings data:
   - Check vault for holdings snapshots (SSGA, iShares, Vanguard disclosure pages)
   - Web search: `"TICKER holdings" site:ssga.com OR site:ishares.com OR site:vanguard.com`
   - Check if the fund publishes daily holdings (many ETFs do via CSV/Excel on their website)
5. Determine fund characteristics:
   - **Levered or unlevered?** (leveraged funds need financing cost modeling)
   - **Futures-based or cash?** (futures funds have roll yield and collateral dynamics)
   - **Currency-hedged or unhedged?** (international bond ETFs vary — this matters hugely)
   - **Rebalancing frequency?** (daily ERC, quarterly, annual)

## Phase 1: Holdings Analysis & Proxy Mapping

1. Extract the fund's actual holdings into asset classes. Standard taxonomy:
   - Equities (US, Europe, Japan, EM, China, etc.)
   - Nominal bonds (US long, US intermediate, international)
   - Inflation-linked (TIPS, linkers)
   - Commodities (gold, broad, energy, agriculture)
   - Other (REITs, currencies, alternatives)

2. For each holding, identify the best tradeable proxy:

   **Proxy selection hierarchy** (prefer higher):
   1. Actual instrument if in DB (e.g., GC=F for gold futures)
   2. Direct ETF equivalent (e.g., TLT for US long bonds)
   3. Index + FX for unhedged international (e.g., IBGL.L + EURUSD=X for Euro-Bund)
   4. Broad category ETF as fallback (e.g., VGK for all European equities)

3. Build the holdings-to-proxy mapping table. Format for the vault note:

   ```markdown
   | Fund holding | Notional | ETF proxy | Futures proxy | Key mismatch |
   |---|---|---|---|---|
   | S&P 500 E-Mini | $XXM | SPY / SPLG | ES=F | Minimal |
   | Euro-Bund Future | $XXM | BNDX (hedged) | IBGL.L + EURUSD=X | Currency hedge |
   ```

4. Ensure all proxy tickers are in the database:
   ```bash
   python scripts/add_ticker.py PROXY1 PROXY2 PROXY3
   ```
   For international instruments not in the wide table, use yfinance directly:
   ```python
   import yfinance as yf
   df = yf.Ticker("^STOXX50E").history(start="2020-01-01", end="2026-12-31")
   ```
   Store to `prices_long` via `replication_utils.store_ticker()`.

## Phase 2: Build Replication Script

Create `scripts/create_TICKER_repl.py` following the established pattern. The script should use shared utilities from `scripts/replication_utils.py`:

```python
from replication_utils import (
    get_prices, compute_returns, build_index,
    interpolate_schedule, store_ticker
)
```

**Standard replication tiers** (build progressively):

### Tier 1: Static weights (simplest)
- Fixed asset class weights (from latest holdings)
- Map to broadest possible proxies (4-6 ETFs)
- Unlevered (1x)
- This is the baseline — shows how much a simple passive mix captures

### Tier 2: Dynamic weights + leverage
- Time-varying asset class weights (from allocation history or holdings snapshots)
- Add leverage modeling if the fund uses it
- Financing cost: `leverage * return - (leverage - 1) * daily_rate`
- Interpolate weights between known data points using `interpolate_schedule()`

### Tier 3: Granular proxies (optional, for levered/futures funds)
- Replace broad ETFs with closer instrument matches
- Use actual futures where available (ZB=F, GC=F, ES=F)
- Use local-currency bond ETFs + FX pairs for unhedged international bonds
- Geographic sub-weights within asset classes (e.g., Europe = STOXX50E 55% + FTSE 23% + AXJO 22%)

**Script structure:**
```python
def main():
    store = '--store' in sys.argv

    # 1. Get prices
    prices_df = get_prices(ALL_TICKERS, start_date=START_DATE)

    # 2. Compute returns
    returns = compute_returns(prices_df, ALL_TICKERS)
    dates = prices_df['Date'].values

    # 3. Get anchor price
    # (fetch actual fund price at base_date for initial_price)

    # 4. Build each tier
    tier1_vals = build_index(dates, returns, STATIC_WEIGHTS,
                             base_date=BASE_DATE, initial_price=anchor)
    tier2_vals = build_index(dates, returns, dynamic_weights,
                             leverage=lev_array, base_date=BASE_DATE,
                             initial_price=anchor)

    # 5. Store
    if store:
        store_ticker(result_df, 'Date', 'TICKER_REPL', 'TICKER_REPL',
                     'TICKER Static Replication')
        # ... repeat for each tier

    # 6. Print comparison
    # Show returns for fund vs each replication tier
```

Run with `--store` to persist: `python scripts/create_TICKER_repl.py --store`

## Phase 3: Generate Charts

Produce the standard 4-chart set. All charts go in `investing/attachments/`.

### Chart 1: Normalized comparison
Compare actual fund vs all replication tiers, normalized to 100 at inception.
```bash
curl -o "investing/attachments/TICKER-replication-comparison-chart.png" \
  "http://localhost:5000/api/chart/lw?tickers=TICKER,TICKER_REPL,TICKER_REPL_DYN&start=START&normalize=true&primary=TICKER"
```
If the chart server isn't running, use Flask test client or matplotlib directly.

### Chart 2: Rolling correlation (30-day)
Rolling correlation of each replication vs the actual fund. Use matplotlib:
```python
from replication_utils import rolling_correlation
corr_df = rolling_correlation(prices_df, 'TICKER', ['TICKER_REPL', 'TICKER_REPL_DYN'])
```
Save as `TICKER-rolling-correlation-chart.png`.

### Chart 3: Notional evolution (absolute $M)
Line chart of each asset class's notional exposure over time, plus NAV dashed line.
Only possible if NAV/AUM data is available. Save as `TICKER-notional-evolution-chart.png`.

### Chart 4: Allocation % over time
Line chart of each asset class as % of gross notional. This is always possible if weight history exists.
Save as `TICKER-notional-pct-chart.png`.

**Chart verification:** Always check file size (`wc -c`) — files under 1KB are errors, not PNGs.

## Phase 4: Update Vault Note

Add a `## Replication analysis` section to the fund's actor note with:

1. **Results table:**
   ```markdown
   | Method | Total return | vs TICKER | Notes |
   |--------|-------------|-----------|-------|
   | TICKER (actual) | +X.XX% | — | Reference |
   | Tier 1 (static 1x) | +X.XX% | X.XXpp | Baseline |
   | Tier 2 (dynamic + lev) | +X.XX% | X.XXpp | Time-varying weights |
   ```

2. **Holdings-to-proxy mapping table** (from Phase 1)

3. **Charts with captions:**
   ```markdown
   ![[TICKER-replication-comparison-chart.png]]
   *Normalized comparison of TICKER vs replication tiers since inception...*
   ```

4. **Gap analysis paragraph:** Explain what the residual is — rebalancing alpha, roll yield, instrument mismatch, currency effects, cash collateral yield. Quantify where possible using the progressive tier comparison (what each improvement closed).

## Phase 5: Compliance

1. Run compliance check:
   ```bash
   python scripts/check_note_compliance.py investing/Actors/TICKER.md
   ```
2. Create stubs for any dead links
3. Add daily note entry summarizing the replication work

## Rules

- **NEVER delete existing chart embeds** from the note — add new ones alongside
- **Always verify proxy data quality** before building — check for gaps, splits, dividend adjustments
- **Use `prices_long` (narrow format)** for storing synthetic tickers — the wide table is at column limit
- **Ticker naming convention:** `TICKER_REPL` (static), `TICKER_REPL_DYN` (dynamic), `TICKER_REPL_FUT` (futures proxy)
- **The residual is the insight.** A perfect replication is boring. The gap between replication and actual fund reveals what the manager is really doing — that's what belongs in the note.
- **Currency matters enormously.** Always check if the fund's international holdings are hedged or unhedged. Using BNDX (hedged) to proxy unhedged Euro-Bund futures can explain 3-5pp of tracking error in a year where EUR moves 6%.
- **Leverage cost = annual rate / 252 per day.** Use the fund's actual financing rate if disclosed, otherwise SOFR + spread (~4.8% as of 2026).
- **Shared utilities in `scripts/replication_utils.py`** — use them. Don't duplicate `build_index`, `compute_returns`, `store_ticker` in new scripts.
