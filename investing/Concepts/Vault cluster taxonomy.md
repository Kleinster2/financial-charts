---
aliases: [Cluster taxonomy, Cluster comparison, Vault clusters, Cluster validation taxonomy]
tags: [concept, framework, cluster-validation, meta-analysis]
---

# Vault cluster taxonomy

Synthesis of cluster-validation findings across the vault's validated and falsified cohorts as of May 2026. Documents what was learned by applying the [[Space pure-plays]] framework to 8 cohorts with matched methodology (1Y window through 2026-05-07, threshold 0.5, identical PCA + factor-decomposition + subset-optimization scripts). The cross-cohort tests revealed structural patterns that recur — useful as a reference when validating new cohorts.

---

## Cross-cohort comparison (matched methodology)

| Cluster | N | Intra-corr (1Y) | Pairwise range | PC1 | Specific factor | Verdict |
|---|---|---|---|---|---|---|
| [[Sectors/WFE\|WFE quartet]] | 4 | 0.804 | 0.740-0.857 | 85.33% | — | Validated (tightest — oligopoly limit) |
| [[Sectors/Korea Memory\|Korea Memory]] | 2 | 0.756 | (pair only) | 87.82% | — | Validated (pair) |
| [[Sectors/US Memory\|US Memory]] | 3 | 0.696 | 0.655-0.754 | 79.72% | — | Validated |
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | 7 | 0.691 | 0.482-0.840 | 73.79% | 37.0% | Validated (tightest N=7) |
| [[Space pure-plays]] | 7 | 0.624 | 0.494-0.749 | 67.96% | 59.6% | Validated |
| [[Sectors/AI Compute\|AI Compute]] | 3 | 0.600 | 0.544-0.663 | 73.37% | — | Validated |
| [[Concepts/Defense primes basket\|Defense primes 6-core]] | 6 | 0.556 | 0.448-0.707 | 64.31% | 36.0% | Validated (after LDOS exclusion) |
| [[Concepts/Defense primes basket\|Defense primes 7-name]] | 7 | 0.512 | 0.210-0.707 | 58.59% | — | Partial (LDOS drag) |
| [[Concepts/Mag 7 cluster\|Mag 7]] | 7 | 0.316 | 0.078-0.461 | 41.82% | 14.6% | Falsified |
| [[Concepts/Boutique advisory consolidation\|Boutique advisory consolidation]] | 6 | 0.73 (May 2025 figures) | — | 77% | — | Validated (older methodology — re-run pending) |
| [[Sectors/UAS defense micro-cluster\|UAS pair]] | 2 | 0.638 | (pair only) | — | — | Validated micro-cluster (KTOS-AVAV) |

All 8+ cohorts run with matched methodology except Boutique advisory (older numbers retained until re-run). [[Space pure-plays]] is the canonical worked example with all 19 analytical sections; [[Concepts/Mag 7 cluster|Mag 7]] is the canonical falsified counterpoint at same N=7.

---

## Ongoing exploration log

This section records boundary tests, candidate screens, and falsified cluster hypotheses that are too important to leave only in daily notes but are not yet part of the matched cross-cohort comparison table. Durable diagnostics still live in the cohort-owning note; this log tracks what was tested, what changed, and where the evidence lives.

