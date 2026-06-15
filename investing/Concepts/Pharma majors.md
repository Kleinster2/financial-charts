---
aliases: [Pharma majors, Big pharma, Pharmaceutical majors, Big pharma cluster]
tags: [concept, cluster-validation, healthcare, pharmaceuticals, usa]
---

# Pharma majors

> [!failure] Cluster status: falsified — big pharma is healthcare beta, not a distinct factor (Jun 2026)
> The big-cap US pharma names ([[Eli Lilly|LLY]]/[[Pfizer|PFE]]/[[Merck|MRK]]/[[AbbVie|ABBV]]/[[Bristol-Myers Squibb|BMY]]) do not trade as one factor. Intra-corr is 0.412 (weekly 0.327 — drops, common noise not a persistent factor), PC1 only 53% with variance spread across PC2–PC5. The cohort shatters: [[Eli Lilly]] clusters with biotech ([[Amgen]]/[[Vertex Pharmaceuticals|VRTX]]) and the health/biotech ETFs, [[Pfizer]]+[[Bristol-Myers Squibb]] pair as patent-cliff decliners, and [[Merck]] and [[AbbVie]] are singletons. The intra-advantage is ~zero versus biotech (+0.005) and NEGATIVE versus the ETFs (−0.005) — it clears the random-basket null (p 0.0050) only on shared healthcare/biotech beta, the grade-2 "sector beta, nothing cohort-specific" signature. Each major trades on its dominant driver, not a shared "big pharma" factor. The [[GLP-1 receptor agonists|GLP-1]] / [[Medtech]] dominant-driver-divergence law at the large-cap-pharma level.

The large-cap-pharma counterpart to the falsified [[GLP-1 receptor agonists|GLP-1/obesity]] and [[Medtech]] cohorts, and the same result. The question was whether the big pharma names cohere as a defensive healthcare factor or shatter on their divergent pipelines and patent cliffs. They shatter — and the way they shatter is the finding: [[Eli Lilly]], the GLP-1 growth winner, trades like biotech (it clusters with [[Amgen]]/[[Vertex Pharmaceuticals]] and inside the health/biotech ETFs, not with its pharma peers), while [[Pfizer]] and [[Bristol-Myers Squibb]] — both working through post-COVID and patent-cliff declines — pair together, and [[Merck]] (Keytruda) and [[AbbVie]] (the Humira-to-Skyrizi transition) each go their own way. There is no "big pharma" factor; there is healthcare/biotech beta plus five idiosyncratic franchises.

## Cluster validation

The candidate cohort is the five big-cap US pharma names — [[Eli Lilly|LLY]], [[Pfizer|PFE]], [[Merck|MRK]], [[AbbVie|ABBV]], [[Bristol-Myers Squibb|BMY]] — tested against large-cap biotech ([[Gilead Sciences|GILD]], [[Amgen|AMGN]], [[Vertex Pharmaceuticals|VRTX]]) and benchmarks (XLV health-care ETF, IBB biotech ETF, SPY).

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.412 [0.283–0.569] | below the 0.50 floor; weekly 0.327 (drops — common noise, not a persistent factor) |
| PC1 explained variance | 53.3% | weak; variance spread across PC2–PC5 (multi-factor) |
| Independence null p | 0.0001 | series co-move at all (necessary, not sufficient) |
| Random-basket null p | 0.0050 (PC1 0.0079) | passes — but only via shared healthcare/biotech beta (see intra-advantage) |
| Holdout (2Y split) | STRENGTHENING 1.28 | ambient healthcare-beta rising, not a pharma factor (loadings corr 0.32 — unstable structure) |
| Threshold clean width | 0.00 | BOUNDARY-DEPENDENT — never forms a clean cluster |
| Intra-adv vs biotech (GILD/AMGN/VRTX) | +0.005 | ~zero — pharma correlates as much with biotech as with itself |
| Intra-adv vs ETFs (XLV/IBB/SPY) | −0.005 | NEGATIVE — it IS healthcare/biotech beta, no pharma-specific factor |

1Y daily log returns through 2026-06-12, threshold 0.5. All US-listed (synchronous). Config: `scripts/cluster_configs/lly.yaml`; registry row 2026-06-15. Terminology: [[Cohort, cluster, basket]].

### Boundary — Lilly with biotech, Pfizer/BMY pair, the rest singletons

