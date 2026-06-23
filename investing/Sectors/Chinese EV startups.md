---
aliases: [Chinese EV startups, China EV, Chinese EVs, China EV startups, Chinese electric vehicles cohort, China EV pure-plays]
tags: [sector, automotive, china, electric-vehicles, cluster-validation]
---

# Chinese EV startups

> [!warning] Cluster status: validated cohesion, durable — but ETF-replicable: the cohort is [[China]] beta ([[FXI]]) with an EV-volatility tilt, distinct from the US EV complex yet out-cohering neither that ETF nor the EV ETF [[KARS]] (Jun 2026)
> The three US-listed Chinese EV pure-plays ([[NIO]]/[[Xpeng|XPEV]]/[[Li Auto|LI]]) form a real, remarkably even factor (all three pairs ~0.54; intra 0.544, PC1 69.6%) that beats the random-basket null (p 0.0029) and the vol-matched null (p 0.0009) and is exceptionally durable (holdout STABLE 0.98 — intra barely moves across the 2-year split). It is genuinely distinct from the US EV complex: +0.246 vs [[Tesla|TSLA]] and +0.255 vs the US startups [[Lucid|LCID]]/[[Rivian|RIVN]] — Chinese EVs do NOT trade as generic "unprofitable EV-startup beta," jurisdiction segments the trade. The factor extends to the giant [[BYD|BYDDY]] (joins at 0.50), giving a clean four-name China-EV cluster that stands apart from Tesla, the US startups, the EV ETF, and the market in the dendrogram. BUT it is ETF-replicable: it does not out-cohere the EV ETF [[KARS]] (+0.02 — and KARS, Tesla-dominated, clusters with TSLA/market not the cohort) and is essentially China beta — [[FXI]] (China large-cap) sits INSIDE the four-name cluster (intra-advantage −0.026), and the names correlate with FXI (0.54) as much as with each other. The one-line read: a Chinese EV stock is more a China stock than an EV stock. See below.

The jurisdiction trade wearing an EV costume. [[NIO]] (premium BEV), [[Xpeng|XPeng]] (mass-market + ADAS), and [[Li Auto|Li Auto]] (EREV, the only consistently profitable one) are different companies on different powertrain and margin paths — yet they move as one, and they move with [[China]], not with electric vehicles. The shared driver is the same exogenous country factor that rules [[Chinese internet|the China internet ADRs]] — China stimulus on/off, [[US-China decoupling|US–China tension]], [[EU-China EV tariffs|tariff]] headlines, ADR sentiment — overlaid on extreme EV-startup volatility (40–61% annualized). When that country factor is loudest the cohort fuses; the 2021–22 EV bubble-and-crash had them at 0.80–0.86. The contrast with [[Chinese internet]] is the instructive part: that cohort had a dedicated ETF ([[KWEB]]) that captured it exactly; the China-EV names have none — [[KARS]] is global and Tesla-led — so they default to broad China beta ([[FXI]]) instead.

## Sector performance

![[china-ev-performance.png]]
*Normalized total return since Jan 2021 vs the EV ETF [[KARS]] (purple) and China large-cap [[FXI]] (cyan). The cumulative dispersion is enormous — [[NIO]] ~−90%, [[Xpeng|XPEV]] ~−66%, [[Li Auto|LI]] the best startup, while the profitable giant [[BYD|BYDDY]] (orange) stayed near flat and the ETFs held up far better — yet daily returns co-move at 0.54. That return-vs-correlation gap is the whole verdict: the names diverge wildly on fundamentals (cash-burn vs profit, BEV vs EREV) but co-move daily on the shared China factor [[FXI]] threads through, while the EV ETF [[KARS]] sits with Tesla, not the cohort.*

## Cluster validation

