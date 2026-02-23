# Claude Code Instructions

This project is an integrated system: **database → charts → vault**.

- **Database** stores raw data (prices, financials, short interest)
- **Charts** visualize that data as rich expressions
- **Vault** (Obsidian notes at `investing/`) provides meaning, narrative, and theses

---

## Code Changes — Explore First

**Before modifying any code file, explore the surrounding codebase first.** Check for existing patterns, utility scripts, and similar implementations elsewhere in the project. Never edit a file you haven't explored the context of. The sequence is always: explore → understand existing patterns → write code that follows them.

---

## Git Workflow

**Direct push to main** — no PRs required. CI runs after push.

```bash
git add <files> && git commit -m "Description" && git push origin main
```

If CI fails, fix forward or `git revert HEAD && git push origin main`.

---

## Tools & Locations

**Tools:**
- gh CLI: `/c/Users/klein/Downloads/gh_2.86.0_windows_amd64/bin/gh.exe`
- Playwright: `npx playwright install chromium` (first-time)
- SEC filings: `python scripts/parse_sec_filing.py TICKER --save filing.txt`
  - WebFetch gets 403'd by SEC — use this script instead
  - Run `python scripts/parse_sec_filing.py --help` for full usage (multi-filing, type selection, Q4 calculation)
- YouTube transcripts: `python scripts/transcribe_youtube.py URL --save output.txt`
  - **Auto-trigger:** When the user pastes a YouTube URL, automatically run this script and present the transcript. No need to wait for explicit instruction.
  - Tries YouTube subtitles first, falls back to Whisper if none available
  - Use `--language pt` for Portuguese, `--model small` for better Whisper accuracy on long content

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

**CRITICAL: Never DELETE or UPDATE data without explicit user authorization.** Filter at query time instead. Data is irreplaceable — re-fetching may not restore original values.

**Location:** `market_data.db` (root directory)

### Schema

**Wide format** — tickers are columns, not rows. `PRAGMA table_info(stock_prices_daily)` to check columns.

**Tables:** `stock_prices_daily` (wide, Date + ticker columns), `ticker_metadata`, `income_statement_annual`, `income_statement_quarterly`, `short_interest`.

### Adding Tickers

```bash
python scripts/add_ticker.py TRI RELX MORN  # adds multiple tickers
```

This downloads history via yfinance, adds columns to `stock_prices_daily`, and updates `ticker_metadata`.

### Adding Fundamentals (for metrics charts)

Price data and fundamentals are **separate**. Metrics charts require both:

```bash
python scripts/add_ticker.py PM          # Step 1: price data (yfinance)
python fetch_fundamentals.py PM          # Step 2: fundamentals (Alpha Vantage)
```

Without step 2, metrics charts return an error. Check existing: `SELECT DISTINCT ticker FROM income_statement_annual ORDER BY ticker;`

### Data freshness (CRITICAL)

**If financial data is publicly available, do your utmost to find and ingest it.** The vault should never be behind publicly available data just because a third-party API hasn't synced yet. Use `/earnings TICKER` for the full procedure.

**Price data** also goes stale — run `python update_market_data.py --lookback 10` before generating price charts if data is more than a day old.

### Synthetic Indices

Custom weighted baskets: `python scripts/create_aiwd_index.py --store`. See that script for the pattern.

### Date Format (CRITICAL)

All dates in `stock_prices_daily` use `'YYYY-MM-DD HH:MM:SS'`. **Never insert date-only format.** SQLite treats date-only and datetime as different strings → silent duplicates.

### Updating Prices

`python update_market_data.py --lookback 10 --assets stocks etfs mutualfunds adrs fx crypto futures iv`

Delisted ticker warnings are expected and harmless. **Never remove historical data for delisted tickers.**

---

## Charts

> **CRITICAL: NEVER overwrite existing chart files without asking first.**
> Read the existing image and ask before making changes.
>
> **NEVER remove attachment embeds (`![[...]]`) from notes without asking first.**
> Adding new charts alongside existing ones is fine. Replacing or removing existing embeds requires explicit approval.

**Full reference:** See `docs/chart-api.md`

Start server: `cd /c/Users/klein/financial-charts && python charting_app/app.py`

**Key parameters:** `tickers`, `start`, `normalize`, `primary` (actor = blue), `metrics`, `forecast_start`. See `docs/chart-api.md` for curl examples and full parameter reference.

**Best practices:**
- Prefer peer comparisons (2-4 tickers) over single-ticker charts
- No titles needed — legend suffices
- Always add italicized interpretation below charts
- Verify output by checking file size (`wc -c`) before reading images — files under 1KB are errors, not PNGs
- **Charts must live in notes** — never save to attachments without embedding in a relevant note
- **Every chart needs a corresponding data table** — reader should see the underlying numbers, not just the visualization

