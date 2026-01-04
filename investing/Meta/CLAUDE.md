# Vault Guidelines

## Philosophy

This is an Obsidian vault. Follow Obsidian philosophy:

- **Atomic notes** — one idea per note, no mega-documents
- **Links over hierarchy** — structure emerges from `[[connections]]`, not folders
- **Bottom-up** — don't over-engineer; let the graph grow organically
- **Daily notes as inbox** — capture first, extract atomic notes when ideas mature
- **No dashboards or indexes** — the graph *is* the dashboard

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

## Daily note structure

Daily notes follow this structure:
1. **Topic sections**: Foundry, Memory, AI/GPU, AI Labs, Equipment & Policy
2. **Thesis implications table**: How new info affects existing theses (columns: Thesis, New evidence, Direction)
3. **Open threads**: Checklist of things to track/follow up

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
| Theses | Investment theses (Long/Short/Pairs) |
| Questions | Open research questions |
| Events | Discrete happenings worth noting |
| Daily | Daily notes (inbox/capture) |
| Meta | Vault conventions and meta-notes |

## Before creating files

**Always check for existing files before batch creation:**

```bash
git -C "C:/Users/klein/financial-charts/investing" ls-files "Actors/*.md"
```

This prevents overwriting detailed notes with generic templates. Existing files often have specific data (yield numbers, timelines, capacity figures) that shouldn't be lost.

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
