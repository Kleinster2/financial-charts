---
aliases: [IT Services, IT services and consulting, IT consulting, IT services sector]
tags: [sector, technology, it-services, cluster-validation]
---

# IT services

**IT services** — Outsourced technology services: consulting, systems integration, managed services, BPO. [[EDS]] pioneered the model (1962).

---

## Why IT services matters

$1T+ global market. Key dynamics:

- Outsourcing model: [[EDS]] created "facilities management" (1962)
- Scale matters: Labor arbitrage, global delivery
- Consolidation: Legacy players merging (CSC + HPE ES → [[DXC Technology]])
- Cloud shift: Traditional outsourcing disrupted by hyperscalers

---

## Major players

| Company | Notes |
|---------|-------|
| [[Accenture]] | Largest pure-play |
| [[Capgemini]] | French global IT services / consulting; explicit [[Agentic AI]] transformation bet |
| [[IBM]] | Global Services |
| [[DXC Technology]] | CSC + HPE ES merger |
| [[Infosys]] | India-based |
| [[TCS]] | Tata, India-based |
| [[Wipro]] | India-based |
| [[NTT Data]] | Japan-based |
| [[Cognizant]] | US-listed, India delivery |

---

## AI shifts the budget owner

The live sector debate is no longer "does AI hurt IT services?" in the abstract. It is which part of the services stack gets repriced.

| Layer | AI effect | Sector read |
|-------|-----------|-------------|
| Routine coding, QA, app maintenance, BPO | Agents automate more of the labor input | Bearish for labor-arbitrage models |
| Data cleanup, governance, cloud architecture, security, workflow redesign | AI deployments become more complex and cross-functional | Bullish for firms with C-suite access and industry knowledge |
| Regulated / sovereign deployments | Local data, hosting, compliance, and operational-control requirements increase | Favors large integrators tied to hyperscalers |

The May 27, 2026 [[Capgemini]] Capital Markets Day was a clean expression of the bull case. Capgemini argued that clients are treating AI as a broader operating-model change rather than a standard IT upgrade, which opens spending beyond the CIO's traditional technology budget. Reuters reported management commentary that the opportunity pipeline already exceeded $12B, while the company guided to +5.5% to +7.5% constant-currency revenue CAGR from 2025 to 2028.

That does not negate [[AI disintermediation]]. It narrows it. Commodity implementation work gets cheaper; orchestration, accountability, controls, and business-process redesign become the defended layer. The winners should look less like pure staff-augmentation vendors and more like enterprise-transformation partners with deep client relationships and cloud/model alliances.

