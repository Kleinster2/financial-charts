---
aliases: [ALTM, Alt managers basket, Private credit basket]
tags: [basket/internal, ai, disruption, alt-managers]
---

# Alternative asset managers basket

Alternative asset manager stocks that sold off heavily during the [[Claude Cowork disruption February 2026|SaaSpocalypse]] Wave 1 (Feb 3-5) despite not being intermediaries. The market initially treated them as part of the "AI replaces financial services" trade — indiscriminate selling before sorting intermediaries from asset owners.

They bounced back ~50% of the drop by Feb 10 as the market distinguished originators/asset owners from advisory middlemen. Tracked as a control group against the [[AI financial disintermediation basket|AIFD]] (which stayed down) and the broader software cascade of [[February 2026 AI Disruption Cascade]] (which stayed down worse).

---

## Constituents

Move-weighted from Feb 2-5 Wave 1 selloff. Bigger drop = higher weight.

| Ticker | Company | Weight | Feb 2-5 move |
|--------|---------|--------|--------------|
| ARES | [[Ares Management]] | 27% | -16.8% |
| KKR | [[KKR]] | 21% | -13.3% |
| OWL | [[Blue Owl]] | 21% | -13.3% |
| BX | [[Blackstone]] | 16% | -10.2% |
| APO | [[Apollo]] | 8% | -5.3% |
| BAM | [[Brookfield]] | 7% | -4.1% |

Total: 100% — 6 constituents, move-weighted

### Why track this?

These firms originate and hold assets (direct lending, PE, real estate, infrastructure). There's no advisory layer for AI to disintermediate — they're capital allocators, not distributors. But the Feb 3-5 selloff proves the market can lump them in with genuine intermediaries during panic. If another AI catalyst hits financial services, ALTM will likely sell off again before recovering.

### Excluded

| Ticker | Company | Why excluded |
|--------|---------|-------------|
| MS | [[Morgan Stanley]] | Diversified bank — wealth management diluted by IB/trading (-2.4% on Feb 10 vs pure-plays at -7 to -9%) |
| GS | [[Goldman Sachs]] | Same — alt management is one division among many |
| CG | [[Carlyle]] | Insufficient price data for weighting period |

### Database tickers

```
ARES, KKR, OWL, BX, APO, BAM
```

---

## Index methodology

- Ticker: ALTM
- Weighting: Move-weighted (Feb 2-5 selloff magnitude = weight)
- Base date: Feb 2, 2026 = 100 (last trading day before Wave 1)
- History: July 2021 – present
- Calculation: Price return
- Script: `scripts/create_altm_index.py --store`

---

## Behaviour pattern

| Period | ALTM | AIFD | Software victims | SPY |
|--------|------|------|------------------|-----|
| Wave 1 (Feb 2-5) | -12.5% | ~flat | -18% | -2.6% |
| Wave 2-3 (Feb 9-10) | ~flat | -8% | continued decline | -1% |
| Net (Feb 2-10) | -7% | -8% | -20%+ | -3% |

Pattern: ALTM sells off with the first wave (beta + confusion), then recovers as market sorts real intermediation targets from asset owners. The Week 1 software cohort and AIFD stay down because those are thesis hits, not beta hits.

---

## Tracking thesis

This basket tests:
1. Contagion risk — do alt managers get dragged into future AI disruption selloffs?
2. Recovery speed — how quickly does the market sort originators from intermediaries?
3. Convergence risk — if AI starts replacing capital allocation (not just advisory), ALTM becomes a real target, not just collateral damage

Watch for:
- AI tools entering direct lending, underwriting, deal sourcing
- Alt manager earnings mentioning AI fee pressure
- Correlation between ALTM and AIFD on future AI catalysts — if it stays high, the market isn't differentiating

---

## Cluster validation — statistical analysis (May 2026)

The ALTM basket was originally constructed from a single-event catalyst (Feb 2-5 2026 SaaSpocalypse Wave 1). Cluster validation tests whether the six names continue to behave as a structural cluster on a 1-year window, distinct from adjacent-sector controls. Script: `scripts/cluster_analysis.py --config scripts/cluster_configs/altm.yaml`. Full procedure in `docs/cluster-validation.md`.

**Result: validated.** ALTM is a tighter cluster than the boutique advisory cohort — intra-corr 0.76 (vs 0.73 for boutique), PC1 80.1% explained variance (vs 77.5%). Hierarchical clustering at 0.4 threshold returns exactly the six basket names without prompting.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | **0.761** (range 0.68-0.85) | Strong cohesion; tighter than boutique advisory |
| Tightest pair | KKR-BX = 0.85 | The two largest publicly-listed alts trade as twins |
| Loosest pair | APO-BAM = 0.68 | Still well above any inter-group benchmark |
| Hierarchical clustering at 0.4 | All 6 merge in single cluster | Boundary confirmed — no extras pulled in, no candidates dropped |
| PCA — PC1 explained variance | **80.1%** | Single dominant factor; equal-weighted basket = factor |
| PC1 loadings | 0.39-0.42 (all positive) | Near-equal loading; no within-cluster outliers |

