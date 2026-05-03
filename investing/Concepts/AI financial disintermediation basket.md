---
aliases: [AIFD, Insurance broker basket, Wealth management disruption basket]
tags: [basket/internal, ai, disruption, insurance, wealth-management]
---

# AI financial disintermediation basket

> [!failure] Cluster status: falsified as single basket — splits into TWO validated sub-clusters (May 2026)
> Intra-cluster correlation only 0.34 across the 10-name combined cohort, PC1 only 43.9% — bimodal. Hierarchical clustering at 0.4 splits AIFD cleanly into [[Insurance brokers basket]] (5 names: WTW, AJG, AON, BRO, MMC) and [[Wealth managers basket]] (3 names: SCHW, RJF, LPLA). Cross-sub-cluster correlation 0.09 — completely uncorrelated despite shared AI-disruption narrative. The Feb 2026 catalyst grouping was a single-event narrative, not a structural cluster. Trade the two sub-baskets separately. See "Cluster validation" section below.

Financial services stocks that correlate on AI capability announcements threatening advisory and intermediation business models. Emerged as a distinct factor during the [[Insurify insurance broker selloff February 2026]] (Feb 9) and [[Altruist wealth management selloff February 2026]] (Feb 10) — the second and third [[AI disintermediation]] shocks after the [[Claude Cowork disruption February 2026|SaaSpocalypse]].

AIFD isolates the advisory-replacement leg of the cascade: human middlemen (insurance brokers, wealth advisors) being pressured by AI comparison and planning tools, as distinct from the product-replacement leg that hit software in Week 1 (SaaS seats → agents). See [[February 2026 AI Disruption Cascade]] for the full sequence.

---

## Constituents

Move-weighted from Feb 9-10 selloff. Bigger drop = higher weight.

### Insurance brokers — Feb 9 Insurify catalyst (58%)

| Ticker | Company | Weight | Feb 9 move |
|--------|---------|--------|------------|
| WTW | [[Willis Towers Watson]] | 15% | -12% |
| AJG | [[Arthur J. Gallagher]] | 12% | -9.9% |
| AON | [[Aon]] | 11% | -9.3% |
| RYAN | [[Ryan Specialty]] | 10% | -8.5% |
| BRO | [[Brown & Brown]] | 7% | -7.8% |
| MMC | [[Marsh McLennan]] | 3% | -6.1% |

### Wealth managers — Feb 10 Altruist catalyst (42%)

| Ticker | Company | Weight | Feb 10 move |
|--------|---------|--------|-------------|
| SCHW | [[Charles Schwab]] | 13% | -8.1% |
| RJF | [[Raymond James]] | 10% | -8.5% |
| LPLA | [[LPL Financial]] | 10% | -8.4% |
| SF | [[Stifel Financial]] | 9% | -7.2% |

Total: 100% — 10 constituents, move-weighted

### Excluded

| Ticker | Company | Why excluded |
|--------|---------|-------------|
| PGR | [[Progressive]] | Insurance carrier, not broker — production layer, not distribution |
| CB | [[Chubb]] | Insurance carrier |
| TRV | [[Travelers]] | Insurance carrier |
| IBKR | [[Interactive Brokers]] | Execution platform, no advisory — immune (+15% YTD) |
| HOOD | [[Robinhood]] | Retail/crypto platform — fell on broader AI fear, not advisory-specific |

Rationale: The basket captures advisory/intermediation exposure specifically. Carriers manufacture the product; execution platforms provide infrastructure. Neither is a middleman. The market confirmed this distinction — carriers fell 1-2% vs. brokers falling 6-12%.

### Database tickers

```
WTW, AJG, AON, RYAN, BRO, MMC, RJF, LPLA, SCHW, SF
```

---

## Index methodology

- Ticker: AIFD
- Weighting: Move-weighted (Feb 9-10 selloff magnitude = weight, with SCHW upweighted for market cap significance)
- Rebalance: Event-driven (re-weight on next major AI disruption catalyst)
- Base date: Feb 7, 2026 = 100 (last trading day before Insurify catalyst)
- History: July 2021 – present (limited by RYAN IPO)
- Calculation: Price return
- Script: `scripts/create_aifd_index.py --store`

---

## Charts

![[aifd-index.png]]
*AIFD basket since Jan 2024. Peaked early 2025 around 112, ground down through H2 2025, then Feb 9-10 catalysts accelerated the decline. Now at ~98 — below the base date.*

### vs the broader software cascade

As of early Feb 2026, AIFD sat at roughly flat relative to its Feb 7 base while the Week 1 software victims (Intuit, ServiceNow, Salesforce, Thomson Reuters) were already down 20-40%. Financial services intermediation was earlier in the repricing cycle than software. Open question: does AIFD follow the software trajectory, or do licensing moats, fiduciary duties, and long enterprise relationships create a floor that software lacked?

---

## AIFD vs the software cascade: structural differences

| Dimension | Software (Week 1 victims) | AIFD (financial services) |
|-----------|---------------------------|---------------------------|
| Revenue model | Per-seat subscription | Commission/AUM fees |
| Switching costs | Low-medium | High (relationships, contracts) |
| Regulatory moat | Low | High (licensing, fiduciary duties) |
| AI replacement type | Product replacement (agent does the work) | Advisory replacement (AI does comparison/planning) |
| Speed of disruption | Fast (software can switch tools quickly) | Slow (enterprise relationships, compliance) |
| Feb 2026 drawdown | -18% from peak | ~-12% from peak |

