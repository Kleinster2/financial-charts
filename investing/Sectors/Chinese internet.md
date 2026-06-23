---
aliases: [Chinese internet, Chinese internet platforms, China internet ADRs, China platform ADRs, Chinese internet cohort]
tags: [sector, technology, china, internet, e-commerce, cluster-validation]
---

# Chinese internet

> [!warning] Cluster status: validated cohesion but ETF-replicable (= [[KWEB]]) — the US-listed Chinese internet ADRs are one loose, regime-dependent "China-risk" factor the China-internet ETF already prices; distinct from their US business-model twins but NOT from [[KWEB]] (Jun 2026)
> The five [[China]] ADRs ([[Alibaba|BABA]]/[[JD.com|JD]]/[[Pinduoduo|PDD]]/[[Baidu|BIDU]]/[[NetEase|NTES]]) cohere — they beat the random-basket null (p 0.0007) and the vol-matched null (p 0.0004) at the floor, and the factor structure is durable (holdout STABLE 0.85, PC1-loadings corr 0.93) — but the cohesion is loose (intra 0.49–0.51, right at the 0.50 floor; weekly only 0.29) and entirely captured by [[KWEB]]: the cohort correlates MORE with the China-internet ETF (0.72) than with itself (0.51), a −0.21 intra-advantage, and [[KWEB]]/[[FXI]]/[[CQQQ]] sit INSIDE the cohort cluster from threshold 0.30 (zero clean band). The one genuinely distinct finding is jurisdiction over business model: the cohort does NOT trade with its US twins [[Amazon|AMZN]]/[[Alphabet|GOOGL]]/[[Meta|META]] (corr 0.21, +0.26 intra-advantage) — but that China-vs-US split is exactly what [[KWEB]] is built on. The first sector-scale test of the [[Vault cluster taxonomy|cluster framework]] outside US-listed cohorts, and it confirms the law holds abroad: a country-sector ADR cohort = its country-sector ETF. See below.

The label that confuses jurisdiction with business model. [[Alibaba|BABA]] (e-commerce + cloud/AI), [[JD.com|JD]] (e-commerce/logistics), [[Pinduoduo|PDD]] (discount e-commerce + Temu/global), [[Baidu|BIDU]] (search + AI + robotaxi), and [[NetEase|NTES]] (gaming) are five different businesses. The market prices them as one "China internet" trade not because the businesses move together but because the dominant shared driver is exogenous and political — [[China platform regulation]], the ADR-delisting threat ([[Chinese Depositary Receipts|HFCAA]]), stimulus on/off, and US–China tension ([[US-China decoupling]]) — a country-risk factor stronger than any of the underlying demand stories. [[KWEB]] (the $7.5B KraneShares China-internet ETF, 34 holdings, mega-cap-platform-weighted) holds these exact names and IS that factor. When China risk dominates — the 2022 crackdown/delisting panic — the cohort fused into one trade (intra 0.80); as the shock faded the names re-diverged onto their own stories ([[Pinduoduo|PDD]]/Temu global, [[Baidu|BIDU]]/AI-robotaxi, [[Alibaba|BABA]]/cloud-AI rerating), pulling cohesion back to the floor.

## Sector performance

![[china-internet-performance.png]]
*Normalized total return since Jan 2021 vs the China-internet ETF [[KWEB]] (cyan). The regime arc made visible: all six crash together through 2021–22 (the [[China platform regulation|crackdown]] + delisting panic — the cohesion peak), then disperse in the recovery. [[NetEase|NTES]] (gaming, purple) decouples to the upside; the e-commerce/search core ([[Alibaba|BABA]]/[[JD.com|JD]]/[[Pinduoduo|PDD]]/[[Baidu|BIDU]]) clusters tightly around [[KWEB]], which threads right through the middle — the ETF IS their average. Cumulative paths diverge while daily co-movement stays high and ETF-priced: that gap is the ETF-replicable verdict.*

## Cluster validation

