---
aliases: [nanochat, nano-chat]
---
#product #ai #opensource #education

**NanoChat** — [[Andrej Karpathy]]'s full ChatGPT training pipeline in ~8,000 lines. Trains a GPT-2-class model from scratch through all six stages (tokenizer, pretraining, midtraining, SFT, RL, eval) in ~1.65 hours on a single 8xH100 node for ~$73. 48.9k GitHub stars.

---

## Quick stats

| Detail | Value |
|--------|-------|
| Creator | [[Andrej Karpathy]] |
| Lines | ~8,000 |
| Hardware | 8xH100 |
| Cost | ~$73 |
| Time | ~1.65 hours |
| GitHub stars | 48.9k |
| Stages | Tokenizer → pretraining → midtraining → SFT → RL (GRPO on GSM8K) → eval |

Down from [[OpenAI]]'s original 168 hours (99% reduction). Configurable from d12 (~180M params) to d26 (~850M). The codebase that [[AutoResearch]] optimizes.

---

## Related

- [[Andrej Karpathy]] — creator
- [[AutoResearch]] — AI agents that autonomously improve NanoChat's training code
- [[OpenAI]] — original GPT-2 training that NanoChat replicates
