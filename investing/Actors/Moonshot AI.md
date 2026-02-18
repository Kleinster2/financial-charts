---
aliases: [Moonshot, Kimi, Kimi AI, Dark Side of the Moon]
---
#actor #ai #china #private

**Moonshot AI** (月之暗面, "Dark Side of the Moon") — Beijing-based AI lab. Makes Kimi chatbot and models. Highest-valued Chinese AI unicorn at $4.8B. Alibaba, Tencent backed.

---

## Why Moonshot matters

Among the "AI Dragons" — [[China]]'s leading post-[[ChatGPT]] AI labs:

| Metric | Value |
|--------|-------|
| Valuation | $4.8B (Jan 2026); targeting $10B (Feb 2026) |
| Total raised | $1.77B over 3 rounds; $700M+ committed to new tranche |
| Cash reserves | >RMB 10B (~$1.4B) |
| HQ | [[Beijing]] |
| Founded | March 2023 |
| Kimi MAU | ~10-15M (down from 36M peak) |
| Key product | Kimi chatbot, K2.5 model |

**The Dragons:** [[MiniMax]] (IPO, >$29B), [[Zhipu]] (IPO, >$29B), Moonshot (private, targeting $10B), Stepfun (private), [[DeepSeek]] (bootstrapped).

---

## $10B valuation target (Feb 17, 2026)

Moonshot is expanding its latest funding round, targeting a $10B valuation — more than double the $4.3B from its Series C just weeks earlier:

- Kicked off discussions in late January to satisfy pent-up investor demand
- Existing backers [[Alibaba]], [[Tencent]], and 5Y Capital have committed >$700M to the first tranche
- At $10B, still undershoots closest rivals: [[Zhipu]] and [[MiniMax]] both valued >$29B after Hong Kong IPOs this year (raised >$1B combined)
- K2.5 is #2 on Artificial Analysis open-source rankings (behind Zhipu's GLM-5) and among the most-used LLMs on OpenRouter, ahead of [[DeepSeek]] and [[Google]] Gemini
- Launched OpenClaw cloud agent service for paid users (Feb 2026)
- Yang wrote internal memo (Dec 2025) saying company is in no rush for IPO — 10B yuan ($1.4B) cash on hand
- Paying users (China + overseas) grew 170% MoM during Sep-Nov 2025

Source: [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-17/china-ai-startup-moonshot-seeks-10-billion-value-in-new-funding)

---

## Kimi K2.5 (Jan 27, 2026)

Open-source multimodal model:

| Spec | Details |
|------|---------|
| Parameters | **1T total** (MoE), 32B active |
| Vision encoder | 400M parameters |
| Training data | 15T tokens (text + multimodal) |
| Architecture | Mixture of Experts |
| Optimization | Muon algorithm (faster training) |
| License | Open source ([[Hugging Face]]) |

**Benchmarks:**

| [[Benchmark]] | Score |
|-----------|-------|
| HLE-Full | **\#1** (highest ever) |
| SWE-Bench Verified | 76.8% |
| SWE-Bench Multilingual | 73.0% |
| Terminal-Bench 2.0 | 50.8% |
| LiveCodeBench v6 | **85.0%** |

Claims to beat GPT-5.2 on several benchmarks. Generally within a few points of Claude 4.5 Opus.

**Agent Swarm capability:**
- Up to 100 sub-agents running in parallel
- 1,500 tool calls concurrently
- 4.5x faster than single-agent models
- Splits complex tasks into sub-steps automatically

**Kimi Code:** New open-source coding tool launched alongside K2.5, competing with [[Claude]] Code and [[Gemini]] CLI.

---

## Model history

| Model | Date | Key feature |
|-------|------|-------------|
| Kimi v1 | 2023 | 128K context (first at this scale) |
| Kimi K1.5 | Jan 2025 | Matched [[OpenAI]] o1 on math/coding |
| Kimi K2 | Jul 2025 | 1T MoE, 32B active |
| Kimi K2 Thinking | Nov 2025 | Open-source reasoning, ~$4.6M training |
| **Kimi K2.5** | **Jan 2026** | Multimodal + agent swarm |

**Early differentiator:** First model with 128K context window. Long-context was Kimi's initial moat — now commoditized.

---

## Founding team

| Person | Role | Background |
|--------|------|------------|
| **[[Yang Zhilin]]** | Founder/CEO | Tsinghua BS (1st in class), CMU PhD (4 years), [[Google]] Brain, [[Meta]] AI |
| Zhou Xinyu | Co-founder | Tsinghua |
| Wu Yuxin | Co-founder | Tsinghua |

