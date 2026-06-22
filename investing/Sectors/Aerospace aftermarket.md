---
aliases: [Aerospace aftermarket, Aerospace components, Aerospace suppliers, Aerospace aftermarket cluster]
tags: [sector, industrials, aerospace, aftermarket, cluster-validation]
---

# Aerospace aftermarket

> [!warning] Cluster status: NOT a distinct factor — the aerospace components/aftermarket names are ITA-replicable; distinct from the defense primes but captured by the A&D ETF, with TransDigm an idiosyncratic singleton (Jun 2026)
> The aerospace components/aftermarket compounders ([[TransDigm|TDG]]/[[Heico|HEI]]/[[Howmet Aerospace|HWM]]/[[Curtiss-Wright|CW]]) cohere only weakly — intra-corr 0.519, PC1 64% — and the decisive number is a NEGATIVE −0.063 intra-advantage versus the A&D ETF [[ITA]]/XLI/SPY: the names track ITA more than each other. They ARE distinct from the defense primes (+0.184 versus [[Lockheed Martin|LMT]]/[[General Dynamics|GD]] — aerospace components and pure primes are two A&D sub-poles), but [[ITA]] holds both, so the components names are ITA-replicable, not a separable factor. The cohort also doesn't really hold together: [[Heico|HEI]]/[[Howmet Aerospace|HWM]]/[[Curtiss-Wright|CW]] cluster with ITA, while [[TransDigm|TDG]] — the purest "aftermarket compounder" — is an idiosyncratic singleton (its PE-style roll-up, leverage, and special-dividend story join the others only at 0.584). Own [[ITA]] for the A&D-supplier exposure, or [[Defense primes]] for the prime pole; there is no distinct aftermarket factor, and the one genuinely-distinct thing here ([[TransDigm|TDG]]'s idiosyncrasy) is a single name, not a basket.

The compounder niche that isn't a factor. TransDigm, Heico, Howmet, and Curtiss-Wright are celebrated as high-quality aerospace component/aftermarket compounders, and they do share the commercial-aero build-and-aftermarket cycle — but that cycle is exactly what the A&D ETF captures, and the four are no more correlated with each other than with ITA. The aftermarket "theme" is an ETF exposure plus one idiosyncratic single-stock story (TransDigm).

## Sector performance

