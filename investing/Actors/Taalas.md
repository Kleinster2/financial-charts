---
aliases: [Taalas AI, Hard Coded Inference]
---
#actor #fabless #ai #inference #asic #canada

**Taalas** — Toronto chip startup that **hardwires AI model weights directly into silicon transistors**, producing model-specific ASICs that eliminate the memory wall entirely. Claims 10x the tokens/sec and 20x lower production cost vs. conventional GPU inference. Founded by ex-[[Tenstorrent]]/[[AMD]] team. One of the most radical architectural bets in AI silicon.

---

## Quick stats

| Metric | Value |
|--------|-------|
| HQ | Toronto, Canada |
| Founded | Mid-2023 (~2.5 years old) |
| Employees | ~25 |
| Total raised | **$219M** ($169M latest, Feb 19, 2026) |
| R&D spent | ~$30M (has $170M+ in the bank) |
| Key investors | Quiet Capital, [[Fidelity]], Pierre Lamond (legendary chip VC) |
| Foundry | [[TSMC]] (6nm N6 process) |
| First product | HC1 chip (Llama 3.1 8B) |

---

## Founders

All three co-founders came from [[Tenstorrent]], which itself spun out of the AMD/ATI chip design ecosystem in Toronto:

| Name | Role | Background |
|------|------|------------|
| **Ljubisa Bajic** | CEO | Founded [[Tenstorrent]]; senior architect at AMD (hybrid CPU-GPU) and NVIDIA. Left Tenstorrent when [[Jim Keller]] arrived (fall 2022) |
| **Lejla Bajic** | COO | Wife of Ljubisa. Senior engineer at ATI → AMD → Tenstorrent. Systems engineering lead |
| **Drago Ignjatovic** | CTO | Director of ASIC design at AMD, VP hardware engineering at Tenstorrent |
| **Paresh Kharya** | VP Products | Ex-NVIDIA (3 years, datacenter product mgmt) → Google Cloud (GPU/TPU infrastructure) |

The team is tiny (25 people) but deep — engineers from AMD, Apple, Google, NVIDIA, and Tenstorrent with experience shipping chips from idea to systems.

---

## The core idea: The Model IS the Computer

Traditional AI inference:
1. General-purpose GPU loads model weights from HBM memory
2. Shuffles data between compute units and memory repeatedly
3. Memory bandwidth becomes the bottleneck (the "memory wall")
4. Requires expensive HBM, complex packaging, massive cooling

**Taalas approach:**
1. **Encode model weights directly into transistors** as ROM — weights become part of the chip itself
2. **Large SRAM blocks** alongside compute — no HBM, no off-chip memory
3. **Computation happens at DRAM-level density** — eliminates the memory wall entirely
4. **No software overhead** — no CUDA, no frameworks, no driver stack. Pure silicon execution

The chip is fabricated with ~100 layers pre-built, then the **final 2 metal layers are customized** per model. This means TSMC can produce a model-specific chip in **~2 months** (vs ~6 months for a full NVIDIA Blackwell).

---

## HC1: First product

| Spec | Value |
|------|-------|
| Process | TSMC 6nm (N6) |
| Die size | Up to **815 mm²** (nearly H100-sized) |
| Model | Meta [[Llama]] 3.1 8B baked in |
| Form factor | PCIe card |
| Claims | **10x tokens/sec** vs high-end GPU infrastructure |
| Cost claims | **20x lower production cost** |
| No HBM | No advanced cooling, no complex packaging |

### DeepSeek R1 cluster demo

Taalas demonstrated [[DeepSeek]] R1 running at **12,000 tokens/sec/user** in a 30-chip configuration. For context, typical H100 inference clusters achieve ~1,000-2,000 TPS/user on comparable models.

---

## Why it matters

### Threat to NVIDIA's inference revenue

Taalas attacks the most valuable part of NVIDIA's future: **inference**, which is projected to be a **$250B+ market by 2030**. Over a model's lifetime, inference costs are **15x training costs** and utilization grows **31x per year**.

If Taalas works at scale, it fundamentally undermines the case for GPU-based inference:

| NVIDIA GPU inference | Taalas hardwired inference |
|---------------------|---------------------------|
| General-purpose (any model) | Model-specific (one model per chip) |
| Requires HBM ($$$) | No HBM — weights in ROM, context in SRAM |
| CUDA software stack | No software — pure silicon execution |
| ~6 month fabrication | ~2 month customization |
| Flexible — swap models anytime | Frozen — new chip per model version |
| $25K-$40K per GPU | Claims 20x lower production cost |