**Yang's credentials:**
- Original author of [[Transformer]]-XL and XLNet papers
- Worked under Ruslan Salakhutdinov, William Cohen at CMU
- Worked with Quoc V. Le at [[Google]] Brain, Jason Weston at [[Meta]] AI
- Previous startup: Recurrent AI (founded 2016, age 23)
- Also a drummer — band called Skip List

**Company name:** Launched on 50th anniversary of Pink Floyd's *The Dark Side of the Moon* (Yang's favorite album).

---

## Funding history

| Round | Date | Amount | Valuation | Lead investor |
|-------|------|--------|-----------|---------------|
| Seed | Mid-2023 | $60M | — | Early backers |
| Series A | Feb 2024 | $1B | $2.5B | [[Alibaba]] |
| Series B | Aug 2024 | $300M | $3.3B | [[Tencent]], Gaorong |
| Series C | Jan 2026 | $500M | $4.3B | IDG Capital |
| Latest | Jan 2026 | — | $4.8B | — |
| Expansion | Feb 2026 | $700M+ committed | Targeting $10B | Alibaba, Tencent, 5Y Capital |

Total raised: $1.77B + $700M+ new tranche in progress

**Key investors:** [[Alibaba]], [[Tencent]], IDG Capital, Sequoia [[China]], [[Meituan]], Xiaohongshu, Gaorong Capital.

---

## Cap table

Limited public disclosure. Known details:

| Holder | Notes |
|--------|-------|
| Yang Zhilin | Founder/CEO |
| [[Alibaba]] | Series A lead, cornerstone |
| [[Tencent]] | Series B participant |
| IDG Capital | Series C lead |
| Sequoia [[China]] | Early investor |
| [[Meituan]] | Series A participant |
| Xiaohongshu | Series A participant |

**Controversy:** Zhang Yutong reportedly concealed 14% stake in free shares. Separate from main investor dispute.

**Legal dispute:** Five investors in Yang's prior company (Recurrent AI) filed arbitration — GSR Ventures, Jingya Capital, Boyu Capital, Huashan Capital, Wanyu Capital. Alleged Yang launched Moonshot without consent waivers. No resolution disclosed.

---

## MAU trajectory

| Period | Kimi MAU | Notes |
|--------|----------|-------|
| Oct 2024 | **36M** | Peak |
| Jan 2026 | **10-15M** | Current |
| Decline | **>50%** | Long-context moat eroded |

**Comparison:** [[Doubao]] ([[ByteDance]]) has 160M+ MAU stable, leveraging [[Douyin]] distribution.

**Why the decline:** Long-context was Kimi's differentiator. Now [[Alibaba]]'s Tongyi Qianwen, [[Baidu]]'s Wenxin, and [[DeepSeek]] all have similar capability. When "long-text" stopped being unique, Kimi lost its edge.

---

## Competitive positioning

| vs | Moonshot advantage | Disadvantage |
|----|-------------------|--------------|
| [[DeepSeek]] | More funding, consumer focus | Less efficiency cred |
| [[Doubao]] | Open source, pure AI play | No [[Douyin]] distribution |
| [[MiniMax]] | Private (flexible) | No public market validation |
| US labs | Chinese market access | US export controls, talent |

---

## Investment implications

**Private company** — not directly investable.

**Indirect exposure:**
- [[Alibaba]] — major investor
- [[Tencent]] — investor
- IDG Capital — lead Series C

**Watch for:**
- IPO path (following [[MiniMax]], [[Zhipu]])
- Kimi MAU recovery
- K2.5 adoption vs [[DeepSeek]], open models
- Legal dispute resolution

---

## Quick stats

| Metric | Value |
|--------|-------|
| Status | Private (no rush for IPO per Dec 2025 memo) |
| Valuation | Targeting $10B (Feb 2026); last closed at $4.8B |
| Total raised | $1.77B + $700M+ new tranche |
| Key model | Kimi K2.5 (#2 open-source on Artificial Analysis) |
| Kimi MAU | 10-15M |
| HQ | [[Beijing]] |

*Updated 2026-02-17*

---

## Related

### People
- [[Yang Zhilin]] — founder/CEO ([[Transformer]]-XL author)

### Peers/Competitors
- [[DeepSeek]] — Chinese AI peer (efficiency leader)
- [[MiniMax]] — Chinese AI peer (IPO Jan 2026)
- [[Zhipu]] — Chinese AI peer (IPO Jan 2026)
- [[Alibaba]] — lead investor (Series A)
- [[Tencent]] — investor (Series B)
- [[ByteDance]] — competitor via [[Doubao]]
- [[Baidu]] — competitor (Wenxin)
- [[US-China AI race]] — competitive context
- [[Anthropic]] — competitor (Claude Code vs Kimi Code)
