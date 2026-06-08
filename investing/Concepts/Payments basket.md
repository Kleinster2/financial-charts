---
aliases: [Payments cluster, US payments, Payments stocks]
tags: [concept/cluster, payments, fintech, financials]
---

# Payments basket

> [!failure] Cluster status: falsified as single basket — splits into 4+ sub-factors (May 2026)
> Intra-cluster correlation only 0.40 across V/MA/AXP/PYPL/FIS/FISV/COF/SHOP. PC1 only 48.4%. Hierarchical clustering at 0.4 reveals 4 distinct groups: card networks (V+MA tight pair, correlation 0.87 — the cleanest pair in the entire validation pass); consumer credit / issuer (AXP+COF cluster with banks); processors (FIS, FISV) singletons; digital commerce (PYPL singleton, SHOP joins broad ETFs). The "payments" framing is a sector taxonomy that does not produce a tradable factor. See "Cluster validation" section below.

The 8-name "payments" cohort — card networks (V, MA), card-issuer-network hybrid (AXP), consumer credit (COF), payment processors (FIS, FISV), and digital wallets / commerce platforms (PYPL, SHOP) — does not cluster as one factor. It splits into 4+ sub-factors corresponding to distinct business models.

---

## Constituents and algorithmic clustering

| Sub-cluster | Members | Cluster correlation | Note |
|---|---|---|---|
| Card networks duopoly | V, MA | 0.87 | Cleanest pair in the entire validation pass; same business model (interchange-based two-sided network) |
| Consumer credit / issuer | AXP + COF | (cluster with banks JPM/BAC/WFC at 0.4) | AXP is network+issuer hybrid; COF is bank-issuer; both trade on credit-cycle factor |
| Payment processors | FIS, FISV | Each a singleton | Bank-back-end services; trade on bank IT spending cycle, not network growth |
| Digital wallets / commerce | PYPL (singleton), SHOP (joins broad ETFs) | Idiosyncratic | PYPL on its multi-year reset; SHOP on commerce-growth + general SaaS factor |

