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

| Generation | Bandwidth | GPUs supported |
|------------|-----------|----------------|
| NVLink 1.0 | 160 GB/s | 8 GPUs |
| NVLink 2.0 | 300 GB/s | 8 GPUs |
| NVLink 3.0 | 600 GB/s | 8 GPUs |
| NVLink 4.0 | 900 GB/s | 8 GPUs |
| **NVLink 5.0** | 1.8 TB/s | Blackwell |

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
- [[Amazon]] — Trainium4 NVLink Fusion adopter
- [[Upscale AI]] — challenger (scale-up Ethernet alternative, $300M raised)
- [[Celesta Capital]] — Upscale AI investor
- [[CUDA moat]] — software lock-in companion to hardware interconnect
- [[Blackwell]] — NVLink 5.0 debut
- [[Astera Labs]] — adjacent (data center connectivity)
- [[Broadcom]] — adjacent (networking silicon)

---

*Updated 2026-03-08*
