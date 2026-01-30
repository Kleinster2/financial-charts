# Claude Code Instructions

This project is an integrated system: **database → charts → vault**.

- **Database** stores raw data (prices, financials, short interest)
- **Charts** visualize that data as rich expressions
- **Vault** (Obsidian notes at `investing/`) provides meaning, narrative, and theses

They are not separate concerns—they are one system.

---

## Git Workflow

**Main branch is protected** - all changes require a PR with passing CI.

### Making Changes

1. Run tests before committing:
   ```bash
   npm run test:unit      # 109 unit tests
   npm run test:smoke     # 6 Playwright tests
   ```

2. Create a feature branch and PR (never push directly to main):
   ```bash
   git checkout -b feature-name
   git add <files>
   git commit -m "Description"
   git push -u origin feature-name
   ```

3. Create PR using gh CLI:
   ```bash
   /c/Users/klein/Downloads/gh_2.80.0_windows_amd64/bin/gh.exe pr create --title "Title" --body "Description"
   ```

4. After PR is approved/merged:
   ```bash
   /c/Users/klein/Downloads/gh_2.80.0_windows_amd64/bin/gh.exe pr merge <number> --merge --delete-branch
   git checkout main
   git pull
   git fetch --prune
   ```

5. Clean stale local branches:
   ```bash
   git branch | grep -v main | xargs git branch -D
   ```

### Tool Error Recovery

**After Edit/Write tool errors, always check for unintended modifications:**
```bash
git status --short
```

Tool errors like "File has not been read yet" can indicate internal state issues that may cause:
- Partial writes to wrong files
- Truncated content
- Unintended modifications to other files

If you see unexpected modified files, compare line counts and restore if needed:
```bash
# Check if file was truncated
git show HEAD:"path/to/file.md" | wc -l  # committed version
wc -l "path/to/file.md"                   # working version

# Restore if damaged
git restore "path/to/file.md"
```

## Tools

- **gh CLI**: `/c/Users/klein/Downloads/gh_2.80.0_windows_amd64/bin/gh.exe`
- **Playwright**: `npx playwright install chromium` (first-time setup)

## Key Locations

### App

- **Dashboard features**: `charting_sandbox/chart-dashboard.js`
- **Backend API**: `charting_app/app.py`
- **Unit tests**: `tests/unit/`
- **Smoke tests**: `tests/playwright/`

### Vault

- **Vault root**: `investing/`
- **Actors**: `investing/Actors/` (companies, orgs, people, geographies)
- **Concepts**: `investing/Concepts/` (ideas, dynamics, phenomena)
- **Events**: `investing/Events/` (discrete happenings)
- **Theses**: `investing/Theses/` (investment theses)
- **Daily notes**: `investing/Daily/` (inbox, changelog)
- **Sectors**: `investing/Sectors/` (industry hubs)

**DEPRECATED**: The old "My Vault" at `C:\Users\klein\onedrive\pictures\documents\my vault` is deprecated.

## Cache Busting

After modifying JS files, increment `?v=` in `charting_sandbox/index.html`.

## Database Maintenance

### Date format in `stock_prices_daily`

All dates in `stock_prices_daily` (and `stock_volumes_daily`) use the format `'YYYY-MM-DD HH:MM:SS'` (e.g., `'2020-01-02 00:00:00'`). **Never insert dates in date-only format** (e.g., `'2020-01-02'`).

SQLite treats these as different strings, so mixing formats creates silent duplicate rows — one with data, one with NULLs. The integrity check in `download_all_assets.py` will then block all future updates.

If this happens again, clean up with:
```sql
-- Delete NULL date-only duplicates
DELETE FROM stock_prices_daily
WHERE Date NOT LIKE '%00:00:00'
AND (Date || ' 00:00:00') IN (SELECT Date FROM stock_prices_daily WHERE Date LIKE '%00:00:00');

-- Convert any remaining date-only rows
UPDATE stock_prices_daily SET Date = Date || ' 00:00:00' WHERE Date NOT LIKE '%00:00:00';
```

### Updating prices

