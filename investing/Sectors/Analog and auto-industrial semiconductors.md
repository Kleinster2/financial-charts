---
aliases: [Analog and auto-industrial semiconductors, Analog semiconductors, Analog semis, Analog chips, Auto and industrial semiconductors, Analog semi cohort]
tags: [sector, technology, semiconductors, analog, cluster-validation]
---

# Analog and auto-industrial semiconductors

> [!success] Cluster status: VALIDATED — a distinct, durable auto/industrial-semiconductor factor; the cap-weighted semi ETF does not capture it (Jun 2026)
> The analog/mixed-signal/microcontroller/power names ([[Texas Instruments|TXN]]/[[Analog Devices|ADI]]/[[Microchip Technology|MCHP]]/[[onsemi|ON]]/[[NXP|NXPI]]/[[STMicro|STM]]) trade as one tight, durable factor — intra-corr 0.729, PC1 77.5%, rejecting the independence, random-basket and vol-matched nulls all at the 0.0001 floor — and it is genuinely distinct. The decisive numbers: a clean separable threshold band [0.35–0.50] (stable width 0.15, WIDE) where the six names form one uncontaminated cluster, and a +0.446 intra-advantage versus the AI-compute names ([[Nvidia|NVDA]]/[[Broadcom|AVGO]]) — the two semiconductor cycles decoupled in 2024-25. The subtle part is the +0.079 intra-advantage versus the broad semi ETF [[SMH]]/[[SOXX]]: thin, yet the cohort separates cleanly because SMH is cap-weighted and AI-dominated (NVDA/AVGO/TSM are ~40%+), so the ETF tracks the AI-compute pole, not these names — it holds the analog names but does not track them, and no pure analog-semi ETF exists. This is the campaign's 9th distinct non-ETF factor and the first semiconductor one: every prior semi cohort (fabless AI, WFE equipment, foundry, memory) was ETF-replicable or regime-dependent. The holdout is WEAKENED (0.81) — durable but normalizing off the extreme 2024-25 inventory-correction peak (train intra 0.90).

The other semiconductor cycle. The semiconductor map is dominated by the AI-compute boom — GPUs, custom accelerators, HBM, the WFE tools and foundry that build them. This cohort is the part that runs on a completely different clock: analog, mixed-signal, microcontrollers, and power chips whose end-markets are autos, industrial equipment, and the broad electronics supply chain, governed by the inventory cycle (the 2022-23 shortage, the 2024-25 destock) rather than by hyperscaler capex. The 2024-25 divergence proved they are a separate factor: the AI names ([[Nvidia|NVDA]], [[Broadcom|AVGO]]) ripped on data-center demand while [[Texas Instruments|TXN]], [[Analog Devices|ADI]], [[onsemi|ON]] and the rest languished on the auto/industrial destock. The cap-weighted broad semi ETF, dominated by the AI mega-caps, captures the first cycle and not the second — which is exactly why this concentrated basket is distinct and not ETF-replicable.

## Cluster validation

