# Cross-Vault Linking Rules

Full architecture: `C:\Users\klein\obsidian\geopolitics\vault-architecture.md`

---

## Scope

The investing vault covers market impact — price action, sector moves, portfolio implications. Military operations, diplomatic timelines, casualty counts, and strategic assessments belong in the geopolitics vault. When a geopolitical event moves markets, create the core event note in geopolitics and a market-impact note here, cross-linked.

Overlap between vaults is expected and desirable. Both need core facts; each adds its own lens. Don't strip content just because it "belongs" in another vault — strip it only if it's irrelevant to this vault's purpose.

---

## Format

When a note has a meaningful counterpart in another vault, add clickable `obsidian://` URI links:

```markdown
### Cross-vault
- [Geopolitics: Note Name](obsidian://open?vault=geopolitics&file=Folder%2FNote%20Name) — what the other perspective adds
```

Rules:
- Place under `### Cross-vault` subheading at end of Related section
- URL-encode paths: spaces → `%20`, slashes → `%2F`
- Brief description of what the other vault's perspective adds
- Only cross-link notes with meaningful counterparts — not every shared entity
- These links won't appear in graph view or backlinks — navigation aids only

---

## Post-Ingestion Gate

After creating a new event or making a major update, check all four sibling vaults:

- **Geopolitics** (`~/obsidian/geopolitics/`) — statecraft, sanctions, diplomatic precedent, alliance dynamics, infrastructure competition
- **Brazil** (`~/obsidian/brazil/`) — Brazilian actors, markets (BRL, DI, Ibovespa, ADRs), domestic policy/institutions
- **History** (`~/obsidian/history/`) — structural breaks, first-of-kind precedents, long-arc patterns. When a topic has deep historical roots (sanctions, trade wars, monetary policy), check for relevant precedent.
- **Technologies** (`~/obsidian/technologies/`) — foundational tech shifts (chip architectures, fab capacity, AI model breakthroughs, supply chain restructuring)

Flag relevant vaults to the user. Don't silently skip — the default is to ask. Routine updates to existing notes don't trigger this.
