---
aliases: [ChatGLM, GLM-4, Z.ai GLM]
---
#product-family #ai #china

**GLM** — [[Zhipu]]'s (Z.ai) AI model family. Open source. **GLM-4.7** matches Claude Sonnet 4.5 on coding at **$3/month** (or free locally). First major model trained on **Huawei hardware only**.

---

## Why GLM matters

| Metric | Value |
|--------|-------|
| Latest model | GLM-4.7 (Dec 2025) |
| SWE-Bench Verified | **73.8%** (best open source) |
| LiveCodeBench | **84.9%** (beat Claude Sonnet 4.5) |
| Price | **$3/month** or free (open weights) |
| Parent | [[Zhipu]] (Z.ai) |
| Huawei-only | GLM-Image (Jan 2026) |

Open source + domestic chips = [[China]]'s AI independence play.

---

## GLM-4.7 (Dec 2025)

| Spec | Details |
|------|---------|
| Focus | Coding, reasoning |
| Price | $3/month or free (local) |
| License | Open source |
| Key feature | "Preserved Thinking" |

**Benchmarks:**

| [[Benchmark]] | Score | vs Competitors |
|-----------|-------|----------------|
| LiveCodeBench | **84.9%** | Beat Claude Sonnet 4.5 |
| SWE-Bench Verified | **73.8%** | Best open source |
| AIME 2025 (math) | **95.7%** | Top tier |
| Humanity's Last Exam | 42.8% | +41% vs predecessor |
| τ²-Bench (tool use) | **87.4%** | Multi-step agentic |

**Preserved Thinking:** Maintains reasoning chains across multiple turns instead of resetting. Targets biggest frustration in AI-assisted coding: constant repetition.

---

## Model evolution

| Model | Date | Params | Notes |
|-------|------|--------|-------|
| GLM-4.5 | Jul 2025 | 355B/32B active | MIT license, 128K context |
| GLM-4.6 | Sep 2025 | 355B/32B active | Apache 2.0, 200K context |
| **GLM-4.7** | Dec 2025 | — | Coding focus, $3/month |
| GLM-Image | Jan 2026 | 16B | **Huawei-only training** |

### GLM-4.6 details

| Spec | Value |
|------|-------|
| Total params | 355B |
| Active params | 32B |
| Architecture | MoE [[Transformer]] |
| Context | **200K tokens** |
| Chips | FP8 on Cambricon, [[Moore Threads]] |
| License | Apache 2.0 |

**Hardware flexibility:** Runs on 8× [[NVIDIA]] H20 chips (export-compliant).

---

## GLM-Image (Jan 2026)

**First major model trained entirely on Huawei hardware:**

| Spec | Details |
|------|---------|
| Training hardware | Huawei [[Ascend]] Atlas 800T A2 |
| Generator | 9B params (autoregressive) |
| Decoder | 7B params (diffusion, DiT) |
| Architecture | Autoregressive + diffusion hybrid |

**Significance:** Proves [[China]] can train competitive models without [[NVIDIA]]. [[Export controls]] workaround demonstrated.

---

## Pricing disruption

| Option | Cost |
|--------|------|
| GLM-4.7 API | **$3/month** |
| Open weights | **Free** |
| vs Claude Code | $200/month |
| vs GPT-4 | ~$20/month |

**98.5% cheaper** than US premium alternatives for similar coding performance.

---

## Zhipu (Z.ai) context

| Metric | Value |
|--------|-------|
| IPO | Jan 8, 2026 ([[HKEX]]) |
| Origin | Tsinghua University spinoff |
| Valuation | $3B+ |
| Rebrand | Zhipu AI → Z.ai (2025) |

See [[Zhipu]] for company details.

---

## Competitive position

| vs | GLM advantage | Disadvantage |
|----|--------------|--------------|
| Claude | **98% cheaper**, open source | Less polish, smaller community |
| [[Qwen]] | Coding focus, Huawei-trained | Less multimodal |
| [[DeepSeek]] | Coding benchmarks | Less efficiency narrative |
| GPT-4 | Price, open weights | Less brand recognition |

**Niche:** Best open-source coding model. Developers who want Claude Code capabilities without $200/month.

---

## Investment implications

**Indirect exposure:**
- [[Zhipu]] ([[HKEX]]) — parent, publicly traded as of Jan 2026
- Huawei — chip partnership (private)

**Thesis implications:**
- Open source commoditizing coding AI
- Huawei chips becoming viable for training
- [[China]] AI not dependent on [[NVIDIA]]

---

## Quick stats

| Metric | Value |
|--------|-------|
| Parent | [[Zhipu]] (Z.ai) |
| Latest | GLM-4.7 |
| Price | $3/month or free |
| SWE-Bench | 73.8% (best open source) |
| Huawei-trained | GLM-Image |

*Created 2026-01-27*

---

## Related

- [[Zhipu]] — parent company (Z.ai)
- [[DeepSeek]] — open source peer
- [[Qwen]] — open source peer ([[Alibaba]])
- [[Claude]] — premium competitor
- [[Export controls]] — Huawei training significance
- [[Huawei]] — chip partner
