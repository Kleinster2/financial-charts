---
aliases:
  - GPT
  - GPT-4
  - GPT-4o
  - GPT-4.5
  - OpenAI GPT-4.5
  - GPT-5
  - GPT-5.2
  - GPT-3.5
  - o
  - o1
  - o3
  - o-series
  - OpenAI o
tags:
  - product-family
  - ai
parent_actor: "[[OpenAI]]"
parent_concept: "[[Frontier models]]"
---

# GPT

[[OpenAI]]'s model family. Powers [[ChatGPT]]. GPT-4 (2023) established frontier model category. GPT-5 unified general-purpose and reasoning capabilities — the o-series is now "thinking mode."

## Quick stats (GPT-5.4)

| Metric | Value |
|--------|-------|
| Type | Unified multimodal + reasoning + agentic |
| Context | 1M tokens (GPT-5.4); 400K (GPT-5/5.2); 128K (GPT-4 era) |
| Modalities | Text, vision, voice |
| Thinking modes | Instant, Auto, Thinking (Light→Heavy) |
| Current flagship | [[OpenAI GPT-5.4]] (Mar 5, 2026) |
| Access | ChatGPT, API, Codex |
| Parameters | Not disclosed. Leaked estimates: GPT-4 ~1.76T (8x220B MoE); GPT-4.5 est. 4-5T |
| ChatGPT market share | 68% (Jan 2026, down from 87% Jan 2025) |

---

## Version history

### GPT series (general-purpose)

| Model | Release | Key changes |
|-------|---------|-------------|
| GPT-3.5 | Nov 2022 | ChatGPT launch model |
| GPT-3.5 Turbo | Mar 2023 | Faster, cheaper API |
| GPT-4 | Mar 2023 | Multimodal, major reasoning leap |
| GPT-4 Turbo | Nov 2023 | 128K context, cheaper |
| GPT-4o | May 2024 | Omni — native voice, vision, speed |
| GPT-4o mini | Jul 2024 | Cheap/fast tier |
| GPT-4.1 | 2025 | Incremental improvements |
| GPT-4.5 | Feb 2025 | Research preview, "Orion." Incremental over GPT-4o, lower hallucinations. Deprecated Jul 2025 after GPT-5 release |
| GPT-5 | Aug 2025 | Unified reasoning + general, thinking modes. First $1B revenue month (Jul 2025) |
| GPT-5.1 | 2025 | Refinements |
| GPT-5.2 | Dec 2025 | Codex backbone |
| GPT-5.3 Instant | Early Mar 2026 | Fast tier |
| [[OpenAI GPT-5.4]] | Mar 5, 2026 | Current flagship. Agentic: native computer use, tool calling. See standalone note for benchmarks |

### o-series (reasoning → merged into GPT-5)

| Model | Release | Key changes |
|-------|---------|-------------|
| o1-preview | Sep 2024 | First reasoning model |
| o1-mini | Sep 2024 | Faster, cheaper reasoning |
| o1 | Dec 2024 | Full reasoning model |
| o1 Pro | Dec 2024 | Pro-tier exclusive, extended thinking |
| o3 | Apr 2025 | Flagship reasoning |
| o3-mini | Jan 2025 | Efficient reasoning |
| o4-mini | 2026 | Latest (retiring Feb 2026) |

**Convergence:** GPT-5 unified the o-series reasoning architecture with GPT's conversational abilities. The o-series is now "thinking mode" within GPT-5.

---

## Key releases

### GPT-3.5 / GPT-3.5 Turbo (Nov 2022 / Mar 2023)

The model that launched [[ChatGPT]] and triggered the AI arms race. Parameters not disclosed (leaked estimates ~154B, possibly MoE ~1.76T — unconfirmed). Training cutoff: Sep 2021. Context: 4K tokens (16K version added ~Jun 2023). Text-only, instruction-tuned via RLHF.

Pricing: $0.002 per 1K tokens at launch (Mar 2023) — 10x cheaper than prior GPT-3.5 models. Later cut to $0.50/$1.50 per M tokens (Jan 2025).

Adoption was unprecedented: ChatGPT reached 1M users in 5 days, 100M MAU in 2 months — fastest consumer product adoption in history, beating [[TikTok]]'s 9-month pace. ChatGPT Plus ($20/mo) launched Feb 1, 2023.

Competitive responses: [[Google]] declared internal "code red" Dec 2022. Launched Bard Feb 6, 2023. [[Microsoft]] announced Bing Chat Feb 7, 2023.

