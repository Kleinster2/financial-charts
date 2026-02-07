---
aliases:
  - GPT
  - GPT-4
  - GPT-4o
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

## Quick stats (GPT-5.2)

| Metric | Value |
|--------|-------|
| Type | Unified multimodal + reasoning |
| Context | 128K tokens |
| Modalities | Text, vision, voice |
| Thinking modes | Instant, Auto, Thinking (Light→Heavy) |
| Release | 2025-2026 |
| Access | ChatGPT, API |

---

## Version history

### GPT series (general-purpose)

| Model | Release | Key changes |
|-------|---------|-------------|
| GPT-3.5 | Nov 2022 | ChatGPT launch model |
| GPT-3.5 Turbo | Mar 2023 | Faster, cheaper API |
| **GPT-4** | Mar 2023 | Multimodal, major reasoning leap |
| GPT-4 Turbo | Nov 2023 | 128K context, cheaper |
| GPT-4o | May 2024 | Omni — native voice, vision, speed |
| GPT-4o mini | Jul 2024 | Cheap/fast tier |
| GPT-4.1 | 2025 | Incremental improvements |
| **GPT-5** | 2025 | Unified reasoning + general, thinking modes |
| GPT-5.1 | 2025 | Refinements |
| **GPT-5.2** | 2026 | Current flagship |

### o-series (reasoning → merged into GPT-5)

| Model | Release | Key changes |
|-------|---------|-------------|
| o1-preview | Sep 2024 | First reasoning model |
| o1-mini | Sep 2024 | Faster, cheaper reasoning |
| **o1** | Dec 2024 | Full reasoning model |
| o1 Pro | Dec 2024 | Pro-tier exclusive, extended thinking |
| **o3** | Apr 2025 | Flagship reasoning |
| o3-mini | Jan 2025 | Efficient reasoning |
| o4-mini | 2026 | Latest (retiring Feb 2026) |

**Convergence:** GPT-5 unified the o-series reasoning architecture with GPT's conversational abilities. The o-series is now "thinking mode" within GPT-5.

---

## Thinking mode (formerly o-series)

GPT-5 integrated chain-of-thought reasoning as a mode toggle:

| Mode | Behavior | Access |
|------|----------|--------|
| **Instant** | No extended thinking, fast | All tiers |
| **Auto** | Router decides depth | All tiers |
| **Thinking** | Extended reasoning | Plus+ |

### Thinking levels (GPT-5.2)

| Level | Depth | Access |
|-------|-------|--------|
| Light | Snappiest | Pro only |
| Standard | Default | Plus, Business |
| Extended | Deeper reasoning | Plus, Business |
| Heavy | Maximum thinking | Pro only |

### How thinking works

| Aspect | Details |
|--------|---------|
| Thinking | Model reasons step-by-step before responding |
| Tokens | Uses "thinking tokens" not shown to user |
| Time | Takes longer but more accurate on hard problems |
| Cost | More expensive per query (API) |

---

## Benchmarks (thinking mode)

| Benchmark | o1 Performance |
|-----------|----------------|
| AIME (math) | 83.3% (vs 13.4% GPT-4o) |
| GPQA (science) | 77.3% |
| Codeforces | 89th percentile |

Thinking mode excels at math, science, coding.

---

## GPT-4 significance

| Impact | Details |
|--------|---------|
| Benchmark leap | First model to pass bar exam, medical boards |
| Multimodal | Vision understanding built-in |
| Context | 8K → 32K → 128K expansion |
| Competition | Triggered Claude 3, Gemini responses |

GPT-4 defined "frontier model" category.

---

## API pricing

| Model | Input | Output |
|-------|-------|--------|
| GPT-4o | $2.50/M | $10/M |
| GPT-4o mini | $0.15/M | $0.60/M |
| o1 | $15/M | $60/M |
| o1-mini | $3/M | $12/M |

Thinking/reasoning models significantly more expensive due to thinking tokens.

---

## Specialized variants

| Model | Purpose | Note |
|-------|---------|------|
| [[DALL-E]] | Image generation | Separate product family |
| [[Sora]] | Video generation | Separate product family |
| Whisper | Speech-to-text | — |
| TTS | Text-to-speech | — |
| Codex | Code generation | Deprecated |

---

## Model retirements (Feb 2026)

| Retiring | Replacement |
|----------|-------------|
| GPT-4o | GPT-5.2 |
| GPT-4.1 / 4.1 mini | GPT-5.2 |
| o4-mini | GPT-5.2 Thinking |
| GPT-5 Instant/Thinking | GPT-5.2 |

---

## vs DeepSeek-R

| Aspect | GPT (thinking) | [[DeepSeek-R]] |
|--------|----------------|----------------|
| Approach | Proprietary | Open weights |
| Cost | Premium | Low cost |
| Access | API/ChatGPT | Self-host, Azure |
| Performance | Top tier | Competitive |

[[DeepSeek-R|DeepSeek R1]] showed reasoning can be done efficiently, pressuring OpenAI pricing.

---

## Related

- [[OpenAI]] — parent actor
- [[ChatGPT]] — UI product
- [[Frontier models]] — category
- [[Reasoning models]] — category (thinking mode)
- [[Claude]] — competitor
- [[Gemini]] — competitor
- [[DeepSeek-R]] — reasoning competitor
