---
aliases: [Drug distributors, Drug distribution, Pharmaceutical distributors, Drug wholesalers, Big-3 drug distributors]
tags: [sector, healthcare, distribution, drug-distribution, cluster-validation]
---

# Drug distributors

> [!success] Cluster status: VALIDATED — a distinct, robust drug-distribution factor; the campaign's most ETF-independent and most threshold-stable cohort (Jun 2026)
> The US drug-distribution big-3 ([[McKesson|MCK]]/[[Cencora|COR]]/[[Cardinal Health|CAH]]) trade as one tight factor — intra-corr 0.644 (weekly 0.682, HIGHER), PC1 76.3%, rejecting the random-basket and vol-matched nulls, with a STABLE 2Y holdout (ratio 0.93, loadings corr 0.876). And they are strikingly distinct: a +0.502 intra-advantage versus the healthcare and medical-device ETFs ([[XLV]]/IHI) — the LARGEST distinctness margin in the campaign — and +0.390 versus the adjacent healthcare distributor [[Henry Schein|HSIC]]. The big-3 form a clean cluster while XLV/IHI, HSIC, and SPY all sit apart; the threshold scan returns the cohort intact across a wide band ([0.40–0.70], stable width 0.30 — the widest of any validated-distinct cohort). This is the sixth genuinely distinct non-ETF factor in the campaign — and the purest "the basket beats every ETF" case — alongside [[Railroads]], [[Tobacco majors basket|tobacco]], [[Solid waste]], [[Life science tools]], and [[Trucking and LTL]].

The fee-based logistics layer of pharma. McKesson, Cencora, and Cardinal Health move ~90% of US prescription drugs on razor-thin margins, and their economics are nothing like the drugs they ship: generic deflation, branded-price inflation, fee-for-service distribution contracts, the opioid-settlement overhang, and high-volume new-modality flow (COVID products, then GLP-1s) drive all three together — and none of that is what moves drug-makers or device companies. That is why the cohort is so far from [[XLV]]: it is a regulated, oligopolistic logistics business wearing a healthcare label.

## Cluster validation

The candidate cohort is the three US drug-distribution majors — [[McKesson|MCK]], [[Cencora|COR]], [[Cardinal Health|CAH]] — tested against an adjacent healthcare distributor ([[Henry Schein|HSIC]], dental/medical), healthcare (XLV), medical devices (IHI), and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.644 [0.565–0.686] | well above the 0.50 floor; weekly 0.682 (HIGHER — robust) |
| PC1 explained variance | 76.3% | a strong single factor (weekly 78.8%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0006 | real cohesion beyond a random 3-pick |
| Vol-matched null p | 0.0006 / 0.0007 | cohesion exceeds vol-matched baskets — a real factor |
| Holdout (2Y split) | STABLE 0.93 | train 0.693 → test 0.644, loadings corr 0.876 (same structure) |
| Threshold stable width | 0.30 [0.40–0.70] | a clean separable cluster across the widest band in the campaign |
| Intra-adv vs adjacent (HSIC) | +0.390 | distinct from other healthcare distribution |
| Intra-adv vs ETFs (XLV/IHI/SPY) | +0.502 | the campaign's LARGEST — far from healthcare/medtech beta |

All US-listed. Config: `scripts/cluster_configs/mck.yaml`; registry row 2026-06-20.

### Boundary — the big-3 cluster alone; ETFs and HSIC all apart

![[drugdist-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. [[McKesson|MCK]]/[[Cencora|COR]]/[[Cardinal Health|CAH]] form one clean cluster; the healthcare ETF [[XLV]] and device ETF IHI pair off separately, the adjacent distributor [[Henry Schein|HSIC]] is its own node, and SPY is apart. Everything that is not a drug distributor is on the other side of the boundary — the signature of a distinct, non-replicable factor.*

The threshold scan returns the big-3 as a clean cluster across [0.40–0.70] (stable width 0.30) — the widest separable band of any validated-distinct cohort (waste 0.15, railroads 0.10, trucking 0.15). Combined with the +0.502 intra-advantage over the ETFs (the largest in the campaign) and the STABLE holdout, this is the strictest kind of validation: a tight, durable factor that no liquid ETF captures. [[Henry Schein|HSIC]] sitting apart (+0.390) shows even other healthcare distribution is a different factor — drug distribution is its own thing.

### Topology — three tight names, no internal split

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | MCK + COR | 0.314 | the two largest distributors |
| 2 | CAH + (MCK+COR) | 0.377 | the third joins tightly — no laggard |

The big-3 close at 0.377 — a tight, homogeneous cluster with no internal split (unlike the auto-parts duopoly + laggards). PC1 explains 76.3% with near-equal loadings, the mark of a clean single factor.

### PC1 index weights

![[drugdist-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 76.3% (weekly 78.8%) — a dominant common factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| MCK | 0.600 | 34.6% | 29.2% | 36.5% |
| COR | 0.566 | 32.7% | 33.0% | 30.4% |
| CAH | 0.565 | 32.6% | 30.3% | 33.1% |

Near-equal loadings (~0.57–0.60) — a genuine shared factor; [[McKesson|MCK]] (the largest, lowest-vol) carries the top weight.

### Distinctness — the campaign's most ETF-independent cohort

![[drugdist-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A uniformly hot MCK/COR/CAH block; XLV/IHI/HSIC are conspicuously cool against the three — far cooler than the three are against each other.*

The +0.502 intra-advantage versus the ETFs is the largest distinctness margin recorded in the campaign — larger than [[Solid waste|waste]]'s +0.424. The reason is structural: drug distribution is low-margin, regulated, fee-based logistics whose drivers (generic deflation, branded inflation, distribution-fee contracts, opioid-settlement cash flows, new-modality volume) are orthogonal to the drug-development and device-innovation cycles that move [[XLV]] and IHI. There is no ETF that isolates this factor; it must be owned as the [[McKesson|MCK]]/[[Cencora|COR]]/[[Cardinal Health|CAH]] basket.

### Historical tightness evolution

![[drugdist-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Durably tight (0.50–0.74), dipping only in 2024; currently near its highs.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.741 | 82.8% |
| 2022 | 0.669 | 78.0% |
| 2023 | 0.718 | 81.3% |
| 2024 | 0.504 | 67.0% |
| 2025 | 0.667 | 78.0% |
| 2026 | 0.696 | 79.8% |

Latest 90-day reading: intra 0.620, PC1 74.8%. The factor is durable — intra holds 0.50+ every year, the holdout is STABLE (0.93) with a near-identical factor structure across halves (loadings corr 0.876), and it is currently near its highs. A persistent, ownable oligopoly factor — the healthcare analogue of [[Solid waste|waste]] and [[Railroads|rail]] (defensive, fee/route-based oligopolies that escape their sector ETFs), and the most ETF-distinct of them all.

## Related

- [[Railroads]], [[Tobacco majors basket]], [[Solid waste]], [[Life science tools]], [[Trucking and LTL]] — the other genuinely distinct, non-ETF-replicable factors in the campaign
- [[McKesson]], [[Cencora]], [[Cardinal Health]] — the big-3 oligopoly
- [[Henry Schein]] — the adjacent healthcare distributor (dental/medical), a separate factor
- [[XLV]] — the healthcare ETF the cohort is most distinct from
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/mck.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
