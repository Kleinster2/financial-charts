---
aliases: [Neoclouds, Neocloud, GPU clouds, AI neoclouds, Neocloud cohort]
tags: [concept, ai-infrastructure, datacenter, cloud, cluster-validation]
---

# Neoclouds

The listed AI-GPU-cloud and datacenter buildout names — pure GPU clouds ([[CoreWeave]] CRWV, [[Nebius]] NBIS) that rent NVIDIA compute outside the hyperscalers, plus the bitcoin-miner-to-AI-datacenter converters ([[IREN]], [[Cipher Mining]] CIFR, [[Applied Digital]] APLD) repurposing power and shells into AI hosting. The category sits between the [[Sectors/Crypto-to-AI|Crypto-to-AI]] miners and the [[AI hyperscalers|hyperscalers]] — and, as the validation shows, trades with the former, not as a separate factor.

> [!warning] Cluster status: real cohort, but not distinct from Crypto-to-AI (June 2026)
> The five neocloud names form a real, coherent, near-single-factor cohort — intra-corr 0.624, PC1 69.9%, rejecting the independence, random-basket and vol-matched nulls at the 0.0001–0.0002 floor (the cohesion is real even against same-vol baskets, despite extreme 92–110% annualized volatility). But they are not a *distinct* factor: at every threshold from 0.35 up the cohort merges with the [[Sectors/Crypto-to-AI|Crypto-to-AI]] miners (CORZ/HUT/WULF/MARA/CLSK/RIOT) plus IBIT, and the intra-advantage vs that cohort is exactly +0.000 — the neoclouds correlate as much with the miners as with themselves. The "neocloud" label does not separate from the validated Crypto-to-AI factor; both are the same high-beta AI-datacenter-buildout / BTC-beta complex. The internal structure: a pure-GPU-cloud pair ([[CoreWeave]]+[[Nebius]], 0.73) and a miner-convert sleeve ([[IREN]]+[[Cipher Mining]], 0.79) bridged by [[Applied Digital]]. The cohort is distinct from AI-compute/hyperscalers ([[NVIDIA]]/[[Microsoft]], +0.316) — it is not just NVDA beta. See below.

Neoclouds are the equity expression of the AI-datacenter buildout one rung below the hyperscalers: capacity-constrained GPU capacity sold on take-or-pay contracts, financed with high leverage against NVIDIA allocations and power access. That financing/momentum profile — not the underlying business model — is why the pure clouds (CRWV/NBIS) trade with the miner-converts (IREN/CIFR/APLD) and the broader Crypto-to-AI complex: they are all levered bets on the same AI-capacity scarcity, with the highest realized volatility in the vault's cluster set.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.624 [0.497–0.790] | Coherent; weekly 0.585 |
| PC1 explained variance | 69.9% | Near single-factor |
| Random-basket p (10k) | 0.0002 | Real cohesion — beats random 5-picks at the floor |
| Vol-matched p (10k) | 0.0002 | Real beyond shared vol (despite 92–110% annualized) |
| Holdout (2Y split) | INDETERMINATE | Cohort too young — CRWV/NBIS listed 2024–25, no train half |
| Threshold clean width | 0.00 | Miners contaminate from 0.35 — inseparable from Crypto-to-AI |
| Intra-adv vs Crypto-to-AI miners | +0.000 | Not distinct — same factor |
| Intra-adv vs AI-compute ([[NVIDIA]]/[[Microsoft]]) | +0.316 | Distinct from GPU supplier / hyperscaler |
| Intra-adv vs IBIT/[[SPY]] | +0.171 | Partly distinct from BTC / broad market |

