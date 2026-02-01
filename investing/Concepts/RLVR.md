---
aliases: [Reinforcement Learning with Verifiable Rewards, RL with verifiable rewards]
---

Reinforcement Learning with Verifiable Rewards — the post-training technique that enabled reasoning models.

## How it works

Model generates answers, system grades completion for correctness, accuracy becomes reward signal for RL. Unlike [[RLHF]] where reward comes from human preferences, RLVR uses objective verification.

**Key insight:** You don't constrain how the model solves the problem — only that it arrives at the correct answer. The model learns to explain step-by-step, self-correct, and use more tokens to improve accuracy.

## Origin

Term coined by [[Allen Institute for AI]] team (including [[Nathan Lambert]]) in Tulu 3 work, before [[DeepSeek]] R1 popularized the scaling approach.

## Why it scales

RLHF has no scaling law — you can't log-increase compute for linear performance gains. RLVR does: DeepSeek showed if you increase training compute logarithmically, you get linear increase in evaluations.

This is field-defining: to do the best RLHF you don't need 10-100x more compute. To do the best RLVR, you do.

## Domains

- Math (most proven)
- Code (verifiable via execution)
- Scientific problems (expanding frontier)
- Rubrics / LLM-as-judge (more open-ended)

## The "aha moment"

DeepSeek R1 paper showed models trained with RLVR spontaneously develop self-correction: recognizing mistakes and trying again. This emerges from the reward signal alone.

## Training economics

RLVR runs are getting longer. [[Allen Institute for AI]] ran 5 days for initial release, then 3.5 more weeks for notable improvement. Time allocation to post-training approaching pre-training duration.

## Related

- [[RLHF]] — predecessor technique using human preferences
- [[DeepSeek]] — popularized RLVR scaling
- [[Inference-time scaling]] — enabled by RLVR training
- [[Allen Institute for AI]] — coined the term
