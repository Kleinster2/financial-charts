# Cross-Vault Linking Rules

Full architecture: `C:\Users\klein\obsidian\geopolitics\vault-architecture.md`

---

## Scope

The investing vault covers market impact — price action, sector moves, portfolio implications. Military operations, diplomatic timelines, casualty counts, and strategic assessments belong in the geopolitics vault. When a geopolitical event moves markets, create the core event note in geopolitics and a market-impact note here, cross-linked.

Overlap between vaults is expected and desirable. Both need core facts; each adds its own lens. Don't strip content just because it "belongs" in another vault — strip it only if it's irrelevant to this vault's purpose.

---

## Vault of record — the lens test

Before writing durable content into the investing vault, ask: *which vault's lens does this content primarily live in?*

Each sibling vault has its own lens — the angle it looks at the world through:

| Vault | Lens |
|---|---|
| Investing | Market impact, positioning, prices, portfolio implications — what should I own today and why |
| History | "How did we get here" — durability, precedent, structural breaks, long-arc patterns |
| Technologies | Foundational tech shifts — chip architectures, fab capacity, model breakthroughs, supply-chain evolution |
| Geopolitics | Statecraft, alliances, sanctions architecture, military operations, diplomatic timelines |
| Brazil | Brazilian actors, markets (BRL, B3, DI, Ibovespa, ADRs), domestic institutions, domestic policy |

Content can touch multiple lenses — an Iran oil story engages investing (WTI price), geopolitics (Strait of Hormuz), and history (prior oil shocks). One lens is primary. The others get a 1-2 sentence gloss and an `obsidian://` link in the respective vaults.

Durable content inherits the half-life of whatever note it's embedded in. A 1975 statute embedded in a 2026-positioning concept note gets archived with that concept note — findable only if a future reader already knows to look there. Keep durable content in durable vaults.

### Durability corollary (history specifically)

For content that *could* live in history, a sharper test: *will this still be true, and still be the primary place to find this, in five years?*

- Yes → history owns it. Write it there first. The investing note gets a 1-2 sentence gloss and an `obsidian://` link.
- No → live decision / live positioning / live crisis → investing owns the full treatment.

This is the cleanest version of the lens test for history because history's lens is fundamentally about durability. For technologies/geopolitics/Brazil, use the lens directly — "is this a tech-architecture story?", "is this a statecraft story?", "is this a Brazil-domestic story?" — not the durability question.

### Ownership by content type

| Content type | Vault of record | Investing treatment |
|---|---|---|
| Legislation, statutes, policy regimes (1975 EPCA, Glass-Steagall, Dodd-Frank) | History | Gloss + link |
| Historical crises, prior-cycle patterns (1970s stagflation, 2008 GFC, 2015 CNY devaluation) | History | Gloss + link for precedent |
| Long-arc technology shifts (transistor, EUV origins, Bell Labs) | Technologies | Gloss + link when referenced |
| Foundational chip/model architectures (transformer, TPU, HBM origins) | Technologies | Ticker-level exposure only |
| Military operations, diplomatic timelines, sanctions architecture | Geopolitics | Market-impact lens only |
| Alliance shifts, multilateral frameworks (BRICS, AUKUS) | Geopolitics | Market-impact lens only |
| Brazilian domestic politics, institutions, Plano Real | Brazil | Market impact (BRL, B3, ADRs) only |
| Brazilian macro policy, Copom decisions, fiscal framework | Brazil | Market impact only |
| Current positioning, price action, portfolio impact | Investing | Full treatment |
| Live policy triggers, active frameworks | Investing | Full treatment |

### Warning signs that investing is being used as a dumping ground

- Content whose natural home is another vault's lens (legislation → history; chip architecture → technologies; diplomatic timeline → geopolitics; Brazilian institution → Brazil)
- Dates predating the vault's time horizon (investing thinks in months/quarters; 5+ years old is precedent)
- Passed legislation cited as a live variable (it becomes history once enacted)
- Narrative arcs with beginning-middle-end (that's a historical story; investing writes the open chapter)
- "How did we get here" framing (that's literally the history vault's lede question)
- Content that doesn't change based on today's price, position, or catalyst

If two or more apply, the content's vault of record is a sibling vault, not investing.

### Proximity bias

The working directory pulls toward inlining — writing across vaults requires a context switch. Pay the switch cost. Future retrieval from the wrong vault is more expensive than one context switch during ingestion.

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
