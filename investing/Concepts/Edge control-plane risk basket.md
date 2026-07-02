---
aliases:
  - ECPR
  - AI edge control-plane risk basket
tags:
  - basket/internal
  - ai
  - infrastructure
  - edge
---

# Edge control-plane risk basket

> [!failure] Cluster status: FALSIFIED out of sample (formal, 2026-07-02) — the framework's first and clearest OOS falsification
> Formally downgraded from "weak cluster" at the July capstone pass, on 40 post-definition observations: in-sample intra 0.468 collapsed to 0.042 out of sample (ratio 0.085), and random baskets from the verified clean pool beat the cohort on 59% of draws (p_oos 0.588). The cohort passed every in-sample diagnostic (random-basket p 0.0123, BH-pass) and then simply stopped existing on unseen data — precisely the selection-on-the-dependent-variable failure the post-definition OOS pass was built to catch. The May 2026 in-sample read (intra 0.47, PC1 64.8%, all three names singletons at the cut) already flagged it as event-driven rather than structural; the OOS data settles it. Treat FSLY/AKAM/NET co-movement as a narrative-shock artifact, not a basket. See "Cluster validation — weak cluster confirmed" section below and the [[2026-06-15-cluster-validation-capstone|June capstone]] for the arc.

Plain English: not all AI infrastructure is safe just because AI traffic grows. If model vendors bundle execution, state, permissions, and tracing into their own hosted agent runtimes, the edge layer closest to that control plane can get repriced hard.

This basket tracks the public edge cluster most exposed when the market decides that value may migrate upstream from neutral runtime vendors to the model provider itself.

---

## What it is testing

The old simplification was: application software loses, infrastructure software wins.

[[Anthropic Managed Agents selloff April 2026]] broke that frame. The better question is whether the edge vendor owns a durable network/perimeter function, or whether the higher-multiple part of the story was really a claim on the agent control plane.

This basket isolates that risk cluster.

---

## Constituents

Move-weighted from the Apr 10, 2026 Managed Agents selloff. Bigger drop = higher weight.

| Ticker | Company | Weight | Apr 9 close | Apr 10 close | Move | Why it belongs |
|--------|---------|--------|-------------|--------------|------|----------------|
| FSLY | [[Fastly]] | 42% | $29.46 | $23.07 | -21.7% | Most levered to developer-facing edge execution and programmable runtime narrative |
| AKAM | [[Akamai]] | 32% | $109.61 | $91.35 | -16.7% | Enterprise delivery and security incumbent, but still exposed where runtime/control-plane value was being capitalized |
| NET | [[Cloudflare]] | 26% | $193.05 | $166.99 | -13.5% | Broadest neutral edge platform, including AI-facing services and agentic workload pitch |

Total: 100% — 3 constituents, move-weighted

---

## What it is not

| Excluded | Why excluded |
|----------|--------------|
| [[Amazon]], [[Microsoft]], [[Google]] | Hyperscalers are much broader than the edge-runtime readthrough |
| [[CrowdStrike]], [[Palo Alto Networks]], [[Zscaler]] | Security names with overlapping AI narratives, but not the core edge-control-plane cluster |
| Integrated software platforms like [[Oracle]], [[Microsoft]], [[Salesforce]] | Those are data / distribution / identity platforms, not neutral edge/runtime vendors — see [[Software AI bifurcation]] for the split |

---

## Index methodology

- Ticker: ECPR
- Weighting: Move-weighted from Apr 10, 2026 selloff magnitude
- Base date: Apr 9, 2026 = 100
- History: Sep 13, 2019 – Apr 10, 2026 (common history and latest common close)
- Calculation: Price return
- Data source: `prices_long` in `market_data.db`
- Script: `scripts/create_ecpr_index.py --store`

---

## Early read

As of the latest common close on Apr 10, 2026, ECPR is down 18.0% from the Apr 9 base date.

