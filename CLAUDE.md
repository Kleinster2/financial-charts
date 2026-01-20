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

**ALWAYS use the charting app API. NEVER use matplotlib or other tools to generate charts.**

The charting app produces consistent, high-quality charts with proper styling (LightweightCharts). Matplotlib charts look different and break visual consistency.

### Headless export via API (preferred)

The `/api/chart/lw` endpoint generates charts headlessly using Playwright — no browser needed.

1. **Start the app:**
   ```bash
   cd /c/Users/klein/financial-charts
   python charting_app/app.py
   ```

2. **Export via curl:**
   ```bash
   # Single ticker (raw prices, log scale)
   curl "http://localhost:5000/api/chart/lw?tickers=AAPL&start=2020-01-01" \
     -o investing/attachments/aapl-price-chart.png

   # Comparison chart (normalized to 0%, with legend)
   curl "http://localhost:5000/api/chart/lw?tickers=AAPL,QQQ&start=2020-01-01&normalize=true" \
     -o investing/attachments/aapl-vs-qqq.png

   # Custom dimensions
   curl "http://localhost:5000/api/chart/lw?tickers=NVDA&width=1600&height=800" \
     -o investing/attachments/nvda-wide.png
   ```

**API parameters:**
| Parameter | Description | Default |
|-----------|-------------|---------|
| `tickers` | Comma-separated (required) | — |
| `start` | Start date (YYYY-MM-DD) | All data |
| `end` | End date (YYYY-MM-DD) | Today |
| `title` | Chart title | Ticker list |
| `width` | Image width px | 1200 |
| `height` | Image height px | 600 |
| `show_title` | Show title on chart | true |
| `normalize` | Rebase to 0% for comparison | false |

### Comparison charts (normalize=true)

For comparing multiple tickers, use `normalize=true`:
- All series rebased to **0% at start date**
- Y-axis shows **percentage change** (+50%, -10%, etc.)
- **Log scale** preserved for proper ratio visualization
- **Legend** auto-generated showing ticker names with colors
- **Title hidden** (legend is sufficient for multi-ticker charts)

This matches the dashboard's "Show % Basis" mode.

### Manual export (alternative)

If you need interactive configuration:
1. Open `http://localhost:5000` in browser
2. Configure chart (tickers, date range, overlays)
3. Right-click → "Export as PNG" or use `ChartExport.exportToPNG(chart, { filename: 'name.png' })`
4. Move to `investing/attachments/`

### Naming conventions

| Pattern | Example |
|---------|---------|
| Single ticker | `aapl-price-chart.png` |
| Comparison | `tsmc-vs-samsung-foundry.png` |
| With date range | `nvda-2024-rally.png` |
| Event-specific | `saks-bond-prices-collapse-2025-2026.png` |

### When charts need updating

```bash
# Re-export with same filename to overwrite
curl "http://localhost:5000/api/chart/lw?tickers=AAPL&start=2020-01-01" \
  -o investing/attachments/aapl-price-chart.png
```

**Do NOT regenerate charts with matplotlib** — it produces inconsistent styling.

## Pending Design Decisions

### Short interest charting integration

**Status:** Database and API complete, UI integration pending.

**Context:** Short interest data is stored in `short_interest` table (normalized: ticker + settlement_date) with API endpoints `/api/short-interest` and `/api/short-interest/latest`. Need to decide how to expose SI time series in the charting UI.

**Options:**
- **A) Synthetic tickers** — `AAPL_SI_PCT`, `AAPL_SI_DAYS`, etc. Most consistent with existing architecture.
- **B) Separate chart overlay** — New UI component to overlay SI on price charts.
- **C) Wide table** — Add to existing `/api/data` endpoint via wide-format table.

**Related files:**
- `scripts/update_short_interest.py` — fetcher (yfinance)
- `charting_app/app.py` — API endpoints
- `investing/Concepts/Short interest.md` — vault concept note

---

# Vault Guidelines

## Philosophy

This is an Obsidian vault. Follow Obsidian philosophy:

- **Atomic notes** — one idea per note, no mega-documents
- **Self-contained** — each note tells its complete story; links are for depth, not basic comprehension
- **Links over hierarchy** — structure emerges from `[[connections]]`, not folders
- **Organic at the bottom, deliberate at the top** — actors/concepts grow organically as encountered; sector hubs are deliberate scaffolding that can start sparse
- **Daily notes as inbox** — capture first, extract atomic notes when ideas mature
- **Hubs can have dangling links** — sector hubs guide where new notes land; empty `[[links]]` fill in over time

## Self-contained notes

**A reader should understand the full story without clicking any links.**

Links provide depth and specificity, not basic comprehension. If understanding a note requires clicking through to other notes, the note is incomplete.

| Wrong | Right |
|-------|-------|
| "The $5B debt came from [[Saks-Neiman merger]]" (reader must click to understand) | "In late 2024, Baker orchestrated a $2.7B acquisition of Neiman that loaded $5B in debt..." then link [[Saks-Neiman merger]] for full deal details |
| "[[Richard Baker]] was replaced as CEO" (who is he?) | "Richard Baker—real estate investor who built Saks through acquisitions—was replaced as CEO" then link [[Richard Baker]] for his full history |

**The test:** Can someone reading ONLY this note understand the narrative? Links should make them want to learn more, not leave them confused.

**What links are for:**
- Drilling deeper into a specific actor's full history
- Exploring a concept's broader implications
- Finding related events or patterns
- Navigating to connected notes

