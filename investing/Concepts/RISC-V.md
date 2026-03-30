# RISC-V

#concept #semiconductors #china #opensource

**RISC-V** — Open-source instruction set architecture (ISA). [[China]]'s strategic bet to bypass ARM/x86 licensing and US export controls. State-backed "Silicon Sovereignty" strategy with nationwide policy (March 2025). Key players: Alibaba XuanTie, VeriSilicon+Nuclei, SpacemiT.

---

## What is RISC-V

| Aspect | Detail |
|--------|--------|
| Type | Instruction Set Architecture (ISA) |
| Origin | UC Berkeley (2010) |
| License | **Open-source, royalty-free** |
| Governance | RISC-V International ([[Switzerland]]) |
| Alternative to | ARM (licensed), x86 ([[Intel]]/[[AMD]] proprietary) |

**Key difference from ARM:** No licensing fees, no export control restrictions, fully customizable.

---

## Why [[China]] is betting on RISC-V

| Driver | Detail |
|--------|--------|
| **US export controls** | ARM licenses restricted for Chinese firms |
| **Self-sufficiency** | No foreign IP dependency |
| **Cost** | No royalties to ARM/[[Intel]] |
| **Customization** | Can optimize for specific workloads (AI, IoT) |
| **Security** | Full visibility into chip design |

**Strategic context:** US restricted [[Huawei]], [[SMIC]] from advanced chips. RISC-V is the escape route.

---

## [[China]] government policy

### March 2025 nationwide guidance

| Detail | Value |
|--------|-------|
| Drafting bodies | 8 agencies (CAC, MIIT, MOST, CNIPA) |
| Scope | Nationwide RISC-V adoption |
| Focus areas | R&D, standards, applications, global cooperation |
| Market reaction | VeriSilicon +10% limit up |

### [[China]] RISC-V Industry Alliance

| Detail | Value |
|--------|-------|
| Formed | 2018 |
| Chair | Dai Weimin (VeriSilicon) |
| Function | Patent sharing, ecosystem development |
| Members | 100+ companies |

---

## Key Chinese players

| Company | Product/Role | Status |
|---------|--------------|--------|
| **[[Alibaba]]** (T-Head/Damo) | [[XuanTie C950]] server CPU (Mar 2026) | 5nm, RISC-V world record SPECint2006 >70, native LLM inference |
| **[[Alibaba]]** (T-Head/Damo) | XuanTie C930 server chip (Mar 2025) | Server-grade, RVA23, 8 TOPS matrix engine |
| **VeriSilicon** | IP provider, acquiring Nuclei | Public (688521.SH) |
| **Nuclei System** | RISC-V CPU IP specialist | Being acquired by VeriSilicon |
| **[[SpacemiT]]** | K1 chip, edge/robotics | Series B ($86M, Jan 2026) |
| **StarFive** | RISC-V SoCs | Backed by government funds |
| **Sophgo** | AI chips on RISC-V | BitMain spinoff |

### VeriSilicon + Nuclei merger (Aug 2025)

| Detail | Value |
|--------|-------|
| Acquirer | VeriSilicon (688521.SH) |
| [[Target]] | Nuclei System Technology |
| Rationale | Consolidate RISC-V IP leadership |
| VeriSilicon R&D investment | 1.3B yuan in R&D center |

### Alibaba [[XuanTie C950]] (March 2026) — current flagship

| Spec | Value |
|------|-------|
| Architecture | 64-bit multi-core RISC-V, out-of-order superscalar |
| Profile | RVA23 (v23.1) |
| Process | 5nm (reportedly [[TSMC]]) |
| Clock | 3.2 GHz, 8-instruction decode, 16-stage pipeline |
| AI acceleration | XuanTie Tensor Processing Engine (TPE), 8 TOPS, FP16 to INT4/FP8 |
| LLM support | Natively runs [[Qwen|Qwen3]]-235B and [[DeepSeek]] V3-671B |
| SPECint2006 | >70 (RISC-V world record, 3x C920) |
| SPECInt 2017 | ~[[Apple]] M1 (2020) level per Google researcher |
| [[Target]] | Data center AI inference, [[Agentic AI]] workloads |

