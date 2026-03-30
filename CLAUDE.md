# Project Instructions

This project is an integrated system: **database → charts → vault**.

- **Database** stores raw data (prices, financials, short interest)
- **Charts** visualize that data as rich expressions
- **Vault** (Obsidian notes at `investing/`) provides meaning, narrative, and theses

---

## Daily Note Rules

When updating or creating notes, ALWAYS update TODAY's daily note (based on current date), never yesterday's. Before writing to a daily note, run `date` to confirm the current date.

After creating or expanding any entity note, ALWAYS log it in the daily note's summary section before finishing. Every stub created must also be logged. This is the #1 cause of compliance hook failures.

---

## Code Changes — Explore First

**Before modifying any code file, explore the surrounding codebase first.** Check for existing patterns, utility scripts, and similar implementations elsewhere in the project. Never edit a file you haven't explored the context of. The sequence is always: explore → understand existing patterns → write code that follows them.

## Workflow Changes — Map the Full System First

**Before changing any workflow, search the entire repo for all components of that workflow.** That means scripts, skills (`.claude/skills/`), docs, hooks, and CLAUDE.md itself. Follow dependency chains: a pre-creation check implies a creation workflow exists; a compliance rule implies an enforcement point. The question is always "where is this workflow actually defined end-to-end?" — not "which files do I already know about?"

---

## Git Workflow

**Direct push to main** — no PRs required. CI runs after push.

```bash
git add <files> && git commit -m "Description" && git push origin main
```

If CI fails, fix forward or `git revert HEAD && git push origin main`.

---

## Related Repos

This repo is the hub of a multi-vault research ecosystem. Full map in `~/.claude/CLAUDE.md`.

- **Geopolitics vault** (`~/obsidian/geopolitics/`, vault `geopolitics`) — Geopolitical events that move markets. Bidirectional cross-vault links via `obsidian://` URIs.
- **History vault** (`~/obsidian/history/`, vault `history`) — Historical precedents for current macro dynamics.
- **Brazil vault** (`~/obsidian/brazil/`, vault `Brazil News & Analysis`) — Brazilian politics/economy affecting BRL, B3, Brazilian ADRs, BCB rates.
- **Risk Parity vault** (`~/obsidian/risk-parity/`, vault `Risk Parity`) — Risk parity strategy research. Draws market data from this repo's database.
- **Art vault** (`~/obsidian/art/`, vault `art`) — Art-as-asset-class, alternative investments.
- **Technologies vault** (`~/obsidian/technologies/`, vault `technologies`) — Tech foundations behind AI/semiconductor investment theses.
- **portuguese** (`~/portuguese/`) — Gil's Portuguese tutoring platform (separate business domain).

---

## Tools & Locations

**Tools:**
- gh CLI: `gh` (installed via winget, on PATH)
- Playwright: `npx playwright install chromium` (first-time)
- SEC filings: `python scripts/parse_sec_filing.py TICKER --save filing.txt`
  - WebFetch gets 403'd by SEC — use this script instead
  - Run `python scripts/parse_sec_filing.py --help` for full usage (multi-filing, type selection, Q4 calculation)
- Obsidian CLI: `"/c/Users/klein/AppData/Local/Programs/Obsidian/Obsidian.com"`
  - Requires Obsidian desktop running (CLI talks to the app process)
  - Target vaults with `vault=investing`, `vault=geopolitics`, etc.
  - Use `move` / `rename` for link-preserving file operations (preferred over manual renames)
  - Use `unresolved`, `orphans`, `deadends`, `backlinks` for vault health checks
  - Use `search query=X` for full-text vault search
  - Full command list: run with `--help`
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
- Infrastructure: `investing/Infrastructure/` (chokepoints, pipelines, terminals, ports — fixed physical assets enabling trade/energy flows)
- Regions: `investing/Regions/` (multi-country only: LATAM, GCC, Southeast Asia)
- Concepts: `investing/Concepts/`
- Events: `investing/Events/`
- Theses: `investing/Theses/`
- Daily: `investing/Daily/`
- Sectors: `investing/Sectors/`
- Assets: `investing/Assets/` (securities notes — tradeable instruments, price history, relative value, charts for actors)

**Countries go in Actors, not Regions.** See `India.md` for hub template (~100-150 lines max).

**Products vs Actors:** Products lack agency — the parent Actor makes decisions. NVIDIA (Actor) → H100 (Product). See `[[Linking and hierarchy]]`.

