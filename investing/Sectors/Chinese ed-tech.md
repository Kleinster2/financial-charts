---
aliases: [Chinese ed-tech, China ed-tech, China tutoring stocks, double-reduction cohort, China after-school tutoring]
tags: [sector, china, education, cluster-validation, adr]
---

# Chinese ed-tech

> [!warning] Cluster status: FALSIFIED / ETF-replicable — a loose, decohering [[China]]-ADR-beta cohort. The 2021 "double-reduction" (双减) shock forged a tight regulatory-survival factor that peaked at 0.72 in 2022 and has faded to 0.42 by 2026 as the survivors pivoted into different businesses. Distinct from US/global ed-tech (jurisdiction beats business model) but NOT from the China ETFs. (Jun 2026)
> The three US-listed tutoring ADRs ([[New Oriental|EDU]]/[[TAL Education|TAL]]/[[Gaotu Techedu|GOTU]]) co-move (independence null rejected at p<0.001), but the cohesion is loose (intra 0.399, below the 0.50 floor; weekly 0.427) and barely beats a random basket (p 0.027 — the null's 95th percentile is 0.375, the cohort's 0.399 just clears). It is +0.000 intra-advantage vs the China ETFs [[KWEB]]/[[FXI]]/[[CQQQ]] (the cohort correlates with them exactly as much as with itself — NOT distinct from China beta) and the threshold scan is FRAGILE (intact only at a single point, shatters into three singletons at the 0.5 cut). The one robust finding is jurisdiction over business model: +0.261 vs US/global ed-tech (DUOL/CHGG/COUR, corr 0.138) — but that is itself a China-factor statement, the same result as [[Chinese internet]]. See below.

The cohort the regulator created and then dissolved. [[New Oriental|EDU]] (overseas/test prep + East Buy livestream e-commerce), [[TAL Education|TAL]] (small-class enrichment + learning devices), and [[Gaotu Techedu|GOTU]] (exam/vocational prep, "All with AI" on [[DeepSeek]]) were one trade for two years — when the July 2021 [[Common Prosperity|"double-reduction" (双减) crackdown]] banned for-profit K-12 academic tutoring, their entire common business was the binary "is this legal" bet, and they fused (intra 0.80, PC1 81% in 2022). Forcing each survivor into a different permitted business is exactly what de-correlated them; their charts now reflect three different companies sharing only a Chinese domicile and a regulatory scar. The result resolves to [[China]]-ADR beta — the same verdict as [[Chinese internet]] (= [[KWEB]]) and [[Chinese EV startups]] (= [[FXI]]), and looser than either.

## Sector performance

![[china-edtech-performance.png]]
*Normalized total return since Jan 2021 vs the China-internet/ADR ETF [[KWEB]] (the closest liquid benchmark — no pure China-ed-tech ETF exists). The 2021 crackdown is the cliff all four go over together — the cohesion peak. What follows is divergence, not co-movement: [[KWEB]] is the most resilient (~−60%), then [[New Oriental|EDU]] (~−70%, lifted by East Buy), [[TAL Education|TAL]] (~−85%), and [[Gaotu Techedu|GOTU]] worst (~−97%, still near its lows). An ETF-replicable cohort tracks its benchmark; this one neither tracks KWEB tightly nor holds together — the legible picture of a loose China-beta basket whose members now move on their own pivots.*

## Cluster validation