```bash
# Daily update (all price assets, last 10 days)
python update_market_data.py --lookback 10 --assets stocks etfs mutualfunds adrs fx crypto futures iv
```

Delisted ticker warnings (YFPricesMissingError, YFTzMissingError) are expected and harmless — the NaN-skip in the merge logic prevents them from corrupting historical data.

### Delisted tickers

**Never remove historical data for delisted tickers.** Acquisitions, bankruptcies, and delistings happen — the historical price data remains valuable for analysis and charting. When a ticker stops updating (e.g., HOUS acquired by Compass Jan 2026), the column stays in the database with data through its final trading day.

## Generating Charts for the Vault

**ALWAYS use the charting app API. NEVER use matplotlib or other tools.**

> **🚨 CRITICAL: NEVER overwrite existing chart files without asking first.**
>
> Before touching ANY existing chart:
> 1. **READ the existing image** to see what's there
> 2. **ASK the user** before making changes
>
> Existing charts may have levered benchmarks (e.g., SMH_1_44X), custom date ranges, or other carefully chosen parameters that are NOT obvious from the filename. Overwriting destroys this work.
>
> **No exceptions. Always ask.**

### Headless export via API (preferred)

```bash
# Start the app
cd /c/Users/klein/financial-charts && python charting_app/app.py

# Single ticker
curl "http://localhost:5000/api/chart/lw?tickers=AAPL&start=2020-01-01" \
  -o investing/attachments/aapl-price-chart.png

# Comparison (normalized)
curl "http://localhost:5000/api/chart/lw?tickers=AAPL,QQQ&start=2020-01-01&normalize=true" \
  -o investing/attachments/aapl-vs-qqq.png

# Fundamentals (standard: revenue + net income in separate panes)
curl "http://localhost:5000/api/chart/lw?tickers=AAPL&metrics=revenue,netincome" \
  -o investing/attachments/aapl-fundamentals.png
```

**Fundamentals charts use separate panes** when multiple metrics are requested. Revenue and net income have different scales (revenue always positive and large, net income can be negative and smaller), so they render in stacked panes with independent Y-axes. This is automatic — just include both metrics.

