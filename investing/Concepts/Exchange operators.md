---
aliases: [Exchange operators, Listed exchanges, Exchange oligopoly, Exchanges cluster]
tags: [concept, exchanges, financials, market-structure, cluster-validation]
---

# Exchange operators

The listed US exchange oligopoly — [[CME Group]] (CME), [[Intercontinental Exchange]] (ICE), [[Nasdaq]] (NDAQ), [[CBOE]] (CBOE). The hypothesis was a [[Sectors/WFE|WFE]]-type ceiling: four toll-collecting oligopolists with network-effect moats and recurring revenue should form one tight, near-single-factor cluster. The data says otherwise — the cohort has fragmented as two of the four pivoted from transaction venues into recurring-data businesses.

> [!failure] Cluster status: falsified as a single cluster — two decoupled sub-factors (June 2026)
> The four exchanges do not trade as one factor: intra-corr 0.360 (below the 0.50 floor), PC1 only 52.2% with a large PC2 (27.9%), and hierarchical clustering never returns the four as a clean cluster at any threshold (zero stable width). The split is structural — [[Intercontinental Exchange]] and [[Nasdaq]] cluster with the financial-data providers ([[S&P Global]], [[Moody's]], [[MSCI]]), not with the other exchanges, while [[CME Group]] and [[CBOE]] form a separate derivatives/volatility pair. Intra-advantage is +0.030 vs the data providers and −0.006 vs electronic-trading venues — no distinct "exchange" factor. The cohort was tight in the 2020 COVID-volatility spike (0.744) and has fragmented since (0.29–0.40) as ICE and Nasdaq shifted revenue to data/SaaS. The validated structures underneath are a CME/CBOE derivatives pair and a "data toll road" cluster (ICE/NDAQ + [[S&P Global]]/[[Moody's]]/[[MSCI]]). See below.

Unlike the [[Sectors/WFE|WFE quartet]] — four oligopolists serving the same customers on one capex cycle, the framework's tightest cluster at 0.804 — the exchanges share a label and a moat structure but not a return factor. The business models diverged: [[CME Group]] and [[CBOE]] remain transaction/volatility venues (revenue scales with volume, which spikes on rate and vol shocks), while [[Intercontinental Exchange]] (ICE Data Services, mortgage technology) and [[Nasdaq]] (index, anti-financial-crime SaaS, market-data) have shifted enough revenue to recurring subscriptions that the market prices them as data companies.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.360 [0.151–0.607] | Weak — below the 0.50 floor |
| PC1 explained variance | 52.2% (PC2 27.9%) | Multi-factor — the two-pair split |
| Random-basket p (10k) | 0.0195 | Marginal — barely beats a random 4-pick |
| Vol-matched p (10k) | 0.0240 | Marginal |
| Threshold stable width | 0.00 — BOUNDARY-DEPENDENT | Never a clean cluster at any cut |
| Holdout ratio (2Y split) | 1.04 (STABLE at 0.36) | Durably weak, not durably tight |
| Intra-adv vs data providers | +0.030 | Not distinct — ICE/NDAQ are data toll roads |
| Intra-adv vs electronic trading | −0.006 | Not distinct |
| Intra-adv vs IAI / [[XLF]] / [[SPY]] | +0.135 | Only mildly distinct from broad financials |

1Y daily log returns through 2026-06-12, threshold 0.5. Config: `scripts/cluster_configs/exchanges.yaml`; registry row 2026-06-13. Terminology: [[Cohort, cluster, basket]].

### Boundary — the cohort splits across business models

