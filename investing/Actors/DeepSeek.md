---
aliases: [DeepSeek AI, DeepSeek R1]
---
#actor #china #ai #models

**DeepSeek** — Hangzhou-based AI lab. DeepSeek R1 model notable for efficiency. Available on Azure, competitive with frontier models at lower cost.

---

## Why DeepSeek matters

China's most prominent open-ish AI lab, known for efficiency:

| Metric | Value |
|--------|-------|
| HQ | [[Hangzhou]] |
| Key model | DeepSeek R1 |
| Approach | Efficiency-focused, open weights |
| Availability | Azure, Hugging Face, self-host |
| Backed by | High-Flyer (quant fund) |

---

## DeepSeek V3 (Dec 2024)

The early warning that most missed:

| Spec | Details |
|------|---------|
| Parameters | 671B total, 37B active per query |
| Architecture | Mixture of Experts (MoE) |
| Training compute | 2048 H800s (~2M GPU hours) |
| Claimed cost | ~$6M (final run only) |
| Performance | Competitive with GPT-4 Turbo |

**Who noticed:** Some VCs, quant funds, China watchers. Wall Street largely missed it.

---

## The cost/chip debate

**The $6M claim is misleading:**

| What it includes | What it excludes |
|------------------|------------------|
| Final training run | Prior experiments, failed runs |
| Compute only | Infrastructure, salaries, R&D |

**Real investment:** Likely $100M+ over 2+ years. Still far below US labs.

**The chip situation:**

| Question | Answer |
|----------|--------|
| What chips? | H800s (China-legal), possibly some H100s |
| How many? | 10,000-50,000 (estimates vary) |
| Gray market? | Widely suspected, unconfirmed |
| The point | Made fewer/weaker chips work through efficiency |

---

## DeepSeek R1 (Jan 2025)

| Spec | Details |
|------|---------|
| Type | Reasoning model (like OpenAI o1) |
| Architecture | MoE with chain-of-thought |
| Efficiency | Lower cost/token than GPT-4 |
| Weights | Open (downloadable) |
| Inference | Runs on consumer hardware |

**Why it matters:** Proves China can build competitive models despite GPU restrictions. Efficiency offsets hardware disadvantage.

**Why R1 hit harder than V3:** Reasoning models are the hardest task — proving efficiency works here meant it works everywhere.

**Market impact:** R1 release triggered [[DeepSeek day]] (Jan 27, 2025) — NVIDIA lost $600B, largest single-day market cap loss in US history.

---

## mHC Research (Jan 2026)

One year later, DeepSeek published research validating their efficiency claims:

| Spec | Details |
|------|---------|
| Paper | "Manifold-Constrained Hyper-Connections" (mHC) |
| Published | January 1, 2026 |
| Co-author | Liang Wenfeng (founder) |
| Tested | Models up to 27B parameters |
| Claim | "Superior scalability with negligible computational overhead" |

**Why it matters:** Technical proof behind the efficiency claims that crashed markets a year earlier. Not just a one-off — a systematic approach.

**Builds on:** [[ByteDance]] 2024 research into hyper-connection architectures.

**Industry reaction:**
- Counterpoint (Wei Sun): "striking breakthrough" that "bypasses compute bottlenecks"
- Omdia (Lian Jye Su): Publishing shows "newfound confidence in Chinese AI industry"

**What's next:** R2 model expected around Feb 2026 (Spring Festival), continuing pattern of holiday releases.

---

## LiveBench rankings (Jan 2026)

| Rank tier | Models |
|-----------|--------|
| Top 3 | Google Gemini 3 (overtook OpenAI Nov 2025) |
| Top 15 | **2 Chinese low-cost models** |

**The efficiency story:** China's models developed at fraction of US cost now competitive on global benchmarks.

---

## Humanity's Last Exam (mid-2025)

Rigorous benchmark with thousands of questions across math, science, other subjects:

| Model | Accuracy |
|-------|----------|
| OpenAI | >20% |
| Google | >20% |
| xAI | >20% |
| **DeepSeek** | **14%** |
| Qwen | 11% |

**Sam Altman (May 2025 hearing):** "It is very hard to say how far ahead we are. But I would say not a huge amount of time."

**Implication:** Gap exists but narrowing. Efficiency-focused development closing distance despite chip constraints.

---

## Available on major platforms

| Platform | Status |
|----------|--------|
| [[Microsoft]] Azure | ✓ (listed alongside GPT, Claude) |
| Hugging Face | ✓ (open weights) |
| Self-hosted | ✓ |
| China cloud | ✓ (Alibaba, etc.) |

Azure listing is notable — Microsoft offering Chinese model alongside OpenAI, Anthropic.

---

## Backing: High-Flyer

DeepSeek is backed by High-Flyer (幻方量化), a major Chinese quant fund:

| Aspect | Details |
|--------|---------|
| Type | Quantitative hedge fund |
| AUM | $8B+ |
| Why AI | Compute for trading → AI research |
| Approach | Patient capital, long-term research |

**Unusual model:** Quant fund funding AI lab. Compute infrastructure repurposed.

---

## Efficiency thesis

DeepSeek represents China's response to GPU constraints:

| US approach | China/DeepSeek approach |
|-------------|-------------------------|
| Best chips (Blackwell) | Efficient algorithms |
| Scale compute | Optimize per-FLOP |
| Frontier capability | Competitive at lower cost |

**The insight:** If you can't get the best chips, make better use of the chips you have. MoE architecture, distillation, quantization.

---

## Competitive positioning

| vs Model | DeepSeek advantage | Disadvantage |
|----------|-------------------|--------------|
| GPT-4 | Cheaper, open weights | Less capable on some tasks |
| Claude | Self-hostable | Smaller context, less polish |
| Llama | Comparable openness | Less community adoption |
| Qwen | More efficient | Alibaba has more resources |

---

## Financials

| Metric | Value |
|--------|-------|
| Status | Private (not separately funded) |
| Backer | High-Flyer (幻方量化) |
| High-Flyer AUM | $8B+ |
| Valuation | Not disclosed (internal project) |
| Revenue model | API access, open weights |
| Funding approach | Internal (quant fund profits) |

**Unusual structure:** DeepSeek is not a typical startup. It's an AI research arm of High-Flyer, funded by quant trading profits. No external VC rounds announced.

---

## Investment implications

**Private company** — not directly investable.

**Indirect exposure:**
- [[Microsoft]] — offers R1 on Azure
- [[Alibaba]] — offers on China cloud
- [[NVIDIA]] — still needs GPUs (H200 likely)

**Thesis implications:**
- Validates China AI capability despite [[Export controls]]
- Efficiency-focused approach may influence global model development
- Open weights pressure closed model pricing

---

*Updated 2026-01-04*

---

## Related

- [[DeepSeek day]] — event (Jan 27, 2025 market crash)
- [[Hangzhou]] — HQ (China's AI hub)
- [[Microsoft]] — distribution (Azure)
- [[Model landscape]] — context (China open models)
- [[China AI clusters]] — context (compute infrastructure)
- [[Export controls]] — constraint (GPU restrictions)
- [[Inference economics]] — thesis (efficiency implications)
- [[Open source commoditization]] — trend (open weights pressure)
- [[Alibaba]] — peer (Qwen models)
- [[ByteDance]] — peer (Doubao)
- [[NVIDIA]] — affected (largest single-day loss)
