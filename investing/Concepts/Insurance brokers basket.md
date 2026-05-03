---
aliases: [INSBROK, Insurance broker basket, Commercial insurance brokers]
tags: [basket/internal, insurance, brokers]
---

# Insurance brokers basket

> [!success] Cluster status: validated (May 2026)
> Intra-cluster correlation 0.67, PC1 72.2% explained variance. Hierarchical clustering at 0.4 returns 5-name tight core (WTW, AJG, AON, BRO, MMC); RYAN is borderline-singleton at 0.4 but loads positively on PC1 (0.34) — track as adjacency. Cluster vs wealth managers: +0.58 advantage (the cleanest separation in financial services). See "Cluster validation" section below.

The mathematically-validated public commercial-insurance-broker cohort. Surfaced as one of the two sub-clusters when [[AI financial disintermediation basket]] (AIFD, 10-name combined cohort) failed cluster validation: AIFD splits cleanly into insurance brokers + wealth managers, which catalyzed on different days (Insurify Feb 9 vs Altruist Feb 10 2026) and trade as two completely separate factors.

The cluster also surfaced consistently in adjacent validations: AON, AJG, BRO appeared as a tight 3-name cluster in the [[Alternative asset managers basket]] control universe (intra ~0.75, with NEGATIVE correlation to ALTM at 0.13). Across three independent test designs (AIFD falsification, ALTM control test, this dedicated test), the insurance broker cohort consistently clusters tightly with itself and stays distant from the rest of financial services. That convergence is robust mathematical evidence the cluster is real.

---

## Constituents

5 names in the tight core. RYAN as adjacency.

| Ticker | Company | PC1 loading | Tier |
|--------|---------|-------------|------|
| WTW | [[Willis Towers Watson]] | 0.402 | Tight core |
| AJG | [[Arthur J. Gallagher]] | 0.432 | Tight core |
| AON | [[Aon]] | 0.432 | Tight core |
| BRO | [[Brown & Brown]] | 0.416 | Tight core |
| MMC | [[Marsh McLennan]] | 0.417 | Tight core |
| RYAN | [[Ryan Specialty]] | 0.343 | Adjacency (singleton at 0.4 threshold; specialty/wholesale model differs from retail brokers) |

Total: 6 candidates; 5-name tight core. Internal ticker proposal: INSBROK.

### Why each name belongs

- [[Willis Towers Watson]] — global commercial broker; consulting + insurance brokerage; M&A advisory
- [[Arthur J. Gallagher]] — global commercial broker; aggressive M&A roll-up
- [[Aon]] — global commercial broker; reinsurance broker via Aon Reinsurance
- [[Brown & Brown]] — US-focused commercial broker; mid-market specialist
- [[Marsh McLennan]] — largest global commercial broker; consulting (Mercer, Oliver Wyman)
- [[Ryan Specialty]] — specialty/wholesale broker — different sub-segment from retail commercial brokers; loads on PC1 but trades with idiosyncratic specialty-market dynamics

### Excluded — and why

