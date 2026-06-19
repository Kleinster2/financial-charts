---
aliases: [Automakers, Autos, Auto stocks, US automakers, Automakers cluster, Autos and EV]
tags: [sector, automakers, ev, consumer-discretionary, usa, cluster-validation]
---

# Automakers

> [!failure] Cluster status: falsified — "automakers" is a label spanning four return drivers, not a factor (Jun 2026)
> The US-listed automakers ([[Tesla|TSLA]]/[[General Motors|GM]]/[[Ford|F]]/[[Rivian|RIVN]]/[[Lucid Motors|LCID]]) do NOT trade as one factor — intra-corr 0.325 (weekly 0.246, lower), PC1 only 46%, and a NEGATIVE −0.134 intra-advantage versus the ETFs (the names correlate more with CARZ/QQQ/SPY than with each other). The cohort shatters by dominant driver: [[Tesla|TSLA]] clusters with tech/market ([[NVIDIA|NVDA]]/QQQ/SPY), not the automakers; [[General Motors|GM]]+[[Ford|F]] are the one real pair (legacy cyclical value); [[Rivian|RIVN]] and [[Lucid Motors|LCID]] are idiosyncratic EV-startup singletons. Random-basket null only borderline (intra p 0.032, PC1 p 0.051); decohering monotonically since the 2022 EV bubble (0.63 → 0.34). The driver-divergence law in its purest auto form — and note the cap-weighted auto ETF CARZ is itself a TSLA/market proxy, so even the ETF is not an "auto factor."

The clean driver-divergence case. "Automakers" reads as one industry, but the five US-listed names are paid on four different things: [[Tesla]] on an AI/autonomy/robotaxi narrative (it trades as a Mag-7/tech name), [[General Motors]] and [[Ford]] on the cyclical ICE-truck/credit cycle (legacy value), and [[Rivian]]/[[Lucid Motors]] on cash-burn, production ramps, and funding runway (EV-startup options). There is no shared "auto" return factor binding them; the only real co-movement is the GM/F legacy pair and the broad market/discretionary beta they all carry.

## Cluster validation

