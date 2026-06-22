---
aliases: [Data Center REITs, Data center REITs, Colocation REITs, Datacenter REITs, DC REIT cohort]
tags: [sector, real-estate, reit, data-center, cluster-validation]
---
#datacenter #infrastructure

# DC REITs

> [!success] Cluster status: VALIDATED distinct — the AI/cloud-demand data-center REITs ([[Equinix|EQIX]]/[[Digital Realty|DLR]]/[[Iron Mountain|IRM]]) decouple from the rate-driven REIT complex AND from the tower REITs; the one REIT sub-sector with a non-rate demand driver (Jun 2026)
> Intra-corr 0.636 (weekly 0.605), PC1 75.8%, all three nulls reject (random-basket and vol-matched at 0.0006), with a WIDE separable band [0.40–0.55] (width 0.15, MODERATELY ROBUST) — broad REITs ([[VNQ]]/[[XLRE]]) and the tower REITs ([[American Tower|AMT]]/[[Crown Castle|CCI]]) contaminate only at 0.60. A +0.115 intra-advantage over broad REITs (modest, like net-lease) but a large +0.310 over the towers: the two "digital-infrastructure" REITs are different factors — towers fuse with VNQ, data centers do not. The AI/cloud capacity-demand driver is what separates DC REITs from the broad rate-driven complex. [[Iron Mountain|IRM]] (records storage + a fast-growing data-center segment) fits the cohort cleanly (DLR+IRM the tightest pair, 0.69). Holdout WEAKENED 0.80 on level off the older window, but durable in recent years (0.58–0.71). See "Cluster validation" below.

Data center real estate investment trusts — the picks-and-shovels of AI/cloud capacity. [[Equinix|EQIX]] (interconnection), [[Digital Realty|DLR]] (wholesale/hyperscale), and [[Iron Mountain|IRM]] (storage + a growing data-center segment) trade as a distinct, moderately-tight factor, separate from both broad REITs and the tower REITs, because their demand is driven by cloud/AI capacity build rather than the interest-rate cycle that prices the rest of real estate.

## Sector performance

![[dc-reits-sector-chart.png]]
*Normalized total return since Jan 2023 — the three DC REITs vs broad REITs [[VNQ]]. [[Equinix|EQIX]]/[[Digital Realty|DLR]]/[[Iron Mountain|IRM]] move together and ahead of VNQ on the AI/cloud capacity-demand tailwind — the distinct, demand-driven REIT factor against the rate-driven broad-REIT complex.*

---

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Avg correlation | 0.69 | Strong (tight pair) |
| vs [[Crypto-to-AI]] | 0.08-0.20 | Separate clusters |
| vs [[CoreWeave]] | 0.23-0.38 | Loose connection |
| Period | 2024-01 to present | |

Pairwise detail:
| Pair | Correlation |
|------|-------------|
| EQIX - DLR | 0.69 |

DC REITs trade together, separate from crypto-to-AI pivots despite all being "data center" companies.

---

## Cluster validation

