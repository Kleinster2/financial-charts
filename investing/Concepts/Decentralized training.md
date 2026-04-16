---
aliases:
  - Distributed training
  - Decentralized AI training
  - Distributed model training
tags:
  - concept
  - ai
  - crypto
  - infrastructure
  - depin
---

#concept #ai #crypto #infrastructure

# Decentralized training

The class of decentralized AI protocols that coordinate model *training* across untrusted GPU contributors — distinct from the larger and easier category of *inference* networks ([[Render Network]], [[Akash Network]], [[io.net]], [[Morpheus]], [[Aethir]]) that serve already-trained models. Training is the larger spend item for AI labs (most of [[Anthropic]] / [[OpenAI]] / [[Google]] AI capex goes to training, not inference) but is technically much harder to decentralize because it requires synchronized gradient updates across contributors who may be slow, dropout, or actively adversarial.

---

## Why it's harder than decentralized inference

| Dimension | Inference (easier) | Training (harder) |
|-----------|--------------------|--------------------|
| Coordination | Each query is independent — route to any provider | Each training step updates a shared model — all contributors must agree |
| Latency tolerance | Tens to hundreds of ms per query | Milliseconds matter at gradient-sync time |
| Trust | Verify by re-running query against another provider | Verify by checking gradients are honest, not adversarial |
| Bandwidth | Small (query in, completion out) | Massive (gradients are GBs per step on large models) |
| State | Stateless | Stateful — model snapshots have to stay coherent |

Inference is embarrassingly parallel; training is tightly coupled. This is the central engineering problem decentralized-training projects are betting they can solve.

---

## Active projects

| Project | Token | Chain | Approach | Status |
|---------|-------|-------|----------|--------|
| [[Nous Research]] (Psyche) | — (unlaunched) | [[Solana]] | Distributed training network for [[Hermes Agent|Hermes]] family models | Live with Oracle, Northern Data, Crusoe, Lambda, Andromeda; $1B token valuation (Paradigm, Apr 2025) |
| Gensyn | — (pre-token) | — | Verifiable distributed ML training with proof-of-learning | Private |
| Prime Intellect | PRIME | — | Decentralized training of open-source models (INTELLECT-1 launched Nov 2024 — first decentralized 10B model) | Public token, smaller market cap |

---

## Why it matters for the [[Decentralized AI landscape]]

Inference-side decentralization (Render/Akash/io.net) competes with [[AWS]] / [[CoreWeave]] on commodity GPU pricing — a real market but a price-taker market. Training-side decentralization, if it works, attacks the structural moat of the centralized frontier labs: their training-cluster capex. A working decentralized training network would let an open-source coalition train a frontier-class model without owning a Stargate-scale cluster.

The bear case is straightforward — every distributed-training experiment has so far produced models meaningfully behind centralized-cluster-trained equivalents at the same parameter count. Bandwidth and latency penalties from spreading training across geographies and trust-sets show up as model quality. Whether algorithmic improvements (low-bandwidth gradient compression, asynchronous SGD variants) close the gap is the open empirical question.

---

## Related

- [[Decentralized AI landscape]] — parent category map
- [[Nous Research]] — flagship distributed-training project (Psyche)
- [[Solana]] — host chain for Psyche
- [[Paradigm]] — funded Nous at $1B token valuation
- [[Bittensor]] — adjacent (subnet-based competitive training markets)
- [[DePIN]] — parent infrastructure category
