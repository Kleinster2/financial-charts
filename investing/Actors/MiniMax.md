---
aliases:
  - MiniMax AI
tags:
  - actor
  - ai-lab
  - china
---

# MiniMax

Chinese AI lab producing frontier-competitive models. Backed by [[HongShan]] ([[Neil Shen]]). Consumer app **Talkie** has gained US market traction. Completed Hong Kong IPO.

## M2.5 (Feb 2026)

![[openrouter-leaderboard-feb2026.jpg]]
*OpenRouter leaderboard, Feb 2026. MiniMax M2.5 #1 by token volume (3.07T, +524%).*

![[minimax-m25-swebench-comparison.jpg]]
*MiniMax M2.5 vs Claude Opus 4.5/4.6, Gemini 3 Pro, GPT-5.2 across coding benchmarks.*

| Benchmark | M2.5 | Claude Opus 4.6 | GPT-5.2 | Gemini 3 Pro |
|-----------|------|-----------------|---------|--------------|
| SWE-Bench Verified | **80.2** | 80.8 | 80 | 78 |
| SWE-Bench Pro | **55.4** | 55.4 | 55.6 | 54.1 |
| Terminal Bench 2 | **51.7** | 55.1 | 54 | 54 |
| Multi-SWE-Bench | **51.3** | 50.3 | — | 42.7 |
| SWE-Bench Multilingual | **74.1** | 77.8 | 72 | 65 |
| VIBE-Pro (AVG) | **54.2** | 55.6 | — | 36.9 |

Essentially tied with Western frontier models on coding benchmarks. Key differentiator: **speed**. Fireworks serves M2.5 at 273 tokens/sec — 2.5x the next provider.

![[minimax-m25-speed-benchmarks.jpg]]
*MiniMax M2.5 output speed by provider. Fireworks at 273 tok/s, 2.5x faster than #2.*

## Token volume dominance

M2.5 leads OpenRouter with 3.07T tokens processed — 5x [[Anthropic]]'s Claude Opus 4.6 (617B). Combined with [[Moonshot AI]]'s Kimi K2.5 (1.16T) and [[Zhipu AI]]'s GLM 5 (1.03T), Chinese models dominate the top 3 by volume, suggesting developers are voting with their wallets on cost/performance.

## Distillation accusations (Feb 23, 2026)

[[Anthropic]] accused MiniMax of the largest distillation campaign of the three Chinese labs — **13 million exchanges** with [[Claude]] via fraudulent accounts, targeting agentic coding, tool use, and orchestration. MiniMax redirected nearly half its traffic to siphon capabilities when [[Anthropic]] launched new [[Claude]] models.

Part of a broader pattern: [[OpenAI]] accused [[DeepSeek]] on Feb 12, [[Anthropic]] named [[DeepSeek]], [[Moonshot AI]], and MiniMax on Feb 23. Combined: 24,000+ fake accounts, 16M+ exchanges.

MiniMax's M2.5 benchmark performance (essentially tied with Western frontier models on coding — see above) raises the question of how much was built on distilled capabilities vs independent development.

See [[AI distillation wars (2025-2026)]] and [[model distillation]].

---

## Related

- [[HongShan]]
- [[Neil Shen]]
- [[Moonshot AI]]
- [[Zhipu AI]]
- [[Chinese AI labs]]
- [[Inference economics]]
- [[AI adoption curve]]
- [[AI distillation wars (2025-2026)]] — largest distillation campaign (13M exchanges with Claude)
- [[Model distillation]] — technique, accused by Anthropic (Feb 2026)