The candidate cohort is the five US-listed automakers — [[Tesla|TSLA]], [[General Motors|GM]], [[Ford|F]] (established) and [[Rivian|RIVN]], [[Lucid Motors|LCID]] (EV pure-plays) — tested against a tech/Mag-7 control ([[Apple|AAPL]]/[[Microsoft|MSFT]]/[[NVIDIA|NVDA]] — does TSLA trade here?) and benchmarks (CARZ auto ETF, XLY discretionary, QQQ Nasdaq, SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.325 [0.250–0.575] | below the 0.50 floor; weekly 0.246 (LOWER — no persistent factor) |
| PC1 explained variance | 46.1% | below 50% — multi-factor (PC2 19%, PC3 15%) |
| Independence null p | 0.0001 | series co-move at all (necessary, not sufficient) |
| Random-basket null p | intra 0.032 / PC1 0.051 | BORDERLINE — barely beats a random 5-pick on intra, fails on PC1 |
| Vol-matched null p | 0.027 / 0.043 | marginal — cohesion is mostly shared high-beta |
| Holdout (2Y split) | WEAKENED 0.66 | eroding (train 0.435 → test 0.288) |
| Threshold clean width | 0.00 | never isolates; CARZ/XLY/QQQ/SPY join from 0.40 |
| Intra-adv vs tech (AAPL/MSFT/NVDA) | +0.130 | barely — and TSLA sits IN the tech cluster |
| Intra-adv vs ETFs (CARZ/XLY/QQQ/SPY) | −0.134 | NEGATIVE — the names track the ETFs more than each other |

All US-listed. Config: `scripts/cluster_configs/tsla.yaml`; registry row 2026-06-19.

### Boundary — the cohort shatters into four homes

![[autos-ev-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The cohort does not cluster. [[Tesla|TSLA]] joins the tech/market block ([[NVIDIA|NVDA]], CARZ, XLY, QQQ, SPY) — green; [[General Motors|GM]]+[[Ford|F]] form the one real pair; [[Rivian|RIVN]] and [[Lucid Motors|LCID]] are singletons; [[Apple|AAPL]] and [[Microsoft|MSFT]] sit alone. Five proposed names, four different homes.*

The threshold scan never returns the cohort as a clean cluster (zero width): at every cut the "cluster" that forms around the cohort is really TSLA plus the market ETFs (CARZ/XLY/QQQ/SPY join from 0.40). The candidate join sequence tells the same story — GM+F pair at 0.425 (the only sub-cut join), then RIVN+LCID only at 0.616 (above the cut), TSLA attaching at 0.677, and the whole thing closing at 0.726. This is the grade-2 falsification signature: the names beat random baskets only marginally and via shared market/discretionary beta (negative intra-advantage vs the ETFs), with no auto-specific factor. The one constructive micro-structure is the [[General Motors|GM]]+[[Ford|F]] legacy pair.

### Topology — TSLA is the outlier, GM/F the only pair

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | GM + F | 0.425 | the legacy pair — the only sub-0.5 join |
| 2 | RIVN + LCID | 0.616 | EV startups pair, but ABOVE the cut |
| 3 | TSLA + (RIVN+LCID) | 0.677 | TSLA attaches loosely |
| 4 | (GM+F) + rest | 0.726 | the cohort "closes" far above the cut |

Only [[General Motors]]+[[Ford]] join below the 0.5 threshold (the legacy cyclical pair). Against the full universe, [[Tesla]] does not even attach to the other automakers — it clusters with [[NVIDIA]]/QQQ/SPY. [[Rivian]] and [[Lucid Motors]] are each singletons (their funding/ramp idiosyncrasies dominate). PC1 explains only 46% (vs >70% for a real cluster), with TSLA carrying the lowest loading (0.401) — it is the least part of whatever weak auto factor exists.

### PC1 index weights

![[autos-ev-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains only 46.1% (weekly 41.5%) with a large PC2 (19%) and PC3 (15%) — a multi-factor cohort, not a single-factor cluster. TSLA carries the lowest loading.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| TSLA | 0.401 | 18.0% | 42.6% | 20.1% |
| GM | 0.479 | 21.5% | 35.8% | 28.4% |
| F | 0.478 | 21.4% | 39.5% | 25.8% |
| RIVN | 0.451 | 20.2% | 67.7% | 14.2% |
| LCID | 0.421 | 18.9% | 77.5% | 11.6% |

PC1 explains under half the variance — the defining failure, since a real cluster runs PC1 above 70%. The highest loadings belong to [[General Motors]] and [[Ford]] (the genuine legacy pair); the high-vol EV startups [[Rivian]]/[[Lucid Motors]] take the smallest raw PC1-mimic weights. Whatever weak common factor exists is mostly the GM/F pair plus shared market beta, not an auto-sector factor.

### Distinctness — negative vs the ETFs; TSLA is a tech name

![[autos-ev-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. No uniformly-hot block. The hottest cohort relationships are GM↔F and the TSLA↔QQQ/NVDA market link; RIVN/LCID are cool against everything except weakly each other.*

The decisive number is the −0.134 intra-advantage versus the ETFs: the cohort correlates with CARZ/XLY/QQQ/SPY more than with itself, so there is no auto-specific factor beyond shared market/discretionary beta. And the cap-weighted auto ETF CARZ is itself dominated by Tesla, so it tracks TSLA/market rather than an "auto" factor — there is no clean ETF expression of "automakers" either. TSLA's real cohort is tech/Mag-7 ([[Mag 7 cluster]]): it trades on autonomy/AI optionality, not the auto cycle.

### Historical tightness evolution

![[autos-ev-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2022–2026. Monotonic decoherence — tight (0.63) in the 2022 EV-bubble/rate-shock, fragmenting every year since to 0.34.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2022 | 0.634 | 70.8% |
| 2023 | 0.459 | 57.0% |
| 2024 | 0.411 | 53.3% |
| 2025 | 0.377 | 50.5% |
| 2026 | 0.342 | 47.6% |

Latest 90-day reading: intra 0.388, PC1 51.2%. The history is the finding: autos were a real factor only during the 2022 EV-bubble and rate-shock, when every name moved on the same "EV growth + duration" trade (0.63). As the bubble unwound, the names re-separated onto their own drivers — TSLA to AI/autonomy, GM/F to the truck/credit cycle, RIVN/LCID to survival economics — and cohesion has fallen every single year since. A sector that was a factor under a common shock and is not one in normal times (the [[Restaurants]] / [[Streaming and CTV|streaming]] shape).

## Related

- [[Mag 7 cluster]] — TSLA's actual factor home (it trades as a tech/Mag-7 name, not an automaker)
- [[Tesla]], [[General Motors]], [[Ford]] — the established automakers (GM/F the one real pair)
- [[Rivian]], [[Lucid Motors]] — the EV pure-plays (idiosyncratic singletons)
- [[US auto affordability]] — the demand-side concept for the legacy auto cycle
- [[GLP-1 receptor agonists]], [[Ad-tech]] — the driver-divergence law's other purest cases (a label spanning divergent dominant drivers)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-19. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/tsla.yaml`; registry row 2026-06-19. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
