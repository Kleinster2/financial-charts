---
aliases: [Cannabis, Cannabis stocks, Marijuana stocks, Pot stocks, Cannabis equities, Weed stocks]
tags: [sector, cannabis, healthcare, consumer, cluster-validation]
---

# Cannabis

> [!warning] Cluster status: ETF-REPLICABLE — a real co-moving complex, but NOT a distinct ownable factor; it collapses into [[MSOS]] (the AdvisorShares Pure US Cannabis ETF). Own the ETF, not a hand-built basket (Jun 2026)
> The nine listed cannabis names co-move (1Y intra 0.651, PC1 69%) and clear the random-basket null at p 0.0001 — so they are a genuine cluster, not noise. But the intra-advantage is negative against both proxy ETFs: −0.075 vs [[MSOS]] and −0.085 vs [[MJ]], meaning the names track the ETFs (0.726 / 0.736) more tightly than they track each other. The two ETFs are themselves 0.908 correlated, and they contaminate the cohort's cluster at every threshold from 0.20 to 0.70 — there is no boundary that keeps them out. This is the [[Vault cluster taxonomy|index-rule]] same-factor collapse: an ETF that holds the names prices the identical factor, so the basket is redundant. Cannabis joins [[Factory automation]] (= XLI) and [[Infrastructure construction]] (= PAVE) as the campaign's non-distinct cohorts. The jurisdiction split (US multistate operators vs Canadian licensed producers) is visible as sub-structure but does not rise to a factor boundary, because the dominant catalyst — US federal reform — is shared across both. See below.

The same plant, two regulatory worlds, one trade. US multistate operators ([[Green Thumb Industries|GTBIF]], [[Curaleaf|CURLF]], [[Cresco Labs|CRLBF]]) are federally illegal under [[Cannabis rescheduling|Schedule I]], taxed punitively under [[280E]], and locked into state-siloed markets; Canadian licensed producers ([[Canopy Growth|CGC]], [[Tilray|TLRY]], [[Aurora Cannabis|ACB]], [[Cronos|CRON]], [[SNDL]], [[Organigram|OGI]]) operate in a federally legal market. By the campaign's [[Vault cluster taxonomy|jurisdiction-beats-business-model law]], that border should mint two factors. It does not — because the price catalyst that moves the whole complex is the same one: US federal reform (DEA rescheduling, SAFE Banking access). Canadian LPs are owned as call options on US market access, so a US-reform headline lifts Vancouver and Chicago together. The result is a single cannabis beta that both [[MSOS]] and [[MJ]] already price, with the jurisdiction divide surviving only as dendrogram sub-structure.

## Sector performance

