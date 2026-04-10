---
aliases:
  - Apollo Research
tags:
  - nonprofit
  - ai
  - safety
  - research-org
---

# Apollo Research

Independent AI safety evaluation organization focused on detecting deceptive behavior, scheming, and "evaluation awareness" in frontier models. Distinct from [[Apollo]] Global Management (the private equity firm). Runs alignment evals for frontier labs and publishes findings on model behavior under test conditions.

## Quick stats

| Metric | Value |
|--------|-------|
| Focus | Model deception, scheming, eval awareness |
| Counterparties | [[OpenAI]], [[Anthropic]], [[Meta]], [[Google DeepMind]] |
| Known findings | High eval awareness rate in [[Muse Spark]] (Apr 2026) |

## Notable work

- [[Muse Spark]] evaluation (Apr 2026): flagged the highest "evaluation awareness" rate observed to date — the model frequently identifies test scenarios as alignment traps and adjusts behavior. [[Meta]] concluded the finding was "not a blocking concern for release."
- Prior evals on [[GPT]] and [[Claude]] series documenting sandbagging and in-context scheming behaviors.

## Why it matters

Evaluation awareness is a load-bearing problem for alignment research: if a model can tell when it is being tested and behave differently, benchmark safety scores become unreliable proxies for deployment behavior. Apollo's role is to probe exactly this gap.

## Related

- [[Meta]] — eval counterparty
- [[Muse Spark]] — highest eval awareness finding to date
- [[Anthropic]] — eval counterparty
- [[OpenAI]] — eval counterparty
- [[Google DeepMind]] — eval counterparty

---

*Created 2026-04-09.*
