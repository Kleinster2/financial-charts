---
aliases: [Brent-WTI differential, WTI-Brent spread, Atlantic Basin spread, transatlantic crude spread]
tags: [concept, energy, oil, benchmark, spread]
---

# Brent-WTI spread

The price difference between [[Brent crude]] (ICE, London) and [[WTI]] (NYMEX, [[CME Group]]) — the two dominant crude oil benchmarks. Expressed as Brent minus WTI. Positive = Brent premium (normal). Negative = WTI premium (inversion, historically rare).

---

## Synthesis

The spread is a live readout of how connected or disconnected the US oil market is from the rest of the world. In normal conditions, Brent trades $2-5 above WTI because WTI delivery is landlocked at Cushing, Oklahoma, while Brent is seaborne. But the spread's range and direction shift with structural changes in US energy infrastructure and global supply disruptions.

Three regimes dominate the historical record: (1) pre-2011, when the spread was narrow and occasionally inverted because the US was a net importer and Cushing congestion drove WTI below global prices; (2) 2011-2015, when the [[US Shale|shale revolution]] flooded Cushing faster than pipeline capacity could evacuate it, blowing the Brent premium to $20-25; (3) post-2015, when new pipeline capacity to the Gulf Coast normalized the spread to $3-7, reflecting export logistics costs. The [[2026 Iran conflict market impact|March 2026 Strait of Hormuz closure]] widened the spread again — Brent spiked harder than WTI because the disruption was physically distant from US supply chains. [[Amrita Sen]] ([[Energy Aspects]]) described a three-tier pricing structure: [[Dubai crude]] at $150-160 (Asian physical tightness), Brent in the middle ("most mispriced"), and WTI at the bottom (most shielded). Then on April 2, 2026, the spread inverted to -$2.51 — the first inversion since 2022 and deepest since 2010.

---

## How the spread works

| Factor | Widens spread (Brent premium) | Narrows/inverts (WTI premium) |
|--------|-------------------------------|-------------------------------|
| Gulf disruption ([[Strait of Hormuz]], [[OPEC]] cuts) | Brent exposed to seaborne supply loss | WTI insulated by domestic production |
| Cushing inventory | Low stocks tighten WTI | High stocks depress WTI |
| US export capacity | Pipeline bottlenecks trap WTI inland | Ample pipeline/export capacity lets WTI track global prices |
| US production growth | Overwhelming domestic capacity → WTI discount | Moderate growth absorbed by [[Gulf Coast refiners]] |
| [[Strategic Petroleum Reserve\|SPR]] releases | — | Adds WTI-grade supply, can push WTI up if market reads as tight |
| Speculative positioning | — | Pre-crisis short WTI / long Brent unwinds violently |

---

## Historical regimes

| Period | Avg spread | Driver |
|--------|-----------|--------|
| 2007-2010 | ~$1-3, frequent inversions | US net importer, Cushing congestion, financial crisis volatility |
| 2011-2014 | +$10-25 | Shale production outran pipeline capacity; Cushing glutted |
| 2015-2019 | +$3-7 | New pipeline capacity (Seaway reversal, Permian-to-Gulf builds) |
| 2020-2024 | +$3-6 | Stable, occasional compression during demand shocks |
| Feb 2026 (pre-conflict) | +$5.14 to +5.54 | Normal range |
| Mar 2026 (Iran conflict) | +$4.19 to +$16.97 | [[Strait of Hormuz]] closure; Brent spiked harder than WTI |
| Apr 2, 2026 | -$2.51 | Inversion — WTI +11.4% in a day, Brent +7.8% |

---

## Historical inversions

WTI above Brent is rare. Since 2007 (BZ=F data start):

| Year | Inversion days | Deepest |
|------|---------------|---------|
| 2007 | 99 | -$4.87 |
| 2008 | 197 | -$14.88 (Sep 22 — Lehman aftermath) |
| 2009 | 120 | -$2.37 |
| 2010 | 106 | -$2.68 |
| 2015 | 8 | -$1.00 |
| 2016 | 7 | -$0.60 |
| 2020 | 1 | -$0.16 |
| 2022 | 4 | -$0.68 |
| 2026 | 1 (Apr 2) | -$2.51 |

The 2007-2010 cluster was structural — US was still a net crude importer and [[Cushing]] storage dynamics dominated WTI pricing. Post-shale, inversions became fleeting and shallow. The April 2026 inversion at -$2.51 is the deepest since 2010 and warrants monitoring for persistence.

---

## April 2, 2026 inversion

WTI closed at $111.54, Brent at $109.03. Spread: -$2.51.

This contradicted the prevailing analyst consensus. [[Amrita Sen]] (Mar 23) had predicted the WTI-Brent spread would *widen further*, not invert. [[Robin J. Brooks]] framed WTI as the politically decisive benchmark but expected it to remain below Brent. The inversion suggests either a US-specific supply tightness ([[Iran|Iran]]-related refinery demand, SPR dynamics, pipeline flows) or a speculative unwind of the short-WTI positioning that [[Nadia Martin Wiggen]] ([[Stellen Capital]]) identified as at 10-year extremes pre-crisis.

The previous day (Apr 1) the spread was +$1.04 — nearly flat. The swing from +$1 to -$2.51 in a single session implies a sharp repositioning event, not gradual fundamental convergence.

![[brent-wti-spread-chart.png]]
*WTI (blue) vs Brent (red) since 2024, with spread below. Green = normal Brent premium; red = WTI premium (inversion). The April 2 inversion visible at far right.*

---

## Database

WTI futures: `CL=F` in `prices_long` (6,430 data points, from Aug 2000). Brent futures: `BZ=F` in `prices_long` (4,648 data points, from Jul 2007). Spread can be computed as a join on Date.

---

## Related

- [[WTI]] — US benchmark, NYMEX delivery at Cushing
- [[Brent crude]] — global benchmark, ICE London
- [[Dubai crude]] — Middle East physical benchmark (third tier in Sen's framework)
- [[Physical Oil Trading]] — the paper-vs-physical divergence that the spread reflects
- [[US Energy Independence Six Countries]] — why "US production" doesn't insulate all US regions equally
- [[Strategic Petroleum Reserve]] — SPR releases affect WTI directly
- [[Strait of Hormuz]] — primary risk factor widening the spread
- [[Iran conflict oil price timeline]] — chronological price action during March 2026
- [[Amrita Sen]] — three-tier pricing, predicted widening
- [[Robin J. Brooks]] — WTI as politically decisive benchmark
- [[Nadia Martin Wiggen]] — pre-crisis positioning extremes
- [[Cushing]] — WTI delivery point, storage dynamics

*Created 2026-04-03.*
