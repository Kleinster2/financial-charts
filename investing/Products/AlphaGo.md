---
aliases: [Alpha Go, AlphaZero, Alpha Zero, AlphaGo Zero, AlphaGo Master, MuZero, AlphaGo system]
tags: [product, ai, reinforcement_learning, deep_learning, mcts, games, deepmind]
---

# AlphaGo

[[Google DeepMind]]'s Go-playing AI system, which defeated [[Lee Sedol]] 4-1 in March 2016 — the first program to beat a professional Go player at full strength without handicap. Move 37 in Game 2 became an iconic moment of AI creativity: an unconventional shoulder hit that no human would play, which turned out to be a winning move. The system architecture (deep neural networks + Monte Carlo Tree Search) became the foundation of a successor family — [[AlphaGo Zero]] (2017), [[AlphaZero]] (2017), and [[MuZero]] (2019) — that generalised the approach to chess, shogi, and arbitrary environments with progressively less human input.

The system's deeper relevance for the 2026 AI investment thread is not Go itself but the algorithmic comparison it offers to current [[LLM]] reinforcement-learning approaches. [[Eric Jang]] articulated this in a May 15, 2026 [[Dwarkesh Podcast]] interview built around his reconstruction of AlphaGo from scratch using modern tools: AlphaGo's MCTS-driven search "sidesteps the credit assignment problem" that hobbles naive policy-gradient RL on long-trajectory LLM training (per Eric Jang, Dwarkesh May 15). That comparison is the canonical case for why forward search hasn't transferred cleanly from games to reasoning — and a forecast about whether it ever will.

[[Jakub Pachocki]] (OpenAI) cites AlphaGo as the precedent for AI models discovering novel strategies, comparing [[FrontierMath]] solutions to watching AlphaGo "play interesting games indefinitely" — positioning it as the historical anchor for OpenAI's o-series and frontier-reasoning lineage.

---

## Synopsis

AlphaGo solved a problem long considered the canonical AI moonshot: Go is computationally intractable for brute-force search (~10^170 board positions, ~250 legal moves per turn vs ~35 for chess) and lacks the linear-tactical structure that made chess yield to engines. The breakthrough was combining two innovations: deep convolutional neural networks trained on expert games (supervised) and self-play (reinforcement), and Monte Carlo Tree Search guided by those networks. Neither component alone was sufficient; the integration was.

The succession demonstrated that the system could be progressively de-coupled from human knowledge:

- AlphaGo Fan (Oct 2015) — beat European champion Fan Hui 5-0, first major milestone
- AlphaGo Lee (Mar 2016) — beat Lee Sedol 4-1, the cultural moment
- AlphaGo Master (Jan 2017) — beat 60 top human players online, then world champion Ke Jie 3-0 in May
- AlphaGo Zero (Oct 2017) — trained from scratch with no human game data, surpassed all prior AlphaGo versions in 40 days
- AlphaZero (Dec 2017) — generalised to chess and shogi using the same architecture
- MuZero (Nov 2019) — learned the environment's dynamics rather than receiving them, enabling application to Atari and beyond

By [[KataGo]] (2020), open-source implementations had achieved "a 40x reduction in the compute needed to train a really strong Go bot" (per Eric Jang, Dwarkesh May 15) — putting Go-superhuman AI in reach of individual researchers rather than institutional teams. This compression of the training-cost frontier from "millions of dollars and a team of research scientists" to "a few thousand dollars of rented compute" (per Eric Jang) is structurally important: it shows what the AI cost curve does for closed-domain games over a decade, and offers a lower bound on what to expect for reasoning systems once the recipe stabilises (inference).

---

## Architecture

The AlphaGo system has three components that combine into a single decision-making loop (per Eric Jang, Dwarkesh May 15; DeepMind 2016 Nature paper).

### Policy network

A convolutional neural network that takes the current board state as input and outputs a probability distribution over legal moves (roughly 361 possible positions on a 19x19 board, minus already-occupied squares). The policy network is the "intuition" component: it predicts what a strong player would consider playing without doing any search.

In the original AlphaGo, the policy network was trained in two phases:

1. Supervised learning on ~30M positions from KGS amateur dan-level games — gives the network the prior of expert-level move preference
2. Reinforcement learning via self-play — refines the network by playing against earlier versions of itself, updating weights based on game outcomes