| Excluded | Why excluded |
|----------|--------------|
| Insurance carriers ([[Progressive]], [[Chubb]], [[Travelers]]) | Carriers manufacture the product, brokers distribute it. Different factor. Carriers cluster +0.27 from brokers but don't merge at 0.4 threshold. |
| Wealth managers ([[Charles Schwab]], [[Raymond James]], [[LPL Financial]]) | The OTHER half of AIFD. Different end-market (retail/HNW investing vs commercial/employee benefits). Cluster correlation 0.09 = essentially uncorrelated. |
| Alt asset managers ([[Blackstone]], [[KKR]]) | Capital allocation, not distribution. See [[Alternative asset managers basket]] — its own validated cluster. |
| Banks (XLF) | Different business mix; cluster correlation 0.22 = mostly uncorrelated. |

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/insurance_brokers.yaml`. Full standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.668 (range 0.34-0.79) | Strong cohesion in 5-name core; RYAN drags the average |
| Tightest pair | WTW-AJG = 0.79, AJG-BRO = 0.79 | Two pairs at the 0.79 ceiling |
| PC1 explained variance | 72.2% | Strong single-factor cohort |
| Hierarchical clustering at 0.4 | WTW + AJG + AON + BRO + MMC merge; RYAN singleton | Clear 5-name boundary |
| Cluster vs wealth managers | 0.093 (+0.576 advantage) | Cleanest separation found in financial services validations |
| Cluster vs insurance carriers | 0.394 (+0.274 advantage) | Distribution factor distinct from manufacturing factor |
| Cluster vs alt asset managers | 0.153 (+0.516 advantage) | Distribution factor distinct from origination factor |
| Cluster vs broad ETFs | 0.216 (+0.452 advantage) | Highly distinct from broad financials beta |

### Pairwise correlations (1Y, 5-name tight core)

|  | WTW | AJG | AON | BRO | MMC |
|---|---|---|---|---|---|
| WTW | — | 0.79 | 0.78 | 0.61 | 0.68 |
| AJG | 0.79 | — | 0.78 | 0.79 | 0.75 |
| AON | 0.78 | 0.78 | — | 0.71 | 0.78 |
| BRO | 0.61 | 0.79 | 0.71 | — | 0.68 |
| MMC | 0.68 | 0.75 | 0.78 | 0.68 | — |

AJG is the central node — correlates 0.75-0.79 with all four other tight-core names. WTW-BRO at 0.61 is the loosest pair in the tight core (still above any inter-group benchmark).

### What the +0.58 separation from wealth managers means

This is the cleanest separation found in any financial-services cluster validation. Despite both being "fee-income financial services" with parallel AI-disruption narratives (Insurify catalysts insurance brokers; Altruist catalysts wealth managers), the math says they are completely separate factors at the equity level. The Feb 2026 [[AI financial disintermediation basket|AIFD basket]] grouping was a single-event narrative, not a structural cluster. Trade these baskets separately.

---

## YTD 2026 cohort tracking

![[ins-brokers-basket-2026ytd-price-chart.png]]

*AJG (blue, primary) vs WTW, AON, BRO, MMC, RYAN normalized from 2025-12-31. Cohort moves together through Q1 2026 — including the Feb 9 Insurify selloff and subsequent recovery. RYAN's path diverges visually from the 5-name core, consistent with its singleton status at the 0.4 threshold.*

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long insurance broker factor | Equal-weighted WTW + AJG + AON + BRO + MMC | Commercial broker distribution economics |
| Long with adjacency | Add RYAN (specialty/wholesale exposure) | Broader broker sentiment; loosens factor |
| Pair: long brokers / short wealth managers | INSBROK basket vs SCHW + RJF + LPLA basket | The two AIFD halves trade independently — pair captures cross-sub-sector factor differential |
| Pair: long brokers / short carriers | INSBROK vs PGR/CB/TRV | Distribution vs manufacturing economics |
| Pair: long brokers / short XLF | INSBROK vs XLF | Isolates broker-specific factor (+0.45 advantage available) |

---

## Why the cluster works

Commercial insurance brokers share a single dominant business model:
- Recurring commission revenue tied to premium volume
- 90%+ client retention rates (multi-year contracts, complex switching costs)
- Roll-up M&A growth playbook (all 5 names are active acquirers)
- Same end-market sensitivity (commercial premium pricing cycle, employer headcount, M&A activity affecting placements)
- Shared regulatory environment (state insurance commissioners, NAIC frameworks)
- Comparable margin structures (~25-32% operating margin, low capital intensity)

Same business, different scale. The math reflects this — pairwise correlations 0.61-0.79 across the 5-name core.

---

## What could break the cluster

| Scenario | Effect on cluster |
|---|---|
| AI advisory tools penetrate small commercial broker market | All 5 names re-rate together; cluster cohesion increases on the way down |
| Carrier-direct distribution shift (cuts out brokers) | Cluster fractures: brokers with carrier diversification (MMC, AJG) decouple from those with concentrated carrier panels |
| One major broker is acquired (e.g., AON takes over WTW post-2021 failure) | Acquirer name decouples from cluster around deal-noise periods |
| Soft commercial pricing cycle (premium rates fall) | Cluster persists during selloff — premium-tied commission means all 5 see same pressure |
| Specialty markets boom (RYAN-led) | RYAN further decouples from retail broker core |

---

## Tracking

- Re-run validation quarterly: `python scripts/cluster_analysis.py --config scripts/cluster_configs/insurance_brokers.yaml`.
- Watch RYAN's PC1 loading — if it rises above 0.40, RYAN re-joins the tight core (would signal specialty wholesale converging with retail commercial broker factor).
- Watch broker M&A — large deals between cluster members would force cluster recomposition.
- Cross-check vs [[Wealth managers basket]] — if cross-cluster correlation rises above 0.30, the AIFD parent-narrative might be re-asserting (sector-wide AI-disruption sentiment overriding sub-sector business-model differences).

---

## Related

### Member actors

- [[Willis Towers Watson]] — tight core
- [[Arthur J. Gallagher]] — tight core (central PC1 node)
- [[Aon]] — tight core
- [[Brown & Brown]] — tight core
- [[Marsh McLennan]] — tight core
- [[Ryan Specialty]] — algorithmic adjacency (singleton at 0.4)

### Adjacent concept notes

- [[AI financial disintermediation basket]] — parent (10-name AIFD that splits into this basket + wealth managers)
- [[Wealth managers basket]] — the other half of AIFD; opposite cluster (cluster correlation 0.09)
- [[Alternative asset managers basket]] — sibling validated cluster (different business model: origination vs distribution)
- [[Boutique advisory consolidation]] — sibling validated cluster (different business model: M&A advisory)
- [[Insurance]] — sector hub
- [[Insurify insurance broker selloff February 2026]] — Feb 9 catalyst that revealed the cluster
- [[AI disintermediation]] — thesis driving the AI-narrative leg

### Excluded names (with cluster results)

- [[Progressive]], [[Chubb]], [[Travelers]] — insurance carriers; +0.27 separation
- [[Charles Schwab]], [[Raymond James]], [[LPL Financial]] — wealth managers; +0.58 separation (cleanest)
- [[Blackstone]], [[KKR]] — alt asset managers; +0.52 separation

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/insurance_brokers.yaml` — config for this cluster

*Created 2026-05-03 — fourth concept note created under the new cluster-validation standard*
