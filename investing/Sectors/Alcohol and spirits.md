---
aliases: [Alcohol and spirits, Alcoholic beverages, Beer wine and spirits, Drinks cohort, Alcohol cohort, Spirits and beer]
tags: [sector, consumer-staples, alcohol, beverages, cluster-validation]
---

# Alcohol and spirits

> [!warning] Cluster status: NOT a distinct factor — real co-movement, but a loose, fragmented cohort that splits by category (beer vs spirits); below the cohesion floor; factor structure unstable (Jun 2026)
> The alcohol & spirits names ([[Constellation Brands|STZ]]/[[Brown-Forman|BF-B]]/[[Molson Coors|TAP]]/[[Boston Beer|SAM]]/[[Diageo|DEO]]) do not hold as one factor. Intra-corr is 0.483 — BELOW the 0.50 cohesion floor (weekly 0.462), PC1 only 58.9% with 26% of the variance in PC2+PC3 (the category splits). The cohort beats all three nulls (independence 0.0001, random-basket 0.0006, vol-matched 0.0012), so the co-movement is real and exceeds a same-volatility random staples basket — this is NOT pure dispersion. But at the standard 0.50 cut the cohort does not cohere: it splits into beer {[[Molson Coors|TAP]]+[[Boston Beer|SAM]], the tightest pair 0.60} and spirits {[[Constellation Brands|STZ]]+[[Brown-Forman|BF-B]], join 0.456}, with [[Diageo|DEO]] a near-singleton; the names fuse into one group only ABOVE the cut (the four US/spirits names at 0.526, DEO at 0.551). The stable clean band is [0.60–0.65], width 0.05, entirely above the floor, and the 2Y holdout — though labelled "STABLE 0.91" on the intra level — carries a NEGATIVE PC1-loadings correlation (−0.24), meaning the factor structure inverts between regimes (which names lead shifts). Yet it is NOT simply inside the staples ETF either: the alcohol names separate from the staples cluster {[[Coca-Cola|KO]]/[[XLP]]/[[KXI]]} at ~0.65 and carry a positive +0.088 intra-advantage over [[XLP]]/[[KXI]] (+0.224 over KO, +0.435 over SPY). The verdict is the campaign's cleanest "fragmented theme": a real consumer category the market prices as a beer story and a spirits story, not one tradeable factor. See below.

The recognizable category that does not trade as a monolith. The premise was a consumer-staples cohesion test — do the alcohol names form one "drinks" factor the way the [[Tobacco majors basket|tobacco majors]] do, or do they fragment the way apparel and other consumer categories do? The answer is the fragmented shape, and decisively so: alcohol is the only cohort this session whose intra-correlation sits below the 0.50 floor. There is a genuine common mode — the names co-move more than random staples baskets, and they separate cleanly from generic staples — but it is diluted by category-specific drivers that hit the members unevenly: the [[GLP-1 receptor agonists|GLP-1]]/moderation worry presses hardest on spirits, the secular volume decline on mass-market beer, premiumization and FX/tariffs on the global names. Beer and spirits each cohere as a pair; "alcohol" as a whole does not.

## Sector performance

![[alcohol-performance.png]]
*Normalized total return since Jan 2023, the five alcohol names vs consumer staples [[XLP]]. Defensive and staples-adjacent, but the beer ([[Molson Coors\|TAP]]/[[Boston Beer\|SAM]]) and spirits ([[Constellation Brands\|STZ]]/[[Brown-Forman\|BF-B]]/[[Diageo\|DEO]]) wings visibly diverge — the fragmentation behind the failed-factor verdict.*

## Cluster validation

