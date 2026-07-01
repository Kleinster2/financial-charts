---
aliases: [Factory automation, Industrial automation, Automation, Factory and industrial automation]
tags: [sector, industrials, automation, robotics, cluster-validation]
---

# Factory automation

> [!warning] Cluster status: NOT a distinct factor — the automation names are broad-industrials beta (= [[XLI]]); the theme fragments by geography, and only a tight US process/control pair [[Rockwell Automation|ROK]]+[[Emerson Electric|EMR]] coheres — itself = XLI (Jun 2026)
> The four automation majors ([[Rockwell Automation|ROK]]/[[Emerson Electric|EMR]]/[[Fanuc|FANUY]]/[[Siemens|SIEGY]]) cohere only loosely (intra 0.506, at the floor; weekly 0.634 once the FANUY/SIEGY ADR async is smoothed) and are NOT distinct from broad industrials: a NEGATIVE −0.120 intra-advantage vs [[XLI]] (the cohort correlates with the industrials ETF 0.625 — MORE than with itself), and −0.157 vs the robotics ETF BOTZ. They beat the random-basket null (p 0.0033 at 10k permutations — real industrials co-movement) but the holdout is WEAKENED 0.77 with an unstable factor structure (loadings-corr 0.48), and the threshold scan is boundary-dependent. It fragments by geography: [[Fanuc|FANUY]] (Japan robotics) and the aerospace conglomerate [[Honeywell|HON]] are singletons; only the US process/control pair [[Rockwell Automation|ROK]]+[[Emerson Electric|EMR]] is tight (0.76) — and even that pair has EXACTLY 0.000 intra-advantage vs [[XLI]] (it IS core industrials). The mirror image of [[Cable broadband|cable]]: where cable escaped its ETF (XLC is Meta/Alphabet-ruled), automation collapses into [[XLI]] because the names ARE XLI. Own XLI. See below.

The label that is just industrials. "Factory automation" groups four companies the market prices as core cyclical industrials — [[Rockwell Automation|Rockwell]] (US control systems), [[Emerson Electric|Emerson]] (US process automation), [[Fanuc]] (Japanese robotics/CNC), and [[Siemens]] (German Digital Industries) — but their shared driver is the broad industrial-capex cycle, not a separable "automation" factor. [[XLI]] is built on exactly that cycle and holds [[Rockwell Automation|ROK]]/[[Emerson Electric|EMR]] near the top, so the cohort cannot out-cohere it. The reshoring / AI-capex / humanoid-robotics narrative is real, but it has not (yet) created a distinct automation factor: the trade is still industrials beta with idiosyncratic geographic stories on top.

## Sector performance

![[automation-performance.png]]
*Normalized total return since 2019 vs broad industrials [[XLI]]. The US names ([[Rockwell Automation|ROK]]/[[Emerson Electric|EMR]]) and [[Siemens|SIEGY]] track XLI closely — they are XLI — while [[Fanuc|FANUY]] (Japan robotics) is the laggard, dragged by the China/Asia automation-capex slump. No distinct "automation" line separates from the industrials benchmark; that visual convergence is the ETF-replicable verdict.*

## Cluster validation

The candidate cohort is the four automation majors — [[Rockwell Automation|ROK]], [[Emerson Electric|EMR]], [[Fanuc|FANUY]], [[Siemens|SIEGY]] — tested against a diversified-industrial conglomerate ([[Honeywell|HON]]), the robotics/AI ETF (BOTZ), broad industrials ([[XLI]] — the key benchmark), and the market ([[SPY]]). 1Y window through 2026-06-22 (199 obs); threshold 0.5; [[Fanuc|FANUY]]/[[Siemens|SIEGY]] are US-listed ADRs (the weekly cross-check covers residual async). Config: `scripts/cluster_configs/automation.yaml`; registry row 2026-06-23. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-corr (1Y) | 0.506 (4-name) / 0.758 (ROK+EMR pair) | At the floor; weekly 0.634 (ADR async-corrected) |
| PC1 explained variance | 63.3% | Moderate |
| Random-basket null p | 0.0006 | Real co-movement — industrials beta |
| Holdout (2Y split) | WEAKENED 0.77, loadings-corr 0.48 | Eroding; unstable factor structure |
| Threshold stable width | 0.00 | [[XLI]]/BOTZ/SPY contaminate — no clean band |
| Intra-adv vs [[XLI]] (industrials) | −0.120 (4-name) / +0.000 (pair) | NEGATIVE / zero — IS broad industrials |
| Intra-adv vs robotics ETF (BOTZ) | −0.157 | = the robotics ETF too |
| Intra-adv vs [[Honeywell\|HON]] | +0.100 | Modestly tighter than the aerospace conglomerate |
| Intra-adv vs market (SPY) | −0.107 | Correlates with SPY more than with itself |

### Boundary — the automation names fuse with the industrials ETF

