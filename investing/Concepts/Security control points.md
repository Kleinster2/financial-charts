---
aliases:
  - Cyber control points
  - Security control-plane cluster
  - Cloud security control points
tags:
  - concept
  - cybersecurity
  - ai
  - market-structure
---

# Security control points

> [!warning] Cluster status: partial validation (May 2026)
> Intra-cluster correlation 0.57, PC1 64.8% — moderate cohesion. Hierarchical clustering at 0.4 returns only 3 of 6 candidates as a tight sub-core (CRWD, PANW, ZS — "platform cyber"), pulls in OKTA/S/TENB from controls, excludes FTNT/NET/RBRK as standalones. The 6-name "structural core" is a thesis grouping; the tradable cluster is the 3-name platform-cyber sub-core. See "Cluster validation — partial confirmation, sub-structure revealed" section below.

Plain English: the market is separating generic cybersecurity from the vendors that sit at a control point. These are the companies that still see the traffic, enforce the policy, own the telemetry, or control the recovery loop after AI changes the tooling layer.

The important distinction is not just cyber winners versus cyber losers. It is whether a vendor sits in a part of the stack customers still have to pass through: secure access, network policy, endpoint telemetry, or data protection and recovery. Those positions can still matter even if frontier labs get much better at vulnerability discovery and exploit generation.

---

## Synthesis

The April 13, 2026 cluster signal showed a cleaner structure inside cybersecurity than the broad sector label suggests. `scripts/cluster_movers.py` flagged a seven-name up cluster led by [[Fortinet]], [[Zscaler]], [[Palo Alto Networks]], [[Akamai]], [[CrowdStrike]], [[Cloudflare]], and [[Rubrik]] at roughly +5.1% excess return and a +2.0 z-score. That by itself could have been written off as one day's tape. The more useful result came from rerunning the same logic across 60-day, 90-day, and 120-day correlation windows.

Across those windows, the durable core kept reappearing as [[CrowdStrike]], [[Fortinet]], [[Cloudflare]], [[Palo Alto Networks]], [[Rubrik]], and [[Zscaler]]. At that tighter threshold, the cluster often pulled in adjacent names such as [[Datadog]], [[MongoDB]], [[Okta]], and [[SentinelOne]], while [[Akamai]] only re-entered when the correlation threshold was relaxed. The average pairwise excess-return correlation for the core stayed around 0.55 over 60 days, 0.49 over 90 days, and 0.47 over 120 days. That is strong enough to treat the grouping as structural rather than accidental.

What binds these companies is not simply that they sell security. It is that they own a control surface enterprises still need even when AI gets better. [[Zscaler]] and [[Palo Alto Networks]] sit in policy enforcement and traffic inspection. [[Fortinet]] owns the appliance and network-policy layer for a large installed base. [[CrowdStrike]] controls endpoint telemetry and response. [[Rubrik]] owns recovery and resilience after prevention fails. [[Cloudflare]] bridges security and edge delivery through proxy, routing, and perimeter services. The market is clustering around vendors that remain on the path of traffic, policy, or recovery.

That makes this concept adjacent to, but distinct from, both [[Edge cloud]] and [[AI cybersecurity disruption basket]]. The disruption basket captures days when frontier labs scare cyber investors by improving vulnerability discovery. Security control points captures the opposite durability argument: once AI increases the speed and scale of attack, the vendors that sit closest to enforcement, telemetry, and restoration can become more central rather than less. The cluster is not saying all cyber is safe. It is saying some parts of cyber still own the bottleneck.

---

## What binds the cluster

| Control surface | Representative names | Why it matters |
|----------------|----------------------|----------------|
| Policy enforcement and secure access | [[Zscaler]], [[Palo Alto Networks]], [[Fortinet]], [[Cloudflare]] | Enterprise traffic still has to be filtered, routed, authenticated, and inspected somewhere |
| Endpoint telemetry and response | [[CrowdStrike]], [[SentinelOne]] | AI raises the speed of attacks, which makes always-on telemetry and response loops more valuable |
| Data protection and recovery | [[Rubrik]] | If prevention fails faster, recovery and resilience become a larger part of the control plane |
| Adjacent telemetry / developer data layers | [[Datadog]], [[MongoDB]], [[Okta]] | These names can get pulled into the same market bucket when observability, identity, and application control are repriced together |
| Edge and perimeter adjacency | [[Cloudflare]], [[Akamai]] | The edge overlaps with security, but not all edge vendors are equally central to the security-control-point read |