AlphaGo Zero (2017) eliminated phase 1 entirely and trained the policy network from scratch via self-play, reaching superhuman performance in 40 days.

### Value network

A second convolutional neural network that takes a board state as input and outputs a scalar estimate of win probability (range 0-1). The value network is the "evaluation" component: it estimates how good a position is without rolling out any sequence of moves.

The value network and policy network share a [[ResNet]] backbone with two output heads. Eric Jang's observation: "ResNets still outperform transformers" in low-data regimes for Go due to local convolution inductive biases, though transformers excel when "you want more global context" (per Eric Jang, Dwarkesh May 15). The Go-specific structure — local tactical patterns, board symmetries, position-specific shape considerations — fits the convolutional prior.

### Monte Carlo Tree Search ([[MCTS]])

The decision-making loop. From the current board state, MCTS builds a search tree of possible future positions, biased by the policy and value networks:

1. Selection — at each node, choose the next move using PUCT (Predictor + UCT) — a formula that balances exploration (visit unfamiliar moves) against exploitation (visit moves the policy network thinks are good). The PUCT exploration bonus is √N/(1+N_a), where N is total visits to the parent and N_a is visits to that action
2. Expansion — when reaching an unexplored node, evaluate it with both networks
3. Simulation / rollout — play out from this node using the policy network to bias the moves (in the original AlphaGo; AlphaGo Zero eliminated the rollout step)
4. Backpropagation — update visit counts and value estimates along the path from root to leaf, biasing the next iteration

After running MCTS for some computational budget (originally minutes per move, later seconds), the algorithm chooses the move with the highest visit count from the root.

The structural property that makes MCTS powerful in Go: it converts the noisy single-network estimate into a much sharper signal by averaging across hundreds or thousands of search rollouts. This is the property Eric Jang highlights as the algorithmic insight that does not transfer cleanly to LLMs.

---

## The MCTS-vs-LLM-RL framework

