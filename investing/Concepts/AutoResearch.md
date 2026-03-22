---
aliases: [auto research, autonomous research, AI research automation]
---
#concept #ai #research #automation

**AutoResearch** — AI agents autonomously running experiments, evaluating results against objective metrics, and iterating without human involvement. Coined and demonstrated by [[Andrej Karpathy]] (March 2026) on his GPT-2 training codebase.

---

## Synthesis

AutoResearch represents the logical endpoint of the agent revolution applied to AI development itself: remove the human researcher as bottleneck, maximize autonomous token throughput, let agents iterate against verifiable metrics. Karpathy's proof of concept found optimizations a two-decade veteran missed overnight. The immediate implication is that frontier labs' research pipelines are ripe for automation — and their researchers know it. The deeper implication is that the "untrusted compute" variant (distributed auto research via internet swarms) could democratize AI improvement in ways that undermine the frontier lab moat. The constraint: only works where metrics are objective and evaluation is cheap. Anything "soft" — taste, judgment, creativity — remains outside the loop.

---

## How it works

The agent:
1. Reads the training code (`train.py`)
2. Hypothesizes an improvement
3. Edits the code
4. Runs a short experiment (~5 minutes)
5. Evaluates against validation loss
6. If improvement: commits via git. If not: resets.
7. Repeats indefinitely.

A 2-day run on Karpathy's datachat project made ~700 autonomous changes, found ~20 additive improvements, and cut time-to-GPT-2 by 11%. Critically, the agent found oversights that Karpathy — after two decades of ML research and extensive manual tuning — had missed: weight decay on value embeddings, under-tuned Adam betas, and joint interactions between parameters.

*(Source: Karpathy GitHub, No Priors podcast Mar 20 2026)*

---

## Key constraint: verifiable metrics

> "If you can't evaluate, you can't auto research it." — [[Andrej Karpathy]] (No Priors, Mar 20 2026)

AutoResearch is "extremely well suited to anything that has objective metrics that are easy to evaluate": CUDA kernel optimization, training hyperparameters, architecture search. Anything without clean metrics — design taste, UX quality, creative writing — falls outside the paradigm.

The same constraint applies to RL-trained models: verifiable domains improve rapidly, everything else stagnates (the "atoms joke" problem — [[ChatGPT]] still tells the same joke from 3-4 years ago).

---

## Meta-optimization: program.md

The instructions to the auto researcher are written in a `program.md` file — Karpathy's "crappy attempt at describing how the auto researcher should work." Different program.mds produce different research outcomes. This opens a meta-layer:

- Different program.mds = different research organizations (more risk-taking vs. conservative, fewer standups vs. more)
- You can evaluate which program.md produces the most improvement for the same hardware
- You can give that evaluation data to a model and ask it to write a better program.md
- "There's no way we don't get something better"

Contest idea (floated on the podcast): let people write different program.mds for the same hardware budget, measure improvement, then feed all results to a model to synthesize the optimal approach.

---

## Distributed auto research (SETI@home for AI)

*(Source: No Priors podcast, Mar 20 2026)*

Karpathy's most speculative but structurally interesting extension: an untrusted pool of internet workers collaborating to improve LLMs, analogous to [[Folding@home]] or SETI@home.

The core insight: AI improvement is expensive to discover but cheap to verify. Someone might try 10,000 ideas to find one that works, but checking that a candidate commit actually improves validation loss requires only a single training run.

The proposed structure resembles a blockchain:
- Commits instead of blocks
- Proof of work = experimentation (computationally expensive search)
- Cheap verification (run one training loop to check)
- Reward = leaderboard position (no monetary reward yet)

Security challenges: running arbitrary code from untrusted internet sources. Sandboxing and verification systems required.

> "A swarm of agents on the internet could collaborate to improve LLMs and could potentially even run circles around frontier labs. Frontier labs have a huge amount of trusted compute, but the Earth is much bigger and has a huge amount of untrusted compute."

If compute becomes the thing people "contribute to the pool" (like donating money to institutions today), people could join auto research tracks for causes they care about — cancer research, materials science, climate modeling — by purchasing compute and directing it at specific problems.

---

## Application beyond LLMs

- CUDA kernel optimization — inefficient code → efficient code with identical behavior. "Perfect fit."
- Materials science — [[Periodic]] (CEO: Liam, friend of Karpathy) applying auto research to material discovery. Sensors are expensive lab equipment rather than text logs.
- Biology — similar sensor cost and experimental loop structure
- Any domain with objective metrics and automated evaluation

---

## Implications for frontier labs

Karpathy's assessment: frontier labs are employing ~1,000 researchers who are "basically glorified auto... they're automating themselves away, actively." The logical endpoint is:

1. Researchers contribute ideas to a queue (alongside an automated scientist that scans arXiv and GitHub)
2. Automated workers pull items from the queue and run experiments
3. Successful results go to a feature branch
4. Humans monitor and merge to main
5. Researchers shouldn't be "enacting" ideas — they have "way too much confidence"

Experimentation happens on small models, with scaling laws used to extrapolate. The vast majority of exploration is cheap; only the final scaling runs require frontier compute.

---

## Related

- [[Andrej Karpathy]] — creator, demonstrated on datachat/GPT-2 training
- [[NanoChat]] — the training codebase that AutoResearch optimizes
- [[Agentic AI]] — AutoResearch is agents applied to research itself
- [[Jevons Paradox]] — cheaper research → more research, not less
- [[Open source commoditization]] — distributed auto research could democratize AI improvement
- [[OpenAI]] — frontier lab whose research pipeline this automates
- [[Anthropic]] — same
- [[Periodic]] — materials science auto research (Karpathy connection)

### Cross-vault
- [Technologies: Open LLM Training](obsidian://open?vault=technologies&file=Open%20LLM%20Training) — technical deep dive on the training pipeline AutoResearch optimizes
