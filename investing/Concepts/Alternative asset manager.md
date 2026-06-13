#concept #finance #investing

**Alternative asset manager** — Firm managing investments outside traditional stocks/bonds. Includes [[Private Equity]], [[Private credit]], real estate, infrastructure, hedge funds.

> [!success] Cluster status: validated — the listed alt-manager complex is a tight one-factor cohort (1Y intra-correlation 0.751, PC1 78.3%, all eight members join at ≤0.281 distance). Newly-formed and strengthening (90-day rolling tightness 0.57 → 0.86 → 0.75 across 2024–2026), a product of the FRE re-rating. [[Pátria Investimentos|Pátria]] is the validated EM-exception singleton. Full diagnostics below.

---

## Key players

AUM and FRE from FY2025 results where verified ([[Apollo]], [[Carlyle]], [[Blue Owl]], [[Brookfield]]); others approximate.

| Firm | AUM | FRE (FY2025) | Focus |
|------|-----|--------------|-------|
| [[Brookfield]] (BAM) | $1T+ | $3.0B (+22%) | Real assets, infra, renewables |
| [[Blackstone]] (BX) | ~$1.1T | — | Diversified |
| [[Apollo]] (APO) | $938B (fee-gen $709B) | $2.5B (record) | Credit + insurance ([[Athene]]) |
| [[Ares Management]] (ARES) | ~$600B | — | Credit-dominant |
| [[KKR]] | $500B+ | — | PE, credit, insurance |
| [[Carlyle]] (CG) | $477B | record, +12%, 47% margin | PE, credit |
| [[Blue Owl]] (OWL) | $307B | $1.5B | Direct lending, GP stakes, net lease |
| [[TPG]] | ~$250B | — | PE, growth, credit |

---

## Fee model

| Fee | Typical | Description |
|-----|---------|-------------|
| Management | 1-2% | On committed/invested capital |
| Performance | 20% | Carry on gains above hurdle |

Fee-related earnings (FRE) = management fees minus expenses. More stable than realized income.

---

## The FRE re-rating

The structural re-rating of 2023–2025 was a shift in what the market pays for. Performance fees (carry) are lumpy and cyclical; fee-related earnings (FRE) — management fees on long-duration, often permanent capital, minus expenses — are annuity-like. As the complex grew FRE-heavy (private credit, insurance balance sheets, perpetual vehicles), the market began valuing these names on FRE multiples rather than realized carry, lifting the whole group. The sub-models diverge on what feeds the FRE engine:

- Insurance-fed: [[Apollo]] ([[Athene]]) and [[KKR]] (Global Atlantic) originate assets for captive annuity balance sheets — spread-related earnings (SRE) plus FRE. Apollo originated a record ~$309B in 2025.
- Real-assets-fed: [[Brookfield]] — infrastructure, renewables, and now AI-infrastructure capital ($600B+ fee-bearing capital, the chart-less actor note covers its full-stack AI thesis).
- Permanent-capital credit: [[Blue Owl]] — direct lending BDCs + GP stakes + net-lease, ~90%+ permanent capital; the 2026 retail-BDC redemption stress is the counter-case to "permanent."
- Diversified PE-to-credit: [[Blackstone]], [[Carlyle]] (record FRE +12%, 47% margin under CEO Harvey Schwartz), [[TPG]].

## Cluster validation — does the complex trade as one?

Cohort: [[Apollo]], [[Blackstone]], [[KKR]], [[Ares Management]], [[Carlyle]], [[Blue Owl]], [[TPG]], [[Brookfield]]; controls = traditional asset managers ([[BlackRock]]) and ETFs (SPY, XLF). Config `scripts/cluster_configs/alt_managers.yaml`, 1-year window to 2026-06-12.

Finding: the listed alt managers are a genuine one-factor cohort. The eight names join hierarchically at distances 0.15–0.281 — a tight, evenly-loaded cluster (PC1 loadings all 0.34–0.37, no outlier) — and the factor intensified through the FRE re-rating (90-day rolling intra-correlation 0.57 in 2024 → 0.86 in 2025 → 0.75 in 2026).

| Diagnostic | Value | Read |
|-----------|-------|------|
| Avg intra-cohort correlation (1Y) | 0.751 | Tight, co-moving complex |
| PC1 explained variance | 78.3% | One dominant "alt-manager beta" factor |
| Join-distance range | 0.15–0.281 | All eight assemble cleanly; [[Brookfield\|BAM]] joins last (0.281) |
| PC1 loadings | 0.34–0.37 (even) | No member dominates or sits outside |
| Vol-adjusted weights | [[Brookfield\|BAM]] highest (lowest vol ~32%), [[Blue Owl\|OWL]] lowest (highest vol ~48%) | BAM the defensive core, OWL the high-beta sleeve |
| Cohort vs traditional AM | 0.622 (advantage +0.129) | Modest separation from plain AM (BLK co-moves with financials) |
| Cohort vs ETF | 0.559 (advantage +0.192) | Clear separation from broad market |
| Weekly cross-check | intra 0.690, PC1 73.0% | Robust to async-close timing |

### Candidate join-distance topology

1Y, average linkage, Distance (1-|corr|). The whole cohort assembles between 0.15 and 0.281 — well inside the 0.5 cut — before any broad-market name attaches.