The candidate cohort is the five US-listed Chinese internet ADRs — [[Alibaba|BABA]], [[JD.com|JD]], [[Pinduoduo|PDD]], [[Baidu|BIDU]], [[NetEase|NTES]] — tested against the China-equity ETFs ([[KWEB]] the sector ETF, [[CQQQ]] China-tech, [[FXI]] China-large-cap), the US internet majors ([[Amazon|AMZN]]/[[Alphabet|GOOGL]]/[[Meta|META]] — the key distinctness control: same business models, different jurisdiction), and the market ([[SPY]]/[[QQQ]]/[[VWO]]). 1Y window through 2026-06-18 (159 obs on the full control set; 251 obs on the clean candidate-only window); threshold 0.5. The first framework test outside US-listed-only cohorts at the candidate level. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.491 (159-obs) / 0.507 (clean 251-obs) | At the 0.50 floor; weekly only 0.291 — looser still |
| Intra-corr, core-4 ex-[[NetEase\|NTES]] | 0.562 | [[NetEase\|NTES]] (gaming) a mild drag — but still = [[KWEB]] |
| PC1 explained variance | 59.9% | Moderate; 27% in PC2+PC3 (idiosyncratic) |
| Independence null p (10k) | 0.0001 | Series co-move (necessary, not sufficient) |
| Random-basket null p (10k) | 0.0007 (intra), 0.0009 (PC1) | Real cohesion — beats a random 5-pick |
| Vol-matched null p (10k) | 0.0004 (intra), 0.0005 (PC1) | Not just shared high-vol beta — a real factor |
| Holdout (2Y split) | STABLE 0.85, loadings corr 0.93 | Durable factor structure across regimes |
| Threshold stable width | 0.00 (none) | [[KWEB]]/[[FXI]]/[[CQQQ]] contaminate from 0.30 |
| Intra-adv vs sector ETF ([[KWEB]]) | −0.209 | NEGATIVE — the cohort IS the ETF |
| Intra-adv vs China-ETF avg | −0.148 | = the China complex |
| Intra-adv vs US internet (AMZN/GOOGL/META) | +0.258 | Jurisdiction beats business model |
| Intra-adv vs market ([[SPY]]) | +0.151 | Distinct from US market beta |

Config: `scripts/cluster_configs/china_internet.yaml`; registry row 2026-06-22 (definition date 2026-06-12).

### Boundary — the China ETFs are inside the cluster

