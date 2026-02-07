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

---

## Related

- [[NVIDIA]] — owner
- [[Amazon]] — Trainium4 NVLink Fusion adopter
- [[CUDA moat]] — software lock-in companion to hardware interconnect
- [[Blackwell]] — NVLink 5.0 debut

---

*Created 2026-02-06*