The candidate cohort is the three US-listed Chinese EV pure-plays — [[NIO]], [[Xpeng|XPEV]], [[Li Auto|LI]] — tested against the US EV leader ([[Tesla|TSLA]]), the profitable Chinese giant ([[BYD|BYDDY]]), the US EV startups ([[Lucid|LCID]]/[[Rivian|RIVN]] — the key control: same business model, different jurisdiction), the EV/mobility ETF ([[KARS]]), broad auto ([[CARZ]]), China large-cap ([[FXI]]), and the market ([[SPY]]/[[QQQ]]). 1Y window through 2026-06-18 (198 obs); threshold 0.5. The thesis cohort behind [[Chinese EVs enter US]], and the second sector-scale framework test outside US-listed cohorts. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.544 (3-name) / 0.533 (4-name +BYD) | Above the floor; pairs near-identical (0.54-0.55); weekly 0.476 |
| PC1 explained variance | 69.6% (3-name) | Solid single factor; near-equal loadings (0.573-0.580) |
| Random-basket null p (10k) | 0.0029 | Real cohesion — beats a random 3-pick |
| Vol-matched null p (10k) | 0.0009 (intra), 0.0012 (PC1) | Not just shared high-vol beta — a real factor |
| Holdout (2Y split) | STABLE 0.98, loadings corr 0.92 | Exceptionally durable — intra 0.552→0.543 |
| Threshold stable width | 0.00 | But contaminant is the SIBLING [[BYD\|BYDDY]] (0.50) then [[FXI]]; ETFs/Tesla only at 0.65 |
| Intra-adv vs [[Tesla\|TSLA]] | +0.246 | Distinct from the US EV leader |
| Intra-adv vs US startups (LCID/RIVN) | +0.255 | NOT generic EV-startup beta — jurisdiction segments it |
| Intra-adv vs broad auto ([[CARZ]]) | +0.117 | Modestly distinct from global autos |
| Intra-adv vs EV ETF ([[KARS]]) | +0.023 | ≈ZERO — does not out-cohere the EV ETF |
| Intra-adv vs China large-cap ([[FXI]]) | +0.006 (3-name) / −0.026 (4-name) | ≈ZERO/NEGATIVE — it IS China beta |

Config: `scripts/cluster_configs/china_ev.yaml` (+ `sub_china_ev_byd.yaml` for the 4-name); registry rows 2026-06-22.

### Boundary — distinct from US EV, but China beta sits inside

