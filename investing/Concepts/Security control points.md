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