**Product note gate:** When a major product launch is the catalyst for an actor note update (new chip, new platform, new vehicle — anything with its own specs, customers, roadmap, and competitive landscape), create the product note automatically in the same pass. Don't wait to be asked. The actor note keeps the strategic framing (Synopsis, business model, competitive analysis, Evolution); the product note carries the hardware/spec detail (specifications, competitive comparison table, customer list with use cases, economics, roadmap, market discovery timeline). The actor note links to the product note with a summary paragraph. This prevents actor notes from bloating with spec tables while keeping the vault atomically linked. See [[Arm AGI CPU]] as the reference template for product notes tied to a strategic pivot.

**Product note: market discovery timeline (required).** Every product note must include a "Market discovery timeline" section — a chronological table tracking how information about the product became public and how the market priced each disclosure. This covers: rumors/leaks, official announcements, spec reveals, customer confirmations, revenue/guidance disclosures, and the stock price reaction at each step. The analytical value is in the gaps: what the market knew versus what surprised it, and where the actual move came from. A product launch that was "expected" but still moved the stock 16% tells you the surprise was in the *scale*, not the *existence* — that's the kind of insight the timeline makes legible. For products with less public buildup (e.g., a quiet launch), the timeline can be shorter, but it should still exist.

**Infrastructure vs Products vs Actors:** Infrastructure is for fixed physical assets that enable trade/energy flows but don't have agency: straits (Hormuz, Malacca, Danish Straits, Turkish Straits), pipelines (East-West, Habshan-Fujairah, SUMED, IPSA, Goreh-Jask), terminals/hubs (Ras Laffan, Kharg Island). Products are manufactured goods. Actors are entities with agency (companies, countries, people). An emirate like Fujairah stays in Actors (it has a government); its pipeline stays in Infrastructure.

**Sector hubs vs subsector notes:** Sector hub notes (e.g., `Defense.md`) are for structure — correlation data, sub-sector taxonomy, key programs. Market reaction data (price moves, catalyst analysis) goes in subsector notes (e.g., `Defense Primes.md`, `Drones.md`). Don't put live market data in the hub.

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
- **ETF/fund benchmark charts** — any ETF or fund with a benchmark must have a normalized comparison chart plotting the fund against its benchmark (e.g., IBIT vs BTC-USD, a tech ETF vs QQQ). Use `/api/chart/lw` with `normalize=true`. The benchmark chart replaces a solo price chart — no need for both.

### Chart Naming Convention (CRITICAL)

**Use `-vs-` format for comparison charts** (e.g. `aapl-vs-qqq-price-chart.png`). The obsidian-chart-refresh plugin parses tickers from filenames to auto-refresh. First ticker becomes blue (primary).

Exceptions, fallbacks, and plugin limitations: see `docs/chart-api.md` and `investing/chart-registry.md`.

### Financial Statement Charts

Sankey and waterfall charts use a fixed naming convention:

```
{ticker}-sankey.png           # income statement Sankey flow diagram
{ticker}-waterfall.png        # income statement waterfall bar chart
```

Examples: `aapl-sankey.png`, `orcl-waterfall.png`. Always lowercase ticker. No `-chart` suffix, no date suffix. Same ticker always overwrites the previous version — these show the latest fiscal year by default.

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
- **Event notes for multi-actor stories** — when a single event touches 3+ actor notes (e.g., a deal, a policy announcement, a market event), create a dedicated event note in `Events/` with the full detail. Actor notes carry short summaries + `[[link]]` to the event note. Prevents duplication, keeps actors focused.

### Terse Prompts

When the user gives a terse entity name (e.g., 'fermi america', 'nikki beach'), assume they want to check if a note exists and potentially create one. Do not ask for clarification on what the entity is — research it.

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

- **Bold formatting is banned** in note bodies except for section headers and the note name on its first appearance. Not for emphasis, not for key terms, not for evolution bullet openers. This is a hard rule — compliance hooks catch it.
- **All entity references must use `[[wikilinks]]`** — every company, person, product, concept, country mentioned in a note gets linked, no exceptions. If the target note doesn't exist, link it anyway (it becomes a stub candidate).
- **Every note must have frontmatter** — aliases, tags, and relevant metadata. Notes without frontmatter fail compliance checks.
- Private companies must be tagged appropriately in frontmatter
- Always include a funding rounds table where funding data exists — this applies to private companies and to the pre-IPO history of public companies