![[exchanges-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The four exchanges never form one cluster. [[Intercontinental Exchange]] and [[Nasdaq]] merge with the data providers ([[S&P Global]]/[[Moody's]]/[[MSCI]]); [[CME Group]] and [[CBOE]] form a separate derivatives/volatility pair; the e-trading venues (MarketAxess/Tradeweb) sit apart. The "exchange" label does not map to a trading factor.*

The threshold scan is zero-width — like [[Mag 7 cluster|Mag 7]] (semis contaminate) and the [[Snowflake securities note|SNOW/DDOG/MDB]] trio, the cohort never isolates. Here the contaminator is the data-provider complex pulling ICE/NDAQ out: the falsification reveals that two of the four belong to a different cluster entirely.

### Topology — two disjoint pairs

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | ICE + NDAQ | 0.393 | Diversified exchange + data pair |
| 2 | CME + CBOE | 0.423 | Derivatives / volatility pair |
| 3 | (ICE+NDAQ) + (CME+CBOE) | 0.756 | The pairs barely connect — far outside any cluster cut |

The two pairs are real but they do not cohere with each other: they merge only at distance 0.756, far beyond the 0.50 threshold. There is no four-name core.

### PC1 index weights

![[exchanges-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains only 52.2% and PC2 is large (27.9%) — the signature of a two-factor cohort, not a single-factor cluster. Loadings are positive but the low PC1 share means a one-factor basket misses most of the co-movement.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| CME | 0.519 | 26.0% | 22.3% | 29.2% |
| ICE | 0.539 | 27.0% | 23.8% | 28.5% |
| NDAQ | 0.473 | 23.7% | 26.0% | 22.8% |
| CBOE | 0.465 | 23.3% | 29.8% | 19.6% |

Because PC1 captures only ~52% of variance, the raw PC1-mimic basket is not an informative single trade here — the topology (two pairs) is the real structure, not the first principal component.

### Distinctness

![[exchanges-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The two warm pairs (CME-CBOE, ICE-NDAQ) are visible, but the cross-pairs are cold — CME-NDAQ 0.22, CBOE-NDAQ 0.15. The block is not uniformly warm the way a real cluster's is.*

### Historical tightness evolution

![[exchanges-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion. The cohort was a genuine cluster in the 2020 COVID-volatility spike (0.744, PC1 81%) — when every exchange rallied on volume — and has fragmented steadily since as ICE and Nasdaq re-rated on recurring data revenue. By 2024 intra-corr fell to 0.29; it sits ~0.40 now.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2020 | 0.744 | 81.0% | 0.338 |
| 2022 | 0.527 | 65.1% | 0.544 |
| 2024 | 0.290 | 47.5% | 0.795 |
| Latest 90d | 0.401 | 55.1% | 0.695 |

*Fragmenting, not durable: the monotonic decline from the 2020 peak is the signature of a cohort decoupling into separate factor paths (the same shape as [[Mag 7 cluster|Mag 7]]). The "STABLE" 2Y holdout only means the cohesion is durably low (0.36 in both halves), not durably tight.*

### The read-through

- Do not trade "exchanges" as one basket. The four-name cohort has no single factor (intra 0.360, PC1 52%, zero threshold width). A long-exchanges sleeve holding all four is at least two positions.
- ICE and Nasdaq are data toll roads. They cluster with [[S&P Global]], [[Moody's]], and [[MSCI]] — the recurring-data / index / ratings complex — not with the transaction exchanges. The real cluster they belong to is the now-validated [[Financial data providers]] cohort (2026-06-14): NDAQ joins it as a full member and ICE on the boundary, and the cohort is +0.554 of intra-advantage from the CME/CBOE derivatives pair.
- CME and CBOE are the derivatives/volatility pair. Transaction-volume-driven, they re-rate on rate and volatility shocks; this is the closest thing to a genuine "exchange" sub-factor in the set.
- The WFE contrast is the lesson. An oligopoly + a moat does not make a cluster — [[Sectors/WFE|WFE]] coheres at 0.804 because the four serve the same customers on one capex cycle; the exchanges fragmented because two of them changed what business they are in.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation is moot for a falsified cohort but the definition date (2026-06-13) is logged.

## Related

- [[Vault cluster taxonomy]] — cross-cohort comparison; this joins [[Mag 7 cluster]] and [[Foundry monopoly consolidation|Foundry monopoly]] as a documented falsification
- [[Sectors/WFE]] — the validated oligopoly ceiling (the contrast: why a moat is not a cluster)
- [[CME Group]], [[Intercontinental Exchange]], [[Nasdaq]], [[CBOE]] — the four members
- [[Financial data providers]] — the validated cohort ICE and Nasdaq actually belong to (closes this falsification's loop); members include [[S&P Global]], [[Moody's]], [[MSCI]]
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-13.*
