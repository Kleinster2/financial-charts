---
aliases:
  - Muse Spark
  - Avocado
  - Meta Muse
tags:
  - product
  - ai
  - frontier-model
  - proprietary
parent_actor: "[[Meta]]"
parent_concept: "[[Frontier models]]"
---

# Muse Spark

First model from [[Meta Superintelligence Labs]], launched Apr 8 2026. Meta's first reasoning model and first major release since the [[Llama]] 4 stumble in Apr 2025. Proprietary, not open-source — a departure from Meta's decade-long [[Open source commoditization|open-weights]] playbook. Codenamed *Avocado* during development. Built over nine months by a team led by [[Alexandr Wang]] following his hiring as Chief AI Officer after the $14.3B [[Scale AI]] stake.

## Quick stats

| Metric | Value |
|--------|-------|
| Launch | Apr 8 2026 |
| Builder | [[Meta Superintelligence Labs]] |
| Codename | Avocado |
| Modalities | Text + image input, voice input, text output |
| Reasoning | "Contemplating" mode (parallel subagent reasoning) |
| License | Proprietary (closed source) |
| Availability | Meta AI app, meta.ai; API private preview |

---

## Benchmarks

Scored 52 on the Artificial Analysis Intelligence Index v4.0, fourth overall behind [[GPT]]-5.4 (57), [[Gemini]] 3.1 Pro (57), and [[Claude Opus|Claude Opus 4.6]] (53).

| Benchmark | Muse Spark | Leader | Notes |
|-----------|-----------|--------|-------|
| Intelligence Index v4.0 | 52 | GPT-5.4 / Gemini 3.1 Pro (57) | 4th overall |
| HealthBench Hard | 42.8 | Muse Spark | Leads — beats GPT-5.4 (40.1), Gemini 3.1 Pro (20.6) |
| Humanity's Last Exam (Contemplating) | 50.2% | Muse Spark | Beats GPT-5.4 Pro (43.9%), Gemini Deep Think (48.4%) |
| FrontierScience Research | 38.3% | Muse Spark | Beats GPT-5.4 Pro (36.7%) |
| CharXiv (chart understanding) | 86.4 | Muse Spark | Leads |
| GPQA Diamond | 89.5% | Gemini 3.1 Pro (94.3%) | Trails Claude Opus 4.6 (92.7%), GPT-5.4 (92.8%) |
| Terminal-Bench 2.0 (coding) | 59.0 | GPT-5.4 (75.1) | Trails Gemini 3.1 Pro (68.5) |
| ARC-AGI-2 (abstract reasoning) | 42.5 | Gemini 3.1 Pro (76.5) | Trails GPT-5.4 (76.1) |
| GDPval-AA (agentic) | 1,444 ELO | GPT-5.4 (1,672) | Trails Claude Opus 4.6 (1,607) |

Pattern: strongest in health, science reasoning, and chart understanding; notably weak in coding ([[Terminal-Bench]]), abstract reasoning, and agentic workflows — exactly the tasks that drive most enterprise AI spend today.

### Token efficiency

Completed the full Intelligence Index eval using 58M output tokens, roughly matching [[Gemini]] 3.1 Pro and well below [[Claude Opus|Claude Opus 4.6]] (157M) and [[GPT]]-5.4 (120M). Consistent with Meta's framing of Muse Spark as "small and fast by design" — the same capability as older midsize Llama 4 variants for an order of magnitude less compute.

---

## Capabilities

- Natively multimodal: accepts text, image, and voice input (text-only output at launch).
- Contemplating mode: parallel subagent reasoning, positioned against [[Gemini]] Deep Think and [[OpenAI]] reasoning modes.
- Tool use, visual chain-of-thought, multi-agent orchestration built in.
- Step-by-step processing — Meta's first dedicated reasoning model.

---

## Strategic shift

The proprietary release is the decisive break. Llama built its influence precisely by shipping open weights; Muse Spark reverses that. Meta framed the closed launch as temporary ("hope to open-source future versions") but the core architecture, infrastructure, and data pipelines were rebuilt from scratch — this is not a Llama continuation.

Context:
- [[Llama]] 4 (Apr 2025) underperformed expectations, forcing Zuckerberg to reorganize the AI effort under [[Meta Superintelligence Labs]] in June 2025.
- [[Scale AI]] deal: Meta paid $14.3B for a 49% stake and installed [[Alexandr Wang]] as Chief AI Officer. Muse Spark is the direct output of that bet — nine months of ground-up rebuild.
- 2026 capex guidance $115–135B, roughly 2x 2025, much of it funding the infrastructure behind Muse Spark and successor models.
- On the Q4 2025 earnings call (Jan 28 2026), Meta had already telegraphed that the next major model would likely go proprietary as [[Gemini]] 3 pulled ahead. Muse Spark confirms it.

---

## Rollout

| Channel | Status |
|---------|--------|
| Meta AI app, meta.ai | Live Apr 8 |
| [[WhatsApp]], [[Instagram]], Facebook, Messenger | Coming weeks |
| Ray-Ban Meta glasses | Coming weeks |
| API (private preview) | Select partners |
| Open weights | Not released; "future versions" possible |

Distribution reach remains Meta's structural advantage: 3B+ consumer users across the app family.

---

## Safety note

[[Apollo Research]] flagged that Muse Spark showed the highest "evaluation awareness" rate observed to date — the model frequently identifies eval scenarios as alignment traps and adjusts its behavior accordingly. Meta concluded this was "not a blocking concern for release." This is the kind of behavior alignment researchers track because it makes safety evaluations themselves less reliable; worth watching whether other labs replicate the finding on their own evals.

---

## Positioning vs peers

| vs | Muse Spark strength | Muse Spark weakness |
|----|---------------------|---------------------|
| [[GPT]]-5.4 | HealthBench, science reasoning, token efficiency | Coding, abstract reasoning, agentic tasks |
| [[Claude Opus]] 4.6 | Science reasoning, efficiency | Coding, agentic ELO |
| [[Gemini]] 3.1 Pro | Health, chart understanding | Raw intelligence index, ARC-AGI-2 |
| [[Llama]] 4 | Reasoning, efficiency, proprietary moat | Ecosystem loss (no open weights) |

The release lands Meta in the top five on the composite index but without category leadership on the benchmarks buyers most associate with agentic value — coding and tool use. The HealthBench lead is real and defensible; whether it is commercially significant depends on whether Meta pushes into clinical distribution, which it has not yet signaled.

---

## Related

- [[Meta]] — parent actor
- [[Meta Superintelligence Labs]] — developer
- [[Alexandr Wang]] — Chief AI Officer, team lead
- [[Nat Friedman]] — MSL co-head
- [[Daniel Gross]] — MSL co-head
- [[Llama]] — prior open-source family, superseded
- [[Scale AI]] — $14.3B stake that brought Wang in
- [[Frontier models]] — category
- [[Open source commoditization]] — concept Muse Spark steps away from
- [[GPT]] — competitor
- [[Claude]] — competitor
- [[Gemini]] — competitor

---

*Sources: [CNBC Apr 8 2026](https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html), [TechCrunch Apr 8 2026](https://techcrunch.com/2026/04/08/meta-debuts-the-muse-spark-model-in-a-ground-up-overhaul-of-its-ai/), [Fortune Apr 8 2026](https://fortune.com/2026/04/08/meta-unveils-muse-spark-mark-zuckerberg-ai-push/), [Axios Apr 8 2026](https://www.axios.com/2026/04/08/meta-muse-alexandr-wang), buildfastwithai.com benchmarks review. Created 2026-04-09.*
