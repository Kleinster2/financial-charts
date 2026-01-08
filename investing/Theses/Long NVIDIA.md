#thesis #trade #ai #semiconductor

# Long NVIDIA

**Status**: Core holding — platform dominance strengthening
**Created**: 2026-01-02
**Last reviewed**: 2026-01-08

---

## The thesis

NVIDIA's moat is not GPU performance — it's platform control. The [[Inference disaggregation]] thesis actually strengthens NVIDIA: they don't need to be best at everything, just control the hub.

> "The bottleneck moved, and the winning platform moved with it."

---

## Why platform beats product

NVIDIA's strategy:

| Layer | NVIDIA control |
|-------|----------------|
| Training | H100/H200/Blackwell dominance |
| Prefill | GPU-optimal, uncontested |
| Decode | Licensed Groq, building Rubin SRAM |
| Interconnect | NVLink, NVSwitch, InfiniBand |
| Software | CUDA ecosystem lock-in |

**The insight**: NVIDIA opened NVLink to external accelerators (Blackwell/Rubin generation). This is a position-of-strength move — "you open the ecosystem after you've become unavoidable."

---

## The Groq deal as validation

December 2025: NVIDIA licensed [[Groq]]'s SRAM architecture.

| What it signals |
|-----------------|
| NVIDIA acknowledges decode bottleneck |
| Prefers licensing to re-architecting |
| Won't cannibalize GPU margins |
| Will absorb specialists into platform |

Jensen chose to extend the platform rather than disrupt himself.

---

## Three Rubin variants

Gavin Baker's framework:

| Variant | Memory | Optimized for |
|---------|--------|---------------|
| **Rubin CPX** | GDDR | Massive context prefill |
| **Rubin** | HBM | Training + batched inference |
| **Rubin SRAM** | SRAM (Groq-derived) | Low-latency agentic decode |

**Mix and match** for optimal performance/cost per workload. No competitor offers this range.

---

## ASIC consolidation tailwind

Gavin Baker's prediction: most standalone ASICs will be canceled.

**Survivors:**
- NVIDIA (3 variants + ecosystem)
- Google TPU (vertical integration)
- Amazon Trainium (vertical integration)
- [[Cerebras]] (unique niche)

**Dies:**
- Meta ASIC
- Microsoft ASIC
- Most startups

"Consolidation by ecosystem gravity, not brute force."

---

## What validates the thesis

- [x] ~~Inference becomes dominant cost~~ **Already happening**
- [x] ~~NVIDIA extends to decode~~ **Groq licensing (Dec 2025)**
- [x] ~~Platform opening signals confidence~~ **NVLink-C2C announced**
- [ ] Rubin SRAM ships and performs
- [ ] Hyperscaler ASIC cancellations
- [ ] Agentic AI drives latency premium

---

## What invalidates the thesis

- [ ] Google TPU takes significant share
- [ ] Open-source inference stack emerges
- [ ] Training demand saturates
- [ ] China develops alternative ecosystem
- [ ] Regulatory intervention on market power

---

## Position sizing considerations

- NVIDIA already large in most portfolios
- Valuation reflects some of this
- But platform moat may be underappreciated
- Inference disaggregation is new narrative

---

## Link to other theses

**[[Long Broadcom]]**: Broadcom benefits from hyperscaler ASICs, but ASIC consolidation is bearish for ASIC TAM. Watch for cancellations.

**[[Long memory]]**: NVIDIA GPUs drive HBM demand. Rubin variants extend this.

**[[Long Anthropic]]**: Agentic AI drives decode demand — bullish for Rubin SRAM.

---

## Evidence log

| Date | Observation | Implication |
|------|-------------|-------------|
| 2025-12 | NVIDIA licenses Groq architecture | Platform absorption strategy |
| 2025-12 | NVLink-C2C enables external accelerators | Ecosystem opening from strength |
| 2025-12 | Gavin Baker: most ASICs will be canceled | Consolidation thesis |
| 2025-12 | Chamath: "Jensen operates at Elon level" | Platform vision validated |
| **2026-01-08** | **NVIDIA hits $5 trillion market cap** | **First company ever — dominance validated** |
| **2026-01-08** | **Intel partnership: $5B investment + NVLink collab** | **Platform expansion to x86, TSMC diversification hedge** |
| **2026-01-06** | **CES: Vera Rubin 5x Blackwell inference** | **Roadmap execution on track** |

---

## Related

- [[NVIDIA]] — subject (platform dominance)
- [[Groq]] — absorbed (licensed architecture Dec 2025)
- [[Cerebras]] — competitor/target (last independent)
- [[Inference disaggregation]] — opportunity (Rubin SRAM variant)
- [[Long Broadcom]] — related (but ASIC TAM at risk)
- [[Long memory]] — complementary (GPUs drive HBM demand)
- [[Long Anthropic]] — alignment (agentic drives decode demand)

---

*Review quarterly. Watch for Rubin SRAM timeline and ASIC cancellation news.*
