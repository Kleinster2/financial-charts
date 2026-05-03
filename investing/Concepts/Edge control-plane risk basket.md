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

> [!warning] Cluster status: weak cluster (May 2026)
> Intra-cluster correlation 0.47 (below the 0.50 floor), PC1 64.8%. Hierarchical clustering at 0.4 returns ALL THREE names (FSLY, AKAM, NET) as singletons — no cluster forms at the standard threshold. The basket is a risk factor that turns on during control-plane narrative shocks (event-driven), not a permanent structural cluster. See "Cluster validation — weak cluster confirmed" section below.

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

**Result: weak cluster.** Intra-cluster correlation 0.47 (below the 0.50 floor), PC1 64.8%. Hierarchical clustering at 0.4 returns ALL THREE names as singletons — no ECPR cluster forms at the standard threshold. The cluster is real on event days but does not sustain as a durable structural grouping.

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation (1Y) | **0.47** (range 0.42-0.55) | Weak — fails the 0.50 cluster floor |
| PC1 explained variance | **64.8%** | Dominant single factor exists but cluster too loose |
| Hierarchical clustering at 0.4 | All 3 singletons (FSLY, AKAM, NET) | Cluster does not form at standard threshold |
| Cluster vs SCP core (CRWD, PANW, ZS) | 0.37 | Edge ≠ control points; small +0.10 separation |
| Cluster vs hyperscalers (MSFT, GOOGL, AMZN) | 0.11 | Clear +0.36 separation — confirms edge is its own factor |
| Cluster vs broad ETFs (IGV, XLK, SPY) | 0.20-0.29 | Edge factor is distinct from broad market |

PC1 loadings are tight (FSLY 0.59, AKAM 0.60, NET 0.54) — the three names DO share a common factor, but the loading is muted by their idiosyncratic stories (FSLY = developer-edge pure-play, AKAM = enterprise-CDN incumbent, NET = AI-enabled platform). The note's framing is correct: the basket is a *risk factor that turns on during control-plane narrative shocks*, not a permanent cluster. Use as event-driven trade, not a structural basket.

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