AIFD constituents may be structurally more defensible than the Week 1 software victims — insurance brokers have 90%+ retention rates, licensed regulatory requirements, and complex commercial relationships that resist commoditization. But the personal lines / simple advisory wedge is real, and margin compression doesn't require full replacement.

---

## Tracking thesis

This basket should:
1. Spike down on AI advisory/comparison tool launches (new ChatGPT apps, Hazel features, competitor products)
2. Correlate internally more than with broad market on AI catalysts
3. Show insurance broker vs. wealth management divergence on sector-specific catalysts

Watch for:
- Additional insurance AI apps entering ChatGPT/Claude/Gemini directories (dozen+ in pipeline)
- Altruist Hazel expansion into portfolio construction, estate planning
- Broker earnings — any mention of AI fee pressure, client behavior change
- Regulatory response — licensing bodies restricting AI advisory tools

---

## Related

- [[February 2026 AI Disruption Cascade]] — the broader repricing this basket sits inside
- [[Software AI bifurcation]] — why AIFD persists as a cluster while event-derived software composites do not
- [[Alternative asset managers basket]] — control group (sold off in Wave 1 as collateral damage, then recovered)
- [[AI disintermediation]] — thesis driving the financial-services advisory leg
- [[Insurify insurance broker selloff February 2026]] — insurance catalyst (Feb 9)
- [[Altruist wealth management selloff February 2026]] — wealth management catalyst (Feb 10)
- [[Claude Cowork disruption February 2026]] — original SaaSpocalypse catalyst
- [[Insurify]] — insurance AI trigger
- [[Altruist]] — wealth management AI trigger
- [[Insurance]] — sector note
- [[Willis Towers Watson]] — highest-weight constituent
- [[Charles Schwab]] — largest market cap constituent

---

## Cluster validation — falsified as single basket; splits into two validated sub-clusters (May 2026)

Validated 2026-05-03 via `scripts/cluster_analysis.py --config scripts/cluster_configs/aifd.yaml`. Procedure in `docs/cluster-validation.md`.

The 10-name AIFD basket fails as a single cluster: intra-corr 0.34 (range -0.09 to 0.79 — wildly bimodal), PC1 only 43.9%. The wide range is the signature of a bimodal cohort: insurance brokers correlate 0.61-0.79 with each other; wealth managers correlate 0.67-0.73 with each other; cross-sub-sector correlations are 0.00-0.22 (essentially uncorrelated).

PC1 loadings make the bimodality unambiguous:

| Sub-cohort | Names | PC1 loadings |
|---|---|---|
| Insurance brokers | WTW, AJG, AON, BRO, MMC | 0.40-0.43 (all positive, near-equal) |
| Insurance brokers (specialty) | RYAN | 0.34 |
| Wealth managers | SCHW, RJF, LPLA, SF | 0.03-0.10 (essentially zero) |

PC1 IS the insurance broker factor — wealth managers don't load on it at all. PC2 (25%) is essentially the wealth manager factor. The two halves of AIFD are mathematically distinct factors that happened to catalyze on consecutive days during the Feb 2026 [[February 2026 AI Disruption Cascade|cascade]] but do not co-move at baseline.

### What the math validated

Hierarchical clustering at 0.4 returns the two sub-clusters cleanly:

- **Cluster 1: WTW, AJG, AON, BRO, MMC** → see [[Insurance brokers basket]] (intra-corr 0.67, PC1 72.2%)
- **Cluster 2: SCHW, RJF, LPLA** → see [[Wealth managers basket]] (intra-corr ~0.69 in 3-name tight core, PC1 64.3%)
- Singletons: RYAN (specialty broker), SF (mid-IB-exposed wealth platform)

### What this means for the AIFD framing

The note's original framing was correct on the SECTOR-LEVEL narrative (both insurance brokers and wealth managers face AI advisory replacement). But the equity-level cluster claim does not hold: the names trade as two completely separate factors, with cross-sub-cluster correlation of 0.09 — about as decoupled as two financial-services cohorts can be while both being public.

Practical implications:
- **Do not trade AIFD as a single basket.** Equal-weighted exposure dilutes idiosyncratic noise across two unrelated sub-factors.
- **Trade the two sub-baskets separately.** Long [[Insurance brokers basket]] for commercial broker AI disruption; long [[Wealth managers basket]] for retail wealth AI disruption. Cross-sub-cluster correlation of 0.09 means a long-AIFD position is essentially long two unrelated 50% factor exposures.
- **Watch for re-correlation.** If a future cross-sub-sector AI catalyst forces both halves to move together (e.g., a regulatory action affecting both), AIFD might reassemble as a meaningful cluster. Currently it does not.
- **Keep the AIFD note** as the AI-disruption-event narrative parent. The two sub-cluster notes link back here as event lineage; this note retains the conceptual framework + thesis content.

Cross-cluster correlation finding is also notable: insurance brokers (0.13 vs wealth managers, 0.13 vs alt managers, 0.22 vs ETFs) consistently shows the LOWEST correlations of any financial-services cohort tested. The +0.58 separation between insurance brokers and wealth managers is the cleanest within-financial-services separation found in the entire validation pass.

*Cluster validation 2026-05-03 — falsified as single basket; two validated sub-clusters created.*
