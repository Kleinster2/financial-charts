---
aliases: [Precious metals royalties, Gold royalties, Royalty and streaming, Precious-metals royalty and streaming, Royalty companies]
tags: [concept, commodities, metals, gold, royalties, cluster-validation]
---

# Precious metals royalties

Whether the capital-light precious-metals royalty and streaming companies trade as a factor distinct from the gold miners and the metal — or whether even a different business model collapses to gold. The cohort is four liquid royalty/streaming names: [[Franco-Nevada]] (FNV), [[Wheaton Precious Metals]] (WPM), [[Royal Gold]] (RGLD), [[Osisko Gold Royalties]] (OR). They do not mine — they buy royalties and metal streams on mines operated by others, so they carry no operating or capital-cost exposure, lower realized volatility, broad mine diversification, and embedded optionality. The validation answers the question cleanly: they cohere tightly and durably, but the factor binding them is gold, fully captured by the gold-miner ETF [[GDX]] and the metal [[GLD]]. The royalty model does not earn a distinct factor — the commodity-beta law is model-agnostic.

> [!warning] Cluster status: validated cohesion, but it is the gold complex — ETF-replicable by GDX (June 2026)
> The four royalty names are an extremely tight, durable, single-factor cohort: intra-corr 0.859 (weekly 0.876 — synchronous North American listings), PC1 89.4%, rejecting the independence, random-basket and vol-matched nulls all at the 0.0001 floor. But the cohesion is gold beta, not a distinct factor. The decisive numbers: a NEGATIVE −0.034 intra-advantage versus the gold-miner ETFs [[GDX]]/[[GDXJ]] (the royalties correlate with the miners ETF *more* than with each other), and a threshold scan with zero clean width — [[GDX]]/[[GDXJ]] contaminate the cohort from 0.20 and the metal [[GLD]] from 0.25, the earliest, most complete ETF-embedding in the campaign. The royalties add only a thin +0.106 equity/optionality premium over the flat metal — the same magnitude the miners carry — and are +0.475 versus SPY (it is gold, not market beta). Holdout STABLE (1.09 — durable). This is the gold sibling of [[Copper equity beta|copper]]: a real cohort that a single ETF replicates. The instructive contrast is [[Analog and auto-industrial semiconductors|analog semis]] — also held inside a broad ETF, but distinct there because the ETF (SMH) is dominated by a *different* factor (AI); here GDX is dominated by the *same* factor (gold), so the royalties simply are GDX. See below.

