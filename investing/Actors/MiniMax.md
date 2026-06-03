---
aliases:
  - MiniMax AI
tags:
  - actor
  - ai-lab
  - china
---

# MiniMax

[[China|Chinese]] AI lab producing frontier-competitive models and AI products. Backed by [[HongShan]] ([[Neil Shen]]) and now public on [[HKEX]] as 0100.HK. Talkie has gained US market traction; [[Hailuo]] is the video product; [[MiniMax M3]] is the June 2026 long-context / multimodal model release.

The investment question has shifted from private-lab funding to public-market capital formation: MiniMax is already a Hong Kong-listed Chinese AI lab and is now exploring a STAR Market RMB-share route that would give mainland investors direct exposure to the model layer.

## Quick stats

| Metric | Value |
|--------|-------|
| Primary listing | [[HKEX]] 0100.HK |
| Founder / chair | [[Yan Junjie]] |
| Backing | [[HongShan]], [[Tencent]], [[Alibaba]]-linked ecosystem investors |
| Product stack | Talkie, [[Hailuo]], [[MiniMax M3]] |
| Current capital-market signal | Proposed RMB-share issue and [[STAR Market]] listing announced May 31, 2026; not yet submitted or approved |

## Evolution

| Date | Event | Read-through |
|------|-------|--------------|
| January 9, 2026 | HKEX trading began under 0100.HK | MiniMax became a public proxy for [[China]]'s foundation-model lab cohort |
| February 2026 | M2.5 gained [[OpenRouter]] token-volume and coding-benchmark mindshare | Cost/performance became the MiniMax public-equity narrative |
| May 31, 2026 | Board approved preliminary RMB-share / [[STAR Market]] exploration | Mainland capital access became part of the story |
| June 1, 2026 | [[MiniMax M3]] released | Model catalyst arrived one trading session after the STAR proposal |

## Hong Kong listing and STAR Market route

MiniMax listed its Class A ordinary shares on the [[Hong Kong]] Stock Exchange on January 9, 2026 under stock code 0100. The listing made it one of the clearest public-market proxies for [[China]]'s independent foundation-model labs.

On May 31, 2026, MiniMax announced that its board had approved a preliminary proposal to explore issuing RMB-denominated shares and listing those shares on the [[STAR Market]]. The announcement is deliberately early-stage: MiniMax said it had engaged professional advisers and entered a tutoring agreement, but the concrete plan, expected timing, shareholder approvals, and regulatory approvals were still outstanding.

The read-through is capital-market architecture, not completed financing. A STAR Market route would turn MiniMax from a Hong Kong AI IPO story into a dual-market AI funding story: offshore HK shares for international capital plus possible RMB shares for mainland investors and policy-aligned tech capital.

## M3 model (June 2026)

[[MiniMax M3]] was released on June 1, 2026. MiniMax describes it as an open-weight frontier model for coding, agentic work, long context, and native multimodality. The headline architecture claim is MiniMax Sparse Attention, which MiniMax says supports a 1M-token context window; its model page says the API has a guaranteed minimum context of 512K tokens.

MiniMax's benchmark comparisons should stay attributed to the company until independent evaluations catch up. The important vault signal is still real: Chinese model labs are using long-context efficiency and API cost/performance as a public-market narrative, not just a developer benchmark narrative.

## M2.5 (Feb 2026)

![[openrouter-leaderboard-feb2026.jpg]]
*[[OpenRouter]] leaderboard, Feb 2026. MiniMax M2.5 #1 by token volume (3.07T, +524%).*

![[minimax-m25-swebench-comparison.jpg]]
*MiniMax M2.5 vs [[Claude Opus]] 4.5/4.6, [[Gemini]] 3 Pro, [[GPT]]-5.2 across coding benchmarks.*

| [[Benchmark]] | M2.5 | [[Claude Opus]] 4.6 | [[GPT]]-5.2 | [[Gemini]] 3 Pro |
|-----------|------|-----------------|---------|--------------|
| [[SWE-Bench]] Verified | 80.2 | 80.8 | 80 | 78 |
| [[SWE-Bench]] Pro | 55.4 | 55.4 | 55.6 | 54.1 |
| Terminal Bench 2 | 51.7 | 55.1 | 54 | 54 |
| Multi-[[SWE-Bench]] | 51.3 | 50.3 | - | 42.7 |
| [[SWE-Bench]] Multilingual | 74.1 | 77.8 | 72 | 65 |
| VIBE-Pro (AVG) | 54.2 | 55.6 | - | 36.9 |

Essentially tied with Western frontier models on coding benchmarks. Key differentiator: speed. Fireworks serves M2.5 at 273 tokens/sec — 2.5x the next provider.

![[minimax-m25-speed-benchmarks.jpg]]
*MiniMax M2.5 output speed by provider. Fireworks at 273 tok/s, 2.5x faster than #2.*

## Token volume dominance

M2.5 leads [[OpenRouter]] with 3.07T tokens processed — 5x [[Anthropic]]'s [[Claude Opus]] 4.6 (617B). Combined with [[Moonshot AI]]'s [[Kimi]] K2.5 (1.16T) and [[Zhipu AI]]'s [[GLM]] 5 (1.03T), Chinese models dominate the top 3 by volume, suggesting developers are voting with their wallets on cost/performance.

## Distillation accusations (Feb 23, 2026)

[[Anthropic]] accused MiniMax of the largest distillation campaign of the three Chinese labs: 13 million exchanges with [[Claude]] via fraudulent accounts, targeting agentic coding, tool use, and orchestration. MiniMax redirected nearly half its traffic to siphon capabilities when [[Anthropic]] launched new [[Claude]] models.

Part of a broader pattern: [[OpenAI]] accused [[DeepSeek]] on Feb 12, [[Anthropic]] named [[DeepSeek]], [[Moonshot AI]], and MiniMax on Feb 23. Combined: 24,000+ fake accounts, 16M+ exchanges.

MiniMax's M2.5 benchmark performance (essentially tied with Western frontier models on coding — see above) raises the question of how much was built on distilled capabilities vs independent development.

See [[AI distillation wars (2025-2026)]] and [[Model distillation]].

---

## Related

- [[MiniMax M3]] — June 2026 long-context / multimodal model release
- [[MiniMax securities note]] — 0100.HK and proposed RMB-share / STAR Market route
- [[Hailuo]] — MiniMax's video generation product (Chinese top-tier; [[Director AI]] uses it)
- [[STAR Market]]
- [[HKEX]]
- [[China AI Tigers]]
- [[HongShan]]
- [[Neil Shen]]
- [[Moonshot AI]]
- [[Zhipu AI]]
- [[China AI Tigers]]
- [[Inference economics]]
- [[AI adoption curve]]
- [[AI Video Generation]] — concept hub
- [[AI distillation wars (2025-2026)]] — largest distillation campaign (13M exchanges with Claude)
- [[Model distillation]] — technique, accused by Anthropic (Feb 2026)
