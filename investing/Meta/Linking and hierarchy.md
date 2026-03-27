# Linking and Hierarchy

Guidelines for folder structure, note hierarchy, and linking.

**Enforcement:** `scripts/check_note_compliance.py` enforces rules marked with ✓. Unmarked rules are guidance only.

| Enforced | Rule |
|----------|------|
| ✓ | Dead links detected |
| ✓ | Missing links (`--suggest-links` flag) |
| ✓ | Singular names (concept notes) |
| | Never remove wikilinks (process) |
| | Verify before creating (process) |
| | Aliases ≠ notes for distinct entities (process) |
| | Folder placement |
| | Sector composition |
| | Concept vs Sector distinction |
| | Intermediate hierarchy levels |

---

## Folder structure

| Folder | Purpose |
|--------|---------|
| Actors | Companies, orgs, people, countries — entities with agency |
| Products | Things made by Actors — chips, models, drugs, vehicles |
| Infrastructure | Fixed physical assets enabling trade/energy flows — chokepoints, pipelines, terminals |
| Concepts | Ideas, dynamics, phenomena, categories |
| Sectors | Industry hubs with value chains |
| Theses | Investment theses (Long/Short/Pairs) |
| Questions | Open research questions |
| Events | Discrete happenings worth noting |
| Daily | Daily notes (inbox/capture) |
| Meta | Vault conventions and meta-notes |

### Products vs Actors

Products are made by Actors but lack agency. The parent Actor makes all decisions.

| Test | Actor | Product |
|------|-------|---------|
| Does it make decisions? | Yes | No |
| Does it have employees/leadership? | Yes | No |
| Is it an instance of a Concept category? | Sometimes | Always |
| Can you invest in it directly? | Usually | No |

**Examples:**
- NVIDIA (Actor) → H100 (Product) → AI accelerators (Concept)
- Anthropic (Actor) → Claude (Product) → Frontier models (Concept)
- Novo Nordisk (Actor) → Ozempic (Product) → GLP-1 drugs (Concept)

### Infrastructure vs Products vs Actors

Infrastructure is for fixed physical assets that enable trade or energy flows but lack agency. They don't make decisions, aren't manufactured goods, and can't be invested in directly (unlike pipeline companies, which are Actors).

| Test | Actor | Product | Infrastructure |
|------|-------|---------|---------------|
| Does it make decisions? | Yes | No | No |
| Is it manufactured? | N/A | Yes | No (natural or built-in-place) |
| Does it enable flow/transit? | Sometimes | No | Yes |
| Can you invest in it directly? | Usually | No | No |

**Examples:**
- Iran (Actor) → Kharg Island (Infrastructure) — terminal handling 90% of Iran's oil exports
- QatarEnergy (Actor) → Ras Laffan (Infrastructure) — industrial hub with 20% of world LNG capacity
- Saudi Arabia (Actor) → East-West Pipeline (Infrastructure) — 7M bbl/d bypass route
- Plains All American Pipeline (Actor) stays in Actors — it's a company with agency, not the physical pipe

**Chokepoints** are Infrastructure: Strait of Hormuz, Strait of Malacca, Danish Straits, Turkish Straits, SUMED pipeline.

---

## Market / Price split (tradeable concepts)

Tradeable concepts can split into two notes: `[Thing] Market` and `[Thing] Price`. Both live in `Concepts/`.

| Note | Contains | Ages as |
|------|----------|---------|
| `[Thing] Market` | Fundamentals, supply/demand, policy, players, dynamics | Encyclopedia — accumulates |
| `[Thing] Price` | Absolute price chain + relative price chain | Episodic — extends as price moves |

**Naming:** `Uranium Market` / `Uranium Price`. No parentheticals or suffixes.

**Linking:** Each links to the other. Same event can appear in both — different lens. Market note treats a supply cut as a fundamental fact. Price note treats it as what moved the number.

**When to split:** Commodities, rates, currencies, or any concept with a tradeable price to explain.

**When NOT to split:** Analytical concepts (Jevons Paradox), structural concepts (advanced packaging), concepts without a distinct price.

**Migration:** Existing notes like `Uranium.md` rename to `Uranium Market.md`. Create `Uranium Price.md` when there's enough to say — not all at once.

---

## Sector composition rules

Sectors are **correlation clusters**, not GICS categories. Three rules:

| Rule | Rationale |
|------|-----------|
| **Actual correlation** | Group what moves together in markets |
| **Private peers included** | Same competitive dynamics, even without ticker |
| **Segments as peers** | Alienware with gaming hardware, not with Dell |

This makes sectors into **competitive landscapes**. Alienware competes with Razer, not Dell's PowerEdge servers.

**Practical use:** Sector peers define comparison chart groups. A Corsair chart compares to Razer, MSI, Logitech — not random GICS "Technology Hardware" peers.

### Structure template

```
### Public pure-play
- Ticker, exchange, focus

### Segments (parent diversified)
- Segment → [[Parent]]

### Private
- Company, focus
```

### Why not GICS?

| GICS | Vault sectors |
|------|---------------|
| 11 fixed sectors | 80+ flexible clusters |
| Mutually exclusive | Overlapping allowed |
| Company-level | Segments can belong to peers |
| Static | Evolves with investment focus |

---

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

---

## Sector / Sub-sector / Concept hierarchy

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

### When to create this structure

| Trigger | Action |
|---------|--------|
| 3+ actors in same competitive space | Consider sub-sector |
| Sub-sector has non-obvious "why it matters" | Create sister concept |
| Concept explains dynamics across multiple sectors | Keep as standalone concept (not sister) |