![[aero-aftermkt-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[ITA]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is four aerospace components/aftermarket names — [[TransDigm|TDG]], [[Heico|HEI]], [[Howmet Aerospace|HWM]], [[Curtiss-Wright|CW]] — tested against the defense primes ([[Lockheed Martin|LMT]]/[[General Dynamics|GD]]), the A&D ETF [[ITA]], industrials (XLI), and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.519 [0.327–0.690] | barely above the 0.50 floor; weekly 0.511 |
| PC1 explained variance | 64.4% | one dominant factor — but it is A&D/industrials beta |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0014 | beats a random 4-pick, but weakly (via A&D beta) |
| Vol-matched null p | 0.0010 / 0.0012 | beats vol-matched baskets, weakly |
| Holdout (2Y split) | WEAKENED 0.71 | train 0.726 → test 0.518 (eroding) |
| Threshold stable width | 0.00 (none) | never isolates — ITA/XLI contaminate at every cut |
| Intra-adv vs primes (LMT/GD) | +0.184 | distinct from the defense primes (two A&D sub-poles) |
| Intra-adv vs ETFs (ITA/XLI/SPY) | −0.063 | NEGATIVE — the names track ITA more than each other |

All US-listed. Config: `scripts/cluster_configs/tdg.yaml`; registry row 2026-06-20.

### Boundary — components cluster with ITA; primes apart; TDG a singleton

![[aero-aftermkt-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Three groups: the defense primes [[Lockheed Martin|LMT]]/[[General Dynamics|GD]] (a separate pole); the components names [[Heico|HEI]]/[[Howmet Aerospace|HWM]]/[[Curtiss-Wright|CW]] clustered WITH the A&D ETF [[ITA]] (and XLI/SPY); and [[TransDigm|TDG]] alone as a singleton. The ETF sitting inside the components cluster is the mark of ITA-replicability.*

The threshold scan never isolates the cohort (zero stable width) — [[ITA]] and XLI contaminate at every cut — and the intra-advantage versus the ETFs is negative (−0.063). So this is the ETF-replicable verdict: the components/aftermarket names are A&D-sector beta, distinct from the pure defense primes (+0.184) but not from the ETF that holds both. The one separable structure (the prime pole) already has its own validated cohort, [[Defense primes]].

### Topology — a components core (HEI/HWM/CW) and TDG apart

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | HWM + CW | 0.310 | the engine/defense-components pair |
| 2 | HEI + (HWM+CW) | 0.411 | Heico joins the components core |
| 3 | TDG + core | 0.584 | TransDigm joins only above the 0.5 cut — the singleton |

The components core ([[Heico|HEI]]/[[Howmet Aerospace|HWM]]/[[Curtiss-Wright|CW]]) closes at 0.411, but it is ITA-coincident; [[TransDigm|TDG]] joins only at 0.584, above the cut. PC1 explains 64% with a big PC2 (18%) — the TDG-vs-rest axis.

### PC1 index weights

![[aero-aftermkt-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 64.4% (weekly 63.5%); [[TransDigm|TDG]] loads lowest, consistent with being the singleton.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| TDG | 0.416 | 20.9% | 28.0% | 24.2% |
| HEI | 0.523 | 26.3% | 35.2% | 24.1% |
| HWM | 0.537 | 27.0% | 32.1% | 27.1% |
| CW | 0.515 | 25.9% | 34.1% | 24.5% |

The components core ([[Heico|HEI]]/[[Howmet Aerospace|HWM]]/[[Curtiss-Wright|CW]]) carries the high loadings (~0.52); [[TransDigm|TDG]] loads lowest (0.416) — it contributes least to the shared factor because it is the most idiosyncratic.

### Distinctness — distinct from primes, but = ITA

![[aero-aftermkt-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A warm HEI/HWM/CW block with ITA about as warm against them; TDG cooler against everything; the primes (LMT/GD) a separate cool corner.*

Two readings: +0.184 versus the defense primes (the components names are a distinct A&D sub-pole from LMT/GD) but −0.063 versus the ETFs, with [[ITA]] inside the components cluster. ITA is built from both the primes and the suppliers, so it captures the components factor directly; the bespoke basket adds nothing. And [[TransDigm|TDG]] is not even part of the cluster — its leverage/roll-up/special-dividend profile makes it a single-stock story. Own [[ITA]] (or split into [[Defense primes]] for the prime pole); there is no distinct aerospace-aftermarket basket.

### Historical tightness evolution

![[aero-aftermkt-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Moderate (0.49–0.72), peaking in the 2023 commercial-aero-recovery window, eroding to 0.49 in 2026.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.633 | 72.5% |
| 2022 | 0.659 | 74.5% |
| 2023 | 0.717 | 78.8% |
| 2024 | 0.605 | 70.4% |
| 2025 | 0.659 | 74.5% |
| 2026 | 0.493 | 62.7% |

Latest 90-day reading: intra 0.568, PC1 67.7%. Cohesion peaked in the 2023 commercial-aerospace recovery (when build-rate and aftermarket news moved the names together) and has eroded since (holdout WEAKENED 0.71). It was always A&D-sector beta — the components names resolve to [[ITA]], the primes are the separable pole ([[Defense primes]]), and [[TransDigm|TDG]] trades on its own.

## Related

- [[Defense primes]] — the separable A&D pole (the components names are distinct from it, +0.184)
- [[TransDigm]] — the idiosyncratic singleton (PE-style aftermarket roll-up)
- [[Heico]], [[Howmet Aerospace]], [[Curtiss-Wright]] — the components core that clusters with ITA
- [[ITA]] — the aerospace & defense ETF the cohort resolves to
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/tdg.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
