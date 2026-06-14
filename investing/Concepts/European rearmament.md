---
aliases: [European rearmament cohort, European defense cohort, EU rearmament, European defense primes]
tags: [concept, defense, europe, rearmament, cluster-validation]
---

# European rearmament

The European leg of the [[Long global rearmament]] thesis: the listed European defense pure-plays re-rating on the post-Ukraine spending surge, the NATO 5%-of-GDP burden-shift, and Germany's Zeitenwende fiscal turn. This note owns the cohort's cluster validation — the question of whether these names trade as one "European rearmament" factor distinct from the US [[Defense primes basket|hardware primes]]. The thesis and demand drivers live in [[Long global rearmament]]; the durable structural diagnostic lives here.

> [!success] Cluster status: validated — a distinct European factor (June 2026)
> The seven listed European defense names ([[Rheinmetall]], [[BAE Systems]], [[Leonardo]], [[Saab]], [[Thales]], [[Hensoldt]], [[Kongsberg]]) form a real single factor: intra-corr 0.651 (0.717 on weekly returns, correcting for non-synchronous trading), PC1 71.5%, rejecting the independence, random-basket and vol-matched nulls at the 0.0001 floor. It is distinct on every axis — from the US hardware primes ([[Defense primes basket|LMT/RTX/NOC/GD/LHX]], intra-advantage +0.340), from broad European equity ([[VGK]], +0.424), and from the broad market (+0.385). [[Kongsberg]] is the one outlier (joins only at distance 0.592, lowest PC1 loading) on its maritime/offshore leg; the clean tradeable cohort is the six-name core. Holdout STABLE (1.03). See below.

European rearmament is its own factor — not US-defense beta, not general European-equity beta. That is the investable point: the rearmament trade has a European sleeve that a US-primes position or a Europe ETF does not capture.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.651 [0.368–0.782] | Single factor; weekly 0.717 (async-close corrected) |
| PC1 explained variance | 71.5% (PC2 10.9%) | Single-factor; weekly 77.8% |
| Random-basket p (10k) | 0.0001 | Beats random 7-picks (null mean 0.149) |
| Vol-matched p (10k) | 0.0001 | Real factor, not shared vol |
| Holdout ratio (2Y split) | 1.03 — STABLE | Train 0.629 / test 0.649; loadings corr 0.79 (durable structure) |
| Threshold clean band | [0.60, 0.65], width 0.05 | FRAGILE for the 7-name set — [[Kongsberg]] forces a loose cut; the 6-core joins ≤ 0.273 |
| Intra-adv vs US primes | +0.340 | Distinct from the [[Defense primes basket]] |
| Intra-adv vs [[VGK]] (Europe) | +0.424 | Not just European-equity beta |
| Intra-adv vs [[SPY]]/[[ITA]] | +0.385 | Strongly market-distinct |

1Y daily log returns through 2026-06-12, threshold 0.5. Cross-region cohort (Frankfurt/London/Milan/Stockholm/Paris/Oslo listings) — the weekly cross-check (0.717 vs daily 0.651) is the better co-movement estimate. Config: `scripts/cluster_configs/euro_rearmament.yaml`; registry row 2026-06-13. Terminology: [[Cohort, cluster, basket]].

### Boundary — distinct from the US primes; Kongsberg the outlier

