# Claude Code Instructions

This project is an integrated system: **database → charts → vault**.

- **Database** stores raw data (prices, financials, short interest)
- **Charts** visualize that data as rich expressions
- **Vault** (Obsidian notes at `investing/`) provides meaning, narrative, and theses

---

## Git Workflow

**Direct push to main** — no PRs required. CI runs after push.

```bash
git add <files> && git commit -m "Description" && git push origin main
```

If CI fails, fix forward or `git revert HEAD && git push origin main`.

### Tool Error Recovery

After Edit/Write tool errors, check for unintended modifications:
```bash
git status --short
```

If unexpected files modified, compare and restore:
```bash
git show HEAD:"path/to/file.md" | wc -l  # committed
wc -l "path/to/file.md"                   # working
git restore "path/to/file.md"             # restore if damaged
```

---

## Tools & Locations

**Tools:**
- gh CLI: `/c/Users/klein/Downloads/gh_2.86.0_windows_amd64/bin/gh.exe`
- Playwright: `npx playwright install chromium` (first-time)
- SEC parser: `python scripts/parse_sec_filing.py TICKER` — **preferred over browser scrolling**
  - Downloads 10-K/10-Q from EDGAR, extracts key terms (going concern, material weakness, litigation, etc.)
  - SEC requires User-Agent with email; script handles gzip decompression
  - Faster and more comprehensive than browser navigation through EDGAR

**App:**
- Dashboard: `charting_sandbox/chart-dashboard.js`
- Backend: `charting_app/app.py`
- Tests: `tests/unit/`, `tests/playwright/`

**Vault:**
- Root: `investing/`
- Actors: `investing/Actors/` (companies, orgs, people, **countries**)
- Products: `investing/Products/` (chips, AI models, drugs, vehicles — things made by Actors)
- Regions: `investing/Regions/` (multi-country only: LATAM, GCC, Southeast Asia)
- Concepts: `investing/Concepts/`
- Events: `investing/Events/`
- Theses: `investing/Theses/`
- Daily: `investing/Daily/`
- Sectors: `investing/Sectors/`

**Countries go in Actors, not Regions.** See `India.md` for hub template (~100-150 lines max).

**Products vs Actors:** Products lack agency — the parent Actor makes decisions. NVIDIA (Actor) → H100 (Product). See `[[Linking and hierarchy]]`.

**Cache busting:** After modifying JS, increment `?v=` in `charting_sandbox/index.html`.

---

## Database

**Location:** `market_data.db` (root directory)

### Schema

**Wide format** — tickers are columns, not rows:

```sql
-- stock_prices_daily: Date column + one column per ticker
SELECT Date, AAPL, MSFT, GOOGL FROM stock_prices_daily LIMIT 5;

-- Check if ticker exists
PRAGMA table_info(stock_prices_daily);  -- lists all columns
```

**Key tables:**

| Table | Description |
|-------|-------------|
| `stock_prices_daily` | Daily close prices (wide format) |
| `ticker_metadata` | Ticker names, date ranges, data points |
| `income_statement_annual` | Annual financials |
| `income_statement_quarterly` | Quarterly financials |
| `short_interest` | Short interest data |

### Adding Tickers

```bash
python scripts/add_ticker.py TRI RELX MORN  # adds multiple tickers
```

This downloads history via yfinance, adds columns to `stock_prices_daily`, and updates `ticker_metadata`.

### Adding Fundamentals (for metrics charts)

Price data and fundamentals are **separate**. If you need `metrics=revenue,netincome` charts:

```bash
# Step 1: Add price data (yfinance)
python scripts/add_ticker.py PM

# Step 2: Add fundamentals (Alpha Vantage) — required for metrics charts
python fetch_fundamentals.py PM
```

Without step 2, fundamentals charts return `{"error": "No fundamentals data found"}` instead of an image.

**Check existing fundamentals:**
```sql
SELECT DISTINCT ticker FROM income_statement_annual ORDER BY ticker;
```

### Synthetic Indices

Create custom weighted baskets:

```bash
python scripts/create_aiwd_index.py --store  # AI Workflow Disruption basket
```

See `scripts/create_aiwd_index.py` for pattern — define weights dict, calculate returns, store as new column.

### Date Format (CRITICAL)

All dates in `stock_prices_daily` use `'YYYY-MM-DD HH:MM:SS'`. **Never insert date-only format.**

SQLite treats these as different strings → silent duplicates. Fix with:
```sql
DELETE FROM stock_prices_daily WHERE Date NOT LIKE '%00:00:00'
AND (Date || ' 00:00:00') IN (SELECT Date FROM stock_prices_daily WHERE Date LIKE '%00:00:00');
```

### Updating Prices

```bash
python update_market_data.py --lookback 10 --assets stocks etfs mutualfunds adrs fx crypto futures iv
```

Delisted ticker warnings are expected and harmless.

