---
aliases:
  - Qwen
  - Qwen 2.5
  - Qwen 3
  - Qwen3
  - Qwen2.5-Max
  - Qwen3-Max
  - Tongyi Qianwen
  - 通义千问
tags:
  - product-family
  - ai
  - china
parent_actor: "[[Alibaba]]"
parent_concept: "[[Frontier models]]"
---

**Qwen** (通义千问) — [[Alibaba]]'s AI model family and consumer app. 203M MAU (Feb 2026), #3 AI app globally. 1B+ downloads across platforms. Qwen3-Max (1T+ params) competitive with frontier models. Originally fully open-source; as of April 2026, leading models kept proprietary for cloud customers.

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Alibaba]] |
| MAU | 203M (Feb 2026) |
| Global AI app rank | #3 (behind [[ChatGPT]], [[Doubao]]) |
| Flagship | Qwen3-Max (1T+ params) |
| Training data | 36T tokens |
| Languages | 119 |
| License | Apache 2.0 (open variants); leading models now proprietary |
| Parameters | 0.6B to 1T+ |
| Downloads | 1B+ across platforms |
| [[Hugging Face]] | 700M+ downloads |

*Updated 2026-04-10*

---

## MAU trajectory

| Date | MAU | Notes |
|------|-----|-------|
| Nov 17, 2025 | Launch | Public beta |
| Nov 24, 2025 | 10M downloads | First week |
| Nov 2025 | 18.3M | +149% MoM |
| Dec 2025 | 30M | |
| Jan 2026 | 100M+ | |
| Feb 2026 | 203M | Lunar New Year campaigns |

vs competitors (Feb 2026):

| App | MAU |
|-----|-----|
| [[ChatGPT]] | #1 |
| [[Doubao]] ([[ByteDance]]) | #2 |
| **Qwen** ([[Alibaba]]) | #3 — 203M |

---

## Model family

### Flagship: Qwen3-Max

| Spec | Details |
|------|---------|
| Parameters | 1T+ |
| Training tokens | 36T |
| Context | 1M tokens |
| Architecture | Dense (flagship) |
| Thinking mode | Integrated with tools |

Benchmarks:

| [[Benchmark]] | Score | vs Competitors |
|-----------|-------|----------------|
| Text Arena | Top 3 | Beat GPT-5-Chat |
| SWE-Bench Verified | 69.6 | Top coding tier |
| Tau2-Bench (agentic) | 74.8 | Beat Claude Opus 4, DeepSeek V3.1 |

Qwen3-Max-Thinking: Reasoning mode with web search, code interpreter, webpage extraction built in.

### Open source models

| Model | Params | Active | Notes |
|-------|--------|--------|-------|
| Qwen3-235B-A22B | 235B | 22B | MoE, Apache 2.0 |
| Qwen3-Coder-480B | 480B | 35B | Agentic coding, 256K context |
| Qwen3-32B | 32B | Dense | Mid-range |
| Qwen3-14B/8B/4B | Various | Dense | [[Consumer]] GPUs |
| Qwen3-Omni | — | — | Multimodal (glasses, cockpits) |

Qwen3-235B benchmarks:

| [[Benchmark]] | Score |
|-----------|-------|
| ArenaHard | 95.6 |
| LiveBench | 77.1 |
| LiveCodeBench v6 | 74.8 |
| AIME25 (thinking) | 92.3 |

Competitive with [[Gemini]] 2.5 Pro across the board.

---

## Version history

| Model | Release | Key changes |
|-------|---------|-------------|
| Qwen 1.0 | Aug 2023 | Initial release |
| Qwen 1.5 | Feb 2024 | Improved reasoning |
| Qwen 2 | Jun 2024 | Major upgrade |
| Qwen 2.5 | Sep 2024 | 29+ languages, 8K output |
| Qwen 2.5-Max | Jan 2025 | MoE, rivals DeepSeek-V3 |
| Qwen 2.5-VL | Jan 2025 | Vision-language |
| Qwen 2.5-Omni | Mar 2025 | Text/image/video/audio I/O |
| Qwen 3 | Apr 2025 | 36T tokens, 119 languages, reasoning |

### Qwen 3 model sizes

| Model | Params | Architecture |
|-------|--------|--------------|
| Qwen3-0.6B | 0.6B | Dense |
| Qwen3-1.7B | 1.7B | Dense |
| Qwen3-4B | 4B | Dense |
| Qwen3-8B | 8B | Dense |
| Qwen3-14B | 14B | Dense |
| Qwen3-32B | 32B | Dense |
| Qwen3-30B-A3B | 30B (3B active) | MoE |
| Qwen3-235B-A22B | 235B (22B active) | MoE |