The candidate cohort is six analog/auto-industrial semiconductor makers — [[Texas Instruments|TXN]], [[Analog Devices|ADI]], [[Microchip Technology|MCHP]], [[onsemi|ON]], [[NXP|NXPI]], [[STMicro|STM]] — tested against the broad semi ETFs ([[SMH]]/[[SOXX]]), the AI-compute names ([[Nvidia|NVDA]]/[[Broadcom|AVGO]]), and the market (SPY). 1Y window through 2026-06-18, threshold 0.5. All US-listed/synchronous (STM via its NYSE line). Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.729 [0.637–0.817] | Tight and uniform, no outlier; weekly 0.676 |
| PC1 explained variance | 77.5% | A strong single factor (weekly 73.1%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0001 | Far beyond a random 6-pick (null mean 0.150, 99th 0.345) |
| Vol-matched null p (10k) | 0.0001 | Real beyond shared vol (null mean 0.160) — not just high-beta |
| Holdout (2Y split) | WEAKENED 0.81 | train 0.901 (PC1 92%) → test 0.729 (PC1 78%) — durable, off a peak |
| Threshold stable width | 0.15 [0.35–0.50] | WIDE — a clean cluster; SMH/SOXX/NVDA/AVGO/SPY contaminate only at 0.55 |
| Intra-adv vs semi ETF (SMH/SOXX) | +0.079 | Positive but thin — the cap-weighted ETF tracks the AI pole, not these names |
| Intra-adv vs AI-compute (NVDA/AVGO) | +0.446 | The two semi cycles decoupled — the core distinctness number |
| Intra-adv vs market (SPY) | +0.217 | Distinct from the broad market |

Config: `scripts/cluster_configs/analog_semis.yaml`; registry row 2026-06-20.

### Boundary — a clean cluster across [0.35–0.50]; the ETF sits with the AI pole

![[analog-semis-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The six analog names form their own cluster; the broad semi ETFs [[SMH]]/[[SOXX]] cluster with the AI-compute names [[Nvidia|NVDA]]/[[Broadcom|AVGO]] and SPY — not with the analog cohort. The cap-weighted semi ETF tracks the AI mega-caps it is concentrated in, which is why it lands on the other side of the tree.*

The threshold scan returns a WIDE stable band — the six names are one intact, uncontaminated cluster across [0.35–0.50] (stable width 0.15):

| Threshold | State | Read |
|---|---|---|
| 0.20–0.30 | the cohort fragments (5 → 2 subclusters) | tightest pairs only |
| 0.35–0.50 | one clean cluster, all six, zero contamination | the separable band (width 0.15, WIDE) |
| 0.55+ | SMH, SOXX, NVDA, AVGO, SPY all join at once | the broad-market/AI merge — the whole universe |

The contamination signature is the tell: nothing joins the cohort gradually. The entire rest of the universe — the ETFs, the AI names, and the market — merges in together at 0.55, the generic risk-on threshold. Below that, the analog cohort stands alone. This is the separable-band signature of a distinct factor, the same shape as [[Trucking and LTL|trucking]] and [[Tankers|tankers]].

### Topology — a tight power/MCU core, all six close by 0.30

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | MCHP + ON | 0.183 | the microcontroller/power pair (corr 0.82) |
| 2 | ADI + (MCHP+ON) | 0.220 | Analog Devices joins |
| 3 | TXN + core | 0.247 | the analog bellwether joins |
| 4 | NXPI + core | 0.294 | NXP joins |
| 5 | STM + core | 0.304 | STMicro closes the cohort |

All six close by 0.304 — tighter than copper's 0.387-for-six, a genuinely cohesive tree with no outlier (the contrast with [[Rare earth equity beta|rare earths]], where Lynas never joined). [[Microchip Technology|MCHP]] and [[onsemi|ON]] are the tight core (the MCU/power pair); [[NXP|NXPI]] and [[STMicro|STM]] are the loosest members but still well inside the cut.

### PC1 index weights — a flat, balanced factor

![[analog-semis-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 77.5% (weekly 73.1%) with near-equal loadings (0.39–0.43) — a single common factor, no name dominating.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| TXN | 0.399 | 16.3% | 43.6% | 17.2% |
| ADI | 0.410 | 16.8% | 33.9% | 22.7% |
| MCHP | 0.430 | 17.6% | 47.1% | 17.2% |
| ON | 0.422 | 17.2% | 55.9% | 14.2% |
| NXPI | 0.394 | 16.1% | 48.1% | 15.4% |
| STM | 0.392 | 16.0% | 55.1% | 13.4% |

Loadings are flat (0.39–0.43): no single name carries the factor. The lowest-vol name [[Analog Devices|ADI]] (34% annualized) takes the largest vol-adjusted weight (22.7%); the high-vol [[onsemi|ON]]/[[STMicro|STM]] (55%) the smallest. The vols are moderate (34–56%) — these are large, profitable IDMs, not the speculative small-caps of the rare-earth or space cohorts, which is why the vol-matched null is cleared so decisively.

### Distinctness — SMH holds them but does not track them

![[analog-semis-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A uniformly warm analog block (0.64–0.82); the broad semi ETFs warm against it but warmer still against the AI names; the AI-compute pair ([[Nvidia|NVDA]]/[[Broadcom|AVGO]]) distinctly cooler against the analog block.*

The intra-advantage numbers tell the structural story: +0.446 versus the AI-compute names (the analog and AI semi cycles are different factors), +0.217 versus the market, and only +0.079 versus the broad semi ETF [[SMH]]/[[SOXX]]. The thin ETF margin would normally read ETF-replicable — but here it is the opposite, because of how the ETF is built. SMH and SOXX are market-cap-weighted, so [[Nvidia|NVDA]], [[Broadcom|AVGO]] and TSM dominate them; the ETF therefore tracks the AI-compute pole and lands on the far side of the dendrogram from these names. An investor who buys SMH to get analog/auto-industrial exposure gets mostly AI mega-caps instead. The analog names are inside the index but are not what the index does — and no pure analog-semi ETF exists. That is the distinctness: a separable factor that no liquid ETF expresses, the [[Life science tools|life-science-tools]] situation intensified by the ETF being actively dominated by a different pole.

### Historical tightness evolution — durable, off a peak

![[analog-semis-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Durably tight — 0.72 to 0.85 across the whole period — peaking in 2022-23 (the shortage-then-destock, when every analog name moved on the same inventory signal) and easing in 2026 as the cycle bottoms unevenly. A real factor varying in strength with the inventory cycle, not in existence.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.798 | 83.2% |
| 2022 | 0.837 | 86.5% |
| 2023 | 0.850 | 87.6% |
| 2024 | 0.748 | 79.3% |
| 2025 | 0.843 | 87.0% |
| 2026 | 0.720 | 76.9% |

*Durable, not regime-dependent in existence. The holdout WEAKENED reading (0.81) reflects the older 2024-25 half being exceptionally tight (intra 0.90, PC1 92% — the depth of the auto/industrial destock, when the names sold off as one) rather than the factor breaking; the recent half is still 0.73 / PC1 78%. The low PC1-loadings correlation between halves (0.08) is an artifact of the near-uniform loading vector — when all six names load ~0.40, the loadings correlation measures noise, not structure — and should not be read as instability the way it would be for a collapsed-intra cohort like [[Rare earth equity beta|rare earths]]. Latest 90-day: intra 0.753, PC1 79.5%.*

## Related

- [[Semiconductors]] — the sector hub; this is the analog/auto-industrial cohort within it
- [[Texas Instruments]], [[Analog Devices]], [[Microchip Technology]], [[onsemi]], [[NXP]], [[STMicro]] — the cohort members
- [[SMH]], [[SOXX]] — the broad semi ETFs that hold but do not track these names
- [[Nvidia]], [[Broadcom]] — the AI-compute pole the cohort is distinct from (+0.446)
- [[Drug distributors]], [[Tankers]], [[Trucking and LTL]], [[Life science tools]] — comparable Tier-1 distinct factors (life-science tools is the closest: a no-pure-ETF supply-chain factor)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/analog_semis.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
