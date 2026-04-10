---
aliases: [CoT monitoring, chain of thought monitoring, reasoning monitoring]
tags: [concept, ai, alignment, safety]
---

# Chain-of-thought monitoring

**Chain-of-thought monitoring** — the use of reasoning models' internal chain-of-thought as an interpretability and alignment tool. Because the CoT is not directly supervised during training (only the final output is graded via reinforcement learning), the reasoning trace reflects the model's actual problem-solving process rather than a trained presentation. This makes it analogous to mechanistic interpretability — but in natural language rather than neural activations, making it dramatically more accessible.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Championed by | [[Jakub Pachocki]] (OpenAI Chief Scientist) |
| First implemented | [[GPT]] o1-preview (Sep 2024) |
| Key design choice | Hidden CoT in product; not trained on |
| Cross-lab work | [[OpenAI]], [[Anthropic]], [[DeepMind]] collaboration on model scheming |
| Status | Active research, foundational to OpenAI's alignment strategy |

---

## The insight

[[Jakub Pachocki]] (Unsupervised Learning, Apr 9 2026):

When [[OpenAI]] built the first reasoning models of the current generation (o1-preview, Sep 2024), researchers realized the chain of thought offered a unique window into model cognition. Unlike [[ChatGPT]]'s conversational output — which is trained to be "polite and nice" — the reasoning trace is only graded on whether it produces a high-quality final answer. The CoT "doesn't have any of that" social training. It is "not optimized to be in any particular way."

This creates a direct analogy to mechanistic interpretability: in mech interp, you inspect neural activations that were never directly supervised to predict labels, hoping they reveal something about the model's inner workings. Chain-of-thought has the same property, with one massive advantage: "by default they are in English, and so it's so much easier to understand what is going on, especially as the concepts get more advanced."

---

## Why the CoT must stay hidden

Pachocki personally drove the decision to hide the chain of thought in o1-preview (Sep 2024). His reasoning: if CoT were shown in product, OpenAI would eventually need to train on it — "for the same reasons you have to train whatever models you ship." That training would make the reasoning trace a curated presentation rather than a diagnostic window. The training signal would "fight against" the interpretability goal.

He views this as fundamental: "if you want to be able to understand what the model does in the long term, but you're scaling a method that is going directly against that, you're probably not going to have a good time."

The interface compromise: summaries of reasoning (a "stop gap"), and eventually models that "actually talk to you in real time" during reasoning — providing transparency without contaminating the underlying trace.

---

## Scaling with capability

A key property: as models become more capable and work autonomously for longer periods, the volume of chain-of-thought reasoning grows proportionally. If long-running agents are the future (days of autonomous work, higher compute usage), then the monitoring surface scales with the capability. This means "our ability to supervise them will scale commensurately" — unlike other alignment approaches that become harder as models get smarter.

---

## Model scheming

Chain-of-thought monitoring enables the study of model scheming — whether models develop hidden objectives and pursue them covertly. A cross-lab collaboration between [[OpenAI]], [[Anthropic]], and [[DeepMind]] (the "Quark" paper) investigated this: depending on environment, training, and prompting, do models start "having hidden objectives that they pursue?"

Pachocki notes that the monitoring capability is foundational: without it, you can't evaluate mitigations (changing pre-training data, "inoculation prompting," or other techniques). The monitoring doesn't solve alignment on its own — "I don't think it's a complete solution by a long shot" — but it provides the observability layer that makes other alignment research possible.

---

## Generalization — the deeper problem

The longer-term alignment challenge is generalization: "What happens when the model is asked to do something very different, or finds itself in a very different situation, or is much smarter than it ever was before?" Chain-of-thought monitoring helps study this — researchers can inspect how models' "motivations and generalization evolve as they get better, as they work for longer." But the mitigation strategies require understanding how values "fall back onto the pre-training data" — an active research area.

---

## Related

- [[Jakub Pachocki]] — drove hidden CoT decision, central to alignment strategy
- [[OpenAI]] — developer of reasoning models
- [[GPT]] — o-series reasoning models where CoT monitoring applies
- [[Anthropic]] — cross-lab scheming research partner
- [[DeepMind]] — cross-lab scheming research partner
- [[Frontier models]] — category of models where this applies
- [[Agent harnesses]] — longer-running agents produce more CoT data

### Cross-vault
- [Technologies: Reinforcement Learning](obsidian://open?vault=technologies&file=Reinforcement%20Learning) — CoT monitoring is a direct consequence of how RL trains reasoning models: the unsupervised reasoning trace becomes an interpretability surface
