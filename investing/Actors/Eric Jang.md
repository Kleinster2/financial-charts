---
aliases: [Eric Jang AI, Eric Jang robotics]
tags: [actor, ai, researcher, robotics, reinforcement_learning]
---

# Eric Jang

AI researcher with a robotics + reinforcement-learning background, formerly at [[Google]] [[Brain]]/Robotics, currently a research engineer working on agentic AI and embodied learning. Author of the May 15, 2026 [[Dwarkesh Podcast]] interview "Building AlphaGo from scratch" — the canonical articulation of the MCTS-vs-LLM-RL framework via his open-source modern AlphaGo reconstruction at [github.com/ericjang/autogo](https://github.com/ericjang/autogo).

## Quick stats

| Field | Value |
|-------|-------|
| Background | Robotics, reinforcement learning, AI research |
| Prior affiliations | [[Google]] [[Brain]], Google Robotics, [[1X Technologies]] (humanoid robotics) |
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
