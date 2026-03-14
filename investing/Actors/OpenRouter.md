---
aliases: [OpenRouter]
tags: [actor, ai, infrastructure, startup]
---

#actor #ai #infrastructure #startup

**OpenRouter** — unified API gateway routing to 500+ AI models from multiple providers ([[OpenAI]], [[Google]], [[Anthropic]], [[Meta]], [[Mistral]], [[DeepSeek]], etc.) through a single API key. The "Stripe for AI inference."

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 2023 |
| Valuation | $500M (Series A, Apr 2025) |
| Total raised | $40M (Seed + Series A) |
| Seed | [[a16z]] led |
| Series A | [[Menlo Ventures]] led ($28M, Apr 2025) |
| Models | 500+ |
| Legal counsel | Orrick |

---

## What it does

Single API endpoint that routes requests to the best available model/provider based on price, latency, and availability. Key features:
- **Model routing** — automatic fallback if a provider is down or rate-limited
- **Price optimization** — compare costs across providers for the same model
- **BYOK (Bring Your Own Key)** — use your own API keys for direct billing, or pay through OpenRouter
- **Web search plugin** — append `:online` to model slug for web-augmented responses (via Exa.ai)
- **Multimodal** — images, audio, PDFs across supported models

---

## Business model

Takes a margin on API calls routed through the platform. Free tier available with limits. Enterprise pricing with volume discounts. BYOK option for developers who want routing without markup.

---

## State of AI: 100 trillion token study (Jan 2026)

OpenRouter published the most comprehensive empirical dataset on global AI inference consumption, analyzing 100T+ tokens across 300+ models from 60+ providers. Co-published with [[a16z]]. Key findings:

### Country-level token consumption

| Rank | Country | Share |
|------|---------|-------|
| 1 | US | 47.17% |
| 2 | [[Singapore]] | 9.21% |
| 3 | [[Germany]] | 7.51% |
| 4 | [[China]] | 6.01% |
| 5 | [[South Korea]] | 2.88% |
| 6 | Netherlands | 2.65% |
| 7 | [[United Kingdom]] | 2.52% |
| 8 | Canada | 1.90% |
| 9 | [[Japan]] | 1.77% |
| 10 | [[India]] | 1.62% |

Continental: North America 47.22%, Asia 28.61%, Europe 21.32%, South America 1.21%, Oceania 1.18%, Africa 0.46%.

Asia's share doubled from ~13% (early 2024) to ~31% (late 2025).

Caveats: billing-address-based geography. Enterprise accounts may aggregate across regions. China's domestic inference (via [[DeepSeek]], [[Qwen]], [[Baidu]]) largely untracked here — most never touches Western routers.

### Model ecosystem

| Model family | Tokens (Nov 2024-Nov 2025) | Origin |
|-------------|----------------------------|--------|
| [[DeepSeek]] | 14.37T | China |
| [[Qwen]] ([[Alibaba]]) | 5.59T | China |
| [[Llama]] ([[Meta]]) | 3.96T | US |
| [[Mistral]] | 2.92T | France |
| [[OpenAI]] | 1.65T | US |

Proprietary models ~70% of total tokens. Open-source ~30%, of which Chinese OSS averages ~13% (spiking to 30% some weeks on new model drops).

### Usage patterns

- Reasoning models crossed 50% of all token usage by late 2025
- Programming grew from ~11% of tokens (early 2025) to 50%+ by late 2025
- Simplified Chinese: ~5% of token volume (2nd language after English at 82.87%)
- 50%+ of usage originates outside the US

*Source: [OpenRouter State of AI 2025](https://openrouter.ai/state-of-ai), [a16z analysis](https://a16z.com/state-of-ai/), [arXiv paper](https://arxiv.org/html/2601.10088v1)*

---

## Strategic significance

OpenRouter sits at the **inference routing layer** — a chokepoint between developers and model providers. As models commoditize, the routing/optimization layer captures value. Similar dynamics to payment processing ([[Stripe]]) or cloud load balancing.

**Bull case:** Model proliferation makes single-provider lock-in risky. Developers want optionality. OpenRouter becomes the default middleware.

**Bear case:** Model providers can offer multi-model access directly (e.g., [[Amazon]] Bedrock, [[Google]] Vertex AI). Thin margin business if providers compete on routing.

---

## Related

- [[AI extensibility]] — infrastructure layer play
- [[Anthropic]] — model provider (Claude available via OpenRouter)
- [[OpenAI]] — model provider
- [[Google]] — model provider + competitor (Vertex AI)
- [[Amazon]] — competitor (Bedrock)
- [[Menlo Ventures]] — Series A lead (also early [[Anthropic]] investor)
- [[a16z]] — Seed lead
- [[Model lab economics]] — routing layer context
- [[Inference economics]] — uses OpenRouter data for country-level consumption analysis
- [[Sovereign AI race]] — OpenRouter data is best proxy for national AI consumption

*Source: Sacra, Orrick (Jun 2025)*
*Created 2026-02-18*
