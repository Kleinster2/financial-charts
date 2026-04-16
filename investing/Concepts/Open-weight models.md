---
aliases:
  - Open-source models
  - Open weights
  - Open-source AI
  - Open-weight LLMs
tags:
  - concept
  - ai
  - models
  - open-source
---

#concept #ai #models #open-source

# Open-weight models

Foundation models whose weights are publicly downloadable, allowing anyone to run, fine-tune, or modify them without paying API fees or accepting vendor terms of service. Distinct from "open-source" in the strict sense — most open-weight models release weights but not training data or full reproduction recipes. The category includes [[Meta|Llama]], [[Mistral]], [[DeepSeek]], [[Qwen]] (Alibaba), Yi, and the [[Hermes Agent|Hermes]] fine-tune family from [[Nous Research]].

---

## Why this matters for the [[Decentralized AI landscape]]

The decentralized AI thesis is structurally dependent on open-weight models. [[Venice AI]] runs [[Llama]] / [[Qwen]] / [[DeepSeek]] / [[Mistral]] through [[Morpheus]] decentralized inference — without open weights there's no model to route, just a closed API. Same for [[Hermes Agent]] (uses 200+ models via [[OpenRouter]]) and [[Bittensor]] subnets (most subnet miners run open-weight bases plus their own fine-tunes).

Centralized frontier labs ([[OpenAI]], [[Anthropic]], [[Google]]) keep weights closed because the model is the moat. Open-weight providers lose that moat but gain distribution: anyone can download and run their model, which produces ecosystem effects ([[Hugging Face]] downloads, fine-tunes, derivatives) that closed models can't replicate.

---

## Capability gap vs frontier closed models

As of April 2026, top open-weight models are typically 6-18 months behind frontier closed models on benchmarks. This is the central constraint on consumer decentralized AI — [[Venice AI]] users get [[Llama]] 3.x quality, not [[Claude Opus|Claude Opus 4.6]] quality. The bet is that some material minority of users will accept that capability gap in exchange for privacy, lower cost, censorship resistance, or composability.

The gap has been narrowing. [[DeepSeek]] R1 (Jan 2025) and [[Llama]] 4 (2025) closed meaningful distance against frontier. Whether the gap continues to compress, holds steady, or widens is the central determinant of how big the open-weight-dependent stack can grow.

---

## Major open-weight families

| Family | Sponsor | Notable releases | Style |
|--------|---------|------------------|-------|
| [[Llama]] | [[Meta]] | Llama 3.1 (8B/70B/405B), Llama 4 | Permissive license, commercial use ok |
| [[Mistral]] | Mistral AI (France) | Mistral 7B, Mixtral 8x7B, Mistral Large 2 | Mix of open and commercial-license |
| [[DeepSeek]] | DeepSeek (China) | DeepSeek-V3, R1 | Strong reasoning at low parameter count |
| [[Qwen]] | [[Alibaba]] | Qwen 2.5, Qwen 3 | Strong on Chinese + multilingual |
| Yi | 01.AI | Yi-34B | Bilingual EN/ZH |
| Hermes (fine-tunes) | [[Nous Research]] | Hermes 4, DeepHermes 3, OpenHermes 2.5 | Fine-tunes on top of Llama / Mistral bases |

---

## Investability

Open-weight models themselves are not directly investable — the weights are public goods. The investable layer sits adjacent: hosting / inference services that run them ([[Together AI]], [[OpenRouter]], [[Groq]]), specialized hardware that accelerates them ([[Cerebras]], [[Etched]]), or applications built on them ([[Venice AI]], [[Hermes Agent]]). The model labs themselves capture value from compute partnerships, enterprise support contracts, or token-incentive layers ([[Nous Research]]'s Psyche).

---

## Related

- [[Decentralized AI landscape]] — primary category that depends on open weights
- [[Llama]] / [[Mistral]] / [[DeepSeek]] / [[Qwen]] — major families
- [[Hermes Agent]] — agent harness running 200+ open-weight models
- [[Venice AI]] — consumer chat using only open-weight models
- [[Nous Research]] — open-weight fine-tune lab + decentralized training network
- [[Hugging Face]] — primary distribution platform for open weights
- [[OpenRouter]] — API aggregator for open-weight models
- [[Anthropic]] / [[OpenAI]] / [[Google]] — closed-weight frontier counter-class