### The CUDA moat doesn't apply

Taalas completely sidesteps the [[CUDA moat]]. There IS no software stack — the model runs directly as hardware. This means:
- No need for CUDA compatibility
- No driver optimization
- No ROCm competition (AMD's problem disappears too)
- The competitive axis shifts from software ecosystem to **fabrication speed and cost**

### Economics at scale

For production inference (serving millions of users on a stable model), the math could be compelling:
- A hyperscaler running Llama 3 for 100M users doesn't change model weights hourly — it runs the same model for months
- At 10x TPS and 20x lower cost, Taalas chips could slash inference costs by an order of magnitude
- The 2-month turnaround means you CAN update — just not daily

---

## The tradeoffs (bear case)

| Risk | Detail |
|------|--------|
| **Model-locked** | Each chip is frozen to one model version. Update the model → need new silicon. Fine for production; useless for experimentation |
| **Scaling to frontier** | HC1 handles 8B parameter model. Frontier models are 1T+ parameters. Taalas says it will scale to GPT-5.2 class by end of 2026 — unproven |
| **Cluster complexity** | Large models need 30+ chip clusters (DeepSeek R1 demo). Interconnect and orchestration complexity at scale is unknown |
| **Model update frequency** | If the industry shifts to continuous model updates (weekly fine-tuning), hardwired chips become impractical |
| **TSMC dependency** | Single foundry, and Taalas is competing for capacity with NVIDIA, Apple, AMD |
| **Adoption friction** | Enterprises must commit to a specific model version before ordering silicon. That's a procurement paradigm shift |
| **Tiny team** | 25 people. Shipping production silicon to hyperscalers requires 10x the headcount |
| **No revenue** | Claims are impressive but there are zero production deployments yet |

---

## Competitive context

The AI inference silicon space is crowded:

| Company | Approach | Status |
|---------|----------|--------|
| **Taalas** | Hardwired model weights in ROM + SRAM | Pre-revenue, HC1 demo |
| [[Groq]] | SRAM-heavy LPU, software-defined | Acquired by [[NVIDIA]] for $20B (Jan 2026) |
| [[Cerebras]] | Wafer-scale engine, massive SRAM | [[OpenAI]] cloud deal (Jan 2026) |
| [[SambaNova]] | Dataflow architecture | [[Intel]] reportedly acquiring for $1.6B |
| [[Axelera AI]] | In-memory computing (D-IMC) | Edge/low-power focus, $250M raise |
| d-Matrix | SRAM-based digital in-memory compute | Stealth/early |
| [[NVIDIA]] | General-purpose GPU (H100/Blackwell/Rubin) | Dominant incumbent |
| [[AMD]] | General-purpose GPU (MI300X/MI450) | Scaling via [[commercial warrants]] |

**NVIDIA's Groq acquisition** is the tell — NVIDIA saw inference-specific silicon as enough of a threat to spend $20B neutralizing Groq. Taalas takes the same SRAM-centric approach but goes further by eliminating software entirely.

---

## Investment implications

Taalas is private, but the implications ripple across public markets:

1. **NVIDIA** — if hardwired inference works at scale, GPU inference revenue (the growth engine) is threatened. But NVIDIA can acquire (as it did with Groq)
2. **AMD** — same threat. AMD's [[commercial warrants]] strategy assumes GPUs remain the inference platform
3. **TSMC** — benefits regardless. More chip designs = more wafer demand
4. **GPU cloud providers** ([[CoreWeave]], [[Radiant (Brookfield)|Radiant]]) — their business model assumes GPUs. Model-specific ASICs could disrupt GPU rental economics
5. **Hyperscalers** — potential customers. If Meta can bake Llama into Taalas chips for 20x cheaper inference, why rent H100s?

---

## Related

- [[CUDA moat]] — Taalas sidesteps it entirely (no software stack)
- [[Inference economics]] — 10x TPS + 20x cost reduction would reshape the market
- [[NVIDIA]] — primary competitive threat (GPU-based inference)
- [[Groq]] — similar SRAM approach, acquired by NVIDIA for $20B
- [[Cerebras]] — wafer-scale competitor, OpenAI partnership
- [[TSMC]] — sole foundry partner
- [[Tenstorrent]] — all three founders came from here
- [[AMD]] — founders' original employer, competitive implications
- [[GPU rental price index]] — hardwired ASICs could crater rental prices
- [[Jim Keller]] — his arrival at Tenstorrent prompted Bajic to leave and start Taalas
- [[DeepSeek]] — R1 used in 30-chip cluster demo (12K TPS/user)
