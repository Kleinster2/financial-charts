---
aliases: [Japan semi materials, Japan semiconductor materials, Japan materials chokepoint, Japan chip materials]
tags: [concept, semiconductors, materials, japan, cluster-validation]
---

# Japan semi materials

The Tokyo-listed names behind [[Japan]]'s grip on the semiconductor materials chokepoint — photoresists and silicon wafers — and the question of whether they trade as one "Japan materials" factor. The cohort is the union of the vehicles named in [[Long Japan wafers]] and [[Long Japan photoresists]]: [[Tokyo Ohka Kogyo]] (4186.T, photoresist pure-play), [[Shin-Etsu]] (4063.T, wafers + photoresists), [[Sumco]] (3436.T, wafer pure-play), and the two diversified conglomerates [[Sumitomo Chemical]] (4005.T) and [[Fujifilm]] (4901.T). The validation falsifies the cohort: it is a strategic supply-chain category, not a return factor.

> [!failure] Cluster status: falsified — a supply-chain category, not a trading cohort (June 2026)
> "Japan semi materials" does not trade as one factor. Intra-corr is 0.381 (below the 0.50 floor) and collapses to 0.145 on weekly returns; PC1 explains only 50.9% with the rest spread across PC2–PC5 (genuinely multi-factor). The names shatter — at every threshold up to 0.45 they are five separate singletons; only the wafer duopoly [[Shin-Etsu]]+[[Sumco]] forms a pair (0.474), [[Tokyo Ohka Kogyo]] attaches just above the cut (0.515), and the two conglomerates [[Sumitomo Chemical]] and [[Fujifilm]] never join until 0.642 and 0.691 — they trade on petrochemicals and healthcare, not semi materials. The cohort passes the cohesion nulls only marginally (random-basket p 0.0166, vol-matched 0.0065 — the shared-semi-cycle-beta signature, ~165× weaker than the floor-passing cohorts) and the holdout is REGIME-DEPENDENT (0.59 — it was a real 0.607 cohort in 2024–25, collapsed to 0.358 in 2025–26). The constructive sub-structure: the wafer pair is the only durable structure, and the sharper finding is that Japan semiconductor *equipment* ([[Tokyo Electron]]+[[Lasertec]], 0.623) is a far tighter cohort than Japan materials — the opposite of the chokepoint framing. See below.

Why a strategic chokepoint is not a return cohort: [[Japan]] genuinely dominates these materials (~90% of EUV photoresists, ~55% of silicon wafers), but dominance is a fact about market share, not about co-movement. The materials names sell into different sub-markets with different demand curves — wafer area (cyclical, AI-die-size-driven), EUV photoresist layers (secular, node-driven), and for the conglomerates, businesses that have nothing to do with chips. A shared geography and a shared "chokepoint" story do not produce a shared equity factor, the same lesson as [[Medtech]] (a sector, not a factor) but with a real wafer-pair underneath.

## Cluster validation

> [!warning] Async-close and currency caveat
> The cohort and the equipment control are Tokyo-listed and yen-denominated, so intra-cohort and cohort-vs-equipment correlations are synchronous and clean. The US-listed controls (Entegris, EWJ, SOXX) close ~14 hours later and are dollar-denominated, so cohort-vs-US-control daily correlations are understated by async close and muddied by JPY/USD FX. The large "+0.31 intra-advantage vs global materials / ETFs" below is therefore mostly an async/FX artifact, not real factor separation — the only clean distinctness read is vs Japanese equipment (+0.069), and the weekly cross-check (0.145) is the async-robust internal number.

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.381 [0.264–0.526] | Below the 0.50 floor; weekly 0.145 (collapses) |
| PC1 explained variance | 50.9% | Low — variance spread across PC2–PC5 (multi-factor) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0166 | Marginal pass — shared semi-cycle beta, not a tight factor |
| Vol-matched null p (10k) | 0.0065 | Marginal — barely beats same-vol baskets |
| Holdout (2Y split) | REGIME-DEPENDENT 0.59 | 0.607 in 2024–25 → 0.358 in 2025–26 |
| Threshold clean width | 0.00 | Five singletons up to 0.45 — never a clean cluster |
| Intra-adv vs Japan equipment (clean) | +0.069 | Barely distinct from Tokyo Electron/Lasertec |
| Intra-adv vs global materials (ENTG/WAF) | +0.312 | Inflated by Tokyo-vs-US async/FX — not real |
| Intra-adv vs ETF (EWJ/SOXX) | +0.321 | Inflated by async/FX — not real |

