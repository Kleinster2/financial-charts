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

- Keep notes small and focused
- Link liberally with `[[wikilinks]]`
- Prefer linking to an existing note over repeating information
- If a concept doesn't have a note yet, create one (or leave a dangling link for later)
- Don't add structure that doesn't emerge naturally

## When suggesting work

- Don't propose top-down reorganization
- Suggest adding links to existing notes
- Suggest new atomic notes, not comprehensive documents
- Daily notes are the entry point for new information

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
