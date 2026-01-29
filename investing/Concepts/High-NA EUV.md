#concept #semiconductor #manufacturing #equipment

# High-NA EUV

Next-generation EUV lithography with 0.55 numerical aperture (vs 0.33 standard). Enables 8nm resolution, 2.9x transistor density. [[ASML]] EXE series. $350-400M per system. HVM expected 2027-2028.

---

## Quick stats

| Metric | Low-NA EUV | High-NA EUV |
|--------|------------|-------------|
| Numerical aperture | 0.33 | **0.55** |
| Resolution | 13nm | **8nm** |
| Feature improvement | — | 1.7x smaller |
| Density improvement | — | 2.9x |
| System cost | $150-220M | **$350-400M** |
| Series | NXE | **EXE** |

---

## What NA means

**Numerical Aperture** = light-gathering ability of the lens system.

Higher NA → more light angles captured → finer resolution, higher contrast.

**Formula:** Resolution ∝ wavelength / NA

Going from 0.33 to 0.55 NA improves resolution by ~40% while keeping 13.5nm wavelength.

---

## Systems

| System | Purpose | Throughput | Overlay | Price | Status |
|--------|---------|------------|---------|-------|--------|
| **EXE:5000** | R&D | ~185 wph | ~1nm | ~$350M | Shipping |
| **EXE:5200B** | HVM | 175 wph | 0.7nm | ~$380M | First commercial |

---

## Timeline

| Date | Milestone |
|------|-----------|
| Apr 2024 | Intel completes first EXE:5000 assembly |
| Oct 2024 | Intel installs second High-NA |
| Sep 2025 | SK Hynix assembles first commercial High-NA for DRAM |
| Late 2025 | Intel receives first EXE:5200B |
| 2027 | Intel 14A risk production |
| 2027-2028 | High-volume manufacturing |
| 2028 | Intel 14A HVM |

---

## Customer strategies

| Customer | Approach | Nodes | Status |
|----------|----------|-------|--------|
| [[Intel]] | **First-mover** | 14A (1.4nm) | 2+ systems, HVM 2028 |
| [[Samsung]] | Following Intel | 2nm foundry | 2 units ordered (H1 2026) |
| [[SK Hynix]] | DRAM leader | HBM4/5, DDR6 | First commercial DRAM install |
| [[TSMC]] | **Skipping** | Using Low-NA through A14 | R&D only |

---

## TSMC's decision to skip

[[TSMC]] will **not use High-NA for A14 (1.4nm)** — continuing with Low-NA through 2028:

| Node | Year | Lithography |
|------|------|-------------|
| N2 | 2025 | Low-NA EUV |
| A16 | Late 2026 | Low-NA EUV |
| A14 | 2028 | Low-NA EUV |
| A14P/A10? | 2029+ | May use High-NA |

**Rationale:**
- Cost: $380M vs $180M per unit
- IBM research: Single High-NA exposure costs 2.5x more than Low-NA
- TSMC can achieve similar density with Low-NA + multi-patterning

**Kevin Zhang (TSMC SVP):**
> "As long as they continue to find a way, we do not have to use High-NA. Eventually, we will use it at some point."

---

## Why Intel is aggressive

| Factor | Intel view |
|--------|------------|
| Catch-up | Behind TSMC, needs leapfrog |
| 14A | Flagship node, must succeed |
| Cost tolerance | Willing to pay premium |
| First-mover | Wants process leadership claim |

Intel has 3× EXE:5000 (R&D) + first EXE:5200B (production).

---

## SK Hynix for memory

**First commercial High-NA for DRAM** (Sept 2025 at M16 plant).

| Application | Why High-NA |
|-------------|-------------|
| HBM4/HBM5 | Tighter pitches |
| DDR6 | Density requirements |
| Future DRAM | Scaling roadmap |

Memory may become significant High-NA market alongside logic.

---

## Cost comparison

| System | Cost | Cost/wafer |
|--------|------|------------|
| DUV (ArF-i) | $50-90M | Lowest |
| Low-NA EUV | $150-220M | ~$500+ |
| High-NA EUV | $350-400M | ~$1,250 (IBM estimate) |

IBM research: Single High-NA exposure = 2.5x cost of Low-NA.

---

## Future: Hyper-NA

ASML planning beyond 0.55 NA:

| Generation | NA | Timeline | Est. cost |
|------------|-----|----------|-----------|
| Low-NA | 0.33 | Current | $150-220M |
| High-NA | 0.55 | 2027-2028 | $350-400M |
| **Hyper-NA** | 0.75-0.85? | ~2032 | **$724M+** |

---

## Related

**Technology:**
- [[EUV lithography]] — current generation (Low-NA)
- [[DUV lithography]] — predecessor technology

**Companies:**
- [[ASML]] — sole supplier
- [[Intel]] — first-mover customer
- [[Samsung]] — early adopter
- [[SK Hynix]] — first memory adopter
- [[TSMC]] — deliberately skipping

**Nodes:**
- Intel 14A — first High-NA logic node
- Samsung 2nm — High-NA foundry
- [[HBM]] — memory application

*Created 2026-01-28*
