# Vault Guidelines

## Philosophy

This is an Obsidian vault. Follow Obsidian philosophy:

- **Atomic notes** — one idea per note, no mega-documents
- **Links over hierarchy** — structure emerges from `[[connections]]`, not folders
- **Organic at the bottom, deliberate at the top** — actors/concepts grow organically as encountered; sector hubs are deliberate scaffolding that can start sparse
- **Daily notes as inbox** — capture first, extract atomic notes when ideas mature
- **Hubs can have dangling links** — sector hubs guide where new notes land; empty `[[links]]` fill in over time

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

**Before proposing where to add news, search the vault.**

1. **Grep for key terms** — actors, concepts, themes mentioned in the article
2. **Read top 2-3 matches** — understand what already exists
3. **Propose updates to relevant notes** — not just daily note
4. **Don't force weak connections** — "both mention India" is not a connection

**Bad:** Article about India tariffs → link to Reliance battery note (both mention India)
**Good:** Article about India tariffs → update [[India]], [[India-China relations]], [[US-China tariffs]]

The goal is enriching existing notes with new information, not just logging to daily note.

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
   git ls-files "Actors/*.md" | xargs basename -a | sed 's/.md$//' | grep -iE "name1|name2|name3"
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
git -C "C:/Users/klein/financial-charts/investing" ls-files "Actors/*.md"
```

### Check specific names

```bash
cd /c/Users/klein/financial-charts/investing && git ls-files "Actors/*.md" | sed 's|.*/||; s|\.md$||' | grep -iE "search|terms|here"
```

**WARNING:** Do NOT use `xargs basename -a` — it splits on spaces and corrupts filenames like "10x Genomics.md" into separate tokens. The `sed` approach above is safe.

### After creating new actors

**Retroactively link existing mentions.** When you create a new actor, search the vault for unlinked mentions and add `[[wikilinks]]`:

```bash
cd /c/Users/klein/financial-charts/investing && grep -riE "xpeng|XPENG" --include="*.md"
```

Then update unlinked mentions (e.g., `Xpeng` → `[[Xpeng]]`, `XPENG` → `[[Xpeng|XPENG]]`).

**Skip linking in:**
- Section headers (e.g., `### China — Xpeng Aeroht IPO`)
- Source URLs and markdown link text
- Note titles (the `# Title` line)

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