The candidate cohort is the three US-listed Chinese tutoring ADRs — [[New Oriental|EDU]], [[TAL Education|TAL]], [[Gaotu Techedu|GOTU]] — tested against the China-equity ETFs ([[KWEB]] the closest sector proxy, [[CQQQ]] China-tech, [[FXI]] China-large-cap), a global ed-tech control (DUOL/CHGG/COUR — same business model, different jurisdiction, the key distinctness control), and the market/EM ([[SPY]]/[[QQQ]]/[[VWO]]). 1Y window through 2026-06-22 (160 obs); threshold 0.5. The third framework test on a foreign-ADR cohort (after [[Chinese internet]] and [[Chinese EV startups]]). Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.399 (weekly 0.427) | Below the 0.50 floor |
| Pairwise range | 0.30–0.45 (EDU-GOTU lowest) | No tight pair |
| PC1 explained variance | 60.1% (weekly 63.1%) | Modest single factor; ~40% idiosyncratic |
| Independence null p (10k) | 0.0001 (intra & PC1) | Series co-move (necessary, not sufficient) |
| Random-basket null p (10k) | 0.027 (intra), 0.032 (PC1) | Barely rejects — null 95th pct 0.375, cohort 0.399 just clears |
| Vol-matched null p (10k) | 0.011 (intra) | Beats same-vol baskets (not just shared high vol) — but still a weak pass |
| Holdout (2Y split) | WEAKENED 0.83, loadings corr 0.68 | Factor present but eroding out of sample |
| Threshold stable width | 0.00 (point only at 0.65) | Shatters into 3 singletons at ≤0.50; ETF-contaminated at 0.70 |
| Intra-adv vs China ETFs ([[KWEB]]/[[FXI]]/[[CQQQ]]) | +0.000 | NOT distinct from China beta — the verdict |
| Intra-adv vs US/global ed-tech (DUOL/CHGG/COUR) | +0.261 | Jurisdiction beats business model |
| Intra-adv vs market ([[SPY]]/[[QQQ]]/[[VWO]]) | +0.151 | Above broad market beta |

Config: `scripts/cluster_configs/china_edtech.yaml`; definition date 2026-06-22 (config registered for the next capstone batch).

### Boundary — the cohort never forms at the cut

