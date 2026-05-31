# Project Instructions

Integrated system: database (raw data) → charts (visualization) → vault (`investing/`, Obsidian notes with meaning and theses).

## Hard Gates (CRITICAL — do not skip)

1. **Daily note**: After creating/expanding any note, log it in today's daily note (`investing/Daily/YYYY-MM-DD.md`). Run `date` to confirm current date. Every stub counts. Also add or update a non-empty `## Synthesis` section that explains what changed, why it matters, and the causal read-through; the daily note is not complete if it only lists touched files. #1 compliance failure.
2. **Pre-create**: `python scripts/check_before_create.py "Note Name"` before creating ANY new note. If conflicts → link to existing.
3. **Post-edit compliance**: `python scripts/check_note_compliance.py investing/Actors/Note.md` after creating/editing actor notes. Fix errors. Create stubs for dead links (frontmatter, one-line description, Quick stats, Related).
4. **Chart overwrite**: NEVER overwrite existing chart files or remove `![[...]]` embeds without asking.
5. **DB mutation**: NEVER DELETE or UPDATE data without explicit authorization. Filter at query time. Data is irreplaceable.
6. **Chart file size**: `wc -c` before reading any chart — under 1KB = error JSON, not PNG.
7. **Price verification**: Never write price moves into notes without verifying against actual closing data. No secondary sources.
8. **Entity linking**: Before editing any note, check if mentioned entities have notes. Missing → create stub. Always `[[wikilinks]]`.
9. **Concept extraction**: After edits, scan for terms deserving their own concept note. If yes, create and wikilink in same pass. See `docs/note-checklist.md`.
10. **No ephemeral notes**: Dated data releases (jobs reports, CPI prints, PMI, GDP) and earnings previews/calendars are NOT standalone notes. They are data points — fold them into the relevant existing concept or actor note (e.g., NFP data → `2026 recession risk`, bank earnings preview → the bank's actor note). A note earns existence by being a **durable, referenceable entity or concept** — not a single release date or a calendar of upcoming dates. Ask: "Will this note still be useful in 6 months, or will it be stale?" If stale → don't create it.
11. **Cluster validation (public actor notes)**: Every new public-company actor note (with a securities companion) and every concept note that names a peer cohort must include cluster validation: write `scripts/cluster_configs/{primary_ticker}.yaml` defining the candidate cohort + control groups, run `python scripts/cluster_analysis.py --primary TICKER`, embed the dendrogram + summary table in the actor or its parent concept note. The intra-cluster correlation, hierarchical clustering boundary, and PC1 explained variance are required diagnostics — they answer "where does this name actually trade" mathematically, not by analogy. See `docs/cluster-validation.md`.
12. **Provided chart ingestion**: Every chart, table-like visualization, or screenshot supplied by the user or present in an ingested source must leave a durable vault artifact. If rights allow, save the image to `investing/attachments/` and embed it with attribution. If publisher terms or copyright make copying inappropriate, extract the chart's axes, series, dates, values/estimates, and takeaway into the relevant note instead, cite the source, and state in the daily note that the chart was ingested as extracted data rather than copied.
13. **Table-safe wikilinks**: In Markdown table cells, never use raw alias wikilinks like `[[Note|alias]]`; the `|` splits the table into extra columns. Prefer `[[Note]]` in tables, or escape the pipe as `[[Note\|alias]]`. Before finishing table-heavy edits, run `rg -n "\|.*\[\[[^\]\\]+\|" .` and fix any unescaped table-cell alias pipes.

---

## Code & Git

- **Explore first**: Check existing patterns, utility scripts, similar implementations before modifying any code file.
- **Map before acting**: Search all related components (scripts, skills, docs, hooks, configs, vaults) before modifying anything. The question is "what's the full picture?"
- **Skill parity / consistency**: Parity scopes live in `skills/skill-parity-scopes.json`; financial workflow skill names still live in `skills/shared-workflows.json`. After editing shared workflow skills, run `python scripts/promote_shared_skill.py SKILL --from newest` (or `--scope SCOPE --from claude|codex|openclaw` when the intended source/scope is explicit), then run `python scripts/check_skill_parity.py --all-scopes --strict` or `npm run test:consistency`. Codex, Claude, and OpenClaw should match byte-for-byte after newline normalization; OpenClaw runtime setup belongs outside the skill body. `npm run test:consistency` also runs note-compliance regressions and the live market-reaction peer sweep. See `docs/skill-parity.md`.
- **Git**: Direct push to main, no PRs. `git add <files> && git commit -m "Description" && git push origin main`. CI fails → fix forward or revert.
- **Branch rules**: `main` blocks deletion and non-fast-forward pushes. CI still runs on direct pushes, but `smoke` is not a pre-push required check for this solo direct-push workflow.
- **Dependency maintenance**: Dependabot checks GitHub Actions and npm weekly. `.github/workflows/dependabot-automerge.yml` may auto-merge only npm `devDependencies` patch/minor PRs after `Playwright Smoke` passes. Major updates, GitHub Actions updates, runtime dependencies, and unusual diffs stay manual.
- **Cache busting**: After modifying JS, increment `?v=` in `charting_sandbox/index.html`.

---

## Tools

- gh CLI: `gh` (on PATH)
- SEC filings: `python scripts/parse_sec_filing.py TICKER` — run with `--help` for full usage
- Obsidian CLI: `"/c/Users/klein/AppData/Local/Programs/Obsidian/Obsidian.com"` (requires Obsidian running). Key commands: `move`/`rename` (link-preserving), `search query=X`, `unresolved`, `backlinks file=X`, `--help` for full list. When opening notes for the user, use `obsidian://open?...&paneType=tab` for a new tab. If Obsidian still reuses a tab, focus Obsidian, send `Ctrl+T`, then open the note URI into the blank tab. Do not use the stale `newleaf=true` parameter.
- YouTube: `python scripts/transcribe_youtube.py URL --save output.txt` (`--language pt` for Portuguese)
- App: backend `charting_app/app.py` | dashboard `charting_sandbox/chart-dashboard.js` | tests `tests/`

---

## Vault Folders

| Folder | Contents |
|--------|----------|
| `Actors/` | Companies, orgs, people, **countries** (not Regions). See `India.md` for hub template. |
| `Analysts/` | Market analysts, strategists, commentators, and source-people whose frameworks or calls recur across notes. Use tags/role fields for strategist, analyst, economist, journalist, etc. |
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

**Data freshness and stale symbols:** If publicly available, find and ingest it. Use `/earnings TICKER` for full procedure. Update prices before generating charts if data >1 day old. Never remove historical data for delisted, acquired, bankrupt, or renamed tickers; keep legacy series for charts, audit trails, and deal/delisting analysis. Exclude dead or renamed symbols only from live refresh and mover screening. In notes, preserve them as "Former ticker" rather than live aliases when they would pollute `quick_movers`. `quick_movers.py` should prefer canonical `prices_long` and compare each ticker's latest non-null close to the latest [[SPY]] session before treating it as a current mover.

---

## Charts

Full reference: `docs/chart-api.md` | Start server: `python charting_app/app.py`

Always use `/api/chart/lw` for price charts. Key params: `tickers`, `start`, `normalize`, `primary` (actor = blue).

**Axis scale:** Charts that are not about returns must use a linear y-axis. Use log scale only for normalized return/performance charts (`normalize=true`, default `log_y=true`) or an explicitly return/growth-rate interpretation. Raw rates, yields, spreads, macro levels, fundamentals, segments, and other level/unit charts must keep `log_y=false`.

**Naming (CRITICAL):** `-vs-` format for comparisons (`aapl-vs-qqq-price-chart.png`). First ticker = blue (primary). Chart-refresh plugin parses tickers from filenames. Financial statements: `{ticker}-sankey.png`, `{ticker}-waterfall.png` (lowercase, no suffixes).

**Practices:** Peer comparisons (2-4 tickers), no titles (legend suffices), italicized interpretation below, charts must live in notes with data tables, ETF benchmarks get normalized comparison vs benchmark.

**Series coverage:** Every newly added database series must appear in at least one generated chart embedded in a vault note. Don't leave fresh price/macro series as DB-only or table-only artifacts; create or update the relevant chart in `investing/attachments/` and embed it where the series is discussed.

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

**Harvest provided/source charts:** Every chart or visualization provided by the user or present in an ingested source must be ingested. Save and embed the image with attribution when rights allow; otherwise extract its data/structure/takeaway into the relevant note and cite the source. Do not skip charts just because the article text was ingested.

**Cross-vault gate:** After new events or major updates, flag relevant sibling vaults (geopolitics, Brazil, history, technologies). Don't silently skip. See `docs/cross-vault-rules.md`.

**Full-entity sweep on ingestion:** When processing any source (article, transcript, filing), check ALL mentioned entities — not just primary subjects — for needed vault updates. Secondary mentions often reveal gaps: a company's existing note may be missing a partnership, a sector note may lack a competitive development, a Related section may be incomplete. The sweep includes: (1) reading each mentioned entity's note, (2) identifying missing facts or stale data, (3) updating secondary notes in the same pass. Don't extract data points from the primary subject and move on — process the full graph of entities touched by the source.

**Private companies:** Tag appropriately in frontmatter. Include funding rounds table where data exists (also for pre-IPO history of public companies).

**Printing — preserve wikilinks:** Any vault material sent to print (newsletter, note, report) must keep `[[wikilinks]]` visible in the output. Never strip the brackets. The reader wants to see what's linked to what on paper. Use the dedicated print script for the material type (e.g., `scripts/print_newsletter.py`) — never improvise with `Out-Printer` or `notepad /p`.

---

## Workflows

This repo hosts the cross-vault workflow skills. For architecture, vault scope, and the Claude/Codex/OpenClaw skill-parity model, see `WORKFLOWS.md` at the repo root.

- `/daily-scan` — autonomous daily market scan: sigma movers, ticker/IPO/private-capital audits, analyst watchlist, earnings calendar, pre-market briefing. See `.claude/skills/daily-scan/SKILL.md`. (Renamed from `/morning-scan` 2026-05-19 — the skill is time-of-day agnostic.)
- `/substacks [window]` — sweep ~84 tracked newsletter/Substack sources for new posts (default 48h); delegates per-post ingestion to `/ingest`. See `.claude/skills/substacks/SKILL.md`.
- `/news <source>` — article ingestion from a named source (Bloomberg, Reuters, FT, WSJ, etc.); delegates per-article ingestion to `/ingest`, then runs a downstream-impact check. See `.claude/skills/news/SKILL.md`.
- `/ingest` — single-source ingestion (interview, article, filing, screenshots). See `.claude/skills/ingest/SKILL.md`.
- `/earnings TICKER` — DB check, data insert, chart regen, note update. See `.claude/skills/earnings/SKILL.md`.
- `/report TOPIC` — read-only cross-vault synthesis on an existing topic. Saves to `investing/Reports/`. See `.claude/skills/report/SKILL.md`.
- `/explain TOPIC` — plain-language briefing on an existing vault topic for a reader unfamiliar with the actors and subtopics. Same gather as `/report`, journalistic-explainer voice with first-mention introductions and subtopic glosses. Saves to `investing/Reports/`. See `.claude/skills/explain/SKILL.md`.
- `/story [YYYY-MM-DD]` — daily "what is the story" report. Reads the daily note and every meaningful note/topic touched that day, then saves a compact story-card map to `investing/Reports/YYYY-MM-DD-story-report.md`. See `.claude/skills/story/SKILL.md`.
- `/replicate TICKER` — ETF/fund replication analysis with proxy mapping, synthetic indices, charts, and vault-note update. See `.claude/skills/replicate/SKILL.md`.

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
| Workflow architecture, vault scope, skill-parity model | `WORKFLOWS.md` |
| Chart API, forecasts, data setup | `docs/chart-api.md` |
| Note completion checklist | `docs/note-checklist.md` |
| News search, verification, sourcing | `docs/research-workflow.md` |
| Actor voice, synopsis, evolution, concept structure | `docs/vault-note-guide.md` |
| Actor/securities split, economics/prices split | `docs/vault-note-guide.md` |
| Cluster validation (correlation + hierarchical + PCA) | `docs/cluster-validation.md` |
| Cross-vault linking format and gates | `docs/cross-vault-rules.md` |
| Note templates, Related format | `[[Note structures]]` |
| Folder rules, concept vs sector | `[[Linking and hierarchy]]` |
| Financials templates | `[[Financials templates]]` |
| Thesis naming | `[[Thesis conventions]]` |