### GPT-4 (Mar 2023)

Defined the "frontier model" category. Parameters not disclosed; leaked architecture (George Hotz, Jun 2023; corroborated by Soumith Chintala/[[Meta]]): mixture of 8 x 220B parameter experts, ~1.76T total. 16 internal MoE experts with ~111B params each for MLP layers; 2 experts routed per forward pass. Training cutoff: Sep 2021 (extended to Dec 2023 in later versions). Context: 8K standard, 32K variant.

Pricing: $30/$60 per M tokens at launch. 32K variant: $60/$120.

| Benchmark | Score |
|-----------|-------|
| MMLU | 86.4% (0-shot) |
| HumanEval | 67.0% |
| Bar exam | 90th percentile (OpenAI claim; independent analysis ~69th percentile, ~48th on essays) |
| SAT EBRW | 93rd percentile |
| SAT Math | 89th percentile |
| AIME | 1.8/15 (12.5%) |

First model to accept image inputs (text + image in, text out). Function calling added later. First to pass bar exam and medical boards (with caveats). Triggered competitive responses: [[Anthropic]] released [[Claude]] 1.0 (Mar 2023), [[Google]] upgraded Bard with PaLM 2 (May 2023).

### GPT-4 Turbo (Nov 2023)

Announced at [[OpenAI DevDay 2024|OpenAI DevDay]] (Nov 6, 2023). Same architecture as GPT-4. Training cutoff: Apr 2023. Context: 128K tokens (~300 pages) — massive expansion from 8K/32K. Preview Nov 2023; GA Apr 2024.

Pricing: $10/$30 per M tokens — 3x cheaper on input, 2x cheaper on output vs GPT-4.

Added: vision (image input), parallel function calling, JSON mode, reproducible outputs (seed parameter), improved instruction following for specific formats (XML, etc.).

Competitive responses: [[Google]] launched [[Gemini]] 1.0 (Ultra/Pro/Nano) Dec 6, 2023 — one month after. [[Anthropic]] released Claude 2.1 with 200K context in Nov 2023.

### GPT-4o (May 2024)

"Omni" — natively multimodal: real-time voice conversation, vision, text in a single model. First GPT to handle audio/voice/image as native modalities rather than through separate pipelines. 2x faster and 50% cheaper than GPT-4 Turbo. Training cutoff: Oct 2023 (later extended to Jun 2024). Context: 128K.

Pricing: $5/$15 per M tokens at launch, later cut to $2.50/$10 — a 12x reduction from GPT-4's launch price in 14 months.