| Step | Join | Distance |
|------|------|----------|
| 1 | BX + KKR | 0.152 |
| 2 | ARES + (BX+KKR) | 0.178 |
| 3 | APO + core | 0.214 |
| 4 | CG + TPG | 0.220 |
| 5 | (APO+ARES+BX+KKR) + (CG+TPG) | 0.253 |
| 6 | OWL + core | 0.267 |
| 7 | BAM + core | 0.281 |

### PC1 index weights

Raw PC1-mimic weights scale each PC1 loading by inverse realized volatility — the topology (who loads on the factor) versus the tradable basket (what an equal-factor-exposure portfolio would hold once vol is accounted for).

| Member | PC1 loading | Ann vol | Raw PC1-mimic weight |
|--------|-------------|---------|----------------------|
| [[Brookfield\|BAM]] | 0.340 | 31.7% | 14.9% |
| [[Blackstone\|BX]] | 0.363 | 37.6% | 13.4% |
| [[Apollo\|APO]] | 0.351 | 37.4% | 13.0% |
| [[KKR]] | 0.369 | 40.0% | 12.8% |
| [[Carlyle\|CG]] | 0.340 | 38.0% | 12.5% |
| [[TPG]] | 0.357 | 40.1% | 12.4% |
| [[Ares Management\|ARES]] | 0.363 | 45.5% | 11.1% |
| [[Blue Owl\|OWL]] | 0.344 | 48.1% | 9.9% |

[[Brookfield\|BAM]] is the defensive core (lowest vol, highest weight); [[Blue Owl\|OWL]] the high-beta sleeve (highest vol, lowest weight).

### Historical tightness evolution

90-day rolling. The cohort is newly-formed and strengthening, not a long-standing structural cluster — it tightened sharply in 2025 as the market re-rated the group on FRE multiples, then eased modestly in 2026. The factor has a birthday: it is a product of the re-rating, not a permanent feature of these businesses.

| Year | Avg corr | PC1 |
|------|----------|-----|
| 2024 | 0.570 | 62.7% |
| 2025 | 0.859 | 87.7% |
| 2026 | 0.747 | 78.0% |

![[altmgr-cluster-dendrogram-1y.png]]
*Hierarchical clustering (1Y, distance = 1−|corr|). The eight alt managers form one tight block; broad financials ([[BlackRock\|BLK]], SPY, XLF) join only at looser distances.*

![[altmgr-cluster-pca-1y.png]]
*PCA on the cohort: PC1 explains 78.3% of variance with near-uniform loadings — the signature of a real shared factor, not one name dragging the rest.*

![[altmgr-cluster-correlation-1y.png]]
*Pairwise 1Y correlation heatmap — the eight-name block is visibly tighter internally than its correlation to the [[BlackRock\|BLK]]/SPY/XLF controls.*

![[altmgr-cluster-rolling-tightness-90d.png]]
*90-day rolling tightness: the 2025 spike is the FRE re-rating compressing the cohort into a single factor.*

The exception that proves the cohort: [[Pátria Investimentos]] (PAX), the LatAm alt manager, is *not* in this cluster — run against the same cohort it is a hierarchical singleton (join distance 0.494, lowest PC1 loading), because its Brazil/EM factor dominates. Business comparability ("mini-Blackstone of LatAm") is not trading comparability. See [[Pátria Investimentos]] for that diagnostic.

## Synthesis

The listed alternative-asset managers have become a single trade. A decade ago they were idiosyncratic — PE houses, credit shops, a real-assets group — valued on lumpy carry. The migration to fee-related earnings on permanent and insurance capital turned them into annuity-like compounders, and the market re-rated the whole group on FRE multiples. The cluster math captures the consequence: an ~80%-PC1, 0.75-intra-correlation cohort that did not exist as a tight factor in 2024 and was forged in the 2025 re-rating. The sub-models still differ in what feeds the engine — insurance ([[Apollo]], [[KKR]]), real assets ([[Brookfield]]), permanent-capital credit ([[Blue Owl]]), diversified PE ([[Blackstone]], [[Carlyle]], [[TPG]]) — but on a returns basis those differences are now second-order to the shared factor. The boundary is geographic, not stylistic: [[Pátria Investimentos]], structurally the same business in Brazil, trades on the EM factor and sits outside the cluster. The risk the cohesion creates is its own undoing — a group that re-rated together on one thesis (FRE durability) will de-rate together if that thesis cracks, and the [[Blue Owl]] retail-BDC redemption stress is the first live test of whether "permanent capital" is as permanent as the multiple assumes.

## Related

- [[Private Equity]] — buyouts, growth equity
- [[Private credit]] — direct lending, mezzanine
- [[Private markets]] — broader category
- [[Apollo]] / [[Blackstone]] / [[KKR]] / [[Ares Management]] / [[Carlyle]] / [[Blue Owl]] / [[TPG]] / [[Brookfield]] — cohort members
- [[Pátria Investimentos]] — LatAm alt manager; validated singleton (the cohort exception)
- [[Athene]] — Apollo's insurance balance sheet (the FRE/SRE engine)

*Created 2026-02-05. Cluster validation + FY2025 cohort refresh added 2026-06-13.*
