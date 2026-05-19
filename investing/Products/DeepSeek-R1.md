---
aliases: [DeepSeek R1, R1, DeepSeek R1 model, DeepSeek-R1-Zero, R1-Zero]
tags: [product, ai, llm, reasoning, china, open_source, deepseek]
---

# DeepSeek-R1

[[DeepSeek]]'s reasoning-focused large language model, released January 20, 2025 with full open-source weights and a published technical report. The model matched [[OpenAI]] o1-level reasoning capability at a fraction of the inference cost, achieved primarily through reinforcement learning with verifiable rewards on math and code rather than process supervision via human-labelled step verifiers. The release catalysed the late-January 2025 China-AI repricing — including the historic single-day [[NVIDIA]] selloff — and reframed Western assumptions about the China-US AI capability gap.

The technical contribution that mattered most was the demonstration that reasoning capability could emerge from RL on verifiable rewards alone, without [[PRM]]-style human-labelled step supervision. DeepSeek-R1-Zero (the precursor) was trained from a base model with pure RL using rule-based rewards (math correctness, code unit tests), and exhibited self-reflective reasoning patterns ("wait, let me check this") that hadn't been deliberately trained in.

---

## Quick stats

| Field | Value |
|-------|-------|
| Developer | [[DeepSeek]] |
| Release date | January 20, 2025 |
| License | MIT (open weights) |
| Parameters | 671B (DeepSeek-R1) — Mixture-of-Experts |
| Active parameters per token | ~37B |
| Context window | 128K tokens |
| Training paradigm | RL with verifiable rewards via [[GRPO]] (Group Relative Policy Optimization) |
| Inference cost vs OpenAI o1 | ~10-30x cheaper |
| Distillation outputs | DeepSeek-R1-Distill-Qwen-{1.5B, 7B, 14B, 32B}, DeepSeek-R1-Distill-Llama-{8B, 70B} |
| Repository | [github.com/deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) |
| Successor | DeepSeek V4 (May 2026) — see #Successor — DeepSeek V4 |

## Successor — DeepSeek V4 (May 2026)

DeepSeek released V4 in May 2026 as two variants (per [[Nathan Lambert]] Interconnects #21, May 16 2026):

| Variant | Architecture | Notes |
|---------|--------------|-------|
| DeepSeek V4 Pro | 1.6T-A49B MoE | "seems to underdeliver relative to its size" per Lambert |
| DeepSeek V4 Flash | 284B-13B | Stronger performer of the pair; architectural changes for better and cheaper long-context performance |

The V4 release came in the same window as Google's [[Gemma 4]] (4B/9B/31B + 26B-A4B MoE, Apache 2.0), Moonshot AI's [[Kimi K2.6]] (long-horizon focus, "running over hours"), Xiaomi's [[MiMo V2.5-Pro]] (Apache 2.0, neck-and-neck with K2.6 and GLM-5.1), and Zai-Org's [[GLM-5.1]]. The cluster represents the largest concurrent open-model release wave since R1 itself.

### CAISI V4 assessment

The Center for AI Standards and Innovation's V4 evaluation found that "open models lag behind the American frontier, with the gap becoming wider over time" (per CAISI via Lambert, May 16 2026). Methodology: Item Response Theory across nine benchmarks; enormous Elo differences driven by weaker performance on CTF-Archive-Diamond, PortBench, and ARC-AGI-2.

Lambert's important caveat (per Interconnects May 16): the standardised CAISI / Epoch ECI setups "don't match how models are actually trained" — coding tasks evaluated using bash access rather than within harnesses like Claude Code or OpenCode that models are actually trained in. The benchmark-vs-deployment gap may be the largest source of measurement error in the open-vs-closed assessment (inference — Lambert raises this; the full framing as the dominant measurement error is mine).

The Florian-vs-Lambert disagreement on the closing gap is the cleanest articulation of the open question: Florian believes the proximity of open frontier to closed is closer than benchmarks suggest; Lambert believes closed maintains larger leads. Both acknowledge imperfect measurements.

## The market impact

DeepSeek-R1's release on January 20, 2025 triggered the largest single-day reset of AI-equity valuation in 2025 (the so-called "DeepSeek moment"):

- [[NVIDIA]] fell ~17% on January 27, 2025 — single-stock market-cap loss exceeded $590B
- Broader semiconductor selloff: [[Broadcom]] -17%, [[TSMC]] -13%, hyperscaler capex narratives questioned
- [[Hang Seng Tech Index]] rallied as China-AI narrative repriced
- [[Anthropic]] / [[OpenAI]] valuation pressure on cost-per-token comparisons

The structural read at the time was that DeepSeek's training-cost claim (~$5.6M for the precursor V3 model) represented a fundamental challenge to the hyperscaler-capex-dependent AI thesis. By mid-2025 the immediate panic faded as: (a) inference-scale economics still favoured the major labs at frontier; (b) DeepSeek's training-cost figure excluded substantial R&D and prior model investment; (c) the reasoning-RL recipe was demonstrated to be reproducible by US labs within months. But the structural repricing of US-China AI capability gap persisted.

## Algorithmic significance

DeepSeek-R1 is significant for the [[AlphaGo]] / MCTS-vs-LLM-RL framework because it demonstrated that the [[Reinforcement learning]] recipe for LLMs can work without explicit [[PRM]] training, given:

1. Verifiable terminal states (math, code, formal proof) provide unambiguous outcome rewards
2. Group Relative Policy Optimization ([[GRPO]]) — DeepSeek's policy-gradient variant — gives lower-variance training than naive [[PPO]] without requiring a separate critic network
3. Emergent self-reflection — the model learned to verify its own work mid-trajectory as an instrumental behaviour, providing implicit process supervision without explicit step labels

This is the "verifiable rewards" path through the credit-assignment problem, distinct from the PRM path. Both are dense-supervision workarounds for the limitation [[Eric Jang]] articulated (per Dwarkesh May 15, 2026); they have different strengths.

## Distillation and downstream models

DeepSeek released distilled versions of R1 into smaller base models (Qwen and Llama families). The distilled models inherit significant reasoning capability at much smaller parameter counts, accelerating downstream adoption. By mid-2025 these distilled models were widely deployed in open-source tooling, agentic frameworks, and research pipelines.

## Related

- [[DeepSeek]] — developer
- [[Reinforcement learning]] — broader category
- [[AlphaGo]] — algorithmic predecessor framework
- [[PRM]] — alternative credit-assignment approach
- [[GRPO]] — DeepSeek's RL algorithm
- [[OpenAI]] o-series — Western reasoning-RL lineage
- [[Claude Mythos]] — Anthropic's 2026 reasoning model
- [[Gemini Deep Think]] — Google's reasoning system
- [[NVIDIA]] — January 27, 2025 single-stock selloff catalyst
- [[Hang Seng Tech Index]] — counter-rallied on China-AI repricing
- [[Liang Wenfeng]] — DeepSeek CEO
- [[High-Flyer]] — DeepSeek parent quant fund

## Sources

- DeepSeek-AI. "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning." January 20, 2025
- DeepSeek-AI. "DeepSeek-V3 Technical Report." December 2024 — V3 base model with the ~$5.6M training-cost claim
- [github.com/deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) — official repository
- Eric Jang on [[Dwarkesh Podcast]], May 15, 2026 — placing R1 in the credit-assignment framework

*Created 2026-05-18.*
