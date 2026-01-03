#thesis #trade #ai #semiconductor

# Short Standalone ASICs

**Status**: High conviction — consolidation underway
**Created**: 2026-01-02
**Last reviewed**: 2026-01-02

---

## The thesis

Most standalone AI ASICs will be canceled. Only vertically integrated hyperscalers and extreme niche players survive. "Consolidation by ecosystem gravity, not brute force."

> "All ASICs except TPU, AI5 and Trainium will eventually be canceled." — Gavin Baker

---

## Why ASICs are dying

NVIDIA's 3 Rubin variants + ecosystem make standalone competition nearly impossible:

| NVIDIA advantage | ASIC disadvantage |
|------------------|-------------------|
| 3 chip variants (CPX, HBM, SRAM) | Single-purpose design |
| NVLink ecosystem | PCIe isolation |
| CUDA software stack | Custom tooling |
| Networking (InfiniBand, NVSwitch) | Buy from NVIDIA anyway |
| Scale economics | Small volumes |

**The math**: Why build your own when NVIDIA offers mix-and-match?

---

## Survivors

| Player | Why survives |
|--------|--------------|
| **NVIDIA** | Platform owner, 3 variants |
| **Google TPU** | Vertical integration, captive workload |
| **Amazon Trainium** | Vertical integration, AWS lock-in |
| **[[Cerebras]]** | Unique niche (wafer-scale), strategic scarcity |

These survive because they either own the platform or have architectural uniqueness NVIDIA can't replicate.

---

## At risk

| Player | Problem |
|--------|---------|
| **Meta ASIC** | "Surprisingly weak" — may buy Rubin instead |
| **Microsoft ASIC** | Can't compete with Rubin variants |
| **Intel/[[SambaNova]]** | Late, weaker, acquired for defense |
| **Graphcore** | Already struggling |
| **Tenstorrent** | Niche, limited traction |
| **Most VC-backed startups** | Ecosystem gravity |

---

## The Broadcom complication

[[Broadcom]] designs ASICs for hyperscalers. If ASICs get canceled:

| Effect on Broadcom |
|-------------------|
| Near-term: Still designing TPU, Trainium |
| Long-term: TAM shrinks if Meta/MSFT cancel |
| Offset: Networking revenue grows |

Watch Broadcom's ASIC backlog carefully.

---

## What validates the thesis

- [ ] Meta cancels or scales back ASIC program
- [ ] Microsoft shifts to NVIDIA Rubin
- [ ] More ASIC startups shut down or pivot
- [ ] Hyperscaler capex shifts to NVIDIA
- [ ] TPU/Trainium remain but don't expand share

---

## What invalidates the thesis

- [ ] Meta ASIC succeeds at scale
- [ ] Open-source ASIC ecosystem emerges
- [ ] NVIDIA stumbles on Rubin
- [ ] Regulatory limits NVIDIA market power
- [ ] China ASIC ecosystem becomes viable

---

## How to express this

**Direct short**: Difficult — most targets are private or inside conglomerates.

**Indirect expressions**:

| Position | Rationale |
|----------|-----------|
| Long NVIDIA | Platform winner |
| Careful on Broadcom ASIC exposure | TAM risk |
| Avoid ASIC startup investments | High failure rate |
| Long Cerebras (speculative) | Survivor with scarcity value |

---

## The Meta ASIC as bellwether

Meta's ASIC program is the key signal:
- If canceled → thesis validated
- If succeeds → thesis challenged

Gavin Baker: "OpenAI's ASIC will be surprisingly good (much better than Meta and Microsoft ASICs)."

Watch for Meta capex guidance on custom silicon.

---

## Link to other theses

**[[Long NVIDIA]]**: Platform winner from ASIC consolidation.

**[[Long Cerebras]]**: Survivor because of unique architecture.

**[[Long Broadcom]]**: Mixed — designs ASICs but TAM at risk.

---

## Evidence log

| Date | Observation | Implication |
|------|-------------|-------------|
| 2025-12 | NVIDIA licenses Groq | Absorbs rather than competes |
| 2025-12 | Intel acquires SambaNova | Defensive consolidation |
| 2025-12 | Gavin Baker: most ASICs canceled | Smart money consensus |
| 2025-12 | 3 Rubin variants announced | Mix-and-match kills single-purpose |

---

## Related

- [[NVIDIA]] — winner (platform consolidates ASICs)
- [[Cerebras]] — survivor (unique wafer-scale niche)
- [[Google]] — survivor (TPU, vertical integration)
- [[Amazon]] — survivor (Trainium, vertical integration)
- [[Broadcom]] — mixed (designs ASICs, but TAM at risk)
- [[Inference disaggregation]] — mechanism (Rubin variants kill standalone)

---

*Review quarterly. Watch Meta and Microsoft ASIC program updates.*