---

## Structural core vs adjacent names

| Bucket | Names | Read |
|-------|-------|------|
| Structural core | [[CrowdStrike]], [[Fortinet]], [[Cloudflare]], [[Palo Alto Networks]], [[Rubrik]], [[Zscaler]] | Persisted across 60d, 90d, and 120d windows at the standard correlation threshold |
| Frequent adjacencies | [[Datadog]], [[MongoDB]], [[Okta]], [[SentinelOne]] | Join the cluster in broader control-plane or telemetry repricings |
| Loose edge adjacency | [[Akamai]] | Related through perimeter and delivery, but weaker correlation to the cyber core |

---

## Why AI can strengthen this layer

| AI dynamic | Implication for control points |
|-----------|-------------------------------|
| Faster vulnerability discovery | More incidents still have to be blocked, inspected, or contained in production |
| Faster exploitation and lateral movement | Endpoint telemetry, policy enforcement, and segmentation matter more, not less |
| More autonomous software agents | Identity, secure access, logging, and traffic policy become more central to governance |
| Higher breach frequency | Recovery and resilience vendors gain strategic importance |

This is why the market can sell off cyber on one AI announcement and then rotate back into a narrower control-point cluster later. AI can commoditize some detection and scanning workflows while simultaneously making the always-on enforcement and recovery layers more important.

### Horizon split

The strengthening case is a 1-2 year read. At that horizon enterprises still run human-supervised networks, humans still own the policy decisions, and AI pressure shows up as faster attack surface rather than reorganized architecture. At a 3-5 year horizon the thesis is no longer automatic. If autonomous agents run their own identity, policy enforcement, observability, and recovery loops inside agent-native stacks, the enterprise-facing control points that own human-admin-facing policy consoles and telemetry dashboards may not be where the value sits anymore. The cluster in this note is built on the short-horizon read; the long-horizon read depends on whether agent-native infrastructure reuses the current control points or routes around them.

---

## Empirical signal

### Apr 13, 2026 cluster result

| Cluster | Excess return | Z-score | Raw move |
|--------|---------------|---------|----------|
| [[Fortinet]], [[Zscaler]], [[Palo Alto Networks]], [[Akamai]], [[CrowdStrike]], [[Cloudflare]], [[Rubrik]] | +5.06% | +2.0 | +6.0% |

### Persistence check

| Window | Durable overlap | Read |
|-------|------------------|------|
| 60d | 6 of 7 core names, with high-correlation adjacencies | Strong structural cluster |
| 90d | 6 of 7 core names, plus adjacent control-plane names | Still structural |
| 120d | 6 of 7 core names, similar composition | Still structural |
| Threshold relaxation | [[Akamai]] re-enters around 0.25 to 0.20 | More adjacent than core |

The cleanest read is that the durable market-implied grouping is cyber and control-plane heavy, not pure edge delivery.

### Historical persistence (2020-2026)

The grouping is not a 2026 artifact. Running the same pairwise excess-return correlation (over [[SPY]]) across multi-year periods shows the core has been a coherent cluster back to at least 2020.

| Period | Core avg pair corr | Members available | Note |
|--------|--------------------|-------------------|------|
| 2020 H2 | 0.55 | 5 of 6 | Rubrik not yet public |
| 2021 | 0.55 | 5 of 6 | |
| 2022 | 0.68 | 5 of 6 | Elevated by tech drawdown co-movement |
| 2023 | 0.46 | 5 of 6 | |
| 2024 H1 | 0.37 | 5 of 6 | [[Rubrik]] IPO Apr 2024 |
| 2024 H2 | 0.45 | 6 of 6 | First full window with Rubrik |
| 2025 H1 | 0.54 | 6 of 6 | |
| 2025 H2 | 0.42 | 6 of 6 | |
| 2026 YTD | 0.64 | 6 of 6 | |

Since Rubrik IPO'd, the 60-day rolling average pairwise correlation for the full 6-name core has run 0.24 to 0.74 with mean 0.51 and standard deviation 0.13 over 644 daily observations. The current reading around 0.67 sits in the upper third of that distribution but well inside it, not an outlier.

Two supporting reads:

- The pre-Rubrik 5-name core (CRWD, FTNT, NET, PANW, ZS) averaged 0.46 to 0.68 across 2020-2023. The grouping pre-dates Rubrik's addition by years; Rubrik slotted into an already-coherent cluster after its 2024 IPO.
- The adjacent bucket (DDOG, MDB, OKTA, S) underperforms the core correlation in every period tested, and AKAM runs a step below the core in every window. The structural-core-versus-adjacent distinction in the table above is historical, not a window-specific artifact.

