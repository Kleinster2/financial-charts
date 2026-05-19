---
aliases: [RL, reinforcement learning, deep RL, deep reinforcement learning, RL training]
tags: [concept, ai, machine_learning, hub, framework]
---

# Reinforcement learning

The branch of machine learning in which an agent learns to make decisions by interacting with an environment, receiving rewards, and updating its policy to maximise cumulative reward over time. RL is the canonical paradigm for sequential decision-making in AI — distinct from supervised learning (which has labelled examples) and unsupervised learning (which has no rewards). The combination of deep neural networks as function approximators with RL ("deep RL") is the foundation for [[AlphaGo]], game-playing AI, robotics, and — since 2022 — the post-training of large language models via [[RLHF]] / [[RLAIF]] / process supervision.

The 2026 investment-relevant frame: RL is the algorithmic engine of the frontier-reasoning lineage ([[OpenAI]] o-series, [[DeepSeek-R1]], [[Claude Mythos]], [[Gemini Deep Think]]). Whether RL-on-LLMs continues to compound, and which workarounds for the credit-assignment problem win, determines the cost structure of reasoning capability through 2028.

---

## The framing

An RL setup has five components:

| Component | Definition | Example (AlphaGo) | Example (LLM RLHF) |
|-----------|------------|-------------------|---------------------|
| Agent | The thing that takes actions | Neural network producing moves | LLM producing tokens |
| Environment | What the agent acts on | Go board + opponent | User prompt + judging system |
| State | The current situation | Board position | Conversation context + partial response |
| Action | What the agent chooses | A move | A token (or sequence) |
| Reward | The signal that drives learning | Win/loss at end of game | Human/model judgment on the response |

The training objective is to find a policy (state → action distribution) that maximises expected cumulative reward.

---

## Key algorithmic families

### Policy-gradient methods

Directly parameterise the policy and use gradient ascent on expected reward. Examples: [[REINFORCE]], [[PPO]], [[GRPO]] ([[DeepSeek]]'s variant used in R1). Strength: works with continuous and high-dimensional action spaces. Weakness: high variance; the credit-assignment problem is severe for long trajectories. "Naive policy gradient RL has to figure out which of the 100k+ tokens in your trajectory actually got you the right answer" (per [[Eric Jang]], Dwarkesh May 15, 2026).

### Value-based methods

Learn a value function (state → expected future reward) and act greedily with respect to it. Examples: Q-learning, [[DQN]], double DQN. Strength: sample-efficient when value function is well-conditioned. Weakness: doesn't extend cleanly to continuous actions; struggles when intermediate-state evaluation is hard (a key constraint for LLM reasoning, see [[AlphaGo]] MCTS-vs-LLM-RL framework).

### Actor-critic methods

Combine a policy network ("actor") with a value network ("critic"). Examples: A2C, A3C, SAC, [[PPO]] (also classified here). Strength: balances policy gradient and value-based stability.

### Search + RL hybrid (AlphaGo template)

Pair a policy network and value network with [[MCTS]] to convert noisy single-network estimates into a sharper supervision signal. Sidesteps the credit-assignment problem but requires the four preconditions to hold (see [[MCTS]] and [[AlphaGo]]).

### Process supervision

Train per-step verifiers (process reward models, [[PRM]]) rather than only end-of-trajectory rewards. Provides dense local supervision that approximates the per-move targets MCTS gives in games, without requiring MCTS's preconditions. Dominant approach for LLM reasoning in 2026.

---

## RL for LLMs — 2022 to 2026 timeline

| Phase | Approach | Notes |
|-------|----------|-------|
| Pre-2022 | Supervised fine-tuning only | LLM post-training was straightforward fine-tuning |
| Late 2022 | [[RLHF]] (Reinforcement Learning from Human Feedback) | InstructGPT + ChatGPT release; PPO on pairwise preference rewards |
| 2023 | [[RLAIF]] (RL from AI Feedback) — [[Anthropic]]'s [[Constitutional AI]] | Replace human feedback with AI-generated feedback at scale |
| 2024 | [[DPO]] (Direct Preference Optimization) — Stanford | Eliminate explicit reward model; train directly on pairwise preferences |
| Late 2024 | Reasoning-RL — [[OpenAI]] o1 release | RL on verifiable tasks (math, code) for reasoning capability |
| 2025 | [[GRPO]] — [[DeepSeek-R1]] release | Lighter-weight policy-gradient variant; January 2025 release was the China-AI inflection |
| 2026 | Process supervision dominant + RL-with-verifiable-rewards | [[PRM]] training + step-by-step verifier signals |

The 2024-2026 shift is from "RL on human preferences" (RLHF style) to "RL on verifiable correctness" (math, code, formal proof). The latter dodges the reward-hacking problems of preference RL by grounding the reward in something that can be machine-verified.

---

## Why RL is harder for LLMs than for games (the May 2026 [[AlphaGo]] framework)

Per [[Eric Jang]] (Dwarkesh May 15, 2026), three structural reasons (see [[AlphaGo]] for the full framework):

1. Action spaces in language are vast and effectively continuous (~100k+ tokens) — too large for [[PUCT]]-style exploration
2. Intermediate-state evaluation in reasoning is generally not independent of solving the full problem — value functions don't have local meaning
3. Terminal states in reasoning are often not decidable — "correct" is a judgment call

The implication: forward search is unlikely to be the dominant LLM RL paradigm. Process supervision, RL with verifiable rewards, and dense local supervision should compound faster.

---

## Investment-thread implications

Three structural reads (inference):

1. RL infrastructure firms (verifier data, step-labelled traces, formal proof datasets) sit in a structurally favourable position regardless of which model lab wins. Candidates: [[Scale AI]], [[Surge]], [[Snorkel AI]], [[Mercor]]
2. Compute-cost compression for reasoning-trained models will follow the AlphaGo trajectory (1000-10000x reduction over ~5 years). This implies application-layer pricing power based on inference cost is short-lived
3. The lab that figures out reasoning-RL recipe efficiency first compounds fastest — small algorithmic differences compound exponentially in self-play-style training. Watch [[Anthropic]], [[OpenAI]], [[DeepMind]], and [[DeepSeek]] for recipe shifts

---

## Related

- [[AlphaGo]] — canonical search+RL application
- [[MCTS]] — companion search algorithm
- [[PRM]] — process reward models for credit-assignment workaround
- [[RLHF]] — preference-based RL for LLM alignment
- [[RLAIF]] — AI-feedback variant
- [[Constitutional AI]] — [[Anthropic]]'s RLAIF framework
- [[DPO]] — direct preference optimisation
- [[GRPO]] — DeepSeek's policy-gradient variant
- [[DeepSeek-R1]] — January 2025 reasoning-RL inflection
- [[Eric Jang]] — May 2026 RL framework articulator
- [[Generative AI]] — broader hub
- [[Reinforcement learning for locomotion]] — narrow robotics-side application

---

## Sources

- Sutton + Barto. *Reinforcement Learning: An Introduction* (2nd ed, 2018) — canonical textbook
- Schulman et al. "Proximal Policy Optimization." 2017 — PPO
- Ouyang et al. "Training language models to follow instructions with human feedback." 2022 — InstructGPT / RLHF
- Bai et al. "Constitutional AI." 2022 — Anthropic RLAIF
- Rafailov et al. "Direct Preference Optimization." 2023 — DPO
- DeepSeek-AI. "DeepSeek-R1." January 2025 — GRPO + verifiable rewards
- Eric Jang on [[Dwarkesh Podcast]], May 15, 2026 — MCTS-vs-LLM-RL framework
