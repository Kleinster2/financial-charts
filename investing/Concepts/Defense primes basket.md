---
aliases: [Defense primes, US defense primes, DEFPRIME]
tags: [basket/internal, defense, industrials, government]
---

# Defense primes basket

> [!success] Cluster status: validated at 6-name core, partial at 7-name (May 2026 matched methodology)
> 7-name cohort: intra-corr 0.512, PC1 58.59%, hierarchical clustering at 0.5 splits into 5-name core (LMT/RTX/NOC/HII/LHX) + GD/LDOS pair + singletons. 6-name core (excluding LDOS): intra-corr 0.556, PC1 64.31%, ALL 6 cluster together. LDOS is the IT-services singleton that drags the 7-name validation; removing it materially tightens the cohort. The cluster validates as 6-name (LMT/RTX/NOC/GD/HII/LHX) — DoD-customer factor is real, especially when IT-services are excluded. See full diagnostic below + cross-cohort comparison vs [[Space pure-plays]] (validated 0.624) and [[Concepts/Mag 7 cluster|Mag 7]] (falsified 0.316).

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

## Cluster validation compliance addendum (2026-06-07)

Generated from `scripts/cluster_configs/defense_primes.yaml` using `scripts/cluster_analysis.py` methodology. The 1Y diagnostic window is 2025-05-09 to 2026-05-08 (174 observations); the rolling history starts at `2020-01-01` where data are available.

### Required validation plots

![[defense-primes-cluster-correlation-1y.png]]

*One-year correlation heatmap for the `Defense primes` validation universe.*

![[defense-primes-cluster-dendrogram-1y.png]]

*Hierarchical clustering tree using average linkage on distance `1-|corr|`.*

![[defense-primes-cluster-pca-1y.png]]

*PCA diagnostic for the candidate cohort; PC1 explains 58.6% of standardized daily-return variance.*

### PC1 index weights vs cluster topology

The topology table answers which names join the tree first or last. The raw PC1-mimic table answers which raw-return weights best replicate the standardized common factor after realized-volatility scaling. These are deliberately different readings of the same cluster.

| Step | Left | Right | Distance (1-\|corr\|) | Read |
|---|---|---|---|---|
| 1 | LMT | NOC | 0.293 | Tightest merge |
| 2 | HII | LHX | 0.361 | Candidate cohort merge step |
| 3 | LMT+NOC | HII+LHX | 0.435 | Candidate cohort merge step |
| 4 | RTX | LMT+NOC+HII+LHX | 0.450 | Candidate cohort merge step |
| 5 | GD | LDOS | 0.487 | Candidate cohort merge step |
| 6 | RTX+LMT+NOC+HII+LHX | GD+LDOS | 0.559 | Final cohort join / loosest boundary |

| Ticker | PC1 loading | Normalized loading weight | Ann. vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| LMT | 0.377 | 14.30% | 25.70% | 15.30% |
| RTX | 0.362 | 13.74% | 25.59% | 14.78% |
| NOC | 0.413 | 15.68% | 26.64% | 16.19% |
| GD | 0.371 | 14.08% | 23.26% | 16.65% |
| HII | 0.390 | 14.80% | 37.68% | 10.81% |
| LHX | 0.419 | 15.91% | 26.52% | 16.50% |
| LDOS | 0.302 | 11.48% | 32.37% | 9.76% |

Interpretation: use the dendrogram / join-distance topology to identify the tight core and later-joining members; use the Raw PC1-mimic weight column only for investable factor-replication sizing.

### Historical tightness evolution

![[defense-primes-cluster-rolling-tightness-90d.png]]

*Ninety-day rolling tightness diagnostic: avg intra-correlation, PC1 share, core correlation, satellite-to-core correlation, and final candidate join distance.*

| Year | Avg corr median | PC1 median | Core corr median | Satellite-to-core median | Final join distance median |
|---|---|---|---|---|---|
| 2020 | 0.675 | 72.5% | 0.663 | 0.704 | 0.383 |
| 2021 | 0.560 | 62.8% | 0.552 | 0.588 | 0.553 |
| 2022 | 0.647 | 70.1% | 0.644 | 0.631 | 0.449 |
| 2023 | 0.636 | 70.0% | 0.613 | 0.693 | 0.493 |
| 2024 | 0.425 | 53.2% | 0.388 | 0.466 | 0.802 |
| 2025 | 0.445 | 53.3% | 0.472 | 0.412 | 0.656 |
| 2026 | 0.530 | 60.5% | 0.537 | 0.508 | 0.631 |