1Y daily log returns through 2026-06-12, threshold 0.5. All members US-listed (no async-close issue). Config: `scripts/cluster_configs/neoclouds.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — inseparable from the Crypto-to-AI miners

![[neoclouds-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The five neoclouds and all six [[Sectors/Crypto-to-AI|Crypto-to-AI]] miners (plus IBIT) form one cluster — the neoclouds do not separate from the miners. [[NVIDIA]] and the hyperscaler [[Microsoft]] sit apart, so the cohort is not AI-compute beta. The neocloud category is a sub-set of the AI-datacenter-buildout factor, not a distinct one.*

The threshold scan returns zero width because the Crypto-to-AI miners contaminate the cohort from threshold 0.35 — the lowest cut tested. This is the same "real cohort, inseparable from its parent factor" signature as [[Nuclear renaissance|Nuclear / SMR]] (URA/NLR) and [[Brazil fintech]] (the banks): the neoclouds are a high-beta sleeve of the validated [[Sectors/Crypto-to-AI|Crypto-to-AI]] cohort, which already carries this factor.

### Topology — a pure-cloud pair and a miner-convert sleeve

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | IREN + CIFR | 0.210 | Miner-convert pair (bitcoin → AI datacenter) |
| 2 | CRWV + NBIS | 0.272 | Pure-GPU-cloud pair (CoreWeave / Nebius) |
| 3 | APLD + (IREN+CIFR) | 0.332 | Applied Digital joins the converters |
| 4 | (CRWV+NBIS) + (APLD+IREN+CIFR) | 0.437 | The two sleeves merge |

The cohort is two sleeves: the pure GPU clouds ([[CoreWeave]]+[[Nebius]]) and the miner-converts ([[IREN]]+[[Cipher Mining]], with [[Applied Digital]] attaching). They merge at 0.437 — one factor, two business origins. The pure-cloud pair is the only "true neocloud" sleeve that is not literally a Crypto-to-AI miner; the converters *are* Crypto-to-AI.

### PC1 index weights

![[neoclouds-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains 69.9% with near-identical loadings (0.43–0.46) — a clean single factor. Note the realized volatilities: 92–110% annualized across the board, the highest-beta cohort in the vault's cluster set.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| CRWV | 0.429 | 19.2% | 91.9% | 21.1% |
| NBIS | 0.441 | 19.7% | 94.9% | 21.0% |
| IREN | 0.463 | 20.7% | 105.4% | 19.9% |
| CIFR | 0.448 | 20.0% | 109.8% | 18.5% |
| APLD | 0.454 | 20.3% | 105.6% | 19.5% |

Loadings and vols are so uniform that the PC1-mimic basket is nearly equal-weighted — there is no calm anchor to lean on. The whole cohort is a single, extreme-volatility AI-capacity-scarcity bet.

### Distinctness

![[neoclouds-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The neocloud block is warm — but it is not cooler against the Crypto-to-AI miners (cohort-vs-miners 0.623 ≈ internal 0.624), the zero intra-advantage made visible. It is clearly cooler against [[NVIDIA]]/[[Microsoft]].*

### Historical tightness evolution

![[neoclouds-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion. Short history — the cohort only exists since the 2024–25 listings ([[CoreWeave]] IPO'd 2025, [[Nebius]] relisted Oct 2024) — but tightening fast: 0.562 in 2025 to 0.696 in 2026 as the AI-datacenter trade consolidated into one momentum factor.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2025 | 0.562 | 65.1% | 0.483 |
| 2026 | 0.696 | 75.7% | 0.359 |
| Latest 90d | 0.674 | 73.9% | 0.395 |

*Newly formed and tightening: the neocloud factor consolidated through 2025–26 as the names listed and the AI-capacity-scarcity trade matured. Too young for a holdout (no 2-year train half), so durability is unproven — but the trajectory is consolidation, not fragmentation.*

### The read-through

- Neoclouds are not a separate trade from Crypto-to-AI. The cohort is +0.000 from the [[Sectors/Crypto-to-AI|Crypto-to-AI]] miners and inseparable at every threshold — both are the high-beta AI-datacenter-buildout / capacity-scarcity factor. A "neocloud basket" is a sleeve of that factor, not a distinct one.
- The pure-cloud pair is the only non-miner expression. [[CoreWeave]]+[[Nebius]] is the way to own the neocloud factor without the bitcoin-mining leg; [[IREN]]/[[Cipher Mining]]/[[Applied Digital]] are Crypto-to-AI converters that carry BTC beta.
- Highest-beta cohort in the set. At 92–110% annualized vol, position sizing dominates — this is the most volatile factor the framework has measured, more than the space pure-plays or SMR developers.
- It is not NVDA beta. The +0.316 intra-advantage vs [[NVIDIA]]/[[Microsoft]] confirms the neoclouds trade on their own capacity/financing factor, not simply as levered AI-compute demand.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-14); holdout will become computable as history accrues.

## Related

- [[Sectors/Crypto-to-AI]] — the validated cohort the neoclouds are not distinct from (the converters belong to it)
- [[CoreWeave]], [[Nebius]] — pure GPU clouds; [[IREN]], [[Cipher Mining]], [[Applied Digital]] — miner-converts
- [[AI hyperscalers]] — the tier above (the neoclouds' customers and competitors)
- [[NVIDIA]] — GPU supplier and backer
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
