---
aliases: [PLAT_CYBER, Platform cyber, Cyber platform basket, PXSEC]
tags: [basket/internal, cybersecurity, ai, infrastructure]
---

# Platform cyber basket

> [!success] Cluster status: validated (May 2026)
> Intra-cluster correlation 0.71, PC1 80.7% explained variance. Hierarchical clustering at 0.4 returns CRWD + PANW + ZS plus algorithmic adjacencies (OKTA, S, TENB, SNOW, IGV). The 3-name tight core surfaced in BOTH [[Security control points]] partial validation and [[Cybersecurity consolidation]] falsification — surfacing twice in independent tests is strong mathematical evidence the cluster is real. See "Cluster validation" section below.

The mathematically-validated 3-name tight core inside the broader cyber complex. Surfaced twice in independent cluster-validation tests:

1. The [[Security control points]] partial-validation test ran the SCP "structural core" of 6 names (CRWD, FTNT, NET, PANW, RBRK, ZS) and found that only CRWD/PANW/ZS clustered tightly at the 0.4 threshold; FTNT/NET/RBRK were standalones.
2. The [[Cybersecurity consolidation]] falsification test ran the strategic "consolidator" cohort (PANW, CRWD, MSFT, CSCO) and found the same result: PANW + CRWD form the algorithmic cluster (with ZS pulled in from controls); MSFT/CSCO trade as singletons.

The two tests had different starting points (control-points framework vs M&A-consolidator framework) and pulled in different control universes. Both surfaced CRWD + PANW + ZS as the consistent algorithmic cluster. That convergence is the mathematical signature of a real factor: the cluster boundary is robust across different test designs.

---

## Constituents

3 names. Equal-weighted starting point.

| Ticker | Company | PC1 loading | Why it belongs |
|--------|---------|-------------|----------------|
| CRWD | [[CrowdStrike]] | 0.598 | Endpoint + cloud platform; bellwether for the sub-sector |
| PANW | [[Palo Alto Networks]] | 0.567 | Most aggressive M&A consolidator; multi-product platform (network, cloud, SOC, identity post-CyberArk) |
| ZS | [[Zscaler]] | 0.566 | Cloud-native zero-trust platform; secure access leader |

Total: 3 constituents. Internal ticker proposal: PXSEC.

### Algorithmic adjacencies (pulled in at 0.4 threshold but NOT in the tight core)

The hierarchical clustering at 0.4 threshold also pulls in five names that are not in the tight 3-name candidate cohort:

| Ticker | Company | Why it joins | Hold-status decision |
|---|---|---|---|
| OKTA | [[Okta]] | Identity is adjacent control surface; OKTA platform is multi-product like the core | Algorithmic adjacency — track but do not put in core basket |
| S | [[SentinelOne]] | AI-native endpoint platform; competes with CRWD directly | Algorithmic adjacency — same end-market as CRWD |
| TENB | [[Tenable]] | Vulnerability management; pulled in via cyber-platform sentiment | Algorithmic adjacency — narrower business than the core 3 |
| SNOW | [[Snowflake]] | Data platform; security data lake usage and cyber-data-platform narrative | Cross-sector — software platform pulled in by 2026 SaaS-cyber sentiment correlation |
| IGV | iShares Software ETF | Captures the broader software factor that the 3-name cluster shares | Benchmark, not a basket member |

These names share the platform-cyber factor but each has additional idiosyncratic exposure. Use the 3-name tight core for clean factor isolation; use the wider 5-name set for broader cyber-platform sentiment exposure.

### What is excluded — and why

| Excluded | Why excluded |
|----------|--------------|
| [[Fortinet]] (FTNT) | Singleton at 0.4 — appliance / network-policy installed base behaves differently from the platform-cyber names |
| [[Cloudflare]] (NET) | Singleton at 0.4 — edge / CDN exposure pulls it away from pure cyber co-movement (see [[Edge control-plane risk basket]]) |
| [[Rubrik]] (RBRK) | Singleton at 0.4 — data protection / recovery is a different end-market; only public since Apr 2024 with thinner correlation history |
| [[Microsoft]] (MSFT) | Singleton — too diversified across cloud / productivity / AI / gaming for cyber to dominate factor exposure |
| [[Cisco]] (CSCO) | Singleton — legacy networking with cyber bolted on (Splunk acquisition); trades like networking infrastructure |
| [[Qualys]], [[Rapid7]] | Cyber periphery — pure vulnerability management, narrower business model than platform vendors |

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/platform_cyber.yaml`. Full standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.710 (range 0.63-0.75) | Strong cohesion |
| Tightest pair | CRWD-PANW = 0.75, CRWD-ZS = 0.75 | Two of three pairs at the 0.75 ceiling |
| PC1 explained variance | 80.7% | Single dominant factor; among the tightest in the validation pass |
| Hierarchical clustering at 0.4 | CRWD + PANW + ZS + OKTA + S + TENB + SNOW + IGV cluster | Tight 3-name core + 5-name algorithmic adjacency band |
| Cluster vs SCP "other core" (FTNT, NET, RBRK) | 0.562 (+0.148 advantage) | Clear separation from the rest of SCP |
| Cluster vs cyber adjacent (OKTA, S, TENB) | 0.614 (+0.096 advantage) | Small separation — adjacencies are close, hence pull-in |
| Cluster vs cyber periphery (QLYS, RPD) | 0.396 (+0.314 advantage) | Clear separation from narrow vulnerability vendors |
| Cluster vs broad ETFs | 0.488 (+0.222 advantage) | Distinct from broad market |

### Pairwise correlations (1Y)

|  | CRWD | PANW | ZS |
|---|---|---|---|
| CRWD | — | 0.75 | 0.75 |
| PANW | 0.75 | — | 0.63 |
| ZS | 0.75 | 0.63 | — |

CRWD is the central node — both other names correlate 0.75 with CRWD. PANW-ZS at 0.63 is the loosest pair (both compete with CRWD on different surfaces — PANW on network policy, ZS on secure access — so the indirect link via CRWD is tighter than the direct link).

---

## YTD 2026 cohort tracking

![[platform-cyber-basket-2026ytd-price-chart.png]]

*CRWD (blue, primary) vs PANW, ZS normalized from 2025-12-31. Visual co-movement confirms the math — all three names track the same factor through Q1 2026 cyber sentiment swings.*

---

## How this fits the broader cyber complex

```
Cybersecurity sector (XLK / IGV exposure)
    ↓
