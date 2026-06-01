# Analyst Watchlist

9 tracked analysts scanned by `/daily-scan`. When they publish new commentary, ingest their quotes, data points, and price calls into both their `Analysts/` note and the relevant concept/event notes — not just the source-person note.

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
| [[Brad Setser]] | [[Council on Foreign Relations]] | Cross-border capital flows, FX reserves, foreign Treasury demand, sovereign debt | `"Brad Setser" OR "Follow the Money" OR "Setser CFR"` |

## Scan discipline

1. Search the pattern for appearances in the last 48 hours: CNBC, Bloomberg, FT, research notes, interviews.
2. Check against the `Analysts/` note to see if the commentary is already captured.
3. If new, surface in the morning briefing's "Analyst signals" section.
4. Full ingestion (quotes into concept/event notes, not just the analyst note) happens via `/ingest URL` — the morning scan surfaces; `/ingest` writes.
5. X-primary sources (e.g., [[Brad Setser]] at [@Brad_Setser](https://x.com/Brad_Setser)): web search misses raw posts, so also sweep their X profile via Claude-in-Chrome MCP during `/daily-scan` when the authenticated browser is available. This is a triggered manual step, not autonomous — Chrome MCP needs the live logged-in session (Playwright has no cookies; X's API is gated). Load older posts before reading, ingest thesis-relevant ones via `/ingest`, and skip retweets/replies unless they carry original data or a call.

## Why these nine

Each covers a high-leverage corner of the vault's theses:

- **Commodities cohort (Croft, Currie, Kaneva, Blanch)** — four desks with distinct house views on oil and metals; consensus or dissent between them is itself a signal.
- **Macro independents (Alden, Pozsar)** — fiscal-dominance / monetary-plumbing frames that mainstream sell-side rarely articulates.
- **Equity strategists (Yardeni, Wilson)** — opposite poles of US equity positioning; their disagreement is durable enough to be a vault structure.
- **Capital flows (Setser)** — cross-border flows, FX-reserve accumulation, foreign Treasury demand, and sovereign debt. Added 2026-05-31 to close a structural gap: this is the domain behind the vault's [[Treasuries]] foreign-demand, [[De-dollarization]], [[Basis trade]], [[Dollar reserve status erosion]], and chip-exporter-FX ([[Korean won]] "DRam dollars") threads, which none of the other eight own. Primary outlets: the CFR [Follow the Money](https://www.cfr.org/blog/Setser) blog and X ([@Brad_Setser](https://x.com/Brad_Setser)); also tracked as a `/substacks` source.

Adding a tenth analyst should require a thesis-relevant gap, not just a name recognition vote.