The candidate cohort is the three US data-center REITs — [[Equinix|EQIX]] (interconnection/colocation), [[Digital Realty|DLR]] (wholesale/hyperscale), [[Iron Mountain|IRM]] (records storage + a fast-growing data-center segment) — tested against broad REITs ([[VNQ]]/[[XLRE]]), the tower REITs ([[American Tower|AMT]]/[[Crown Castle|CCI]] — the other "digital-infrastructure" REIT), and the market (SPY). 1Y window through 2026-06-18 (198 obs), threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.636 [0.578–0.690] | Moderately tight; weekly 0.605; no outlier |
| PC1 explained variance | 75.8% | A strong single factor (weekly 73.7%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0006 | Beyond a random 3-pick — a real factor |
| Vol-matched null p (10k) | 0.0006 | Real beyond shared vol |
| Holdout (2Y split) | WEAKENED 0.80; loadings-corr 0.28 (flat-vector) | train 0.730 → test 0.585; durable in recent years |
| Threshold stable width | 0.15 [0.40–0.55] | WIDE — broad REITs + towers contaminate only at 0.60 |
| Intra-adv vs broad REITs (VNQ/XLRE) | +0.115 | Modestly distinct from the rate-driven REIT complex |
| Intra-adv vs tower REITs (AMT/CCI) | +0.310 | Large — the two digital-infra REITs are different factors |
| Intra-adv vs market (SPY) | +0.231 | Not market beta |

Config: `scripts/cluster_configs/dc_reits.yaml`; registry row 2026-06-22.

### Boundary — its own cluster; towers fuse with broad REITs, data centers don't

![[dc-reits-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The three DC REITs {[[Equinix|EQIX]]/[[Digital Realty|DLR]]/[[Iron Mountain|IRM]]} form their own cluster (orange, closing at 0.391). The tower REITs [[American Tower|AMT]]/[[Crown Castle|CCI]] fuse with broad REITs [[VNQ]]/[[XLRE]] (green) — confirming towers = the REIT complex — while the data centers stay separate, merging with that complex only at ~0.58. SPY sits apart.*

The threshold scan returns a WIDE clean band — the three are an intact, uncontaminated cluster across [0.40–0.55] (width 0.15):

| Threshold | Joins the cohort cluster | Read |
|---|---|---|
| 0.40–0.55 | (nothing) | the three DC REITs alone — the separable band |
| 0.60 | VNQ, XLRE, AMT, CCI | the broad-REIT + tower complex merges |

That broad REITs and the towers contaminate only at 0.60 — a 0.15 margin above the band — is what makes this a genuine distinct factor, more robustly separable than [[Net-lease REITs|net-lease]] (width 0.05) despite a similar intra-advantage over VNQ.

### Topology — IRM fits, not an outlier

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | DLR + IRM | 0.310 | the tightest pair (corr 0.69) — wholesale + storage/DC |
| 2 | EQIX + (DLR+IRM) | 0.391 | interconnection joins; the cohort closes below 0.40 |

[[Iron Mountain|IRM]] is not the outlier one might expect — its data-center build has pulled it into the cohort (DLR+IRM is the tightest pair). All three close by 0.391, no straggler. PC1 explains 75.8%.

### PC1 index weights — an even, single-factor cohort

![[dc-reits-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 75.8% with near-equal loadings (0.56–0.59) — a clean single factor. [[Iron Mountain|IRM]] carries the highest vol (32.7%) and the smallest raw weight.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| EQIX | 0.561 | 32.38% | 23.17% | 36.39% |
| DLR | 0.594 | 34.33% | 24.11% | 37.07% |
| IRM | 0.576 | 33.29% | 32.67% | 26.54% |

### Distinctness — the AI/cloud demand driver, not rates

![[dc-reits-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The three DC REITs run warm (0.58–0.69); they are cooler against broad REITs and cooler still against the towers — the demand-driven names separating from the rate-driven complex.*

The intra-advantage numbers: +0.115 versus broad REITs ([[VNQ]]/[[XLRE]]) — a modest but positive edge, in net-lease territory — and a large +0.310 versus the tower REITs. The towers number is the structural point: [[American Tower|AMT]]/[[Crown Castle|CCI]] (mobile/5G site rentals) cluster with the broad rate-driven REIT complex, while the data centers (AI/cloud capacity demand) form a separate factor. Data-center REITs are the one REIT sub-sector whose demand driver — hyperscaler/AI capacity build — genuinely decouples them from the interest-rate cycle that prices the rest of real estate. There is no pure data-center REIT ETF, so the basket is the way to own the factor.

### Historical tightness evolution — durable except the 2021 dip

![[dc-reits-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Mostly tight (0.58–0.71) with a single dip in 2021 (0.40, the post-COVID divergence when EQIX/DLR de-rated unevenly); back to 0.65 in 2025–26 (latest 90-day 0.632).*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.601 | 73.8% |
| 2021 | 0.400 | 61.5% |
| 2022 | 0.711 | 81.0% |
| 2023 | 0.648 | 76.6% |
| 2024 | 0.576 | 71.8% |
| 2025 | 0.649 | 76.8% |
| 2026 | 0.650 | 76.7% |

*Durable in recent years (0.58–0.71, currently 0.65) — the 2021 dip is what pulls the 2Y holdout to WEAKENED 0.80, but the factor is structurally intact (the low loadings-corr is the flat-vector artifact of an even-loaded three-name cohort, as with [[Net-lease REITs|net-lease]]).*

## Where this sits in the REIT map

Data-center REITs complete the campaign's REIT map, and they are the standout — the only sub-sector with a non-rate demand driver:

- [[Residential REITs]] — distinct (apartment rent/supply, +0.360, the tightest REIT cohort).
- Data-center REITs (this note) — distinct (AI/cloud capacity demand, +0.115 vs VNQ but +0.310 vs towers, wide band).
- [[Net-lease REITs]] — marginally distinct (+0.106, a thin band).
- [[Tower REITs]] — = VNQ (mobile/5G site rentals trade with the rate complex).
- [[Self-storage REITs]] — = VNQ (big-three a sub-factor).
- [[Mortgage REITs]] — = REM (leveraged MBS/credit, a different REIT type).

The map's lesson — a single-asset REIT is distinct only if its demand driver decouples from the broad rate/REIT factor — is clearest here: the AI/cloud build is the one driver strong enough to pull a REIT sub-sector fully out of the rate complex, which is exactly why data centers separate while the towers (also "digital infrastructure," but rate-driven site rentals) do not.

## Key actors

| Company | Ticker | Focus | Market Cap |
|---------|--------|-------|------------|
| [[Equinix]] | EQIX | Interconnection, enterprise | ~$80B |
| [[Digital Realty]] | DLR | Wholesale, hyperscale | ~$53B |

---

## Business model

| Factor | DC REITs | vs Crypto-to-AI |
|--------|----------|-----------------|
| Revenue model | Long-term leases | GPU hosting, volatile |
| Customer | Enterprise, hyperscaler | AI startups, crypto |
| Margins | 60-70% gross | Lower, more variable |
| Capital | REIT structure, stable | Equity/debt dependent |
| Risk profile | Predictable | High beta, speculative |

---

## Why separate from Crypto-to-AI

| Factor | Evidence |
|--------|----------|
| Correlation | EQIX-CORZ: 0.10, EQIX-HUT: 0.15 |
| Business model | Lease vs operate GPUs |
| Customer base | Enterprise/cloud vs AI/crypto |
| Investor base | REIT funds vs growth/spec |

The 0.08-0.20 cross-correlation proves these are fundamentally different businesses despite both owning data centers.

---

## Related

### Parent
- [[Data Centers]] — parent sector

### Sister
- [[Crypto-to-AI]] — crypto miners pivoting to AI hosting

### Actors
- [[Equinix]] — interconnection leader
- [[Digital Realty]] — hyperscale leader
- [[QTS Data Centers]] — private (Blackstone)
- [[CyrusOne]] — private (KKR)

### Context
- [[AI Infrastructure]] — demand driver
- [[Power constraints]] — key bottleneck

*Created 2026-01-30*
