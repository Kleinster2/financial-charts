---
aliases: [Process Reward Model, process reward models, process reward model, PRMs, step verifier]
tags: [concept, ai, reinforcement_learning, llm, credit_assignment]
---

# PRM

Process Reward Model — a verifier that scores individual reasoning steps within an LLM's response, providing dense local supervision instead of relying only on the end-of-trajectory outcome reward. PRMs emerged in 2023-2024 as the principal workaround for the credit-assignment problem in LLM [[Reinforcement learning]] (per [[Eric Jang]], [[Dwarkesh Podcast]] May 15, 2026 — see [[AlphaGo]] for the full MCTS-vs-LLM-RL framework). By 2026 they have become the dominant approach for training frontier-reasoning models.

The structural intuition: where [[MCTS]] gives AlphaGo a "strictly better action every single move" as a supervision target, PRMs give the LLM a per-step verifier signal that plays the analogous role for chain-of-thought reasoning — without requiring the four preconditions ([[MCTS]] doesn't satisfy in language).

---

## The mechanism

A PRM is a model trained to predict the correctness of each step in a multi-step reasoning trace. During the main model's RL training, the PRM produces a score for each reasoning step; the policy gradient is computed against these step scores rather than only against the final outcome. The result is dense supervision: the model learns which intermediate moves were good, not just whether the whole trajectory succeeded.

Two main flavours of PRM training:

| Approach | Mechanism | Labour cost |
|----------|-----------|-------------|
| Human-labelled step verifiers | Annotators mark each reasoning step as correct/incorrect/partial | High — requires expert annotators for math/code/science |
| Automatic step verifiers | Rule-based or model-based scoring of step correctness (e.g., does this proof step preserve logical validity? does this code compile?) | Lower — but only works for verifiable domains |

The 2024-2026 trend is toward hybrid: bootstrap PRMs from human-labelled traces in math/code (where ground truth is verifiable), then use the bootstrapped PRMs to scale supervision to less-verifiable domains.

---

## Why PRMs work where MCTS doesn't

PRMs give the same algorithmic advantage MCTS gives in games — dense local supervision — without requiring MCTS's four preconditions ([[MCTS]] section on this):

| Precondition | MCTS in Go | PRMs in LLM reasoning |
|--------------|------------|------------------------|
| Decidable terminal states | Built-in to game | Required for training data (use verifiable domains) but not for inference |
| Bounded action space | ~250 moves | Not required — PRMs score steps that are already produced, no action-space exploration |
| Evaluable intermediate states | Built-in to game | Provided by the PRM itself |
| Useful state revisitation | Built-in to game | Not required — PRMs operate on linear traces |

The PRM essentially trades MCTS's "forward search for a better action" for "backward scoring of an action already taken." The model still has to produce candidates via its policy network, but the PRM gives a sharper learning signal than a single end-of-trajectory reward.

---

## Investment-thread implications

PRMs imply a structural shift in where AI training value accrues (inference):

1. Verifier data is the bottleneck. The firms that can produce high-quality step-labelled data — [[Scale AI]], [[Surge]], [[Mercor]], [[Snorkel AI]] — capture meaningful value regardless of which model lab wins
2. Verifiable domains (math, formal proof, code with unit tests, regulatory compliance) train much faster than open-ended reasoning. This implies the next wave of reasoning models will be strongest in these domains first
3. PRM training is the operational answer to the [[Eric Jang]] critique. Firms that lead on PRM infrastructure (currently [[Anthropic]] and [[OpenAI]] internally, plus the data-services cohort externally) compound the credit-assignment advantage

---

## Related

- [[Reinforcement learning]] — broader category
- [[AlphaGo]] — comparison framework via Eric Jang Dwarkesh interview
- [[MCTS]] — alternative credit-assignment mechanism (works in games, not language)
- [[Eric Jang]] — May 2026 framework articulator
- [[DeepSeek-R1]] — leading 2025-2026 reasoning RL model
- [[OpenAI]] o-series — 2024-2026 reasoning-RL lineage
- [[Claude Mythos]] — 2026 Anthropic reasoning model
- [[Scale AI]] — verifier data labelling
- [[Surge]] — verifier data labelling
- [[Mercor]] — expert data labelling

---

## Sources

- Lightman et al. ([[OpenAI]]). "Let's Verify Step by Step." 2023 — canonical PRM paper, introduced step-level supervision
- Uesato et al. ([[DeepMind]]). "Solving math word problems with process- and outcome-based feedback." 2022 — early process-supervision work
- DeepSeek-AI. "DeepSeek-R1." January 2025 — uses verifiable rewards rather than PRMs explicitly, but operates in the same algorithmic family
- Eric Jang on [[Dwarkesh Podcast]], May 15, 2026 — credit-assignment framing
