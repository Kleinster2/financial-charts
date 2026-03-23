#concept #nvidia #interconnect

**NVLink** — [[NVIDIA]]'s proprietary high-speed GPU interconnect technology. Critical for scaling multi-GPU AI training.

---

## Why it matters

NVLink enables GPUs to communicate faster than PCIe, essential for:
- Large language model training
- Multi-GPU inference
- Hyperscaler AI clusters

---

## Generations

| Generation | Bandwidth | GPUs supported | Technology | Year |
|------------|-----------|----------------|------------|------|
| NVLink 1.0 | 160 GB/s | 8 GPUs | Copper | 2016 |
| NVLink 2.0 | 300 GB/s | 8 GPUs | Copper | 2017 |
| NVLink 3.0 | 600 GB/s | 8 GPUs | Copper | 2020 |
| NVLink 4.0 | 900 GB/s | 8 GPUs | Copper | 2022 |
| **NVLink 5.0** | 1.8 TB/s | Blackwell | Copper | 2024-25 |
| **NVLink 6.0** | 3.6 TB/s | Vera Rubin | Copper | 2026 |
| **NVLink 8** | TBD | Feynman | Copper + CPO | 2028 |

**Lane count stagnation:** NVLink lane count barely moved across generations — from 32 lanes (v1.0) to 36 lanes (v5.0). Almost all bandwidth gains came from faster lanes rather than more lanes. This creates a scaling challenge: if lane speed hits physics limits, copper scaling cannot continue without architectural changes.

**Vera Rubin details (2026):** NVLink 6.0 doubles bandwidth to 3.6TB/s by doubling lanes rather than increasing speed — using 224G SerDes with bi-directional transmission. The Oberon rack configuration requires 5,000+ cables totaling roughly 2 miles of copper interconnect.

**Rubin Ultra (2027):** Moves to Kyber rack architecture with 144 GPU packages (576 GPU dies total), replacing cables with a PCB midplane but maintaining copper electrical signaling.

**Feynman transition (2028):** NVLink 8 marks the first integration of [[Co-Packaged Optics]] into scale-up interconnect. Jensen at GTC 2026: "Feynman has Kyber with copper and CPO scale-up." This represents coexistence rather than full transition — copper and optical operating together.

---

## NVLink Fusion

Announced 2025 — allows non-NVIDIA chips to connect via NVLink protocol.

**First adopter:** [[Amazon]] Trainium4 will support NVLink Fusion, enabling interoperability with NVIDIA GPUs.

**Strategic significance:** NVIDIA opening its interconnect moat — signals confidence or competitive pressure from custom silicon.

---

## Competitive context

| Interconnect | Owner | Notes |
|--------------|-------|-------|
| **NVLink** | [[NVIDIA]] | Proprietary, fastest |
| Infinity Fabric | [[AMD]] | Open, slower |
| UALink | Consortium | Emerging standard |
| CXL | Industry | Memory-focused |
| **[[Upscale AI]]** | Startup ([[Celesta Capital]]) | Scale-up Ethernet alternative; $300M raised |

### Upscale AI challenge

[[Upscale AI]] emerged from stealth in Sep 2025 ($100M seed) and raised another $200M in Jan 2026, specifically targeting the scale-up interconnect function that NVLink/NVSwitch serve today. The approach: open-standards Ethernet leveraging UEC (Ultra Ethernet Consortium) specs, UALink, and SAI. Backed by [[Celesta Capital]]. [[Sriram Viswanathan]] (Celesta): "We've raised a significant amount of capital to really go after what NVLink offers from NVIDIA, but really try to do it from scale-up Ethernet for the scale of architecture in the data center." If successful, this would let operators connect GPU blades without [[NVIDIA]]'s proprietary networking — enabling multi-vendor racks.

---

## Related

- [[NVIDIA]] — owner
- [[Co-Packaged Optics]] — NVLink 8 (Feynman) integration technology
- [[Amazon]] — Trainium4 NVLink Fusion adopter
- [[Upscale AI]] — challenger (scale-up Ethernet alternative, $300M raised)
- [[Celesta Capital]] — Upscale AI investor
- [[CUDA moat]] — software lock-in companion to hardware interconnect
- [[Blackwell]] — NVLink 5.0 debut
- [[Astera Labs]] — adjacent (data center connectivity)
- [[Broadcom]] — adjacent (networking silicon)

---

*Updated 2026-03-08*
