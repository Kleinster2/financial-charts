---
aliases:
  - DeepSeek-V
  - DeepSeek-V3
  - DeepSeek-V2
  - DeepSeek V3
  - DeepSeek V4
  - DeepSeek-V4
  - DeepSeek V4 Pro
  - DeepSeek V4 Flash
tags:
  - product-family
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
| DeepSeek-V3 | Dec 2024 | 671B params, $6M training claim |
| DeepSeek-V4 Preview | Apr 2026 | 1M-token context, Flash/Pro tiers, domestic-chip deployment |

---

## V4 Preview (Apr 2026)

DeepSeek launched V4 Preview on Apr. 24, 2026 as the follow-through to V3/R1 rather than a clean surprise. The important change is not just model quality; it is the stack. [[CNN]] reported that [[Huawei]] is supporting DeepSeek with Supernode technology built from large [[Ascend]] 950 clusters, and [[Counterpoint Research|Counterpoint]]'s Wei Sun said V4 runs on domestic chips from Huawei and [[Cambricon Technologies]] rather than NVIDIA hardware.

Reported model structure:

| Variant | Reported size | Active parameters | Positioning |
|---------|---------------|-------------------|-------------|
| V4 Flash | 284B parameters | ~13B active | Cheaper, faster tier |
| V4 Pro | 1.6T parameters | ~49B active | Higher-capability tier; compute-constrained |

Other reported features:

| Feature | Detail |
|---------|--------|
| Context window | Up to 1M tokens |
| Architecture | MoE plus Hybrid Attention Architecture |
| Target workloads | Coding, reasoning, agentic workflows, long-document/codebase processing |
| Openness | Open-source / open-weight strategy continues |
| Relative position | Strongest among Chinese/open systems, still behind the latest [[Gemini]]-class frontier systems per CNN's summary |

### V4 pricing (Apr 24, 2026)

[[Fortune]] reported the headline output-token prices alongside US-frontier comparisons:

| Model | Output price (per 1M tokens) | Anchor |
|-------|------------------------------|--------|
| V4 Flash | $0.28 | Cheaper-tier open model |
| V4 Pro | $3.48 | Reasoning-tier open model |
| [[OpenAI]] equivalent | ~$30 | Per Fortune's framing of "equivalent usage" |
| [[Anthropic]] equivalent | ~$25 | Per Fortune's framing of "equivalent usage" |

The pricing is the structural weapon. Open weights remove the captive-API moat; aggressive token pricing on the hosted endpoint removes any remaining cost rationale for serving DeepSeek through [[OpenAI]] or [[Anthropic]] APIs in China. Inference-cost arbitrage now tilts strongly toward V4 + domestic compute for any workload where the capability gap is tolerable.

### V4 frontier-gap framing (Apr 24, 2026)

DeepSeek's own V4 tech report compared the model against [[Anthropic]]'s [[Claude]] Opus 4.6, [[OpenAI]]'s GPT-5.4, and [[Google]]'s [[Gemini]] 3.1 Pro, per Fortune. Per the report, V4 falls "marginally short of GPT-5.4 and Gemini 3.1 Pro," with a "developmental trajectory that trails state-of-the-art frontier models by approximately three to six months."

That self-assessment is more useful than the headline benchmark wins because it sets the gap in time, not score. Three to six months is the cadence at which Chinese open models can now follow US closed-frontier releases. If the cadence holds, the practical gap is the time it takes a downstream developer to validate the new model on their workload — short enough that for many enterprise and agentic workloads it is no longer load-bearing.

The product implication is that DeepSeek-V is no longer just the efficient-model family; it is becoming a hardware-software bridge for Chinese domestic AI clusters. If V4 is good enough for enterprise and government deployment, the value migrates from benchmark rank to distribution, cost, and sovereignty.

---

## V3 architecture

| Component | Details |
|-----------|---------|
| MoE layers | Mixture of Experts routing |
| Active params | 37B per forward pass |
| Total params | 671B across all experts |
| Efficiency | ~14x fewer active params than total |

Why it matters: MoE enables massive capacity without massive inference cost.

---

## The $6M claim

| What it includes | What it excludes |
|------------------|------------------|
| Final training run | Prior experiments, failed runs |
| Compute only | Infrastructure, salaries, R&D |

Real investment: Likely $100M+ over 2+ years. Still far below US labs.

See [[DeepSeek]] for chip situation and efficiency thesis (company-wide context).

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

### Cross-vault

- [Technologies: Chinese AI Stack](obsidian://open?vault=technologies&file=Chinese%20AI%20Stack) — V4 as the first credible threshold-crossing event for the alternative compute stack