**API parameters:** `tickers` (required for stocks), `start`, `end`, `title`, `width` (1200), `height` (800), `show_title` (false — legend already shows ticker), `normalize` (false), `metrics` (revenue, netincome, eps, fcf, operatingincome, ebitda, grossprofit), `forecast_start` (date to begin dotted forecast line), `labels` (custom legend labels, e.g., `labels=SMH_1_44X:SMH%201.44x%20Lev`), `sort_by_last` (sort legend by final value, high→low), `primary` (actor ticker — always gets first color, blue #2962FF)

**Product metrics (for #product notes):** Use `product` and `product_metrics` instead of `tickers`:
```bash
# TikTok usage chart (MAU + revenue in separate panes)
curl "http://localhost:5000/api/chart/lw?product=TikTok&product_metrics=global_mau,revenue" \
  -o investing/attachments/tiktok-usage.png
```
Available product_metrics: `global_mau`, `us_mau`, `dau`, `revenue`. Data must be added to `product_metrics` table first via deep research.

**Naming:** `aapl-price-chart.png`, `tsmc-vs-samsung-foundry.png`, `nvda-2024-rally.png`

**Chart links:** Every chart embed must have an italicized line below it linking to the *other* tickers shown — never link the note you're currently in:

```markdown
# On the Apple note, showing AAPL vs QQQ:
![[aapl-vs-qqq.png]]
*vs [[Nasdaq|QQQ]]*

# On a concept note showing both:
![[aapl-vs-qqq.png]]
*[[Apple]] · [[Nasdaq|QQQ]]*
```

**Prefer peer comparisons over single-ticker charts.** A chart showing just one ticker wastes the comparison opportunity. Include 2-4 relevant peers so readers see relative performance. Use `normalize=true` for comparisons.

```bash
# Good: TSMC vs Samsung foundry comparison
curl "http://localhost:5000/api/chart/lw?tickers=TSM,005930.KS&normalize=true&start=2020-01-01&show_title=false"

# Bad: Just TSMC alone (redundant - legend already shows ticker)
curl "http://localhost:5000/api/chart/lw?tickers=TSM&start=2020-01-01"
```

For comparison charts, add link line below pointing to the *other* tickers (not the note you're on).

**Before creating charts, ensure price data exists.** Check the database for all tickers you plan to chart:
```bash
sqlite3 market_data.db "PRAGMA table_info(stock_prices_daily);" | grep -iE "AAPL|MSFT|etc"
```

If missing, add them BEFORE generating the chart:
```python
import yfinance as yf
import sqlite3
conn = sqlite3.connect('market_data.db')
for ticker in ['BCS', 'LYG']:
    t = yf.Ticker(ticker)
    hist = t.history(period='max')
    try:
        conn.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{ticker}" REAL')
    except: pass  # column exists
    for date, row in hist.iterrows():
        date_str = date.strftime('%Y-%m-%d') + ' 00:00:00'
        conn.execute(f'UPDATE stock_prices_daily SET "{ticker}" = ? WHERE Date = ?',
                    (row['Close'], date_str))
    conn.commit()
```

**Always verify chart output.** After generating a chart, READ the image file to confirm:
1. All requested tickers appear in the legend
2. All tickers have visible data lines (not missing/flat)
3. The narrative in your chart note matches what the chart actually shows

**Chart notes:** Always add an italicized interpretive note below charts explaining what the reader is seeing. Charts without context are just shapes — the interpretation is what makes them useful.

```markdown
![[stne-price-chart.png]]
*Peaked ~$90 in 2021 fintech boom, crashed to ~$8 in 2022 on Brazil macro + Linx issues, now recovering ~$12-14.*
```

Good chart notes include:
- Key inflection points (peaks, troughs, breakouts)
- What caused major moves (earnings, macro, sector rotation)
- Current context (where it sits now relative to history)

Keep notes concise (1-2 sentences). The goal is orientation, not analysis.

### Handling losses in fundamentals charts

Quarterly losses distort chart scale. **Always NULL them out and add a note below the chart:**

```sql
UPDATE income_statement_quarterly SET net_income = NULL WHERE ticker = 'MSFT' AND net_income < 0;
```

Then add italicized note below the chart in the note:
```
*Q2 2012 loss (-$492M, aQuantive writedown) excluded from chart.*
```

### Adding forecasts to fundamentals charts

> **⚠️ NEVER use WebFetch on Yahoo Finance analysis pages.**
> `WebFetch("https://finance.yahoo.com/quote/TICKER/analysis/")` crashes the session.
> **Use Chrome browser automation tools instead** (`mcp__claude-in-chrome__*`).

**1. Get consensus estimates** from Yahoo Finance (`/quote/TICKER/analysis/`). You need:
- Quarterly EPS estimates (current + next quarter)
- Annual revenue estimates (current + next year)
- Annual EPS estimates (current + next year)

> **Yahoo uses fiscal years, labeled by the calendar year the fiscal year ends in.**
> - "Current Year (2026)" = fiscal year ending in 2026
> - "Next Year (2027)" = fiscal year ending in 2027
>
> For NVDA (FY ends Jan): "Next Year (2027)" = FY27 (Feb 2026 - Jan 2027)
> For AAPL (FY ends Sep): "Next Year (2026)" = FY26 (Oct 2025 - Sep 2026)
>
> Yahoo only shows 2 fiscal years. To extend coverage, extrapolate additional years using YoY growth.

**2. Get shares outstanding:**
```sql
sqlite3 market_data.db "SELECT shares_outstanding FROM company_overview WHERE ticker='AAPL';"
```

**3. Calculate net income from EPS:**

For US stocks:
```
Net Income = EPS × shares_outstanding
```

For ADRs (e.g., TSM where 1 ADR = 5 Taiwan shares):
```
Net Income = (ADR_EPS / ADR_ratio) × FX_rate × shares_outstanding
Example: ($3.29 / 5) × 31.6 TWD/USD × 25.94B shares = NT$539B
```

**4. Extrapolate future quarters** using YoY growth (preserves seasonality + trend):

Calculate separate growth rates for revenue and net income:
```
Revenue growth = FY_next_revenue / FY_current_revenue
NI growth = FY_next_EPS / FY_current_EPS
```

Apply to each quarter from the prior year:
```
Q1_next = Q1_current × growth_rate
Q2_next = Q2_current × growth_rate
...
```

**Verify totals match annual estimates** before inserting.

**5. Insert forecasts into database:**
```sql
sqlite3 market_data.db "
INSERT OR REPLACE INTO income_statement_quarterly
  (ticker, fiscal_date_ending, total_revenue, net_income)
VALUES
  ('AAPL', '2026-12-31', 147400000000, 43200000000),
  ('AAPL', '2027-03-31', 111700000000, 30000000000);
"
```

**6. Generate chart with dotted forecast line:**
```bash
curl "http://localhost:5000/api/chart/lw?tickers=AAPL&metrics=revenue,netincome&forecast_start=2025-10-01" \
  -o investing/attachments/aapl-fundamentals.png
```

Note: `forecast_start` should be the day after the last actual quarter (e.g., 2025-10-01 if last actual is 2025-09-30).

## Pending Design Decisions

### Short interest charting integration

**Status:** Database, API, and **dashboard columns complete**. Chart overlay pending.

**Dashboard:** SI %, Days to Cover, SI Shares columns added to data dashboard (sortable, filterable).

**Remaining (for charting on price charts):**
- **A) Synthetic tickers** — `AAPL_SI_PCT`, `AAPL_SI_DAYS` for charting
- **B) Separate chart overlay** — New UI component

### Obsidian chart refresh plugin

**Status:** Planned. See `docs/obsidian-chart-refresh-plugin.md` for full spec.

**Problem:** Charts are static PNGs that become stale. Manual refresh via curl is tedious.

**Solution:** Custom Obsidian plugin that refreshes chart images on note open.

**Key decisions needed:**
- **Filename vs frontmatter** for chart params mapping
- **Auto-advance forecast_start?** As time passes

**Estimate:** ~150-200 lines TypeScript, 2-4 hours.

---

## Before creating public company notes

**Do this BEFORE writing the note — not after.**

### 1. Check if price data exists

```bash
sqlite3 market_data.db "PRAGMA table_info(stock_prices_daily);" | findstr /i "TICKER"
```

### 2. If ticker missing, add it

```python
import yfinance as yf
import sqlite3

conn = sqlite3.connect('market_data.db')
ticker = 'TICKER'
t = yf.Ticker(ticker)
hist = t.history(period='max')

try:
    conn.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{ticker}" REAL')
except: pass  # column exists

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

### 4. If financials missing, fetch them

**Option A: Use fetch_fundamentals.py (preferred for US stocks)**

```bash
# Fetch fundamentals via Alpha Vantage API
python fetch_fundamentals.py TICKER

# Check freshness status
python fetch_fundamentals.py --status
```

**Option B: Manual backfill (for international stocks not on Alpha Vantage)**

Search web for quarterly revenue/net income data (macrotrends, SimplyWallSt, stockanalysis.com), then:

```python
import sqlite3
conn = sqlite3.connect('market_data.db')

# Example: (ticker, date, revenue, net_income)
data = [
    ('TICKER', '2024-12-31', 10000000000, 1000000000),
    # ... more quarters
]

for row in data:
    conn.execute('''
        INSERT OR REPLACE INTO income_statement_quarterly 
        (ticker, fiscal_date_ending, total_revenue, net_income)
        VALUES (?, ?, ?, ?)
    ''', row)
conn.commit()
```

### 5. Generate charts BEFORE creating note

```bash
# Start charting app
cd /c/Users/klein/financial-charts && python charting_app/app.py

# Price chart with peers
curl "http://localhost:5000/api/chart/lw?tickers=TICKER,PEER1,BENCHMARK&normalize=true&primary=TICKER&start=2020-01-01" \
  -o investing/attachments/ticker-price-chart.png

# Fundamentals chart
curl "http://localhost:5000/api/chart/lw?tickers=TICKER&metrics=revenue,netincome&start=2015-01-01" \
  -o investing/attachments/ticker-fundamentals.png
```

### 6. Verify charts rendered correctly

Read the generated images to confirm all tickers appear and have data.

**Never add "charts omitted" disclaimers.** Either:
- Do the work to add data and generate charts, OR
- Create an explicit TODO with timeline (and actually do it)

Notes should be complete on creation, not patched later.

---

## Actor note completion checklist

**Run this before marking any public actor note "done" (companies AND ETFs):**

### Currency (MUST DO FIRST)
- [ ] **Web search for recent news** before reviewing note content
- [ ] Key facts reflect current state (not stale by weeks/months)
- [ ] Major developments since last update are captured
- [ ] Numbers are latest available (MAU, revenue, valuations, ownership stakes)

### Specificity
- [ ] **No lazy shorthand** — "American-owned" unacceptable without: who owns what %, board composition, economic rights vs equity, operational control
- [ ] Ownership changes include: exact stakes, governance, economic rights (may differ from equity), retained rights, compliance concerns
- [ ] Revenue/valuation claims have exact figures, not "significant" or "major"
- [ ] Partnerships/deals specify: terms, duration, exclusivity, economics

See [[Note structures#Currency and specificity]] for full requirements.

### Leadership (companies only)
- [ ] Leadership section exists with table format
- [ ] CEO and CFO included (CFO for public/PE-backed)
- [ ] Board members with notable affiliations (PE sponsors, major investors)
- [ ] Executives wikilinked if they have own notes or cross-vault affiliations
- [ ] Brief backgrounds: years experience, prior roles, education if notable

### Charts
- [ ] Price chart exists (all public instruments need one)
- [ ] Price chart uses `primary=TICKER` (actor is always blue)
- [ ] Price chart has actor + peers/benchmark (companies: actor + peers + sector ETF; ETFs: vs SPY or parent index)
- [ ] Fundamentals chart exists (companies only, not ETFs)
- [ ] Read the generated images to verify they rendered correctly
- [ ] Chart captions mention all tickers shown
- [ ] **Research major moves before explaining them** — don't fabricate explanations for outperformance/underperformance; web search the actual causes (earnings, macro, sector events)
- [ ] **Link chart captions to vault notes** — when explaining moves, link to relevant actors/concepts in the vault; flag gaps if key topics lack notes

### Links
- [ ] Every company/person/product in tables is `[[wikilinked]]`
- [ ] Every company/person/product in body text is `[[wikilinked]]`
- [ ] Related section includes all entities linked in the note

### Quick link audit
```bash
# Find potential unlinked entities (capitalized words not in wikilinks)
grep -oE '\b[A-Z][a-z]+\b' note.md | sort -u
```

Compare against wikilinks in the note. If a proper noun appears without `[[brackets]]`, fix it.

### Automated compliance check

**REQUIRED:** After creating or modifying any actor note, run the compliance checker and fix all errors before marking the note complete:

```bash
python scripts/check_note_compliance.py investing/Actors/NewNote.md
```

**Workflow:**
1. **Web search first** — verify note reflects current reality
2. Update any stale content with specificity (no lazy shorthand)
3. Create/modify the note
4. Run the checker
5. Fix any errors (red)
6. Address warnings if reasonable (yellow)
7. Only then mark the note complete

**What it checks (automated):**
- Dead links (wikilinks to non-existent notes)
- Missing price charts (public companies and ETFs)
- Missing fundamentals charts (companies only)
- Missing chart captions
- Missing Related section
- Missing Quick stats section
- Missing historical financials (10-year for public companies)
- Missing cap table (private companies)

**What it does NOT check (manual):**
- Currency — is the note up to date?
- Specificity — are claims drilled with real detail?
- These must be verified via web search BEFORE running the checker.

**Exit codes:** 0 = pass (warnings OK), 1 = errors found

---

# Vault Guidelines

## Philosophy

- **Atomic notes** — one idea per note, no mega-documents
- **Self-contained** — each note tells its complete story; links are for depth, not basic comprehension
- **Links over hierarchy** — structure emerges from `[[connections]]`, not folders
- **Organic at the bottom, deliberate at the top** — actors/concepts grow organically; sector hubs are deliberate scaffolding
- **Daily notes as inbox** — capture first, extract atomic notes when ideas mature

## Self-contained notes

**A reader should understand the full story without clicking any links.**

| Wrong | Right |
|-------|-------|
| "The $5B debt came from [[Saks-Neiman merger]]" | "In late 2024, Baker orchestrated a $2.7B acquisition of Neiman that loaded $5B in debt..." then link for details |
| "[[Richard Baker]] was replaced as CEO" | "Richard Baker—real estate investor who built Saks through acquisitions—was replaced as CEO" then link for history |

**Repetition is acceptable** when needed for comprehension. Each note should stand alone.

## Numbers matter

**Never overlook hard data.** Capture financial metrics, operational data, comparisons, source and date.

**Bad:** "TSMC's US fabs have lower margins"
**Good:** "Taiwan 62% gross margin vs US 8%, depreciation +386%, labor +100% (SemiAnalysis, Nov 2025)"

## Charts and images

When the user shares images: (1) confirm you see them, (2) extract key data points, (3) add data to relevant notes.

**Saving images:** Find in `~/.claude/image-cache/`, copy to `investing/attachments/`, embed with `![[name.png]]`.

## Author framing matters

Capture the thesis, not just data. Note hedging language. Don't assume causation. Capture the author's interpretation.

## Dating investment calls

**Always include dates on positioning.** Calls go stale. Include date in section header, source attribution, note if position changed.

## When creating notes

- **Always do deep research** before creating — web search, multiple sources, hard data
- **If it's mentioned, it's linked** — every company, person, investor, or concept gets a `[[wikilink]]`. In intros, tables, body text, everywhere. No exceptions.
- **No thin stubs** — if no time to research, add to daily note instead

See [[Note structures]] for actor requirements, templates, and linking rules.

### "What makes X, X" analysis

Go beyond facts to explain why something works: flywheel, moats, structural advantage, the math.

## When editing existing notes

**Every edit is an opportunity to rebuild.** Check for: thin stubs, missing financials/cap tables, outdated data, no Related section. Make the requested edit first, then assess quality gaps.

**Deep research for updates:** Before updating any note, do web searches to:
1. Find recent news/developments (last 6-12 months)
2. Verify existing data is current (AUM, valuations, financials, status)
3. Discover new information to add — not just links

Don't just add a wikilink and move on. If you're touching a note, refresh it.

**Quality check:** Whenever you read any actor note (whether asked to or encountered during other work), check it against [[Note structures]] depth standards. Flag gaps proactively — especially private companies: full cap table, historical financials, derivative arrangements.

## Processing new information

**Every piece of news needs an atomic home — daily notes are never the only location.**

**Principle:** If information is worth putting in the daily note, it belongs in at least one permanent note (actor, concept, event). The daily note is a log and index — it can summarize and reference, but should never be the sole repository for any substantive information. When processing news or transcripts, update permanent notes FIRST, then summarize in daily note.

1. **Check existing notes first** — search vault before web
2. **Find the right home** — actors taking actions, not catch-all concepts
3. **Regional actors stay high-level** — specific news goes on specific actors
4. **Always update daily notes** — use event date, not article date
5. **Check for events** — M&A, bankruptcy, IPO → create Event note
6. **Recognize systemic events** — see below

See [[Note structures]] for event criteria and templates.

### Systemic vs company-specific news

**If a single event affects multiple actors, create a Concept or Event note FIRST.**

| Signal | Action |
|--------|--------|
| Same news hits 2+ companies | Create concept/event note first |
| Policy/regulatory change | Concept note for the policy |
| Sector-wide selloff | Concept note for the catalyst |
| Macro event (rates, tariffs) | Concept note |

**Then** update actor notes to:
- Link to the concept for systemic context
- Focus only on company-specific impact

**Wrong:** Repeat the same policy explanation in UNH, HUM, CVS notes.
**Right:** Create [[Medicare Advantage]] concept, actor notes link to it.

Actor notes should answer "how does this affect THIS company specifically?" — not re-explain what happened to the whole sector.

## Conventions

See [[Thesis conventions]] for thesis naming. See [[Taxonomy discussion]] for hashtag structure.

## Daily note structure

See [[Note structures]] for the standard daily note template. **Vault activity is mandatory** — journal all note creation/modification.

## Research workflow

1. **Company filings first** — 10-Ks, 10-Qs, 8-Ks, proxy statements are the authoritative source for financials, headcount, segment data, risk factors. Use SEC EDGAR or investor relations pages.
2. **Web search** for major news
3. **X/Twitter lists** for commentary (Chips & Semiconductors, AI Infrastructure, SemiAnalysis)
4. Add findings to daily note first, extract to actor/concept notes if substantial

### Sourcing standards

**Prefer official sources for hard data:**

| Data type | Primary source | Fallback |
|-----------|----------------|----------|
| Revenue, Net Income, EPS | 10-K, 10-Q | Earnings releases |
| Employee headcount | 10-K (annual), proxy | News articles (flag as estimate) |
| Segment breakdown | 10-K, 10-Q | Investor presentations |
| Guidance | Earnings calls, 8-K | News coverage |
| Ownership/cap table | Proxy (DEF 14A), 13-F | News (flag as estimate) |

**When using non-filing sources**, note it: "~210k employees (company website, Jan 2026)" or "estimated from news reports."

**SEC EDGAR shortcuts:**
- All filings: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TICKER&type=10-K`
- Recent 10-K: search `"[company] 10-K 2024 filetype:pdf"`
- Earnings call transcripts: Seeking Alpha, Motley Fool, or company IR page

### Daily news search checklist

When user asks for "today's news", cover these categories:

**CRITICAL: Use exact date format.** `"January 27 2026"` not `"January 2026"`. Month-only queries return the month's biggest stories (e.g., CES), not today's news.

| Category | Search terms |
|----------|--------------|
| **Market movers** | "biggest stock gainers losers [exact date]" |
| **Markets** | "stock market news [exact date]" |
| **USD/FX** | "US dollar DXY [exact date]" |
| **Treasuries** | "treasury yields bonds [exact date]" |
| **Commodities** | "gold oil copper prices [exact date]" |
| **Semiconductors** | "semiconductor chip news [exact date]" |
| **AI/Tech** | "AI news [exact date]" |
| **China macro** | "China economy news [exact date]" |
| **China tech** | "China tech news [exact date]" |
| **Fed/Rates** | "Federal Reserve news [exact date]" |
| **Energy/Nuclear** | "energy power grid news [exact date]" |
| **Robotics** | "robotics humanoid news [exact date]" |
| **Japan tech** | "Japan semiconductor news [exact date]" |
| **Korea semis** | "Korea semiconductor memory news [exact date]" |
| **Trade/Tariffs** | "tariffs trade war news [exact date]" |
| **Europe** | "Europe tech news [exact date]" |
| **Earnings** | Check calendar for major reports |

**Market movers catch what categories miss.** Corning +16.6% on Meta deal wouldn't appear in "semiconductor" or "AI" searches — but it's a top mover.

**Don't miss:** China domestic news (GDP, [[NDRC]], stimulus, regulatory) — often absent from US-focused searches.

### Verify before reporting

**Summary articles recycle recent news as "context."** A search for "AI news January 27" often returns roundups that mention December deals as background. This pollutes results with stale news presented as current.

**For any major deal, acquisition, or announcement mentioned:**
1. Search `"[company] [deal] announcement date"` to verify when it actually happened
2. If older than 3 days, classify as "Recent" not "Today"

**Present news in two sections:**

| Section | Criteria |
|---------|----------|
| **Confirmed Today** | Verified same-day (earnings, FOMC, policy, stock moves with %) |
| **Recent (Not Today)** | Mentioned in today's articles but announced earlier — include actual date |

**High-confidence "today" signals:**
- Earnings reports (scheduled dates)
- FOMC meetings (Fed calendar)
- Policy announcements with effective dates
- Stock moves with real-time % changes

**Red flags for recycled news:**
- Acquisitions/deals (often announced weeks ago)
- "Landmark" or "historic" framing (journalists rehash for context)
- Round-number valuations without transaction details

### Follow up on big movers

**Any stock move >10% needs a "why" search.** Don't just list the ticker and percentage.

For each major mover:
1. Search `"[ticker] stock why up/down [date]"`
2. Identify the catalyst (earnings, deal, upgrade, macro)
3. Include in report with context

Big moves often reveal deals/news that category searches miss (e.g., Corning +17% on Meta fiber deal wouldn't appear in "semiconductor" or "AI" searches).

### Earnings searches need multiple queries

**General news searches miss forward guidance.** A search for "[company] news [date]" returns headline results focused on:
- EPS beat/miss
- Revenue beat/miss
- Dramatic capex changes

But **forward guidance** (Q1 revenue outlook, full-year EPS estimates) often doesn't make headlines and requires a targeted search:

```
"[company] Q1 2026 revenue guidance"
"[company] earnings outlook guidance"
"[company] Q1 forecast"
```

**For any earnings report, run two searches:**
1. General: `"[company] earnings [date]"` — gets headline results
2. Guidance: `"[company] Q1/FY guidance [date]"` — gets forward estimates

Forward guidance often moves stocks more than backward-looking beats, so don't miss it.

## Key actors to track

The vault covers investing broadly. Key focus areas:

- **AI stack** — chips, infrastructure, hyperscalers, AI labs, applications
- **Semiconductors** — foundry, memory, equipment, fabless
- **Robotics** — humanoids, automation, manufacturing
- **China** — tech decoupling, industrial policy, geopolitics
- **Energy** — power demand, grid, renewables, nuclear
- **Manufacturing** — reshoring, industrial policy

Plus macro, rates, media, and wherever there's signal.

## Note decisions

- **Major standalone topic** → new atomic note
- **Update to existing actor/concept** → add section
- **Incremental news** → daily note only

### Frame notes for intrinsic value

Don't frame around what triggered creation. Notes should explain why the topic matters on its own terms.

### Check for intermediate levels

Before linking specific → general, check for intermediates. See [[Linking and hierarchy]] for patterns.

## Events vs Actor sections

**Prefer Event notes for corporate events.** Events are atomic — specific time, specific actors, own narrative.

See [[Note structures]] for when to create events and the event template.

## Folder and hierarchy

See [[Linking and hierarchy]] for folder structure, Concept vs Sector criteria, and Sub-sector/Sister Concept patterns.

## Before creating files

### CRITICAL: Always verify before creating

**Every time you propose creating actors, you MUST first check if they already exist.**

```bash
cd /c/Users/klein/financial-charts/investing && git ls-files "Actors/*.md" | sed 's|.*/||; s|\.md$||' | grep -iE "name1|name2|name3"
```

Use broad patterns (abbreviations, tickers, variants). Explicitly state result for each:
```
Honeywell  — NOT FOUND (safe to create)
NVIDIA     — EXISTS (do not create)
```

**WARNING:** Do NOT use `xargs basename -a` — corrupts filenames with spaces.

### After creating/updating notes

1. **Journal** — update today's daily note Vault activity
2. **Link mentions** — search vault, convert to `[[wikilinks]]`
3. **Add backlinks** — update Related sections of connected notes

## Actor conventions

### Actors don't need to be investable

Track policy-makers, private companies, geographies, individuals — anyone affecting investment outcomes.

### Regional actors stay high-level

Geographic actors are scaffolding, not repositories. Specific news → specific actors. Regional notes link to those actors.

### Concepts don't need theses

Concepts capture knowledge, not just trade ideas. If you'd reference it from multiple notes, it deserves a concept note.

### Financials and cap tables

- **Public companies**: Historical financials (see [[Financials templates]])
- **Private companies**: Full historical cap table (founding → present), 10+ year financials, derivative arrangements (puts/calls/earnouts) with strategic implications. See [[Note structures]] for depth standard; [[Valentino]] is the template.
- **Banks**: Use bank-specific metrics (see [[Financials templates]])

## Finding links

See [[Linking and hierarchy]] for systematic approach: check what exists, steal from peers, category checklists, reverse lookup, concept connections.

## Related section convention

See [[Note structures]] for format and annotation types.
