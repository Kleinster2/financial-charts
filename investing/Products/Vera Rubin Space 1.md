---
aliases: [Vera Rubin Space-1, Space 1 Module, Rubin Space Module]
---
#product #semiconductors #ai-infrastructure #space

**Vera Rubin Space 1** — [[NVIDIA]]'s space-qualified compute module, announced by Jensen Huang at GTC 2026 (March 16-17). Six-chip integrated platform delivering up to 25x H100 AI compute in a size/weight/power-constrained orbital form factor. Distinguishes NVIDIA's role in the orbital data center platform war: not building a constellation (like [[SpaceX]] [[Terrafab]] or [[Blue Origin]] [[Project Sunrise]]), but selling the picks and shovels — every constellation builder is a potential customer.

---

## Quick stats

| Metric | Value |
|---|---|
| Maker | [[NVIDIA]] |
| Announced | GTC 2026 (March 16-17, 2026) |
| AI compute (vs H100) | Up to 25x for space-based inferencing |
| Form factor | Size/weight/power-constrained orbital module |
| Architecture | Tightly integrated CPU-GPU with high-bandwidth interconnect |
| Availability | TBD (announced launch customers list) |

---

## Module composition (6 chips)

| Chip | Role |
|---|---|
| [[NVIDIA Vera CPU]] | Main processor |
| [[NVIDIA Rubin GPU]] | AI compute |
| [[NVIDIA NVLink 6 Switch]] | High-bandwidth GPU interconnect |
| [[NVIDIA ConnectX-9 SuperNIC]] | Network interface |
| [[NVIDIA BlueField-4 DPU]] | Data processing unit |
| [[NVIDIA Spectrum-6 Ethernet Switch]] | Networking fabric |

The architecture choice — six-chip integrated module rather than discrete GPU sales — reflects the orbital constraint set. In a satellite, you can't add new boards or repair components, so the module is sold as a unit with networking, security, and orchestration baked in.

---

## Launch customers (announced at GTC)

| Customer | Profile |
|---|---|
| [[Aetherflux]] | Space solar power |
| [[Axiom Space]] | Commercial space station + orbital DC |
| [[Kepler Communications]] | Inter-satellite optical mesh |
| [[Planet Labs]] | Earth observation |
| [[Sophia Space]] | Space-based AI compute startup |
| [[Starcloud]] | NVIDIA-backed orbital DC venture |

The customer mix spans Earth observation (real-time AI inference on imagery), space stations (orbital workloads + research), space solar (compute attached to power infrastructure), and dedicated orbital DC ventures. NVIDIA is selling the same module across all of them — analogous to how H100s sold into hyperscaler training, sovereign AI, and enterprise within months of release.

---

## Why Vera Rubin Space 1 matters

Per [[Space Capital]] (Chad Anderson, Apr 26, 2026): "Then NVIDIA made its position explicit. At GTC, Jensen Huang unveiled the Vera Rubin Space 1 module. His words: 'Space computing — the final frontier — has arrived.' That's not a product announcement. That's a market declaration from the most important infrastructure company in AI."

The strategic read: NVIDIA's commercial position in orbital DCs is to be Switzerland — supplier to all builders rather than a constellation operator competing with them. That maximizes the addressable market (every constellation builder is a customer) but caps upside (NVIDIA captures the chip layer of the stack, not the data center layer that hyperscalers monetize). Within the [[Sovereign AI stack]] framework that [[Deepwater Asset Management]] applies to [[SpaceX]], NVIDIA is the supplier dependency that competing constellations have to manage.

The 25x H100 multiplier is engineering-marketing speak rather than a clean benchmark — the actual performance depends on workload, networking topology, and power budget in orbit. But the order-of-magnitude signal is real: a Rubin-class module in space versus an H100 cluster on Earth is the comparison NVIDIA is asking customers to underwrite.

---

## Earth equivalents

| Metric | Vera Rubin Space 1 | NVIDIA H100 (Earth, 2025) | NVIDIA B200 (Earth, 2026) |
|---|---|---|---|
| AI compute (relative) | 25x H100 (space-inference) | baseline | ~2-3x H100 |
| Form factor | Orbital module | Server rack | Server rack |
| Power envelope | Solar + radiator | Grid + liquid cooling | Grid + liquid cooling |
| Networking | Optical mesh | InfiniBand / Ethernet | InfiniBand / Ethernet |
| Repair | None (no orbital service) | RMA via vendor | RMA via vendor |

The 25x figure is for space-based inferencing specifically — not training, where networking and reliability constraints would dominate. See [[Space data centers]] (SemiAnalysis section) for the technical critique of orbital DC training-scale workloads.

---

## Related

- [[NVIDIA]] — maker
- [[Jensen Huang]] — CEO; GTC 2026 keynote announcing the module
- [[GTC]] — NVIDIA's annual conference; March 2026 was the launch venue
- [[Space data centers]] — concept; orbital DC platform-war framing
- [[Project Sunrise]] — [[Blue Origin]] orbital DC (potential customer)
- [[Project Suncatcher]] — [[Google]] orbital DC (potential alternative)
- [[Terrafab]] — SpaceX/[[xAI]] chip program (competing path: vertical integration)
- [[Sovereign AI stack]] — Deepwater framework
- [[Starcloud]] — NVIDIA-backed orbital DC operator

---

## Sources

- [NVIDIA Newsroom: Space Computing](https://nvidianews.nvidia.com/news/space-computing)
- [CNBC: Nvidia announces Vera Rubin Space-1 chip system](https://www.cnbc.com/2026/03/16/nvidia-chips-orbital-data-centers-space-ai.html)
- [Tom's Hardware coverage](https://www.tomshardware.com/pc-components/gpus/nvidia-announces-vera-rubin-space-module)
- [Space Capital Space IQ Q1 2026](https://youtu.be/iGmr4g4Iot4) — platform-war framing

*Created 2026-04-27*