### Group-pair correlations (cluster vs neighbors)

| Group pair | Avg pairwise corr | Cluster's intra-advantage |
|---|---|---|
| Cluster (intra) | 0.761 | — |
| Cluster vs traditional asset mgrs (BLK, TROW, BEN) | 0.576 | +0.184 |
| Cluster vs boutique advisory (PWP, EVR, LAZ, MC) | 0.566 | +0.195 |
| Cluster vs broad financials ETFs (XLF, SPY) | 0.558 | +0.203 |
| Cluster vs bulge brackets (GS, MS, JPM) | 0.447 | +0.314 |
| Cluster vs REIT proxies (XLRE, VNQ) | 0.297 | +0.463 |
| Cluster vs insurance brokers (AON) | 0.136 | +0.625 |

The largest within-financials-complex separation is from bulge brackets (+0.31). This is the most analytically important finding: ALTM trades with a clearly different factor than the integrated banks despite both being financial-services. Insurance brokers (+0.63) and REIT proxies (+0.46) round out the distance hierarchy — the further from "originator-economics business model," the lower the correlation.

### Hierarchical clustering result (threshold 0.4)

![[altm-cluster-dendrogram-1y.png]]

| Cluster | Members |
|---|---|
| **Alt asset managers (ALTM)** | **ARES, KKR, OWL, BX, APO, BAM** |
| REIT proxies | XLRE, VNQ (correlation 0.99 with each other) |
| Broad financials block | BLK, PWP, LAZ, EVR, MC, GS, MS, JPM, XLF, SPY |
| Standalone | AON (insurance broker), TROW, BEN (traditional managers) |

Two notable findings:

- **BLK clusters with broad financials, not ALTM.** Despite being included in `trad_mgr` controls, BlackRock trades more with bulge brackets / XLF / SPY than with the alt managers. Confirms that BLK's passive/index-heavy mix and capital-light business model puts it in a different factor than the alt-manager originate-and-hold model.
- **TROW and BEN are standalones** at the 0.4 threshold — neither clusters with BLK nor ALTM. Traditional active managers face their own structural pressure (passive flows, fee compression) and trade idiosyncratically.

### PCA on the candidate cohort

PC1 = **80.1%** of variance. PC2 = 5.8%. PC3 = 5.1%. The cohort is overwhelmingly single-factor — even more so than boutique advisory (77.5%). Loadings are tight (0.39-0.42, all positive), meaning the equal-weighted basket is essentially the factor itself. Pair-trading any one ALTM name vs the basket isolates ~20% idiosyncratic noise; trading the basket cleanly isolates the alt-manager systematic factor.

### Conclusions

1. **ALTM is real, tight, and stable.** Original basket (constructed from a single event in Feb 2026) holds up as a structural cluster on a full year of post-construction data. PC1 80.1% is among the tightest single-factor cohorts in the vault.
2. **Cluster contains exactly these six names**: ARES, KKR, OWL, BX, APO, BAM. BLK does not belong (passive-heavy mix). Bulge brackets are the most distant within-financials comparator (+0.31 advantage).
3. **The cluster is tradable as a basket.** Equal-weighted ALTM ≈ PC1. Useful for: (a) long basket vs short XLF to isolate alt-manager factor (clean +0.20 spread), (b) event-driven setups when a single alt manager prints — read-through to others is high (avg 0.76 correlation), (c) AI-disruption stress tests — original Feb 3-5 catalyst pattern is mathematically replicable.
4. **The +0.63 separation from insurance brokers** parallels the boutique advisory finding — both clusters are about deal-cycle / origination economics, not generic financial-services beta. AON-type fee businesses operate on a different factor entirely.

---

## Related

- [[AI financial disintermediation basket]] — the real intermediation targets
- [[February 2026 AI Disruption Cascade]] — the broader repricing ALTM was indiscriminately caught in
- [[AI disintermediation]] — thesis driving the advisory-replacement leg
- [[PE software talent drain]] — the deeper reason ALTM sold off: PE portfolio software risk
- [[Alternative asset manager]] — concept note
- [[Alternative Managers]] — sector note
- [[Boutique advisory consolidation]] — adjacent cluster, similarly validated (May 2026)
- [[Claude Cowork disruption February 2026]] — Wave 1 catalyst that hit ALTM
- [[Ares Management]] — highest-weight constituent
- [[KKR]] — second-highest weight
- [[Blackstone]] — largest AUM constituent

*Created 2026-02-11*
*Cluster validation 2026-05-03 — `scripts/cluster_configs/altm.yaml`, intra-corr 0.76, PC1 80.1%, hierarchical clustering at 0.4 returns the 6 candidate names*
