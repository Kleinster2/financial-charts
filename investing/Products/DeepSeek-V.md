---
aliases:
  - DeepSeek-V
  - DeepSeek-V3
  - DeepSeek-V2
  - DeepSeek V3
tags:
  - product
  - ai
  - china
parent_actor: "[[DeepSeek]]"
parent_concept: "[[Frontier models]]"
---

# DeepSeek-V

[[DeepSeek]]'s general-purpose model family. MoE architecture. Known for training efficiency. V3 triggered early tremors before [[DeepSeek-R]] crashed markets.

## Quick stats (V3)

| Metric | Value |
|--------|-------|
| Parameters | 671B total, 37B active |
| Architecture | Mixture of Experts (MoE) |
| Training compute | 2048 H800s (~2M GPU hours) |
| Claimed cost | ~$6M (final run only) |
| Context | 128K tokens |
| Release | December 2024 |

---

## Version history

| Version | Release | Key changes |
|---------|---------|-------------|
| DeepSeek LLM | Nov 2023 | Initial 7B/67B dense models |
| DeepSeek-Coder | Jan 2024 | Code-specialized |
| DeepSeek-VL | Mar 2024 | Vision-language |
| **DeepSeek-V2** | May 2024 | MoE architecture, efficiency breakthrough |
| DeepSeek-V2.5 | Sep 2024 | Unified chat + code |
| **DeepSeek-V3** | Dec 2024 | 671B params, $6M training claim |

---

## V3 architecture

| Component | Details |
|-----------|---------|
| MoE layers | Mixture of Experts routing |
| Active params | 37B per forward pass |
| Total params | 671B across all experts |
| Efficiency | ~14x fewer active params than total |

**Why it matters:** MoE enables massive capacity without massive inference cost.

---

## The $6M claim

| What it includes | What it excludes |
|------------------|------------------|
| Final training run | Prior experiments, failed runs |
| Compute only | Infrastructure, salaries, R&D |

**Real investment:** Likely $100M+ over 2+ years. Still far below US labs.

---

## Chip situation

| Question | Answer |
|----------|--------|
| What chips? | H800s ([[China]]-legal), possibly some H100s |
| How many? | 10,000-50,000 (estimates vary) |
| Gray market? | Widely suspected, unconfirmed |
| The point | Fewer/weaker chips + efficiency gains |

---

## Benchmarks

| Benchmark | V3 Performance |
|-----------|----------------|
| MMLU | Competitive with GPT-4 Turbo |
| HumanEval | Top tier coding |
| Math | Strong |

V3 was the "early warning" most of Wall Street missed before R1 crashed markets.

---

## Related

- [[DeepSeek]] — parent actor
- [[DeepSeek-R]] — reasoning model family
- [[Frontier models]] — category
- [[Chinese open models]] — category
- [[DeepSeek day]] — market event (R1, not V3)