![[china-ev-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5 (3-name config). The China-EV names [[NIO]]/[[Xpeng|XPEV]]/[[Li Auto|LI]] + [[BYD|BYDDY]] form one clean cluster (orange/green at left, all four joining by ~0.475) that stands cleanly apart from the entire US EV complex — the US startups [[Lucid|LCID]]/[[Rivian|RIVN]] (a separate pair) and the [[Tesla|TSLA]]/[[KARS]]/[[CARZ]]/market pole (right, green). The EV ETF [[KARS]] sits with Tesla and the market, NOT with the cohort — it holds the Chinese names but is Tesla-dominated, so it tracks the global-EV/Tesla factor. The two complexes only merge at ~0.64.*

The threshold scan returns no clean band, but for a benign reason: the only name joining the three startups at the 0.50 cut is [[BYD|BYDDY]] — a China-EV sibling, not a contaminant — and in the four-name run the next to join is [[FXI]] (China large-cap). The actual outside controls ([[Tesla|TSLA]], [[KARS]], the US startups) do not enter until 0.65. So the cohort is a clean, separable China-EV cluster against the US EV complex; what it cannot separate from is China itself. [[FXI]] sitting inside the four-name cluster (intra-advantage −0.026) is the verdict: this is China-country beta with an EV-volatility overlay, and no China-EV-specific ETF exists to price it (only [[KARS]], which is Tesla-led).

### Topology — an equal-weight trio plus the giant

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | NIO + XPEV | 0.445 | the two cash-burning premium/mass BEV makers (corr 0.55) |
| 2 | LI + (NIO+XPEV) | 0.462 | [[Li Auto\|Li Auto]] (profitable EREV) joins — the trio closes just below the cut |
| — | + BYDDY | ~0.50 | the giant [[BYD\|BYDDY]] joins the cluster (4-name intra 0.533) |

The three startups are an unusually even cohort — every pair is 0.54–0.55, PC1 loadings 0.573–0.580 (near-identical), no tight core or outlier, because the shared China factor dominates each name's idiosyncratic powertrain/margin story equally. [[BYD|BYDDY]] (the profitable, vertically-integrated, battery-making giant — a different business entirely) still joins at 0.50, because it too is priced off the China-EV factor. The cohesion is split 70/30 between the shared factor (PC1 69.6%) and idiosyncratic variance (PC2+PC3 30%).

### PC1 index weights — even loadings, extreme vol

![[china-ev-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 69.6% — a solid single "China EV" factor with near-identical loadings (0.573–0.580). Annualized vols are extreme (40–61%); [[Li Auto|LI]] (the profitable one) is the least volatile, [[NIO]] the most.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| [[NIO]] | 0.580 | 33.49% | 61.45% | 27.67% |
| [[Xpeng\|XPEV]] | 0.579 | 33.40% | 56.44% | 30.04% |
| [[Li Auto\|LI]] | 0.573 | 33.11% | 39.75% | 42.29% |

### Distinctness — ≠ US EV, but = China × EV

![[china-ev-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The three startups run an even ~0.54 with each other and with [[BYD|BYDDY]]; they are cool to [[Tesla|TSLA]] (0.30) and the US startups [[Lucid|LCID]]/[[Rivian|RIVN]] (0.29), but warm to [[FXI]] (0.54) — as warm as to each other.*

Two findings, and together they place the cohort exactly. Against the US EV complex the intra-advantage is strongly positive: +0.246 vs [[Tesla|TSLA]], +0.255 vs the US startups [[Lucid|LCID]]/[[Rivian|RIVN]]. The China-EV names do not trade with their US business-model twins — the same jurisdiction-over-business-model result found for [[Chinese internet]]. But against the two ETFs that bracket the trade the advantage vanishes: +0.023 vs the EV ETF [[KARS]] and +0.006 / −0.026 vs China large-cap [[FXI]]. The cohort correlates with broad China (0.54) as much as with itself, so it does not earn distinctness over [[FXI]]; and it is no tighter than [[KARS]]. The China-EV factor is the intersection of China-country beta and EV-sector beta — distinct from US EVs because it carries the China factor they lack, distinct from broad China only by its EV volatility — and each of those is an existing ETF. Own [[FXI]] for the China tilt or [[KARS]] for the EV tilt; the bespoke basket adds no edge.

### Historical tightness evolution — a bubble factor that stayed durable

![[china-ev-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion since the three startups were all listed (late 2020). The arc: extreme tightness (0.80–0.86) through the 2021–22 EV bubble and crash, when the China-EV-startup trade moved as one speculative-growth block, loosening as the names diverged (Li Auto to profit, NIO/XPeng still burning cash) — but stabilizing at ~0.54, above the floor, where it has held durably (holdout STABLE 0.98).*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.800 | 86.7% |
| 2022 | 0.858 | 90.5% |
| 2023 | 0.718 | 81.2% |
| 2024 | 0.537 | 69.4% |
| 2025 | 0.540 | 69.4% |
| 2026 | 0.553 | 70.3% |

*Like [[Chinese internet]], the cohort was tightest under stress (the 2021–22 bubble/crash, analogue of the internet cohort's 2022 crackdown peak) and loosened as the shock faded. Unlike Chinese internet, it stopped loosening above the floor (~0.54) and stayed there — a durable factor, not a regime-dependent one. The weekly cross-check (0.476 vs daily 0.544) holds up far better than the internet cohort's (0.29 vs 0.49), another sign the daily co-movement is a real shared factor.*

## Where this sits in the campaign

Chinese EV startups is the campaign's second sector-scale test outside US-listed cohorts, and it rhymes with the first:

- It is Tier 2 — real, durable cohesion (beats both nulls, STABLE 0.98 holdout) but ETF-replicable. Where [[Chinese internet]] resolves to one dedicated ETF ([[KWEB]]), China EV resolves to the intersection of two — China beta ([[FXI]]) and EV beta ([[KARS]]) — out-cohering neither. No China-EV-specific ETF exists, so the names default to broad China beta.
- The jurisdiction-over-business-model law holds a second time: +0.246 vs [[Tesla|TSLA]] and +0.255 vs the US EV startups. Chinese EVs are not "EV beta"; they are China beta with EV volatility. The same five-business-models / same-jurisdiction logic from [[Chinese internet]], now in autos.
- The [[Vault cluster taxonomy|index-rule law]] is confirmed from the ETF side: [[KARS]] holds the Chinese names but is ruled by Tesla/global mobility, so it clusters with TSLA, not the cohort — the analog-semis-inside-[[SMH]] pattern. The difference from gold-royalties=GDX is why China internet (=KWEB, same-factor ETF) collapsed cleanly while China EV stays a hair apart from its sector ETF — but lands on [[FXI]] instead.

## Related

- [[NIO]], [[Xpeng]], [[Li Auto]] — the cohort members (an even trio, no core/outlier); [[BYD]] — the profitable giant that shares the factor (joins at 0.50)
- [[Tesla]], [[Lucid]], [[Rivian]] — the US EV complex the cohort does NOT trade with (+0.25 — jurisdiction beats business model)
- [[FXI]] — China large-cap, the factor the cohort actually IS (own this for the China tilt); [[KARS]] — the EV/mobility ETF (Tesla-led, own for the EV tilt); [[CARZ]] — broad global autos
- [[Chinese internet]] — the sibling China-ADR cohort (= [[KWEB]]); same jurisdiction-beats-business-model result
- [[Chinese EVs enter US]] — the thesis; [[EU-China EV tariffs]], [[Reverse tech transfer in China auto]], [[China battery leverage]] — the China-EV drivers
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis; [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-22. 1Y daily log returns through 2026-06-18; configs `scripts/cluster_configs/china_ev.yaml` + `sub_china_ev_byd.yaml`; registry rows 2026-06-22. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
