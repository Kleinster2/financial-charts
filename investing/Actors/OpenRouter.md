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

*Source: Sacra, Orrick (Jun 2025)*
*Created 2026-02-18*
