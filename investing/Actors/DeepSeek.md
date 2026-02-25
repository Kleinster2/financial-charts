---
aliases: [DeepSeek AI]
---
#actor #china #ai #private

**DeepSeek** — [[Hangzhou]]-based AI lab. Division of High-Flyer quant fund. Known for efficiency — [[DeepSeek-R|R1]] triggered [[DeepSeek day]], wiping $600B from [[NVIDIA]].

---

## Quick stats

| Metric | Value |
|--------|-------|
| HQ | [[Hangzhou]] |
| Structure | High-Flyer division (not standalone) |
| Founder | Liang Wenfeng |
| Global chatbot share | **4%** |
| Approach | Efficiency-focused, open weights |

---

## Products

| Family | Description |
|--------|-------------|
| [[DeepSeek-V]] | General-purpose models (V2, V3) |
| [[DeepSeek-R]] | Reasoning models (R1, R2) |

See product notes for specs and versions.

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

## Distillation accusations (Feb 2026)

Both [[OpenAI]] (Feb 12) and [[Anthropic]] (Feb 23) publicly accused DeepSeek of systematically distilling their frontier models:

| Accuser | Date | Details |
|---------|------|---------|
| [[OpenAI]] | Feb 12 | DeepSeek employees used obfuscated routers to circumvent access restrictions on [[ChatGPT]] |
| [[Anthropic]] | Feb 23 | ~150,000 exchanges via fraudulent accounts targeting foundational logic, alignment, and censorship-safe alternatives to policy-sensitive queries |

[[Anthropic]]'s blog attributed the campaign "with high confidence" through IP correlation, request metadata, and corroboration from other labs. DeepSeek's operation was smaller in volume than [[MiniMax]] (13M) and [[Moonshot AI]] (3.4M) but focused on core reasoning capabilities.

Both disclosures timed to the US [[export controls]] debate — building the argument that API access needs restrictions, not just chips. Significant backlash over hypocrisy: the accusing labs themselves trained on scraped internet data without compensating creators, and [[Anthropic]] settled $1.5B over Library Genesis.

See [[AI distillation wars (2025-2026)]] and [[model distillation]].

---

## V4 model and Blackwell investigation (Feb 25, 2026)

Reuters exclusive (Feb 25): DeepSeek is withholding its latest V4 model from US chipmakers including [[NVIDIA]], giving early access to [[Huawei]] instead. A senior US official told Reuters that DeepSeek trained V4 on banned [[Blackwell]] chips — "likely clustered at its data center in Inner Mongolia" — potentially violating [[export controls]].

Federal investigation underway. [[NVIDIA]] has previously stated: "We're not shipping Blackwells to China." If confirmed, chips likely reached DeepSeek through gray market channels (see [[SEA chip diversion]]).

The shift to [[Huawei]] early access is strategic: DeepSeek optimizing for [[Ascend]] chips rather than NVIDIA hardware, aligning with Beijing's domestic chip ecosystem push.

---

## Chip situation

| Question | Answer |
|----------|--------|
| What chips? | H800s ([[China]]-legal), possibly some H100s |
| How many? | 10,000-50,000 (estimates vary) |
| Gray market? | Widely suspected, unconfirmed |

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

*Updated 2026-02-25*

---

## Related

- [[DeepSeek-R]] — reasoning model family
- [[DeepSeek-V]] — general model family
- [[DeepSeek day]] — event (Jan 27, 2025 market crash)
- [[Hangzhou]] — HQ ([[China]]'s AI hub)
- [[Microsoft]] — distribution (Azure)
- [[Export controls]] — constraint (GPU restrictions)
- [[Alibaba]] — peer ([[Qwen]] models)
- [[ByteDance]] — peer ([[Doubao]])
- [[NVIDIA]] — affected; technical assistance allegations
- [[John Moolenaar]] — House China Committee chair; Jan 2026 investigation
- [[AI distillation wars (2025-2026)]] — accused by both OpenAI and Anthropic (Feb 2026)
- [[Model distillation]] — technique used to extract capabilities from US labs
- [[Huawei]] — V4 early access partner, Ascend chip ecosystem
- [[SEA chip diversion]] — likely channel for banned Blackwell chips
