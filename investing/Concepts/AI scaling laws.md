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

## AI R&D automation feedback loop

[[AI R&D automation]] is a separate scaling question from ordinary pre-training, RL, or inference-time scaling. The object being scaled is the research process itself: if AI systems can do enough frontier-model R&D, then AI progress depends not only on how much compute is used by the next model, but also on how much compute is used by the AI labor force improving future models.

The [[Software-only singularity]] version is the extreme case where recursive software improvement becomes self-accelerating. [[Ryan Greenblatt]]'s May 2026 framing is more useful for investing because it weakens the claim: even if the loop is subcritical and eventually fizzles, full AI R&D automation can still create a large one-time speed-up and increase the returns to marginal compute.

That makes scaling-law analysis more path-dependent. The same number of GPUs can represent more effective progress after the research loop is partially automated than before, because the GPUs support both the experiments and the AI researchers choosing and executing them.

## Related

- [[RLVR]] — RL scaling axis
- [[Inference-time scaling]] — test-time scaling axis
- [[NVIDIA]] — compute provider
- [[Blackwell]] — next-gen chips
- [[AI R&D automation]] — scaling the research loop itself
- [[Software-only singularity]] — recursive software-improvement threshold
