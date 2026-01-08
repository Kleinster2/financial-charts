# Taxonomy discussion

**Date:** 2026-01-08

As the vault scales globally (~500 actors), the current hashtag pattern may need revision.

---

## Current pattern

Line 1 after frontmatter:
```
#type #sector #subsector #geography #ownership
```

Examples:
- `#actor #finance #exchange #usa #public`
- `#actor #housing #homebuilder #usa #public`
- `#concept #housing #policy #trump #2026`

---

## Problems identified

| Problem | Example |
|---------|---------|
| **Geography ambiguity** | `#china` = Chinese company? Exposed to China? Affected by China policy? |
| **No size/tier** | NVIDIA and small-cap chipmaker both `#semiconductors` |
| **No value chain position** | Supplier vs customer vs platform |
| **No investment status** | Position vs watchlist vs reference |
| **Cross-cutting themes** | AI infra vs AI models vs AI applications |
| **Temporal relevance** | Active thesis vs historical reference |

---

## Options

### Option 1: Hierarchical tags

```
#geo/asia/china
#geo/latam/brazil
#sector/tech/semis/foundry
#sector/finance/exchange
#status/position
#status/watching
```

**Pros:** Visual in graph, clickable, familiar
**Cons:** Verbose, harder to type consistently

---

### Option 2: Richer frontmatter (Dataview friendly)

```yaml
---
aliases: [TSMC, Taiwan Semiconductor]
type: actor
sector: [semiconductors, AI infrastructure]
subsector: foundry
hq: taiwan
exposure: [china, usa, japan, europe]
market_cap: mega
status: watching
value_chain: supplier
---
```

**Pros:** Queryable via Dataview, structured, flexible
**Cons:** Not visible in graph, requires plugin, more typing

---

### Option 3: Hybrid

Keep simple tags for browsing + add structured frontmatter for queries:

```yaml
---
aliases: [TSMC]
market_cap: mega
status: watching
exposure: [china, usa]
---
#actor #semiconductors #foundry #taiwan #public
```

**Pros:** Best of both worlds
**Cons:** Redundancy, maintenance burden

---

## Questions to decide

1. **Primary use case:** Visual graph browsing vs structured queries?
2. **Dataview adoption:** Will we use Dataview plugin for queries?
3. **Migration effort:** Update existing ~500 notes or grandfather them?
4. **Consistency:** Who maintains taxonomy discipline?

---

## Decision

**Status:** Pending

---

## Related

- [[CLAUDE.md]] — vault guidelines
- Obsidian Dataview plugin documentation