![[china-internet-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The decisive picture: [[KWEB]]+[[FXI]] are the tightest pair in the entire tree (join 0.08), [[CQQQ]] joins them, and the candidates [[Alibaba|BABA]]/[[Baidu|BIDU]]/[[JD.com|JD]]/[[Pinduoduo|PDD]] hang directly off that China-ETF core (orange) — the cohort does not form its own cluster, it forms one WITH the ETFs at the center. The top split (gray, 0.64) is China-complex (left) vs US-complex (right): the US internet majors [[Meta|META]]/[[Alphabet|GOOGL]]/[[Amazon|AMZN]] sit with the US-market ETFs (green), nowhere near their Chinese business-model twins. [[NetEase|NTES]] (gaming) decouples, joining only at 0.53 — above the cut.*

The threshold scan returns no clean band — the cohort never forms an uncontaminated single cluster at any cut, because [[KWEB]]/[[FXI]]/[[CQQQ]] join it from threshold 0.30 (the most complete ETF-embedding signature: the sector ETF is inside the cluster almost everywhere). That, with the −0.21 intra-advantage over [[KWEB]], is the ETF-replicable verdict: there is no Chinese-internet basket worth owning over the ETF, because the ETF holds the names and prices the same China-risk factor.

### Topology — a tight triad, a Temu satellite, a gaming decoupler

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | BABA + JD | 0.275 | the megacap e-commerce pair — the tight core (corr 0.73) |
| 2 | BIDU + (BABA+JD) | 0.383 | search/AI joins the old-guard triad (corr ~0.62) |
| 3 | PDD + core | 0.539 | [[Pinduoduo\|PDD]] (Temu/global) joins above the cut — the divergent grower |
| 4 | NTES + core | 0.608 | [[NetEase\|NTES]] (gaming) joins last, far out — the decoupler |

The clean structure is a tight "old guard" triad — [[Alibaba|BABA]]+[[JD.com|JD]]+[[Baidu|BIDU]] (0.59–0.73), the megacap e-commerce/search ADRs that anchor [[KWEB]] — with [[Pinduoduo|PDD]] a looser satellite (0.43–0.52; its Temu/global-growth story and lighter China-onshore exposure pull it away) and [[NetEase|NTES]] the decoupler (0.36–0.46; gaming is a different, more defensive end-market, the upside breakout in the performance chart). Dropping [[NetEase|NTES]] lifts intra 0.507→0.562, but the core-4 is still −0.18 vs [[KWEB]] — unlike the [[Hospital operators|ex-CYH]] or [[IT services|ex-Wipro]] cases, removing the outlier does not rescue distinctness here, because the ETF captures even the tight core. No sub-cohort to carve out.

### PC1 index weights — even loadings, very high vol

![[china-internet-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 59.9% — a single "China internet" factor, but a loose one (27% sits in PC2+PC3, the idiosyncratic AI/e-commerce/gaming stories). Loadings are fairly even (0.37–0.50), [[NetEase|NTES]] lowest. All five carry extreme annualized vol (30–49%) — speculative, headline-driven ADRs.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| BABA | 0.504 | 22.68% | 43.04% | 19.50% |
| JD | 0.484 | 21.80% | 32.37% | 24.91% |
| PDD | 0.401 | 18.04% | 34.35% | 19.43% |
| BIDU | 0.467 | 21.01% | 49.33% | 15.76% |
| NTES | 0.366 | 16.48% | 29.88% | 20.40% |

### Distinctness — = KWEB, but NOT the US twins

![[china-internet-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The [[Alibaba|BABA]]/[[JD.com|JD]]/[[Baidu|BIDU]] triad runs warm (0.59–0.73); the candidates are about as warm to [[KWEB]]/[[FXI]]/[[CQQQ]] as to each other (the ETF-embedding), and cold to [[Amazon|AMZN]]/[[Alphabet|GOOGL]]/[[Meta|META]] (~0.21).*

Two distinctness numbers, opposite signs, and together they are the whole story. Against the China ETFs the intra-advantage is NEGATIVE (−0.209 vs [[KWEB]], −0.148 vs the China-ETF average): the cohort co-moves with [[KWEB]] more than with itself, so the ETF is the better expression — the country-sector analogue of the [[Vault cluster taxonomy|commodity-beta law]] (miners = the metal; ADRs = the country ETF). Against the US internet majors the intra-advantage is strongly POSITIVE (+0.258): [[Alibaba|BABA]] does not trade with [[Amazon|AMZN]], [[Baidu|BIDU]] does not trade with [[Alphabet|GOOGL]], [[Pinduoduo|PDD]] does not trade with [[Meta|META]] — same business models, but jurisdiction (China policy/ADR risk) beats business model. That is a real and interesting structural fact, but it is not an ownable edge: [[KWEB]] already isolates exactly that China-vs-US factor.

### Historical tightness evolution — a crisis factor that loosened

![[china-internet-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion since 2019. The arc is the verdict's backbone: loose pre-crackdown (0.48–0.58), a brief loosening as the regulatory storm hit unevenly in 2021 (0.44), then a sharp fusion to 0.80 in 2022 — the depths of the [[China platform regulation|crackdown]] and the [[Chinese Depositary Receipts|HFCAA delisting]] panic, when "China risk" swamped every idiosyncratic story — followed by a steady loosening back to the floor (0.49) by 2026 as the shock faded and the names re-diverged.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2019 | 0.475 | 59.0% |
| 2020 | 0.582 | 67.6% |
| 2021 | 0.441 | 55.6% |
| 2022 | 0.804 | 84.4% |
| 2023 | 0.684 | 74.9% |
| 2024 | 0.488 | 60.4% |
| 2025 | 0.528 | 63.6% |
| 2026 | 0.496 | 60.2% |

*The cohesion is regime-dependent in strength: the shared "China-risk" factor is strongest exactly when the political shock is largest (0.80 in 2022) and decays toward the floor when the names are left to their own demand stories. That is the same shock-dependence seen in [[Rare earth equity beta|rare earths]] — except here the factor pre-existed the shock and survives it (durable holdout), it just loosens. The weekly intra-corr (0.29 vs daily 0.49) says even the daily cohesion overstates the underlying weekly co-movement: much of it is shared same-day reaction to China-macro headlines.*

## Where this sits in the campaign

Chinese internet is the campaign's first sector-scale test outside US-listed cohorts, and the result extends the central law abroad rather than breaking it:

- It is Tier 2 — real, durable cohesion (beats all three nulls at the floor, STABLE holdout) but ETF-replicable (= [[KWEB]]). The country-sector analogue of the ETF-embedding majority: a foreign-sector ADR cohort resolves to its foreign-sector ETF the same way US sectors resolve to their sector ETFs ([[Mortgage REITs]] = REM, [[Regional banks]] = KRE, [[Self-storage REITs]] = VNQ).
- The [[Vault cluster taxonomy|index-rule law]] is confirmed from a new angle: [[KWEB]] is ruled by the SAME China-risk factor as its holdings, so the cohort collapses into it — exactly the [[Precious metals royalties|gold-royalties = GDX]] case, not the [[Analog and auto-industrial semiconductors|analog-semis-inside-SMH]] escape (where the ETF is ruled by a different factor).
- The distinctive contribution is the jurisdiction-over-business-model finding (+0.258 vs the US internet majors): a clean demonstration that the cohesion is a country factor, not an industry one. The same five business models, listed in the US, would scatter; listed as China ADRs, they fuse — but into [[KWEB]].

## Related

- [[Alibaba]], [[JD.com]], [[Baidu]], [[Pinduoduo]], [[NetEase]] — the cohort members (BABA/JD/BIDU the tight triad; PDD a Temu satellite; NTES the gaming decoupler)
- [[KWEB]] — the China-internet ETF that holds these names and prices the factor (own this, not the basket); [[CQQQ]], [[FXI]] — the broader China-equity ETFs that also contaminate the cluster
- [[Amazon]], [[Alphabet]], [[Meta]] — the US business-model twins the cohort does NOT trade with (+0.258 — jurisdiction beats business model)
- [[Chinese Depositary Receipts]] — the ADR/HFCAA-delisting structure behind the 2022 cohesion peak; [[US-China decoupling]], [[China special valuation]] — the country-risk drivers
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis; [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-22. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/china_internet.yaml` (definition date 2026-06-12); registry row 2026-06-22. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