**What links are NOT for:**
- Replacing inline context needed to understand the current note
- Hiding essential information behind a click
- Avoiding repetition at the cost of comprehension

**Repetition is acceptable** when needed for comprehension. If three notes all need to explain that "Richard Baker was a real estate investor who acquired department stores to monetize their property"—that's fine. Each note should stand alone.

## Numbers matter

**Never overlook hard data.** When ingesting news or research, capture:

- Financial metrics (margins, costs, revenue, market share)
- Operational data (capacity, yields, volumes, timelines)
- Comparisons (vs competitors, vs prior periods)
- Source and date for all data points

Use tables for structured numeric data. Qualitative narrative without quantitative support is opinion.

**Bad:** "TSMC's US fabs have lower margins"
**Good:** "Taiwan 62% gross margin vs US 8%, depreciation +386%, labor +100% (SemiAnalysis, Nov 2025)"

## Charts and images

**Always acknowledge charts when attached.** When the user shares screenshots or images:

1. Explicitly confirm you see the chart(s)
2. Extract and list the key data points
3. Add the data to relevant notes (don't just summarize — capture the numbers)

If multiple charts are attached, process each one. Don't assume article text contains all chart data — charts often have unique data not in the text.

### Saving images to the vault

When the user wants to save an image they've shared in the conversation:

1. **Find the image in Claude's cache:**
   ```bash
   find "/c/Users/klein" -maxdepth 4 -name "*.png" -mmin -5 2>/dev/null
   ```
   Images shared in Claude Code are stored at: `~/.claude/image-cache/<session-id>/<n>.png`

2. **Copy to attachments folder:**
   ```bash
   cp "/c/Users/klein/.claude/image-cache/<session-id>/<n>.png" \
      "/c/Users/klein/financial-charts/investing/attachments/<descriptive-name>.png"
   ```

3. **Embed in the relevant note:**
   ```markdown
   ![[descriptive-name.png]]
   ```

**Attachments folder:** `investing/attachments/` — configure Obsidian to use this as default attachment location (Settings → Files & Links → Default location for new attachments).

**Naming convention:** Use descriptive kebab-case names like `global-dc-water-stress.png`, `us-power-prices-2025.png`.

## Author framing matters

**Capture the thesis, not just the data.** When processing articles:

1. **Read the headline** — it often contains the author's main argument
2. **Note hedging language** — "may", "unclear", "shrouded in mystery" = uncertainty
3. **Don't assume causation** — two charts side by side doesn't mean one causes the other
4. **Capture the interpretation** — what does the author *conclude*, not just what data they present

**Bad:** "Productivity +4.9%, AI adoption 18% → AI is driving productivity"
**Good:** "Productivity +4.9%, AI adoption 18%, but article says cause is 'shrouded in mystery' — correlation not proven"

Popular narratives (like "AI boosts productivity") can bias interpretation. Let the author's framing guide the note.

---

## Dating investment calls

**Always include dates on positioning and investment calls.** Calls go stale — a bullish call from 6 months ago may no longer be valid.

When recording firm positioning or analyst views:
1. Include the date in the section header (e.g., `### Goldman Sachs — Jan 6, 2026`)
2. Add source attribution (e.g., `*Source: Bloomberg interview*`)
3. Note if a position has changed (e.g., "Was overweight 1yr ago")

This applies to: Asset allocation notes, thesis updates, strategist calls, price targets.

## When creating notes

**Notes should be atomic (single topic) but extremely thorough.**

- **Always do deep research** before creating a new note — web search, multiple sources, hard data
- Link liberally with `[[wikilinks]]`
- Prefer linking to an existing note over repeating information
- If a concept doesn't have a note yet, create one (or leave a dangling link for later)
- Don't add structure that doesn't emerge naturally

### Actor note requirements

| Actor type | Required content |
|------------|------------------|
| **Public companies** | Extensive historical financials (revenue, margins, growth rates, valuation multiples) |
| **Private companies** | Cap table (investors, rounds, valuations, total raised) |
| **Research shops / funds** | Key analysts, AUM, notable positions, recent calls |
| **Individuals** | Role, affiliations, key decisions, track record |
| **Geographies** | Economic data, key sectors, policy environment |

**No thin stubs.** If you don't have time to research properly, add to daily note instead and create the actor note later.

### "What makes X, X" analysis

**Go beyond facts to explain why something works.** The best notes answer: "What makes this actor unique, durable, or important?"

| Element | Question to answer |
|---------|-------------------|
| **Flywheel** | What reinforcing loops drive success? |
| **Moats** | What can't be copied? Why is this durable? |
| **Structural advantage** | What design choices create leverage? |
| **The math** | What economic logic makes this work? |

**Example — Y Combinator:**
- Facts: "5,300 companies, $500K for 7%"
- Analysis: "Network effect business disguised as an investment fund. 1% acceptance → prestige → better applicants → better outcomes → stronger brand. The alumni graph (5,300 nodes helping each other) can't be copied."

**When to add this analysis:**
- Accelerators, VCs, platforms with network effects
- Companies with unusual business models
- Any actor where "why it works" isn't obvious from the facts
- Entities with compounding advantages

This transforms notes from "reference material" to "understanding."

## When editing existing notes

**Every edit is an opportunity to rebuild.**

When touching a note for any reason (adding news, updating data, fixing links), assess whether the note meets current quality standards:

| Check | Action if failing |
|-------|-------------------|
| Thin stub (< 100 words) | Rebuild with deep research |
| Missing founder/key people section | Add or link to founder notes |
| No financials (public company) | Add 10-year annual + 12-quarter tables |
| No cap table (private company) | Add funding rounds, investors, valuations |
| Redundant info duplicated elsewhere | Slim down, link to canonical source |
| Outdated data (> 1 year old) | Refresh with current figures |
| No Related section | Add annotated links |

**Workflow:**
1. Make the requested edit first
2. Scan the full note for quality gaps
3. If gaps exist and time permits, rebuild in the same session
4. If no time, add to daily note as open thread: `- [ ] Rebuild [[Actor Name]] — missing X`

**Founder/company separation:** Biographical detail about individuals belongs in person notes (e.g., [[Ray Dalio]]), not company notes (e.g., [[Bridgewater]]). Company notes should link to founder notes and focus on firm performance, funds, structure.

## When suggesting work

- Don't propose top-down reorganization
- Suggest adding links to existing notes
- Suggest new atomic notes, not comprehensive documents
- Daily notes are the entry point for new information

## Processing new information

**Every piece of news needs an atomic home — daily notes are never the only location.**

### Check existing notes first

**Before searching the web, check what the vault already knows.**

When the user asks about a topic or wants updates:

1. **Search the vault first** — grep for actors, concepts, events
2. **Read existing notes** — understand current coverage depth
3. **Then search externally** — web, news, sources
4. **Present only the delta** — new info not already in notes

| Wrong | Right |
|-------|-------|
| Search web → dump all findings | Check notes → search web → report only new info |
| Present 10 facts, 8 already in notes | "Notes are comprehensive; one new detail: X" |

**Why this matters:** The vault often has deeper coverage than news articles. Presenting info the user already has wastes their time.

### Finding the right home

Before creating a catch-all concept, ask: **are there actors missing from the vault?**

| Wrong | Right |
|-------|-------|
| News about margin tightening → create "China equity market regulation" concept | News about margin tightening → create Shanghai/Shenzhen/Beijing Stock Exchange actor notes |
| News about Fed policy → add to high-level "Federal Reserve" note | News about Fed policy → create specific actor (FOMC, specific governor) or event note |

**The principle:** News is created by actors taking actions. Find the actors first. Concepts describe dynamics and patterns, not catch-all buckets for news.

### Regional actors stay high-level

Regional actor notes (China, Brazil, EU, Japan) should be **high-level scaffolding**, not dumping grounds for every piece of regional news. They link to:
- Specific actors within the region (companies, exchanges, regulators)
- Concepts about regional dynamics
- Events that happened there

**Bad:** Add margin tightening details to China.md
**Good:** Add margin tightening to China A-share exchanges.md, link from China.md

### Search before proposing

1. **Grep for key terms** — actors, concepts, themes mentioned in the article
2. **Read top 2-3 matches** — understand what already exists
3. **Propose updates to relevant notes** — not just daily note
4. **Don't force weak connections** — "both mention India" is not a connection

**Bad:** Article about India tariffs → link to Reliance battery note (both mention India)
**Good:** Article about India tariffs → update [[India]], [[India-China relations]], [[US-China tariffs]]

The goal is enriching existing notes with new information, not just logging to daily note.

### Always update daily notes

**When processing any news, always add to the appropriate daily note.**

1. **Use the event date, not the article date:**
   - Article published Jan 17 about a deal announced Jan 14 → add to Jan 14 daily note
   - Look for phrases like "announced Tuesday", "filed yesterday", specific dates in the text
   - If unclear, use the earliest date mentioned
2. **Add to the correct daily note:**
   - Create the daily note if it doesn't exist
   - Use the standard daily note structure
3. **Update actors/concepts AND daily note** — not just one or the other

**Workflow:**
```
User shares news →
  1. Find the EVENT date (not article publication date)
  2. Update/create relevant actor notes
  3. Check for discrete events → create Event notes if warranted
  4. Add summary to correct daily note (create if needed)
  5. Update thesis implications if relevant
```

**Why this matters:** Daily notes are the changelog. Events should be logged on the day they happened, not when we read about them.

### Check for events

When processing news, ask: **is there a discrete, dated occurrence?**

| Signal | Action |
|--------|--------|
| Specific date + major action (deal signed, policy announced, filing made) | Create Event note |
| M&A, bankruptcy, IPO, major funding, product launch | Create Event note |
| Ongoing trend or dynamic | Concept note instead |
| Incremental news about existing event | Update existing Event note |

**Don't wait to be asked.** If news contains event-worthy material, propose Event notes proactively.

See "Events vs Actor sections" below for full criteria and Event note structure.

## Conventions

See [[Thesis conventions]] for how to read thesis names (Long X, Short X, pairs trades).

See [[Taxonomy discussion]] for open questions about hashtag/frontmatter structure as the vault scales globally.

## Daily note structure

Daily notes follow this structure:

1. **Vault activity** (at top): Track notes created/modified during the session
   - Created: table with Note, Type, Topic
   - Modified: table with Note, Changes
2. **Market data**: Levels, moves, key stats
3. **Topic sections**: News by category (varies by day)
4. **Thesis implications table**: How new info affects existing theses (columns: Thesis, New evidence, Direction)
5. **Open threads**: Checklist of things to track/follow up
6. **Sources**: Articles referenced

**Vault activity is mandatory** — provides a changelog for research continuity across sessions.

**Always journal vault changes.** Every time you create or modify notes, update the appropriate daily note's Vault activity section before finishing the task. This applies to:
- New actor, concept, event, or thesis notes
- Significant edits to existing notes (new sections, data updates, link additions)
- Don't log trivial fixes (typos, formatting)

When adding news, always consider which thesis it supports or challenges.

## Research workflow

1. **Web search** for major news sources
2. **X/Twitter lists** for industry commentary (access via Lists sidebar → Your Lists):
   - **"Chips & Semiconductors"** — your list (15 members), foundry/memory news
   - **"AI Infrastructure"** — your list (13 members), datacenter/power/buildout
   - **"SemiAnalysis"** — your list (5 members), deep semi analysis, power/energy for AI
   - "Semiconductors / Chips" by @compound248 — broader industry feed (42 members)
   - Other topic lists: AI, Anthropic, LLMs, Lithium, Macroeconomics, Robotics, Solar, etc.
3. Add findings to daily note first, extract to actor/concept notes if substantial

## Inputs Folder Workflow (Idea for Exploration)

The concept of an `Inputs/` directory serves as a potential staging ground for raw intelligence (reports, transcripts, articles, links, PDFs) before it is synthesized into atomic notes (`Actors/`, `Concepts/`, `Theses/`). This could formalize an "inbox" function for non-daily inputs and ensure the main vault remains clean and focused on curated knowledge.

**Potential Workflow:**
1.  **Ingest:** When encountering new, raw information, a new note could be created in `Inputs/` (e.g., `Inputs/Goldman 2026 Energy Outlook.md`), with raw content pasted or linked.
2.  **Process:** Review the `Inputs/` note, extract relevant data points, insights, or updates to enrich existing `Actors/`, `Concepts/`, `Theses/`, or `Events/` notes, or create new atomic notes.
3.  **Archive/Delete:** Once value is extracted, the `Inputs/` note could be moved to `Inputs/Archive/` or deleted.

**Potential Benefits:**
-   **Clarity:** Distinguishes raw data from curated knowledge.
-   **Cleanliness:** Prevents clutter in core folders.
-   **Traceability:** Provides a temporary source record for all updates.

---

## Actor Indexing (Idea for Exploration)

Given the growing size of the `Actors/` directory (596 files), the idea of creating "Actor Index" notes (e.g., `Actors/Index - Semi.md`, `Actors/Index - Banks.md`) could be explored to improve browsing and discovery of specific actors within a sector. These would function as curated "Table of Contents" for large actor clusters.

---

## Key actors to track

Foundry: [[TSMC]], [[Samsung]], [[Intel Foundry Services]], [[GlobalFoundries]]
Memory: [[SK Hynix]], [[Micron]], [[Samsung]]
GPU/AI chips: [[NVIDIA]], [[AMD]], [[Broadcom]]
AI Labs: [[OpenAI]], [[Anthropic]], [[xAI]], [[Google DeepMind]]
Equipment: [[ASML]], [[Applied Materials]], [[Lam Research]], [[Tokyo Electron]]

## Note decisions

When new information emerges:
- If it's a **major standalone topic** → create new atomic note
- If it's an **update to existing actor/concept** → add section to existing note
- If it's **incremental news** → daily note only

Example: Intel Magdeburg cancellation → added "Geographic retreat" section to [[Intel Foundry Services]] rather than standalone note.

### Frame notes for intrinsic value

**Don't frame notes around what triggered their creation.** Notes should explain why the topic matters on its own terms, not why you happened to add it.

| Wrong | Right |
|-------|-------|
| "El-Erian mentioned this, so it's relevant to Powell" | "This is the modern template for bond vigilante discipline" |
| "Adding because it came up in today's research" | "Key precedent for fiscal credibility crises" |
| Note exists because of external reference | Note exists because topic matters intrinsically |

**The trigger is incidental.** A news article, expert quote, or conversation tangent may prompt you to create a note, but the note itself should stand alone. Future readers (including yourself) won't care what reminded you to add it — they need to understand why it matters.

**Test:** Would this note make sense to someone who never saw the triggering context?

---

### Check for intermediate levels

**Before linking a specific note to a general note, check if an intermediate hub exists or should be created.**

| Too direct | Better hierarchy |
|------------|------------------|
| EU-China EV tariffs → [[EU]] | EU-China EV tariffs → [[EU-China trade]] → [[EU]] |
| TSMC Arizona → [[Taiwan]] | TSMC Arizona → [[TSMC]] → [[Taiwan]] |
| Blackwell delay → [[AI hyperscalers]] | Blackwell delay → [[NVIDIA]] → [[AI hyperscalers]] |

**When to create an intermediate:**
- Specific policy → Bilateral relationship → Institution (e.g., tariff deal → country-pair trade → bloc)
- Company event → Company → Sector
- Multiple specific notes would link to same general note

**Checklist:**
1. Is there already a hub note between my specific note and the general note?
2. Would other notes benefit from the same intermediate?
3. Does the parallel pattern exist? (e.g., if [[US-China trade]] exists, [[EU-China trade]] probably should too)

**Why this matters:** Linking a specific tariff policy directly to [[EU]] clutters a general institutional note with granular details. Intermediate hubs keep general notes clean and create useful groupings.

## Folder structure

| Folder | Purpose |
|--------|---------|
| Actors | Companies, orgs, entities |
| Concepts | Ideas, dynamics, phenomena |
| Sectors | Industry hubs with value chains |
| Theses | Investment theses (Long/Short/Pairs) |
| Questions | Open research questions |
| Events | Discrete happenings worth noting |
| Daily | Daily notes (inbox/capture) |
| Meta | Vault conventions and meta-notes |

## Events vs Actor sections

**Prefer Event notes for corporate events.** Events are atomic — they happened at a specific time, involved specific actors, and have their own narrative. Keeping events separate from actors:

- Prevents actor notes from bloating with historical detail
- Allows multiple actors to link to the same event without duplication
- Creates a clear timeline in the Events folder
- Separates "who they are" (actor) from "what happened" (event)

### When to create an Event note

| Event type | Create Event note? |
|------------|-------------------|
| M&A (mergers, acquisitions, divestitures) | ✅ Yes |
| Bankruptcies, restructurings | ✅ Yes |
| IPOs, spinoffs, delistings | ✅ Yes |
| Major funding rounds ($100M+) | ✅ Yes |
| Major product launches | ✅ Yes |
| Strategic pivots, major partnerships | ✅ Yes |
| Major legal/regulatory actions | ✅ Yes |
| Quarterly earnings | ❌ No (stays in actor) |
| Minor executive changes | ❌ No (stays in actor) |
| Small funding rounds | ❌ No (stays in actor/daily) |
| Routine product updates | ❌ No (stays in actor) |

### Event note structure

```markdown
#event #[category] #[year]

# Event Name

Brief summary of what happened and why it matters.

---

## What happened

Timeline, key facts, numbers.

---

## Why it matters

Impact, implications, what changed.

---

## Actors involved

| Actor | Role |
|-------|------|
| [[Company A]] | Acquirer |
| [[Company B]] | Target |
| [[Person X]] | Decision-maker |

---

## Related

- [[Actor 1]] — role in event
- [[Concept]] — dynamic this illustrates
- [[Other Event]] — connected event
```

### Actor notes reference events

Actor notes should have a "Key events" section that links to Event notes:

```markdown
## Key events

- [[Saks-Neiman merger]] — 2024, $2.7B acquisition
- [[Saks bankruptcy]] — Jan 2026, Chapter 11
```

This keeps actor notes focused on "who they are" while events carry the narrative.

## Concept vs Sector hub

| | **Concept** | **Sector Hub** |
|---|---|---|
| Purpose | Single idea/phenomenon | Industry scaffolding |
| Growth | Organic (encountered) | Deliberate (top-down) |
| Focus | "What is this dynamic?" | "Who plays in this space?" |
| Links | Examples of the concept | Organized by value chain/segment |
| Theses | May have one angle | Multiple competing theses |

**Keep as Concept when:**
- It's a trend/phenomenon, not a full industry
- Key actors live primarily in other sectors
- No clear value chain structure yet
- Not enough dedicated pure-plays to organize

**Promote to Sector when:**
- 10+ actors whose primary business is in this space
- Multiple distinct theses (Long X, Short Y, pairs)
- Clear value chain emerges (components → assembly → brands)
- Making allocation decisions at the sector level

**Example:** "AI Infrastructure" is a Sector — has NVIDIA, hyperscalers, power companies, cooling companies organized by role. "Wearable AI" is a Concept — mostly a feature of bigger companies (Amazon, Meta, Apple), no dedicated pure-plays yet.

## Sector / Sub-sector / Concept hierarchy

**Three-tier structure for industry clusters:**

```
Sector (parent)
    └── Sub-sector (cluster of competing actors)
            └── Sister Concept (the "why it matters")
```

### Definitions

| Type | Purpose | Example |
|------|---------|---------|
| **Sector** | Broad industry category | [[AI Infrastructure]] |
| **Sub-sector** | Cluster of actors that compete | [[AI Storage]] |
| **Sister Concept** | Explains WHY the sub-sector matters | [[AI storage bottleneck]] |

**Test for sub-sector:** Do the actors mostly compete with each other and NOT with actors in other clusters? If yes → sub-sector.

**Test for sister concept:** Is there an underlying dynamic/phenomenon that explains why this cluster matters? If yes → create sister concept.

### Linking rules

| Note type | Links TO | Does NOT link to |
|-----------|----------|------------------|
| **Actor** | Its sub-sector | Sister concept (redundant) |
| **Sub-sector** | Parent sector, sister concept, actors | — |
| **Concept** | Sister sector, related concepts | Individual actors (too granular) |

**Key principle:** Actors reach concepts via their sub-sector. No redundant direct links.

### Example — AI Storage cluster

```
Pure Storage.md (actor)
    → links to: [[AI Storage]] (sub-sector)
    → hint: (→ [[AI storage bottleneck]]) in Related section
    → does NOT link directly to concept

AI Storage.md (sub-sector)
    → links to: [[AI Infrastructure]] (parent)
    → links to: [[AI storage bottleneck]] (sister concept)
    → links to: [[Pure Storage]], VAST Data, Weka (actors)

AI storage bottleneck.md (concept)
    → links to: [[AI Storage]] (sister sector)
    → explains WHY the sector matters
    → does NOT list every actor
```

### Actor Related section format

When an actor belongs to a sub-sector with a sister concept:

```markdown
### Sectors
- [[AI Storage]] — sub-sector (→ [[AI storage bottleneck]])
- [[AI Infrastructure]] — parent sector
```

The `(→ [[concept]])` notation hints that the concept exists without creating a redundant direct link.

### When to create this structure

| Trigger | Action |
|---------|--------|
| 3+ actors in same competitive space | Consider sub-sector |
| Sub-sector has non-obvious "why it matters" | Create sister concept |
| Concept explains dynamics across multiple sectors | Keep as standalone concept (not sister) |

**Not every sub-sector needs a sister concept.** Only create one when the underlying dynamic isn't obvious from the sector description itself.

## Before creating files

### CRITICAL: Always verify before creating

**Every time you propose creating actors, you MUST first check if they already exist.**

This is non-negotiable. The vault has 400+ actors. Creating duplicates or overwriting detailed notes with generic templates destroys research work.

### Verification workflow

1. **Before proposing any new actor**, run:
   ```bash
   cd /c/Users/klein/financial-charts/investing && git ls-files "Actors/*.md" | sed 's|.*/||; s|\.md$||' | grep -iE "name1|name2|name3"
   ```

2. **Use broad, partial patterns** — names may be stored differently:
   ```bash
   # Looking for "Bank of America"? Search multiple ways:
   grep -iE "bank.*america|bofa|bac"

   # Looking for "ServiceNow"? Try partial:
   grep -iE "servicenow|service.*now|snow"

   # Looking for "AT&T"? Handle special chars:
   grep -iE "at&t|att|at.t"
   ```

3. **Check abbreviations, tickers, and variants:**
   - Full name: "Goldman Sachs"
   - Ticker: "GS"
   - Short form: "Goldman"
   - With spaces/without: "BlackRock" vs "Black Rock"

4. **Explicitly state the result** for each proposed actor:
   ```
   Honeywell  — NOT FOUND (safe to create)
   NVIDIA     — EXISTS (do not create)
   ```

5. **Only then propose creation** of actors confirmed NOT FOUND.

### Why this matters

- Existing files often contain specific data (yield numbers, capacity figures, timelines, cap tables) that took time to research
- Generic templates would overwrite this detailed work
- The vault is large enough that memory alone cannot track what exists

### Full actor list check

```bash
cd /c/Users/klein/financial-charts/investing && git ls-files "Actors/*.md"
```

### Check specific names

```bash
cd /c/Users/klein/financial-charts/investing && git ls-files "Actors/*.md" | sed 's|.*/||; s|\.md$||' | grep -iE "search|terms|here"
```

**WARNING:** Do NOT use `xargs basename -a` — it splits on spaces and corrupts filenames like "10x Genomics.md" into separate tokens. The `sed` approach above is safe.

### After creating/updating notes

**Always complete these steps:**

1. **Journal** — update today's daily note Vault activity (Created/Modified tables)
2. **Link mentions** — search for unlinked text mentions, convert to `[[wikilinks]]`
3. **Add backlinks** — update Related sections of connected notes to link back to new note

#### Link mentions

Search the vault for unlinked mentions and add `[[wikilinks]]`:

```bash
cd /c/Users/klein/financial-charts/investing && grep -riE "xpeng|XPENG" --include="*.md"
```

Then update unlinked mentions (e.g., `Xpeng` → `[[Xpeng]]`, `XPENG` → `[[Xpeng|XPENG]]`).

**Skip linking in:**
- Section headers (e.g., `### China — Xpeng Aeroht IPO`)
- Source URLs and markdown link text
- Note titles (the `# Title` line)

#### Add backlinks

When creating a note, also update Related sections of connected notes to point back:

| New note | Add backlink to |
|----------|-----------------|
| Actor | Investors, competitors, sector hubs |
| Event | All actors involved |
| Concept | Actors that exemplify it |

**Example:** Created [[Stretto]] → add to [[Saks bankruptcy]] Related section

## Actor conventions

### Actors don't need to be investable

Actors include any entity that affects investment outcomes:

| Type | Examples | Why track |
|------|----------|-----------|
| Investable | [[NVIDIA]], [[Chevron]] | Direct positions |
| Policy-makers | [[BIS]], [[OFAC]], [[US Government]] | Drive sector-wide moves |
| Private companies | [[Anthropic]], [[OpenAI]] | Shape competitive dynamics |
| Geographies | [[Venezuela]], [[Taiwan]] | Geopolitical risk factors |
| Individuals | [[Jensen Huang]], [[Sam Altman]] | Key decision-makers |

**Principle:** Non-investable actors that drive investable outcomes are essential context.

### Regional actors stay high-level

Geographic actors (China, Brazil, EU, Japan, etc.) are **scaffolding**, not repositories:

| Content type | Where it belongs |
|--------------|------------------|
| Specific policy action | Actor who took action (exchange, regulator, ministry) |
| Market data/news | Daily note + specific actor |
| Bilateral relationships | Relationship note (e.g., [[EU-China trade]]) |
| Structural dynamics | Concept note (e.g., [[China economic transition]]) |

**Regional actor notes should contain:**
- High-level overview of why this region matters
- Links to specific actors, concepts, events within the region
- Key macro data (GDP, trade balance, etc.)

**Regional actor notes should NOT contain:**
- Granular news items (belongs on specific actors)
- Detailed policy mechanics (belongs on regulator/exchange actors)
- Event narratives (belongs in Events/)

**Example:** China margin tightening news → lives on [[China A-share exchanges]], not [[China]]. China.md links to the exchange hub.

### Concepts don't need theses

Concepts capture knowledge, not just trade ideas:

| Type | Examples | Why track |
|------|----------|-----------|
| Investable dynamics | [[AI hyperscalers]], [[Power constraints]] | Active theses |
| Emerging tech | [[Solid-state batteries]], [[Sodium-ion batteries]] | Future relevance |
| Market structure | [[Battery supply chain]], [[Rare earth leverage]] | Context for decisions |
| Phenomena | [[China retaliatory toolkit]], [[Export controls]] | Explains price action |

**Principle:** If you might reference it from multiple notes, it deserves a concept note — regardless of whether there's a trade.

### Cap tables for private companies

Private actors (non-public companies) should include a **cap table / investors section** with:

- Major investors and amounts
- Funding rounds (date, amount, valuation)
- Total raised
- Notable patterns (e.g., "both Google AND Amazon invested")

Public companies don't need cap tables — ownership is public via SEC filings.

**Private actors requiring cap tables:**
- AI labs: [[Anthropic]], [[OpenAI]], [[xAI]]
- Startups: [[Groq]] (until acquired)
- Consortiums: [[Rapidus]] (stakeholder list instead)

**VCs** (Benchmark, Craft Ventures, ZhenFund) track portfolios, not cap tables.

### Financials for public companies

Public company actors should include a **historical financials section** with:

- Revenue (10 years, growth rates)
- Margins (gross, operating, net)
- Earnings (EPS, net income)
- Cash flow (operating, free cash flow)
- Key segment breakdowns
- Valuation multiples (P/E, EV/EBITDA, P/S as relevant)
- Balance sheet highlights (cash, debt, shares outstanding)
- Returns (ROE, ROIC)

**Format**: Use tables for multi-year AND quarterly data. Include source and date.

**Stock price history**: For all publicly traded companies, include period-end stock prices in both annual and quarterly tables. This enables return analysis and valuation context.

**Annual example (10 years)**:

| Metric | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|--------|------|------|------|------|------|------|------|------|------|------|
| Revenue ($B) | 15.0 | 18.0 | 22.0 | 26.0 | 30.0 | 35.0 | 42.0 | 50.0 | 60.0 | 75.0 |
| Revenue growth | 18% | 20% | 22% | 18% | 15% | 17% | 20% | 19% | 20% | 25% |
| Gross margin | 45% | 46% | 48% | 49% | 50% | 52% | 54% | 55% | 57% | 59% |
| Operating margin | 15% | 16% | 18% | 19% | 20% | 22% | 24% | 25% | 28% | 30% |
| Net margin | 12% | 13% | 15% | 16% | 17% | 18% | 20% | 21% | 23% | 25% |
| EPS | $0.80 | $1.00 | $1.40 | $1.70 | $2.00 | $2.50 | $3.20 | $4.00 | $5.20 | $7.00 |
| FCF ($B) | 2.5 | 3.2 | 4.5 | 5.5 | 6.5 | 8.0 | 10.5 | 12.0 | 15.0 | 20.0 |
| ROE | 18% | 19% | 21% | 22% | 24% | 25% | 28% | 30% | 32% | 35% |
| **Stock price** | $12 | $18 | $22 | $30 | $38 | $55 | $48 | $72 | $95 | $120 |

**Quarterly example (12 quarters)**:

| Metric | Q1'23 | Q2'23 | Q3'23 | Q4'23 | Q1'24 | Q2'24 | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 |
|--------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Revenue ($B) | 11.5 | 12.0 | 12.8 | 13.7 | 13.5 | 14.2 | 15.3 | 17.0 | 16.5 | 18.0 | 19.5 | 21.0 |
| Rev growth YoY | 15% | 16% | 18% | 20% | 17% | 18% | 20% | 24% | 22% | 27% | 27% | 24% |
| Gross margin | 54% | 55% | 55% | 56% | 56% | 57% | 57% | 58% | 58% | 59% | 59% | 60% |
| Op margin | 24% | 25% | 25% | 26% | 27% | 27% | 28% | 29% | 28% | 29% | 30% | 31% |
| EPS | $0.90 | $0.95 | $1.02 | $1.13 | $1.15 | $1.22 | $1.35 | $1.48 | $1.50 | $1.65 | $1.80 | $2.05 |
| **Stock price** | $58 | $62 | $65 | $72 | $78 | $82 | $88 | $95 | $102 | $108 | $115 | $120 |

*Source: Company filings, Jan 2026*

**Segment breakdowns** (where relevant):

| Segment | Revenue | % of total | Growth |
|---------|---------|------------|--------|
| Cloud | $30B | 40% | +35% |
| Enterprise | $25B | 33% | +15% |
| Consumer | $20B | 27% | +10% |

### Financials for banks

Banks use different metrics than typical companies. **Do not use gross/operating/net margins** — use bank-specific metrics instead.

**Required metrics for banks:**

| Metric | What it measures |
|--------|------------------|
| **NII** | Net interest income — core earnings from lending |
| **NIM** | Net interest margin — NII as % of earning assets |
| **Efficiency ratio** | Non-interest expense / revenue (lower = better) |
| **CET1 ratio** | Common equity tier 1 capital / risk-weighted assets |
| **NCO rate** | Net charge-offs as % of loans (credit quality) |
| **ROE / ROA** | Return on equity / assets |
| **Book value / TBV** | Book value and tangible book value per share |

**Annual example (banks, 10 years)**:

| Year | Revenue | Net Income | EPS | ROE | Stock Price |
|------|---------|------------|-----|-----|-------------|
| 2016 | $96B | $25B | $6.19 | 10% | $86 |
| 2017 | $100B | $24B | $6.31 | 10% | $107 |
| 2018 | $109B | $32B | $9.00 | 13% | $98 |
| 2019 | $115B | $36B | $10.72 | 14% | $139 |
| 2020 | $120B | $29B | $8.88 | 11% | $127 |
| 2021 | $131B | $48B | $15.36 | 17% | $158 |
| 2022 | $129B | $38B | $12.09 | 13% | $134 |
| 2023 | $158B | $50B | $16.23 | 16% | $170 |
| 2024 | $173B | $58B | $19.75 | 17% | $242 |
| 2025 | $187B | $58B | $20.02 | 16% | $330 |

**Quarterly example (banks, 12 quarters)**:

| Quarter | Revenue | Net Income | EPS | NII | Stock Price |
|---------|---------|------------|-----|-----|-------------|
| Q1 '23 | $39.3B | $12.6B | $4.10 | $20.8B | $130 |
| Q2 '23 | $42.4B | $14.5B | $4.75 | $21.9B | $144 |
| Q3 '23 | $40.7B | $13.2B | $4.33 | $22.9B | $146 |
| Q4 '23 | $38.6B | $9.3B | $3.04 | $24.2B | $170 |
| Q1 '24 | $42.5B | $13.4B | $4.44 | $23.1B | $199 |
| Q2 '24 | $51.0B | $18.1B | $6.12 | $22.9B | $203 |
| Q3 '24 | $43.3B | $12.9B | $4.37 | $23.5B | $211 |
| Q4 '24 | $43.7B | $14.0B | $4.81 | $23.5B | $242 |
| Q1 '25 | $44.9B | $14.6B | $5.07 | $23.4B | $250 |
| Q2 '25 | $45.7B | $15.0B | $5.24 | $23.1B | $268 |
| Q3 '25 | $47.1B | $14.4B | $5.07 | $23.4B | $295 |
| Q4 '25 | $46.8B | $13.0B | $4.63 | $25.1B | $330 |

*Source: Company filings, Jan 2026*

**Bank-specific metrics (4 years)**:

| Metric | 2022 | 2023 | 2024 | 2025 |
|--------|------|------|------|------|
| NIM | 2.4% | 2.7% | 2.8% | 2.9% |
| Efficiency ratio | 58% | 55% | 52% | 52% |
| CET1 ratio | 13.2% | 15.0% | 15.7% | 15.0% |
| NCO rate | 0.3% | 0.5% | 0.6% | 0.7% |

**Balance sheet (banks)** — include:
- Total assets
- Stockholders' equity
- Book value per share
- Tangible book value per share
- AUM (if wealth management segment)

## Finding links

**Systematic approach to discovering what to link.**

### 1. Check what exists

```bash
# Find actors matching a term
cd /c/Users/klein/financial-charts/investing && git ls-files "Actors/*.md" | sed 's|.*/||; s|\.md$||' | grep -iE "term"

# Find all mentions across vault
grep -riE "term" --include="*.md"
```

### 2. Steal from peers

Look at Related sections of similar actors. If writing a hedge fund note, check how [[Bridgewater]], [[Millennium]], [[D.E. Shaw]] are structured — they've already solved "what should a hedge fund link to."

| Actor type | Check these for patterns |
|------------|-------------------------|
| Hedge funds | [[Bridgewater]], [[Millennium]], [[Two Sigma]] |
| YC companies | [[Stripe]], [[Coinbase]], [[Brex]] |
| Semiconductors | [[TSMC]], [[NVIDIA]], [[ASML]] |
| Oil majors | [[Chevron]], [[Exxon]] |

### 3. Category checklist

Standard links by actor type:

| Actor type | Should link to |
|------------|---------------|
| **Companies** | Founders, competitors, investors, customers, suppliers |
| **Hedge funds** | Founder, strategy type, peer funds, key positions |
| **VCs/Accelerators** | Partners, top portfolio companies, co-investors |
| **Individuals** | Current org, prior orgs, key decisions, peers |
| **Geographies** | Key sectors, trading partners, policy actors |

### 4. Reverse lookup (after creating)

After creating a note, find notes that should link TO it:

```bash
# Find unlinked mentions of new actor
grep -riE "new actor name" --include="*.md" | grep -v "\[\[New Actor Name\]\]"
```

Then update those notes to add the `[[wikilink]]`.

### 5. Concept connections

Ask: "What dynamics affect this actor?"

| If the actor... | Consider linking to |
|-----------------|-------------------|
| Has China exposure | [[US-China tariffs]], [[Export controls]] |
| Is in batteries | [[China battery leverage]], [[Sodium-ion batteries]] |
| Is AI-related | [[AI hyperscalers]], [[Power constraints]] |
| Has geopolitical risk | Relevant geography notes |

## Related section convention

Notes should end with an annotated `## Related` section that explains *why* each note is linked:

```markdown
## Related

- [[NVIDIA]] — primary customer, GPU ecosystem
- [[Broadcom]] — competitor in PCIe switches
- [[AI hyperscalers]] — end customers driving demand
```

**Relationship types to annotate:**
- Customer / supplier
- Competitor / peer
- Investor / investee
- Partner
- Adjacent player (same ecosystem, different layer)
- Industry context (concept notes)

**Why this matters:** Obsidian's graph shows connections but not context. Annotated links are scannable without reading the full note.