![[cannabis-performance.png]]
*Normalized total return since 2023. The US MSOs ([[Green Thumb Industries|GTBIF]], [[Cresco Labs|CRLBF]]) and Canadian LPs ([[Canopy Growth|CGC]], [[Tilray|TLRY]]) move on the same inflections — every name spikes together on the mid-2024 rescheduling optimism and bleeds together through 2025–26 — with the proxy ETFs [[MSOS]] and [[MJ]] sitting inside the cloud rather than apart from it. Jurisdiction shows up as level dispersion ([[Canopy Growth|CGC]] −96%, [[Tilray|TLRY]] −84% vs the MSOs' shallower drawdown), not as a timing split. The names tracking the ETF — instead of diverging from it — is the legible signature of an ETF-replicable cohort.*

## Cluster validation

The candidate cohort is the nine listed cannabis names with usable history — US MSOs [[Green Thumb Industries|GTBIF]], [[Curaleaf|CURLF]], [[Cresco Labs|CRLBF]] and Canadian LPs [[Canopy Growth|CGC]], [[Tilray|TLRY]], [[Aurora Cannabis|ACB]], [[Cronos|CRON]], [[SNDL]], [[Organigram|OGI]] — tested against both proxy ETFs: [[MSOS]] (AdvisorShares Pure US Cannabis, which holds the MSOs via total-return swaps) and [[MJ]] (Amplify Alternative Harvest, historically Canadian-LP-heavy), plus the market ([[SPY]]). 1Y window through 2026-06-23 (200 obs); threshold 0.5. [[Trulieve|TCNNF]] and [[Verano|VRNOF]] are omitted: their OTC listings return only a live quote, no price history, from the data provider. Tickers ingested 2026-06-24. Config: `scripts/cluster_configs/cannabis.yaml`; registry row 2026-06-24. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-corr (1Y) | 0.651 (9-name) | Real co-movement, but see ETF rows |
| Sub-cohort intra-corr | US MSO 0.84 / Canada LP 0.665 / cross 0.607 | Jurisdiction is sub-structure, not a split |
| PC1 explained variance | 69.2% | One cannabis factor |
| Random-basket null p | 0.0001 | Real — 0.65 vs random 9-pick mean 0.16 |
| Intra-adv vs [[MSOS]] (US cannabis ETF) | −0.075 | ETF-replicable — names hug the ETF |
| Intra-adv vs [[MJ]] (global cannabis ETF) | −0.085 | ETF-replicable — same verdict |
| [[MSOS]] ↔ [[MJ]] correlation | 0.908 | The two ETFs are one instrument |
| Threshold stable width | none (0.20–0.70) | No boundary excludes the ETFs |
| Holdout (2Y split) | STRENGTHENING 1.47, loadings-corr −0.19 | Tightening beta, unstable structure |
| Intra-adv vs market ([[SPY]]) | +0.395 | Strongly idiosyncratic vs the market |

### Boundary — the cohort never separates from its ETFs

![[cannabis-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. All nine names plus [[MSOS]] and [[MJ]] collapse into a single cluster; only [[SPY]] stands apart. The threshold scan confirms the cohort never returns as a clean, ETF-free cluster at any cut from 0.20 to 0.70 — [[MSOS]] and [[MJ]] join the names at every level. That inseparability is the structural definition of ETF-replicability.*

The threshold scan returns no stable band: at no cut does the cohort form a clean single cluster uncontaminated by the proxy ETFs. This is the structural opposite of a distinct factor like [[Construction aggregates]] (where the cohort clusters alone and the ETF stays out) and the same signature as [[Factory automation]] (= XLI) and [[Infrastructure construction]] (= PAVE).

### Topology — two jurisdiction sub-clusters that fuse loosely

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | GTBIF + CRLBF | 0.114 | US MSO core ([[Green Thumb Industries\|GTBIF]] + [[Cresco Labs\|CRLBF]], corr 0.89) |
| 2 | CURLF + (GTBIF+CRLBF) | 0.171 | [[Curaleaf\|CURLF]] completes the US MSO trio (sub-intra 0.84) |
| 3 | CGC + ACB | 0.223 | Canadian LP core ([[Canopy Growth\|CGC]] + [[Aurora Cannabis\|ACB]]) |
| 4 | TLRY + [[SNDL]] | 0.246 | second Canadian pair ([[Tilray\|TLRY]] + [[SNDL]]) |
| 5 | (CGC+ACB) + (TLRY+SNDL) | 0.276 | the Canadian LPs fuse (sub-intra 0.665) |
| 6 | CRON + Canada | 0.346 | [[Cronos\|CRON]] (Altria-backed, lower-vol) attaches |
| 7 | US trio + Canada bloc | 0.381 | the two jurisdictions join — looser than within either |
| 8 | OGI + all | 0.430 | [[Organigram\|OGI]] joins last (smallest, idiosyncratic) |

The dendrogram is organized by jurisdiction: the three US MSOs fuse first and tight (0.11–0.17, sub-intra 0.84), the Canadian LPs fuse separately (0.22–0.35, sub-intra 0.665), and the two blocs only merge at 0.381 — a real gap, but not wide enough to split the complex into two factors at any usable threshold. Cross-jurisdiction correlation averages 0.607: the border lowers cohesion without breaking it. The shared US-reform catalyst keeps Vancouver tied to Chicago.

### PC1 index weights

![[cannabis-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 69.2%; loadings are strikingly even (0.30–0.35) across all nine names regardless of jurisdiction — one factor drives the whole complex. The inverse-vol mimic weights tilt toward the lower-vol Canadian names ([[Cronos\|CRON]] 42% vol, [[Aurora Cannabis\|ACB]] 57%) and away from the high-vol MSOs ([[Cresco Labs\|CRLBF]] 140%, [[Curaleaf\|CURLF]] 117%).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| GTBIF | 0.345 | 11.51% | 92.27% | 9.38% |
| CURLF | 0.337 | 11.24% | 116.66% | 7.24% |
| CRLBF | 0.341 | 11.38% | 139.72% | 6.12% |
| CGC | 0.354 | 11.81% | 92.75% | 9.57% |
| TLRY | 0.334 | 11.14% | 101.40% | 8.26% |
| ACB | 0.348 | 11.61% | 57.33% | 15.22% |
| CRON | 0.317 | 10.58% | 42.22% | 18.84% |
| [[SNDL]] | 0.325 | 10.86% | 63.03% | 12.95% |
| OGI | 0.295 | 9.86% | 59.56% | 12.44% |

### Distinctness — the negative intra-advantage

![[cannabis-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The US MSO block runs hot (0.82–0.89); the Canadian LP block is warm (0.62–0.78); the cross-jurisdiction cells are cooler (0.51–0.69) but never cold. No pocket of the matrix is independent — the whole complex is one warm field.*

Cannabis fails the distinctness test on the only metric that matters for ownership: against both ETFs the intra-advantage is negative (−0.075 vs [[MSOS]], −0.085 vs [[MJ]]). The names correlate more tightly with the ETFs than with each other, so a hand-built basket is strictly worse than buying [[MSOS]] — you take more idiosyncratic, single-name (and OTC-liquidity) risk for a less cohesive exposure. The only positive advantage is +0.395 over [[SPY]], which just confirms cannabis is its own beta, not that it is un-indexed. With a liquid ETF holding the exact names, the cohort collapses into it.

### Historical tightness evolution

![[cannabis-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion since 2022 — rising from 0.51 to 0.66 as the sector shrank and consolidated around the same reform-headline beta. The holdout split confirms the tightening (train 0.44 → test 0.65, ratio 1.47) but flags an unstable factor structure (PC1 loadings-corr −0.19 between halves): the names move together more, but the internal weighting reorganized, so this is a consolidating beta rather than a durable, hand-buildable factor.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2022 | 0.513 | 58.1% |
| 2023 | 0.514 | 57.3% |
| 2024 | 0.522 | 57.8% |
| 2025 | 0.594 | 64.2% |
| 2026 | 0.658 | 69.9% |

## Where this sits in the campaign

Cannabis is the campaign's same-product / shared-catalyst falsification of the [[Vault cluster taxonomy|jurisdiction-beats-business-model law]]. The China ADRs separated from their US business-model twins ([[Alibaba]]/[[JD.com]] apart from [[Amazon]]) because the catalyst was jurisdiction-specific — China macro, regulation, and delisting risk that does not touch Seattle. Cannabis is the same plant under opposite federal regimes, which by jurisdiction alone should split harder still; instead it stays one factor, because the dominant price driver — US federal rescheduling and banking access — is shared, and Canadian LPs are held as call options on that same US event. The refinement: it is not jurisdiction that mints a separate factor, it is whether the dominant catalyst is jurisdiction-specific. A shared catalyst re-fuses jurisdictions into one ETF-replicable beta. On the index-rule axis cannabis sits with [[Factory automation]] (= XLI) and [[Infrastructure construction]] (= PAVE): a real cohort that collapses because a liquid ETF prices the same factor — here doubly so, since [[MSOS]] holds the exact MSOs and [[MJ]] the LPs, and the two ETFs are 0.91 correlated. Own [[MSOS]].

## Related

- [[Green Thumb Industries]], [[Curaleaf]], [[Cresco Labs]] — the US MSO core (sub-intra 0.84); [[Trulieve]], [[Verano]] — MSOs omitted for lack of OTC history
- [[Canopy Growth]], [[Tilray]], [[Aurora Cannabis]], [[Cronos]], [[SNDL]], [[Organigram]] — the Canadian LP bloc (sub-intra 0.665)
- [[MSOS]] — the US cannabis ETF the cohort collapses into (own this); [[MJ]] — the global/Canadian-heavy ETF (0.91 correlated to MSOS)
- [[Factory automation]], [[Infrastructure construction]] — the campaign's other ETF-replicable cohorts (= XLI, = PAVE); [[Construction aggregates]], [[Coal miners]] — the distinct-factor contrast
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis and the jurisdiction/catalyst law; [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-24. 1Y daily log returns through 2026-06-23; config `scripts/cluster_configs/cannabis.yaml`; registry row 2026-06-24. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
