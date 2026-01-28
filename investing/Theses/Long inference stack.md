#thesis #trade #ai #infrastructure

# Long Inference Stack

**Status**: Emerging — disaggregation creates new opportunities
**Created**: 2026-01-02
**Last reviewed**: 2026-01-02

---

## The thesis

[[Inference disaggregation]] creates investment opportunities across the stack. As inference splits into prefill/decode with different optimal hardware, the supporting infrastructure becomes more valuable.

> "Memory bandwidth is now as important as compute."

---

## The stack layers

| Layer | Function | Beneficiaries |
|-------|----------|---------------|
| **Prefill silicon** | Prompt processing | [[NVIDIA]], [[Google]] TPU |
| **Decode silicon** | Token generation | [[Groq]], [[Cerebras]], [[Etched]], Rubin SRAM |
| **Edge Inference** | On-device processing | [[Arm Holdings]], [[Qualcomm]], [[Apple]] |
| **Interconnect** | Chip-to-chip data movement | NVIDIA (NVLink), [[Broadcom]], [[Lightmatter]] |
| **Memory** | [[HBM]] for prefill, SRAM for decode | [[SK Hynix]], [[Samsung]], [[Micron]] |
| **Networking** | Rack-to-rack | NVIDIA, [[Arista Networks]] |
| **Storage** | Context caching | WEKA, VAST Data |
| **Cooling** | Thermal management | [[Vertiv]], [[Modine Manufacturing]] |

---

## Why disaggregation expands TAM

Old model: One GPU does everything
New model: Specialized chips for each phase

| Effect | Implication |
|--------|-------------|
| More chip types | More silicon TAM |
| Interconnect critical | Networking premium |
| Memory hierarchy complex | Memory TAM expands |
| System integration harder | Services opportunity |

**Disaggregation is accretive to infrastructure spend, not cannibalistic.**

---

## The latency premium

Users will pay more for faster inference:

| Use case | Latency sensitivity | Willingness to pay |
|----------|---------------------|-------------------|
| Voice AI | Extreme | High |
| Agentic reasoning | High | High |
| Real-time copilots | High | Medium-High |
| Batch processing | Low | Low |

[[Agentic AI]] drives decode demand — this is where SRAM shines.

---

## Energy Efficiency: The Hidden Driver

Inference at scale is an energy problem. General-purpose GPUs are power-hungry. Specialized chips offer 10x better tokens-per-watt.

| Architecture | Efficiency | [[Trade]]-off |
|--------------|------------|-----------|
| **GPU (NVIDIA)** | Low | Maximum flexibility (runs anything) |
| **LPU (Groq)** | High | Deterministic, limited memory |
| **ASIC (Etched)** | Extreme | Zero flexibility ([[Transformer]] only) |

**Thesis Link:** [[Power constraints]] forces data centers to adopt specialized silicon for high-volume inference to stay within power envelopes.

---

## What validates the thesis

- [ ] Inference becomes >50% of AI compute spend
- [ ] Prefill/decode pricing diverges
- [ ] Interconnect revenue grows faster than silicon
- [ ] Memory shortage extends ([[HBM]] + SRAM)
- [ ] Agentic AI adoption accelerates

---

## What invalidates the thesis

- [ ] Training remains dominant cost
- [ ] Inference consolidates back to single architecture
- [ ] Open-source inference eliminates premium
- [ ] Demand growth slows

---

## [[Position sizing]] considerations

This is a basket thesis — multiple exposures:

| Exposure | Vehicle |
|----------|---------|
| Silicon | [[NVIDIA]] (see [[Long NVIDIA]]) |
| Memory | [[SK Hynix]], [[Samsung]], [[Micron]] (see [[Long memory]]) |
| Networking | [[Broadcom]], [[Arista Networks]] |
| Cooling | [[Vertiv]], [[Modine Manufacturing]] |

---

## Link to other theses

**[[Long NVIDIA]]**: Platform owner benefits most from disaggregation.

**[[Long memory]]**: [[HBM]] for prefill, memory bandwidth critical.

**[[Long Broadcom]]**: Interconnect and networking layer.

---

## Evidence log

| Date | Observation | Implication |
|------|-------------|-------------|
| 2025-12 | NVIDIA-Groq licensing | Disaggregation validated |
| 2025-12 | NVLink opens to external chips | Interconnect value rises |
| 2025-12 | Gavin Baker: 3 Rubin variants | Mix-and-match becomes standard |
| 2025-12 | Chamath: "Much cheaper → much more valuable" | Inference TAM expands |

---

## Related

- [[Inference disaggregation]] — mechanism (prefill/decode split)
- [[Long NVIDIA]] — component (platform benefits most)
- [[Long memory]] — component ([[HBM]] for prefill, memory bandwidth critical)
- [[Long Broadcom]] — component (interconnect, networking)
- [[Agentic AI]] — driver (decode-heavy use case)
- [[SK Hynix]] — beneficiary ([[HBM]] leader)
- [[Etched]] — ASIC challenger ([[Transformer]] only)
- [[Arm Holdings]] — edge inference architecture
- [[Qualcomm]] — edge inference chips
- [[Vertiv]] — beneficiary (cooling infrastructure)
- [[Lightmatter]] — optical interconnect (photonics)

---

*Review quarterly. Track inference vs training spend ratio.*