![[pharma-majors-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. [[Eli Lilly]] clusters with biotech ([[Vertex Pharmaceuticals|VRTX]], [[Amgen|AMGN]]) and the health/biotech ETFs (XLV/IBB, green); [[Pfizer]]+[[Bristol-Myers Squibb]] pair (orange, the patent-cliff decliners); [[Merck]], [[AbbVie]], [[Gilead Sciences|GILD]] and SPY are singletons. The candidate cohort never forms.*

The decisive feature is where Lilly lands: inside the biotech/health-ETF cluster, not with the other pharma majors — the GLP-1 growth re-rating has pulled it out of "pharma" and into "growth healthcare." The only intra-cohort pair is Pfizer+BMY, two names bound by the same post-patent-cliff decline rather than a shared pharma factor. With the health and biotech ETFs sitting inside the cohort's only real cluster, there is nothing pharma-specific left to own.

### Topology — only the decliner pair joins below the cut

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | PFE + BMY | 0.431 | the patent-cliff decliner pair (the only sub-0.5 join) |
| 2 | MRK + (PFE+BMY) | 0.537 | Merck joins above the cut |
| 3 | ABBV + (MRK+PFE+BMY) | 0.601 | AbbVie joins higher |
| 4 | LLY + (rest) | 0.642 | Lilly last — the most decoupled, trades with biotech |

Only Pfizer+BMY join below the 0.5 threshold; Merck, AbbVie, and especially Lilly attach well above it. Lilly joining last (0.642) — more distant from its pharma peers than any other member — is the quantitative form of "the GLP-1 winner trades like biotech."

### PC1 index weights

![[pharma-majors-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains only 53.3% with a fat tail of PC2–PC5 — a multi-factor cohort, not a single one. Loadings are dispersed (0.40–0.49).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| Eli Lilly (LLY) | 0.397 | 17.8% | 36.8% | 13.0% |
| Pfizer (PFE) | 0.479 | 21.5% | 23.4% | 24.7% |
| Merck (MRK) | 0.452 | 20.3% | 27.1% | 20.1% |
| AbbVie (ABBV) | 0.409 | 18.4% | 24.7% | 20.0% |
| Bristol-Myers Squibb (BMY) | 0.491 | 22.1% | 26.7% | 22.2% |

The dispersed loadings and weak PC1 confirm no dominant common factor. [[Eli Lilly]] carries the lowest loading and the highest volatility (36.8%) — the GLP-1 high-flyer is both the most idiosyncratic and the least representative of whatever weak common factor exists.

### Distinctness — it IS healthcare beta

![[pharma-majors-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. No uniformly hot block; the warmest cells are Pfizer–BMY and Lilly–biotech, and the cohort is just as warm against XLV/IBB as internally.*

The ~zero intra-advantage versus biotech (+0.005) and the negative one versus the ETFs (−0.005) are the verdict: the big pharma names correlate with healthcare and biotech beta as much as with each other, so there is no distinct pharma factor to extract. This is grade-2 falsification in the campaign's taxonomy — it clears the random-basket null (p 0.0050) but only on shared sector beta, exactly like [[Medtech]] (which "correlates more with IHI/XLV than with itself"). For healthcare exposure, own XLV; for the GLP-1 trade, own [[Eli Lilly]] (or the [[GLP-1 receptor agonists]] names); there is no "big pharma basket" worth holding as a distinct factor.

### Historical tightness evolution

![[pharma-majors-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Never tight — a loose 0.63 in the 2020 COVID-defensive trade, fragmenting to 0.20 by 2024 as the franchises decoupled (Lilly's GLP-1 ascent, Pfizer's COVID unwind), a partial 2025 recovery to 0.43, easing to 0.37 in 2026.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.628 | 70.5% |
| 2021 | 0.474 | 58.4% |
| 2022 | 0.517 | 61.9% |
| 2023 | 0.353 | 48.6% |
| 2024 | 0.204 | 39.2% |
| 2025 | 0.433 | 56.2% |
| 2026 | 0.369 | 50.1% |

Big pharma has never been a tight factor and reached its loosest (0.20) in 2024 — the opposite of a durable cluster. The 2024 trough coincides with the franchises' drivers maximally diverging: Lilly re-rating on GLP-1, Pfizer derating on the COVID unwind, Merck and AbbVie on their own pipeline clocks. The label is durable; the factor is not.

## Related

- [[Eli Lilly]], [[Pfizer]], [[Merck]], [[AbbVie]], [[Bristol-Myers Squibb]] — the five majors, each on its own driver
- [[GLP-1 receptor agonists]] — the falsified obesity cohort (same dominant-driver-divergence law; Lilly is the link)
- [[Medtech]] — the sibling healthcare falsification (grade-2, sector beta)
- [[Healthcare]] — the broad sector hub
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-15. 1Y daily log returns through 2026-06-12; config `scripts/cluster_configs/lly.yaml`; registry row 2026-06-15. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
