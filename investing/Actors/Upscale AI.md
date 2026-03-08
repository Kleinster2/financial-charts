---
aliases: [Upscale]
---
#actor #ai #networking #usa #private

**Upscale AI** — AI networking startup building scale-up Ethernet to challenge [[NVIDIA]]'s [[NVLink]]/NVSwitch monopoly on GPU interconnect.

---

## Synopsis

Emerged from stealth in September 2025 with a $100M seed round, then raised another $200M in January 2026 — $300M total before shipping product. The pitch: an open-standards Ethernet alternative for scale-up GPU interconnect, leveraging the [[Ultra Ethernet Consortium]] (UEC) specs, UALink, and SAI standards. This attacks [[NVIDIA]]'s [[NVLink]] lock-in directly — if you can connect GPU blades in a rack via Ethernet at competitive bandwidth, you don't need NVSwitch, and you can mix silicon from different vendors. [[Celesta Capital]] portfolio company. CEO is Barun Kar. The constraint-flow thesis ([[Sriram Viswanathan]]'s framing) predicts networking becomes the binding bottleneck after memory — and Upscale is positioned exactly at that transition. The risk: [[NVIDIA]] opened NVLink via Fusion ([[Amazon]] Trainium4 is the first adopter), and incumbents like [[Broadcom]] and [[Astera Labs]] already compete in data center networking.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | Private |
| HQ | USA |
| CEO | Barun Kar |
| Total raised | $300M |
| Seed | $100M (Sep 2025) |
| Series A | $200M (Jan 2026) |
| Focus | Scale-up Ethernet for AI data centers |

---

## Leadership

| Role | Name | Background |
|------|------|------------|
| CEO | Barun Kar | — |

---

## Technology

Building scale-up Ethernet interconnect for AI racks — the same function [[NVLink]] and NVSwitch serve today, but using open standards:

| Standard | Role |
|----------|------|
| UEC (Ultra Ethernet Consortium) | Ethernet specs for AI workloads |
| UALink | GPU-to-GPU interconnect standard |
| SAI | Switch abstraction interface |

The goal: let data center operators connect GPU blades without proprietary [[NVIDIA]] networking, enabling multi-vendor silicon and lower costs.

---

## Cap table

| Round | Date | Amount | Notes |
|-------|------|--------|-------|
| Seed | Sep 2025 | $100M | Emerged from stealth |
| Series A | Jan 2026 | $200M | — |
| Total | | $300M | |

---

## Related

- [[Celesta Capital]] — investor
- [[NVLink]] — incumbent competitor (proprietary GPU interconnect)
- [[NVIDIA]] — NVLink/NVSwitch owner
- [[Astera Labs]] — peer (data center connectivity)
- [[Broadcom]] — peer (networking silicon)
- [[Supply chain bottlenecks]] — networking as next binding constraint
- [[Sriram Viswanathan]] — Celesta partner articulating constraint-flow thesis