| Date | Exploration | Status | Finding | Canonical evidence |
|---|---|---|---|---|
| 2026-05-27 | [[Space pure-plays]] post-SpaceX-IPO-hype refresh | Existing cluster held | Refreshed `prices_long` through 2026-05-27 and fixed date filtering in `scripts/cluster_analysis.py`; the seven-name cohort still clustered together at the 0.5 threshold with 1Y intra-correlation 0.625 and PC1 68.0%. `VOYG` is the best watch-list addition candidate, `KTOS` remains a defense-tech boundary case, and `DXYZ` is an event co-mover rather than structural member. | [[Space pure-plays]]; `scripts/cluster_configs/rklb.yaml`; `space-pureplays-cluster-may27-*` diagnostics |
| 2026-05-28 | [[Luxury]] / global luxury basket retest | Validated narrower core; broad basket falsified | Broad "global luxury" is a useful industry basket, not one clean correlation cluster. Strict European core = `MC.PA`, `RMS.PA`, `KER.PA`, `CFR.SW`, `MONC.MI` with 1Y avg correlation 0.664 and PC1 73.3%; loose core adds `BRBY.L` and `BC.MI`. `1913.HK` and `ZGN` remain outside the validated core. | [[Luxury]]; `scripts/cluster_configs/luxury_global.yaml`; `global-luxury-cluster-*` diagnostics |
| 2026-05-28 | [[Prada]]/[[Zegna]] fashion-cluster hypothesis | Falsified | `1913.HK` / `ZGN` pair correlation was only 0.175 over 1Y and 0.151 over 2Y; the wider fashion/premium set had only 0.288 1Y avg correlation and 39.1% PC1. [[Burberry]] and [[Brunello Cucinelli]] attach more to the loose luxury core than to a fashion sleeve. | [[Luxury]]; `scripts/cluster_configs/luxury_global.yaml`; follow-up Python screen logged in `investing/Daily/2026-05-28.md` |
| 2026-05-28 | Luxury-adjacent cluster screen | Watch list | Strongest neighbor was affluent-consumer beta, not fashion: `RACE`, `RL`, `ZGN`, `SPY`, `XLY`, `VGK`, `EWQ` showed 0.591 2Y avg correlation and 67.2% PC1. U.S. accessible premium/apparel was moderate; athletic premium was weaker; beauty/eyewear did not validate as one adjacent cluster. | [[Luxury]]; `investing/Daily/2026-05-28.md` |

---

## Structural patterns observed across cohorts

### 1. Cohort size does not determine cluster structure

Three N=7 cohorts span the verdict spectrum:

| Cohort | Intra-corr | Verdict |
|---|---|---|
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | 0.691 | Validated (tightest N=7) |
| [[Space pure-plays]] | 0.624 | Validated |
| [[Concepts/Mag 7 cluster\|Mag 7]] | 0.316 | Falsified |

Same N=7, materially different cluster structures. The binding constraint is business-model coherence, not cohort size. When validating a new N=7 cohort, the comparison question becomes "which of these three is it closest to in business-model variance?"

### 2. Three distinct stability trajectories

Cohort cohesion can move in three directions over time:

| Pattern | Example | Mechanism |
|---|---|---|
| Tightening | [[Space pure-plays]] (0.48 → 0.64 over 3Y → YTD) | Institutional basket construction (Nov 2025 regime shift) |
| Stable | [[Sectors/Crypto-to-AI\|Crypto-to-AI]] (0.69-0.74 throughout 3Y) | Cluster identity formed early (2023-2024 AI capex flood) and stayed |
| Stable | [[Concepts/Defense primes basket\|Defense primes 6-core]] (0.55-0.59 throughout) | DoD-customer factor is structurally durable, no narrative shift |
| Loosening | [[Concepts/Mag 7 cluster\|Mag 7]] (0.47 → 0.32 over 3Y → YTD) | Cohort decoupling into individual catalyst paths post-2024 |

Cleanest signature of an institutional-basket-construction event: PC2 collapses while PC1 rises (Space pure-plays Nov 2025: PC2 21.2% → 7.9%, PC1 51.9% → 71.2%). Cleanest signature of fragmentation: intra-correlation falls monotonically across windows (Mag 7).

### 3. Three distinct PC2 sub-structure types

PC2 captures cohort sub-structure when it exists. Three observed patterns:

| Pattern | Example | Description |
|---|---|---|
| Balanced 2-sleeve | [[Sectors/Crypto-to-AI\|Crypto-to-AI]] (pure miners vs AI-pivot) | PC2 loadings split roughly evenly with multiple names in each sleeve |
| Balanced 2-sleeve | [[Space pure-plays]] (data businesses vs hardware) | Same |
| Single-name outlier | [[Concepts/Defense primes basket\|Defense primes]] (HII +0.77 alone) | One name isolated on PC2; rest cluster near zero |
| Multi-axis fragmentation | [[Concepts/Mag 7 cluster\|Mag 7]] (PC2 + PC3 both meaningful) | No clean PC2 split; cohort spreads across multiple factors |