![[euro-rearmament-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Six European names ([[Rheinmetall]], [[BAE Systems]], [[Leonardo]], [[Saab]], [[Thales]], [[Hensoldt]]) form their own cluster; the US primes (LMT/RTX/NOC/GD/LHX + ITA) form a separate one, and the equity ETFs (VGK/SPY) a third. [[Kongsberg]] sits apart. The European defense factor is structurally distinct from the US one — not the same trade in two regions.*

### Topology — a tight six-name core plus an outlier

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | BA.L + LDO.MI | 0.218 | Diversified-prime pair (BAE / Leonardo) |
| 2 | RHM.DE + HAG.DE | 0.226 | German air-defense pair (Rheinmetall / Hensoldt) |
| 3 | (BA.L+LDO.MI) + (RHM.DE+HAG.DE) | 0.242 | The two pairs merge |
| 4 | + SAAB-B.ST | 0.251 | Saab joins the core |
| 5 | + HO.PA | 0.273 | Thales joins — six-name core complete |
| 6 | + KOG.OL | 0.592 | [[Kongsberg]] joins far out — the outlier |

The six-name core ([[Rheinmetall]], [[BAE Systems]], [[Leonardo]], [[Saab]], [[Thales]], [[Hensoldt]]) is extremely tight — every member joins below 0.273. [[Kongsberg]] joins only at 0.592, the European mirror of the [[Defense primes basket|LDOS exclusion]] from the US primes: a genuine rearmament beneficiary whose maritime/offshore leg gives it a partly separate factor. The clean tradeable cohort is the six.

### PC1 index weights

![[euro-rearmament-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains 71.5% with near-identical loadings (0.39–0.41) across the six core names; [[Kongsberg]] is the low loading (0.244), confirming its outlier status.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| RHM.DE | 0.397 | 15.2% | 47.1% | 13.1% |
| BA.L | 0.395 | 15.1% | 31.7% | 19.3% |
| LDO.MI | 0.406 | 15.5% | 39.5% | 15.9% |
| SAAB-B.ST | 0.395 | 15.1% | 41.9% | 14.6% |
| HO.PA | 0.388 | 14.8% | 31.8% | 18.9% |
| HAG.DE | 0.394 | 15.0% | 54.7% | 11.1% |
| KOG.OL | 0.244 | 9.3% | 53.1% | 7.1% |

The loadings are near-equal across the core, so the raw PC1-mimic basket tilts toward the lower-volatility names: [[BAE Systems]] (19.3%) and [[Thales]] (18.9%) carry the largest investable weights despite mid-pack loadings, because they are the calmest (~32% annualized) versus [[Rheinmetall]] (47%) and [[Hensoldt]] (55%). To reproduce the standardized factor you over-weight the calm names; to express the high-beta rearmament torque you do the opposite and over-weight Rheinmetall.

### Distinctness

![[euro-rearmament-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The six core European names form a warm block, visibly cooler against the US primes, the European equity ETF, and the broad market.*

### Historical tightness evolution

![[euro-rearmament-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion since 2022 — durable and tightening into 2026 as the rearmament trade consolidated into a single factor.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2022 | 0.633 | 69.4% | 0.568 |
| 2024 | 0.559 | 62.5% | 0.531 |
| 2025 | 0.610 | 67.2% | 0.532 |
| Latest 90d | 0.657 | 71.9% | 0.573 |

*Structurally durable: the cluster has held through the post-2022 Ukraine surge, eased mid-2024, and re-tightened into 2026 on the NATO 5% / Zeitenwende fiscal turn. The 2Y holdout (1.03, STABLE, loadings correlation 0.79) confirms the same factor structure persists out of sample.*

### The read-through

- European rearmament is a distinct, investable factor. It is +0.340 from the US [[Defense primes basket|hardware primes]] and +0.424 from broad European equity ([[VGK]]) — a US-defense position or a Europe ETF does not capture it. The clean expression is the six-name core ([[Rheinmetall]], [[BAE Systems]], [[Leonardo]], [[Saab]], [[Thales]], [[Hensoldt]]).
- Two regional defense factors, not one. The same rearmament demand drives both the US primes and the European cohort, but they trade as separate factors — a global-defense sleeve that holds both is running two positions, not one.
- [[Kongsberg]] is a beneficiary, not a core member. Its maritime/offshore leg detaches it from the tight European-defense-equity factor; treat it as a satellite, not part of the core basket.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation is queued for the July 2026 quarterly pass (definition date 2026-06-13).

## Related

- [[Long global rearmament]] — the thesis and demand drivers (the European leg of which this cohort expresses)
- [[Defense primes basket]] — the US hardware-prime cohort (+0.340 intra-advantage away; the comparator)
- [[Defense IT Services]] — the US GovCon-IT cohort (another defense sub-factor)
- [[European Defense Industry]] — broader sector context
- [[Rheinmetall]], [[BAE Systems]], [[Leonardo]], [[Saab]], [[Thales]], [[Hensoldt]], [[Kongsberg]] — cohort members
- [[Vault cluster taxonomy]] — cross-cohort comparison and verdict thresholds

*Created 2026-06-13.*