### Actor Note Philosophy: Executive Brief + Comprehensive Primer

An actor note serves two functions simultaneously:

1. **Frame the key economic value questions.** The Synopsis distills the 3-5 durable questions that determine the entity's economic value — not "what's the stock doing" but "what determines whether this entity is worth more or less." These questions should still be relevant six months from now.

2. **Provide everything the reader needs to answer those questions independently.** The body is a comprehensive primer: ownership structures, financials, competitive dynamics, regulatory context, technology, history. A complete actor note is self-contained — the reader shouldn't need to look elsewhere to understand the entity or evaluate its value.

Stock price moves, analyst calls, and catalysts go in the securities note (`Assets/`), not the actor note. The actor note cites earnings numbers and business events; the securities note tracks how the market priced them. See the Actor/Securities Split section below.

**Synopsis framing: key economic questions, not market recap.** The Synopsis should center on the questions that matter: Is the core business durable? Is the valuation justified? What structural forces help or hurt? Not "the stock doubled after CES" but "the valuation depends on whether Boston Dynamics' robotics business is real or speculative optionality." Catalysts are evidence — "BD IPO → governance restructuring → Korea discount unwind" supports the question "can the structural discount close?" rather than standing as a standalone listicle.

**Answer your own questions.** The body must contain analytical sections that directly address the Synopsis questions — not just factual/historical sections that provide raw material. If the Synopsis asks "can the business survive the regulatory assault," the body needs a section that presents the dynamics and evidence, not just a timeline of events. History, ownership, and financials are inputs; the note isn't complete until those inputs are synthesized into analysis the reader can evaluate. A note that frames three questions and then provides only chronological facts is half a note.

**No bull/bear framing.** Do not organize analysis into "bull case" / "bear case" sections. This forces editorial binary thinking — reality is more nuanced, and the vault's job is to present dynamics and open questions, not pre-package conclusions. Instead: present what's happening (the dynamics driving the entity), what's structurally different or historically consistent (grounded in data), and what's unresolved (the open questions). The reader decides what it means for positioning. Same applies to "risks vs. opportunities," "positives vs. negatives," and any other binary editorial frame.

**Sum-of-parts in prose.** When a SOTP structure exists, state it plainly with numbers inline: "BNP Paribas calculates the core auto business trades at just 10.3x PE after stripping out BD and India."

**Voice and density: the Hyundai standard.** Every actor note should read like a sharp analyst briefing someone smart over coffee — not a Wikipedia article, not a consulting deck. Lead with what matters most. Stack dynamics with specific numbers and chain logic (BD IPO → governance restructuring → Korea discount unwind). Use analyst quotes as named evidence ("Samsung Securities analyst Esther Yim:"), not anonymous authority. State SOTP math in plain English. The following Hyundai Motor summary is the gold standard for tone, density, and structure — all actor note Synopses and body sections should aspire to this voice:

> Hyundai traded sideways at 100K-300K KRW for a decade. After the Atlas humanoid debut at CES 2026 (Jan 5), it doubled to 674K KRW. Now pulled back to 492K KRW (~27% off peak). Forward PE ~9.6x.
>
> Three dynamics are driving the repricing:
>
> 1. Boston Dynamics IPO (potentially 2027 Nasdaq). Hyundai owns 88% (affiliates 68% + Chairman Chung Euisun personally 22.6%). Valuations range wildly: KB Securities 128T won, Hanwha 150T won, others 40-60T won. Chung paid ~$220M for his 20% stake — could be worth $13.6B+. SoftBank holds 9.5% with a put option exercisable by June 2026. CEO Robert Playter just left, replaced by CFO Amanda McMaster — commercial pivot signal. Atlas production target: 30,000 units by 2028 at $130-140K each.
> 2. Governance restructuring. BD IPO proceeds give Chung the war chest to unwind Hyundai's circular ownership (the only major Korean chaebol that still has it). Inheritance tax on his father's 7T+ won stake alone is ~4T won. This has been a decade-long investor complaint — resolution would trigger a Korea discount unwind.
> 3. Google DeepMind partnership for Atlas AI + Nvidia for autonomous driving. Previously the knock on Atlas was Tesla Optimus had the data advantage. DeepMind collaboration changes that equation. Samsung Securities analyst: "If robotics and solid-state battery tech are validated, Tesla — not Toyota — becomes the valuation comp."
>
> Open questions: Analysts cut 2026 earnings estimates 22% on tariffs at 25% on Korea (deal to reduce to 15% but Korean legislature hasn't ratified). Pulled IONIQ 6 from US market (tariff-exposed, made in Korea); IONIQ 5/9 safe (Georgia plant). Chinese EVs eating market share outside US/India. $20B US investment + $5.8B Louisiana steel plant is political insurance but capital-heavy. BNP Paribas calculates the core auto business trades at 10.3x PE after stripping out Hyundai Motor India + Boston Dynamics — the SOTP math hinges on what BD IPO actually prices at and whether the governance restructuring materializes.

### Synopsis (Actor Notes)

Every actor note (non-stub) must include a synopsis immediately after the frontmatter/one-liner intro and before Quick stats. No `## Synopsis` header — the position does the work (always between the one-liner and Quick stats). This is a 2-4 paragraph dense summary that frames the key economic dynamics and gives the reader the full picture without scrolling: what the entity is, the dynamics driving it, and the open questions. Write it as sharp prose with hard numbers — not a teaser, but a self-contained briefing. If someone reads only the synopsis, they should understand the entity and what questions remain unresolved.

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

### Concept Note Structure: Story + Reference

Concept notes (non-stub) must follow a **story + reference** structure. The narrative exposition leads; structured reference material supports.

**Structure:**
1. **One-liner** — frontmatter + single paragraph: what it is, why it matters, current state. Dense, self-contained.
2. **The story** — the full narrative arc as connected analytical prose. This is the core value of the note. Each paragraph exists because the previous one demanded it. Trace the causal chain: physics/fundamentals → economics → ecosystem/players → implications. A reader who knows nothing about the domain should be able to follow the full arc and understand the investment case by the end.
3. **Reference** — tables, specs, quick stats, company lists, timeline data, key quotes. Scannable, precise, linkable. Everything the vault already does well, but positioned as the supporting layer you drill into for specifics.
4. **Related** — wikilinks to connected notes.

**Writing rules for "The story" section:**
- Sharp analytical prose, not bullet points or tables. No headers within the story — it reads as continuous exposition.
- Each section explains WHY something matters and how it leads to the next thing. Cause → effect chains, not isolated facts.
- Hard numbers inline with sources. "[[Broadcom]]'s numbers: 800Gbps port, pluggable at 15W versus CPO at 5.5W" — not "CPO is more power-efficient."
- All entity references get `[[wikilinks]]` even within prose.
- Don't editorialize without evidence. Show the reader what happened and let them draw conclusions.
- The story should be self-contained — a reader who reads only this section understands the full picture.

**Length:** Scale to complexity. A narrow concept (a single mechanism or pattern) might need 5-8 paragraphs. A broad technology transition with multiple domains, competing approaches, and ecosystem dynamics might need 15-20. The story section can be the longest section in the note.

**Reference:** See [[Co-Packaged Optics]] for the template — narrative traces fermion/boson physics → power wall → two-domain analysis → engineering challenges → pluggable counterattack → timeline → investment read. Reference section below carries NVIDIA roadmap table, power comparison data, XPO specs, key quotes, industry player matrix, adoption timeline.

**When to use this structure:** Any concept note where the reader benefits from understanding the causal chain, not just the facts. Technology transitions, market dynamics, structural themes, policy mechanisms. Not every concept note needs a 15-paragraph story — some (e.g., a narrow technical definition) are fine as structured reference. Use judgment.

### Actor / Securities Split

Actors with tradeable instruments get a two-note structure: the actor note (what the entity is and does) and a securities note (how the market prices it and how to express a view).

**The actor note** covers the entity itself — Synopsis, Evolution, business economics, financials, competitive dynamics, capex, strategy, management. Everything about what the entity IS and DOES, regardless of whether a stock exists. Earnings numbers go here; stock reactions go in securities.

**The securities note** covers all tradeable instruments linked to the actor and their price dynamics:

1. Instruments — what exists (stock, bonds, ETFs, options, derivatives, cross-listings)
2. Price history — absolute price chain (chronological: what event, what price, what effect)
3. Relative value — beta-adjusted ratios against sector/peers, with chronological explanatory chain
4. Sector correlation — correlation table with relevant ETFs
5. Earnings reactions — stock moves on results (the numbers themselves stay in the actor note)
6. Analyst coverage — PTs, ratings, upgrades/downgrades
7. Market expectations — what's priced in, what isn't
8. Charts — all price/comparison charts

The boundary is crisp: "Is this about the entity or about the market's pricing of the entity?"

**Naming:** `[Actor name] securities` — lowercase "securities" keeps the actor name dominant. Examples: `Micron securities`, `Brazil securities`, `NVIDIA securities`.

**Folder:** Securities notes live in `investing/Assets/`.

**Linking:** Actor note links to securities note in Related under `### Securities`. Securities note links back to actor as first Related entry. The same event can appear in both — earnings numbers in the actor note, the stock move in the securities note.

**Applies to:** Any actor with tradeable instruments — companies (stock, bonds, options), countries (ETFs, ADRs, FX, sovereign bonds, CDS), institutions.

**Does NOT apply to:** Actors without tradeable instruments (most people, some private companies). Stubs don't need a securities note — create when there's enough market content to justify it.

**Reference:** See [[Micron]] and [[Micron securities]] as the template.

### Economics / Prices Split (Concepts Only)

For non-actor concepts with tradeable prices (commodities, rates, currencies), the Economics/Prices split still applies. This is for things that don't have an "actor" — uranium, oil, gold, treasuries, yen.

**The Economics note** covers how the thing works — supply, demand, structure, players, mechanics. Story + reference structure.

**The Prices note** has two aspects, both chronological explanatory chains:

1. Absolute price — the number and what put it there.
2. Relative price — against correlated markets and peers, always risk/beta-adjusted.

Relative prices must be risk-adjusted — a stock outperforming its benchmark by 20% means nothing if its beta is 2x. State the beta, adjust the ratio, then explain the residual.

**Naming:** `Uranium Economics` / `Uranium Prices`. The name does the work.

**Folder:** Both live in `Concepts/`.

**Does NOT apply to:** Purely analytical concepts (Moore's Law, Jevons Paradox), structural concepts (advanced packaging, co-packaged optics), or anything without a tradeable price. Also does not apply to actors — use the Actor/Securities split instead.

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

**Scope rule:** Military operations, diplomatic timelines, casualty counts, and strategic assessments belong in the geopolitics vault. This vault covers the market impact — price action, sector moves, portfolio implications. When a geopolitical event moves markets, create the core event note in geopolitics and a market-impact note here, cross-linked.

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

**Post-ingestion gate:** After creating a new event or making a major update, check all four sibling vaults:
- **Geopolitics** — statecraft, sanctions, diplomatic precedent, alliance dynamics, infrastructure competition
- **Brazil** — Brazilian actors, markets (BRL, DI, Ibovespa, ADRs), domestic policy/institutions
- **History** — structural breaks, first-of-kind precedents, long-arc patterns
- **Technologies** — foundational tech shifts (chips, fabs, AI architectures, supply chains)
Flag relevant vaults to the user. Don't silently skip — the default is to ask. Routine updates to existing notes don't trigger this.

**History vault reference:** The **history vault** (`C:\Users\klein\obsidian\history\`) covers long-arc economic history — trade, institutions, innovation from prehistory to modernity. When writing about a topic with deep historical roots (sanctions, trade wars, infrastructure control, monetary policy, commodity economics, Monroe Doctrine, etc.), check the history vault for relevant precedent. When an event represents a genuine structural break or first-of-its-kind precedent (novel sanctions mechanism, new form of economic statecraft, industry-reshaping consolidation), flag it for the history vault — today's inflection points become tomorrow's history.

**Brazil vault gate:** The **Brazil vault** (`C:\Users\klein\obsidian\brazil\`) covers domestic Brazilian politics, economy, and institutions. When a story involves Brazilian actors (Lula, BCB, Petrobras, B3, STF, Congress), Brazilian markets (BRL, DI curve, Ibovespa, Brazilian ADRs), or Brazil-specific policy (fiscal framework, tax reform, Mercosul), flag it for the Brazil vault. The investing vault keeps the market-impact angle; the Brazil vault keeps the domestic political/institutional angle. Both need the core facts.

**Technologies vault gate:** The **technologies vault** (`C:\Users\klein\obsidian\technologies\`) covers tech foundations — semiconductors, AI architectures, quantum, crypto infrastructure. When a story involves foundational tech shifts (new chip architectures, fab capacity, AI model breakthroughs, supply chain restructuring) rather than just company earnings, flag it for the technologies vault. The investing vault covers the companies and trades; the technologies vault covers the underlying technology and its trajectory.
