# Analyst Watchlist

8 tracked analysts scanned by `/morning-scan`. When they publish new commentary, ingest their quotes, data points, and price calls into both their actor note and the relevant concept/event notes — not just the analyst note.

## Watchlist

| Analyst | Firm | Focus | Search pattern |
|---------|------|-------|----------------|
| [[Helima Croft]] | [[RBC Capital]] | Oil, MENA, energy geopolitics | `"Helima Croft" OR "RBC commodities"` |
| [[Jeff Currie]] | [[Carlyle]] | Commodities supercycle, metals, macro regime | `"Jeff Currie" OR "Currie Carlyle"` |
| [[Natasha Kaneva]] | [[JPMorgan]] | Commodities | `"Natasha Kaneva" OR "JPMorgan commodities"` |
| [[Francisco Blanch]] | [[Bank of America]] | Commodities, oil | `"Francisco Blanch" OR "BofA commodities"` |
| [[Lyn Alden]] | Independent | Macro, fiscal dominance, energy-to-rates | `"Lyn Alden"` |
| [[Zoltan Pozsar]] | Ex Uno Plures | Rates, monetary plumbing, petrodollar | `"Zoltan Pozsar" OR "Ex Uno Plures"` |
| [[Ed Yardeni]] | Yardeni Research | Equity strategy, macro | `"Ed Yardeni" OR "Yardeni Research"` |
| [[Mike Wilson]] | [[Morgan Stanley]] | US equity strategy | `"Mike Wilson" OR "Morgan Stanley equity strategy"` |

## Scan discipline

1. Search the pattern for appearances in the last 48 hours: CNBC, Bloomberg, FT, research notes, interviews.
2. Check against the actor note to see if the commentary is already captured.
3. If new, surface in the morning briefing's "Analyst signals" section.
4. Full ingestion (quotes into concept/event notes, not just the analyst note) happens via `/ingest URL` — the morning scan surfaces; `/ingest` writes.

## Why these eight

Each covers a high-leverage corner of the vault's theses:

- **Commodities cohort (Croft, Currie, Kaneva, Blanch)** — four desks with distinct house views on oil and metals; consensus or dissent between them is itself a signal.
- **Macro independents (Alden, Pozsar)** — fiscal-dominance / monetary-plumbing frames that mainstream sell-side rarely articulates.
- **Equity strategists (Yardeni, Wilson)** — opposite poles of US equity positioning; their disagreement is durable enough to be a vault structure.

Adding a ninth analyst should require a thesis-relevant gap, not just a name recognition vote.
