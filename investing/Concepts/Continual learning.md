---
aliases: [online learning, lifelong learning]
---

The ability for AI to learn quickly from feedback and update its behavior — a key limitation of current LLMs.

## Why it matters for AGI

Current framing of AGI: AI that could replace any remote worker. Key gap: employees learn from feedback. If you hire a good editor and they make a mistake, they don't repeat it. LLMs don't have this ability to modify themselves quickly.

## Current approaches

**In-context learning:** Provide extensive context about preferences, past interactions. Models "learn" by having more information, not by updating weights.

**LoRA adapters:** Small weight matrices overlaid on base model. Learn less but forget less. Can customize per-user but expensive at scale.

**Periodic retraining:** GPT-5 → 5.1 → 5.2. Curated updates based on community feedback. Not personalized.

## The economic problem

Updating weights for each user is prohibitively expensive. Would only be feasible with on-device compute where cost is on consumer (Apple's approach).

## Alternative view

Maybe models don't need weight updates — just better context. If models are smart enough with sufficient context about your preferences, it has the "appearance" of learning fast without actually modifying weights.

## Cursor's approach

[[Cursor]] updates Composer model weights every 90 minutes based on real-world user feedback. Closest thing to production continual learning happening today.

## Related

- [[Inference-time scaling]] — alternative path (smarter models need less learning)
- [[Cursor]] — implementing real-world weight updates
- [[AGI]] — continual learning as key gap