**Never remove historical data for delisted tickers** — data remains valuable.

---

## Charts

> **CRITICAL: NEVER overwrite existing chart files without asking first.**
> Read the existing image and ask before making changes.

**Full reference:** See `docs/chart-api.md`

### Quick Start

```bash
cd /c/Users/klein/financial-charts && python charting_app/app.py

# Price comparison
curl "http://localhost:5000/api/chart/lw?tickers=AAPL,QQQ&normalize=true&start=2020-01-01" \
  -o investing/attachments/aapl-vs-qqq.png

# Fundamentals
curl "http://localhost:5000/api/chart/lw?tickers=AAPL&metrics=revenue,netincome" \
  -o investing/attachments/aapl-fundamentals.png
```

**Key parameters:** `tickers`, `start`, `normalize`, `primary` (actor = blue), `metrics`, `forecast_start`

**Best practices:**
- Prefer peer comparisons (2-4 tickers) over single-ticker charts
- No titles needed — legend suffices
- Always add italicized interpretation below charts
- Verify output by reading generated images
- **Charts must live in notes** — never save to attachments without embedding in a relevant note

---

## Pending Design Decisions

### Short interest charting
Database/API/dashboard complete. Chart overlay pending — see `docs/PROPOSALS.md`.

### Obsidian chart refresh plugin
Planned. See `docs/obsidian-chart-refresh-plugin.md`.

---

## Daily News Workflow

### Earnings (CRITICAL)

**Always check earnings calendar when doing daily news.** Major earnings move markets and affect actors.

1. **Search:** `"earnings reports week [date]"` or check Yahoo Finance calendar
2. **Capture all relevant earnings** — not just focus areas. Disney, PayPal, consumer names matter for macro context
3. **For each earnings report:**
   - Add section to actor note with key metrics (EPS, revenue, guidance)
   - Add to daily note with stock reaction
   - Note any CEO changes, guidance surprises, or strategic shifts
4. **Don't wait for "today's" earnings** — search for prior day's after-hours and pre-market results

**Earnings that matter beyond focus areas:**
- Mag 7 (AAPL, MSFT, GOOGL, AMZN, META, NVDA, TSLA)
- Major financials (JPM, GS, BAC)
- Consumer bellwethers (DIS, PYPL, NFLX, SBUX)
- Industrial/macro signals (CAT, UPS, FDX)

---

## Vault Guidelines

### Philosophy

- **Atomic notes** — one idea per note
- **Self-contained** — reader understands without clicking links
- **Links over hierarchy** — structure from `[[connections]]`
- **Daily notes as inbox** — capture first, extract when mature

### Entity Linking (CRITICAL)

**Before editing ANY note that mentions an entity:**

1. **Check** if entity note exists (including aliases)
2. **If missing** → create stub OR flag dead link
3. **Always use `[[wikilinks]]`** for entities in the edit

This applies to daily notes, earnings additions, news items — everything. Entity linking is a **pre-edit gate**, not post-edit cleanup.

### Key Rules

- **Deep research before creating** — web search, multiple sources, hard data
- **No info outside note** — all research findings go in the note, not just conversation
- **Everything linked** — every entity gets a `[[wikilink]]`
- **Numbers matter** — exact figures with sources, not "significant"
- **Never remove wikilinks** — create missing notes instead. See `[[Linking and hierarchy]]` for details.
- **MUST run before creating ANY new note** — check for existing notes and aliases:
  ```bash
  python scripts/check_before_create.py "Proposed Note Name"
  ```
  If conflicts found, link to existing note instead of creating. This is a **hard gate** — never skip it.
- **Run compliance after creating/editing actor notes**:
  ```bash
  python scripts/check_note_compliance.py investing/Actors/NewNote.md
  ```
  Fix errors before moving on. Warnings (dead links) are expected for new notes.
- **Create stubs for dead links** — after compliance check, create minimal stub notes for any dead-linked entities. Stubs need: frontmatter with aliases, tags, one-line description, Quick stats table, Related section.

### Detailed References

| Topic | Location |
|-------|----------|
| Chart API, forecasts, data setup | `docs/chart-api.md` |
| Note completion checklist | `docs/note-checklist.md` |
| News search, verification, sourcing | `docs/research-workflow.md` |
| Note templates, Related format | `[[Note structures]]` |
| Folder rules, concept vs sector | `[[Linking and hierarchy]]` |
| Financials templates | `[[Financials templates]]` |
| Thesis naming | `[[Thesis conventions]]` |

### Focus Areas

- **AI stack** — chips, infrastructure, hyperscalers, labs
- **Semiconductors** — foundry, memory, equipment, fabless
- **Robotics** — humanoids, automation
- **China** — decoupling, industrial policy
- **Energy** — power demand, grid, nuclear
- **Manufacturing** — reshoring, industrial policy

Plus macro, rates, media, and wherever there's signal.
