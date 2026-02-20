#concept #ai #economics #commoditization

# Inference economics

Training gets the headlines. Inference is where the money is — or isn't.

---

## The price collapse (Dec 2025)

| Provider | Model | Input / Output per 1M tokens |
|----------|-------|------------------------------|
| [[OpenAI]] | GPT-5 | $30 / $60 |
| [[Anthropic]] | [[Claude]] Opus 4.5 | $15 / $75 |
| [[Anthropic]] | [[Claude]] Sonnet 4 | $3 / $15 |
| [[Anthropic]] | [[Claude]] Haiku 3.5 | $1 / $5 |
| **[[DeepSeek]]** | **V3.2** | **$0.27 / $1.10** |

**10-30x price gap** between frontier and open source.

---

## Why prices keep falling

1. **Open source competition** — [[DeepSeek]], [[Llama]], [[Mistral]] at near-zero margin
2. **Hardware efficiency** — Each generation does more per dollar
3. **Quantization** — Smaller models, less compute
4. **Inference-specific chips** — Groq LPUs, [[Cerebras]], custom silicon
5. **Competition** — Too many providers, not enough differentiation

---

## Training vs inference economics

| | Training | Inference |
|---|----------|-----------|
| Cost driver | Compute (GPUs) | Compute + bandwidth |
| Frequency | Once per model | Every API call |
| Moat | Capital + talent | Scale + efficiency |
| Margin trend | High (few can do it) | **Declining** (commoditizing) |

**Insight**: Training is a moat. Inference is a commodity.

---

## The NVIDIA angle

NVIDIA acquired **Groq for $20B** (Dec 2025) — inference-specific LPU chips.

- LPUs: 10x faster, 1/10th energy for inference
- NVIDIA entering non-GPU inference market
- Defensive move against inference commoditization

See [[CUDA moat]] — NVIDIA trying to own inference layer too.

---

## [[Trade]] implications

**Bearish inference margins:**
- API providers (OpenAI, Anthropic consumer products)
- Inference-as-a-service startups
- Anyone competing on price

**Bullish:**
- Volume plays (hyperscalers can lose on inference, win on cloud)
- Hardware (chips needed regardless of margin)
- Vertical integration (inference as loss leader for other products)

---

## The endgame

Inference becomes like cloud compute — commodity pricing, winner-take-most at scale, margins compressed to infrastructure cost + small markup.

**Who survives:**
- Hyperscalers (scale + bundling)
- Self-hosted (enterprises owning their inference)
- Specialized chips (if efficiency gains continue)

**Who dies:**
- Pure-play API providers
- Premium-priced inference without differentiation

---

## True compute cost vs. API pricing (Feb 2026)

The gap between what providers *charge* and what inference *costs* is enormous. A first-principles analysis using [[DeepSeek]] R1's architecture (671B params, 37B active via MoE) on H100s at $2/hr retail rental:

### Raw compute cost per million tokens

| Phase | Tokens/hr (72× H100 cluster) | True cost / MTok |
|-------|-------------------------------|------------------|
| **Input (prefill)** | ~46.8B | **~$0.003** |
| **Output (decode)** | ~46.7M | **~$3.08** |

**The asymmetry is ~1,000×** — input processing parallelizes across all tokens simultaneously, while output generation is sequential (one token per forward pass per sequence).

### API margins

| Model | API price (input/output) | Est. true cost | **Gross margin** |
|-------|--------------------------|----------------|------------------|
| [[Claude]] Sonnet 4 | $3 / $15 per MTok | ~$0.01 / $3 | **80-95%** |
| [[Claude]] Opus 4 | $15 / $75 per MTok | ~$0.01 / $3-5 | **90%+** |

These are software-like margins, not infrastructure-like. Even if estimates are off by 3×, providers are still highly profitable on API.

*Source: [Martin Alderson analysis](https://martinalderson.com/posts/are-openai-and-anthropic-really-losing-money-on-inference/) (Aug 2025), updated with current pricing.*

### Subscription plan economics (Claude Max $200/mo)

A Reddit user reverse-engineered [[Anthropic]]'s Max 20× plan rate limits:

| Metric | Value |
|--------|-------|
| Weekly API-equivalent credits | **~$625** |
| Monthly API-equivalent credits | **~$2,679** |
| 5-hour window limit | ~$83 in API credits |
| Windows per week | ~7.5× |

But API credits ≠ actual cost. For a heavy [[Claude Code]] Max user (6 hrs/day):

| | Daily usage | Monthly cost to Anthropic |
|---|-------------|--------------------------|
| Input tokens | ~10M/day | ~$0.30 (essentially free) |
| Output tokens | ~100K/day | ~$9-10 |
| **Total** | | **~$17/month** → **11.8× markup** |

For a lighter $20/mo Pro user (~100K tokens/day, 70/30 input-output split): **actual cost ~$3/month** → 6× markup.

**The nightmare scenario**: a user maxing every rate limit window generating pure Opus output tokens could cost ~$300/month — which is why rate limits exist. But 90%+ of subscribers never come close.

*Source: [Reddit analysis](https://www.reddit.com/r/ClaudeAI/comments/1ppkhat/) (Dec 2025)*

### Why coding agents are wildly profitable

[[Claude Code]], [[Cursor]], [[GitHub Copilot]] — coding use cases have hugely asymmetric I/O. They ingest entire codebases, docs, and stack traces (cheap input) but generate small code snippets (minimal output). The cost structure is almost purpose-built for this pattern.

### Key insight

The "AI is unsustainably expensive" narrative may serve incumbent interests more than it reflects reality. At retail H100 prices, inference margins are already software-like. The real money losers are:
- **Training** (billions per frontier model run)
- **Video generation** (massive output from minimal input — inverted economics)
- **Extended thinking** (internal chain-of-thought tokens are output tokens the user never sees but Anthropic still pays for)

---

## Related

- [[NVIDIA]] — player (acquired Groq $20B for inference)
- [[Groq]] — acquired (LPUs for fast inference)
- [[OpenAI]] — exposed (GPT-5 $30/$60 vs [[DeepSeek]] $0.27/$1.10)
- [[Anthropic]] — exposed (API pricing pressure)
- [[Open source commoditization]] — driver ([[DeepSeek]], [[Llama]], [[Mistral]])
- [[Model lab economics]] — context (training vs inference margins)
- [[CUDA moat]] — context (NVIDIA trying to own inference)
