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
| [[AI control-point basket]] names like [[Oracle]], [[Microsoft]], [[Salesforce]] | Those are integrated software/control-point platforms, not neutral edge/runtime vendors |

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

## Related

- [[Anthropic Managed Agents selloff April 2026]]
- [[Software AI bifurcation]]
- [[Edge cloud]]
- [[Agent harnesses]]
- [[Cloudflare]]
- [[Fastly]]
- [[Akamai]]
- [[AI control-point basket]]

*Created 2026-04-14*
