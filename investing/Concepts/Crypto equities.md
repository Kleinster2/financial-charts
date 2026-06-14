---
aliases: [Crypto equities, Crypto financials, Listed crypto proxies, Crypto-equity complex]
tags: [concept, crypto, bitcoin, fintech, cluster-validation]
---

# Crypto equities

The listed crypto-financial proxies — the stocks investors buy for crypto exposure without holding the coins: [[Coinbase]] (COIN, the exchange), [[MicroStrategy|Strategy]] (MSTR, a levered bitcoin-treasury company), [[Robinhood]] (HOOD, the retail broker), and [[Circle]] (CRCL, the USDC stablecoin issuer). Distinct from the bitcoin miners (which sit in the validated [[Sectors/Crypto-to-AI]] cohort). The validation shows a real, cohesive cohort — that trades as bitcoin beta.

> [!warning] Cluster status: real cohort, but it IS bitcoin beta (June 2026)
> The four crypto-financial proxies form a genuine, single-factor cohort — intra-corr 0.680 (weekly 0.690), PC1 76.2%, rejecting the independence, random-basket and vol-matched nulls (p 0.0001 / 0.0003 / 0.0001), with all four joining a clean tree ([[Coinbase]]+[[Robinhood]] at 0.20 → [[MicroStrategy|Strategy]] 0.28 → [[Circle]] 0.39). But it is not a *distinct* factor: the intra-advantage vs spot bitcoin (IBIT) is −0.032 — the cohort correlates more with IBIT (0.712) than with itself (0.680) — and the threshold scan is boundary-dependent because IBIT contaminates the cohort from threshold 0.30. It clusters with IBIT/QQQ/SPY. It IS distinct from broad financials (+0.326 vs XLF) — even [[Coinbase]] and [[Robinhood]], which are financial companies, trade as bitcoin proxies rather than as brokers. Holdout INDETERMINATE ([[Circle]] only IPO'd June 2025, no 2-year train half), but the cohort tightened 0.58 (2025) → 0.72 (2026). The crypto analogue of copper: a real cohort replicable by the underlying — here IBIT (bitcoin), with leverage. See below.

The defining feature is what the cohort is NOT distinct from. These are nominally a fintech / financials group — an exchange, a broker, a software company, a payments/stablecoin issuer — yet the tape prices them as one bitcoin-beta object (+0.326 distinct from XLF, −0.032 from IBIT). The business taxonomy says financials; the market says bitcoin. [[Circle]] is the sharpest case: a stablecoin issuer earns interest on its USDC reserves, so it is structurally rate-exposed, not bitcoin-price-levered — and it still joins the crypto cluster at 0.385. The market prices the whole crypto-adjacent equity complex as bitcoin beta regardless of each name's actual economic driver.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.680 [0.551–0.799] | Cohesive; weekly 0.690 (all US-listed) |
| PC1 explained variance | 76.2% | Single-factor cohort |
| Independence null p | 0.0001 | Series co-move |
| Random-basket null p | 0.0003 | Beats a random 4-pick — real cohesion |
| Vol-matched null p | 0.0001 | Real beyond shared (crypto-level) vol |
| Holdout (2Y split) | INDETERMINATE | Circle IPO'd Jun 2025 — no 2-year train half |
| Threshold clean width | 0.00 | IBIT contaminates from 0.30 — not separable from BTC |
| Intra-adv vs spot BTC (IBIT) | −0.032 | Negative — it IS bitcoin beta |
| Intra-adv vs financials (XLF) | +0.326 | Distinct — not a financials trade |
| Intra-adv vs growth/market (QQQ/SPY) | +0.147 | Weakly distinct from high-beta growth |

1Y daily log returns through 2026-06-12, threshold 0.5. All US-listed (synchronous). [[Circle]] IPO'd 2025-06-05, so it covers the 1Y window but limits the holdout. Config: `scripts/cluster_configs/crypto_equities.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — cohesive, but inseparable from bitcoin

![[cryptoeq-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The four crypto-financial names form one cluster — but it merges with spot bitcoin (IBIT) and the growth/market ETFs (QQQ/SPY). Broad financials (XLF) sit apart. The cohort is real and single-factor, but it is bitcoin beta, not a standalone crypto-equity factor.*

The threshold scan returns zero clean width because IBIT joins the cohort's cluster from threshold 0.30 — a tight cut — and QQQ/SPY from 0.50. The crypto-equities cannot be separated from spot bitcoin: they are levered, equity-wrapped BTC exposure. This is the [[Brazil fintech]] / copper / [[Datacenter power and cooling|DC power]] signature — a real cohort that is replicable by its parent benchmark — with IBIT (bitcoin) as the parent here, and the [[Sectors/Crypto-to-AI|Crypto-to-AI]] miners as the other listed expression of the same BTC factor.

### Topology — Coinbase the hub, Circle the looser leg

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | COIN + HOOD | 0.201 | Exchange + broker — the tightest pair (0.80) |
| 2 | MSTR + (COIN+HOOD) | 0.281 | The levered-BTC treasury joins |
| 3 | CRCL + rest | 0.385 | Stablecoin issuer joins last (rate-exposed, the loosest) |

[[Coinbase]] is the central node (highest pairwise correlations, pairs tightest with [[Robinhood]] at 0.80). [[Circle]] is the loosest member (joins at 0.385, lowest pairwise 0.55–0.73) — consistent with its rate-exposed stablecoin economics being a step removed from bitcoin price — but it still sits inside the cohort, which is the point: the market trades it as crypto beta anyway.

### PC1 index weights

![[cryptoeq-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains 76.2% with fairly even loadings (0.46–0.54) — a single factor with [[Coinbase]] slightly dominant.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| Coinbase (COIN) | 0.544 | 27.2% | 70.4% | 29.8% |
| Strategy (MSTR) | 0.491 | 24.6% | 73.9% | 25.6% |
| Robinhood (HOOD) | 0.499 | 25.0% | 69.8% | 27.6% |
| Circle (CRCL) | 0.463 | 23.2% | 104.5% | 17.1% |

[[Circle]] takes the smallest raw PC1-mimic weight despite being the highest-vol name (104%) — its idiosyncratic stablecoin/rate dynamics dilute its loading. The other three (70–74% vol) are the cleaner bitcoin-beta core.

### Distinctness

![[cryptoeq-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The cohort block is warm — and just as warm against IBIT (the −0.032 intra-advantage made visible). It is distinctly cooler against XLF: these are not trading as financials.*

The cohort is overwhelmingly distinct from broad financials (+0.326 vs XLF) and weakly from growth/market (+0.147 vs QQQ/SPY), but not from bitcoin (−0.032 vs IBIT). The investable read: this is equity-wrapped bitcoin exposure, replicable by IBIT (with the leverage [[MicroStrategy|Strategy]] adds), not a separate financials or fintech factor.

### Historical tightness evolution

![[cryptoeq-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion. Short history (capped by [[Circle]]'s 2025 IPO) but tightening: 0.58 in 2025 to 0.72 in 2026 as the crypto-equity complex consolidated alongside bitcoin's institutionalization.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2025 | 0.578 | 68.5% | 0.473 |
| 2026 | 0.715 | 78.9% | 0.350 |
| Latest 90d | 0.707 | 78.3% | 0.382 |

*Newly formed and tightening: the cohort has consolidated as bitcoin became an institutional asset (spot ETFs, treasury-company proliferation). Durability is untested out of sample (Circle too young), but the trajectory is consolidation toward a single bitcoin-beta factor.*

### The read-through

- It is equity-wrapped bitcoin. The four names are a real cohort (intra 0.680, all nulls passed) that trades as bitcoin beta (−0.032 vs IBIT, IBIT inside the cluster from 0.30) — own IBIT (with leverage via [[MicroStrategy|Strategy]]) to replicate; there is no separate crypto-equity factor to capture.
- The market ignores the business model. These are an exchange, a broker, a treasury company and a stablecoin issuer — +0.326 distinct from financials but −0.032 from bitcoin. Even the rate-exposed stablecoin name ([[Circle]]) trades as crypto beta. Business taxonomy ≠ factor.
- It is the financial sibling of the Crypto-to-AI miners. Both the crypto-equity proxies and the [[Sectors/Crypto-to-AI|Crypto-to-AI]] miners are listed expressions of the same bitcoin factor — different operating models, one underlying.
- Highest-beta inside is Circle, but it is the loosest. CRCL (104% vol) is the most volatile and the least central — the stablecoin model is a step removed from BTC price, so it is the name most likely to decouple if the factor weakens.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-14).

## Related

- [[Sectors/Crypto-to-AI]] — the bitcoin miners: the other listed expression of the same BTC factor
- [[Coinbase]], [[MicroStrategy]], [[Robinhood]], [[Circle]] — the cohort members
- [[Fintech]] — the sector taxonomy the cohort defies (distinct from XLF)
- [[CLARITY Act]] — crypto-regulation context
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
