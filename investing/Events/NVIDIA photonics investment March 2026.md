---
aliases: [NVIDIA Lumentum Coherent deal, NVIDIA $4B photonics deal, NVIDIA CPO investment]
tags: [event, semiconductors, ai-infrastructure, optical]
---

# NVIDIA photonics investment March 2026

On March 2, 2026, [[NVIDIA]] announced $4B in strategic investments — $2B each in [[Lumentum]] and [[Coherent]] — to secure supply of advanced photonic components for co-packaged optics (CPO). The deals include equity stakes, multibillion-dollar purchase commitments, and capacity rights, with both companies expanding US-based manufacturing.

---

## Deal structure

| Term | Lumentum | Coherent |
|------|----------|---------|
| Investment | $2B equity | $2B equity |
| Purchase commitment | Multibillion-dollar (undisclosed) | Multibillion-dollar (undisclosed) |
| Exclusivity | Nonexclusive | Nonexclusive |
| Key tech | Ultra-high-power lasers for CPO | Silicon photonics, 1.6T transceivers, 6-inch InP wafers |
| US manufacturing | New fabrication facility (location TBD) | Expansion at Saxonburg, PA |
| Relationship history | New strategic partnership | Builds on 20-year relationship |
| Use of funds | R&D, capacity, operations | R&D, capacity, operations |

Both deals are nonexclusive — Lumentum and Coherent retain the right to sell to other customers (hyperscalers, other chip companies). Equity stake percentages and investment timelines were not disclosed.

---

## Technical context

### The interconnect bottleneck

As AI clusters scale to hundreds of thousands of GPUs, the bottleneck shifts from compute to interconnect. Copper links can't deliver the bandwidth or power efficiency needed for data centers "sized like a stadium" (Jensen Huang). Co-packaged optics integrates optical engines directly into switch silicon, replacing pluggable transceivers.

### NVIDIA's CPO architecture

NVIDIA's Spectrum-X and Quantum-X switches use [[TSMC]]'s COUPE process to stack 220M transistors on top of 1,000 photonic integrated circuits.

| Spec | Value |
|------|-------|
| Engines per package | 18 silicon photonics engines |
| Optical connections | 324 |
| Throughput | 4.8 Tb/s |
| Port speed | 1.6 Tb/s per port |
| Modulator | 200 Gb/s micro ring modulator (MRM) |

### Performance vs pluggable transceivers

| Metric | CPO advantage |
|--------|---------------|
| Power efficiency | 3.5x better |
| Signal integrity | 64x better |
| Network resiliency | 10x (fewer active devices) |
| Deployment speed | ~30% faster |
| Lasers required | 4x fewer |

Current GPU configurations require 6 transceivers per GPU at 180W and $6,000 per unit — CPO eliminates this bottleneck.

### Supplier roles

- Lumentum: laser sources for Spectrum-X (ultra-high-power lasers)
- Coherent: silicon photonics collaboration, 1.6T transceiver form factor, 6-inch InP wafers (4x production efficiency vs 4-inch industry standard), proprietary Thermadite cooling

### Product timeline

- Quantum-X Photonics InfiniBand switches: shipping 2H 2025
- Spectrum-X Photonics Ethernet switches: available 2H 2026

---

## Market context

IDTechEx forecasts the co-packaged optics market at 37% CAGR from 2026 to $20B+ by 2036. Hyperscalers (AWS, Azure, Google, Meta) are the primary demand drivers.

By locking in purchase commitments with both leading photonics suppliers, NVIDIA de-risks its supply chain for next-gen networking switches while securing priority capacity as CPO demand scales. The nonexclusive structure avoids an exclusivity premium — NVIDIA gets capacity rights without preventing competitors from accessing supply.

### Ecosystem partners

- [[TSMC]] — foundry for COUPE CPO process
- [[Corning]] — fiber
- [[Foxconn]] — systems integration
- SENKO — connectors

---

## Market reaction (March 2 premarket)

| Ticker | Company | Move |
|--------|---------|------|
| LITE | Lumentum | +8% |
| COHR | Coherent | +6.5% |
| NVDA | NVIDIA | -4.16% (broader risk-off from [[2026 Iran conflict market impact|Iran conflict]]) |

POET Technologies (optical communications) caught a sympathy bid.

### Analyst commentary

Bloomberg Intelligence (Jake Silverman): Lumentum has "strengthened position as key supplier for ultra high-powered lasers for CPO." Expansion plans carry "reduced risk" given NVIDIA's purchase commitments.

Wall Street consensus on Coherent moved to "Ultra-Bullish" — several banks raised price targets to $300-$320 range. Coherent described as "no longer just a supplier, but a strategic partner." Key risk: valuation premium at highest forward multiples in a decade.

---

## Strategic read

This is NVIDIA extending its platform control into the physical layer. The pattern: dominate compute (CUDA), then networking (InfiniBand/Spectrum-X), now the optical interconnect that makes networking work at scale. Each layer deepens lock-in — if your switches use NVIDIA CPO with Lumentum lasers and Coherent transceivers optimized for NVIDIA silicon, switching costs compound.

Jensen Huang: "Computing has fundamentally changed. In the age of AI, software runs on intelligence with tokens generated in real time by AI factories."

---

## Related

- [[NVIDIA]] — investor, platform integrator
- [[Lumentum]] — $2B investment recipient, laser supplier
- [[Coherent]] — $2B investment recipient, transceiver/silicon photonics
- [[TSMC]] — foundry for CPO process
- [[Fabrinet]] — contract manufacturer for both Lumentum and Coherent
- [[Arista Networks]] — adjacent (networking)
- [[Broadcom]] — competitor (silicon photonics approach)

---

*Created 2026-03-02*