---

## Creating notes

### Never remove wikilinks

If a `[[link]]` is dead, create the missing note. Never downgrade a link to plain text. When compliance checker flags dead links, create the missing note — never remove brackets to silence the warning.

### Verify before creating

Always check if note exists first. If a similar name exists (e.g., `SPACs.md` when creating `SPAC.md`), **read it to check aliases** before creating a duplicate.

```bash
# Search ALL folders
cd /c/Users/klein/financial-charts/investing && git ls-files "**/*.md" | sed 's|.*/||; s|\.md$||' | grep -iE "keyword"

# Or search specific folder
git ls-files "Actors/*.md" | sed 's|.*/||; s|\.md$||' | grep -iE "name"
```

### Aliases are not substitutes for notes

Aliases are for alternate names of the same entity (e.g., "OXY" → `Occidental Petroleum.md`). If a subsidiary, fund, or division operates independently or is referenced in a distinct context, it gets its own note — not an alias on the parent.

| Wrong | Right |
|-------|-------|
| `Draper Fisher Jurvetson.md` with alias "DFJ Growth" | Separate `DFJ Growth.md` linking to `[[Draper Fisher Jurvetson]]` as parent |
| `Baron Capital.md` with alias "BPTRX" | BPTRX is a fund ticker alias (acceptable — same entity, different name) |

Test: would a reader looking up this name expect to land on the parent, or on something more specific? If more specific → own note.

### Singular names

Concept notes use singular form: `SPAC.md` not `SPACs.md`, `Direct lender.md` not `Direct lenders.md`.

---

## Linking practices

### Core principle: If it's mentioned, it's linked

**Every actor, company, person, or concept mentioned in a note should be a wikilink.** No exceptions. This applies to:

- Intros and summaries
- Tables (investors, customers, competitors, partners)
- Body text mentions
- Related sections

**Why this matters:**
- Broken links show what notes need to be created
- Links get resolved automatically when notes are created
- The graph reveals connections across the vault
- Readers can navigate to learn more

### Specific rules

**Link in intros.** If a note mentions multiple entities (e.g., "OTB owns Diesel, Margiela, Marni, Jil Sander"), link them all — not just ones with existing notes.

**Link in tables.** Investor tables, customer lists, competitor comparisons — every named entity should be linked:

```markdown
| Investor | Role |
|----------|------|
| [[Tiger Global]] | Series D lead |      ✓ Correct
| Greenoaks | Series B lead |              ✗ Wrong — should be [[Greenoaks]]
```

**Link in body text.** Don't leave company names, people, or concepts as plain text:

```markdown
✗ Wrong: "Acquired by Capital One for $5.15B"
✓ Right: "Acquired by [[Capital One]] for $5.15B"
```

**After creating notes, revisit links.** When you create related notes, go back and ensure all cross-references are properly linked.

**Update linked notes.** When you create a new note, add it to the Related sections of notes that reference it.

---

## Finding links

### 1. Check what exists

```bash
# Find actors matching a term
cd /c/Users/klein/financial-charts/investing && git ls-files "Actors/*.md" | sed 's|.*/||; s|\.md$||' | grep -iE "term"

# Find all mentions across vault
grep -riE "term" --include="*.md"
```

### 2. Steal from peers

Look at Related sections of similar actors:

| Actor type | Check these for patterns |
|------------|-------------------------|
| Hedge funds | [[Bridgewater]], [[Millennium]], [[Two Sigma]] |
| YC companies | [[Stripe]], [[Coinbase]], [[Brex]] |
| Semiconductors | [[TSMC]], [[NVIDIA]], [[ASML]] |
| Oil majors | [[Chevron]], [[Exxon]] |

### 3. Category checklist

| Actor type | Should link to |
|------------|---------------|
| **Companies** | Founders, competitors, investors, customers, suppliers |
| **Hedge funds** | Founder, strategy type, peer funds, key positions |
| **VCs/Accelerators** | Partners, top portfolio companies, co-investors |
| **Individuals** | Current org, prior orgs, key decisions, peers |
| **Geographies** | Key sectors, trading partners, policy actors |

### 4. Reverse lookup (after creating)

```bash
# Find unlinked mentions of new actor
grep -riE "new actor name" --include="*.md" | grep -v "\[\[New Actor Name\]\]"
```

### 5. Concept connections

| If the actor... | Consider linking to |
|-----------------|-------------------|
| Has China exposure | [[US-China tariffs]], [[Export controls]] |
| Is in batteries | [[China battery leverage]], [[Sodium-ion batteries]] |
| Is AI-related | [[AI hyperscalers]], [[Power constraints]] |
| Has geopolitical risk | Relevant geography notes |

---

## Intermediate levels

Before linking a specific note to a general note, check if an intermediate hub exists.

| Too direct | Better hierarchy |
|------------|------------------|
| EU-China EV tariffs → [[EU]] | EU-China EV tariffs → [[EU-China trade]] → [[EU]] |
| TSMC Arizona → [[Taiwan]] | TSMC Arizona → [[TSMC]] → [[Taiwan]] |
| Blackwell delay → [[AI hyperscalers]] | Blackwell delay → [[NVIDIA]] → [[AI hyperscalers]] |

**Checklist:**
1. Is there already a hub note between my specific note and the general note?
2. Would other notes benefit from the same intermediate?
3. Does the parallel pattern exist? (e.g., if [[US-China trade]] exists, [[EU-China trade]] probably should too)
