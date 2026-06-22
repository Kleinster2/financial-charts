---
aliases: [Railroads, Railways, Class I railroads, North American railroads, Rail operators]
tags: [sector, industrials, transports, railroads, cluster-validation]
---

# Railroads

> [!success] Cluster status: validated — a distinct, separable rail-oligopoly factor, NOT the transports ETF (Jun 2026)
> The five listed North American Class I railroads ([[Union Pacific|UNP]]/[[CSX]]/[[Norfolk Southern|NSC]]/[[Canadian Pacific Kansas City|CP]]/[[Canadian National|CNI]]) trade as one tight factor — intra-corr 0.646 (weekly 0.720), PC1 71.8%, rejecting the random-basket and vol-matched nulls at the floor. The standout: unlike most sectors this campaign measured, railroads do NOT collapse to their ETF. The five form their own clean dendrogram cluster, separate from the transports ETF IYT, freight (ODFL/UPS/FDX), industrials, and the market — threshold MODERATELY ROBUST [0.45–0.55], +0.203 vs IYT, +0.238 vs freight. IYT is dominated by trucking/air/parcel behaviour; the rail oligopoly is its own thing. Internal structure: a mild US (UNP/NSC/CSX) vs Canada (CP/CNI) sub-grouping, and the pending [[Union Pacific|UNP]]–[[Norfolk Southern|NSC]] merger inflates that pair to the cohort's tightest (0.095). A genuinely distinct factor — own the rail basket, not IYT.