Latest 90D through 2026-05-08: avg corr 0.517, PC1 59.5%, core corr 0.501, satellite-to-core corr 0.556, final join distance 0.592.

Historical verdict: regime-dependent but measurable cluster; cohesion exists, but the rolling path is not consistently tight enough to call structurally durable.

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

*Created 2026-05-03 — partial-validation note. Expanded 2026-05-11 with matched-methodology re-run + 6-name core validation + advanced patterns.*

---

## Matched-methodology re-validation (May 11, 2026) — 6-name core cohort

Re-ran the diagnostic with methodology matched to [[Space pure-plays]] (1Y window through 2026-05-07, threshold 0.5). Tested both the 7-name original cohort and a 6-name core (excluding LDOS, the IT-services singleton with weakest PC1 loading in the original run).

| Cohort | N | Intra-corr | PC1 | Hierarchical clustering at 0.5 |
|---|---|---|---|---|
| 7-name (with LDOS) | 7 | 0.512 | 58.59% | Splits: 5-name core (LMT/RTX/NOC/HII/LHX) + GD/LDOS pair |
| 6-name core (no LDOS) | 6 | 0.556 | 64.31% | All 6 cluster together |

Removing LDOS tightens the cluster from 0.512 to 0.556 (+4pp) and lifts PC1 share from 58.6% to 64.3% (+6pp). The 6-name core is the cleaner expression of the defense-prime cluster. LDOS's 1Y cumulative return of -30.0% (vs +18-23% for top 6-name performers) confirms it's both factor-misaligned and a return drag.

### Stability across windows (6-name core)

The cluster is remarkably stable — intra-correlation barely moves across windows. No regime shift.

| Window | Obs | Intra-corr | Range | PC1 | PC2 | Vs BA | Gap |
|---|---|---|---|---|---|---|---|
| YTD 2026 | 88 | 0.578 | 0.38-0.73 | 66.5% | 13.3% | 0.333 | +0.245 |
| 1Y | 175 | 0.556 | 0.45-0.71 | 64.3% | 12.7% | 0.291 | +0.265 |
| 2Y | 231 | 0.586 | 0.47-0.71 | 65.8% | 11.3% | 0.399 | +0.187 |
| 3Y | 335 | 0.590 | 0.49-0.74 | 66.0% | 12.0% | 0.356 | +0.234 |

Cluster-vs-BA gap is consistently +0.19 to +0.27 across all windows. Defense primes is cleanly distinct from Boeing — the commercial-aerospace cycle doesn't drive defense returns.

### PC2 sub-structure — HII as the cohort's outlier

PC2 captures 12.7% of variance with [[Huntington Ingalls|HII]] (+0.77) as the dominant single-name loading. The other names cluster near zero or slightly negative.

| Ticker | PC2 loading | Read |
|---|---|---|
| HII | +0.77 | Sole naval shipbuilder (CVN/SSN); zero aerospace exposure |
| GD | -0.05 | Diversified (naval + IT + Gulfstream) |
| LHX | -0.10 | Mixed comms / naval IT |
| RTX | -0.31 | Engines + missile defense + Pratt & Whitney |
| LMT | -0.34 | Tactical aircraft + missile primes |
| NOC | -0.44 | Aerospace + space + missile defense |

PC2 isolates [[Huntington Ingalls|HII]] from the rest of the cohort. HII is the pure-naval-shipbuilder — sole builder of CVN aircraft carriers and SSN submarines, no aerospace exposure. The other 5 names all have aerospace + missile-defense overlap that PC2 captures as a single grouping. Compare to [[Space pure-plays]] PC2 (data vs hardware sleeves, ~equal sizes) and [[Sectors/Crypto-to-AI|Crypto-to-AI]] PC2 (pure miners vs AI-pivot, ~equal sizes) — defense primes' PC2 is a single-outlier structure, not a balanced 2-sleeve split.

### PC3 sub-structure — LMT vs RTX axis

PC3 captures 7.8% of variance:

| Ticker | PC3 loading | Read |
|---|---|---|
| LMT | +0.66 | Tactical aircraft + missile primes |
| NOC | +0.22 | Aerospace + space (smaller PC3 magnitude) |
| HII | +0.14 | Already isolated by PC2 |
| LHX | -0.26 | Mixed comms / naval IT |
| GD | -0.36 | Diversified naval + IT + jets |
| RTX | -0.55 | Engines + missile defense |

