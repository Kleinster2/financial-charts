---
aliases: [Monte Carlo Tree Search, Monte-Carlo Tree Search, monte carlo tree search, MCTS algorithm, MCTS search]
tags: [concept, ai, algorithm, reinforcement_learning, search, games]
---

# MCTS

Monte Carlo Tree Search — a heuristic search algorithm that builds a decision tree by simulating random rollouts and using the observed outcomes to bias subsequent search toward promising branches. Became famous as the search component of [[AlphaGo]] (2016), where it was paired with deep neural networks to guide tree exploration in a game whose ~250-branching-factor + ~10^170 state space made traditional minimax search intractable. MCTS combined with policy and value networks remains the canonical algorithmic recipe for game-playing AI through 2026.

The algorithm's structural importance for the 2026 AI thread is what it can't do — apply cleanly to LLM reasoning. [[Eric Jang]]'s May 15, 2026 Dwarkesh interview articulates the framework: MCTS provides per-move supervision that "sidesteps the credit assignment problem" of naive policy-gradient RL, but its preconditions (decidable terminal states, discrete action space small enough for PUCT exploration, evaluable intermediate states) don't hold for language. See [[AlphaGo]] for the full MCTS-vs-LLM-RL framework.

---

## The algorithm

MCTS iteratively builds a search tree where each node represents a game state and each edge an action. Each iteration has four phases (per Browne et al. 2012, the canonical MCTS survey):

| Phase | What happens | Purpose |
|-------|--------------|---------|
| Selection | From the root, traverse the tree using a selection policy (typically [[UCT]] or [[PUCT]]) until reaching an unexplored node | Balance exploration of less-visited branches vs exploitation of high-value branches |
| Expansion | Add one or more child nodes to the unexplored leaf | Grow the tree toward promising regions |
| Simulation / Rollout | From the new node, play out the game using a default policy (random or learned) until terminal state | Estimate the value of the new node empirically |
| Backpropagation | Update visit counts and value estimates for all nodes on the path from root to new node | Make the estimates progressively sharper |

After running for some computational budget, the algorithm returns the action with the highest visit count from the root.

The UCT (Upper Confidence Bounds for Trees) selection policy was the original 2006 contribution (Kocsis + Szepesvári). PUCT (Predictor + UCT) — used in AlphaGo — augments UCT with a prior probability from a neural network, biasing the exploration toward moves the network considers good. The PUCT exploration bonus is √N/(1+N_a) where N is total visits to the parent and N_a is visits to the candidate action.

---

## Why MCTS works in games but not (yet) in language

MCTS has four preconditions that hold tightly in board games and don't transfer to LLM reasoning (per [[Eric Jang]], Dwarkesh May 15, 2026):

| Precondition | Games | LLMs |
|--------------|-------|------|
| Decidable terminal states | Win/loss/draw — game ends with definite outcome | "Correct" is often a judgment call |
| Bounded action space | ~250 moves in Go, ~35 in chess | ~100k+ tokens, effectively continuous |
| Evaluable intermediate states | Position value can be estimated from board state alone | Reasoning intermediate states are usually only evaluable by running the whole reasoning chain |
| Useful state revisitation | Multiple paths reach similar positions | Language paths diverge rapidly; little useful revisitation |

These constraints mean PUCT-style exploration breaks down in language, value functions don't generalise from intermediate states, and the search cannot prune effectively. Research on tree-search-for-reasoning continues but "the jury is still out as to whether this can ever work" (per Eric Jang).

The narrow domains where MCTS-style search might transfer to LLM reasoning are those where the four preconditions partially hold: theorem proving (decidable terminal states via formal verification), code generation with unit tests (decidable terminal states), and constrained-domain reasoning tasks where intermediate states have verifiable structure.

---

## Cross-domain applications

MCTS is used in domains beyond board games:

| Domain | Application | Comment |
|--------|-------------|---------|
| Board games | [[AlphaGo]], [[AlphaZero]], [[KataGo]] | The canonical application; defined the modern formulation |
| Robotics | Motion planning under uncertainty | Bounded action spaces + simulatable physics make MCTS tractable |
| Scheduling | Operations research, job shop scheduling | Discrete action spaces with computable objectives |
| Drug discovery | Molecule generation with reward signals | Discrete action space (atom/bond additions) + evaluable intermediate states |
| Theorem proving | [[Lean]], [[Coq]] proof search | Decidable terminal states; growing 2024-2026 |
| Code synthesis with tests | Some research systems | Tests as terminal-state evaluators |

The pattern: MCTS works where the four preconditions hold; the domains where it underperforms are where they don't.

---

## Related

- [[AlphaGo]] — canonical application + MCTS-vs-LLM-RL framework
- [[Reinforcement learning]] — broader category
- [[Eric Jang]] — May 2026 framework articulator
- [[PRM]] — process reward models, an alternative credit-assignment workaround for LLM RL
- [[Lean]] — theorem-proving environment where MCTS-style search transfers
- [[KataGo]] — modern open-source Go AI; canonical MCTS+NN reference

---

## Sources

- Browne et al. "A Survey of Monte Carlo Tree Search Methods." *IEEE Transactions on Computational Intelligence and AI in Games* 4(1) 2012 — canonical algorithmic survey
- Kocsis + Szepesvári. "Bandit based Monte-Carlo Planning." *ECML* 2006 — original UCT contribution
- Silver et al. 2016 / 2017 / 2018 — AlphaGo / AlphaGo Zero / AlphaZero papers, MCTS+NN integration
- Eric Jang on [[Dwarkesh Podcast]], May 15, 2026 — MCTS-vs-LLM-RL framework
