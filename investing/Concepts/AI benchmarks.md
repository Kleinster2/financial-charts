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

## Prediction-market layer (May 19, 2026)

[[Kalshi]] now has liquid AI-model-leadership markets that can be used as a sentiment overlay on benchmark data. These are not benchmark results; they are market-implied expectations about which lab will sit at the top of named ranking systems at resolution.

| Market | Top prices | Read-through |
|---|---|---|
| Best AI in Dec 2026 (KXLLM1) | [[Claude]] / [[Anthropic]] 59c; [[Gemini]] / [[Google DeepMind]] 20.9c; [[ChatGPT]] / [[OpenAI]] 12c; [[Grok]] / [[xAI]] 6.9c | Traders are pricing [[Anthropic]] as the year-end general-model leader, even with [[OpenAI]] still holding the distribution advantage. |
| Best coding model on Dec 31, 2026 (KXCODINGMODEL) | [[Anthropic]] 58c; [[OpenAI]] 25c; [[Google DeepMind]] 16c; [[xAI]] 4c | The coding-specific market is even more Anthropic-skewed, which makes it a useful cross-check against [[Claude Code]], [[Terminal-Bench]], and agentic-workflow revenue signals. |

The useful vault read is not that [[Claude]] will necessarily win. It is that public prediction-market participants are willing to pay up for an [[Anthropic]] leadership thesis in both general and coding benchmarks, while treating [[OpenAI]] as a strong but second-place probability mass and [[Google DeepMind]] as the main non-OpenAI challenger.

*Sources: [[Kalshi]] API series KXLLM1 and KXCODINGMODEL, read May 19, 2026: https://external-api.kalshi.com/trade-api/v2/markets?limit=1000&series_ticker=KXLLM1 and https://external-api.kalshi.com/trade-api/v2/markets?limit=1000&series_ticker=KXCODINGMODEL*

---

## Related

- [[Frontier models]] — primary subjects of benchmark evaluation
- [[Claude]] — [[Anthropic]]'s model family
- [[US-China AI race]] — benchmarks as competitive scoreboard
- [[Open source commoditization]] — benchmark convergence as evidence
- [[Kalshi]] — prediction-market source for model-leadership expectations
