---
aliases: [test-time compute, reasoning models, thinking models]
---

Letting models generate more tokens to solve harder problems. The key unlock of 2025.

## The shift

Previously: faster responses preferred. Now: models think for seconds, minutes, or hours before responding.

[[OpenAI]] o1 introduced this publicly. Models trained with [[RLVR]] naturally learn to use more tokens — DeepSeek showed responses grow longer as training progresses.

## Why it matters

Inference-time scaling offers alternative to pre-training scaling:
- Pre-training: fixed cost, capability forever
- Inference scaling: pay per query, scales with difficulty

For simple tasks, use cheap fast model. For hard tasks, let model think longer. This is why $200/month subscriptions exist — and $2,000 tiers may come.

## Enables tool use

Extended thinking lets models try tools, see results, try again. This iterative loop is why agentic coding (Claude Code, Cursor) works. Model learns to search, run commands, check outputs.

## User experience change

"The first token used to come immediately. Now they'll go off for seconds, minutes or even hours generating hidden thoughts before giving you the first word of your answer."

## Economics

Pre-training compute is shrinking relative to inference compute. As models serve hundreds of millions of users, recurring inference costs dwarf one-time training costs.

## Related

- [[RLVR]] — training technique that enables this
- [[DeepSeek]] — R1 demonstrated scaling
- [[OpenAI]] — o1 introduced to consumers
- [[Claude]] — extended thinking feature
