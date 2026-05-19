---
aliases: [Eric Jang AI, Eric Jang robotics, ericjang]
personal_site: https://evjang.com
book: AI Is Good for You
github: https://github.com/ericjang
tags: [actor, ai, researcher, robotics, reinforcement_learning, author]
---

# Eric Jang

AI researcher with a robotics + reinforcement-learning background. Most recently VP of AI at [[1X Technologies]] (humanoid robotics), currently on sabbatical from 1X (per a May 2026 interview); previously Senior Research Scientist at [[Google]] [[Brain]] Robotics (2016-2022). Co-inventor of the Gumbel-Softmax / Concrete distribution — a foundational categorical-reparameterisation technique used widely in modern deep-learning architectures. Author of *AI Is Good for You* (self-published; he began writing it in 2019), a book-length treatment of his views on AGI development.

Author of the May 15, 2026 [[Dwarkesh Podcast]] interview "Building AlphaGo from scratch" — the canonical articulation of the MCTS-vs-LLM-RL framework via his open-source modern AlphaGo reconstruction at [github.com/ericjang/autogo](https://github.com/ericjang/autogo). Maintains a personal blog at [evjang.com](https://evjang.com) with regular posts on AI / robotics / reinforcement-learning topics (most recent at time of writing: "As Rocks May Think," Feb 2026).

## Quick stats

| Field | Value |
|-------|-------|
| Current role | On sabbatical from [[1X Technologies]] (was VP of AI; per May 2026 interview) |
| Prior role | Senior Research Scientist, [[Google]] [[Brain]] Robotics, 2016-2022 |
| Personal site / blog | [evjang.com](https://evjang.com) |
| Book | *AI Is Good for You* (self-published, evjang.com/book/) |
| Notable research contribution | Co-inventor, Gumbel-Softmax / Concrete distribution (2016) |
| Notable May 2026 content | "Building AlphaGo from scratch" — [[Dwarkesh Podcast]] May 15 |
| Open-source artefact | [github.com/ericjang/autogo](https://github.com/ericjang/autogo) — modern AlphaGo reconstruction |
| Areas of focus | Agentic AI, embodied learning, RL training dynamics, robotics |

## Why he matters

Eric Jang is in a small set of researchers who can articulate the algorithmic primitives of pre-LLM AI (MCTS, policy gradient, value functions) clearly enough to use them as a lens on current LLM training. The May 2026 Dwarkesh interview is the canonical statement of why the AlphaGo paradigm doesn't transfer cleanly to LLM reasoning:

- "Naive policy gradient RL has to figure out which of the 100k+ tokens in your trajectory actually got you the right answer, while AlphaGo's MCTS suggests a strictly better action every single move, giving you a training target that sidesteps the credit assignment problem"
- Value functions don't work for LLMs because "there's no way to just locally evaluate and improve your next move in a way that's independent of actually solving the problem"
- The action space for LLMs is too open-ended for PUCT-style exploration: "Because language is so broad and open-ended, a discrete set of actions is not really an appropriate choice for an LLM"

His autogo reconstruction is also significant as a cost-curve demonstration: what required "a whole team of research scientists at DeepMind and millions of dollars" in 2016 can now be done for "a few thousand dollars of rented compute" in 2026.

## Robotics-side relevance

Jang's robotics background (Google Brain robotics team + earlier 1X) connects this analytical framework to the embodied-AI thread. Robotics applications are a domain where forward search and value functions plausibly transfer better than they do in language — terminal states are often decidable (the object is grasped or it isn't), action spaces are constrained, and intermediate evaluation is tractable. Watch for forward-search architectures resurfacing in robotics-AI before they do in language (inference — Jang himself doesn't explicitly stake out this prediction, but the implication is consistent with his framework).

## Related

- [[AlphaGo]] — May 2026 reconstruction subject
- [[Dwarkesh Podcast]] — May 15, 2026 interview venue
- [[Google DeepMind]] — original AlphaGo developer (Jang's discussion subject)
- [[MCTS]] — core algorithmic concept in the framework
- [[Reinforcement learning]] — broader category
- [[Generative AI]] — adjacent thread
- [[Dwarkesh Patel]] — interview host
- [[1X Technologies]] — prior humanoid-robotics affiliation