The "payments sector" frame groups them by what they do (move money) but the equity returns reflect what they ARE economically.

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/payments.yaml`. Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation (8-name) | 0.40 (range 0.17-0.87) | Far below 0.50 floor; bimodal range |
| V-MA pair | 0.87 | Tightest pair anywhere in the validation pass |
| Tightest cross-business-model pair | AXP-COF = 0.79 | Consumer credit factor (bank-like) |
| PC1 explained variance | 48.4% | Just below the 50% multi-factor floor |
| Hierarchical clustering at 0.4 | V+MA pair; AXP+COF cluster with banks; FIS/FISV/PYPL singletons; SHOP joins broad ETFs | 4 distinct groups |
| Cluster vs banks | 0.35 (+0.05) | Some payments names ARE in the bank factor (AXP, COF) |
| Cluster vs broad ETFs | 0.43 (-0.02 NEGATIVE) | Payments names trade with broad market more than each other |

### Pairwise correlations (1Y)

|  | V | MA | AXP | PYPL | FIS | FISV | COF | SHOP |
|---|---|---|---|---|---|---|---|---|
| V | — | 0.87 | 0.46 | 0.31 | 0.43 | 0.24 | 0.40 | 0.29 |
| MA | 0.87 | — | 0.51 | 0.27 | 0.48 | 0.29 | 0.50 | 0.33 |
| AXP | 0.46 | 0.51 | — | 0.28 | 0.47 | 0.21 | 0.79 | 0.46 |
| PYPL | 0.31 | 0.27 | 0.28 | — | 0.57 | 0.31 | 0.27 | 0.47 |
| FIS | 0.43 | 0.48 | 0.47 | 0.57 | — | 0.45 | 0.40 | 0.41 |
| FISV | 0.24 | 0.29 | 0.21 | 0.31 | 0.45 | — | 0.20 | 0.17 |
| COF | 0.40 | 0.50 | 0.79 | 0.27 | 0.40 | 0.20 | — | 0.42 |
| SHOP | 0.29 | 0.33 | 0.46 | 0.47 | 0.41 | 0.17 | 0.42 | — |

Two correlation peaks dominate the matrix:
- V-MA = 0.87 (network duopoly)
- AXP-COF = 0.79 (consumer credit factor)

Everything else is 0.20-0.50 noise.

---

## What each sub-factor actually trades on

| Sub-factor | Names | Dominant driver |
|---|---|---|
| Card networks | V, MA | Global card spend volume; cross-border travel; interchange fee regulation |
| Consumer credit / issuer | AXP, COF | Credit losses; consumer health; net charge-off rates; FICO migration |
| Bank-back-end processors | FIS, FISV | Bank IT spending cycles; long sales cycles; integration revenue |
| Digital wallets | PYPL | Cross-border + Venmo + Braintree mix; 2024-26 reset story |
| Commerce platforms | SHOP | Merchant GMV growth; Shop Pay adoption; broader SaaS factor |

These are five distinct businesses — the only thing they share is "money moves through them." Equity returns reflect the underlying economics, not the surface taxonomy.

---

## The card networks duopoly — see dedicated note

V-MA pairwise correlation of 0.87 is the tightest pair in the entire validation pass. Now formalized as its own sub-cluster note: see [[Card networks duopoly]] for full validation, structural analysis, and trade implications. The duopoly trades as essentially one stock with ~6% idiosyncratic spread (PC1 explains 93.7% of variance).

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long card networks | V + MA (equal-weighted, intra 0.87) | Global card spend volume + interchange |
| Long consumer credit | AXP + COF (intra 0.79) | Consumer health + credit cycle |
| Long bank IT spending | FIS + FISV (intra 0.45 — looser) | Bank technology spending cycles |
| Long PYPL | Solo | PYPL idiosyncratic reset story |
| Long SHOP | Solo | Commerce platform + general SaaS |
| AVOID: long "payments basket" (8-name) | Dilutes 4-5 unrelated factors | No clean exposure |
| Pair: long V-MA / short AXP-COF | Captures network vs credit-cycle factor differential | Cross-payment-business-model |

---

## Cluster validation compliance addendum (2026-06-07)

Generated from `scripts/cluster_configs/payments.yaml` using `scripts/cluster_analysis.py` methodology. The 1Y diagnostic window is 2025-05-01 to 2026-04-30 (171 observations); the rolling history starts at `2020-01-01` where data are available.

### Required validation plots

![[payments-cluster-correlation-1y.png]]

*One-year correlation heatmap for the `Payments` validation universe.*

![[payments-cluster-dendrogram-1y.png]]

*Hierarchical clustering tree using average linkage on distance `1-|corr|`.*

![[payments-cluster-pca-1y.png]]

*PCA diagnostic for the candidate cohort; PC1 explains 47.9% of standardized daily-return variance.*

### PC1 index weights vs cluster topology

The topology table answers which names join the tree first or last. The raw PC1-mimic table answers which raw-return weights best replicate the standardized common factor after realized-volatility scaling. These are deliberately different readings of the same cluster.

| Step | Left | Right | Distance (1-\|corr\|) | Read |
|---|---|---|---|---|
| 1 | V | MA | 0.134 | Tightest merge |
| 2 | AXP | COF | 0.212 | Candidate cohort merge step |
| 3 | PYPL | FIS | 0.435 | Candidate cohort merge step |
| 4 | V+MA | AXP+COF | 0.553 | Candidate cohort merge step |
| 5 | SHOP | PYPL+FIS | 0.562 | Candidate cohort merge step |
| 6 | V+MA+AXP+COF | SHOP+PYPL+FIS | 0.637 | Candidate cohort merge step |
| 7 | FISV | V+MA+AXP+COF+SHOP+PYPL+FIS | 0.735 | Final cohort join / loosest boundary |

| Ticker | PC1 loading | Normalized loading weight | Ann. vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| V | 0.379 | 13.53% | 23.22% | 18.73% |
| MA | 0.396 | 14.15% | 22.99% | 19.78% |
| AXP | 0.392 | 14.01% | 28.79% | 15.64% |
| PYPL | 0.308 | 11.02% | 44.21% | 8.01% |
| FIS | 0.387 | 13.83% | 30.19% | 14.72% |
| FISV | 0.241 | 8.60% | 79.94% | 3.46% |
| COF | 0.374 | 13.38% | 34.06% | 12.63% |
| SHOP | 0.321 | 11.48% | 52.50% | 7.03% |

Interpretation: use the dendrogram / join-distance topology to identify the tight core and later-joining members; use the Raw PC1-mimic weight column only for investable factor-replication sizing.

### Historical tightness evolution

![[payments-cluster-rolling-tightness-90d.png]]

*Ninety-day rolling tightness diagnostic: avg intra-correlation, PC1 share, core correlation, satellite-to-core correlation, and final candidate join distance.*

| Year | Avg corr median | PC1 median | Core corr median | Satellite-to-core median | Final join distance median |
|---|---|---|---|---|---|
| 2020 | 0.691 | 74.7% | 0.664 | 0.770 | 0.573 |
| 2021 | 0.377 | 51.2% | 0.329 | 0.521 | 0.877 |
| 2022 | 0.598 | 65.5% | 0.577 | 0.656 | 0.516 |
| 2023 | 0.462 | 53.8% | 0.435 | 0.571 | 0.626 |
| 2024 | 0.418 | 49.6% | 0.426 | 0.396 | 0.659 |
| 2025 | 0.562 | 63.4% | 0.543 | 0.619 | 0.591 |
| 2026 | 0.418 | 50.4% | 0.404 | 0.451 | 0.679 |

Latest 90D through 2026-04-30: avg corr 0.455, PC1 52.7%, core corr 0.458, satellite-to-core corr 0.446, final join distance 0.628.

Historical verdict: regime-dependent / fragmenting cluster; current rolling cohesion is below durable-cluster thresholds.

---

## Related

### Member actors

- [[Visa]] — card network duopoly
- [[Mastercard]] — card network duopoly
- [[American Express]] — network + issuer hybrid (clusters with banks via consumer credit factor)
- [[Capital One]] — consumer credit issuer (clusters with AXP + banks)
- [[PayPal]] — digital wallet (singleton; multi-year reset)
- [[FIS]] — payment processor (singleton)
- [[Fiserv]] — payment processor (singleton)
- [[Shopify]] — commerce platform (clusters with broad ETFs)

### Adjacent concept notes

- [[Payment waterfall]] — payments-stack technology framework
- [[Mega banks basket]] — AXP and COF cluster with mega banks at 0.4
- [[Banking primer]] — sector hub adjacent to consumer credit

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/payments.yaml` — config for this test

*Created 2026-05-03 — falsified-cluster note documenting the payments sector's 4+ sub-factor structure*
