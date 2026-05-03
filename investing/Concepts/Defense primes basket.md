---
aliases: [Defense primes, US defense primes, DEFPRIME]
tags: [basket/internal, defense, industrials, government]
---

# Defense primes basket

> [!warning] Cluster status: partial validation (May 2026)
> Intra-cluster correlation 0.52 (range 0.22-0.70), PC1 59.0%. The 7-name cohort partially validates — distinct from BA (commercial-aerospace dominated, +0.29 advantage) and broader industrials (HON/CAT/DE, +0.26 advantage), but doesn't fully cluster at 0.4 threshold. Pairs that emerge: LMT-NOC (aerospace/missile primes) and HII-LHX (naval + IT services). LDOS is a singleton (services-heavy mix). The DoD-customer factor is real but split across program-type sub-cohorts. See "Cluster validation" section below.

The seven public US defense primes — Lockheed Martin, RTX, Northrop Grumman, General Dynamics, Huntington Ingalls Industries, L3Harris, Leidos — share the DoD-customer end-market but split by program-type at the equity level. The cluster validates against external comparators (commercial aerospace BA; broader industrials HON/CAT/DE) but does not fully cohere internally.

---

## Constituents

7 names total, 2-name sub-pairs at the 0.4 threshold.

| Ticker | Company | PC1 loading | Sub-tier |
|--------|---------|-------------|----------|
| LMT | [[Lockheed Martin]] | 0.373 | Aerospace/missile primes (clusters with NOC) |
| NOC | [[Northrop Grumman]] | 0.410 | Aerospace/missile primes (clusters with LMT) |
| HII | [[Huntington Ingalls]] | 0.393 | Naval + IT (clusters with LHX) |
| LHX | [[L3Harris]] | 0.419 | Mixed comms / naval IT (clusters with HII) |
| RTX | [[RTX]] | 0.366 | Singleton — diversified commercial+defense aerospace + Pratt & Whitney |
| GD | [[General Dynamics]] | 0.376 | Singleton — diversified naval + IT + business jets (Gulfstream) |
| LDOS | [[Leidos]] | 0.295 | Singleton — IT services, weakest PC1 loading |

Internal ticker proposal: DEFPRIME.

### Excluded — and why

| Excluded | Why excluded |
|----------|--------------|
| [[Boeing]] (BA) | Commercial aerospace dominates revenue mix — only ~40% defense; trades on 737 MAX / 787 cycle, not DoD budget |
| Industrials (HON, CAT, DE) | Different end-market; +0.26 separation from defense primes |
| ITA (defense ETF) | The ETF is too broad — clusters with XLI/SPY in the test, not with defense pure-plays |

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/defense_primes.yaml`. Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.52 (range 0.22-0.70) | Just above 0.50 floor; range wide |
| Tightest pair | LHX-NOC = 0.66 (cross-tier); HII-LHX = 0.65 | Defense names cluster more by program-type than overall |
| PC1 explained variance | 59.0% | Moderate single factor |
| Hierarchical clustering at 0.4 | Sub-pairs LMT+NOC and HII+LHX; RTX/GD/LDOS singletons | Cluster splits by program-type |
| Cluster vs commercial aero (BA) | 0.23 (+0.29 advantage) | Clean separation from commercial-aerospace cycle |
| Cluster vs industrials (HON/CAT/DE) | 0.26 (+0.26 advantage) | Defense factor distinct from industrial-cycle factor |
| Cluster vs broad ETFs (ITA/XLI/SPY) | 0.42 (+0.10 advantage) | Defense modestly distinct from broad-market beta |

### Why the cluster doesn't fully cohere internally

The DoD-customer factor IS real (cluster cleanly separates from BA and industrials) but the program-type heterogeneity creates within-cluster sub-structure:

| Sub-tier | Members | Shared factor |
|---|---|---|
| Aerospace/missile primes | LMT, NOC | Tactical aircraft (F-35), missile defense, space; Air Force / Space Force budget |
| Naval + IT services | HII, LHX | Naval shipbuilding (HII = sole CVN/SSN builder); IT-heavy mix; Navy budget |
| Diversified primes | RTX, GD | Mixed commercial+defense (RTX) or naval+IT+jets (GD) |
| Pure IT services | LDOS | Services contracts; less hardware exposure |

LMT-NOC pair is the cleanest sub-cluster. HII-LHX pair is a Navy-IT-heavy bundle.

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long defense (broad) | Equal-weighted DEFPRIME (7 names) | DoD-customer factor |
| Long aerospace/missile primes | LMT + NOC pair | Air Force / Space Force budget cycle |
| Long Navy + IT | HII + LHX pair | Navy budget + IT services cycle |
| Pair: long DEFPRIME / short BA | Captures defense vs commercial-aerospace split (+0.29 separation) | Pure defense factor |
| Pair: long DEFPRIME / short XLI | Captures defense vs industrial cycle (+0.26 separation) | Defense vs civilian-cycle factor |
| AVOID: pair trades within DEFPRIME | Captures program-type differentials, not defense-vs-not-defense factor |

---

## Related

### Member actors

- [[Lockheed Martin]] — aerospace/missile prime (LMT-NOC pair)
- [[Northrop Grumman]] — aerospace/missile prime (LMT-NOC pair)
- [[Huntington Ingalls]] — naval shipbuilding (HII-LHX pair)
- [[L3Harris]] — naval IT + comms (HII-LHX pair)
- [[RTX]] — diversified prime (singleton)
- [[General Dynamics]] — diversified naval + IT + jets (singleton)
- [[Leidos]] — IT services (singleton)

### Adjacent concept notes

- [[Defense supply chain]] — upstream supplier landscape
- [[Trump defense budget]] — political driver of DoD-customer factor
- [[European defense spending]] — international comparator
- [[Defense Production Act]] — regulatory framework
- [[Private capital in defense tech]] — adjacent private-market thesis
- [[Boeing]] — commercial-aerospace comparator (NOT in cluster)

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/defense_primes.yaml` — config for this cluster

*Created 2026-05-03 — partial-validation note*