The candidate cohort is five alcoholic-beverage makers — [[Constellation Brands|STZ]] (beer/wine/spirits), [[Brown-Forman|BF-B]] (premium spirits), [[Molson Coors|TAP]] (mass beer), [[Boston Beer|SAM]] (craft beer/FMB), [[Diageo|DEO]] (global spirits) — tested against the consumer-staples ETFs ([[XLP]] US, [[KXI]] global), non-alcoholic beverages ([[Coca-Cola|KO]]), and the market (SPY). 1Y window through 2026-06-18 (198 obs), threshold 0.5. [[Diageo|DEO]] is a London-listed ADR (some async-close noise; the weekly cross-check controls for it). Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.483 [0.366–0.597] | LOOSE — below the 0.50 floor; weekly 0.462 |
| PC1 explained variance | 58.9% | Weak single factor; 26% in PC2+PC3 (category splits) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0006 | Beats a random 5-pick from the staples universe — real, not dispersion |
| Vol-matched null p (10k) | 0.0012 | Exceeds same-vol random baskets — not just shared staples beta |
| Holdout (2Y split) | "STABLE" 0.91 on level, but loadings-corr −0.24 | train 0.529 → test 0.483; factor STRUCTURE inverts between regimes |
| Threshold stable width | 0.05 [0.60–0.65] | NARROW and ABOVE the floor — the cohort is one clean group only when the cut is loosened past 0.50 |
| Intra-adv vs staples (XLP/KXI) | +0.088 | Positive — NOT simply inside the staples ETF |
| Intra-adv vs beverages (KO) | +0.224 | Distinct from non-alcoholic beverages |
| Intra-adv vs market (SPY) | +0.435 | Defensive — SPY corr 0.049, near-zero market beta |

Config: `scripts/cluster_configs/alcohol.yaml`; registry row 2026-06-21.

### Boundary — the cohort shatters at the standard cut