Caveat: 2022's 0.68 reading partly reflects drawdown co-movement (tech fell together that year). Non-crisis periods (2023, 2024 H2, 2025) still run 0.42 to 0.54, which supports a structural grouping rather than a crisis-correlation result.

![[security-control-points-core-vs-akam-2026-price-chart.png]]
*Normalized price chart for [[CrowdStrike]], [[Fortinet]], [[Cloudflare]], [[Palo Alto Networks]], [[Rubrik]], [[Zscaler]], and [[Akamai]], start 2026-01-01 = 100.*

*The visual read matches the cluster work: the cyber and control-point names mostly travel together, while [[Akamai]] participates in the tape but remains a looser adjacent member than part of the tightest structural core.*

---

## Why this matters

When a cyber move hits the tape, the useful question is no longer just whether security spending rises or falls. The better question is which vendors still own the control surfaces that enterprise traffic, identity, telemetry, and recovery have to pass through.

That is the layer this concept is trying to isolate.

---

## Cluster validation — partial confirmation, sub-structure revealed (May 2026)

Re-validation of the SCP "structural core" using the standardized procedure (`scripts/cluster_analysis.py --config scripts/cluster_configs/scp.yaml`, full procedure in `docs/cluster-validation.md`) with a wider control universe including cyber adjacencies (OKTA, S, DDOG, MDB, AKAM), cyber periphery (QLYS, RPD, TENB), broad software (SNOW, VEEV, MSFT), and software/broad ETFs (IGV, XLK, SPY).

**Result: moderate cluster, partial validation.** Intra-cluster correlation 0.57 (consistent with the prior 60d/90d/120d analysis showing 0.55/0.49/0.47). PC1 explained variance 64.8% — above the 50% multi-factor floor but below the 70% strong-cohort line. Hierarchical clustering at 0.4 threshold reveals significant sub-structure: only 3 of the 6 candidate names form a tight algorithmic cluster (CRWD, PANW, ZS), and the algorithm pulls in adjacencies (OKTA, S, TENB, SNOW, IGV) instead of including the other 3 (FTNT, NET, RBRK as standalones).

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | **0.574** (range 0.45-0.75) | Moderate cohesion |
| Tightest pairs | CRWD-PANW = 0.75, CRWD-ZS = 0.75 | Three-name "platform cyber" sub-core |
| Loosest pair | FTNT-NET = 0.45 | Below the 0.50 floor — these don't co-move much |
| Hierarchical clustering at 0.4 | 3 of 6 names cluster (CRWD, PANW, ZS); others standalone | Boundary not clean |
| PCA — PC1 explained variance | **64.8%** | Dominant single factor but not single-factor cohort |
| PC1 loadings | 0.38-0.46 (all positive) | Reasonably equal-weight; no inverted loadings |

### Pairwise correlations within the candidate cluster

|     | CRWD | FTNT | NET | PANW | RBRK | ZS |
|---|---|---|---|---|---|---|
| CRWD | — | 0.58 | 0.65 | 0.75 | 0.58 | 0.75 |
| FTNT | 0.58 | — | 0.45 | 0.64 | 0.49 | 0.48 |
| NET | 0.65 | 0.45 | — | 0.52 | 0.48 | 0.54 |
| PANW | 0.75 | 0.64 | 0.52 | — | 0.51 | 0.63 |
| RBRK | 0.58 | 0.49 | 0.48 | 0.51 | — | 0.56 |
| ZS | 0.75 | 0.48 | 0.54 | 0.63 | 0.56 | — |

The correlation structure reveals a tight three-name sub-core (CRWD-PANW-ZS at 0.63-0.75) and a looser tier (FTNT, NET, RBRK at 0.45-0.65 with each other and the core).

### Hierarchical clustering result (threshold 0.4)

![[scp-cluster-dendrogram-1y.png]]

| Cluster | Members |
|---|---|
| **Algorithmic cyber-software cluster** | **CRWD, PANW, ZS, OKTA, S, TENB, SNOW, IGV** |
| Broad market | XLK + SPY (correlation ~0.99) |
| Standalone | FTNT, NET, RBRK, DDOG, MDB, MSFT, VEEV, AKAM, QLYS, RPD |

