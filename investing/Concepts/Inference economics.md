#concept #ai #economics #commoditization

# Inference economics

Training gets the headlines. Inference is where the money is — or isn't.

---

## The price collapse (Dec 2025)

| Provider | Model | Input / Output per 1M tokens |
|----------|-------|------------------------------|
| [[OpenAI]] | GPT-5 | $30 / $60 |
| [[Anthropic]] | Claude Opus 4.5 | $15 / $75 |
| [[Anthropic]] | Claude Sonnet 4 | $3 / $15 |
| [[Anthropic]] | Claude Haiku 3.5 | $1 / $5 |
| **DeepSeek** | **V3.2** | **$0.27 / $1.10** |

**10-30x price gap** between frontier and open source.

---

## Why prices keep falling

1. **Open source competition** — DeepSeek, Llama, Mistral at near-zero margin
2. **Hardware efficiency** — Each generation does more per dollar
3. **Quantization** — Smaller models, less compute
4. **Inference-specific chips** — Groq LPUs, Cerebras, custom silicon
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

## Trade implications

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

## Related

- [[NVIDIA]] — player (acquired Groq $20B for inference)
- [[Groq]] — acquired (LPUs for fast inference)
- [[OpenAI]] — exposed (GPT-5 $30/$60 vs DeepSeek $0.27/$1.10)
- [[Anthropic]] — exposed (API pricing pressure)
- [[Open source commoditization]] — driver (DeepSeek, Llama, Mistral)
- [[Model lab economics]] — context (training vs inference margins)
- [[CUDA moat]] — context (NVIDIA trying to own inference)
