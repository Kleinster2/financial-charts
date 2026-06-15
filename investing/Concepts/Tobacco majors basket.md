---
aliases: [Tobacco majors, Tobacco majors basket, Nicotine majors, Big Tobacco basket]
tags: [concept/cluster, tobacco, consumer-staples, defensive]
---

# Tobacco majors basket

> [!warning] Cluster status: real and distinct defensive factor, but two regional pairs not one basket, and weakening (2026-06-14)
> The four big Western nicotine majors — [[Altria]] (MO), [[Philip Morris]] (PM), [[British American Tobacco]] (BTI), [[Imperial Brands]] (IMBBY) — clear all three permutation nulls including the vol-matched null (intra p 0.0034), so the cohesion is a genuine tobacco-specific factor, not merely shared low-vol/duration. At an average pairwise correlation of -0.002 to [[SPY]] the cohort is essentially uncorrelated with the market — a true defensive. BUT the intra-cluster correlation is only 0.493 (PC1 63.6%), the cohort is boundary-dependent (it never forms a clean four-name island — it splits into a UK pair BTI/IMBBY and a US pair MO/PM that unify only where staples [[XLP]] joins), and the factor is weakening (2y holdout ratio 0.76) as the smoke-free transition pulls [[Philip Morris]] away from the combustibles names. This is the deliberate counter-case to [[China special valuation]]: both are defensive low-vol cohorts, but 中特估 FAILED the vol-matched null (a duration basket) while tobacco PASSES it (a real industry factor). See "Cluster validation" below.

The four largest Western tobacco and nicotine brand-owners cohere as a real but soft defensive factor. They share what no diversified staple shares — the same regulatory overhang, litigation history, ESG-exclusion flows, and secular volume decline — which is why their co-movement survives the vol-matched null where a generic low-vol basket would not. But they are not a clean tradeable basket: the factor is split by geography ([[United Kingdom]]-listed BTI/IMBBY vs US-listed MO/PM), diluted toward consumer staples at the boundary, and eroding as the four names' smoke-free transitions diverge their fundamentals.

---

## Constituents

| Company | Ticker | Listing / base | Profile | 1Y return | Ann vol |
|---|---|---|---|---|---|
| [[Altria]] | MO | US (NYSE) | US-domestic combustibles (Marlboro US), on! pouches; 35% JUUL writedown | +23.9% | 24.2% |
| [[Philip Morris]] | PM | US (NYSE) | Ex-US, smoke-free leader (IQOS, Zyn/Swedish Match) | +2.7% | 28.0% |
| [[British American Tobacco]] | BTI | UK (NYSE ADR) | UK-based global; Lucky Strike, Dunhill, Camel ex-US, Vuse | +35.9% | 23.7% |
| [[Imperial Brands]] | IMBBY | UK (OTC ADR) | UK-based #4 Western major; combustibles-heavy, blu vaping | +1.2% | 21.4% |

