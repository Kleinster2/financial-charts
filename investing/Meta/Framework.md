# Investment Vault Framework

This vault tracks the global investable universe. One vault, many sectors, unified by tags and links.

---

## Core principles

**Investment is the purpose. Everything else is a lens.**

Sectors, geographies, macro themes, geopolitics — all are lenses on the same goal: understanding what to own and why.

**Numbers matter. Capture them.**

Hard data enables future analysis. When ingesting news or research:

| Capture | Examples |
|---------|----------|
| Financial metrics | Margins, costs, revenue, market share, multiples |
| Operational data | Capacity, yields, volumes, wafer starts, timelines |
| Comparisons | vs competitors, vs prior periods, vs expectations |
| Source/date | Always cite where data came from and when |

Use tables for structured data. Qualitative narrative without quantitative support is opinion. This vault prioritizes data.

**Example:** Don't just say "TSMC's US fabs have lower margins." Capture: Taiwan 62% gross margin vs US 8%, depreciation +386%, labor +100%, total cost per wafer $6,681 vs $16,123 (SemiAnalysis, Nov 2025).

---

## Folder structure

| Folder | Contains | Examples |
|--------|----------|----------|
| **Actors/** | Entities that affect investments | Companies, countries, people, institutions, VCs |
| **Concepts/** | Ideas, dynamics, themes | Technologies, strategies, market structures |
| **Events/** | Discrete happenings | M&A, crashes, policy changes, product launches |
| **Theses/** | Investment ideas | Long/Short/Pairs positions |
| **Questions/** | Open research questions | Uncertainties to resolve |
| **Daily/** | Inbox/capture | News, observations, raw notes |
| **Meta/** | Vault documentation | This file, conventions |

Folders define **note type**, not topic. A cybersecurity company goes in Actors/, not a "Cybersecurity/" folder.

---

## Tag taxonomy

Tags define **what a note is about**. Use multiple tags per note.

### Note type (required)

| Tag | Use for |
|-----|---------|
| `#actor` | Companies, people, countries, institutions |
| `#concept` | Themes, technologies, dynamics |
| `#event` | Discrete happenings |
| `#thesis` | Investment ideas |
| `#question` | Open research questions |

### Sector

| Tag | Sector |
|-----|--------|
| `#semiconductor` | Chips, foundries, equipment, memory |
| `#ai` | AI labs, models, compute |
| `#cybersecurity` | Security software, threat landscape |
| `#energy` | Power, utilities, generation |
| `#nuclear` | Nuclear power specifically |
| `#infrastructure` | Data centers, networks, physical buildout |
| `#fintech` | Financial technology |
| `#crypto` | Cryptocurrency, blockchain |
| `#biotech` | Biotechnology, pharma |
| `#telecom` | Telecommunications |
| `#automotive` | Vehicles, autonomy |
| `#defense` | Defense, aerospace |
| `#commodities` | Raw materials, mining |
| `#quantum` | Quantum computing |

Add new sector tags as needed. Keep them flat (not `#sector/semi`).

### Geography

| Tag | Region |
|-----|--------|
| `#usa` | United States |
| `#china` | China |
| `#taiwan` | Taiwan |
| `#korea` | South Korea |
| `#japan` | Japan |
| `#israel` | Israel |
| `#europe` | European Union / Europe broadly |
| `#gcc` | Gulf Cooperation Council (Saudi, UAE, etc.) |
| `#latam` | Latin America |
| `#sea` | Southeast Asia |

### Entity status

| Tag | Meaning |
|-----|---------|
| `#public` | Publicly traded |
| `#private` | Private company |
| `#government` | Government entity |
| `#sovereign` | Sovereign wealth / state actors |

### Role tags (for actors)

| Tag | Role |
|-----|------|
| `#hyperscaler` | Cloud giants (Google, Amazon, Microsoft, Meta) |
| `#foundry` | Chip fabrication |
| `#fabless` | Chip design without fabs |
| `#memory` | Memory chips (DRAM, NAND, HBM) |
| `#equipment` | Semiconductor equipment |
| `#vc` | Venture capital |
| `#datacenter` | Data center operators |

---

## Tagging examples

```
# NVIDIA
#actor #semiconductor #ai #usa #public #fabless

# Palo Alto Networks
#actor #cybersecurity #usa #public

# Export controls
#concept #semiconductor #geopolitics #usa #china

# Taiwan
#actor #taiwan #geopolitics #semiconductor

# Long NVIDIA
#thesis #semiconductor #ai
```

---

## Cross-sector concepts

Some concepts span multiple sectors. Tag them with all relevant sectors:

```
# Power constraints
#concept #energy #ai #infrastructure #datacenter

# China risk
#concept #geopolitics #semiconductor #ai #china
```

This allows the note to appear in filtered views for any relevant sector.

---

## MOCs (Maps of Content)

For thematic navigation, create MOC files that curate notes on a topic:

```markdown
# Cybersecurity MOC

Hub for cybersecurity investment research.

## Key actors
- [[Palo Alto Networks]]
- [[CrowdStrike]]
- [[Zscaler]]

## Key concepts
- [[Zero trust]]
- [[XDR consolidation]]

## Active theses
- [[Long cybersecurity consolidation]]
```

MOCs are manually curated (not auto-generated) to highlight what matters.

For auto-generated lists, use Dataview:

```markdown
## All cybersecurity actors
```dataview
LIST FROM #actor AND #cybersecurity
SORT file.name ASC
```
```

---

## Publishing subsets

To publish a focused subset (e.g., "cybersecurity vault"):

1. Filter by tag: all notes with `#cybersecurity`
2. Export via Obsidian Publish or static site generator
3. Unresolved links to non-published notes render as plain text

Readers see a coherent publication. They don't see broken links.

No special `#public` tagging needed — filtering happens at publish time.

---

## Scaling to 10,000 notes

This structure scales because:

| Element | How it scales |
|---------|---------------|
| **Folders** | Fixed set (Actors, Concepts, etc.) — doesn't grow |
| **Tags** | Add new sector/geo tags as needed |
| **Links** | Graph handles unlimited connections |
| **Search** | Local, indexed, fast at any scale |
| **MOCs** | Add new hubs as themes emerge |

**What to watch:**
- Full graph view slows down — use local graph or filtered views
- Tag discipline matters — don't create synonyms (`#cyber` vs `#cybersecurity`)
- MOCs become essential for navigation

---

## Adding a new sector

When expanding to a new sector (e.g., biotech):

1. **Create sector tag**: `#biotech`
2. **Add key actors**: Put in Actors/ with appropriate tags
3. **Add key concepts**: Put in Concepts/ with sector tag
4. **Create MOC** (optional): `Biotech MOC.md` for navigation
5. **Cross-link**: Connect to existing notes where relevant

No new folders. No structural changes. Just new notes with new tags.

---

## Tag hygiene

To prevent tag fragmentation:

- Check existing tags before creating new ones
- Use singular form (`#semiconductor` not `#semiconductors`)
- Use lowercase (`#usa` not `#USA`)
- Prefer specific over generic (`#nuclear` over `#power` for nuclear-specific notes)

To audit tags:
```bash
grep -rh "^#[a-z]" *.md | tr ' ' '\n' | grep "^#" | sort | uniq -c | sort -rn
```

---

## Related

- [[CLAUDE]] — operational guidelines for Claude sessions
- [[Thesis conventions]] — how to read thesis names
