---
aliases: [Regulated utilities, Regulated utilities basket, Regulated electric utilities, Utility equity factor]
tags: [concept/cluster, utilities, electric, defensive, cluster-validation]
---

# Regulated utilities

Whether the listed regulated electric utilities are a real factor or a bond-proxy duration basket. The candidate is six large US regulated electrics: [[Duke Energy]] (DUK), [[Southern Company]] (SO), [[Dominion Energy]] (D), [[American Electric Power]] (AEP), [[NextEra Energy]] (NEE), [[Xcel Energy]] (XEL). The answer is a real factor: they clear the vol-matched null, so the cohesion is regulated-utility-specific and not merely shared low volatility. It is the second defensive cohort after the [[Tobacco majors basket]] to pass that test, and like tobacco it confirms the defensive-factor law — a defensive cohort is a real factor when its members share a business, a duration basket when they share only a financial profile (the failed [[China special valuation]] case). Two findings sharpen it: utilities are barely correlated with long bonds (0.193 with TLT), so the "bond proxy" label is weaker than assumed; and they are distinct from merchant power ([[AI-power IPPs]], 0.129), so "utilities" is not one sleeve. Unlike tobacco, though, the factor is cleanly ETF-replicable — it is XLU.

> [!warning] Cluster status: a real regulated-utility factor (not a duration basket), uncorrelated with the market — but it is XLU (June 2026)
> The six regulated electrics cohere as a real, durable factor: intra-corr 0.602 (weekly 0.691), PC1 67.6%, and they reject the independence, random-basket (p 0.0001) and vol-matched (p 0.0006) nulls — the cohesion exceeds same-volatility baskets, so it is utility-specific, not generic low-vol. They are uncorrelated with the market (cluster vs [[SPY]] -0.046 — a true defensive, like tobacco's -0.002) and the holdout is STABLE (ratio 0.88). Two things they are NOT: a bond proxy (cluster vs TLT only 0.193, +0.409 intra-advantage — they outran bonds +8-29% vs +1% this year), and merchant power (cluster vs the CEG/VST IPPs only 0.129, +0.473). What they ARE is XLU: cluster vs the sector ETF is -0.094 (it correlates more with XLU than with itself), and XLU contaminates the cluster from threshold 0.30. [[NextEra Energy]], the regulated/renewables hybrid, splits off (the loose satellite). See below.

A defensive cohort can be a real sector factor or a duration basket, and the vol-matched null tells them apart — utilities pass it for the same reason tobacco did: the members share a real business, not just a low-vol profile. Regulated electrics share a rate-base growth model, an allowed-ROE and rate-case cycle, and now a common AI-datacenter load-growth tailwind, and that common business dominates their modest rate-sensitivity (only 0.193 correlation to long bonds). The cohesion is genuine, durable, and market-neutral — but it is fully captured by XLU, so the investable expression is the ETF, with single-name selection (Vogtle nuclear at [[Southern Company]], transmission at [[American Electric Power]], renewables growth at [[NextEra Energy]]) the idiosyncratic overlay.

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/regulated_utilities.yaml`, with `cluster_permutation_test.py --null all`, `cluster_threshold_scan.py`, `cluster_holdout_test.py --window 2y`, and a sub-cohort scan (`sub_regulated_core.yaml`). Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-06-13 to 2026-06-12)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.602 (weekly 0.691) | Real cohesion; pure-regulated core (ex-NEE) 0.674 |
| PC1 explained variance | 67.6% | Strong single factor |
| Tightest pair | DUK-SO = 0.853 | The two big Southeast regulated utilities |
| Loosest member | NEE (0.33-0.56 to peers) | The regulated/renewables hybrid, splits off |
| Cluster vs sector ETF (XLU) | 0.696 (-0.094) | Negative advantage — the cohort IS XLU |
| Cluster vs long bonds (TLT) | 0.193 (+0.409) | NOT a bond proxy — modest rate-sensitivity only |
| Cluster vs merchant IPPs (CEG/VST) | 0.129 (+0.473) | Distinct from merchant power |
| Cluster vs market (SPY) | -0.046 (+0.648) | Uncorrelated with the market — true defensive |
| Independence / random-basket / vol-matched nulls | reject (0.0001 / 0.0001 / 0.0006) | A real regulated-utility factor, not a duration basket |
| Threshold scan | boundary-dependent | XLU contaminates from 0.30 |
| 2y holdout | STABLE (ratio 0.88) | Durable across regimes |

![[regulated-utilities-cluster-correlation-1y.png]]
*1Y correlation matrix: a tight DUK/SO/AEP/XEL/D regulated block; NEE the weak column (the hybrid).*

### Hierarchical clustering and join distances

The five pure-regulated names build a tight cluster; the hybrid NEE attaches last, and the sector ETF sits on top of the whole group.

![[regulated-utilities-cluster-dendrogram-1y.png]]

| Step | Left | Right | Distance (1-\|corr\|) | Members |
|---|---|---|---|---|
| 1 | DUK | SO | 0.147 | DUK+SO |
| 2 | XEL | DUK+SO | 0.291 | +Xcel |
| 3 | AEP | (cluster) | 0.334 | +AEP |
| 4 | D | (cluster) | 0.382 | pure-regulated core |
| 5 | NEE | (core) | 0.542 | all six |

Final join distance 0.542 — the pure-regulated core unifies by 0.382, with NEE the late, loose addition. The threshold scan returns no stable width: XLU contaminates from threshold 0.30, so the cohort is never a clean island. BOUNDARY-DEPENDENT. A sub-scan of the pure-regulated core (DUK/SO/D/AEP/XEL, intra 0.674, `sub_regulated_core.yaml`) is also boundary-dependent — even ex-NEE, regulated utilities are XLU.

![[regulated-utilities-cluster-threshold-scan.png]]

### PC1 index weights

PCA is run on standardized daily log returns. Raw PC1-mimic weight scales the PC1 loading by inverse realized volatility — and these are genuinely low-vol names (15-24%), the defensive signature.

| Member | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| DUK | 0.458 | 18.80% | 15.20% | 23.14% |
| SO | 0.446 | 18.32% | 17.00% | 20.16% |
| D | 0.386 | 15.86% | 21.47% | 13.83% |
| AEP | 0.404 | 16.61% | 18.76% | 16.56% |
| NEE | 0.319 | 13.12% | 24.00% | 10.23% |
| XEL | 0.421 | 17.28% | 20.10% | 16.08% |

![[regulated-utilities-cluster-pca-1y.png]]
*DUK/SO carry PC1; NEE is the low-loading outlier (0.319). The 15-24% vols are the lowest of any cohort in the campaign — utilities are the genuine low-vol defensive.*

### Permutation nulls

![[regulated-utilities-cluster-permutation.png]]

The vol-matched null is the decisive duration-basket test, and utilities pass it. Low-volatility names share more baseline correlation than the broad universe (the vol-matched null mean is 0.223, against ~0.15 for the high-vol commodity cohorts), so the bar is higher — yet the cohort's 0.602 clears the 99th percentile (0.439) at p 0.0006. The cohesion is therefore regulated-utility-specific, not an artifact of all six being low-vol bond-proxies. This is what separates utilities (and tobacco) from [[China special valuation]], whose low-vol SOEs failed the same test.

### Historical tightness evolution

![[regulated-utilities-cluster-rolling-tightness-90d.png]]

| Year | Avg corr | PC1 | Final join distance |
|---|---|---|---|
| 2020 | 0.787 | 82.3% | 0.252 |
| 2021 | 0.582 | 65.8% | 0.545 |
| 2022 | 0.726 | 78.2% | 0.456 |
| 2023 | 0.776 | 81.7% | 0.347 |
| 2024 | 0.591 | 66.3% | 0.513 |
| 2025 | 0.673 | 73.1% | 0.440 |
| 2026 | 0.617 | 68.7% | 0.519 |

This is a durable, mid-life factor — neither newly formed nor decaying. Cohesion oscillates in a 0.58-0.79 band (tightest in rate-shock years like 2020 and 2022-23, when a common rate driver dominates; looser in 2021/2024 when idiosyncratic stories — Dominion's strategic review, NextEra's renewables swings — reassert). The holdout reads STABLE (0.88), so the factor holds out of sample; it breathes with the rate cycle but does not erode.

---

## What the verdict means

Utilities are the second proof of the defensive-factor law and a useful debunk. Three reads:
- A real factor, not a duration basket. The vol-matched null rejects (p 0.0006) and the correlation to long bonds is only 0.193 — regulated utilities are not levered bonds, they are a real sector with a rate-base business and an AI-power demand tailwind. The "bond proxy" shorthand is weaker than assumed.
- But it is XLU. The -0.094 advantage versus the sector ETF, and XLU contaminating from threshold 0.30, mean the factor is fully ETF-replicable. Unlike tobacco (no clean ETF expression), the clean trade here is simply XLU.
- Two genuine distinctions worth trading. Regulated utilities are uncorrelated with the market (-0.046 — real defensive ballast) and distinct from merchant power ([[AI-power IPPs]], 0.129 — the rate-base names and the power-price-exposed generators are different factors). And NextEra, the regulated/renewables hybrid, is the one member that decouples, on its renewables-growth premium.

---

## Trade implications

| Trade | Verdict |
|---|---|
| Long XLU | The clean expression of the regulated-utility factor (the cohort IS XLU) |
| Long utilities / short SPY | Real market-neutral defensive ballast (cohort beta to SPY near zero) |
| Long utilities / short TLT | NOT a tight hedge — only 0.193 correlation; utilities are not levered bonds |
| Long regulated (DUK/SO/AEP) / short merchant IPPs (CEG/VST) | Captures the +0.473 rate-base-vs-merchant-power separation — two real factors |
| NEE as a standalone | The regulated/renewables hybrid — a growth overlay, not the regulated factor |
| Pair trades within the core | Idiosyncratic (Vogtle nuclear, transmission capex, service-territory load growth) |

---

## Related

### Member actors
- [[Duke Energy]] — large SE regulated electric, tightest pair with Southern
- [[Southern Company]] — SE regulated (Georgia/Alabama Power), Vogtle nuclear
- [[Dominion Energy]] — regulated electric (Virginia), data-center load growth
- [[American Electric Power]] — largest US transmission network, 11-state regulated
- [[NextEra Energy]] — regulated FPL + largest renewables developer (the hybrid that splits)
- [[Xcel Energy]] — Upper-Midwest/Mountain regulated electric

### Adjacent concept notes
- [[Tobacco majors basket]] — the other defensive that passes the vol-matched null (real business, not duration)
- [[China special valuation]] — the defensive that FAILS it (duration basket, only a financial profile)
- [[AI-power IPPs]] — merchant power generators, the distinct (+0.473) other half of "utilities"
- [[Grid infrastructure super-cycle]] — the AI-datacenter load-growth tailwind
- [[Vault cluster taxonomy]] — the cross-cohort map

### Methodology
- `docs/cluster-validation.md`
