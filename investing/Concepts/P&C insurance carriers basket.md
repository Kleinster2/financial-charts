---
aliases: [PC insurance carriers, P&C carriers, PC carriers, PCINS]
tags: [basket/internal, insurance, p-and-c]
---

# P&C insurance carriers basket

> [!success] Cluster status: validated (May 2026)
> Intra-cluster correlation 0.64 (range 0.54-0.81), PC1 71.6% explained variance. Hierarchical clustering at 0.4 returns exactly the 5 candidate names (PGR, CB, TRV, ALL, HIG). Cleanest separation: vs banks (+0.50 advantage), vs broad ETFs (+0.48). Tightest pair: TRV-HIG = 0.81. The lowest broad-market beta of any validated cluster in the validation pass — P&C carriers trade on insurance underwriting cycle, not equity beta. See "Cluster validation" section below.

The mathematically-validated public US property-and-casualty insurance carrier cohort. Surfaced as the dominant sub-cluster within the broader [[Insurance carriers basket]] (8-name cohort that fails as one cluster but contains this 5-name validated sub-cluster + a 2-name life-insurance pair + AIG singleton).

---

## Constituents

5 names — equal-weighted starting point.

| Ticker | Company | PC1 loading | Why it belongs |
|--------|---------|-------------|----------------|
| PGR | [[Progressive]] | 0.411 | Auto leader; pricing-cycle exposure; usage-based pioneer |
| CB | [[Chubb]] | 0.436 | Largest US commercial P&C insurer; high-net-worth personal lines |
| TRV | [[Travelers]] | 0.461 | Pure-play P&C; commercial + personal mix; DJIA component |
| ALL | [[Allstate]] | 0.457 | Personal-lines auto + home; brand-driven distribution |
| HIG | [[Hartford]] | 0.468 | Mixed P&C + small-employer benefits |

Total: 5 constituents. Internal ticker proposal: PCINS.

### Excluded — and why

| Excluded | Why excluded |
|----------|--------------|
| [[MetLife]], [[Prudential Financial]] | Life insurers — different factor (long-duration rate exposure). 2-name pair correlation 0.69 within themselves; cross-correlation with P&C cluster only 0.26 |
| [[AIG]] | Specialty + complex restructured business; singleton at 0.4 threshold |
| Insurance brokers (WTW/AJG/AON/BRO/MMC) | Distribution layer, not manufacturing — different economics. See [[Insurance brokers basket]] |
| Reinsurance pure-plays (Munich Re, Swiss Re) | International listings; reinsurance-cycle is more event-driven than P&C primary |

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/pc_carriers.yaml`. Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.644 (range 0.54-0.81) | Strong cohesion |
| Tightest pair | TRV-HIG = 0.81 | Two pure-play P&C with similar mix |
| PC1 explained variance | 71.6% | Strong single-factor cohort |
| Hierarchical clustering at 0.4 | All 5 names cluster | Boundary confirmed exactly |
| Cluster vs life insurers (MET, PRU) | 0.255 (+0.389 advantage) | Underwriting vs rate-curve factor are distinct |
| Cluster vs insurance brokers | 0.412 (+0.232 advantage) | Manufacturing vs distribution economics |
| Cluster vs banks | 0.146 (+0.498 advantage) | Underwriting cycle independent of credit cycle |
| Cluster vs broad ETFs | 0.167 (+0.477 advantage) | Lowest broad-market beta of any validated cluster — P&C is its own factor |

### Pairwise correlations (1Y)

|  | PGR | CB | TRV | ALL | HIG |
|---|---|---|---|---|---|
| PGR | — | 0.69 | 0.61 | 0.69 | 0.54 |
| CB | 0.69 | — | 0.65 | 0.61 | 0.67 |
| TRV | 0.61 | 0.65 | — | 0.65 | 0.81 |
| ALL | 0.69 | 0.61 | 0.65 | — | 0.71 |
| HIG | 0.54 | 0.67 | 0.81 | 0.71 | — |

PGR-HIG at 0.54 is the loosest pair (Progressive's auto-pricing-engine model + telematics differs from Hartford's mixed commercial/benefits mix). TRV-HIG at 0.81 is tightest — both are commercial-heavy mixed P&C.

---

## What makes this cluster distinctive

The +0.48 separation from broad ETFs is the most distinctive feature: P&C carriers have the LOWEST broad-market beta of any validated cluster in the entire validation pass. Reasons:

- Underwriting cycle is independent of equity cycle. Pricing cycles (hard market vs soft market) are driven by industry capacity + cat losses, not stock market sentiment.
- Cat losses are the dominant risk factor (hurricanes, wildfires, severe convective storms) — uncorrelated with broad-market drivers.
- Investment income is mostly fixed-income (insurer balance sheets are bond-heavy) — partial rate-curve exposure but not equity beta.
- Reserve-release dynamics add idiosyncratic earnings noise that doesn't tie to market regime.

This makes P&C carriers a useful diversifier in equity portfolios — they offer "financial services" exposure without the bank-cycle / broad-market beta of XLF.

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long P&C underwriting cycle | Equal-weighted PCINS basket | P&C pricing + cat losses + reserve releases |
| Long P&C / short XLF | Captures +0.48 separation from financials beta | Pure underwriting cycle |
| Long P&C / short SPY | Captures +0.48 separation from broad market | Insurance-as-diversifier |
| Long P&C / short life insurers | Captures +0.39 separation from rate-curve factor | Underwriting cycle vs rate cycle |
| Long P&C / short insurance brokers | Captures manufacturing vs distribution | Limited usefulness — both fee/commission economies |
| Pair within P&C (e.g., long PGR / short ALL) | Captures auto-direct vs brand-distribution model | Within-cluster business-model differentials |

---

## What could break the cluster

| Scenario | Effect on cluster |
|---|---|
| Major cat event (hurricane, wildfire) | Cluster cohesion increases — all 5 names re-rate together |
| Hard market pricing cycle | Cluster persists — cluster is the pricing-cycle exposure |
| Auto-insurance disruption (telematics scaling, EVs changing claim patterns) | PGR may decouple — its model is most exposed to telematics-driven repricing |
| Major reserve release surprise from one carrier | One name decouples around earnings event |
| Climate-change reset in cat modeling | Cluster cohesion increases on the way down (sector-wide repricing) |

---

## Tracking

- Re-run validation quarterly: `python scripts/cluster_analysis.py --config scripts/cluster_configs/pc_carriers.yaml`.
- Watch PGR's PC1 loading — auto-direct telematics differentiation may pull it out over time.
- Watch HIG — its small-employer benefits leg may pull it toward life-insurance factor on rate-cycle moves.
- Cross-check vs [[Insurance brokers basket]] — confirms manufacturing-vs-distribution remains distinct.

---

## Related

### Member actors

- [[Progressive]] — auto pure-play
- [[Chubb]] — commercial P&C leader
- [[Travelers]] — pure-play P&C, DJIA component
- [[Allstate]] — personal-lines brand
- [[Hartford]] — mixed P&C + benefits

### Adjacent concept notes

- [[Insurance carriers basket]] — parent (8-name cohort that splits)
- [[Insurance brokers basket]] — distribution-side sibling cluster (manufacturing vs distribution)
- [[Insurance float]] — Buffett-era frame for the asset side
- [[Reinsurance sidecars]] — adjacent reinsurance capital structure
- [[Insurance]] — sector hub

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/pc_carriers.yaml` — config for this cluster

*Created 2026-05-03 — sixth concept note created under the new cluster-validation standard*