| Benchmark | Score |
|-----------|-------|
| MMLU | 88.7% (vs GPT-4's 86.5%) |
| Audio speech recognition | State-of-the-art at release |
| Multilingual benchmarks | State-of-the-art at release |

Made available to free ChatGPT users — first frontier model accessible without subscription. 47% of paying users cited GPT-4o access as primary subscription reason. GPT-3.5 usage dropped 70%+ after launch. 40% increase in user retention YoY. Became the default ChatGPT model.

Competitive responses: [[Anthropic]] released Claude 3.5 Sonnet (Jun 2024), which outperformed GPT-4o on many coding benchmarks. [[Google]] released [[Gemini]] 1.5 Pro with 1M context window.

### GPT-4o mini (Jul 2024)

Dramatically smaller/cheaper than GPT-4o — designed for the cost-sensitive API tier. Training cutoff: Oct 2023. Context: 128K.

Pricing: $0.15/$0.60 per M tokens — 60% cheaper than GPT-3.5 Turbo while outperforming it on every benchmark. This killed GPT-3.5 as a product.

| Benchmark | GPT-4o mini | Gemini Flash | Claude Haiku |
|-----------|-------------|-------------|--------------|
| MMLU | 82.0% | 77.9% | 73.8% |
| HumanEval | 87.2% | 71.5% | 75.9% |
| MGSM (math) | 87.0% | 75.5% | 71.7% |
| MMMU (multimodal) | 59.4% | 56.1% | 50.2% |

Replaced GPT-3.5 Turbo as default for free ChatGPT users. Created the cheap/fast tier that powered most API usage volume.

### o1 / o1-preview / o1-mini / o1 Pro (Sep-Dec 2024)

The reasoning breakthrough. Chain-of-thought "thinking" before responding, trained via reinforcement learning. First model to use invisible "thinking tokens" — the model reasons step-by-step internally, then produces a final answer. Context: 128K input/32K output (preview); 200K (full o1).

Pricing: o1-preview $15/$60 per M tokens. o1-mini $3/$12. o1 (full, Dec 2024) $15/$60. o1 Pro available only via ChatGPT Pro ($200/mo).

| Benchmark | o1-preview | o1 (full) | vs GPT-4o |
|-----------|-----------|-----------|-----------|
| AIME (math) | 83% (12.5/15) | 78% std, 86% pro | 13% (1.8/15) |
| Codeforces | 89th %ile (Elo ~1258) | Elo 1673 | — |
| GPQA Diamond | — | 78.1% | — |
| o1-mini Codeforces | Elo 1650 | — | — |

o1-preview launched Sep 12, 2024 with severe rate limits (50 queries/week). Full o1 launched Dec 5, 2024 (Day 1 of "12 Days of OpenAI"). o1 Pro introduced as part of $200/mo ChatGPT Pro tier. o1 (full) reduced "major errors" by 34% vs o1-preview.

Triggered the reasoning model race: [[Google]] released Gemini 2.0 Flash Thinking (Dec 2024). [[DeepSeek-R|DeepSeek R1]] (Jan 2025) demonstrated comparable reasoning at dramatically lower cost — shook markets.

### o3 / o3-mini (Jan-Apr 2025)

OpenAI skipped "o2" entirely — signaling a major leap. o3-mini released Jan 31, 2025 with three reasoning effort levels (low/medium/high). o3 GA Apr 16, 2025 alongside o4-mini. Context: 200K tokens.

Pricing: o3-mini $1.10/$4.40 at launch. o3 $10/$40 at launch → 80% price cut Jun 10, 2025 to $2/$8. o3-pro $20/$80 (Jun 2025).

| Benchmark | o3 | o3-mini |
|-----------|-----|---------|
| ARC-AGI (low-compute) | 75.7-76% | — |
| ARC-AGI (high-compute, 172x) | 87.5% (surpassed 85% human threshold) | — |
| SWE-bench Verified | 71.7% (vs o1's 48.9%) | — |
| GPQA Diamond | — | 77.0% (high effort) |
| Codeforces | — | Elo 2073 (high effort) |
| ARC-AGI-2 | 3% (vs 60% avg human) | — |

The ARC-AGI-2 result (3% vs 60% human) exposed the limits of the reasoning approach — massive compute scaling doesn't generalize to genuinely novel problems. ARC Prize Foundation estimated o3 high-compute cost at $3,000-$30,000 per ARC-AGI task.

Last standalone reasoning models before merger into GPT-5.

### GPT-4.5 "Orion" (Feb 27, 2025)

OpenAI's largest model to date. Originally intended as GPT-5 (training started early 2024 as "Orion"). Parameters estimated 4-5T, potentially 20-30x larger than GPT-4o. Training cutoff: Oct 1, 2023. Context: 128K.

Pricing: $75/$150 per M tokens — 30x GPT-4o input. Absurdly expensive, drew widespread criticism.

| Benchmark | GPT-4.5 | GPT-4o | Claude 3.7 Sonnet |
|-----------|---------|--------|-------------------|
| MMLU | 89.6% | 88.7% | — |
| SimpleQA | 62.5% | 38.2% | — |
| Hallucination rate | 37.1% | 61.8% | — |
| GPQA | 71.4% | 53.6% | 78.2% |
| SWE-bench Verified | 38.0% | 30.7% | 70.0% |

Higher "EQ"/emotional intelligence, significantly reduced hallucination (best in class at release — outperformed o1 and o3-mini). But Claude 3.7 Sonnet demolished it on coding (70% vs 38% SWE-bench) and science (78% vs 71% GPQA). Research preview only — no default chain-of-thought reasoning. Review consensus: meaningful but not a giant leap — *"~20% better on specific tasks"* ([[Aaron Levie]], Axios). Outperformed GPT-4o on MMLU across all 15 tested languages.

API deprecated Apr 14, removed Jul 14 in favor of GPT-4.1. Fully deprecated with GPT-5 release (Aug 2025); retained only for Pro users under "Legacy Models." One of OpenAI's shortest-lived models.

### GPT-5 (Aug 7, 2025)

The unification moment. Merged o-series reasoning architecture with GPT's conversational abilities — reasoning became "thinking mode" rather than a separate model line. Multiple sub-models (main, mini, thinking, nano) with a router that auto-switches between fast and reasoning modes. Parameters not disclosed (estimates range 2T-10T+, likely MoE). Training cutoff: Sep 30, 2024 (main); May 31, 2024 (mini). Context: 400K input, 128K output.

Pricing: $1.25/$10 per M tokens (50% cheaper than GPT-4o input). GPT-5 Mini: $0.25/$2.

| Benchmark | GPT-5 |
|-----------|-------|
| AIME 2025 | 94.6% |
| SWE-bench | 74.9% |
| GPQA (with reasoning) | 85.7% (vs 77.8% without) |
| Hallucination reduction | 80% fewer vs predecessors |
| Factual errors | 5x fewer with gpt-5-thinking vs o3 |

Thinking mode levels: Instant (no extended thinking, fast), Auto (router decides depth), Thinking with depth levels (Light → Standard → Extended → Heavy). Light and Heavy Pro-only at extremes. Uses "thinking tokens" not shown to user.

Adoption: ChatGPT hit 700M WAU by Aug 2025, growing to 800M by Oct. OpenAI hit first $1B revenue month (Jul 2025). ARR reached $13B by August.

Competitive responses: [[Claude]] Opus 4.1 released Aug 5 — two days before GPT-5. [[Grok]] 4 Heavy achieved 100% on AIME 2025 (vs GPT-5's 94.6%). [[Gemini]] 2.5 Pro had launched earlier (Mar 2025).

### GPT-5.2 (Dec 11, 2025)

Released in response to internal "code red" after [[Google]]'s Gemini 3 Pro (Nov 18) and [[Anthropic]]'s Claude Opus 4.5 (Nov 24). Most competitive 6-week stretch in AI history. Three-tier architecture: Instant/Thinking/Pro. Training cutoff likely extends beyond GPT-5's Sep 2024. Context: 400K.

Pricing: $1.75/$14 per M tokens (40% increase over GPT-5.1).

| Benchmark | GPT-5.2 |
|-----------|---------|
| SWE-bench Verified | 80.0% (nearly matching Claude Opus 4.5's 80.9%) |
| SWE-bench Pro | 55.6% (SOTA at release) |
| ARC-AGI-2 | 52.9% Thinking, 54.2% Pro (35-point jump from GPT-5.1's 17.6%) |
| AIME 2025 | 100% (without tools) |
| Response error rate | 6.2% (down from 8.8% — 38% fewer errors) |

Codex backbone — powered the relaunched coding agent (Feb 2026, Windows+Mac). Professional knowledge work optimization tested across 44 occupations via GDP-Val benchmark.

### GPT-5.3 Instant (Mar 3, 2026)

Fast tier release. Training cutoff: Aug 31, 2025. Context: 400K. Pricing: ~$0.30/$1.20 per M tokens (cheapest GPT-5 variant).

| Benchmark | GPT-5.3 Instant |
|-----------|----------------|
| GPQA | 92.4% |
| MMLU | 90.1% |
| AIME 2025 | 100% |
| MATH | 98% |
| GSM8k | 99% |
| IFEval | 95% |
| Hallucination reduction | 26.8% fewer vs predecessor |

Notable for the "anti-cringe" tone overhaul — removed sycophantic RLHF patterns, filler phrases ("Great question!"), excessive exclamation points. Sub-second time-to-first-token latency. Became default ChatGPT model for all users, replacing GPT-5.2 Instant.

### GPT-5.4 (Mar 5, 2026)

Current flagship. First OpenAI model with 1M token context (matching [[Google]]/[[Anthropic]]). Training cutoff: Aug 31, 2025. Context: 1M tokens max (272K standard; doubles pricing above 272K). Three tiers: Instant (light), Thinking (reasoning), Pro (max compute).

Pricing: $2.50/$15 per M tokens (standard). GPT-5.4 Pro: $30/$180 (12x premium for deep-horizon reasoning).

First general-purpose AI to outperform humans on OSWorld (computer use from screenshots — navigating desktops, clicking UIs, sending emails, filling forms): 75% vs 72.4% human reference. 47% reduction in token usage via dynamic resource management.

| Benchmark | GPT-5.4 | vs |
|-----------|---------|-----|
| GDP-Val (44 occupations) | 83.0% | GPT-5.2: 70.9% |
| OSWorld (desktop computer use) | 75% | Human: 72.4% |
| GPQA Diamond (Pro) | 94.3% | — |
| SWE-bench Pro | 57.7% | — |
| Investment banking modeling | 87.3% | GPT-5.2: 68.4% |

See [[OpenAI GPT-5.4]] for additional benchmark analysis (hallucination rate, Proof Q&A regression, Frontier Math tier 4 breakthrough).

Released into a market where Claude Opus 4.6 (Feb 4, 2026) holds SWE-bench crown at 80.8% and Gemini 3.1 Pro (Feb 19, 2026) matches GPT-5.4 Pro's GPQA at 15x lower cost ($2 vs $30 input). GPT-5.4 differentiates on computer use and professional knowledge work rather than pure coding benchmarks.

---

## API pricing history

| Model | Input/M | Output/M | Date | Notes |
|-------|---------|----------|------|-------|
| GPT-3.5 Turbo | $2.00 | — | Mar 2023 | Per-token only, later $0.50/$1.50 |
| GPT-4 | $30 | $60 | Mar 2023 | 32K: $60/$120 |
| GPT-4 Turbo | $10 | $30 | Nov 2023 | 3x cheaper than GPT-4 |
| GPT-4o | $5 → $2.50 | $15 → $10 | May 2024 | Price cut within months |
| GPT-4o mini | $0.15 | $0.60 | Jul 2024 | Killed GPT-3.5 |
| GPT-4.5 | $75 | $150 | Feb 2025 | 30x GPT-4o. Drew criticism |
| o1 | $15 | $60 | Dec 2024 | Reasoning premium |
| o1-mini | $3 | $12 | Sep 2024 | — |
| o3 | $10 → $2 | $40 → $8 | Apr 2025 | 80% cut Jun 2025 |
| o3-mini | $1.10 | $4.40 | Jan 2025 | — |
| GPT-5 | $1.25 | $10 | Aug 2025 | 50% cheaper than GPT-4o input |
| GPT-5 Mini | $0.25 | $2 | Aug 2025 | — |
| GPT-5.2 | $1.75 | $14 | Dec 2025 | 40% increase over 5.1 |
| GPT-5.3 Instant | ~$0.30 | ~$1.20 | Mar 2026 | Cheapest GPT-5 variant |
| GPT-5.4 | $2.50 | $15 | Mar 2026 | Standard tier |
| GPT-5.4 Pro | $30 | $180 | Mar 2026 | 12x premium |

The arc: GPT-4 launched at $30/$60 → GPT-5 at $1.25/$10 in 28 months. 24x cheaper on input. But reasoning/Pro tiers command heavy premiums — the pricing is bifurcating between cheap fast tiers and expensive deep reasoning.

---

## Specialized variants

| Model | Purpose | Note |
|-------|---------|------|
| [[DALL-E]] | Image generation | Separate product family |
| [[Sora]] | Video generation | Separate product family |
| Whisper | Speech-to-text | — |
| TTS | Text-to-speech | — |
| Codex | Coding agent (GPT-5.2-Codex) | Relaunched Feb 2026, Windows+Mac |

---

## Model retirements (Feb-Mar 2026)

| Retiring | Replacement |
|----------|-------------|
| GPT-4o | GPT-5.2 → GPT-5.4 |
| GPT-4.1 / 4.1 mini | GPT-5.2 → GPT-5.4 |
| GPT-4.5 | Deprecated Jul 2025 |
| o4-mini | GPT-5.2 Thinking → GPT-5.4 Thinking |
| GPT-5 Instant/Thinking | GPT-5.2 → GPT-5.4 |

---

## Competitive pressure

[[DeepSeek-R|DeepSeek R1]] showed reasoning can be done efficiently with open weights at a fraction of OpenAI's cost — pressuring API pricing. [[Claude]] 3 (Mar 2024) was the first model to match GPT-4; by Claude 4.6 (Feb 2026), Anthropic leads on enterprise preference surveys. [[Gemini]] displaced ChatGPT as Apple's default AI (Jan 2026). The moat is distribution (900M+ ChatGPT users), not model quality — which is converging across labs.

---

## Related

- [[OpenAI]] — parent actor
- [[ChatGPT]] — UI product
- [[Frontier models]] — category
- [[Reasoning models]] — category (thinking mode)
- [[OpenAI GPT-5.4]] — current flagship (standalone note with benchmark analysis)
- [[Claude]] — competitor
- [[Gemini]] — competitor
- [[DeepSeek-R]] — reasoning competitor
