---
aliases: [scaling laws, Chinchilla scaling, compute scaling]
---

Power law relationship between compute/data and model performance. The foundation of modern AI investment thesis.

## The core insight

If you log-increase compute, you get linear increase in held-out prediction accuracy. This relationship has held for 13 orders of magnitude of compute.

"It's held for 13 orders of magnitude, so why would it ever end?"

## Three axes of scaling

1. **Pre-training scaling** — bigger models, more data
2. **RL scaling** — longer reinforcement learning (RLVR)
3. **Inference-time scaling** — more tokens at test time

All three still working. Low-hanging fruit picked on RL and inference scaling in 2025.

## Pre-training economics

Not dead, just expensive. To scale pre-training implies serving a very large model to users — costs compound.

DeepSeek: ~$5M at cloud rates for pre-training. Serving to hundreds of millions of users: billions of dollars.

## The bitter lesson

Compute-intensive approaches win. "Computers will become more abundant, and the ones that get 100x out of it will win."

Even within abundant compute, better scaling law slope or offset determines winners.

## Architecture stability

Remarkable fact: GPT-2 (2019) to today, architecture is fundamentally the same. Mixture of Experts, attention variants, normalization tweaks — but still autoregressive transformer.

Progress comes from:
- Data quality and curation
- Post-training (RLHF, RLVR)
- Systems optimization (FP8, FP4, distributed training)
- Not new architectures

## 2026 compute build-out

Very large Blackwell clusters and gigawatt-scale facilities coming online. Contracts signed 2022-2023, 2-3 year lead times.

This compute will be used. Question is how: more pre-training, longer RL, or inference?

## Related

- [[RLVR]] — RL scaling axis
- [[Inference-time scaling]] — test-time scaling axis
- [[NVIDIA]] — compute provider
- [[Blackwell]] — next-gen chips