A different business model, the same trade. The premise that makes royalties interesting is that they are structurally unlike miners: no mines, no opex, no capex blowouts, no jurisdiction-specific operating disasters — just a diversified, capital-light claim on metal prices with optionality on reserve expansion. If any non-mining model could escape pure commodity beta, this would be it. It does not. [[Franco-Nevada]], [[Wheaton Precious Metals]], [[Royal Gold]] and [[Osisko Gold Royalties]] move as one because they are all levered to the same exogenous gold price, and that price is exactly what [[GDX]] and [[GLD]] already deliver. The model changes the risk profile (lower vol, more optionality) but not the factor.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.859 [0.819–0.894] | Very tight; weekly 0.876 (synchronous, clean) |
| PC1 explained variance | 89.4% | A near-pure single factor (weekly 90.7%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0001 | Floor — but a commodity cohort should crush this |
| Vol-matched null p (10k) | 0.0001 | Real beyond shared vol — still trivial for one-price names |
| Holdout (2Y split) | STABLE 1.09 | train 0.791 → test 0.859 — durable across regimes |
| Threshold clean width | 0.00 | GDX/GDXJ contaminate from 0.20, GLD from 0.25 — never isolates |
| Intra-adv vs miner ETFs (GDX/GDXJ) | −0.034 | Negative — correlates with the miners ETF more than itself |
| Intra-adv vs the metal (GLD) | +0.106 | A thin equity/optionality premium over flat gold |
| Intra-adv vs market (SPY) | +0.475 | It is gold, not market beta |

1Y daily log returns through 2026-06-18, threshold 0.5. All members North American (NYSE/Nasdaq/TSX) — synchronous, no async caveat. Config: `scripts/cluster_configs/precious_metals_royalties.yaml`; registry row 2026-06-20. SAND (Sandstorm) excluded — data-source download failed. Terminology: [[Cohort, cluster, basket]].

### Boundary — never a clean cluster, because it is the gold trade

![[royalties-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The four royalty names cluster tightly — but so do [[GDX]] (gold miners), [[GDXJ]] (junior miners), and [[GLD]] (the metal): everything gold merges into one cluster, and only SPY stays out. The cohort cannot be isolated from the miners ETF or the underlying metal.*

The threshold scan returns zero clean width, and the contamination order is the whole story — what the royalties cannot be distinguished from, tightest-first:

| Threshold | Joins the cohort cluster | Read |
|---|---|---|
| 0.20 | GDX, GDXJ | The gold-miner ETFs — the royalties *are* GDX from the tightest cut |
| 0.25 | + GLD | The gold price itself joins |
| 0.30–0.50 | (gold complex intact) | One gold cluster throughout |

GDX joining at 0.20 — the very first threshold — is the most complete ETF-embedding recorded in the campaign (copper's COPX also joined at 0.20; here both miner ETFs do). [[GDX]] holds [[Franco-Nevada|FNV]] and [[Wheaton Precious Metals|WPM]] among its top weights, so the cohort is literally inside its own benchmark.

### Topology — a tight tree, no outlier

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | WPM + OR | 0.106 | Tightest pair (corr 0.89) |
| 2 | FNV + (WPM+OR) | 0.125 | Franco-Nevada joins |
| 3 | RGLD + core | 0.164 | Royal Gold closes the cohort |

All four close by 0.164 — an exceptionally tight tree, tighter than any commodity-equity cohort in the family. There is no satellite: even the mid-cap [[Osisko Gold Royalties|OR]] sits in the core. The internal cohesion is real and high; it is the external boundary that fails.

### PC1 index weights

![[royalties-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains 89.4% with a tiny tail (PC2 4.8%) — a near-pure single factor, as expected when one metal price drives every name. Loadings are essentially identical (0.49–0.51).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| Franco-Nevada (FNV) | 0.501 | 25.1% | 37.0% | 28.6% |
| Wheaton (WPM) | 0.509 | 25.4% | 47.4% | 22.7% |
| Royal Gold (RGLD) | 0.490 | 24.5% | 39.9% | 26.0% |
| Osisko (OR) | 0.500 | 25.0% | 46.5% | 22.7% |

The loadings are the flattest in the campaign (0.49–0.51) — a perfectly uniform single factor. The lower-vol [[Franco-Nevada|FNV]] (37% annualized, the diversified large-cap) takes the largest vol-adjusted weight; but the PC1-mimic basket is just a worse-tracking [[GDX]], which already holds these names.

### Distinctness — it is gold, regardless of the model

![[royalties-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The royalty block is uniformly warm — but no warmer than its correlation to GDX and the metal. There is no royalty-equity factor that sits apart from gold.*

The intra-advantage numbers make the verdict quantitative: −0.034 versus the miner ETFs (GDX/GDXJ), +0.106 versus the metal (GLD), +0.475 versus the market (SPY). A royalty factor distinct from gold would show a clearly positive advantage versus GDX; −0.034 says the royalties are levered gold and almost nothing else — and correlate with the miners ETF marginally *more* than with each other. The +0.106 premium over flat gold is the equity/optionality content (the same thin premium the miners carry over the metal), not a separable factor. The royalty model lowers volatility and adds optionality, but the return driver is identical to the miners'.

### Historical tightness evolution

![[royalties-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Durably tight — 0.70 to 0.89 across the period — dipping only in the 2024 macro lull and tightening to 0.889 in the 2026 gold rally. The gold factor is always on; it varies in strength with the metal cycle, not in existence.*

| Year | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2020 | 0.794 | 84.6% | 0.229 |
| 2022 | 0.850 | 88.8% | 0.175 |
| 2024 | 0.697 | 77.3% | 0.344 |
| 2025 | 0.794 | 84.6% | 0.256 |
| 2026 | 0.889 | 91.6% | 0.127 |

*Durable, not regime-dependent in existence: the cohort is a real cluster every year, tightening and loosening with the gold cycle. The holdout STABLE reading (1.09) reflects the cohort tightening into the 2025-26 gold bull (test 0.86 > train 0.79); the low PC1-loadings correlation across halves (0.26) is a flat-vector artifact — when all four names load ~0.50, the loadings correlation measures noise, not a structural break (the same caveat as [[Analog and auto-industrial semiconductors|analog semis]], and the inverse of [[Rare earth equity beta|rare earths]] where low loadings-corr coincided with a collapsed train-half intra). Latest 90-day: intra 0.889, PC1 91.7%.*

### The read-through

- The royalties are one factor, and that factor is gold. Own [[GDX]] for the levered gold-equity beta or [[GLD]] for the metal; a hand-picked basket of royalty names is a worse-tracking GDX. There is no separable royalty-equity factor to harvest (+0.106 over the price, the same as the miners).
- Business model does not create a factor; the commodity does. The capital-light, lower-vol, optionality-rich royalty model is genuinely different from mining — yet it produces the same factor, because both are levered to one exogenous price. The campaign's commodity-beta law is model-agnostic.
- The ETF-embedding is the most complete in the campaign. GDX and GDXJ contaminate from threshold 0.20 (GDX literally holds FNV/WPM at top weight), and the metal GLD from 0.25 — there is no threshold at which the royalties stand alone.
- Single-name selection is risk-profile, not factor. Choosing [[Franco-Nevada|FNV]] (diversified, lower vol) over [[Osisko Gold Royalties|OR]] (mid-cap, Canada-weighted) is a volatility and diversification choice on top of the same gold beta, not a different trade.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-20).

## Related

- [[Gold equity beta]] — the gold-miners cohort; the royalties are its capital-light sibling and reach the same verdict (= gold)
- [[Franco-Nevada]], [[Wheaton Precious Metals]], [[Royal Gold]], [[Osisko Gold Royalties]] — the cohort members
- [[GDX]], [[GDXJ]] — the gold-miner ETFs the royalties cannot be distinguished from (contaminate from 0.20)
- [[GLD]] — the metal the cohort tracks (joins at 0.25)
- [[Copper equity beta]], [[Lithium equity beta]], [[Uranium equity beta]], [[Steel and aluminum equity beta]] — the commodity-beta family; royalties confirm the law is model-agnostic
- [[Analog and auto-industrial semiconductors]] — the instructive contrast: held inside an ETF dominated by a *different* factor, so distinct; royalties are inside an ETF dominated by the *same* factor, so not
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/precious_metals_royalties.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