PC3 separates LMT (+0.66) from RTX (-0.55). The cleanest interpretation: program-type axis where LMT (missile + tactical aircraft) and RTX (engines + missile defense) trade on different DoD program-budget cycles. The Air Force / Space Force budget heavy on LMT; Navy/aircraft engine budget heavy on RTX. PC3 captures the residual program-mix divergence after PC1 (DoD factor) and PC2 (HII naval) have been extracted.

### Factor decomposition — defense factor is real

Regressing the equal-weighted 6-name basket against various benchmark combinations:

| Benchmarks | R² | Notes |
|---|---|---|
| SPY only | 7.4% | Defense barely tracks broad market |
| ITA only (aero+def ETF) | 57.8% | ITA captures ~58% of basket variance |
| ITA + SPY | 63.7% | SPY beta turns NEGATIVE (-0.52); defense names trade INVERSE to broad market controlling for ITA |
| ITA + SPY + XLI (industrials) | 63.8% | Industrials add nothing |

Residual cohort-specific factor: ~36%. Compare to:

- [[Space pure-plays]]: 59.6% residual after SPY+IWM+ITA
- [[Sectors/Crypto-to-AI|Crypto-to-AI]]: 37% residual after SPY+IBIT+QQQ+CRWV
- Defense primes (this cohort): 36% residual after ITA+SPY
- [[Concepts/Mag 7 cluster|Mag 7]]: 14.6% residual after broad benchmarks

Defense primes sits between Space pure-plays and Mag 7 in factor specificity. The interesting structural finding: SPY beta is essentially zero (+0.46 alone, -0.52 controlling for ITA). Defense primes is structurally insulated from broad market — even more than [[Space pure-plays]] (-0.12 SPY beta). The cluster has its own real factor that doesn't co-move with general equity risk.

### Subset optimization

Top 2-name expressions by tracking correlation to the 6-name basket:

| Pair | Intra-corr | Tracking corr | Sharpe | Cum % |
|---|---|---|---|---|
| NOC + HII | 0.528 | 0.935 | 0.35 | +7.2% |
| NOC + LHX | 0.661 | 0.924 | 0.25 | +4.4% |
| LMT + LHX | 0.559 | 0.918 | 0.76 | +12.9% |
| RTX + HII | 0.493 | 0.910 | 1.07 | +22.6% |
| HII + LHX | 0.639 | 0.909 | 0.87 | +19.3% |

Top 2-name expressions by Sharpe (different objective):

| Pair | Intra-corr | Tracking corr | Sharpe | Cum % |
|---|---|---|---|---|
| RTX + GD | 0.474 | 0.867 | 1.27 | +20.3% |
| RTX + LHX | 0.611 | 0.898 | 1.09 | +19.4% |
| RTX + HII | 0.493 | 0.910 | 1.07 | +22.6% |
| GD + LHX | 0.573 | 0.891 | 1.03 | +17.1% |
| GD + HII | 0.520 | 0.885 | 0.99 | +20.2% |

[[RTX]] appears in 3 of top-5 Sharpe pairs — the cohort's Swiss-Army-knife name. Same pattern as PL in [[Space pure-plays]] (PL in 2 of 3 optima), IREN in [[Sectors/Crypto-to-AI|Crypto-to-AI]] (4 of top-5 Sharpe pairs). Every validated cohort has one Swiss-Army-knife name that diversifies risk in pair combinations. RTX is that name here — diversified commercial+defense exposure makes its residual returns uncorrelated with the pure-defense names.

### Complement test — top tracking pair underperforms

Top tracking pair NOC+HII vs full 6 vs complement 4:

| Metric | Top 2 (NOC+HII) | Full 6 | Complement 4 |
|---|---|---|---|
| Cum return % | +7.2% | +13.3% | +16.5% |
| Annualized vol | 28.2% | 21.9% | 20.3% |
| Sharpe | 0.35 | 0.82 | 1.09 |

Same surprise pattern as [[Sectors/Crypto-to-AI|Crypto-to-AI]]: the factor-tracking-clean pair (NOC+HII) UNDERPERFORMS both the full basket and the complement on cumulative return AND Sharpe. The reason: NOC+HII both happen to be the cohort's lower-performing names this period (NOC -6.3%, HII +22.5% — NOC drags). The complement (LMT+RTX+GD+LHX) has the more diversified performers including RTX (top Sharpe Swiss-Army-knife name).

Pattern confirming: factor-tracking optimization ≠ return-maximizing whenever the high-Sharpe / high-return names have lower PC1 loadings or aren't the "factor-clean" tracker pair. The rule of thumb from [[Space pure-plays]] and [[Sectors/Crypto-to-AI|Crypto-to-AI]] holds here too.

### Per-name 1Y cumulative returns