| Ticker | Apr 9 to Apr 10 move |
|--------|-----------------------|
| NET | -13.5% |
| FSLY | -21.7% |
| AKAM | -16.7% |
| ECPR | -18.0% |

That is a real factor move, not noise. The market was not saying edge demand disappears. It was saying the higher-multiple control-plane layer might sit closer to the frontier lab than to the neutral edge vendor.

---

## Persistence check (2020-2026)

Pairwise excess-return correlation (vs [[SPY]]) across multi-year periods. Benchmark: [[Security control points]] core runs 0.30-0.51 historically.

| Period | Avg pair corr | Read |
|--------|---------------|------|
| 2020 H2 | 0.20 | Weak |
| 2021 | 0.29 | Mild |
| 2022 | 0.32 | Moderate |
| 2023 | 0.22 | Weak |
| 2024 H1 | 0.12 | Weak |
| 2024 H2 | 0.51 | Moderate |
| 2025 H1 | 0.19 | Weak |
| 2025 H2 | 0.22 | Weak |
| 2026 YTD | 0.52 | Elevated (Apr 10 event + aftershocks) |

ECPR is an intermittent cluster. [[Fastly]], [[Akamai]], and [[Cloudflare]] travel together in some windows (2022, 2024 H2, 2026 YTD) and diverge in others (2024 H1, 2025). That fits the business-model read: all three are edge vendors, but their customer bases, revenue mixes, and AI-narrative exposure differ enough that they do not behave as a permanent factor. The cluster tightens when the market is repricing edge runtime narrative as a group, then loosens back into three semi-independent stories.

This is a weaker persistence pattern than [[Security control points]] and a stronger one than the event-derived cohort of [[February 2026 AI Disruption Cascade]] victims. The basket is most useful as a risk factor that turns on during control-plane narrative shocks, not as a claim that the three names always move together.

---

## Why this matters

This is the basket that tests the weakest part of the "AI infrastructure" umbrella. If future model launches keep hitting ECPR on execution and orchestration readthroughs, then the taxonomy is right: delivery and perimeter are durable, but runtime/control-plane narrative premium is fragile.

If instead ECPR quickly recovers on enterprise results and spending data, that would argue the selloff was too aggressive and that customers still want a vendor-neutral control layer.

---

## Tracking questions

Watch for:
- future model-vendor launches that bundle more hosted runtime features
- whether [[Cloudflare]] and [[Akamai]] recover faster than [[Fastly]] because delivery/perimeter functions are stickier
- whether enterprise buyers prefer multi-model neutrality over provider-native agent stacks
- how management teams talk about orchestration, state, tracing, and permissions on earnings calls

---

## Cluster validation — weak cluster confirmed (May 2026)

Re-validation via `scripts/cluster_analysis.py --config scripts/cluster_configs/ecpr.yaml` (full procedure in `docs/cluster-validation.md`) confirms the note's own prior assessment ("intermittent cluster, weaker than [[Security control points]]").

Result: weak cluster. Intra-cluster correlation 0.47 (below the 0.50 floor), PC1 64.8%. Hierarchical clustering at 0.4 returns ALL THREE names as singletons — no ECPR cluster forms at the standard threshold. The cluster is real on event days but does not sustain as a durable structural grouping.

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation (1Y) | 0.47 (range 0.42-0.55) | Weak — fails the 0.50 cluster floor |
| PC1 explained variance | 64.8% | Dominant single factor exists but cluster too loose |
| Hierarchical clustering at 0.4 | All 3 singletons (FSLY, AKAM, NET) | Cluster does not form at standard threshold |
| Cluster vs SCP core (CRWD, PANW, ZS) | 0.37 | Edge ≠ control points; small +0.10 separation |
| Cluster vs hyperscalers (MSFT, GOOGL, AMZN) | 0.11 | Clear +0.36 separation — confirms edge is its own factor |
| Cluster vs broad ETFs (IGV, XLK, SPY) | 0.20-0.29 | Edge factor is distinct from broad market |

