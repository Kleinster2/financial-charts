---
aliases: [Kata Go, kata-go, KataGo Go engine]
tags: [product, ai, games, open_source, reinforcement_learning]
---

# KataGo

Open-source Go-playing AI engine developed primarily by David J. Wu (released 2019, paper 2020). Achieved superhuman Go play with "a 40x reduction in the compute needed to train a really strong Go bot" relative to the original [[AlphaGo]] (per [[Eric Jang]], [[Dwarkesh Podcast]] May 15, 2026). KataGo is the canonical modern Go-AI reference point used by Go practitioners and AI researchers for benchmarking, training, and reconstruction work. Its existence is the structural evidence that compute-cost for closed-domain AI capabilities falls fast once the recipe stabilises.

The May 15, 2026 [[Eric Jang]] AlphaGo reconstruction at [github.com/ericjang/autogo](https://github.com/ericjang/autogo) is built from KataGo as the modern baseline; the "few thousand dollars of rented compute" figure Eric Jang cites for modern reconstruction is downstream of KataGo's algorithmic improvements.

---

## Quick stats

| Field | Value |
|-------|-------|
| Developer | David J. Wu (primary) + open-source contributors |
| Initial release | 2019 |
| Paper | Wu, "Accelerating Self-Play Learning in Go." 2019 |
| Architecture | Policy + value networks ([[ResNet]] backbone) + [[MCTS]] |
| Training paradigm | Self-play RL, similar to [[AlphaGo Zero]] / [[AlphaZero]] |
| Compute reduction | ~40x vs original AlphaGo (per Wu 2019, cited by Eric Jang 2026) |
| Repository | [github.com/lightvector/KataGo](https://github.com/lightvector/KataGo) |
| License | MIT |
| Status | Active development; standard tool for top Go players |

## Algorithmic improvements

KataGo introduced several training optimisations over the AlphaGo Zero / AlphaZero baseline (per Wu 2019):

- Auxiliary policy targets — predicting opponent moves alongside own moves accelerates learning
- Score prediction — predicting final score margins (not just win/loss) provides denser supervision
- Improved value-network training — fewer wasted compute cycles on uninformative positions
- Position randomisation in training data — broader board-state coverage

The combination of these produced the 40x compute reduction without sacrificing playing strength.

## Why it matters

KataGo is the empirical evidence that the AlphaGo recipe is reproducible and improvable by individual researchers rather than only by institutional teams. This compression of the training-cost frontier is the data point that grounds the [[AlphaGo]] note's investment-thesis claim that compute-cost compression for AI capabilities follows a 1000-10000x trajectory over ~5-10 years once the recipe stabilises.

The Go community has largely standardised on KataGo as the analytical engine: top professional players review games against KataGo's evaluations; Go teaching tools embed it; competitive play benchmarks against it.

## Related

- [[AlphaGo]] — predecessor and reference point
- [[AlphaZero]] — sibling architecture
- [[MCTS]] — search algorithm at the core
- [[Reinforcement learning]] — broader category
- [[Eric Jang]] — May 2026 reconstruction author who cited KataGo as baseline
- [[Dwarkesh Podcast]] — May 15, 2026 interview venue

## Sources

- Wu, David J. "Accelerating Self-Play Learning in Go." 2019, [arXiv:1902.10565](https://arxiv.org/abs/1902.10565)
- Eric Jang on [[Dwarkesh Podcast]], May 15, 2026 — citing KataGo as the modern baseline + 40x compute reduction
- [github.com/lightvector/KataGo](https://github.com/lightvector/KataGo) — official repository
