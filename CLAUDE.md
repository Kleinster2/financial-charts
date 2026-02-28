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

## Known Limitations

Dead ends that recur across sessions. Do NOT attempt these — use the documented workarounds.

### Web Access
- **SEC EDGAR**: WebFetch gets 403'd. ALWAYS use `python scripts/parse_sec_filing.py TICKER` — never attempt WebFetch on sec.gov URLs.
- **Bloomberg**: Blocked via both WebFetch (403/paywall) AND Playwright (no browser cookies). There is no automated workaround — ask the user to paste article text or provide a summary.
- **Paywalled data sources**: PitchBook, cbonds, Fitch credit reports, SPAC Research — do not attempt to scrape. Ask the user for the data or use alternative free sources.
- **Playwright and authenticated sites**: Playwright uses its own browser context without cookies. It cannot access any site the user is logged into via Chrome. Use the Claude-in-Chrome MCP tools for authenticated browsing instead.

### Data Pipeline
- **Alpha Vantage rate limit (25/day free tier)**: `fetch_fundamentals.py` silently "succeeds" but stores 0 rows when rate-limited. The API returns a rate-limit message that the script doesn't detect. This produces 44-byte error JSON files that crash image reading. **Workaround**: manually insert fundamentals from StockAnalysis.com via SQL. If a chart returns a 44-byte file, do not attempt to re-fetch — Alpha Vantage is likely rate-limited for the day.
- **44-byte chart files**: Any chart output under 1KB is an error JSON, not a PNG. **Hard gate**: always check file size with `wc -c` BEFORE attempting to Read as an image. Never read a sub-1KB "chart" file.

### Windows/Environment
- **Background Flask server**: `python charting_app/app.py &` does NOT work on Windows/Git Bash (`APP_PID=: command not found`). ALWAYS use `app.test_client()` for smoke testing. Never attempt `&` background processes.

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

### Note Formatting

- Do NOT use bold (`**text**`) inside note bodies except for section headers and the note name on its first appearance in the body
- All entity references must use `[[wikilinks]]`
- Private companies must be tagged appropriately in frontmatter
- Always include a funding rounds table where funding data exists — this applies to private companies and to the pre-IPO history of public companies

### Synopsis Section (Actor Notes)

Every actor note (non-stub) must include a **Synopsis** section immediately after the frontmatter/one-liner intro and before Quick stats. This is a 2-4 paragraph dense summary that gives the reader the full picture without scrolling: what the entity is, the deal/structure mechanics if relevant, why it matters (valuation unlock, thesis, market opportunity), and the key risk. Write it as sharp prose with hard numbers — not a teaser, but a self-contained briefing. If someone reads only the synopsis, they should understand the investment case.

### Evolution Section (Actor Notes)

Company, country, and institution actor notes should include an **Evolution** section that tells the full story of how the entity became what it is today. This is narrative history with analytical teeth — not a bullet-point timeline, but a chronological account where each entry explains *why* that moment mattered and what it caused.

**Style:** Each bullet is a year or era, written as a dense paragraph. Open with a thesis sentence that frames the arc ("The story of X is the story of Y"). Each entry should:
- Start with the date/era
- State what happened
- Explain *why* it mattered — the strategic logic, the mistake, the consequence
- Connect to what came before and after (cause → effect chains)
- Include hard numbers (valuations, GPV, MAU, stock prices) to anchor the narrative

**What to cover:** Founding story, key pivots, acquisitions (with deal terms and whether they worked), leadership changes, crises, stock/valuation inflection points, competitive dynamics, and the current state. Don't skip the failures — a $29B acquisition that closed at $13.9B tells you more about management than five years of revenue growth.

**What NOT to do:**
- Don't write a dry timeline ("2018: Acquired X for $Y")
- Don't skip years where nothing happened — if there's a gap, the gap is the story (stagnation, quiet building, etc.)
- Don't editorialize without evidence — every opinion should be backed by a number or a fact in the same bullet

**Length:** Scale to the company's complexity. A startup with 3 years of history needs 3-4 bullets. A company like Block with 17 years of pivots, acquisitions, and drama needs 10-12 dense paragraphs. The Evolution section can be the longest section in the note — that's fine. The reader should finish it understanding not just *what* the company is, but *how* and *why* it got there.

**Template opening:** "The story of [Company] is the story of [core tension/arc]."

**Reference:** See [[Block]] for the gold standard — founding origin story, IPO discount explained by dual-CEO risk, Cash App pivot from Venmo clone to neobank via Bitcoin/stocks hooks, COVID acceleration, peak-hubris acquisition spree, stock collapse, austerity, and AI restructuring. Each bullet explains something about the present.

**Other rules:**
- Wikilink to other investing vault entities (companies, products, people) mentioned in the evolution
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

### Price Data Integrity

**Never write stock price moves into a note without verifying against actual closing prices first.** No secondary sources (cron summaries, article headlines, after-hours estimates). Pull the tape from yfinance or the charting app before committing numbers. If you can't verify, flag it as unverified. Getting the direction right but the day wrong is still wrong.

### Writing Style

Vault prose should be **sharp, not sterile**. Keep the punch and readability of conversational writing. Structure is good (strengths/risks/bull/bear), but don't sand off the edge to sound "professional." This is personal research — it should read like a smart person's honest take, not a consulting deck. If a casual explanation is clearer than a formal one, use the casual one.

### Vault Philosophy

**Super analytical, factual. No assuming before extremely thorough homework.**

The vault is a research engine, not a hot-take factory. Every claim should be backed by data, primary sources, or verified facts. When the story looks obvious, dig deeper — the real insight is usually in the details that surface only after thorough research (e.g., the minute-by-minute Sarandos White House timeline revealed the political dynamics behind what looked like simple "financial discipline"). 

- Don't speculate when you can research
- Don't summarize when you can get the primary source
- Don't write "presumably" or "likely" when 10 more minutes of digging would give you the answer
- When something doesn't add up (price action timing, conflicting narratives), investigate — don't paper over it
- The vault earns its value by being more thorough than what's freely available. If it's just restating headlines, it's not worth having.

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
