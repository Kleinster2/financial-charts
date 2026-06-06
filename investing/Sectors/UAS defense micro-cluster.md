---
aliases: [UAS pair, KTOS-AVAV pair, Drone defense pair, UAS pure-plays]
---
#sector #defense #uas #drones #micro-cluster #public

# UAS defense micro-cluster

A 2-name validated micro-cluster of publicly-traded UAS (uncrewed aerial systems) defense pure-plays. Currently contains [[Kratos]] (KTOS) and [[AeroVironment]] (AVAV). Latest validation through the Jun. 3 2026 local close shows 0.678 trailing-1Y pair correlation, separated from defense primes by +0.31, from broad ETFs by +0.24, and from the [[Space pure-plays]] cohort by +0.21. This is a genuine micro-cluster, but too small to be a full sector cohort note in the conventional sense.

> [!info] Micro-cluster status
> Real 2-name pair with measurable internal cohesion. Not yet a tradeable basket at the same depth as [[Space pure-plays]] or [[WFE]] — needs 3-5 more pure-play candidates to reach full cohort status. Track as expansion candidate when [[Karman Holdings]] (KRMN) or other pure-UAS publics become liquid.

---

## Normalized return chart (Jan 2025 → latest local close, Jun. 3 2026)

![[ktos-vs-avav-price-chart-2025.png]]
*KTOS and AVAV normalized from the common Jan. 6 2025 start through the latest local close, Jun. 3 2026. KTOS (+98%) outperformed AVAV (+17%) over the window, but the two still show 0.678 trailing-1Y daily-return correlation; this is a co-movement cluster with meaningful outcome dispersion, not a same-return pair.*

---

## Members

| Ticker | Actor | Business |
|---|---|---|
| KTOS | [[Kratos]] | Target drones, hypersonic systems, satellite communications, ground systems |
| AVAV | [[AeroVironment]] | Loitering munitions (Switchblade), tactical UAS, small unmanned systems |

Both names share the structural profile of small-mid-cap defense pure-play with UAS / drone-defense exposure that maps to [[Golden Dome]] adjacent demand (target drones, ISR, loitering munitions for layered defense) but operates outside the heritage defense-prime envelope.

---

## Pairwise correlation

| Pair | Correlation (1Y) |
|---|---|
| KTOS - AVAV | 0.678 |

That's the entire intra-cluster matrix at 2 names. Window: daily returns from Jun. 6 2025 through Jun. 3 2026 (189 observations), using canonical `prices_long`.

---

## Separation from controls

How distinct is the pair from adjacent cohorts? Avg correlation of the pair to each reference group over the trailing 1Y:

| Reference | Pair avg correlation | Read |
|---|---|---|
| [[Space pure-plays]] (RKLB cohort) | 0.464 | Distinct from space cluster |
| Heritage defense primes (LMT, RTX, NOC, LHX avg) | 0.368 | Distinct from primes |
| [[LHX]] (closest single prime) | 0.472 | Closest defense-prime peer |
| [[ITA]] (aerospace + defense ETF) | 0.548 | Closest broad defense benchmark |
| [[IWM]] (small-cap) | 0.420 | Some small-cap beta, not the dominant driver |
| [[SPY]] | 0.362 | Mostly distinct from broad market |

The pair has a +0.21 to +0.32 intra-advantage vs the space cohort, defense-prime cohort, IWM, and SPY. ITA remains the closest reference, but the pair still has a +0.13 intra-advantage over the broad aerospace-and-defense ETF. KTOS-AVAV is genuinely its own thematic space, distinct from both space pure-plays and traditional primes — just very small (only 2 names).

---

## Why this isn't yet a full cohort

A 2-name "cluster" is a pair, not a cohort. The validation diagnostics that work for the [[Space pure-plays]] cohort (7 names) — average correlation, hierarchical clustering with cohort vs control groups, PCA on candidate cohort — degenerate or become uninformative at N=2 (average is just the pair, hierarchical clustering trivially groups them, PCA has only one meaningful component).

Tested in the cluster-validation work documented in [[Space pure-plays#Tested hypothesis — Golden Dome defense-tech super-cluster (falsified)|Space pure-plays Golden-Dome-test section]]: adding MRCY, BWXT, HEI, LDOS, PSN, or CACI to KTOS-AVAV all loosened the cluster rather than strengthening it. Specifically:

| Candidate | Avg corr to KTOS-AVAV |
|---|---|
| [[Mercury Systems]] (MRCY) | 0.566 |
| [[BWXT]] | 0.474 |
| [[Leidos]] (LDOS) | 0.400 |
| [[CACI]] | 0.366 |
| [[Heico]] (HEI) | 0.356 |
| [[Parsons]] (PSN) | 0.327 |

Every candidate falls below the pair-internal 0.678 — adding any of them would dilute the cluster's internal cohesion. MRCY remains the closest watch-list addition, but it is still a defense-electronics adjacency rather than a pure UAS member. The 2-name pair stands on its own; the natural extensions don't exist in the current local universe.

---

## Expansion candidates (when available)

The cluster could grow if new pure-play UAS / loitering-munitions / drone-defense names list publicly with sufficient float and trading history:

| Candidate | Status | Why it might fit |
|---|---|---|
| [[Karman Holdings]] (KRMN) | Public 2025+ | Missile defense + fairings; small-cap defense |
| Red Cat Holdings (RCAT) | Public micro-cap | UAS pure-play, currently too thin to validate |
| Edge Autonomy | Private (owned by [[Redwire]]) | Stalker + Penguin UAS — integrated into RDW post-2025 acquisition |
| Mach Industries | Private | Hypersonic + drone defense |
| Anduril | Private | Pre-IPO; would be #1 candidate when public |

The likely path to a full UAS-defense cohort is one or more of [[Anduril]] / Mach / others going public. Until then, KTOS-AVAV is the entire public-tradeable UAS-defense thematic.

---

## Related

### Cohort context
- [[Space pure-plays]] — adjacent sibling cluster; the more developed thematic cohort with 7 validated names
- [[Defense]] — broader sector hub (heritage primes + diversified defense)

### Concepts
- [[Golden Dome]] — adjacent defense program; target drones / hypersonic systems / loitering munitions all map to Golden Dome demand
- [[Drone warfare]] — operational concept that drives demand for both KTOS and AVAV products

### Members
- [[Kratos]] — primary member
- [[AeroVironment]] — primary member

### Tested but rejected as cohort additions
- [[Mercury Systems]] — adjacent defense electronics, doesn't strengthen cluster
- [[BWXT]] — naval/space nuclear, different business model
- [[Heico]] — commercial aerospace heavy

*Created 2026-05-11 as micro-cluster note. Status: validated pair, waiting for expansion candidates to reach full cohort scale. Updated 2026-06-05 with current local-price validation through Jun. 3.*