PC1 loadings are tight (FSLY 0.59, AKAM 0.60, NET 0.54) — the three names DO share a common factor, but the loading is muted by their idiosyncratic stories (FSLY = developer-edge pure-play, AKAM = enterprise-CDN incumbent, NET = AI-enabled platform). The note's framing is correct: the basket is a *risk factor that turns on during control-plane narrative shocks*, not a permanent cluster. Use as event-driven trade, not a structural basket.

---

## Cluster validation compliance addendum (2026-06-07)

Generated from `scripts/cluster_configs/ecpr.yaml` using `scripts/cluster_analysis.py` methodology. The 1Y diagnostic window is 2025-05-01 to 2026-04-30 (171 observations); the rolling history starts at `2020-01-01` where data are available.

### Required validation plots

![[ecpr-cluster-correlation-1y.png]]

*One-year correlation heatmap for the `Edge control-plane risk basket (ECPR)` validation universe.*

![[ecpr-cluster-dendrogram-1y.png]]

*Hierarchical clustering tree using average linkage on distance `1-|corr|`.*

![[ecpr-cluster-pca-1y.png]]

*PCA diagnostic for the candidate cohort; PC1 explains 64.5% of standardized daily-return variance.*

### PC1 index weights vs cluster topology

The topology table answers which names join the tree first or last. The raw PC1-mimic table answers which raw-return weights best replicate the standardized common factor after realized-volatility scaling. These are deliberately different readings of the same cluster.

| Step | Left | Right | Distance (1-\|corr\|) | Read |
|---|---|---|---|---|
| 1 | FSLY | AKAM | 0.459 | Tightest merge |
| 2 | NET | FSLY+AKAM | 0.570 | Final cohort join / loosest boundary |

| Ticker | PC1 loading | Normalized loading weight | Ann. vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| FSLY | 0.590 | 34.07% | 111.19% | 19.98% |
| AKAM | 0.596 | 34.46% | 51.52% | 43.63% |
| NET | 0.545 | 31.47% | 56.42% | 36.39% |

Interpretation: use the dendrogram / join-distance topology to identify the tight core and later-joining members; use the Raw PC1-mimic weight column only for investable factor-replication sizing.

### Historical tightness evolution

![[ecpr-cluster-rolling-tightness-90d.png]]

*Ninety-day rolling tightness diagnostic: avg intra-correlation, PC1 share, core correlation, satellite-to-core correlation, and final candidate join distance.*

| Year | Avg corr median | PC1 median | Core corr median | Satellite-to-core median | Final join distance median |
|---|---|---|---|---|---|
| 2021 | 0.472 | 65.4% | 0.472 | n/a | 0.603 |
| 2022 | 0.508 | 67.4% | 0.508 | n/a | 0.549 |
| 2023 | 0.577 | 72.1% | 0.577 | n/a | 0.509 |
| 2024 | 0.346 | 56.7% | 0.346 | n/a | 0.688 |
| 2025 | 0.431 | 62.2% | 0.431 | n/a | 0.608 |
| 2026 | 0.376 | 58.5% | 0.376 | n/a | 0.656 |

Latest 90D through 2026-04-30: avg corr 0.556, PC1 70.5%, core corr 0.556, satellite-to-core corr n/a, final join distance 0.480.

Historical verdict: regime-dependent but measurable cluster; cohesion exists, but the rolling path is not consistently tight enough to call structurally durable.

---

## Related

- [[Anthropic Managed Agents selloff April 2026]]
- [[Software AI bifurcation]]
- [[Edge cloud]]
- [[Agent harnesses]]
- [[Cloudflare]]
- [[Fastly]]
- [[Akamai]]
- [[Security control points]] — adjacent cluster (similarly partial validation)

*Created 2026-04-14*
*Cluster validation 2026-05-03 — weak cluster confirmed (intra-corr 0.47, PC1 64.8%, all 3 singletons at 0.4 threshold)*
