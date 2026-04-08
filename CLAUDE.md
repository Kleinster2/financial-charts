# Project Instructions

Integrated system: database (raw data) → charts (visualization) → vault (`investing/`, Obsidian notes with meaning and theses).

## Hard Gates (CRITICAL — do not skip)

1. **Daily note**: After creating/expanding any note, log it in today's daily note (`investing/Daily/YYYY-MM-DD.md`). Run `date` to confirm current date. Every stub counts. #1 compliance failure.
2. **Pre-create**: `python scripts/check_before_create.py "Note Name"` before creating ANY new note. If conflicts → link to existing.
3. **Post-edit compliance**: `python scripts/check_note_compliance.py investing/Actors/Note.md` after creating/editing actor notes. Fix errors. Create stubs for dead links (frontmatter, one-line description, Quick stats, Related).
4. **Chart overwrite**: NEVER overwrite existing chart files or remove `![[...]]` embeds without asking.
5. **DB mutation**: NEVER DELETE or UPDATE data without explicit authorization. Filter at query time. Data is irreplaceable.
6. **Chart file size**: `wc -c` before reading any chart — under 1KB = error JSON, not PNG.
7. **Price verification**: Never write price moves into notes without verifying against actual closing data. No secondary sources.
8. **Entity linking**: Before editing any note, check if mentioned entities have notes. Missing → create stub. Always `[[wikilinks]]`.
9. **Concept extraction**: After edits, scan for terms deserving their own concept note. If yes, create and wikilink in same pass. See `docs/note-checklist.md`.
10. **No ephemeral notes**: Dated data releases (jobs reports, CPI prints, PMI, GDP) and earnings previews/calendars are NOT standalone notes. They are data points — fold them into the relevant existing concept or actor note (e.g., NFP data → `2026 recession risk`, bank earnings preview → the bank's actor note). A note earns existence by being a **durable, referenceable entity or concept** — not a single release date or a calendar of upcoming dates. Ask: "Will this note still be useful in 6 months, or will it be stale?" If stale → don't create it.

---

## Code & Git

- **Explore first**: Check existing patterns, utility scripts, similar implementations before modifying any code file.
- **Map before acting**: Search all related components (scripts, skills, docs, hooks, configs, vaults) before modifying anything. The question is "what's the full picture?"
- **Git**: Direct push to main, no PRs. `git add <files> && git commit -m "Description" && git push origin main`. CI fails → fix forward or revert.
- **Cache busting**: After modifying JS, increment `?v=` in `charting_sandbox/index.html`.

---

## Tools

- gh CLI: `gh` (on PATH)
- SEC filings: `python scripts/parse_sec_filing.py TICKER` — run with `--help` for full usage
- Obsidian CLI: `"/c/Users/klein/AppData/Local/Programs/Obsidian/Obsidian.com"` (requires Obsidian running). Key commands: `move`/`rename` (link-preserving), `search query=X`, `unresolved`, `backlinks file=X`, `--help` for full list.
- YouTube: `python scripts/transcribe_youtube.py URL --save output.txt` (`--language pt` for Portuguese)
- App: backend `charting_app/app.py` | dashboard `charting_sandbox/chart-dashboard.js` | tests `tests/`

---

## Vault Folders

| Folder | Contents |
|--------|----------|
| `Actors/` | Companies, orgs, people, **countries** (not Regions). See `India.md` for hub template. |
| `Products/` | Things made by Actors (chips, models, drugs). No agency — parent decides. Every Product requires a parent Actor note. Don’t merge companies into product notes even if the company is small, acquired, or subsidiary — the taxonomy doesn’t care about salience. See `[[Linking and hierarchy]]`. |
| `Infrastructure/` | Fixed physical assets enabling trade/energy flows: straits, pipelines, terminals. |
| `Assets/` | Securities notes — tradeable instruments, price history, charts. See `docs/vault-note-guide.md`. |
| `Concepts/` | Ideas, frameworks, technologies. |
| `Events/` | Discrete happenings with clear dates (a conflict, a policy change, a deal, a crisis). Actor notes carry summary + link. Number of actors is NOT a criterion — what matters is whether it’s a *dated occurrence* vs an ongoing dynamic. Ongoing competitive landscapes, structural trends, and frameworks belong in Concepts/. |
| `Sectors/` | Hub structure only — live market data goes in subsector notes. |
| `Regions/` | Multi-country only (LATAM, GCC, Southeast Asia). |
| `Theses/` | Investment theses. See `[[Thesis conventions]]`. |
| `Daily/` | Daily notes (inbox, synthesis, edit log). |

---

## Database

**Location:** `market_data.db` (root). Wide format — tickers are columns. `PRAGMA table_info(stock_prices_daily)`.

**Tables:** `stock_prices_daily` (wide, Date + ticker cols), `ticker_metadata`, `income_statement_annual`, `income_statement_quarterly`, `short_interest`.

**Date format (CRITICAL):** `'YYYY-MM-DD HH:MM:SS'` always. Never date-only — causes silent duplicates.

**Commands:**
- Add tickers: `python scripts/add_ticker.py TRI RELX MORN`
- Add fundamentals: `python fetch_fundamentals.py PM` (requires price data first via add_ticker)
- Check existing fundamentals: `SELECT DISTINCT ticker FROM income_statement_annual ORDER BY ticker;`
- Update prices: `python update_market_data.py --lookback 10 --assets stocks etfs mutualfunds adrs fx crypto futures iv`
- Synthetic indices: `python scripts/create_aiwd_index.py --store`

**Data freshness:** If publicly available, find and ingest it. Use `/earnings TICKER` for full procedure. Update prices before generating charts if data >1 day old. Never remove historical data for delisted tickers.

---

## Charts

Full reference: `docs/chart-api.md` | Start server: `python charting_app/app.py`

Always use `/api/chart/lw` for price charts. Key params: `tickers`, `start`, `normalize`, `primary` (actor = blue).

**Naming (CRITICAL):** `-vs-` format for comparisons (`aapl-vs-qqq-price-chart.png`). First ticker = blue (primary). Chart-refresh plugin parses tickers from filenames. Financial statements: `{ticker}-sankey.png`, `{ticker}-waterfall.png` (lowercase, no suffixes).

**Practices:** Peer comparisons (2-4 tickers), no titles (legend suffices), italicized interpretation below, charts must live in notes with data tables, ETF benchmarks get normalized comparison vs benchmark.

---

## Known Limitations

**Web access:**
- SEC EDGAR → use `parse_sec_filing.py` (never WebFetch on sec.gov)
- Bloomberg → blocked everywhere; ask user to paste text
- Paywalled sources (PitchBook, cbonds, Fitch) → ask user for data
- Playwright → no cookies; use Claude-in-Chrome MCP for authenticated sites

**Data pipeline:**
- Alpha Vantage 25/day limit → silently returns 0 rows when rate-limited → 44-byte error files. Workaround: manual SQL from StockAnalysis.com.

**Windows:** `python app.py &` doesn't work in Git Bash. Use `app.test_client()` for smoke testing.

---

## Vault Directives

**Philosophy:** Atomic notes, self-contained, links over hierarchy, daily notes as inbox. The vault earns its value by being more thorough than what's freely available.

**Terse prompts:** Bare entity name = check if note exists → research → create if not. Don't ask what it is.

**Product note gate:** Major product launch catalyzing an actor update → create product note in same pass. Actor keeps strategy; product carries specs. See `docs/vault-note-guide.md`.

**Harvest source charts:** Save useful charts/visualizations from sources to `investing/attachments/`, embed with attribution.

**Cross-vault gate:** After new events or major updates, flag relevant sibling vaults (geopolitics, Brazil, history, technologies). Don't silently skip. See `docs/cross-vault-rules.md`.

**Full-entity sweep on ingestion:** When processing any source (article, transcript, filing), check ALL mentioned entities — not just primary subjects — for needed vault updates. Secondary mentions often reveal gaps: a company's existing note may be missing a partnership, a sector note may lack a competitive development, a Related section may be incomplete. The sweep includes: (1) reading each mentioned entity's note, (2) identifying missing facts or stale data, (3) updating secondary notes in the same pass. Don't extract data points from the primary subject and move on — process the full graph of entities touched by the source.

**Private companies:** Tag appropriately in frontmatter. Include funding rounds table where data exists (also for pre-IPO history of public companies).

---

## Workflows

- `/news` — full ingestion workflow. See `.claude/skills/news/SKILL.md`.
- `/ingest` — single-source ingestion (interview, article, filing, screenshots). See `.claude/skills/ingest/SKILL.md`.
- `/earnings TICKER` — DB check, data insert, chart regen, note update. See `.claude/skills/earnings/SKILL.md`.

---

## Memory vs Documentation Discipline

When saving a feedback or workflow memory, apply this gate first:

**Is this a durable rule that will apply across sessions?** → Put it in the relevant doc (`docs/research-workflow.md`, `docs/vault-note-guide.md`, `docs/chart-api.md`, etc.), not in memory. Memory entry should just point to the doc.

**Is this a one-time correction, personal preference, or context-dependent judgment call?** → Memory is the right home.

When MEMORY.md exceeds ~180 lines or at the end of sessions where multiple memories were created, audit for:
- Memory entries that duplicate doc content → collapse to doc pointers
- Durable rules that accumulated in memory instead of docs → promote
- Stale entries that no longer apply → remove

Docs are the source of truth for workflow rules. Memory is for context that helps apply those rules.

---

## References

| Topic | Location |
|-------|----------|
| Chart API, forecasts, data setup | `docs/chart-api.md` |
| Note completion checklist | `docs/note-checklist.md` |
| News search, verification, sourcing | `docs/research-workflow.md` |
| Actor voice, synopsis, evolution, concept structure | `docs/vault-note-guide.md` |
| Actor/securities split, economics/prices split | `docs/vault-note-guide.md` |
| Cross-vault linking format and gates | `docs/cross-vault-rules.md` |
| Note templates, Related format | `[[Note structures]]` |
| Folder rules, concept vs sector | `[[Linking and hierarchy]]` |
| Financials templates | `[[Financials templates]]` |
| Thesis naming | `[[Thesis conventions]]` |