![[china-edtech-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The China and market ETFs ([[KWEB]]/[[FXI]]/[[CQQQ]] + [[SPY]]/[[QQQ]]/[[VWO]], orange) merge into one tight beta cluster below distance 0.4, while the candidates [[New Oriental|EDU]]/[[TAL Education|TAL]]/[[Gaotu Techedu|GOTU]] (blue) stay separate, linking only above the 0.5 line — there is no distinct ed-tech factor at the standard cut. The global ed-tech control (DUOL/COUR, purple) joins far out at ~0.80; CHGG (AI-gutted) is the leftmost outlier.*

The threshold scan returns no clean band: the cohort is in three sub-clusters at every threshold ≤0.50, forms intact only at a single point (0.65, stable width 0.00), and is contaminated by the China/market ETFs at 0.70. Validation depends entirely on the threshold pick — the FRAGILE signature.

### Topology — a loose pair and a laggard

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | TAL + GOTU | 0.546 | the tightest pair, and still loose (corr 0.45) |
| 2 | EDU + (TAL+GOTU) | 0.628 | [[New Oriental|EDU]] joins above the cut (corr ~0.37) — no cluster forms at 0.5 |

There is no tight core to carve out. [[TAL Education|TAL]] and [[Gaotu Techedu|GOTU]] are the closest pair at corr 0.45 (still below the floor), and [[New Oriental|EDU]] — the most diversified survivor, with East Buy e-commerce making it least like a pure-tutoring name — is the loosest of the three (EDU-GOTU just 0.30). Unlike the [[Hospital operators|ex-CYH]] or [[IT services|ex-Wipro]] cases, there is no outlier whose removal rescues a distinct sub-cohort; the whole set is loose.

### PC1 index weights — even loadings, very high vol

![[china-edtech-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 60.1% — a single "China tutoring" factor, but a loose one (~40% sits in PC2+PC3, the divergent pivot stories). Loadings are fairly even (0.55–0.62). All three carry extreme annualized vol (34–47%) — speculative, headline-driven small-cap ADRs.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| EDU | 0.552 | 31.90% | 33.59% | 39.09% |
| TAL | 0.620 | 35.85% | 45.21% | 32.64% |
| GOTU | 0.558 | 32.26% | 46.98% | 28.26% |

The topology (join distances above) is the structure of co-movement; this raw PC1-mimic basket (inverse-vol-scaled PC1 loadings) is the tradeable expression of the same factor — and for this cohort that expression is dominated by EDU once vol is accounted for, but the factor it proxies is the China-ADR one [[KWEB]] already holds.

### Distinctness — = China beta, but NOT US ed-tech

![[china-edtech-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The cohort runs lukewarm to itself (0.30–0.45) and about equally warm to [[KWEB]]/[[FXI]]/[[CQQQ]] — the ETF-embedding — and cold to the US/global ed-tech control (DUOL/CHGG/COUR, ~0.14).*

Two distinctness numbers tell the whole story. Against the China ETFs the intra-advantage is exactly +0.000 — the cohort correlates with [[KWEB]]/[[FXI]]/[[CQQQ]] (0.399) precisely as much as with itself (0.399), so the ETF is the equal-or-better expression; this is the country-sector analogue of the [[Vault cluster taxonomy|commodity-beta law]] (miners = the metal; ADRs = the country ETF). Against the US/global ed-tech names the intra-advantage is strongly positive (+0.261): [[New Oriental|EDU]]/[[TAL Education|TAL]]/[[Gaotu Techedu|GOTU]] do not trade with Duolingo, Chegg, or Coursera (corr 0.138) — same business of selling education, but jurisdiction (China policy / ADR risk) beats business model. That is a real structural fact, but not an ownable edge: it is precisely the China-vs-rest factor [[KWEB]] isolates.

### Historical tightness evolution — a crisis factor that decohered

![[china-edtech-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion since 2019. The arc is the verdict's backbone: loose pre-crackdown (0.33), tightening as 2021 regulatory pressure built (0.68), a sharp fusion to 0.72 (PC1 81%) in 2022 — when the existential 双减 threat and ADR-delisting fear swamped every company-specific difference — then a steady loosening back to the floor (0.42) by 2026 as the survivors pivoted into genuinely different businesses.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2019 | 0.325 | 56.8% |
| 2020 | 0.521 | 68.8% |
| 2021 | 0.680 | 78.9% |
| 2022 | 0.721 | 81.4% |
| 2023 | 0.574 | 71.6% |
| 2024 | 0.492 | 66.1% |
| 2025 | 0.428 | 62.0% |
| 2026 | 0.418 | 61.3% |

*The cohesion is regime-dependent in strength: the shared factor was strongest exactly when the policy shock was largest (0.72 in 2022) and decays toward the floor as the names are left to their own pivots — the same shock-dependence seen in [[Chinese internet]], but here the decoherence is sharper because the ban was existential (it removed the core business) and forced more divergent reinventions. The factor was real at the shock and is fading with distance from it.*

## Where this sits in the campaign

- Tier 3 — FALSIFIED / ETF-replicable. The cohort co-moves (independence null rejected) but only barely beats the random-basket null (p 0.027, the campaign's faint-pass band, alongside [[Gig economy platforms]] and [[Off-price retail]]), has no stable threshold band, and weakens out of sample (0.83). It resolves to [[China]]-ADR beta (+0.000 vs the China ETFs).
- The third foreign-ADR cohort to resolve to its China ETF: [[Chinese internet]] = [[KWEB]], [[Chinese EV startups]] = [[FXI]], Chinese ed-tech = China beta. The [[Vault cluster taxonomy|index-rule law]] holds abroad — a country-sector ADR cohort collapses into its country ETF.
- Looser than either sibling (intra 0.399 vs internet's 0.491 and EV's 0.544), and the clearest case of a regulator-made cohort decohering: the 双减 ban both created the cluster (2022 peak) and, by forcing divergent pivots, dissolved it (2026 floor). The one robust fact — jurisdiction over business model (+0.261 vs US/global ed-tech) — is a China-factor statement, not an edge.

## Related

- [[New Oriental]], [[TAL Education]], [[Gaotu Techedu]] — the cohort members (TAL+GOTU the loose pair; EDU the diversified, least-correlated survivor)
- [[KWEB]] — the China-internet/ADR ETF the cohort resolves into (own this, not the basket); [[FXI]], [[CQQQ]] — broader China ETFs that also capture it
- [[Common Prosperity]] — the 2021 双减 tutoring crackdown that created the cohort
- [[China higher education realignment]] — the demand-side policy reshaping China's education market (degree-catalog overhaul)
- [[Chinese internet]], [[Chinese EV startups]] — sibling China-ADR cohorts, same decohering-from-2022 arc
- [[DeepSeek]] — the model behind Gaotu's "All with AI" pivot
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis; [[Cohort, cluster, basket]] — terminology

### Cross-vault
- [Geopolitics: China AI Employment Anxiety](obsidian://open?vault=geopolitics&file=Concepts%2FChina%20AI%20Employment%20Anxiety) — the China education / labor-policy backdrop

---

*Created 2026-06-22. 1Y daily log returns through 2026-06-22; config `scripts/cluster_configs/china_edtech.yaml` (definition date 2026-06-22). Prices verified against canonical `prices_long`. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