When checking a new cohort: look at PC2 loadings ranked by magnitude. If the loadings fall into two roughly-equal groups of opposite sign, you have a balanced split. If one name dominates PC2 magnitude (>0.6) with others near zero, you have an outlier. If PC2 + PC3 are both meaningful and loadings don't fall into clean groups, the cohort is multi-factor and may not be a single tradeable cluster.

### 4. Factor specificity ranges widely

After regressing the equal-weighted basket against relevant benchmarks, the residual variance reveals how cohort-specific the factor is:

| Cohort | Residual factor share | Reads |
|---|---|---|
| [[Space pure-plays]] | 59.6% | Genuine pure-play factor; basket is the only tradable expression |
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | 37.0% | Real factor but ~60% explained by SPY + IBIT + AI infra |
| [[Concepts/Defense primes basket\|Defense primes 6-core]] | 36.0% | Real factor; SPY beta near zero |
| [[Concepts/Mag 7 cluster\|Mag 7]] | 14.6% | Essentially leveraged QQQ; cohort is the benchmark |

The right threshold for "genuine pure-play factor" is roughly 30-40%+ residual variance after relevant benchmarks. Below 20% the cohort doesn't add factor isolation beyond what's available via broad ETFs. Space pure-plays' 59.6% is the highest residual factor share among tested cohorts — the cleanest case for "you can only express this thesis via the basket."

### 5. The Swiss-Army-knife pattern

Every validated cohort has one diversifying name that appears in 3-4 of the top-5 Sharpe pairs. The name has lower PC1 loading (more idiosyncratic) but high cumulative return, so combining it with high-PC1-loading peers improves Sharpe via uncorrelated residual returns:

| Cohort | Swiss-Army-knife name | PC1 loading | 1Y return | Why it diversifies |
|---|---|---|---|---|
| [[Space pure-plays]] | [[Planet Labs\|PL]] | 0.30 (lowest) | +242% (#2 in cohort) | Pure-data EO; trades on NGA contract cycle |
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | [[Iris Energy\|IREN]] | 0.41 | +163.5% (#1) | Heaviest AI-pivot among miners; HPC scale |
| [[Concepts/Defense primes basket\|Defense primes]] | [[RTX]] | 0.34 | +22.7% (#1) | Most diversified commercial+defense |

The Swiss-Army-knife name is the cohort member with the most-divergent business model relative to the rest. It's the cohort's least-factor-tracking name AND its highest-Sharpe-pair partner. Future cohort analyses should explicitly identify this name — it's the natural complement to the factor-clean tracking subset.

### 6. Factor-tracking ≠ return-maximizing (three independent confirmations)

Optimizing for "best 2-name tracking correlation to the full basket" produces a different optimal pair than optimizing for "best Sharpe" or "best cumulative return":

| Cohort | Best factor-tracking pair | Best Sharpe pair | Best return pair |
|---|---|---|---|
| [[Space pure-plays]] | LUNR+BKSY (0.94 corr) | RKLB+PL (Sharpe 2.03) | LUNR+PL (+254%) |
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | HUT+CLSK (0.97 corr) | RIOT+IREN (1.78) | RIOT+IREN (+136%) |
| [[Concepts/Defense primes basket\|Defense primes]] | NOC+HII (0.94 corr) | RTX+GD (1.27) | RTX+HII (+22.6%) |

Crypto-to-AI and Defense primes both produced the SURPRISE pattern where the factor-tracking pair UNDERPERFORMS the full basket on Sharpe (HUT+CLSK 1.12 < full 7 1.39 < complement 5 1.49; NOC+HII 0.35 < full 6 0.82 < complement 4 1.09). The factor-clean tracking optimization passes over the high-return idiosyncratic names because they're factor-misaligned by construction. Three independent cohort tests confirmed: the right answer depends on the objective.

For traders: pick factor-tracking pair for hedging / pair-trading the basket; pick Sharpe-optimal pair for portfolio-construction position sizing; pick return-maximizing pair for single-name conviction.

### 7. Boundary refinement matters

Sometimes a cohort is mis-defined by one name. The framework can refine the boundary:

| Cohort | Original verdict | After name refinement |
|---|---|---|
| Defense primes | Partial (with LDOS, intra-corr 0.512) | Validated (without LDOS, intra-corr 0.556) |

LDOS had PC1 loading 0.295 (lowest in cohort, vs 0.37-0.42 for the others) AND 1Y return of -30% (vs +18-23% for top performers). Both signals pointed to misalignment. Removing it lifted the cohort's verdict from partial to validated. The rule: when a cohort partially validates, check the lowest-PC1-loading name first — it may be the boundary refinement.

### 8. Validated cohorts have low SPY beta

After benchmark decomposition, the validated cohorts trade on factors uncorrelated with broad market:

| Cohort | SPY beta (multivariate) |
|---|---|
| [[Concepts/Defense primes basket\|Defense primes]] | -0.52 |
| [[Space pure-plays]] | -0.12 |
| [[Sectors/Crypto-to-AI\|Crypto-to-AI]] | +0.71 (with IBIT controls) |
| [[Concepts/Mag 7 cluster\|Mag 7]] | -0.13 (with QQQ control — but QQQ beta +1.84) |

The pattern: validated cohorts have low or negative SPY beta because their factor is *independent* of broad market. The cohort identity is precisely what makes the basket distinct. Mag 7's failure mode is the inverse — high QQQ beta because Mag 7 IS QQQ, no separate factor.

---

## Per-cohort summary cards

### [[Sectors/WFE|WFE quartet]] (N=4, intra-corr 0.804)

The structural ceiling. Four oligopolists (ASML, AMAT, KLAC, LRCX) serving the same 3-4 leading-edge foundry customers on the same capex cycle. Constraints aren't replicable elsewhere in the vault. Use as the upper-bound reference — no thematic-basket cluster should be expected to reach 0.80+ intra-correlation because the constraint structure isn't replicable.

### [[Sectors/Korea Memory|Korea Memory]] (N=2, intra-corr 0.756)

Samsung + SK Hynix. Pair-only cohort — N=2 diagnostics are necessarily limited (no PC2/PC3 sub-structure, hierarchical clustering trivially groups the pair). The 0.756 reading is meaningful directionally but should be weighted appropriately given the small N.

### [[Sectors/US Memory|US Memory]] (N=3, intra-corr 0.696)

MU, SNDK, WDC. Tight cyclical memory cluster. Strong basic validation but no advanced patterns documented yet.

### [[Sectors/Crypto-to-AI|Crypto-to-AI]] (N=7, intra-corr 0.691)

The TIGHTEST N=7 cohort. Bitcoin miners pivoting to AI/HPC hosting. PC2 cleanly separates pure miners (MARA, CLSK, RIOT) from AI-pivot names (CORZ, HUT, WULF, IREN). IREN is the Swiss-Army-knife name. Cohort stable across 3Y/2Y/1Y/YTD (no regime shift). Identity formed in late 2023 with the AI capex flood and has been durable since.

### [[Space pure-plays]] (N=7, intra-corr 0.624)

THE CANONICAL REFERENCE for the framework. 19 analytical sections documenting basic validation + stability + the four follow-on patterns + cross-cohort comparison. Highest cohort-specific factor share (59.6%). Underwent a regime shift in Nov 2025 (PC2 collapsed from 21% to 8%, intra-corr jumped from 0.466 to 0.656). PL is the Swiss-Army-knife name.

### [[Sectors/AI Compute|AI Compute]] (N=3, intra-corr 0.600)

TSM + NVDA + AMD. Canonical AI trade but only N=3. Moderate cluster cohesion. Less coherent than Space pure-plays despite the "AI trade" framing — same trade-name doesn't mean same factor structure.

### [[Concepts/Defense primes basket|Defense primes 6-core]] (N=6, intra-corr 0.556)

LMT + RTX + NOC + GD + HII + LHX. 7-name variant (with LDOS) only partially validates; 6-name core is the clean cluster. PC2 isolates HII (single naval shipbuilder, no aerospace exposure) — single-outlier pattern, unlike the balanced 2-sleeve splits of other validated cohorts. RTX is the Swiss-Army-knife name. SPY beta -0.52 (controlling for ITA) — most insulated from broad market of any tested cohort.

### [[Concepts/Mag 7 cluster|Mag 7]] (N=7, intra-corr 0.316) — FALSIFIED

AAPL, MSFT, GOOGL, AMZN, META, NVDA, TSLA. Below all three falsification thresholds: intra-corr below 0.50, PC1 below 50%, negative intra-advantage vs ETFs (-0.215). Essentially leveraged QQQ (R² 85.4% to broad benchmarks, only 14.6% specific factor). Cohort is loosening over time (0.47 → 0.32 over 3Y → YTD). Canonical reference for "what falsification looks like."

### [[Sectors/UAS defense micro-cluster|UAS pair]] (N=2, intra-corr 0.638)

KTOS + AVAV. Real micro-cluster too small to be a full cohort. Adding any of 6 tested defense-tech expansion candidates (MRCY, BWXT, HEI, etc.) loosens the cluster rather than tightening. Standalone 2-name pair pending future expansion candidates (Karman Holdings KRMN, Anduril when public).

### [[Concepts/Boutique advisory consolidation|Boutique advisory consolidation]] (N=6, May 2025)

PWP, LAZ, EVR, MC, HLI, PJT. Older basic-validation example using non-matched methodology (May 2025 published 0.73 intra-corr). The simpler single-page write-up format that pre-dates the [[Space pure-plays]] full reference treatment. Re-run with matched methodology pending — would slot into the validated band but exact placement TBD.

---

## Methodology notes

### Matched parameters

All cohorts re-run May 11 2026 with identical parameters for cross-cohort comparability:

- Window: 1-year daily returns through 2026-05-07
- Threshold: 0.5 for hierarchical clustering distance cut
- PCA: scikit-learn implementation, all components
- Factor decomposition: linear regression against relevant broad-market + thematic benchmarks
- Subset optimization: enumerate all C(N,2) pairs, rank by three objectives separately

Configs in `scripts/cluster_configs/`: `wfe_quartet.yaml`, `korea_memory.yaml`, `us_memory.yaml`, `crypto_to_ai.yaml`, `rklb.yaml`, `ai_compute.yaml`, `defense_primes.yaml`, `defense_primes_core.yaml`, `mag7.yaml`.

Cohort-specific full-analysis scripts: `mag7_full_analysis.py`, `crypto_to_ai_full_analysis.py`, `defense_primes_full_analysis.py`. Each runs stability + PC2/PC3 + factor decomposition + subset optimization + complement test in one pass.

### Verdict thresholds (per `docs/cluster-validation.md`)

| Diagnostic | Validated | Partial / Weak | Falsified |
|---|---|---|---|
| Intra-cluster correlation (avg) | ≥ 0.70 strong, 0.50-0.70 moderate | <0.50 (above 0.40) | <0.40 OR negative intra-advantage vs ETF |
| PC1 explained variance | ≥ 70% strong | 50-70% | <50% |
| Hierarchical clustering at 0.5 | Returns ≥ candidate cohort | Mixed: partial groupings | Singletons / mass-cluster with benchmarks |
| Cluster vs ETF intra-advantage | Positive (>+0.10 typical) | +0.00 to +0.10 | Negative |

Multi-dimensional verdict: a cohort passes all four for "validated," fails one or two for "partial," fails three or four for "falsified."

---

## Open questions / future cohort work

1. Boutique advisory consolidation re-run — older methodology, should be re-run with matched parameters for direct cross-cohort comparison.
2. Hyperscalers (MSFT, GOOGL, AMZN, META) — config exists (`hyperscalers.yaml`); per the Mag 7 note, an earlier hyperscaler test showed intra-corr 0.29 (falsified). Matched-methodology re-run would confirm.
3. Card networks (V, MA, AXP, DFS) — config exists (`card_networks.yaml`); would be a small but clean test.
4. Insurance brokers (AON, AJG, BRO, MMC, WTW) — config exists.
5. Mega banks (JPM, BAC, WFC, C, GS, MS) — config exists.
6. Payments — config exists.
7. Foundry — config exists.
8. AI distillation wars — not yet tested as a cohort.
9. Brazilian banks (ITUB, BBD, NU) — could be useful for cross-vault analysis.
10. Chinese internet (BABA, JD, PDD, BIDU) — high-vol cohort like crypto miners; would test the framework outside US markets.

Each would extend the cross-cohort taxonomy. The framework is now tested on 8+ cohorts and reproduces interpretable structural patterns reliably; additional cohorts would broaden the empirical base.

---

## Implications for trade construction

Based on the structural patterns above, the right expression of a cluster thesis depends on what the user wants:

| Goal | Expression | Example (Space pure-plays) |
|---|---|---|
| Maximum factor exposure with minimum names | Factor-tracking pair from subset optimization | LUNR + BKSY (0.94 tracking corr) |
| Maximum Sharpe ratio on the thesis | Sharpe-optimal pair (usually includes Swiss-Army-knife name) | RKLB + PL (Sharpe 2.03) |
| Maximum cumulative return | Return-maximizing pair (high-return names) | LUNR + PL (+254%) |
| Cleanest factor isolation (full basket) | Equal-weighted basket of all validated members | All 7 names |
| Hedge against the basket | Long benchmarks / Short basket pair | Long QQQ / Short Mag 7 (won't work because Mag 7 IS QQQ) |
| Pair-trade within cohort | Long PC2-positive sleeve / Short PC2-negative sleeve | Long data sleeve / Short hardware sleeve (Space pure-plays) |

The objective decomposition is the most consistently-useful pattern from this session. Future cohort analyses should explicitly enumerate all four (factor-tracking, Sharpe, return-max, complement) before recommending a position.

---

## Related

### Canonical references
- [[Space pure-plays]] — 19-section worked example, all advanced patterns documented
- [[Concepts/Mag 7 cluster|Mag 7 cluster]] — canonical falsified-cluster example
- `docs/cluster-validation.md` — framework standard procedure

### Cohort notes referenced in this taxonomy
- [[Sectors/WFE|WFE]]
- [[Sectors/Korea Memory|Korea Memory]]
- [[Sectors/US Memory|US Memory]]
- [[Sectors/Crypto-to-AI|Crypto-to-AI]]
- [[Sectors/AI Compute|AI Compute]]
- [[Concepts/Defense primes basket|Defense primes basket]]
- [[Sectors/UAS defense micro-cluster|UAS defense micro-cluster]]
- [[Concepts/Boutique advisory consolidation|Boutique advisory consolidation]]

### Scripts
- `scripts/cluster_analysis.py` — basic validation
- `scripts/cluster_stability_check.py` — multi-window stability
- `scripts/cluster_deep_dive.py` — factor decomposition + PC2 + missing-name screen
- `scripts/cluster_subset_optimization.py` — optimal 2- and 3-name subsets
- `scripts/cohort_extras.py` — vol regime + drawdown
- `scripts/cohort_regime_and_events.py` — pre/post regime + event study
- `scripts/cohort_subset_robustness.py` — rolling robustness + complement
- `scripts/cohort_pc3_and_rates.py` — PC3 + rate sensitivity
- `scripts/may8_factor_decomposition.py` — single-day event study
- `scripts/chart_pc1_component.py` — PC1 factor index charts
- Cohort-specific full-analysis scripts: `mag7_full_analysis.py`, `crypto_to_ai_full_analysis.py`, `defense_primes_full_analysis.py`

*Created 2026-05-11 — synthesizing findings from 8-cohort framework application during May 10-11 sessions.*
