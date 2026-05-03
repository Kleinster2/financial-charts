---
aliases: [Mega banks, US universal banks, MEGABANK]
tags: [concept/cluster, banking, financials]
---

# Mega banks basket

> [!success] Cluster status: validated as cohort, but boundary equals XLF (May 2026)
> Intra-cluster correlation 0.70 (range 0.61-0.78), PC1 75.8% explained variance — strong cohesion. BUT hierarchical clustering at 0.4 merges JPM/BAC/C/WFC/USB with GS, MS, KRE (regional banks), and XLF (financials ETF) into ONE block. The cluster IS the financials sector. There is no "mega bank" sub-factor distinct from XLF — at the equity level, the 5 names ARE the dominant constituents of XLF. The +0.59 separation from insurance carriers is the only meaningful within-financials distinction. See "Cluster validation" section below.

The five largest US universal banks — JPMorgan, Bank of America, Citigroup, Wells Fargo, US Bancorp — cohere tightly as a cluster (intra 0.70, PC1 76%) but the cluster boundary at 0.4 threshold extends to include investment banks (GS, MS), regional banks (KRE), and the broad financials ETF (XLF). Translation: at the 1-year horizon, "mega banks" = "banks" = "XLF financials." The math validates the cluster but says it isn't a separable basket from XLF.

---

## Constituents

5-name candidate cohort. Dendrogram shows it merging with the broader XLF block.

| Ticker | Company | PC1 loading | Note |
|--------|---------|-------------|------|
| JPM | [[JPMorgan Chase]] | 0.434 | Largest US bank; bellwether |
| BAC | [[Bank of America]] | 0.474 | Largest deposit franchise |
| C | [[Citigroup]] | 0.450 | Most international; restructuring story |
| WFC | [[Wells Fargo]] | 0.441 | Domestic-focused; asset cap recently lifted |
| USB | [[US Bancorp]] | 0.436 | Smallest of the major commercial banks |

Internal ticker proposal: MEGABANK.

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/mega_banks.yaml`. Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.696 (range 0.61-0.78) | Strong cohesion |
| Tightest pair | BAC-C = 0.78, BAC-WFC = 0.78 | BAC is the central node |
| PC1 explained variance | 75.8% | Strong single-factor cohort |
| Hierarchical clustering at 0.4 | JPM+BAC+C+WFC+USB+GS+MS+KRE+XLF all merge as ONE cluster | Boundary == financials sector |
| Cluster vs investment banks (GS, MS) | 0.66 (+0.04 advantage) | Barely separates — investment banks ARE in the same factor at this threshold |
| Cluster vs regional banks (KRE) | 0.68 (+0.02 advantage) | Barely separates — regionals are in the same factor too |
| Cluster vs broad ETFs (XLF, SPY) | 0.65 (+0.05 advantage) | Cluster IS the financials factor |
| Cluster vs insurance carriers | 0.109 (+0.587 advantage) | Only meaningful within-financials separation |

### Pairwise correlations (1Y)

|  | JPM | BAC | C | WFC | USB |
|---|---|---|---|---|---|
| JPM | — | 0.73 | 0.71 | 0.64 | 0.61 |
| BAC | 0.73 | — | 0.78 | 0.78 | 0.72 |
| C | 0.71 | 0.78 | — | 0.63 | 0.68 |
| WFC | 0.64 | 0.78 | 0.63 | — | 0.69 |
| USB | 0.61 | 0.72 | 0.68 | 0.69 | — |

### What the boundary-equals-XLF finding means

The cluster validation says: the 5-name cohort IS the dominant factor inside XLF. There is no clean way to construct a "mega banks vs XLF" trade — the cohort accounts for so much of XLF's weighting that the long-short collapses to near-zero net exposure.

Three implications:
- Trading the basket directly = trading XLF with cleaner mega-bank concentration. Useful if you want pure mega-bank exposure without REITs / insurance / consumer-finance dilution.
- Investment banks (GS, MS) trade with the mega bank cohort at the 0.4 threshold — at this horizon, the i-bank vs commercial-bank distinction is not a separable factor. Tighter threshold (0.3) might separate them.
- Regional banks (KRE) also merge with mega banks at 0.4 — the rate-cycle and credit-cycle factors dominate within-banking distinctions at the 1Y horizon.
- The ONLY clean within-financials separation is from insurance carriers (+0.59) — see [[Insurance carriers basket]] / [[P&C insurance carriers basket]].

---

## Trade implications

| Trade | Verdict |
|---|---|
| Long MEGABANK basket | Equivalent to long XLF with mega-bank concentration; useful for pure US universal-bank exposure |
| Long MEGABANK / short XLF | Near-zero net exposure — cluster IS the dominant factor in XLF |
| Long MEGABANK / short KRE | Captures size-tier differential; at 0.4 horizon, this is mostly noise |
| Long MEGABANK / short investment banks (GS+MS) | Captures commercial banking vs investment banking; small but real differential |
| Long MEGABANK / short insurance carriers | Captures the +0.59 within-financials separation — meaningful trade |
| Pair trades within MEGABANK | Captures idiosyncratic restructuring stories (C is the obvious one); not factor exposures |

---

## What could break the cluster (or sharpen it)

| Scenario | Effect on cluster |
|---|---|
| Yield-curve steepening | Cluster cohesion increases — all banks benefit from NII expansion together |
| Credit-cycle deterioration | Cluster cohesion increases — all banks re-rate on credit losses together |
| One-bank idiosyncratic event (WFC asset cap, C restructuring) | Affected name decouples around event-noise |
| Fed cuts in front-end (rate-cycle pivot) | KRE may decouple from MEGABANK as smaller banks have higher NIM sensitivity |
| Banking crisis (2023-style) | Cluster cohesion increases on the way down |

---

## Related

### Member actors

- [[JPMorgan Chase]] — bellwether
- [[Bank of America]] — central PC1 node
- [[Citigroup]] — restructuring story
- [[Wells Fargo]] — domestic franchise
- [[US Bancorp]] — smallest of majors

### Adjacent concept notes

- [[Banking concentration]] — structural backdrop
- [[Bank cronyism]] — political-economy frame
- [[Banking primer]] — sector hub
- [[Goldman Sachs]] — investment bank (clusters with mega banks at 0.4)
- [[Morgan Stanley]] — investment bank (clusters with mega banks at 0.4)

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/mega_banks.yaml` — config for this cluster

*Created 2026-05-03 — validated cluster note with boundary-equals-XLF caveat*