The rare sector that owns a factor an ETF does not. After a long run of cohorts that resolved to their sector ETF (the energy legs to XLE/CRAK/OIH/AMLP, staples to XLP, big hotels to XLY), the North American Class I railroads are the exception: a five-name oligopoly (the only listed Class I's — BNSF is Berkshire-held, KCS folded into CPKC) with shared carload-volume, precision-scheduled-railroading, and pricing dynamics that the broad transports ETF (IYT — airlines + truckers + parcels + rails) does not isolate. To own the rail factor you hold the names, not IYT.

## Sector performance

![[railroads-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[IYT]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is the five listed North American Class I railroads — [[Union Pacific|UNP]], [[CSX]], [[Norfolk Southern|NSC]] (US), [[Canadian Pacific Kansas City|CP]], [[Canadian National|CNI]] (Canadian, NYSE-listed) — tested against freight/logistics (ODFL/UPS/FDX) and benchmarks (IYT transports ETF, XLI industrials, SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.646 [0.496–0.905] | tight; weekly 0.720 |
| PC1 explained variance | 71.8% | strong single factor (weekly 77.7%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | beats a random 5-pick at the floor |
| Vol-matched null p | 0.0001 (PC1 0.0003) | a real rail factor, not just shared vol |
| Holdout (2Y split) | WEAKENED 0.81 | durable-ish (train 0.797 → test 0.645; loadings corr near 0 is the equal-weight artifact) |
| Threshold clean width | 0.10 [0.45–0.55] | MODERATELY ROBUST — a separable cluster (freight/IYT only join at 0.60) |
| Intra-adv vs freight (ODFL/UPS/FDX) | +0.238 | clearly distinct from trucking/parcel |
| Intra-adv vs ETFs (IYT/XLI/SPY) | +0.203 | distinct — IYT is NOT inside the rail cluster |

All US-traded (the Canadian rails via their synchronous NYSE listings). Config: `scripts/cluster_configs/unp.yaml`; registry row 2026-06-19.

### Boundary — a clean, isolated rail cluster (IYT sits with freight, not rails)

![[railroads-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Orange: all five Class I rails (UNP/NSC/CSX + CP/CNI) — one isolated cluster. Green: the transports ETF IYT, industrials XLI, market SPY, and freight (ODFL/UPS/FDX). The two join only at ~0.57. IYT clusters with freight/industrials, NOT with the rails — the decisive distinctness.*

The threshold scan keeps the five-name cohort intact and uncontaminated across [0.45–0.55] (width 0.10, moderately robust); freight, IYT, XLI, and SPY only join at 0.60. This is the rare clean, separable result this campaign produces — the rails are not embedded in their sector ETF the way most cohorts are. The reason is what IYT contains: the Dow Transports ETF is mostly airlines, truckers, and parcel by return behaviour, so the five-name rail oligopoly (carload volumes, PSR operating ratios, the consolidation wave) trades on dynamics IYT averages away. Own the rail basket; IYT does not give you the factor.

### Topology — US/Canada sub-structure, and the merger-arb pair

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | UNP + NSC | 0.095 | the tightest pair — distorted by the pending UNP–NS merger (corr 0.90) |
| 2 | CP + CNI | 0.203 | the Canadian pair |
| 3 | CSX + (UNP+NSC) | 0.318 | the US sub-group closes |
| 4 | (CP+CNI) + (US) | 0.435 | US and Canada merge below the cut — one cohort |

Two structural features. First, a mild geography sub-grouping: the US rails ([[Union Pacific]]/[[Norfolk Southern]]/[[CSX]]) and the Canadian pair ([[Canadian Pacific Kansas City]]/[[Canadian National]]) form sub-blocks that merge at 0.435 — still one cohort, but a visible US/Canada seam. Second, the merger distortion: [[Union Pacific]]+[[Norfolk Southern]] is the tightest pair by a wide margin (0.095 vs the next-tightest 0.203), because the pending UNP acquisition of NSC (the proposed first US transcontinental railroad — STB accepted the revised application May 28 2026, expected close H1 2027) makes NSC trade as merger-arb on UNP's offer rather than on independent rail fundamentals. The cleaner read of the underlying rail factor is the non-merger names (CSX/CP/CNI).

### PC1 index weights

![[railroads-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains 71.8% (weekly 77.7%) with near-identical loadings (0.42–0.47) — a clean single factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| UNP | 0.473 | 21.2% | 22.5% | 21.3% |
| CSX | 0.428 | 19.2% | 22.8% | 19.0% |
| NSC | 0.468 | 21.0% | 21.1% | 22.4% |
| CP | 0.449 | 20.1% | 23.5% | 19.3% |
| CNI | 0.415 | 18.6% | 23.3% | 18.0% |

Near-equal loadings and uniform ~21–23% volatility — the five are interchangeable expressions of one rail factor, close to equal-weighted. [[Norfolk Southern]] (lowest vol, the merger target) takes the largest raw PC1-mimic weight.

### Distinctness — distinct from transports, freight, and market

![[railroads-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The rail block is uniformly hot; the freight names (ODFL/UPS/FDX) and IYT form a separate warm corner; the rails are cool against SPY.*

The two numbers that carry the verdict: +0.238 versus freight (the rails are not trucking/parcel — different volume and pricing cycles) and +0.203 versus the ETFs, with IYT sitting in the freight cluster rather than the rail one. That is the distinctness most cohorts this campaign lacked: railroads are a separable factor, not their sector ETF. Distinct from [[SPY]] (a real industrial-cyclical, not market beta). The investable read is the genuine exception — the five-name rail basket (or a rail-specific ETF) captures something IYT does not.

### Historical tightness evolution

![[railroads-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Durable — 0.67–0.78 every year, a structurally stable oligopoly factor.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.705 | 76.6% |
| 2022 | 0.758 | 80.8% |
| 2023 | 0.780 | 82.4% |
| 2024 | 0.674 | 73.9% |
| 2025 | 0.671 | 73.8% |
| 2026 | 0.704 | 76.5% |

Latest 90-day reading: intra 0.725, PC1 78.1%. The rail factor is durable — a five-name oligopoly running the same carload-volume/PSR business does not decohere (0.67–0.78 across six years, including the 2024 freight recession). The structural stability plus the IYT-distinctness is what makes this the campaign's cleanest "own the basket, not the ETF" verdict among the cyclicals — the rail oligopoly is a real, separable, durable factor.

## Related

- Old Dominion (ODFL), UPS, FedEx — LTL trucking + parcel, the adjacent freight the rails are distinct from (+0.238)
- [[Union Pacific]], [[CSX]], [[Norfolk Southern]] — the US Class I rails
- [[Canadian Pacific Kansas City]], [[Canadian National]] — the Canadian Class I rails (the geography sub-block)
- [[Airlines]] — another transport cyclical (also distinct from rails / broad IYT)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis (railroads = a rare non-ETF-replicable validated cohort)

---

*Created 2026-06-19. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/unp.yaml`; registry row 2026-06-19. The pending UNP–NS merger inflates the UNP/NSC pair (merger-arb). Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
