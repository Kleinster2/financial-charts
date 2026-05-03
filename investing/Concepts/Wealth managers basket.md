---
aliases: [WLTHMGR, Wealth manager basket, Retail wealth platforms]
tags: [basket/internal, wealth-management, advisory]
---

# Wealth managers basket

> [!warning] Cluster status: partial validation (May 2026)
> Intra-cluster correlation 0.50 (just at the floor), PC1 64.3%. Hierarchical clustering at 0.4 returns 3-name tight core (SCHW, RJF, LPLA); SF is singleton with weaker PC1 loading (0.33 vs 0.53-0.56 for the others). The 3-name tight core is the cleanly tradable sub-basket; SF tracks separately. Cluster vs insurance brokers: +0.39 advantage — completely uncorrelated despite both being "fee-income financial services." See "Cluster validation" section below.

The mathematically-validated public retail-and-advisor wealth management cohort. Surfaced as one of the two sub-clusters when [[AI financial disintermediation basket]] (AIFD, 10-name combined cohort) failed cluster validation: AIFD splits cleanly into insurance brokers + wealth managers, which trade as two completely separate factors despite sharing the AI-disruption narrative.

The 4-name candidate cohort partially validates: SCHW + RJF + LPLA form a tight 3-name core (intra ~0.69), SF is a borderline singleton with substantially weaker factor loading. Treat the 3-name core as the tradable basket; SF as adjacent.

---

## Constituents

3-name tight core + SF as adjacency.

| Ticker | Company | PC1 loading | Tier |
|--------|---------|-------------|------|
| SCHW | [[Charles Schwab]] | 0.544 | Tight core |
| RJF | [[Raymond James]] | 0.559 | Tight core |
| LPLA | [[LPL Financial]] | 0.533 | Tight core |
| SF | [[Stifel Financial]] | 0.329 | Adjacency (singleton at 0.4 threshold; mid-IB exposure differs from pure retail wealth) |

Total: 4 candidates; 3-name tight core. Internal ticker proposal: WLTHMGR.

### Why each name belongs

- [[Charles Schwab]] — largest US retail brokerage + advisor custodian; bank holding company structure; net interest income exposure
- [[Raymond James]] — full-service broker + advisor (RJFS); also has investment-banking and asset-management businesses
- [[LPL Financial]] — pure-play independent broker-dealer / advisor custody platform; recurring fee revenue
- [[Stifel Financial]] — full-service brokerage + investment bank + capital markets; mid-IB exposure makes it a partial fit (also surfaced as standalone in [[Boutique advisory consolidation]] mid-IB controls)

### Excluded — and why

