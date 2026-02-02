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

**App:**
- Dashboard: `charting_sandbox/chart-dashboard.js`
- Backend: `charting_app/app.py`
- Tests: `tests/unit/`, `tests/playwright/`

**Vault:**
- Root: `investing/`
- Actors: `investing/Actors/` (companies, orgs, people, **countries**)
- Regions: `investing/Regions/` (multi-country only: LATAM, GCC, Southeast Asia)
- Concepts: `investing/Concepts/`
- Events: `investing/Events/`
- Theses: `investing/Theses/`
- Daily: `investing/Daily/`
- Sectors: `investing/Sectors/`

**Countries go in Actors, not Regions.** See `India.md` for hub template (~100-150 lines max).

**Cache busting:** After modifying JS, increment `?v=` in `charting_sandbox/index.html`.

---

## Database

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

## Vault Guidelines

### Philosophy

- **Atomic notes** — one idea per note
- **Self-contained** — reader understands without clicking links
- **Links over hierarchy** — structure from `[[connections]]`
- **Daily notes as inbox** — capture first, extract when mature

### Key Rules

- **Deep research before creating** — web search, multiple sources, hard data
- **Everything linked** — every entity gets a `[[wikilink]]`
- **Numbers matter** — exact figures with sources, not "significant"
- **Verify before creating** — always check if actor exists first:
  ```bash
  cd /c/Users/klein/financial-charts/investing && git ls-files "Actors/*.md" | sed 's|.*/||; s|\.md$||' | grep -iE "name"
  ```

### Detailed References

| Topic | Location |
|-------|----------|
| Chart API, forecasts, data setup | `docs/chart-api.md` |
| Actor completion checklist | `docs/actor-checklist.md` |
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