![[alcohol-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The alcohol names (right) split into beer {[[Molson Coors|TAP]]+[[Boston Beer|SAM]]} and spirits {[[Constellation Brands|STZ]]+[[Brown-Forman|BF-B]]}, with [[Diageo|DEO]] a near-singleton — three clusters, not one. They separate from the staples block {[[Coca-Cola|KO]]/[[XLP]]/[[KXI]]} only at ~0.65, and [[SPY]] sits apart (defensive). So alcohol is neither one factor (it fragments) nor simply inside the staples ETF (it separates from XLP/KXI).*

The threshold scan returns a stable clean band only at [0.60–0.65] (width 0.05) — entirely above the 0.50 floor, which is the diagnostic signature of a cohort that is not one cluster at the standard cut:

| Threshold | State of the cohort | Read |
|---|---|---|
| 0.50 | three sub-clusters (beer / spirits / DEO) | does NOT cohere at the standard cut |
| 0.55 | the four US/spirits names fuse; DEO still out | partial |
| 0.60–0.65 | all five together, no controls mixed in | the only clean band — but loose |
| 0.65+ | staples (KO/XLP/KXI) merge in | the broad staples complex |

A stable band that exists only above 0.50 means the names are one group only when you accept loose (>0.50 distance) linkage. Contrast the distinct cohorts, whose bands sit well below 0.50.

### Topology — a beer pair, a spirits pair, and a global outlier

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | TAP + SAM | 0.403 | the beer pair — the tightest link (corr 0.60) |
| 2 | STZ + BF-B | 0.456 | the spirits/wine pair (corr 0.54) |
| 3 | (TAP+SAM) + (STZ+BF-B) | 0.526 | beer and spirits fuse — but only above the 0.50 cut |
| 4 | DEO + the four | 0.551 | [[Diageo\|DEO]] (global spirits) joins last, loosest |

The cohort does not close until 0.551 — every join except the beer pair is at or above the 0.50 floor. [[Diageo|DEO]] is the outlier (corr 0.37 to both STZ and SAM), a London-listed global-spirits name that moves on its own FX/emerging-market story. PC1 explains only 58.9%.

### PC1 index weights — an even but weak common mode

![[alcohol-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains only 58.9% (a coherent single factor runs ~65–80%) with a meaningful 26% in PC2+PC3 — that secondary variance is the beer/spirits/global category split. Loadings are fairly even (0.42–0.49), so PC1 is a genuine "alcohol" mode, just a weak one.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| STZ | 0.418 | 18.73% | 30.34% | 20.56% |
| BF-B | 0.476 | 21.31% | 40.37% | 17.58% |
| TAP | 0.486 | 21.76% | 27.65% | 26.22% |
| SAM | 0.430 | 19.26% | 37.05% | 17.31% |
| DEO | 0.423 | 18.94% | 34.41% | 18.33% |

Loadings are even but PC1 is weak (58.9%): there is a common alcohol mode, but the high vols (28–40%) and the large PC2+PC3 share mean each name carries a lot of idiosyncratic, category-specific movement. The negative PC1-loadings correlation across the 2Y holdout (−0.24) — like [[Fertilizer producers|fertilizers']] −0.37 — confirms the structure is unstable: which names anchor the factor changes between regimes, so the automated "STABLE 0.91" intra-level label overstates durability.

### Distinctness — real, but a category not a factor

![[alcohol-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A warm-ish but uneven block (0.37–0.60): the TAP/SAM beer corner and the STZ/BF-B spirits corner are warmest; DEO is cool against STZ and SAM. The staples ETFs and KO are warm but separable; SPY essentially uncorrelated.*

The intra-advantage numbers place it: +0.088 over the staples ETFs ([[XLP]]/[[KXI]]) — positive, so the alcohol names are not simply staples (they separate from the staples cluster at 0.65); +0.224 over non-alcoholic beverages ([[Coca-Cola|KO]]); and +0.435 over the market (SPY corr 0.049 — alcohol is defensive, near-zero market beta). So there is a real, distinct-from-staples consumer-category mode. What it lacks is internal cohesion: at 0.483 it is below the floor, and it fragments into beer and spirits. It is the inverse of the campaign's distinct factors, which are tight (intra >0.55) AND driven by something no ETF prices. Alcohol clears the second test (not inside XLP) but fails the first (not tight enough to be a factor). And there is no pure alcohol ETF, so there is nothing to "own" — the category is best expressed through the individual names or the sub-pairs (beer, spirits).

### Historical tightness evolution — chronically loose, regime-dependent

![[alcohol-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Chronically loose and oscillating — 0.30–0.55, never durably tight, with no sustained period above 0.55 (latest 90-day 0.451). Tightens modestly in stress years (2023, 2025) and loosens otherwise; the opposite of a durable factor.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.301 | 45.0% |
| 2022 | 0.421 | 53.8% |
| 2023 | 0.549 | 64.4% |
| 2024 | 0.410 | 54.2% |
| 2025 | 0.542 | 63.6% |
| 2026 | 0.468 | 57.8% |

*Loose every year — the cohort peaks at 0.55 (2023, 2025) and falls back to 0.30–0.42 otherwise, averaging well below the 0.50 floor over the full period. The latest 90-day reading (0.451, core 0.484, satellite 0.402) confirms the fragmentation is current, not a one-off. A durable factor holds together across regimes; alcohol cohesion comes and goes with the macro/defensive cycle.*

## Where this sits in the campaign

Alcohol is the "fragmented theme" pole of the campaign's failure modes — the mirror image of cohorts that fail by collapsing into an ETF:

- The [[Tobacco majors basket|tobacco majors]] are the consumer-staples cohort that DOES cohere (a tight, concentrated oligopoly) — the contrast that motivated this test. Alcohol has far more players, more category fragmentation, and no equivalent pricing-power oligopoly, so it does not hold.
- [[Fertilizer producers]] are the closest analog: loose, splits (a defector), negative PC1-loadings holdout. Alcohol is looser still (below the floor) and splits by category rather than via one defector.
- [[Silver equity beta]] (same day) is the opposite failure: too tight, fully inside an ETF. Alcohol is too loose to be a factor; silver is too coherent to be distinct from its ETF. Both are Tier 3, for inverse reasons.

## Related

- [[Constellation Brands]], [[Brown-Forman]], [[Molson Coors]], [[Boston Beer]], [[Diageo]] — the cohort members (beer: TAP/SAM; spirits/wine: STZ/BF-B/DEO)
- [[Tobacco majors basket]] — the consumer-staples cohort that coheres; the motivating contrast
- [[Fertilizer producers]] — the closest fragmented-cohort analog (splits, unstable structure)
- [[XLP]], [[KXI]] — consumer-staples ETFs (alcohol separates from these at 0.65); [[Coca-Cola|KO]] — non-alcoholic beverages control
- [[GLP-1 receptor agonists]] — the moderation/demand worry that hits spirits hardest, one driver of the category split
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-21. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/alcohol.yaml`; registry row 2026-06-21. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