### Chart Naming Convention (CRITICAL)

**Use `-vs-` format for comparison charts** (e.g. `aapl-vs-qqq-price-chart.png`). The obsidian-chart-refresh plugin parses tickers from filenames to auto-refresh. First ticker becomes blue (primary).

Exceptions, fallbacks, and plugin limitations: see `docs/chart-api.md` and `investing/chart-registry.md`.

---

## Daily News Workflow

Use `/news` skill for the full ingestion workflow (source discovery, date gate, article ingestion, earnings check, compliance). See `.claude/skills/news/SKILL.md`.

Use `/earnings TICKER` to process earnings — check DB, find latest data, insert, regenerate charts, update notes. See `.claude/skills/earnings/SKILL.md`.

---

## Vault Guidelines

### Philosophy

- **Atomic notes** — one idea per note
- **Self-contained** — reader understands without clicking links
- **Links over hierarchy** — structure from `[[connections]]`
- **Daily notes as inbox** — capture first, extract when mature

### Edit Gates (CRITICAL)

1. **Pre-edit — Entity linking:** Before editing ANY note, check if mentioned entities have notes (including aliases). If missing → create stub. Always use `[[wikilinks]]`.
2. **Post-edit — Daily note:** After updating actor/product/event notes, add a summary entry to today's daily note (`investing/Daily/YYYY-MM-DD.md`) before considering the task done. Create with `#daily` tag if it doesn't exist.
3. **Post-edit — Concept extraction:** Scan for terms that deserve their own concept note. Bar: would a reader benefit from a dedicated note? If yes, create and wikilink in the same pass. See `docs/note-checklist.md`.

### Key Rules

- **Deep research before creating** — web search, multiple sources, hard data
- **Harvest source charts** — when researching, if source articles contain useful charts or visualizations (bond prices, market data, analyst graphics), save them to `investing/attachments/` and show them to the user. Embed in the relevant note with attribution.
- **No info outside note** — all research findings go in the note, not just conversation
- **Everything linked** — every entity gets a `[[wikilink]]`
- **Numbers matter** — exact figures with sources, not "significant"
- **Never replace, always add** — when adding new data, augment existing content, never overwrite it
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

### Evolution Section (Actor Notes)

Company, country, and institution actor notes should include an **Evolution** section — the key inflection points that explain why the entity looks the way it does today. Not a full history, but the strategic genealogy: pivotal acquisitions, divestitures, crises, pivots, and regime changes that shaped current positioning.

- Wikilink to other investing vault entities (companies, products, people) mentioned in the evolution
- Each bullet should be an inflection point that explains something about the present
- When a company's evolution connects to a broader theme in the history vault, add a cross-vault URI link
- Stubs don't need an Evolution section — add it when the note matures beyond a stub

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

### Cross-Vault Linking

> Full architecture: `C:\Users\klein\obsidian\geopolitics\vault-architecture.md`

The **geopolitics vault** (`C:\Users\klein\obsidian\geopolitics\`, repo `Kleinster2/geopolitics`) covers the same topics from a statecraft/frameworks angle. **Overlap is expected and desirable.** Both vaults need core facts; each adds its own lens. This vault includes geopolitical context when it affects investment flows. The geopolitics vault includes economic/business context when it shapes statecraft. Don't strip content just because it "belongs" in the other vault — strip it only if it's irrelevant to this vault's purpose.

When a note has a meaningful counterpart in the other vault, add clickable `obsidian://` URI links.

**Format:**
```markdown
### Cross-vault
- [Geopolitics: Note Name](obsidian://open?vault=geopolitics&file=Folder%2FNote%20Name) — what the other perspective adds
```

**Rules:**
- Place under `### Cross-vault` subheading at end of Related section
- URL-encode paths: spaces → `%20`, slashes → `%2F`
- Brief description of what the other vault's perspective adds
- Only cross-link notes with meaningful counterparts — not every shared entity
- These links won't appear in graph view or backlinks — navigation aids only

**Post-ingestion gate:** After creating a new event or making a major update, ask: *does this also belong in the geopolitics vault?* If the story involves statecraft, sanctions, diplomatic precedent, alliance dynamics, or infrastructure competition, flag it to the user. Don't silently skip — the default is to ask. Routine updates to existing notes don't trigger this.

**History vault reference:** The **history vault** (`C:\Users\klein\obsidian\history\`) covers long-arc economic history — trade, institutions, innovation from prehistory to modernity. When writing about a topic with deep historical roots (sanctions, trade wars, infrastructure control, monetary policy, commodity economics, Monroe Doctrine, etc.), check the history vault for relevant precedent. When an event represents a genuine structural break or first-of-its-kind precedent (novel sanctions mechanism, new form of economic statecraft, industry-reshaping consolidation), flag it for the history vault — today's inflection points become tomorrow's history.