This is the framework Eric Jang articulates in the May 15, 2026 [[Dwarkesh Podcast]] interview, built around his AlphaGo reconstruction at [[github.com/ericjang/autogo](https://github.com/ericjang/autogo)]. It is the most actionable framework AlphaGo offers for understanding 2026 LLM training dynamics (inference — the framework synthesis is mine; Eric Jang articulates the comparison but the "framework" framing pulls his points into a more structured form).

### The credit-assignment problem

In any RL setup, the training algorithm needs to figure out which actions in a sequence of decisions deserve credit for the final outcome. This is the credit-assignment problem.

For LLM reinforcement learning (the o-series / RLVR / RLHF lineage), the trajectory is the full token sequence the model produces. As Eric Jang puts it: "Naive policy gradient RL has to figure out which of the 100k+ tokens in your trajectory actually got you the right answer" (per Eric Jang, Dwarkesh May 15). The training signal is sparse — typically a single reward at the end of the trajectory — and the assignment problem is severe.

For AlphaGo, MCTS sidesteps this entirely: "AlphaGo's MCTS suggests a strictly better action every single move, giving you a training target that sidesteps the credit assignment problem" (per Eric Jang, Dwarkesh May 15). Each move's MCTS distribution is the supervision target for the policy network — local, dense, and immediately actionable.

The contrast is structural, not just quantitative:

| Dimension | AlphaGo / MCTS | LLM / policy gradient |
|-----------|----------------|------------------------|
| Action space | Discrete (~361 moves) | Discrete but enormous (~100k+ tokens) |
| Trajectory length | Hundreds of moves | Hundreds-of-thousands of tokens |
| Terminal-state value | Decidable (game outcome) | Often non-decidable (was the reasoning correct?) |
| Per-move supervision | MCTS distribution = local target | None — only end-of-trajectory reward |
| Credit assignment | Sidestepped by local search | Sparse and severe |

### Why forward search doesn't transfer

Multiple research efforts have tried to apply tree-search structures to LLM reasoning. The general result, in Eric Jang's framing: "the jury is still out as to whether this can ever work" (per Eric Jang, Dwarkesh May 15). Three specific reasons forward search breaks down in language:

1. Value functions don't work: "There's no way to just locally evaluate and improve your next move in a way that's independent of actually solving the problem" (per Eric Jang). In Go, you can evaluate a board position. In a math proof, you cannot evaluate an intermediate step without knowing whether it leads to a valid proof
2. PUCT breaks down on continuous-ish action spaces: the exploration bonus assumes you will revisit similar states. In language, the action space is so broad that effective state revisitation is rare. "Because language is so broad and open-ended, a discrete set of actions is not really an appropriate choice for an LLM" (per Eric Jang)
3. Terminal states are not decidable: in Go, the game has a definite winner. In reasoning, "correct" is often a judgment call (per Eric Jang)

### The "human learning" parallel

Eric Jang argues that human learning is closer to the MCTS local-improvement pattern than to trajectory-level credit assignment: humans get feedback move-by-move (parents correcting, teachers correcting, errors during practice), not just at the end of long sequences (per Eric Jang, Dwarkesh May 15). If true, this implies LLM training architectures that more closely mimic dense local supervision should outperform pure outcome-based RL — which is part of the rationale behind process-supervision approaches like [[PRM]] (Process Reward Models) and step-by-step verifier training (inference — the connection to PRM/step verifiers is mine, not Eric Jang's explicit framing).

### What this means for the AI investment thread

The framework offers concrete predictions for 2026-2028 LLM training dynamics (inference — these are my readings of where the framework cuts on investing questions):

- RL-on-LLMs scaling is fundamentally harder than the Go-to-AlphaZero curve. The compute requirements to brute-force the credit-assignment problem are very large, and most of the "scaling" gains are about working around it rather than solving it
- Process supervision approaches (verifier-step labels, PRM training) should outperform pure outcome RL on compute-equivalent budgets — and the firms investing in this infrastructure ([[Scale AI]], [[Surge]], academic groups, the major labs' verification teams) should be structurally well-positioned
- Forward search will likely resurface for narrow domains where intermediate states are decidable (theorem proving, code with unit tests, formal-verification settings) but is unlikely to be the dominant training paradigm for general reasoning. "I wouldn't rule out that this stuff could come back" (per Eric Jang) but the current bet is on dense supervision rather than search
- The compute frontier compression visible in KataGo (40x reduction by 2020) suggests that whatever recipe stabilises for LLM reasoning will see similar order-of-magnitude reductions over a few years — implying the cost of reasoning-trained model capability falls fast once the training recipe is mature

---

## Eric Jang's reconstruction

The May 15 Dwarkesh interview is built around Eric Jang's open-source AlphaGo reconstruction at [github.com/ericjang/autogo](https://github.com/ericjang/autogo). The reconstruction is structurally interesting for three reasons (per Eric Jang, Dwarkesh May 15):

1. Cost compression: "What took a whole team of research scientists at DeepMind and millions of dollars...can now be done for a few thousand dollars of rented compute" — 1,000-10,000x cost reduction over a decade
2. LLM as coding co-pilot: "[[Claude]] 4.6 wrote" reasonable MCTS data structures when asked — the implementation was tractable in a way it wouldn't have been pre-2024
3. Reference point: built from KataGo (2020) as the modern Go-AI baseline, which already represented a "40x reduction in the compute needed to train a really strong Go bot" vs the original AlphaGo

The reconstruction is a concrete demonstration of the cost curve narrative. It's also a pedagogical artefact — Eric Jang positions the reconstruction as a way to teach modern AI engineers what RL actually looks like at the algorithmic level, before LLMs and the credit-assignment workarounds papered over the underlying problem.

---

## Synthesis

AlphaGo's most enduring contribution is not the Go capability itself but the algorithmic vocabulary it gave the AI field. The four-tuple of (policy network + value network + search + self-play) became the canonical decomposition that every subsequent reasoning-RL system has either implemented, replaced, or worked around. The 2026 frontier-reasoning lineage (o-series, [[DeepSeek-R1]], [[Claude Mythos]], [[Gemini Deep Think]]) all sit somewhere in the space defined by these four primitives — even when they choose to ignore one of them.

The framework's predictive utility (inference) for 2026-2028:

- Forward search will not become the dominant LLM training paradigm. The credit-assignment problem in language is qualitatively different from the one in board games, and PUCT-style exploration breaks down on the LLM action space (per Eric Jang). Bet against firms whose investment thesis depends on tree-search-for-LLMs being the breakthrough.
- Process supervision will compound as the dominant approach. Dense local-supervision signals (verifier scores, step-by-step rewards, PRMs) sidestep the credit-assignment problem more efficiently than search does. The firms building the data and labeling infrastructure for this — [[Scale AI]], [[Surge]], [[Snorkel AI]], possibly [[Mercor]] — sit in a structurally favourable position regardless of which lab wins the model layer (inference).
- Compute-cost compression will continue. The 1,000-10,000x reduction visible in Go training over the decade is a lower bound for what to expect on reasoning once the recipe stabilises. This is bullish for downstream applications (which can afford reasoning models) and bearish for any business model that depends on inference cost being a moat (inference — applies to most current LLM application-layer pricing).
- The AlphaGo-to-AlphaZero generalisation pattern (eliminate human input, generalise to other games) probably has an LLM analogue: eliminate human-labelled reasoning data, generalise to multiple domains. Whether this happens in 2026-2027 or later determines how durable the current data-moat advantages are (inference — this is the most speculative implication).

The investing read: AlphaGo as historical artefact tells you the trajectory; AlphaGo as algorithmic framework tells you why current LLM RL is harder than the analogy suggests; AlphaGo as cost-curve evidence tells you what the endgame looks like once the recipe stabilises.

---

## Quick stats

| Field | Value |
|-------|-------|
| Developer | [[Google DeepMind]] |
| First major milestone | Defeated Fan Hui 5-0, October 2015 |
| Cultural milestone | Defeated [[Lee Sedol]] 4-1, March 2016 |
| Architecture | Policy network + value network + [[MCTS]], ResNet backbone |
| Training paradigm | Supervised pretraining + RL self-play (original); pure self-play (AlphaGo Zero) |
| Iconic moment | Move 37, Game 2 vs Lee Sedol |
| Successor family | AlphaGo Zero (2017) → AlphaZero (2017) → MuZero (2019) |
| Modern baseline | [[KataGo]] (2020) — 40x compute reduction |
| 2026 reconstruction | [[Eric Jang]] / autogo (May 2026) — ~$thousands of compute |

---

## Related

- [[Google DeepMind]] — developer
- [[Google]] — parent company
- [[Demis Hassabis]] — DeepMind CEO + co-founder
- [[Lee Sedol]] — Korean Go champion defeated by AlphaGo Lee
- [[Eric Jang]] — author of May 2026 AlphaGo reconstruction + MCTS-vs-LLM-RL framework
- [[Dwarkesh Podcast]] — May 15, 2026 interview venue
- [[KataGo]] — open-source modern successor used as Eric Jang's reference
- [[MCTS]] — search algorithm at the heart of the system
- [[Reinforcement learning]] — broader category
- [[Generative AI]] — adjacent thread (LLMs as the reasoning-RL successor case)
- [[FrontierMath]] — benchmark where [[Jakub Pachocki]] drew the AlphaGo analogy
- [[Jakub Pachocki]] — OpenAI chief scientist; cites AlphaGo as novelty-discovery precedent
- [[ResNet]] — neural-network architecture backbone
- [[PRM]] — process reward models, the credit-assignment workaround in LLM RL
- [[DeepSeek-R1]] — 2026 frontier-reasoning model trained with RL on verifiable tasks

---

## Sources

- Silver et al. "Mastering the game of Go with deep neural networks and tree search." *Nature* 529, 484-489 (2016) — the original AlphaGo Nature paper
- Silver et al. "Mastering the game of Go without human knowledge." *Nature* 550, 354-359 (2017) — AlphaGo Zero
- Silver et al. "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play." *Science* 362(6419), 1140-1144 (2018) — AlphaZero
- Schrittwieser et al. "Mastering Atari, Go, chess and shogi by planning with a learned model." *Nature* 588, 604-609 (2020) — MuZero
- Wu, "Accelerating Self-Play Learning in Go." 2019 — KataGo
- [Eric Jang on Dwarkesh Podcast: "Eric Jang: Building AlphaGo from scratch"](https://www.dwarkesh.com/p/eric-jang), May 15, 2026 — MCTS-vs-LLM-RL framework + reconstruction
- [Eric Jang's autogo repository](https://github.com/ericjang/autogo) — open-source modern reconstruction
- [[Jakub Pachocki]] commentary on FrontierMath / AlphaGo novelty parallel (sourced in his actor note)

*Last updated 2026-05-18 (significant expansion from April 10 stub).*
