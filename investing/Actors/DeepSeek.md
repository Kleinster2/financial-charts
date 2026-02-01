---
aliases: [DeepSeek AI, DeepSeek R1]
---
#actor #china #ai #models #private

**DeepSeek** — Hangzhou-based AI lab. DeepSeek R1 model notable for efficiency. Available on Azure, competitive with frontier models at lower cost.

**The DeepSeek moment:** R1's January 2025 release surprised everyone — near state-of-the-art with allegedly much less compute. Kicked off a movement in China similar to how ChatGPT kicked off US AI boom. Secretive in communication but open in technical reports.

---

## Why DeepSeek matters

[[China]]'s most prominent open-ish AI lab, known for efficiency:

| Metric | Value |
|--------|-------|
| HQ | [[Hangzhou]] |
| Key model | DeepSeek R1 |
| Global chatbot share | **4%** (vs [[ChatGPT]] 68%, [[Gemini]] 18%) |
| Approach | Efficiency-focused, open weights |
| Availability | Azure, [[Hugging Face]], self-host |
| Backed by | High-Flyer (quant fund) |
| Next model | Expected within weeks (R2) |

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

**Who noticed:** Some VCs, quant funds, [[China]] watchers. Wall Street largely missed it.

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
| What chips? | H800s ([[China]]-legal), possibly some H100s |
| How many? | 10,000-50,000 (estimates vary) |
| Gray market? | Widely suspected, unconfirmed |
| The point | Made fewer/weaker chips work through efficiency |

---

## DeepSeek R1 (Jan 2025)

| Spec | Details |
|------|---------|
| Type | Reasoning model (like [[OpenAI]] o1) |
| Architecture | MoE with chain-of-thought |
| Efficiency | Lower cost/token than GPT-4 |
| Weights | Open (downloadable) |
| Inference | Runs on consumer hardware |

**Why it matters:** Proves [[China]] can build competitive models despite GPU restrictions. Efficiency offsets hardware disadvantage.

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
- [[Omdia]] (Lian Jye Su): Publishing shows "newfound confidence in Chinese AI industry"

**What's next:** R2 model expected around Feb 2026 (Spring Festival), continuing pattern of holiday releases.

---

## Government scrutiny (Jan 2026)

| Country | Action |
|---------|--------|
| **[[Australia]]** | Banned from all government devices (security concerns) |
| **Czech Republic** | Banned from public administration (data security concerns) |
| Various | Privacy policy scrutiny — stores data in [[China]] |

DeepSeek's privacy policy explicitly states personal data stored on computers in [[China]]. Multiple governments reviewing security implications.

**NVIDIA assistance allegations (Jan 28, 2026):**
- **[[John Moolenaar]]** (R-MI), chair of House Select Committee on [[China]], sent letter to Commerce Secretary Lutnick
- Documents from [[NVIDIA]] show technical assistance helped DeepSeek achieve training efficiency
- Internal docs: "DeepSeek-V3 requires only 2.788M H800 GPU hours for its full training — less than what US developers typically require"
- Moolenaar acknowledged NVIDIA treated DeepSeek "as a legitimate commercial partner" at the time
- **NVIDIA response:** "China has more than enough domestic chips for all of its military applications... it makes no sense for the Chinese military to depend on American technology"

---

## One-year anniversary (Jan 27, 2026)

**Today marks one year since [[DeepSeek day]]** — the Jan 27, 2025 crash that wiped $600B from [[NVIDIA]] and ~$1T from tech stocks overall.

**What's changed:**
- DeepSeek now at 4% global chatbot share (from zero)
- [[MiniMax]], [[Zhipu]] IPOs validated Chinese AI sector
- Startup valuations doubled ($10-20M → $20-40M)
- US still dominant but gap narrowing

---

## LiveBench rankings (Jan 2026)

| Rank tier | Models |
|-----------|--------|
| Top 3 | [[Google]] [[Gemini]] 3 (overtook [[OpenAI]] Nov 2025) |
| Top 15 | **2 Chinese low-cost models** |

