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

# Fundamentals
curl "http://localhost:5000/api/chart/lw?tickers=AAPL&metrics=revenue" \
  -o investing/attachments/aapl-revenue.png
```

**API parameters:** `tickers` (required), `start`, `end`, `title`, `width` (1200), `height` (800), `show_title` (true), `normalize` (false), `metrics` (revenue, netincome, eps, fcf, operatingincome, ebitda, grossprofit), `forecast_start` (date to begin dotted forecast line), `labels` (custom legend labels, e.g., `labels=SMH_1_44X:SMH%201.44x%20Lev`), `sort_by_last` (sort legend by final value, high→low)

**Naming:** `aapl-price-chart.png`, `tsmc-vs-samsung-foundry.png`, `nvda-2024-rally.png`

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

**Status:** Database and API complete, UI integration pending.

**Options:**
- **A) Synthetic tickers** — `AAPL_SI_PCT`, `AAPL_SI_DAYS`, etc.
- **B) Separate chart overlay** — New UI component
- **C) Wide table** — Add to `/api/data` endpoint

### Obsidian chart refresh plugin

**Status:** Planned. See `docs/obsidian-chart-refresh-plugin.md` for full spec.

**Problem:** Charts are static PNGs that become stale. Manual refresh via curl is tedious.

**Solution:** Custom Obsidian plugin that refreshes chart images on note open.

**Key decisions needed:**
- **Filename vs frontmatter** for chart params mapping
- **Auto-advance forecast_start?** As time passes

**Estimate:** ~150-200 lines TypeScript, 2-4 hours.

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
- Link liberally with `[[wikilinks]]`
- **No thin stubs** — if no time to research, add to daily note instead

See [[Note structures]] for actor requirements and templates.

### "What makes X, X" analysis

Go beyond facts to explain why something works: flywheel, moats, structural advantage, the math.

## When editing existing notes

**Every edit is an opportunity to rebuild.** Check for: thin stubs, missing financials/cap tables, outdated data, no Related section. Make the requested edit first, then assess quality gaps.

## Processing new information

**Every piece of news needs an atomic home — daily notes are never the only location.**

1. **Check existing notes first** — search vault before web
2. **Find the right home** — actors taking actions, not catch-all concepts
3. **Regional actors stay high-level** — specific news goes on specific actors
4. **Always update daily notes** — use event date, not article date
5. **Check for events** — M&A, bankruptcy, IPO → create Event note

See [[Note structures]] for event criteria and templates.

## Conventions

See [[Thesis conventions]] for thesis naming. See [[Taxonomy discussion]] for hashtag structure.

## Daily note structure

See [[Note structures]] for the standard daily note template. **Vault activity is mandatory** — journal all note creation/modification.

## Research workflow

1. **Web search** for major news
2. **X/Twitter lists** for commentary (Chips & Semiconductors, AI Infrastructure, SemiAnalysis)
3. Add findings to daily note first, extract to actor/concept notes if substantial

### Daily news search checklist

When user asks for "today's news", cover these categories:

| Category | Search terms |
|----------|--------------|
| **Markets** | "stock market news [date]" |
| **Semiconductors** | "semiconductor chip news [date]" |
| **AI/Tech** | "AI news [date]" |
| **China macro** | "China economy news [date]" |
| **China tech** | "China tech news [date]" |
| **Fed/Rates** | "Federal Reserve news [date]" |
| **Energy/Nuclear** | "energy power grid news [date]", "nuclear power news [date]" |
| **Robotics** | "robotics humanoid news [date]" |
| **Japan tech** | "Japan semiconductor news [date]" |
| **Korea semis** | "Korea semiconductor memory news [date]" |
| **Trade/Tariffs** | "tariffs trade war news [date]", "export controls [date]" |
| **Europe** | "Europe tech news [date]", "ECB news [date]" |
| **Earnings** | Check calendar for major reports |

**Don't miss:** China domestic news (GDP, [[NDRC]], stimulus, regulatory) — often absent from US-focused searches.

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
- **Private companies**: Cap table with investors, rounds, valuations
- **Banks**: Use bank-specific metrics (see [[Financials templates]])

## Finding links

See [[Linking and hierarchy]] for systematic approach: check what exists, steal from peers, category checklists, reverse lookup, concept connections.

## Related section convention

See [[Note structures]] for format and annotation types.
