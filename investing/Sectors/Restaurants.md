---
aliases:
  - Restaurant sector
  - Restaurant industry
tags:
  - sector
  - hospitality
  - restaurants
---

**Restaurants** — sector covering restaurant groups, chains, quick-service operators, and independent hospitality concepts. A ~$1T US industry (2024 NRA estimate) characterized by thin margins (3-9% net), high labor intensity, and cyclical consumer spending sensitivity. The post-COVID landscape features persistent labor cost inflation, delivery platform dependency ([[DoorDash]], [[Uber Eats]]), and bifurcation between scaled chains with pricing power and independents facing margin compression.

## Sub-sector taxonomy

| Sub-sector | Characteristics | Key names |
|------------|----------------|-----------|
| QSR (quick-service) | Scale, drive-through, franchising | [[McDonald's]], [[Yum! Brands]], [[Restaurant Brands International]] |
| Fast-casual | Higher ASP, customization | [[Chipotle]], [[Sweetgreen]], [[Cava]] |
| Casual dining | Under pressure, declining traffic | [[Darden Restaurants]], [[Brinker International]] |
| Fine dining / experiential | High ASP, urban, tourism-driven | Independent operators |
| Coffee | Subscription-like frequency | [[Starbucks]], [[Dutch Bros]] |

## Key dynamics

- Delivery platforms (15-30% commission) reshape unit economics but expand addressable market
- Labor cost inflation (minimum wage hikes, tip regulation) compressing margins industry-wide
- Franchised models (90%+ franchise mix) generate high-margin royalty streams with limited capex
- Consumer trade-down risk in recession — QSR gains at casual dining's expense
- AI and automation (kiosks, kitchen robotics) emerging as margin recovery lever

## Key ETFs

- EATZ (AdvisorShares Restaurant ETF), BITE (Roundhill Restaurant ETF — closed)

## Cluster validation

> [!failure] Cluster status: falsified — a label that was a factor only under the COVID shock (Jun 2026)
> The big-cap restaurants ([[McDonald's|MCD]]/[[Starbucks|SBUX]]/[[Chipotle|CMG]]/[[Yum! Brands|YUM]]/[[Darden Restaurants|DRI]]) do not trade as one factor. Intra-corr is 0.364 (weekly 0.472), PC1 only 49%; the cohort clears the random-basket null only marginally (p 0.025) on shared consumer-traffic beta. The names shatter — only [[McDonald's]]+[[Yum! Brands]] (the asset-light global QSR franchisors) pair below the cut; [[Chipotle]], [[Starbucks]], and [[Darden Restaurants]] are singletons. The history is the lesson: restaurants were a tight 0.85 factor in the 2020 COVID lockdown-and-reopen trade, then fragmented to ~0.32–0.35 as each name went idiosyncratic. A sector is a factor only while a common shock dominates; absent one, restaurants are five same-store-sales stories.

The restaurant equities are the consumer-discretionary counterpart to the day's healthcare falsifications, with a sharper time dimension. Going in, the question was whether restaurants cohere as one consumer-traffic factor or split by segment (QSR / fast-casual / casual dining). They neither cohere nor split cleanly by segment — they fragment into one franchisor pair plus singletons, because each name's dominant driver is its own same-store-sales and unit-growth story: [[Chipotle]]'s fast-casual throughput, [[Starbucks]]'s coffee turnaround and China, [[Darden Restaurants]]'s casual-dining traffic, and the [[McDonald's]]/[[Yum! Brands]] global-franchise royalty model. The one durable structure is that franchise-royalty pair.

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.364 [0.268–0.567] | below the 0.50 floor; weekly 0.472 (small-cap reaction timing, all US-listed) |
| PC1 explained variance | 49.2% | weak; variance spread across PC2–PC5 |
| Independence null p | 0.0001 | series co-move at all |
| Random-basket null p | 0.025 (PC1 0.043) | marginal — barely beats random, via shared consumer-traffic beta |
| Holdout (2Y split) | STABLE 0.98 | durably loose — stable at a low level, not regime-flipping (loadings corr 0.52) |
| Threshold clean width | 0.00 | BOUNDARY-DEPENDENT — never forms a clean cluster |
| Intra-adv vs staples (KO/PEP) | +0.128 | weakly distinct from packaged-food staples |
| Intra-adv vs ETFs (XLY/XLP/SPY) | +0.094 | weakly distinct from consumer-discretionary / market beta |

1Y daily log returns through 2026-06-15, threshold 0.5. All US-listed (synchronous). Config: `scripts/cluster_configs/mcd.yaml`; registry row 2026-06-16. Terminology: [[Cohort, cluster, basket]].

### Boundary — only the franchisor pair holds

![[restaurants-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Only [[McDonald's]]+[[Yum! Brands]] form a sub-0.5 cluster (green); [[Starbucks]], [[Chipotle]], and [[Darden Restaurants]] are singletons. The staples (KO/PEP/XLP) and the market (XLY/SPY) cluster separately. No restaurant factor.*

The five names never return as one clean cluster at any threshold. The only intra-cohort join below the cut is McDonald's+Yum! Brands; the other three attach above 0.5, closer to the market (XLY/SPY) than to each other. The packaged-food staples (KO/PEP) form their own cluster, a +0.128 intra-advantage — restaurants are weakly distinct from staples but too loose internally to be a factor.

### Topology — a franchisor pair, then singletons

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | MCD + YUM | 0.433 | the asset-light QSR franchisor pair (the only sub-0.5 join) |
| 2 | CMG + DRI | 0.532 | a loose fast-casual/casual pair, above the cut |
| 3 | SBUX + (CMG+DRI) | 0.603 | Starbucks joins higher |
| 4 | (MCD+YUM) + rest | 0.698 | the two halves merge only at 0.70 |

The only durable micro-structure is McDonald's+Yum! Brands — both global, asset-light franchise-royalty businesses earning a cut of system sales, so they trade on the same royalty-and-unit-growth driver. Everyone else is a singleton whose company-owned same-store-sales story dominates.

### PC1 index weights

![[restaurants-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains only 49.2% with a fat PC2–PC5 tail — multi-factor. Loadings are near-equal (0.42–0.47) but the weak PC1 means there is little common factor to load on.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| McDonald's (MCD) | 0.436 | 19.5% | 16.7% | 28.5% |
| Starbucks (SBUX) | 0.423 | 19.0% | 28.5% | 16.1% |
| Chipotle (CMG) | 0.434 | 19.4% | 39.7% | 11.9% |
| Yum! Brands (YUM) | 0.467 | 20.9% | 21.6% | 23.5% |
| Darden (DRI) | 0.474 | 21.2% | 25.7% | 20.0% |

The low-vol defensive [[McDonald's]] (16.7% vol) takes the largest raw PC1-mimic weight; the high-vol growth name [[Chipotle]] (39.7%) the smallest. The dispersion in volatility (17–40%) is itself a sign of how different these businesses are.

### Distinctness — weak, and not a tradeable factor

![[restaurants-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The warmest cohort cell is McDonald's–Yum! Brands; otherwise the block is tepid, and the names are nearly as warm against XLY/SPY as against each other.*

The intra-advantages are positive but small — +0.128 versus staples, +0.094 versus consumer-discretionary/market — so restaurants are weakly distinct from both, but the 0.364 internal cohesion is too low for a tradeable factor. There is no restaurant basket worth holding as a factor; the names are single-name same-store-sales bets, with the McDonald's/Yum! Brands franchise-royalty pair the one exception.

### Historical tightness evolution

![[restaurants-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. A tight 0.85 in the 2020 COVID lockdown/reopen trade, collapsing through 2021–24 to ~0.31 and holding ~0.32–0.35 since — fragmented and staying fragmented.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.853 | 88.3% |
| 2021 | 0.381 | 51.3% |
| 2022 | 0.630 | 70.5% |
| 2023 | 0.453 | 57.1% |
| 2024 | 0.313 | 47.1% |
| 2025 | 0.318 | 45.7% |
| 2026 | 0.353 | 48.4% |

The arc is the clearest "factor only under a common shock" case in the campaign: in 2020 every restaurant traded on one variable — lockdown severity and reopening pace — and the cohort was a tight 0.85 factor. As that shock faded, the common driver disappeared and the names reverted to their idiosyncratic stories, fragmenting to ~0.32 and staying there. It is the mirror image of [[Managed care]] (which a 2025 shock *re-bound*): the same principle — a sector coheres when a common shock dominates — running in the opposite direction.

## Related

- [[Mercer Street Hospitality]] — NYC multi-concept group (McDonald); Lure Fishbar, Bowery Meat, Seahorse
- [[Frenchette Group]] — NYC French restaurant group (Nasr & Hanson)
- [[Keith McNally]] — iconic NYC restaurateur (Balthazar, Pastis)
- [[Daniel Boulud]] — French fine-dining group (Daniel, Dinex)
- [[DoorDash]] — delivery platform
- [[Chipotle]] — fast-casual leader
- [[Starbucks]] — coffee chain
- [[McDonald's]] — QSR leader
- [[Hotel industry]] — adjacent hospitality sector