![[automation-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. [[Rockwell Automation|ROK]]/[[Emerson Electric|EMR]]/[[Siemens|SIEGY]] cluster WITH broad industrials [[XLI]], the robotics ETF BOTZ, and [[SPY]] (one industrials-beta block) — they do not form their own cluster. [[Fanuc|FANUY]] (Japan robotics) is a singleton and [[Honeywell|HON]] (aerospace conglomerate) another — the theme fragments. The only tight join is the US pair [[Rockwell Automation|ROK]]+[[Emerson Electric|EMR]] (0.24).*

The threshold scan returns no clean band: the industrials and robotics ETFs contaminate the cohort cluster, and the intra-advantage over [[XLI]] is negative. The names are XLI constituents ruled by the same industrial-capex factor as the ETF, so they collapse into it — the [[Precious metals royalties|gold-royalties = GDX]] index-rule case, not the [[Analog and auto-industrial semiconductors|analog-semis-in-SMH]] escape that let [[Cable broadband|cable]] separate from XLC.

### Topology — a US pair plus geographic decouplers

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | ROK + EMR | 0.242 | the US process/control pair — the only tight join (corr 0.76) |
| 2 | SIEGY + (ROK+EMR) | 0.508 | [[Siemens\|SIEGY]] (German diversified) joins above the cut |
| 3 | FANUY + core | 0.569 | [[Fanuc\|FANUY]] (Japan robotics) joins last — the decoupler |

The cohesion lives entirely in [[Rockwell Automation|ROK]]+[[Emerson Electric|EMR]] (0.76, both pure US automation). [[Siemens|SIEGY]] (German, diversified across energy/mobility/health) and [[Fanuc|FANUY]] (Japanese robotics, exposed to the China automation-capex slump) attach above the cut, and [[Honeywell|HON]] (aerospace-dominated) decouples entirely. But ROK+EMR carries a +0.000 intra-advantage vs [[XLI]] — the tight pair is not a distinct sub-factor, it is the industrials core.

### PC1 index weights

![[automation-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 63.3% with [[Rockwell Automation|ROK]]/[[Emerson Electric|EMR]] loading highest and [[Fanuc|FANUY]] lowest (the decoupler, also the highest vol at 49%).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| ROK | 0.543 | 27.25% | 30.76% | 30.92% |
| EMR | 0.538 | 27.02% | 32.13% | 29.34% |
| FANUY | 0.437 | 21.93% | 48.76% | 15.70% |
| SIEGY | 0.474 | 23.80% | 34.57% | 24.03% |

### Distinctness — = broad industrials

![[automation-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. Only [[Rockwell Automation|ROK]]–[[Emerson Electric|EMR]] runs warm (0.76); the cross-geography pairs (FANUY/SIEGY) are 0.41–0.52, about the same as the cohort's correlation to [[XLI]] (0.63).*

The decisive number is the negative intra-advantage vs [[XLI]]: −0.120 for the four names, and 0.000 even for the tight ROK+EMR pair. The automation names correlate with broad industrials as much as (or more than) with each other, because they ARE the industrials — [[Rockwell Automation|ROK]] and [[Emerson Electric|EMR]] are top XLI holdings. The robotics ETF BOTZ (−0.157) likewise captures them (and itself trades at 0.82 to the market). There is no automation basket worth owning over [[XLI]].

### Historical tightness evolution

![[automation-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion since 2019. Regime-variable, not durable: a 0.79 peak in the 2020 COVID everything-correlated shock, a 0.33 trough in the 2021 reopening divergence, and oscillating 0.37–0.64 since — it tightens when the whole industrial cycle moves together and loosens otherwise. The signature of a sub-set of one broad factor (industrials), not a standalone automation factor.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2019 | 0.584 | 69.0% |
| 2020 | 0.788 | 84.1% |
| 2021 | 0.326 | 51.3% |
| 2022 | 0.480 | 61.1% |
| 2023 | 0.502 | 62.8% |
| 2024 | 0.372 | 53.7% |
| 2025 | 0.635 | 72.6% |
| 2026 | 0.446 | 59.3% |

## Where this sits in the campaign

Factory automation is a Tier-2 ETF-replicable cohort (= [[XLI]]) and the clean counter-example to [[Cable broadband|cable]], validated the same day. Both turned on the [[Analog and auto-industrial semiconductors|index-rule law]]: cable escaped its only liquid ETF because [[XLC]] is ruled by [[Meta]]/[[Alphabet]] (a different factor); automation collapses into [[XLI]] because [[Rockwell Automation|ROK]]/[[Emerson Electric|EMR]] ARE XLI (the same factor rules both). It also extends the [[Vault cluster taxonomy|driver-divergence law]] across geography — a label spanning US control systems, Japanese robotics, and German diversified industrials fragments, with only the same-country same-business pair (ROK+EMR) cohering. The reshoring/AI-automation narrative has not yet minted a separable factor; for now it is industrials beta.

## Related

- [[Rockwell Automation]], [[Emerson Electric]], [[Fanuc]], [[Siemens]] — the cohort members (ROK+EMR the tight US pair; FANUY/SIEGY the geographic decouplers)
- [[Honeywell]] — the diversified-industrial conglomerate (aerospace-led, decouples); [[XLI]] — broad industrials, the factor the cohort actually is (own this)
- [[Cable broadband]] — the same-day index-rule counter-example (escaped its ETF); [[Building products]], [[Industrial distributors]] — fellow XLI-replicable industrial cohorts
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis; [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-23. 1Y daily log returns through 2026-06-22; config `scripts/cluster_configs/automation.yaml`; registry row 2026-06-23. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
