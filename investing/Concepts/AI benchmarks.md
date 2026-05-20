---
aliases:
  - AI benchmark
  - model benchmarks
  - LLM benchmarks
tags:
  - concept
  - ai
---

# AI benchmarks

Standardized evaluations for measuring AI model capabilities. Used by labs to differentiate products and by investors to track competitive positioning.

---

## Key benchmarks tracked

| Benchmark | Measures | Created by |
|-----------|----------|------------|
| [[OSWorld]] | Computer use / GUI automation | XLANG Lab (HKU) |
| [[Terminal-Bench]] | Agentic terminal/CLI tasks | Stanford / Laude Institute |
| [[Humanity's Last Exam]] | Expert-level multidisciplinary reasoning | CAIS / Scale AI |
| [[ARC-AGI]] | Abstract reasoning / fluid intelligence | [[Francois Chollet]] |
| [[SWE-Bench]] | Software engineering tasks | Princeton |
| [[MMLU]] | Academic knowledge breadth | UC Berkeley |

---

## Investment relevance

Benchmarks serve three functions in the vault:

1. Product tier differentiation — justifying pricing (e.g., [[Claude Opus]] vs [[Claude Sonnet]] on Terminal-Bench)
2. Competitive tracking — [[US-China AI race]], [[Open source commoditization]] use benchmark gaps as evidence
3. Capability validation — agentic benchmarks ([[OSWorld]], [[Terminal-Bench]]) directly correlate with product revenue potential (e.g., [[Claude Code]] at $2.5B run rate)

Gap closure is the key signal: [[MMLU]] gap between open and closed models shrank from 17.5 to 0.3 points in one year.

---

## Prediction-market layer (May 20, 2026)

[[Kalshi]] now has liquid AI-model-leadership markets that can be used as a sentiment overlay on benchmark data. These are not benchmark results; they are market-implied expectations about which lab will sit at the top of named ranking systems at resolution.

| Market | Top prices | Read-through |
|---|---|---|
| Best AI on May 23, 2026 (KXLLM1-26MAY23) | [[Claude]] / [[Anthropic]] 96c last, 96c / 97c bid-ask; [[ChatGPT]] / [[OpenAI]] 3c; [[Gemini]] / [[Google DeepMind]] 1c; [[Grok]] / [[xAI]] 1c | The near-term ranking market treats [[Claude]] as already entrenched at the top, not merely as a year-end contender. |
| Best AI on May 31, 2026 (KXLLM1-26MAY31) | [[Claude]] / [[Anthropic]] 97c; [[ChatGPT]] / [[OpenAI]] 3c; [[Gemini]] / [[Google DeepMind]] 3c; [[Grok]] / [[xAI]] 1c | Month-end pricing is even more concentrated than the longer-dated market, so any non-Anthropic win would be a genuine benchmark-tape upset. |
| Best AI in Dec 2026 (KXLLM1-26DEC31) | [[Claude]] / [[Anthropic]] 64c last, 62.6c / 62.9c bid-ask; [[Gemini]] / [[Google DeepMind]] 20.6c; [[ChatGPT]] / [[OpenAI]] 12c; [[Grok]] / [[xAI]] 5.1c; [[Meta]] LLaMA 2.1c | Traders are still paying up for an [[Anthropic]] year-end leadership thesis, but the longer-dated market leaves meaningful room for [[Google DeepMind]] or [[OpenAI]] catch-up. |
| Best coding model on Dec 31, 2026 (KXCODINGMODEL) | [[Anthropic]] 55c; [[OpenAI]] 25c; [[Google DeepMind]] 13c; [[xAI]] 4c | The coding-specific market is still Anthropic-skewed, making it a useful cross-check against [[Claude Code]], [[Terminal-Bench]], [[SWE-Bench]], and agentic-workflow revenue signals. |

The useful vault read is not that [[Claude]] will necessarily win. It is that public prediction-market participants are willing to pay up for an [[Anthropic]] leadership thesis in both general and coding benchmarks, while treating [[OpenAI]] as a strong but second-place probability mass and [[Google DeepMind]] as the main non-OpenAI challenger. The shape also fits the enterprise-agent tape: [[Anthropic]] is priced strongest where benchmarks map most directly to monetizable coding and workflow products, while [[OpenAI]] still owns distribution.

Adjacent lab-capital-market read: KXOAIANTH prices [[Anthropic]] at 83c last, 79c / 82c bid-ask to IPO before [[OpenAI]], versus [[OpenAI]] at 27c last, 27c / 30c bid-ask. That is not a benchmark market, but it reinforces the same public-market narrative: traders currently prefer the Anthropic execution story even though OpenAI remains the larger consumer platform.

*Sources: [[Kalshi]] API series KXLLM1, KXCODINGMODEL, and KXOAIANTH, read May 20, 2026: https://external-api.kalshi.com/trade-api/v2/markets?limit=1000&series_ticker=KXLLM1, https://external-api.kalshi.com/trade-api/v2/markets?limit=1000&series_ticker=KXCODINGMODEL, and https://external-api.kalshi.com/trade-api/v2/markets?limit=1000&series_ticker=KXOAIANTH*

---

## Related

- [[Frontier models]] — primary subjects of benchmark evaluation
- [[Claude]] — [[Anthropic]]'s model family
- [[US-China AI race]] — benchmarks as competitive scoreboard
- [[Open source commoditization]] — benchmark convergence as evidence
- [[Kalshi]] — prediction-market source for model-leadership expectations