*Sources: [Reuters via Investing.com, May 27 2026](https://www.investing.com/news/stock-market-news/capgemini-says-ai-widens-client-spending-pool-4712824); [Capgemini 2026 Capital Markets Day press release](https://investors.capgemini.com/en/publication/2026-capital-markets-day/).*

---

## Sector performance

![[it-services-performance.png]]
*Normalized total return since Jan 2023. The cohort co-moves — and has derated hard against the AI-dominated tech ETF: [[XLK]] is up ~220% on the mega-cap AI rally while the IT-services names are flat-to-down. The higher-beta digital-engineering pair [[EPAM Systems|EPAM]]/[[Globant|GLOB]] is worst (−70% to −80%, the most direct GenAI-disruption proxies); the consulting names [[Accenture|ACN]]/[[Cognizant|CTSH]]/[[Infosys|INFY]] are down 25–45%. This is the +0.597 distinctness made visible (the cohort barely tracks XLK) and the [[AI disintermediation|GenAI repricing]] the section above describes — the market has marked down the labor-arbitrage model even as it bid up the AI-compute layer.*

---

## Cluster validation

> [!success] Cluster status: VALIDATED distinct — a strengthening IT-services/consulting factor almost orthogonal to the tech ETF; one of the campaign's most ETF-distinct cohorts (the core-5; [[Wipro]] the outlier) (Jun 2026)
> The IT-services names ([[Accenture|ACN]]/[[Cognizant|CTSH]]/[[Infosys|INFY]]/[[EPAM Systems|EPAM]]/[[Globant|GLOB]], plus the laggard [[Wipro|WIT]]) trade as a genuine distinct factor. The clean cohort is the core five (ex-Wipro): intra-corr 0.703 (weekly 0.758), PC1 76.4%, rejecting all three nulls at the 0.0001 floor, with a WIDE robust threshold band [0.40–0.70] (width 0.30 — tied with [[Drug distributors]] for the widest in the campaign) and a STRENGTHENING holdout (1.05, loadings-corr 0.97). The distinctness number is exceptional: a +0.597 intra-advantage versus the tech ETF [[XLK]] (the core correlates just 0.106 with it), among the largest in the campaign — the index-rule law in its purest form, because XLK is mega-cap hardware/software (a different factor) so labor/consulting IT-services is nearly orthogonal to it. Also +0.254 vs software ([[IGV]]) and +0.513 vs [[SPY]]. And it is strengthening: rolling cohesion has risen from ~0.46 (2021–22) to 0.71 (2026, latest 90-day 0.774) as the GenAI-repricing narrative above pulls the group together. The full six-name cohort is the same factor with [[Wipro|WIT]] (the chronic Indian-major laggard) as a loose outlier that drags the full-cohort threshold band above the 0.50 cut — the [[Self-storage REITs|self-storage-big-3]] pattern: distinctness lives in the core, not the laggard.

The quantitative complement to the AI-repricing debate above. The sector's defining 2025–26 story — is AI a threat ([[AI disintermediation]]) or a widened spending pool (the [[Capgemini]] bull case) — is exactly what makes IT-services a tradeable factor: the market increasingly prices the whole group on one question, so the names co-move on the narrative rather than on idiosyncratic results. The candidate cohort is six US-listed IT-services/consulting names — [[Accenture|ACN]] (global consulting), [[Cognizant|CTSH]] (US-India), [[Infosys|INFY]] and [[Wipro|WIT]] (Indian majors, US ADRs), [[EPAM Systems|EPAM]] and [[Globant|GLOB]] (digital engineering) — tested against the tech ETF ([[XLK]]), software ([[IGV]]), and the market ([[SPY]]). 1Y window through 2026-06-18 (198 obs), threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary (full six-name cohort)

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.598 [0.331–0.833] | Real; weekly 0.590; WIT the outlier (0.33–0.51) |
| PC1 explained variance | 67.7% | A single factor (weekly 69.0%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0001 | Far beyond a random 6-pick |
| Vol-matched null p (10k) | 0.0001 | Real beyond shared vol |
| Holdout (2Y split) | STABLE 0.935, loadings-corr 0.66 | Durable across regimes |
| Threshold stable width | 0.05 [0.65–0.70] | FRAGILE on the full cohort — WIT joins only at 0.613, above the cut |
| Intra-adv vs tech ETF (XLK) | +0.483 | Huge — almost uncorrelated with the tech ETF (0.114) |
| Intra-adv vs software (IGV) | +0.178 | Distinct from software products |
| Intra-adv vs market (SPY) | +0.409 | A strong sector-specific factor |

Config: `scripts/cluster_configs/it_services.yaml` (full), `sub_it_services_core.yaml` (core-5); registry rows 2026-06-21.

### Boundary — its own cluster, far from the tech/software ETFs

![[it-services-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The IT-services names form their own cluster (green: [[Infosys|INFY]]/[[Accenture|ACN]]/[[Cognizant|CTSH]]/[[EPAM Systems|EPAM]]/[[Globant|GLOB]]), entirely separate from the tech/software/market block {[[XLK]]/[[IGV]]/[[SPY]]} (orange) — the two superclusters merge only at ~0.76, an enormous gap. [[Wipro|WIT]] joins the IT-services side at 0.613 (the outlier, but on the right side).*

On the full six-name cohort the threshold scan returns a stable band only at [0.65–0.70] (width 0.05) — above the cut, because [[Wipro|WIT]] joins only at 0.613. That is a [[Wipro]]-outlier artifact, not a contamination problem: at no threshold do the ETFs enter the cohort cluster (they are a separate branch until 0.76). Dropping WIT resolves it (see the core-5 sub-cohort below).

### Topology — a consulting core, a digital-engineering pair, and a laggard

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | ACN + CTSH | 0.167 | the consulting/services core — tightest pair (corr 0.83) |
| 2 | EPAM + GLOB | 0.245 | the digital-engineering pair (corr 0.76) |
| 3 | (ACN+CTSH) + (EPAM+GLOB) | 0.279 | the core four fuse |
| 4 | INFY + core | 0.361 | Infosys joins — the core five close |
| 5 | WIT + core | 0.613 | [[Wipro\|WIT]] joins last, above the cut — the outlier |

The core five close by 0.361 — a tight, homogeneous block spanning global consulting ([[Accenture|ACN]]), US-India ([[Cognizant|CTSH]]), Indian delivery ([[Infosys|INFY]]), and digital engineering ([[EPAM Systems|EPAM]]/[[Globant|GLOB]]). [[Wipro|WIT]] (corr 0.33–0.51 to the rest) joins only at 0.613.

### PC1 index weights

![[it-services-cluster-pca-1y.png]]
*PCA on the full cohort. PC1 explains 67.7% with even loadings across the core five (0.41–0.45) and a low [[Wipro|WIT]] loading (0.27 — the outlier).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| ACN | 0.443 | 18.30% | 44.02% | 18.50% |
| CTSH | 0.447 | 18.47% | 37.32% | 22.03% |
| INFY | 0.410 | 16.91% | 38.96% | 19.32% |
| WIT | 0.271 | 11.19% | 41.94% | 11.88% |
| EPAM | 0.429 | 17.73% | 51.27% | 15.39% |
| GLOB | 0.421 | 17.40% | 60.15% | 12.87% |

[[Wipro|WIT]] carries the lowest loading (0.27) and weight — the structural confirmation that it is a satellite, not a core member.

### Distinctness — almost orthogonal to the tech ETF

![[it-services-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The core block (ACN/CTSH/INFY/EPAM/GLOB) is warm (0.60–0.83); WIT is cool against it (0.33–0.51); and the whole cohort is strikingly cool against the tech ETF [[XLK]] — the IT-services names barely move with it.*

The defining number is the +0.483 intra-advantage over the tech ETF (the core-5 lifts it to +0.597): the IT-services names correlate only ~0.11 with [[XLK]]. This is the [[Analog and auto-industrial semiconductors|index-rule law]] in its cleanest form — [[XLK]] is dominated by mega-cap hardware/software ([[Apple]]/[[Microsoft]]/[[Nvidia]]), an entirely different factor, so labor/consulting IT-services is nearly orthogonal to it. The cohort is also distinct from software ([[IGV]], +0.178) and the market (+0.409). There is no IT-services ETF — [[XLK]] is hardware/software, [[IGV]] is software products — so the basket is the only way to own the factor.

### Historical tightness evolution — strengthening into the GenAI era

![[it-services-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Unusually, RISING — from ~0.42 (2021) to 0.64 (latest 90-day) on the full cohort, and from ~0.46 to 0.77 on the core five. The IT-services factor is tightening as the market increasingly prices the whole group on the GenAI-repricing question.*

| Year | Avg intra-corr (full 6) | PC1 |
|---|---|---|
| 2021 | 0.418 | 51.9% |
| 2022 | 0.478 | 57.3% |
| 2023 | 0.560 | 63.5% |
| 2024 | 0.544 | 62.2% |
| 2025 | 0.600 | 67.1% |
| 2026 | 0.627 | 69.5% |

*The rising trend is the tell of an emerging factor — the opposite of the commodity/ETF-embedded cohorts that loosen. As AI became the sector's single pricing question (2024–26), the names began moving as one.*

### Sub-cohort — the core five (ex-Wipro): the clean distinct factor

Dropping the [[Wipro|WIT]] outlier isolates the tradeable factor — the [[Self-storage REITs|self-storage-big-3]] / [[Auto parts retail|ORLY+AZO]] pattern:

![[it-services-core-cluster-dendrogram-1y.png]]
*Hierarchical clustering of the core five at 0.5. Two clean clusters — the IT-services five (orange, closing at 0.361) and the ETF/market block (green) — merging only at ~0.76. A wide, clean separation.*

| Diagnostic | Full 6 | Core 5 (ex-Wipro) |
|---|---|---|
| Intra-corr (1Y) | 0.598 | 0.703 (weekly 0.758) |
| PC1 | 67.7% | 76.4% (weekly 80.9%) |
| Intra-adv vs XLK | +0.483 | +0.597 |
| Intra-adv vs IGV | +0.178 | +0.254 |
| Threshold band | [0.65–0.70] w0.05 (FRAGILE) | [0.40–0.70] w0.30 (ROBUST) |
| Holdout | STABLE 0.935 | STRENGTHENING 1.05 (loadings-corr 0.97) |

The core five clear every bar decisively: a WIDE robust band (width 0.30, tied with [[Drug distributors]] for the campaign's widest), a STRENGTHENING holdout with near-identical factor structure across regimes (loadings-corr 0.97), and a +0.597 intra-advantage over the tech ETF. This is a distinct, durable, and strengthening IT-services factor. [[Wipro|WIT]] is the loose satellite — own the core, not the laggard.

## Where this sits in the campaign

A new distinct factor, and an unusual one: most of the campaign's distinct cohorts are stable or loosening; IT-services is strengthening. It joins the set of cohorts that are distinct because they sit inside an ETF ruled by a different factor — [[Analog and auto-industrial semiconductors|analog semis]] (distinct from the AI-dominated [[SMH]]), and now IT-services (distinct from the mega-cap-dominated [[XLK]]). The +0.597 core-5 intra-advantage over [[XLK]] ranks with the campaign's most ETF-distinct cohorts ([[Drug distributors]] +0.502, [[Tankers]] +0.483). The shared driver — enterprise IT budgets repriced by GenAI — is a labor/consulting story no technology ETF captures.

---

## Live factor test — the Accenture print (Jun 18 2026)

The cluster thesis got a clean out-of-sample test on the final day of the validation window. On Jun 18 2026 [[Accenture|ACN]] cut full-year revenue-growth guidance (to ≤4% from 3–5%) and reported Q3 new bookings of $19.3bn (−3% YoY); the stock fell 18% to its lowest since 2017, market cap from >$200bn to <$80bn (see [[Accenture]]). The validated factor fired exactly as specified — the cohort sold off in sympathy on a day the market and the tech ETF *rose*.

| Name | 1-day move | Raw σ | Abnormal vs [[SPY]] | Abnormal vs [[XLK]] |
|---|---|---|---|---|
| [[Accenture\|ACN]] | −18.0% | −6.9 | −19.0% (−7.3σ) | −21.0% |
| [[EPAM Systems\|EPAM]] | −12.6% | −4.1 | −13.7% (−4.5σ) | −15.6% |
| [[Globant\|GLOB]] | −11.2% | −3.3 | −12.2% (−3.6σ) | −14.2% |
| [[Cognizant\|CTSH]] | −10.5% | −4.7 | −11.5% (−5.2σ) | −13.5% |
| [[Infosys\|INFY]] | −9.7% | −4.5 | −10.7% (−4.9σ) | −12.7% |
| [[Wipro\|WIT]] | −3.6% | −1.5 | −4.7% | −6.7% |
| [[XLK]] (tech ETF) | +3.0% | +2.1 | +2.0% | — |
| [[IGV]] (software) | −0.1% | — | −1.1% | −3.1% |
| [[SPY]] (market) | +1.0% | — | — | −2.0% |

*Event-day reaction (06-17 → 06-18 close); own-vol from the trailing 1Y excluding the event day. Source: `prices_long`; [[Financial Times|FT]] (Stephen Foley), Jun 18 2026.*

Three things the tape confirms about the validated factor:
- Co-movement on the narrative, not on own results. [[Cognizant|CTSH]], [[Infosys|INFY]], [[EPAM Systems|EPAM]] and [[Globant|GLOB]] had no material news of their own yet fell 9.7–12.6% (3–5σ) on ACN's print — the "names move on the shared question" mechanism the cluster identified.
- Orthogonality to the tech ETF, made real. The cohort fell ~10–18% while [[XLK]] *rose 3%* and software ([[IGV]]) was flat — almost the entire move is abnormal versus the tech complex (ACN −21% vs XLK). The +0.597 core-5 intra-advantage over XLK is exactly this: the shared driver (GenAI repricing the labor-arbitrage model) is a factor the mega-cap-dominated tech ETF does not price.
- The core-vs-satellite split, live. [[Wipro|WIT]] — the loose outlier excluded from the core-5 — fell only 3.6% (−1.5σ), a fraction of the core's move, confirming it does not belong to the tight factor.

This is the [[AI disintermediation]] thesis crossing from sentiment to fundamentals: the Feb 2026 IT-services selloffs were narrative repricings; this was a guidance cut and a bookings decline. The validated factor is now the cleanest way to express the view that GenAI is repricing the labor-arbitrage services model.

---

## Historical players

| Company | Fate |
|---------|------|
| [[EDS]] | → HP (2008) → DXC (2017) |
| [[Computer Sciences Corporation\|CSC]] | → DXC (2017) |
| [[Perot Systems]] | → Dell (2009) → NTT Data (2016) |
| [[HPE Enterprise Services]] | → DXC (2017) |

---

## Related

- [[EDS]] — industry pioneer
- [[DXC Technology]] — major consolidation
- [[Accenture]] — market leader
- [[Capgemini]] — AI transformation / OpenAI Frontier partner
- [[Cloud computing]] — disrupting traditional outsourcing
- [[Enterprise AI adoption]] — demand driver
- [[AI disintermediation]] — automation threat