**The efficiency story:** [[China]]'s models developed at fraction of US cost now competitive on global benchmarks.

---

## Humanity's Last Exam (mid-2025)

Rigorous benchmark with thousands of questions across math, science, other subjects:

| Model | Accuracy |
|-------|----------|
| [[OpenAI]] | >20% |
| [[Google]] | >20% |
| [[xAI]] | >20% |
| **DeepSeek** | **14%** |
| [[Qwen]] | 11% |

**[[Sam Altman]] (May 2025 hearing):** "It is very hard to say how far ahead we are. But I would say not a huge amount of time."

**Implication:** [[Gap]] exists but narrowing. Efficiency-focused development closing distance despite chip constraints.

---

## Available on major platforms

| Platform | Status |
|----------|--------|
| [[Microsoft]] Azure | ✓ (listed alongside GPT, [[Claude]]) |
| [[Hugging Face]] | ✓ (open weights) |
| Self-hosted | ✓ |
| [[China]] cloud | ✓ (Alibaba, etc.) |

Azure listing is notable — Microsoft offering Chinese model alongside [[OpenAI]], [[Anthropic]].

**Regional adoption (Jan 2026):**
- [[Microsoft]] noted DeepSeek usage in Africa is **2-4x higher** than in other regions
- Cost efficiency driving adoption in price-sensitive markets

---

## Cap table / Ownership

**Unusual structure:** DeepSeek is not a typical VC-backed startup. It's an internal AI research division of High-Flyer (幻方量化).

| Aspect | Details |
|--------|---------|
| Parent | High-Flyer (幻方量化) |
| Structure | Internal division, not separate entity |
| External funding | None announced |
| Founder | Liang Wenfeng (also High-Flyer founder) |

### High-Flyer (parent)

| Metric | Value |
|--------|-------|
| Type | Quantitative hedge fund |
| AUM | $8B+ |
| HQ | [[Hangzhou]] |
| Why AI | Compute for trading → AI research |

**Funding model:** Profits from quant trading fund AI research. No external VC rounds. This gives DeepSeek unusual patience and independence.

---

## Efficiency thesis

DeepSeek represents [[China]]'s response to GPU constraints:

| US approach | [[China]]/DeepSeek approach |
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
| [[Claude]] | Self-hostable | Smaller context, less polish |
| [[Llama]] | Comparable openness | Less community adoption |
| [[Qwen]] | More efficient | Alibaba has more resources |

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

## Quick stats

| Metric | Value |
|--------|-------|
| Status | Private (High-Flyer subsidiary) |
| Global chatbot share | 4% |
| Key model | DeepSeek R1 |
| HQ | [[Hangzhou]] |
| Next model | R2 (expected Feb 2026) |

---

## Investment implications

**Private company** — not directly investable.

**Indirect exposure:**
- [[Microsoft]] — offers R1 on Azure
- [[Alibaba]] — offers on [[China]] cloud
- [[NVIDIA]] — still needs GPUs (H200 likely)

**Thesis implications:**
- Validates [[China]] AI capability despite [[Export controls]]
- Efficiency-focused approach may influence global model development
- Open weights pressure closed model pricing

---

*Updated 2026-01-29*

---

## Related

- [[DeepSeek day]] — event (Jan 27, 2025 market crash)
- [[Hangzhou]] — HQ ([[China]]'s AI hub)
- [[Microsoft]] — distribution (Azure)
- [[Model landscape]] — context ([[China]] open models)
- [[China AI clusters]] — context (compute infrastructure)
- [[Export controls]] — constraint (GPU restrictions)
- [[Inference economics]] — thesis (efficiency implications)
- [[Open source commoditization]] — trend (open weights pressure)
- [[Alibaba]] — peer ([[Qwen]] models)
- [[ByteDance]] — peer ([[Doubao]])
- [[NVIDIA]] — affected (largest single-day loss); technical assistance allegations
- [[John Moolenaar]] — House China Committee chair; Jan 2026 investigation