1Y daily log returns through 2026-06-12, threshold 0.5. Cohort all Tokyo-listed (synchronous internally); see the async caveat above for the US-control comparisons. Config: `scripts/cluster_configs/japan_semi_materials.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — the cohort shatters; the wafer pair is the only structure

![[jpmaterials-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The five materials names do not form a cluster: only [[Shin-Etsu]]+[[Sumco]] (the wafer duopoly) pair; [[Tokyo Ohka Kogyo]], [[Sumitomo Chemical]] and [[Fujifilm]] are singletons. The Japanese equipment pair [[Tokyo Electron]]+[[Lasertec]] clusters tightly and separately; the US names (Entegris, EWJ, SOXX) form their own block (async/FX-driven). Japan materials is the loosest structure on the chart.*

The threshold scan returns zero stable width — through threshold 0.45 the cohort is five separate singletons, a pair appears only at 0.50, and the cohort never reaches an intact single cluster; when three names finally group at 0.65, the equipment names contaminate before the conglomerates ([[Sumitomo Chemical]], [[Fujifilm]]) ever join. This is the [[Medtech]] signature — a category that shatters — but with a constructive wafer pair underneath rather than pure dispersion.

### Topology — a wafer pair, a loose materials core, two unrelated conglomerates

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | Shin-Etsu + Sumco | 0.474 | The wafer duopoly — the only sub-0.5 join |
| 2 | Tokyo Ohka Kogyo + (wafer pair) | 0.515 | Photoresist pure-play attaches — loose 3-name materials core, just above the cut |
| 3 | Sumitomo Chemical + core | 0.642 | Conglomerate joins late — trades on petrochemicals |
| 4 | Fujifilm + rest | 0.691 | Conglomerate joins last — trades on healthcare |

The structure is a clean three-tier decomposition: a real wafer pair ([[Shin-Etsu]]+[[Sumco]], 0.53 pairwise — validating the [[Long Japan wafers]] two-vehicle pairing), a photoresist pure-play ([[Tokyo Ohka Kogyo]]) that attaches loosely, and two diversified conglomerates ([[Sumitomo Chemical]], [[Fujifilm]]) that do not belong to a semi-materials factor at all. The conglomerates' minority semi exposure (~15% each) is invisible against their dominant petrochemical and healthcare businesses.

### PC1 index weights

![[jpmaterials-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains only 50.9% with a long tail (PC2 15.6%, PC3 14.6%) — the fingerprint of several factors, not one. The conglomerates [[Sumitomo Chemical]] and [[Fujifilm]] carry the lowest loadings (0.40, 0.37).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| Tokyo Ohka Kogyo (4186.T) | 0.478 | 21.5% | 57.1% | 17.1% |
| Shin-Etsu (4063.T) | 0.476 | 21.4% | 40.7% | 23.8% |
| Sumco (3436.T) | 0.493 | 22.2% | 75.3% | 13.4% |
| Sumitomo Chemical (4005.T) | 0.403 | 18.1% | 42.7% | 19.2% |
| Fujifilm (4901.T) | 0.373 | 16.8% | 28.6% | 26.6% |

Volatilities span a 2.6x range (Fujifilm 28.6% to Sumco 75.3%) — these are not comparable risk objects. Sumco is the high-beta wafer-cycle name; Fujifilm is a low-vol healthcare conglomerate that happens to make some photoresist.

### Distinctness — the only clean test is vs Japanese equipment

![[jpmaterials-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The single warm cell is [[Shin-Etsu]]–[[Sumco]] (0.53). The cohort's apparent coolness against the US names (Entegris, EWJ, SOXX) is async/FX, not distinctness — note the equipment pair [[Tokyo Electron]]–[[Lasertec]] is the warmest block on the chart.*

On the only clean comparison — same market, same currency, same trading session — the materials cohort is barely distinct from Japanese semiconductor equipment (+0.069), and the equipment pair (0.623) is far tighter than the materials cohort (0.381). The "+0.31" advantages vs global materials and the ETFs are Tokyo-vs-US async and JPY/USD FX artifacts and should not be read as factor separation. The honest read: within the Japan chip supply chain, equipment is the cohesive cohort (it belongs to the validated [[WFE]] factor); materials is not.

### Historical tightness evolution

![[jpmaterials-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. The cohort cohered only in the 2022 semiconductor-shortage cycle (0.566) and sits at ~0.37–0.40 in every other year — a cyclically-correlated group, not a standing factor.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2022 | 0.566 | 66.0% | 0.573 |
| 2024 | 0.367 | 51.1% | 0.802 |
| 2025 | 0.373 | 50.0% | 0.681 |
| 2026 | 0.384 | 50.9% | 0.660 |

*Regime-dependent: the names co-move during semiconductor-cycle stress (2022 shortage; the 2024–25 holdout train half at 0.607) and decouple otherwise (2025–26 test half 0.358). The factor is a cycle phenomenon, not a structural one — there is no durable "Japan materials" cohort to own through the cycle.*

### The read-through

- "Japan semi materials" is not a tradeable cohort. Intra 0.381 (weekly 0.145), shatters at every threshold, regime-dependent holdout — a strategic chokepoint category, not a return factor. Owning a "Japan materials basket" buys several unrelated risks plus shared semi-cycle beta.
- The wafer duopoly is the only real structure. [[Shin-Etsu]]+[[Sumco]] (0.53) is the genuine pair — the [[Long Japan wafers]] two-vehicle pairing is the one part of the materials thesis that holds together as a trade. [[Tokyo Ohka Kogyo]] attaches loosely as the photoresist leg.
- The conglomerates do not belong. [[Sumitomo Chemical]] and [[Fujifilm]] trade on petrochemicals and healthcare; their minority semi exposure is not investable as photoresist-factor exposure. The [[Long Japan photoresists]] note's "diversified alternatives" are diversified away from the thesis.
- Japan equipment is the tighter cohort, not materials. [[Tokyo Electron]]+[[Lasertec]] (0.623) is a real cohort on the [[WFE]] capex cycle; the materials names are only +0.069 distinct from it. The common framing that elevates "Japan materials" as the cohesive chokepoint inverts the actual factor structure.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-14).

## Related

- [[Semiconductor Materials]] — the sector hub (global view; this note is the Japan-cohort validation)
- [[Long Japan wafers]] — the thesis whose Shin-Etsu+Sumco pairing the wafer-pair result supports
- [[Long Japan photoresists]] — the thesis whose "diversified alternatives" the conglomerate-singleton result challenges
- [[Tokyo Ohka Kogyo]], [[Shin-Etsu]], [[Sumco]], [[Sumitomo Chemical]], [[Fujifilm]] — the cohort members
- [[Tokyo Electron]], [[Lasertec]] — Japanese semi equipment (the tighter, separate cohort)
- [[WFE]] — the validated equipment cohort the Japanese equipment names belong to
- [[Entegris]], [[Siltronic]] — non-Japan materials peers (control)
- [[JSR Corporation]] — the photoresist leader taken private in 2024 (excluded — no live series)
- [[Photoresists]] — the chokepoint concept
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