| Excluded | Why excluded |
|----------|--------------|
| Insurance brokers (WTW, AJG, AON, BRO, MMC) | The OTHER half of AIFD. Different end-market (commercial vs retail). Cluster correlation 0.09 = essentially uncorrelated. See [[Insurance brokers basket]]. |
| Alt asset managers (BX, KKR, OWL) | Capital allocation, not retail distribution. See [[Alternative asset managers basket]]. Cluster correlation 0.44 — moderate but well below intra-cluster floor. |
| Traditional asset managers (BLK, TROW, BEN) | Manufacturing of products, not distribution platforms. Cluster correlation 0.42 — moderate. |
| Execution platforms ([[Interactive Brokers]], [[Robinhood]]) | No advisory layer; pure execution. Cluster correlation 0.39 — moderate; algorithmically clustered with SPY (broad market beta). |
| Banks (XLF) | Diversified financials; cluster correlation 0.46 — moderate. |

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/wealth_managers.yaml`. Full standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.503 (range 0.27-0.73) | At the cluster floor; SF drags the 4-name average; tight 3-name core is ~0.69 |
| Tightest pair | SCHW-RJF = 0.73 | Two largest full-service platforms |
| 3-name tight core intra-corr | ~0.69 (SCHW + RJF + LPLA) | Strong sub-cohesion |
| PC1 explained variance | 64.3% | Dominant single factor; SF loads weaker |
| Hierarchical clustering at 0.4 | SCHW + RJF + LPLA cluster; SF singleton | 3-name boundary clean |
| Cluster vs insurance brokers | 0.113 (+0.390 advantage) | Cleanest separation in financial services |
| Cluster vs alt asset managers | 0.441 (+0.063 advantage) | Small separation |
| Cluster vs traditional asset managers | 0.417 (+0.087 advantage) | Small separation |
| Cluster vs broad ETFs | 0.458 (+0.045 advantage) | Marginal separation — wealth platforms share more broad-market beta than insurance brokers do |

### Pairwise correlations (1Y, 4-name candidate cohort)

|  | SCHW | RJF | LPLA | SF |
|---|---|---|---|---|
| SCHW | — | 0.73 | 0.67 | 0.27 |
| RJF | 0.73 | — | 0.67 | 0.38 |
| LPLA | 0.67 | 0.67 | — | 0.30 |
| SF | 0.27 | 0.38 | 0.30 | — |

Pairwise structure shows the same pattern as the dendrogram: SCHW + RJF + LPLA form a tight triangle (0.67-0.73 across all 3 pairs), while SF correlates 0.27-0.38 with the others. The 3-name tight core (intra ~0.69) is the validated tradable cluster; SF is a related but distinct name.

### Why SF is singleton at this threshold

[[Stifel Financial]] has substantial investment banking + capital markets exposure (~25-30% of revenue) on top of its wealth management business. The mid-IB / capital markets factor pulls SF away from pure retail-wealth co-movement. SF surfaced as a standalone in the [[Boutique advisory consolidation]] mid-IB controls test as well — it doesn't cluster cleanly with either pure boutique advisory or pure retail wealth, sitting in between.

---

## YTD 2026 cohort tracking

![[wealth-mgr-basket-2026ytd-price-chart.png]]

*SCHW (blue, primary) vs RJF, LPLA, SF normalized from 2025-12-31. The 3-name tight core (SCHW, RJF, LPLA) tracks visibly together through the Q1 2026 sentiment swings — including the Feb 10 Altruist selloff and recovery. SF's path is visibly more independent, consistent with its singleton status.*

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long retail wealth platform factor | Equal-weighted SCHW + RJF + LPLA | Retail wealth distribution / advisor-custody economics |
| Long with adjacency | Add SF (mid-IB exposure included) | Broader wealth+IB sentiment; loosens factor |
| Pair: long wealth managers / short insurance brokers | WLTHMGR vs INSBROK basket | The two AIFD halves trade independently — captures cross-sub-sector factor differential |
| Pair: long wealth managers / short broad market | WLTHMGR vs SPY | Smaller advantage (+0.05) — wealth platforms have more broad-market beta than insurance brokers |
| AVOID: long WLTHMGR / short XLF | Marginal +0.04 advantage; near zero |

---

## Why the cluster works (3-name tight core)

Retail wealth management platforms share business-model exposure:
- Net interest income from sweep deposits (SCHW especially) + fee-based advisor revenue
- AUM growth tied to equity-market beta (asset levels drive fees) + advisor headcount
- Switching costs from advisor relationships and ACAT (account transfer) friction
- Same end-market sensitivity (US retail investor flows, advisor M&A activity)
- Shared exposure to interest-rate cycle (sweep deposit spreads, NII)
- Comparable advisory-revenue margin structures (~30-50% pretax margin)

Different scale, similar economics. SCHW dwarfs RJF and LPLA in size but trades on the same factor.

---

## What could break the cluster

| Scenario | Effect on cluster |
|---|---|
| AI advisory tools (Altruist Hazel, ChatGPT-style planners) penetrate retail | All 3 names re-rate together; cluster cohesion increases on the way down |
| Sustained Fed cuts (NII compression at SCHW) | SCHW decouples from RJF/LPLA — SCHW has heaviest NII exposure |
| LPLA acquired by larger platform | Acquirer + LPLA both decouple around deal-noise |
| Crypto / alts replace traditional advisor channels | All 3 names re-rate; potential decoupling vs IBKR/HOOD execution platforms |
| Mid-IB cycle recovery (deal volume up) | SF re-couples to wealth manager core via revenue-mix improvement |

---

## Tracking

- Re-run validation quarterly: `python scripts/cluster_analysis.py --config scripts/cluster_configs/wealth_managers.yaml`.
- Watch SF's PC1 loading — if it rises above 0.45, SF re-joins tight core.
- Watch SCHW idiosyncratically — its size + NII exposure could pull it out of cluster on rate cycle.
- Cross-check vs [[Insurance brokers basket]] — if cross-cluster correlation rises, AIFD parent narrative is re-asserting.

---

## Related

### Member actors

- [[Charles Schwab]] — tight core
- [[Raymond James]] — tight core
- [[LPL Financial]] — tight core
- [[Stifel Financial]] — adjacency (singleton at 0.4)

### Adjacent concept notes

- [[AI financial disintermediation basket]] — parent (10-name AIFD that splits into this basket + insurance brokers)
- [[Insurance brokers basket]] — the other half of AIFD; opposite cluster (cluster correlation 0.09)
- [[Alternative asset managers basket]] — sibling validated cluster (different business model: origination vs distribution)
- [[Boutique advisory consolidation]] — sibling validated cluster (different business model: M&A advisory; SF is a standalone there too)
- [[Altruist wealth management selloff February 2026]] — Feb 10 catalyst that revealed the cluster
- [[AI disintermediation]] — thesis driving the AI-narrative leg

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/wealth_managers.yaml` — config for this cluster

*Created 2026-05-03 — fifth concept note created under the new cluster-validation standard*