---

## Key capabilities

| Feature | Details |
|---------|---------|
| Reasoning | Toggle on/off (like o1, QwQ) |
| Coding | Rivals GPT-4 (Python, JS, C++) |
| Function calling | OpenAI-compatible format |
| Long output | Up to 8K tokens |
| Multimodal | Vision, audio (Omni variant) |

---

## Qwen 2.5-Max

| Aspect | Details |
|--------|---------|
| Architecture | Mixture-of-Experts |
| Training | 20 trillion tokens |
| Claims | Outperforms GPT-4o, DeepSeek-V3, Llama-405B |
| License | Closed (unlike other Qwen models) |

---

## Pricing

| Tier | Cost |
|------|------|
| API (input) | $0.20-$1.20 per M tokens |
| vs GPT-4.5 | ~0.2% of cost |
| vs DeepSeek V3 | ~40% of cost |
| Open weights | Free (Apache 2.0) |

---

## Distribution

| Channel | Strategy |
|---------|----------|
| Qwen App | [[Consumer]] chatbot (203M MAU) |
| [[Alibaba Cloud]] | Enterprise API |
| [[Hugging Face]] | Open weights |
| [[Taobao]]/Tmall | E-commerce integration |
| DingTalk | Enterprise messaging |

Key advantage: Alibaba's cloud + commerce ecosystem for distribution.

---

## Open source strategy — evolving

Original thesis (2023-early 2026): Sacrifice short-term API revenue for global adoption.

| Approach | Outcome |
|----------|---------|
| Apache 2.0 license | Anyone can use commercially |
| Full model weights | Not just API access |
| Multiple sizes | 0.6B to 480B+ |
| Regular releases | Qwen3 family expanding |

Result: Qwen + [[DeepSeek]] = 30% of global AI model usage.

### April 2026 pivot

[[Alibaba]] now keeping leading Qwen models proprietary for cloud customers. Zhou Jingren (former [[Alibaba Cloud]] CTO) replaced Lin Junyang as AI division head after internal disagreements over commercialization. Lin was under increasing pressure from senior management about resources being spent training open-source models, particularly after [[MiniMax]], [[Zhipu]], and [[Moonshot AI]] released models around Lunar New Year that outperformed Qwen in coding. Alibaba released a flurry of closed-source models in April 2026.

Open-source continues for select models (smaller variants, [[Happy Horse]] video generation) but flagship models are closed-source. MaaS (model-as-a-service) is now positioned as a key cloud revenue driver — Eddie Wu flagged it in the Q1 2026 earnings call. [[Meta]] made a parallel shift with [[Muse Spark]] replacing [[Llama]].

The broader industry consensus: with value shifting to AI applications (coding, agents), building powerful models alone is not enough — the revenue has to come from somewhere. See [[Alibaba#Qwen leadership transition — open-source to revenue pivot (2026)]].

*Source: FT (Apr 10, 2026)*

---

## Competitive position

| vs | Qwen advantage | Disadvantage |
|----|---------------|--------------|
| [[Doubao]] | Open variants, enterprise | Less consumer distribution |
| [[DeepSeek]] | Alibaba resources, multimodal | DeepSeek efficiency |
| [[ChatGPT]] | Price, open variants | Brand, global reach |
| [[Claude]] | Price, agentic benchmarks | Less polish |
| [[GPT]] | Free open variants, price | Ecosystem maturity |
| [[Llama]] | Multilingual (119 vs 8) | Meta pivoting to proprietary too |

---

## Investment implications

Not directly investable — Qwen is an Alibaba product.

Indirect exposure:
- [[Alibaba]] (BABA/9988.HK) — parent, directly benefits
- [[NVIDIA]] — Alibaba GPU customer

Thesis implications:
- Open source winning in [[China]] (for now — proprietary pivot may change dynamics)
- [[Alibaba Cloud]] differentiated by AI
- Price war compressing API margins globally

---

## Related

- [[Alibaba]] — parent company
- [[Alibaba Cloud]] — distribution platform
- [[Happy Horse]] — open-source video gen (Apr 2026)
- [[Doubao]] — competitor (#1 China)
- [[DeepSeek]] — open source peer
- [[DeepSeek-V]] — competitor (model family)
- [[Moonshot AI]] — competitor (Kimi)
- [[Hunyuan]] — competitor ([[Tencent]])
- [[Ernie]] — competitor ([[Baidu]])
- [[ChatGPT]] — global competitor
- [[Llama]] — competitor (open, Meta pivoting to proprietary)
- [[GLM]] — competitor (China)
- [[Frontier models]] — category
- [[Chinese open models]] — ecosystem context
- [[China]] — market