First CPU to natively run trillion-parameter models on RISC-V. The performance gap with Western CPUs is real (4-5 years behind), but the strategic value is that [[Alibaba]] co-designs chip + model + cloud on an architecture with zero US [[export controls]] exposure.

### Alibaba XuanTie C930 (March 2025)

| Spec | Value |
|------|-------|
| Architecture | 64-bit multi-core RISC-V |
| Profile | RVA23 compatible |
| Vector units | Dual 512-bit |
| AI capability | 8 TOPS [[Matrix]] engine |
| [[Target]] | Server workloads |

---

## Use cases

| Segment | Why RISC-V fits |
|---------|-----------------|
| **IoT/Edge** | Low power, customizable |
| **AI inference** | Custom accelerators |
| **[[Automotive]]** | No licensing restrictions |
| **Industrial** | Long-term support |
| **Data centers** | Cost at scale |

---

## RISC-V vs ARM vs x86

| Factor | RISC-V | ARM | x86 |
|--------|--------|-----|-----|
| **License** | Open/free | Per-chip royalty | Proprietary |
| **Customization** | Full | Limited | None |
| **Ecosystem** | Growing | Mature | Mature |
| **Performance** | Catching up (~M1 level) | Mobile leader | Server leader |
| **[[China]] access** | ✅ Unrestricted | ⚠️ Limited | ⚠️ Limited |

---

## DeepSeek connection

RISC-V + efficient AI models = alternative to NVIDIA dependency.

| Insight | Detail |
|---------|--------|
| DeepSeek efficiency | Runs on lower-end chips |
| RISC-V opportunity | 30% performance at lower cost = viable at scale |
| [[China]] Mobile view | Multiple RISC-V units can match NVIDIA/[[Huawei]] |

See [[DeepSeek]], [[US-China tech race]].

---

## Global RISC-V landscape

| Region | Activity |
|--------|----------|
| **[[China]]** | State-backed, largest adoption |
| **[[Europe]]** | European Processor Initiative (EPI) |
| **[[India]]** | Shakti processor program |
| **US** | SiFive, [[Tenstorrent]] (startup-driven) |

**Irony:** US-origin technology (Berkeley) now powering [[China]]'s chip independence.

---

## Investment implications

| Angle | Detail |
|-------|--------|
| **[[China]] chip plays** | VeriSilicon, SpacemiT, Alibaba |
| **US incumbents at risk** | ARM (if [[China]] ecosystem succeeds) |
| **Beneficiaries** | RISC-V IP providers, toolchain companies |
| **Timeline** | 3-5 years to meaningful server share |

### Risks

| Risk | Detail |
|------|--------|
| **Ecosystem maturity** | Software/tools lag ARM |
| **Performance gap** | Still behind ARM/x86 in high-end |
| **Fragmentation** | Too many incompatible extensions |
| **US response** | Could restrict RISC-V tools/software |

---

## Related

### Actors
- [[Alibaba]] — XuanTie RISC-V chips via T-Head/Damo (see [[XuanTie C950]])
- [[SpacemiT]] — K1 chip, Series B ($86M)
- VeriSilicon — 688521.SH, acquiring Nuclei
- [[Lenovo]] — SpacemiT investor

### Concepts
- [[US-China tech race]] — export controls driving RISC-V adoption
- [[US Sanctions]] — chip restrictions context
- [[Semiconductors]] — sector context

### Adjacent
- ARM — licensed alternative
- [[NVIDIA]] — AI chip incumbent

---

## Sources

- [Tom's Hardware: [[China]] RISC-V Policy](https://www.tomshardware.com/pc-components/cpus/chinese-government-shifts-focus-from-x86-and-arm-cpus-promoting-the-adoption-of-risc-v-chips)
- [Jamestown: [[China]] RISC-V Grand Strategy](https://jamestown.org/program/examining-chinas-grand-strategy-for-risc-v/)
- [DigiTimes: VeriSilicon Nuclei Acquisition](https://www.digitimes.com/news/a20250829VL205/verisilicon-shanghai-risc-v-ip-cpu.html)

*Updated 2026-03-30*