[[Security control points]] (6-name structural cluster — partial validation; 0.57 intra-corr)
    ↓
PLATFORM CYBER TIGHT CORE — CRWD + PANW + ZS (this basket; intra-corr 0.71, PC1 80.7%)
    +
Algorithmic adjacencies — OKTA, S, TENB (pulled in at 0.4 threshold; narrower exposure)
```

The relationship to [[Security control points]]: SCP defines the conceptual "control surface" framework (policy, telemetry, recovery). Platform cyber is the validated tradable expression of the SCP framework — it captures the 3 names that own multi-product platforms across the control surfaces, while the SCP "other core" (FTNT/NET/RBRK) names sit in business-model adjacencies (appliance, edge, recovery) that don't co-move at 1Y horizon.

The relationship to [[Cybersecurity consolidation]]: that note's "consolidator" thesis (PANW, CRWD, MSFT, CSCO) was a strategic grouping by M&A activity. The math shows MSFT and CSCO don't trade with the cyber-platform factor; PANW and CRWD do (and ZS joins the cluster algorithmically, despite not being a major M&A acquirer). The validated platform cyber cluster is the trading expression of the consolidator thesis, minus the names whose M&A activity is not their dominant equity factor.

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long platform cyber factor | Equal-weighted CRWD + PANW + ZS | Multi-product cyber platform exposure |
| Long with adjacency exposure | Equal-weighted core + OKTA + S + TENB | Broader cyber-platform sentiment (loosens factor) |
| Pair: long platform cyber / short FTNT | Captures multi-product platform vs appliance-installed-base business model differential | |
| Pair: long platform cyber / short XLK | Isolates platform-cyber-specific factor (+0.22 advantage available) | |
| AVOID: long PXSEC / short IGV | IGV pulls in algorithmically — expressions overlap | |

---

## What could break the cluster

| Scenario | Effect on platform cyber cluster |
|---|---|
| AI vulnerability scanning commoditizes detection (see [[AI cybersecurity disruption basket]] events) | Cluster cohesion increases on the way down (event-driven re-rating) |
| One member is acquired or restructures (e.g., PANW continues large M&A) | Acquirer name decouples from cluster around deal-noise periods |
| Identity (OKTA) merges into the tight core via security-data-platform consolidation | Cluster expands from 3 to 4; PANW's CyberArk acquisition makes this directionally plausible |
| Cloud security commoditization (hyperscalers bundle native cyber) | All 3 names re-rate together; cluster cohesion stays high during selloff |

---

## Tracking

- Re-run validation quarterly: `python scripts/cluster_analysis.py --config scripts/cluster_configs/platform_cyber.yaml`.
- Watch for OKTA inclusion in the tight 3-name core — would signal identity is consolidating into platform-cyber factor.
- Watch for PANW or CRWD decoupling — would signal acquirer/acquired idiosyncratic news overwhelming the platform factor.
- Cross-check against [[Security control points]] when its 6-name structural core is re-validated.

---

## Related

### Member actors

- [[CrowdStrike]] — endpoint + cloud platform leader
- [[Palo Alto Networks]] — M&A-led platform consolidator
- [[Zscaler]] — cloud zero-trust platform

### Algorithmic adjacencies (track separately)

- [[Okta]] — identity platform (likely future cluster member)
- [[SentinelOne]] — AI-native endpoint
- [[Tenable]] — vulnerability management platform

### Adjacent concept notes

- [[Security control points]] — broader 6-name structural framework that this basket is the validated 3-name sub-core of
- [[Cybersecurity consolidation]] — strategic consolidator narrative that this basket is the validated trading expression of (minus MSFT/CSCO)
- [[AI cybersecurity disruption basket]] — event-driven AI-disruption sell-off basket; broader event cohort
- [[Edge control-plane risk basket]] — adjacent (NET) but separate cluster
- [[Cybersecurity]] — broader sector hub
- [[Cybersecurity consolidation|Cyber consolidation thesis]] — strategic narrative

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/platform_cyber.yaml` — config for this cluster

*Created 2026-05-03 — second concept note created under the new cluster-validation standard (after [[AI capex chain basket]])*