1Y total returns (adjusted close, to 2026-06-12). The dispersion is the story: the combustibles-heavy names (BTI +35.9%, MO +23.9%) re-rated hard while the smoke-free / transition names (PM +2.7%, IMBBY +1.2%) lagged — a 2025-26 reversal of the 2020-24 regime in which PM led (+194% vs MO +132% on total return since 2020). Even the two UK names, the tightest correlation pair, diverged by 35 points in 1Y return: co-movement direction is not co-return.

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/tobacco_majors.yaml`, with `cluster_permutation_test.py --null all`, `cluster_threshold_scan.py`, and `cluster_holdout_test.py --window 2y`. Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-06-13 to 2026-06-12)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.493 (weekly 0.541) | Moderate cohesion |
| PC1 explained variance | 63.6% (weekly 65.8%) | Moderate single-factor |
| Tightest pair | BTI-IMBBY = 0.629 | The two UK majors |
| Loosest pair | MO-IMBBY = 0.383 | US-domestic vs UK #4 |
| Cluster vs staples ETF (XLP) | 0.416 (+0.078) | Separates from staples — not just XLP |
| Cluster vs utilities (XLU) | 0.278 (+0.215) | Distinct from the bond-proxy defensive |
| Cluster vs market (SPY) | -0.002 (+0.495) | Uncorrelated with the market — true defensive |
| Independence null | rejected | The four co-move |
| Random-basket null | p 0.0011 | More cohesive than a random four-pick |
| Vol-matched null | p 0.0034 | Cohesion exceeds same-vol baskets — a real tobacco factor, not duration |
| Threshold scan | boundary-dependent | Never a clean four-name island |
| 2y holdout | WEAKENED (ratio 0.76) | Factor present but eroding |

![[tobacco-majors-cluster-correlation-1y.png]]
*1Y correlation matrix: the BTI/IMBBY (UK) and MO/PM (US) blocks are visible; cross-block correlations are lower.*

### Hierarchical clustering and join distances

The dendrogram does not produce a clean four-name cluster. It builds two pairs that merge late, and the merge coincides with consumer staples (XLP) joining — so there is no threshold at which the four tobacco names are an island.

![[tobacco-majors-cluster-dendrogram-1y.png]]

| Step | Left | Right | Distance (1-\|corr\|) | Members |
|---|---|---|---|---|
| 1 | BTI | IMBBY | 0.369 | BTI+IMBBY (UK pair) |
| 2 | MO | PM | 0.502 | MO+PM (US pair) |
| 3 | BTI+IMBBY | MO+PM | 0.542 | all four |

Final join distance 0.542 — the four names only unify at a correlation distance where XLP contaminates (threshold 0.60). The threshold scan returns no stable width: BOUNDARY-DEPENDENT.

![[tobacco-majors-cluster-threshold-scan.png]]

### PC1 index weights

PCA is run on standardized daily log returns. Raw PC1-mimic weight scales the PC1 loading by inverse realized volatility.

| Member | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| MO | 0.450 | 22.52% | 24.15% | 22.48% |
| PM | 0.514 | 25.75% | 28.01% | 22.16% |
| BTI | 0.538 | 26.94% | 23.69% | 27.40% |
| IMBBY | 0.495 | 24.79% | 21.36% | 27.96% |

![[tobacco-majors-cluster-pca-1y.png]]
*Balanced loadings (0.45-0.54) — no single name dominates PC1, consistent with a genuine shared factor rather than one name dragging the others.*

### Permutation nulls

![[tobacco-majors-cluster-permutation.png]]

The vol-matched null is the decisive test for a defensive cohort. Drawing 10,000 random four-name baskets matched to each member's realized-volatility rank (±5%, pool of 266 names), the null intra-correlation averages 0.215 (99th pct 0.477); the tobacco cohort's 0.493 clears it at p 0.0034. Cohesion is therefore not an artifact of all four being low-vol — there is a tobacco-specific factor. This is exactly what separates tobacco from [[China special valuation]], whose ten SOEs failed the same test because their cohesion was only shared duration.

### Historical tightness evolution

![[tobacco-majors-cluster-rolling-tightness-90d.png]]

| Year | Avg corr | PC1 | Final join distance |
|---|---|---|---|
| 2021 | 0.416 | 56.3% | 0.674 |
| 2022 | 0.403 | 55.7% | 0.668 |
| 2023 | 0.520 | 64.0% | 0.573 |
| 2024 | 0.547 | 66.4% | 0.548 |
| 2025 | 0.589 | 69.4% | 0.479 |
| 2026 | 0.521 | 64.3% | 0.547 |

This factor is not durable and not newly formed — it is mid-life and now weakening. Unlike most cohorts, tobacco did not peak in the 2020 COVID shock and loosen after; it tightened from 0.42 (2021) to 0.59 (2025) as the rate-hike cycle drove a defensive and yield bid into the group, then eased to 0.52 in 2026. Part of the 2023-25 cohesion is a duration-bid artifact (rates up, defensives bid together), which is consistent with the holdout weakening (ratio 0.76) as that bid faded and the members' smoke-free transitions diverged.

---

## What the verdict means

Three reads:
- Tobacco is a genuine, market-uncorrelated defensive factor — rare and valuable for diversification. The -0.002 correlation to [[SPY]] is real: this group is portfolio ballast, not a beta proxy. And it is a real factor, not a duration basket — the vol-matched null is what proves it.
- But it is not a clean basket. Express it as two regional pairs — UK ([[British American Tobacco]] / [[Imperial Brands]]) and US ([[Altria]] / [[Philip Morris]]) — not as a single four-name cluster. The UK pair (0.629) is tighter and shares GBP plus London-close exposure; the US pair (0.498) is looser because [[Philip Morris]]'s smoke-free transition has decoupled it from [[Altria]]'s US combustibles.
- The factor is eroding (holdout 0.76) because the members' businesses are diverging: PM is now a smoke-free growth story (IQOS, Zyn), MO a US-combustibles yield story, BTI and IMBBY combustibles-heavy value. The narrative law in reverse — as real, divergent fundamentals reassert, the shared "tobacco" factor loosens.

---

## Trade implications

| Trade | Verdict |
|---|---|
| Long tobacco basket / short SPY | Real market-neutral defensive exposure (cohort beta to SPY near zero) — the cleanest use |
| Long tobacco / short XLP | Captures the +0.078 separation from staples — thin but real |
| Long tobacco / short XLU | Captures +0.215 vs the bond-proxy defensive — tobacco is not just duration |
| UK pair (BTI/IMBBY) as one leg | The tighter, more coherent sub-structure (0.629); carries GBP exposure |
| US pair (MO/PM) as one leg | Looser (0.498) — a bet on the smoke-free-transition spread, not a factor |
| Four-name equal-weight basket | Diluted — the UK/US split and the staples boundary make it a soft factor |

---

## Related

### Member actors
- [[Altria]] — US combustibles, former PM parent
- [[Philip Morris]] — ex-US smoke-free leader (IQOS, Zyn)
- [[British American Tobacco]] — UK-based global major
- [[Imperial Brands]] — UK-based #4 Western major

### Adjacent concept notes
- [[China special valuation]] — the duration-basket counter-case (failed the vol-matched null tobacco passes)
- [[Regulated utilities]] — the second defensive that passes the vol-matched null (real business → real factor), but cleanly ETF-replicable (= XLU) where tobacco is not
- [[Mega banks basket]] — the within-financials cluster, the opposite verdict (cohesive but = XLF)
- [[Alcohol industry decline]] — the other "sin stock" secular-decline staple
- [[Vault cluster taxonomy]] — the cross-cohort map

### Methodology
- `docs/cluster-validation.md`
