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
