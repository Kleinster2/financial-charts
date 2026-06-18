---
aliases: [Tower REITs, Cell tower REITs, US tower REITs, Tower REIT cluster]
tags: [sector, reit, telecom-infrastructure, towers, usa, cluster-validation]
---

# Tower REITs

> [!success] Cluster status: validated — a tight, durable factor, distinct from data-center REITs but embedded in broad REITs (Jun 2026)
> The three US cell-tower REITs ([[American Tower|AMT]]/[[Crown Castle|CCI]]/[[SBA Communications|SBAC]]) trade as one tight factor. Intra-corr 0.730 (weekly 0.794), PC1 82.1%, all three cluster, random-basket null rejected at the 0.0001 floor, holdout STABLE 0.89, durable at 0.77–0.89 every year since 2020. The standout is the +0.418 intra-advantage versus data-center REITs ([[DC REITs|EQIX/DLR]]): "digital-infrastructure REITs" are two distinct factors, not one — towers trade on rate sensitivity and wireless-carrier leasing, data centers on AI/cloud demand. But the cohort is embedded in the broad rate-driven REIT complex — VNQ joins it at 0.43, so the threshold band is narrow [0.35–0.40] and the factor is largely VNQ-replicable. A durable, distinct-from-data-centers but ETF-embedded tower factor.

The cell-tower REITs are the landlords of the [[Telecom|US wireless carriers]]: they own the physical towers and lease vertical space to [[AT&T]], [[Verizon]], and [[T-Mobile]] under long-duration, escalating contracts. That gives them long-dated, bond-like cash flows — which is why they trade as a tight, rate-sensitive factor, and why they sit inside the broad REIT complex rather than apart from it. What they are NOT is the same trade as the data-center REITs: despite both being "digital infrastructure," towers (rate + wireless leasing) and data centers (AI/cloud capacity demand) are sharply separable factors.

## Cluster validation

The candidate cohort is the three US cell-tower REITs — [[American Tower|AMT]], [[Crown Castle|CCI]], [[SBA Communications|SBAC]] — tested against the data-center REITs ([[DC REITs|EQIX/DLR]]) and benchmarks (VNQ broad-REIT ETF, TLT long-bond/rate proxy, SPY).

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.730 [0.654–0.823] | tight; weekly 0.794 |
| PC1 explained variance | 82.1% | strong single factor (weekly 86.4%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 (PC1 0.0001) | rejects at the floor — a real factor |
| Holdout (2Y split) | STABLE 0.89 | durable (the −0.91 loadings corr is the equal-weight artifact — near-identical loadings have no stable orientation) |
| Threshold clean width | 0.05 [0.35–0.40] | NARROW — VNQ joins at 0.43, so the cohort is embedded in broad REITs |
| Intra-adv vs data-center REITs (EQIX/DLR) | +0.418 | sharply distinct — towers ≠ data centers |
| Intra-adv vs ETFs (VNQ/TLT/SPY) | +0.447 | distinct from TLT/SPY, but VNQ sits inside the cluster |

1Y daily log returns through 2026-06-15, threshold 0.5. All US-listed (synchronous). Config: `scripts/cluster_configs/amt.yaml`; registry row 2026-06-18. Terminology: [[Cohort, cluster, basket]].

### Boundary — towers cluster with broad REITs; data centers split off

![[tower-reits-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. AMT/CCI/SBAC form a tight cluster that the broad-REIT ETF VNQ joins at 0.43; the data-center REITs ([[DC REITs|EQIX/DLR]]) cluster separately, and TLT/SPY sit apart. Towers are the rate-driven broad-REIT factor, distinct from data centers.*

The threshold scan keeps the tower cohort clean only over [0.35–0.40] — a narrow band, because VNQ joins at 0.43. That is the "real but embedded" signature: the towers genuinely co-move (intra 0.73), but they are the broad rate-driven REIT factor rather than a separable tower-only one, so VNQ replicates most of it. What is NOT replicated is the separation from data centers: the +0.418 intra-advantage versus EQIX/DLR is one of the larger sub-sector separations in the campaign.

### Topology — a homogeneous three-name block

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | AMT + CCI | 0.177 | tightest pair (corr 0.82) |
| 2 | SBAC + (AMT+CCI) | 0.316 | SBA joins — the cohort closes below 0.32 |

All three join below distance 0.32 (correlation above 0.68) — a homogeneous block with no core/satellite split. [[American Tower]] and [[Crown Castle]] are the tightest pair; [[SBA Communications]] (the smaller, higher-vol, Latin-America-tilted name) joins just behind. Same business, same rate-and-leasing driver.

### PC1 index weights

![[tower-reits-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains 82.1% with near-identical loadings (0.55–0.60) — a clean single factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| American Tower (AMT) | 0.582 | 33.6% | 25.7% | 38.1% |
| Crown Castle (CCI) | 0.597 | 34.5% | 28.7% | 35.0% |
| SBA Communications (SBAC) | 0.552 | 31.9% | 34.4% | 27.0% |

Near-equal loadings; the lower-vol [[American Tower]] takes the largest raw PC1-mimic weight, the higher-vol [[SBA Communications]] the smallest. The cohort is close to equal-weighted — the three are interchangeable expressions of one tower-REIT factor.

### Distinctness — distinct from data centers, embedded in broad REITs

![[tower-reits-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The tower block is uniformly hot; data-center REITs (EQIX/DLR) form a separate warm corner; the towers are cool against TLT and SPY but warm against VNQ.*

The two numbers that define the cohort: +0.418 versus data-center REITs (towers are their own digital-infra factor, not the AI/cloud one) and VNQ sitting inside the cluster (towers are the rate-driven broad-REIT factor). So the investable read is forked: own VNQ if you want the broad rate-sensitive REIT exposure that the towers largely are; own the AMT/CCI/SBAC names specifically only for the tower-vs-data-center distinction — the one thing VNQ does not give you, since VNQ contains both. Distinct from TLT (it is not simply a bond proxy) and from SPY (+0.447 — low market beta).

### Historical tightness evolution

![[tower-reits-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Exceptionally durable — 0.77–0.89 every single year, one of the most structurally stable cohorts in the campaign.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.888 | 92.5% |
| 2021 | 0.797 | 86.4% |
| 2022 | 0.831 | 88.8% |
| 2023 | 0.828 | 88.5% |
| 2024 | 0.817 | 87.8% |
| 2025 | 0.825 | 88.3% |
| 2026 | 0.769 | 84.6% |

Tower REITs are among the most durable cohorts measured — intra-corr never leaves 0.77–0.89 across six years, including the 2022 rate shock that hit all long-duration REITs together. That durability is itself the tell: a three-name oligopoly running the same long-duration-lease business with the same dominant driver (rates) does not decohere. Unlike the regime-dependent restaurants or managed care, the tower factor is structural — but structural and broad-REIT-embedded at once, which is why VNQ captures most of it.

## Related

- [[American Tower]], [[Crown Castle]], [[SBA Communications]] — the three US tower REITs
- [[DC REITs]] — data-center REITs, the sharply distinct sibling (+0.418)
- [[REITs]] — the broad REIT hub (VNQ, the complex the towers are embedded in)
- [[Telecom]] — the wireless carriers the towers lease to
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-18. 1Y daily log returns through 2026-06-15; config `scripts/cluster_configs/amt.yaml`; registry row 2026-06-18. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
