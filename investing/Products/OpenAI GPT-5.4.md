---
aliases: [GPT-5.4]
---
# OpenAI GPT-5.4

#ai #openai #products

## Quick stats

| Metric | Value |
|--------|-------|
| Release | Mar 5, 2026 |
| Variants | GPT-5.4 (core), GPT-5.4 Thinking, GPT-5.4 Pro |
| Context | 1M tokens max (272K standard; premium pricing above 272K) |
| Training cutoff | Aug 31, 2025 |
| Pricing (standard) | $2.50/$15 per M tokens |
| Pricing (Pro) | $30/$180 per M tokens (12x premium) |
| Access | ChatGPT (Plus/Team/Pro/Enterprise/Edu), API, Codex |
| Positioning | Agentic — computer use, tool calling, professional knowledge work |

---

## Capabilities

- Native computer use: keyboard/mouse actions from screenshots — first general-purpose AI to outperform humans on OSWorld (75% vs 72.4% human reference). Can navigate desktops, click UIs, send emails, fill forms
- Better web use + multi-round search to identify sources and synthesize answers
- Tool use: higher accuracy/efficiency calling tools and APIs
- Reasoning: GPT-5.4 Thinking exposes outline of its work for complex queries (web + Android at launch; iOS coming)
- Factuality: OpenAI claims 33% fewer false individual claims vs GPT-5.2
- 47% reduction in token usage via dynamic resource management
- Codex now available on Windows (previously Mac-only)
- Released ~48 hours after GPT 5.3 Instant

---

## Benchmarks

| Benchmark | GPT-5.4 | Comparison | Notes |
|-----------|---------|------------|-------|
| GDP-Val (44 occupations) | 83.0% (70.8% wins, 83% incl. ties) | GPT-5.2: 70.9% | Blind-graded by domain experts. Tasks self-contained and digital. Pro scores *worse* than base |
| OSWorld (desktop computer use) | 75% | Human: 72.4% | First AI to surpass human reference on this benchmark |
| GPQA Diamond (Pro) | 94.3% | Gemini 3.1 Pro matches at 15x lower cost | — |
| SWE-bench Pro | 57.7% | Claude Opus 4.6: 80.8% | Coding not the differentiator |
| Investment banking modeling | 87.3% | GPT-5.2: 68.4% | Professional workflow strength |
| Hallucination rate (Artificial Analysis) | 89% BS rate when wrong | Worst among peers | Close to SOTA on overall accuracy, but least honest when wrong — fabricates rather than admitting ignorance |
| OpenAI Proof Q&A (internal) | Regression | Worse than GPT 5.3 Codex, 5.2 Codex, and 5.2 Thinking | 20 real R&D bottlenecks that each caused 1+ day delay. Spiky/jagged progress across domains |
| Destructive actions | Slight improvement on 5.2 Codex | Worse than 5.3 Codex | Overwriting code, deleting files |
| Frontier Math tier 4 | Solved problem curated ~20 years | — | Mathematician called it his *”personal move 37”* (referencing AlphaGo) |

---

## Assessment

The GDP-Val result is the headline: AI may have passed the point where, task-for-task, autonomous agents outperform humans in white-collar work — analogous to the self-driving crossover. The OSWorld result reinforces this — first AI to beat human reference on real desktop computer use. But the Proof Q&A regression and high BS rate show that progress remains domain-specific and spiky. Models excel where distilled training data exists; struggle where it doesn't. The central debate: will specialization in individual domains eventually generalize, or will each domain require its own rarified data?

GPT-5.4's competitive positioning is revealing: it doesn't try to win on coding (SWE-bench 57.7% vs Claude's 80.8%) or pure reasoning cost-efficiency (GPQA matched by Gemini at 15x lower price). Instead it differentiates on computer use and professional knowledge work — the agentic use cases where the loop is closing between generation, execution, and self-correction. This is [[OpenAI]]'s bet that the platform (agents acting in the real world) matters more than the model (benchmark scores).

Sources
- OpenAI announcement: https://openai.com/index/introducing-gpt-5-4/
- The Verge: https://www.theverge.com/ai-artificial-intelligence/889926/openai-gpt-5-4-model-release-ai-agents
- The New Stack: https://thenewstack.io/openai-launches-gpt-5-4/

Related
- [[OpenAI]] (actor)
- [[GPT]] — model family
- [[AI agents]]
