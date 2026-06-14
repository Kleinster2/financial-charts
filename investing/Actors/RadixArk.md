---
aliases: [RadixArk AI, SGLang]
tags: [actor, ai, infrastructure, inference, private, usa]
---

#actor #ai #infrastructure #inference #private #usa

One-line read: **RadixArk** is the SGLang team's commercial company — SGLang (the RadixAttention KV-cache-reuse engine) already serves trillions of tokens a day for [[Google]], [[Microsoft]], [[NVIDIA]], [[Oracle]], and xAI — founded by ex-xAI and ex-Nvidia systems engineers and backed by Accel and [[NVIDIA]] at a $400M valuation; the bet is that managed infrastructure on SGLang plus the Miles RL framework becomes the serving standard for frontier-AI builders.

---

RadixArk is the commercial company behind SGLang, the open-source LLM inference engine created in 2023 out of the UC Berkeley / LMSYS orbit around Ion Stoica. SGLang's signature technique, RadixAttention, automatically reuses KV-cache across requests via a radix tree of shared prefixes, and the engine now processes trillions of tokens a day for [[Google]], [[Microsoft]], [[NVIDIA]], [[Oracle]], [[AMD]], [[Nebius]], LinkedIn, xAI, and Thinking Machines Lab. Founded by Ying Sheng (who built inference systems for xAI's Grok) and Banghua Zhu (ex-[[NVIDIA]]), RadixArk launched with a $100M seed at a $400M post-money valuation led by Accel with [[NVIDIA]] participating. It ships managed infrastructure on two open-source foundations — SGLang for inference and Miles for reinforcement learning — and sits in the [[Open-source inference engines]] cluster alongside [[Inferact]] (vLLM) and [[TensorMesh]] (LMCache).

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | Private |
| Founded | 2025 (SGLang project: 2023) |
| HQ | San Francisco / UC Berkeley orbit |
| Founders | Ying Sheng (ex-xAI), Banghua Zhu (ex-[[NVIDIA]]) |
| Category | Open-source inference engine (SGLang) — commercial arm |
| Latest valuation | $400M (seed, 2026) |
| Scale | SGLang serves trillions of tokens/day across hyperscalers |

---

## Leadership

- Ying Sheng — co-founder; SGLang creator (2023), previously built inference systems for xAI's Grok.
- Banghua Zhu — co-founder; AI infrastructure/modeling, ex-[[NVIDIA]].

---

## Funding history

| Round | Date | Amount | Valuation | Lead / investors |
|-------|------|--------|-----------|------------------|
| Seed | 2026 | $100M | $400M | Accel (lead); [[NVIDIA]] |

---

## How RadixArk works

The company is built on two open-source foundations: SGLang for inference and Miles for reinforcement learning. SGLang's core innovation, RadixAttention, automatically reuses the KV cache at runtime by organizing shared request prefixes in a radix tree, so repeated context (system prompts, few-shot examples, agent histories) is computed once and reused — a large win for the prefix-heavy, multi-call workloads that dominate agents and reasoning. On top of the engines, RadixArk ships managed infrastructure and tooling so developers, startups, enterprises, and research labs can run advanced AI systems with more speed, control, and performance than self-hosting the raw open-source stack.

---

## Competitive landscape

| Front | Players | Dynamic |
|-------|---------|---------|
| Open-source engine spinouts | [[Inferact]] (vLLM), [[TensorMesh]] (LMCache) | Direct peers from the same Berkeley/Stoica lineage; Inferact carries the higher mark ($800M) |
| Managed inference clouds | [[Fireworks AI]], Together AI, Baseten | Commercial serving competitors |
| Foundation-model first-party serving | [[OpenAI]], [[Anthropic]], [[Google]] | The labs serve their own models; RadixArk's pitch is neutral, high-performance serving |

---

## What to watch

- Hyperscaler dependence vs competition — SGLang already runs inside [[Google]], [[Microsoft]], [[NVIDIA]], [[Oracle]]; whether those become RadixArk customers or build around the OSS engine themselves.
- The Miles RL angle — adding a reinforcement-learning framework widens RadixArk beyond pure serving into the training-adjacent stack; execution on that is the differentiator vs [[Inferact]].
- Valuation vs [[Inferact]] — $400M vs $800M on parallel theses; whether SGLang's hyperscaler footprint closes the gap.
- Foundation-model encroachment — the shared below-the-labs risk for the whole cluster.

---

## Related

- [[Open-source inference engines]] — the cluster (SGLang's commercial arm)
- [[Inferact]] — sibling spinout (vLLM); same UC Berkeley / Ion Stoica lineage
- [[TensorMesh]] — peer (LMCache KV-caching)
- [[Fireworks AI]] — managed-inference competitor
- [[NVIDIA]] — investor and a major SGLang user
- [[Inference economics]] — the cost dynamics it drives

### Cross-vault
- [Technologies: Agentic Inference](obsidian://open?vault=technologies&file=Agentic%20Inference) — why agent inference is memory-bound and decode-heavy (the problem RadixAttention optimizes)

*Created 2026-06-13 (expanded from stub). Private company — figures from funding announcements; revenue undisclosed.*