| Ticker | 1Y return | Notes |
|---|---|---|
| RTX | +22.7% | Top performer; diversified commercial+defense |
| HII | +22.5% | Naval shipbuilder (Iran war / Golden Dome tailwind) |
| GD | +18.0% | Diversified naval + IT + Gulfstream |
| LHX | +16.2% | Mixed comms / naval IT |
| LMT | +9.6% | Aerospace + missile primes |
| NOC | -6.3% | Aerospace + space (relative underperformer) |
| LDOS (excluded) | -30.0% | IT services drag; confirms exclusion from 6-name core |

LDOS's -30% return validates the decision to exclude it from the core cohort. NOC's -6.3% is the surprise — aerospace/space prime that should have benefited from [[Golden Dome]] contract awards but lagged. Worth tracking what's happening at NOC specifically (Sentinel program issues? F-35 weighting? B-21 ramp pace?).

### Cross-cohort comparison

Defense primes joins the matched-methodology comparison set:

| Cluster | N | Avg intra-corr | PC1 variance | Specific factor | Verdict |
|---|---|---|---|---|---|
| [[Sectors/WFE\|WFE]] | 4 | 0.804 | 85.33% | — | Validated (tightest) |
| [[Sectors/Korea Memory\|Korea Memory]] | 2 | 0.756 | 87.82% | — | Validated (pair) |
| [[Sectors/US Memory\|US Memory]] | 3 | 0.696 | 79.72% | — | Validated |
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | 7 | 0.691 | 73.79% | 37.0% | Validated (tightest N=7) |
| [[Space pure-plays]] | 7 | 0.624 | 67.96% | 59.6% | Validated |
| [[Sectors/AI Compute\|AI Compute]] | 3 | 0.600 | 73.37% | — | Validated |
| Defense primes (6-core) | 6 | 0.556 | 64.31% | 36% | Validated |
| Defense primes (7-name) | 7 | 0.512 | 58.59% | — | Partial (LDOS drag) |
| [[Concepts/Mag 7 cluster\|Mag 7]] | 7 | 0.316 | 41.82% | 14.6% | Falsified |

The 6-name core sits in the validated band but at the lower end (intra-corr 0.556 — above the 0.50 floor but below the 0.60 typical for tighter clusters). PC1 share of 64.3% is moderate. Defense primes is a validated cluster with meaningful sub-structure (PC2 isolates HII; PC3 separates LMT vs RTX). Less coherent than the canonical AI / mining / space cohorts because the program-mix heterogeneity within defense is more substantive than the within-cohort variation in other tested clusters.

The 7-name cohort with LDOS slips below 0.55 intra-corr but stays above the 0.50 falsification threshold. The 6-name core is the cleaner expression of the cohort identity.

*Diagnostic source: `python scripts/cluster_analysis.py --config scripts/cluster_configs/defense_primes.yaml` + `defense_primes_core.yaml` + `python scripts/defense_primes_full_analysis.py`, May 11 2026 with methodology matched to [[Space pure-plays]].*

---

## Flow context — value trade → growth play (Foroohar, FT May 17)

[[Rana Foroohar]] in the [Financial Times](https://www.ft.com/content/713d7483-0ca6-46ae-b287-c501b5d81644) (May 17 2026) characterized the cohort as having transitioned from a "value trade" to a "growth play" — a framing shift driven by global conflict acceleration + AI / drone / sensor / robotics integration into modern warfare:

- US defence + aerospace ETF flows: **+573% YoY as of Q3 2025**; monthly record in March 2026
- Most absolute dollars still going to old-line primes (the cohort in this note)
- Most incremental growth + investor excitement around next-gen defence-tech firms ([[Anduril]], [[Palantir]], et al.) — but the primes still hold program-of-record contracts, qualified-supplier ecosystems, and security clearances

The "value-to-growth" reframing matters for cluster validation: a growth-play cohort tends to exhibit higher intra-correlation than a value cohort because shared growth-narrative beta dominates over idiosyncratic earnings drivers. The Defense primes' 0.556 intra-corr (above) is at the *lower* end of the validated band — consistent with "value cohort transitioning, not yet a fully integrated growth cluster." If the Foroohar thesis holds (procurement reform sustains ETF flows + secular tailwind continues), the intra-corr should drift higher over the next 4-8 quarters as the cohort behaves more uniformly.

Cross-link: the procurement-side framework lives in [[Defense procurement reform#Foroohar three-Ds framework + Navy shipbuilding plan (FT, May 17 2026)|Defense procurement reform — Foroohar three-Ds framework + May Navy shipbuilding plan]].