The algorithm pulls 5 names that were NOT in the candidate cohort (OKTA, S, TENB, SNOW, IGV) into the cluster, and excludes 3 candidates (FTNT, NET, RBRK) as standalones. Translation:

- **The market currently views CRWD, PANW, ZS as a coherent "platform cyber" cluster** — the three names with broad multi-product platforms (endpoint + cloud + network).
- **OKTA, S, TENB get pulled in** — identity (OKTA), AI-native endpoint (S), vulnerability management (TENB) trade with the platform-cyber core, contradicting the SCP note's earlier separation of these as "frequent adjacencies."
- **FTNT, NET, RBRK are NOT in the algorithmic cluster** at this threshold:
  - FTNT (Fortinet) trades more idiosyncratically — appliance / network-policy installed base behaves differently from the platform-cyber names.
  - NET (Cloudflare) has edge / CDN exposure that pulls it away from pure cyber co-movement.
  - RBRK (Rubrik) is the data-protection / recovery name — different end-market and a 2024 IPO with thinner correlation history.
- **SNOW and IGV pulling in** suggests the "cluster" is really a broader "growth software" + cyber-platform sub-set, not a pure cyber control-points cluster.

### Group-pair correlations

| Group pair | Avg pairwise corr | Cluster's intra-advantage |
|---|---|---|
| Cluster (intra) | 0.574 | — |
| Cluster vs cyber adjacent (OKTA, S, DDOG, MDB, AKAM) | 0.466 | +0.107 |
| Cluster vs broad software (SNOW, VEEV, MSFT) | 0.462 | +0.112 |
| Cluster vs broad ETFs (IGV, XLK, SPY) | 0.478 | +0.096 |
| Cluster vs cyber periphery (QLYS, RPD, TENB) | 0.420 | +0.154 |

The intra advantages are small (+0.10 to +0.15) — the SCP cluster does not separate cleanly from any comparator group. Compare to ALTM (+0.18 to +0.63 across all comparators) and boutique advisory (+0.13 to +0.60). The SCP cluster trades with the broader software complex about as much as with itself.

### Interpretation — what the math is saying

The SCP concept is structurally valid but is currently expressed in the market as a tighter 3-name platform-cyber sub-cluster (CRWD, PANW, ZS) with OKTA/S/TENB pulled in. The original 6-name "structural core" derivation (60d/90d/120d windows in `scripts/cluster_movers.py`) was correct that *something* is grouping cyber names — but the boundary varies by window and threshold:

- **At 0.4 threshold (1Y window)**: 3 candidates cluster + 3 candidates standalone + 5 non-candidates pulled in → the cluster as defined fails the boundary test.
- **At looser thresholds or shorter windows** (60d): the 6-name original core appears more cohesive.
- **PC1 64.8%** says there IS a dominant factor, but it is shared with broader growth software — not unique to security control points.

The honest revision: the durable structural cluster on a 1Y horizon is **CRWD-PANW-ZS as the platform-cyber tight core**, with OKTA/S/TENB as nearest-neighbor adjacencies, and FTNT/NET/RBRK as related-but-not-co-moving names that justify their own separate analysis (different business models — appliance, edge, recovery).

### What this means for the vault

- **The 3-name tight core (CRWD-PANW-ZS) is tradable as a basket** — intra-corr 0.71, single-factor.
- **The 6-name "structural core" is a thesis grouping, not a tradable basket.** Pair trades within FTNT/NET/RBRK vs the platform-cyber core are likely to capture the business-model differential rather than systematic AI-disruption / control-points factor.
- **Re-run with 60d window for the original derivation context.** The note's 0.46-0.54 readings on 60-day windows are a different signal than the 1Y validation; both can coexist if the SCP cohesion is regime-dependent (tighter under sector stress).
- **Sub-cluster the SCP analysis going forward**: tight platform-cyber (CRWD/PANW/ZS), edge-adjacent (NET), appliance/network (FTNT), data-protection (RBRK). Each merits its own framing.

---

## Related

- [[Cybersecurity]]
- [[Edge cloud]]
- [[Zero Trust|Zero trust]]
- [[AI cybersecurity disruption basket]]
- [[Edge control-plane risk basket]]
- [[Software AI bifurcation]]
- [[CrowdStrike]]
- [[Fortinet]]
- [[Palo Alto Networks]]
- [[Zscaler]]
- [[Cloudflare]]
- [[Rubrik]]
- [[Akamai]]
