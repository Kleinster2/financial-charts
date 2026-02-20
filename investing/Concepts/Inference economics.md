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

The gap between what providers *charge* and what inference *costs* is the central tension in AI economics. Everyone assumes AI inference is a money pit. The math suggests otherwise — at least for pure token generation. The losses come from elsewhere.

---

### GPU infrastructure: the cost floor

All inference runs on GPUs. The economics start here.

**H100 rental market (Feb 2026):**

| Provider type | Cost per H100/hr | Notes |
|---------------|-------------------|-------|
| Specialist (Hyperbolic, Hyperstack, Nebius) | $1.49–$1.90 | Lowest retail |
| Mid-tier (Lambda, Together.ai) | $1.85–$2.50 | Reserved capacity |
| Hyperscaler on-demand ([[AWS]], [[Google Cloud|GCP]], [[Microsoft|Azure]]) | $2.85–$6.98 | Highest retail |
| Spot/preemptible | $2.00–$2.50 | Interruptible |

H100 prices **declined 64-75% from peaks** and stabilized around $2.85-$3.50/hr for most providers. [[NVIDIA]] manufacturing cost per H100 is ~$3,320 — the markup to $25K-$40K retail reflects demand-driven margins.

**Full cluster economics:**
- Complete 8-GPU H100 server system: $200K–$400K (purchase)
- Power per H100: up to 700W under load
- Cooling/facilities upgrades: $15K–$100K depending on scale
- True operational cost for 8×H100 cluster: **$8–$15/hr** all-in (hardware, power, cooling, ops)

**Anthropic doesn't pay retail.** [[Anthropic]] runs on [[AWS]] infrastructure via a multi-billion-dollar partnership (Amazon invested $4B+ into Anthropic). They likely pay significantly below retail H100 rates, possibly 30-50% below public on-demand pricing. This is the critical unknown — Anthropic's actual negotiated rate determines whether their margins are good or amazing.

---

### First-principles cost per token

A detailed analysis by Martin Alderson models inference using [[DeepSeek]] R1's architecture (671B total params, 37B active via mixture of experts) as a proxy for frontier model economics. Setup: 72 H100s at $2/hr retail ($144/hr total), batch size 32, tensor parallelism across 8 GPUs per instance, 9 concurrent model instances.

**The input/output asymmetry:**

| Phase | How it works | Throughput (72× H100) | Cost per MTok |
|-------|-------------|----------------------|---------------|
| **Input (prefill)** | All tokens processed simultaneously in parallel. Each forward pass handles 32K tokens across the batch. Memory-bandwidth-bound. | ~46.8 billion tokens/hr | **~$0.003** |
| **Output (decode)** | Tokens generated sequentially — one token per sequence per forward pass. Memory-bandwidth-bound but 1,000× less parallel. | ~46.7 million tokens/hr | **~$3.08** |

**The asymmetry is ~1,000×.** Input processing is essentially free. Output generation has real costs. This single fact explains almost everything about AI pricing strategy.

**Why the asymmetry exists:** During prefill, a single forward pass processes ALL tokens in ALL sequences simultaneously — 32,000 tokens per pass. During decode, each forward pass produces only 32 tokens (one per sequence in the batch). Same GPU cost, 1,000× fewer tokens.

**Caveats and real-world adjustments:**
- MoE routing diversity can reduce throughput 30-50% (different tokens need different experts)
- Context length >128K shifts from memory-bound to compute-bound (attention scales quadratically), increasing costs 2-10×
- KV cache memory grows with context length and concurrent requests, limiting throughput
- These estimates assume retail H100 pricing — Anthropic/OpenAI likely pay 30-50% less

*Source: [Martin Alderson](https://martinalderson.com/posts/are-openai-and-anthropic-really-losing-money-on-inference/) (Aug 2025)*

---

### Full API pricing table vs. estimated true cost (Feb 2026)

| Model | API input / MTok | API output / MTok | Est. true input cost | Est. true output cost | **Output gross margin** |
|-------|-----------------|-------------------|---------------------|-----------------------|------------------------|
| [[Claude]] Opus 4.1 | $15 | $75 | ~$0.01 | ~$3-8 | **90-96%** |
| [[Claude]] Opus 4.5/4.6 | $5 | $25 | ~$0.01 | ~$2-5 | **80-92%** |
| [[Claude]] Sonnet 4/4.5/4.6 | $3 | $15 | ~$0.01 | ~$1-3 | **80-93%** |
| [[Claude]] Haiku 4.5 | $1 | $5 | ~$0.005 | ~$0.50-1 | **80-90%** |
| [[Claude]] Haiku 3 | $0.25 | $1.25 | ~$0.002 | ~$0.10-0.30 | **76-92%** |
| [[DeepSeek]] V3.2 | $0.27 | $1.10 | ~$0.01 | ~$0.50-1 | **9-55%** |

**Key observations:**
- [[Anthropic]] and [[OpenAI]]'s API pricing carries **80-95%+ gross margins on output tokens**
- Input token pricing is marked up 100-1,000× vs. actual cost, but input is so cheap it barely matters to total cost
- [[DeepSeek]]'s pricing is close to or below true cost at retail GPU rates — they're either subsidizing or have dramatically lower infrastructure costs (Chinese GPU/power pricing)
- Opus 4.5's pricing ($5/$25) vs. Opus 4.1 ($15/$75) represents a 67% price cut with likely similar or lower true cost — margin compression by choice to drive volume

**Prompt caching further improves margins:**
- Cache writes: 1.25× base input price (5-min) or 2× (1-hr)
- Cache reads: 0.1× base input price (90% discount)
- Heavy caching users (RAG systems, agents) pay even less in true compute while paying more on initial cache writes
- Break-even: 2 reads for 5-min cache, 8 reads for 1-hr cache

**Batch API:** 50% discount on all token prices, with 24-hour turnaround. Still profitable given the true cost structure — batching improves GPU utilization, so the discount costs Anthropic less than 50%.

---

### Anthropic's actual company-level margins

The per-token analysis suggests 80-95% gross margins, but [[Anthropic]]'s actual reported margins tell a different story:

| Metric | Value | Source |
|--------|-------|--------|
| 2025 projected gross margin (enterprise/API) | **~40%** | The Information (Jan 2026) |
| Previous internal estimate | ~50% | Revised downward |
| Target by 2028 | ~77% | Internal projections |
| 2025 cash burn | **~$5.2B** | On ~$9B ARR |

**Why the gap between per-token margins (80%+) and actual company margins (40%)?**

1. **Training costs** — frontier model training runs cost hundreds of millions to billions per run, amortized across the revenue base
2. **Idle capacity** — GPUs reserved for inference that aren't running at full utilization (the utilization equation is critical: 50%+ utilization needed to break even on 7B models, 10%+ for 13B)
3. **Third-party cloud markup** — Anthropic runs on [[AWS]]/[[Google Cloud|GCP]] infrastructure, not owned hardware. The hyperscaler takes a cut
4. **Extended thinking overhead** — thinking tokens are billed as output but the model generates far more internal tokens than visible output (see below)
5. **Safety/alignment R&D** — significant engineering spend on RLHF, constitutional AI, red-teaming
6. **Subscription subsidies** — consumer plans (Pro, Max) are priced below API-equivalent value
7. **Headcount** — ~1,500+ employees at AI-lab compensation levels

**Revenue trajectory:**
- Dec 2024: $1B ARR
- Jul 2025: $4B ARR  
- Dec 2025: $9B ARR
- Feb 2026: **$14B ARR** (10× annual growth for 3 consecutive years)
- [[Claude Code]] alone: >$2.5B ARR (from zero in ~9 months)
- Target: $20-26B ARR by end of 2026, $70B by 2028
- 500+ customers spending >$1M/year; 8 of Fortune 10 are customers

*Source: [Shanaka Anslem Perera](https://shanakaanslemperera.substack.com/p/the-growth-miracle-and-the-six-fractures) (Feb 2026), The Information (Jan 2026)*

---

### Subscription plan economics: what $200/mo actually costs Anthropic

[[Anthropic]]'s consumer subscriptions are a fascinating case study in AI unit economics, because the "value" a subscriber gets at API rates vastly exceeds their subscription fee — but the actual compute cost is a fraction of both.

**The plans (Feb 2026):**

| Plan | Price | Usage multiplier | Key features |
|------|-------|-------------------|--------------|
| Free | $0 | 1× | Basic access, rate-limited |
| Pro | $20/mo | ~5× | Priority access, all models |
| Max 5× | $100/mo | 5× Pro limits | [[Claude Code]], higher caps |
| Max 20× | $200/mo | 20× Pro limits | Maximum throughput |

**Reverse-engineering the Max 20× rate limits:**

A Reddit user ([andrew-kramer-inno](https://www.reddit.com/r/ClaudeAI/comments/1ppkhat/)) methodically tested the limits (Dec 2025):

| Metric | Value |
|--------|-------|
| 5-hour rolling window limit | ~$83 in API-equivalent credits |
| Effective Opus 4.5 output tokens per 5h window | ~3.33M |
| Weekly limit | ~$625 in API-equivalent credits |
| Weekly limit as multiple of 5h window | 7.5× (can exhaust 5h limit 7.5 times/week) |
| **Monthly API-equivalent value** | **~$2,679** |

So a Max $200/mo subscriber gets ~$2,679/mo in API-equivalent credits. Sounds like Anthropic is losing $2,479/mo per subscriber. But API prices ≠ actual cost.

**Actual cost-to-serve by user type:**

| User type | Plan | Daily token usage | Monthly compute cost | Markup |
|-----------|------|-------------------|---------------------|--------|
| Casual Pro user | $20/mo | ~50K tokens (70/30 I/O split) | **~$1.50** | **13×** |
| Heavy Pro user | $20/mo | ~100K tokens (70/30 I/O split) | **~$3** | **6.7×** |
| [[Claude Code]] developer (moderate) | $100/mo | ~2M input + 30K output/day | **~$5** | **20×** |
| [[Claude Code]] developer (heavy) | $200/mo | ~10M input + 100K output/day | **~$17** | **11.8×** |
| Max user hammering limits (worst case) | $200/mo | 25M+ output tokens/week | **~$300+** | **0.67× (loss)** |

**The subscription economics work because:**

1. **Most subscribers are casual** — the median Pro user probably costs Anthropic $1-3/mo in compute
2. **Coding agents have asymmetric I/O** — massive context input (essentially free) with small code output. [[Claude Code]]'s 10M input + 30K output per day costs almost nothing in compute
3. **Rate limits cap the whales** — the 5-hour rolling window and weekly cap specifically prevent users from generating unlimited output tokens
4. **The "API-equivalent value" is marketing** — comparing subscription value to API prices is misleading because API prices have 80-95% margins built in. The real comparison is subscription price vs. compute cost
5. **Classic insurance model** — you pay for the *option* of high usage, most people don't exercise it fully

*Source: [Reddit analysis](https://www.reddit.com/r/ClaudeAI/comments/1ppkhat/) (Dec 2025), [Martin Alderson](https://martinalderson.com/posts/are-openai-and-anthropic-really-losing-money-on-inference/) (Aug 2025)*

---

### Extended thinking: the hidden cost multiplier

Extended thinking (chain-of-thought reasoning) is one of the most impactful — and most expensive — features in modern AI. **Thinking tokens are billed as output tokens** on the API, but their cost implications for subscription plans are enormous.

**How it works:** When extended thinking is enabled, [[Claude]] generates internal reasoning blocks before producing visible output. The model "thinks through" the problem step-by-step. These thinking tokens are invisible to the user but are real output tokens that consume the same GPU resources.

**Pricing (API):**
- Thinking tokens charged at standard output rates ($25/MTok for Opus 4.5, $15/MTok for Sonnet 4.5, $5/MTok for Haiku 4.5)
- Minimum budget: 1,024 tokens
- Typical thinking usage: 2,000–50,000+ tokens depending on task complexity

**Example — complex coding task on Sonnet 4.5:**
- Standard mode: 50K output tokens = $0.75
- Extended thinking: 8K thinking + 50K output = $0.87 (16% premium)
- But for hard reasoning tasks, thinking can be 100K+ tokens — doubling or tripling the cost

**Why this matters for subscriptions:** A Max subscriber using extended thinking on every query could be generating 5-10× more output tokens than their visible responses suggest. This is the real "nightmare scenario" — not someone typing messages all day, but someone running complex reasoning tasks that generate massive invisible token streams.

**Why this matters for Anthropic's margins:** Extended thinking is a key differentiator (it makes Claude better at hard problems), but it's also one of the most compute-intensive features to offer. Every thinking token costs the same as an output token to generate. On subscription plans where users pay a flat fee, heavy thinking usage directly erodes margins.

---

### Why coding agents are wildly profitable

[[Claude Code]], [[Cursor]], [[GitHub Copilot]], [[Windsurf]] — coding use cases have the most favorable I/O ratio in all of AI.

**Typical coding agent session:**
- Input: entire codebase (100K-1M tokens), docs, stack traces, error logs, file trees
- Output: a few code snippets, explanations, diff patches (1K-10K tokens)
- **I/O ratio: 100:1 to 1,000:1**

At true compute costs, a coding session that ingests 500K input tokens and generates 5K output tokens costs:
- Input: 0.5M × $0.003/MTok = $0.0015 (literally fractions of a penny)
- Output: 0.005M × $3/MTok = $0.015
- **Total: ~$0.017 per session**

A developer doing 50 such sessions per day costs Anthropic ~$0.85/day or **~$25/month** in compute — while paying $100-200/month for Max. And [[Claude Code]] is already generating >$2.5B ARR.

This is why every AI company is racing into coding tools. The unit economics are structurally superior to every other use case.

---

### The use cases that actually lose money

Not all inference is equal. Some patterns invert the favorable I/O ratio:

| Use case | I/O pattern | Why it's expensive |
|----------|-------------|-------------------|
| **Video generation** | Tiny text prompt → millions of output tokens (frames) | Inverted ratio — massive output from minimal input |
| **Extended thinking on hard problems** | Moderate input → enormous hidden output | 10-100K+ invisible thinking tokens per query |
| **ChatGPT Pro $200/mo power users** | Long conversational sessions with huge output | High output volume, no rate limits (OpenAI initially had none) |
| **Image generation** | Text → dense visual output | Different compute profile entirely (diffusion models) |
| **Real-time voice/audio** | Continuous streaming output | Sustained high-throughput output generation |

[[OpenAI]] CEO Sam Altman admitted the $200/mo ChatGPT Pro plan was "losing money" on some users — this is why. When users generate massive output without corresponding input, the favorable asymmetry inverts.

---

### The "AI is unsustainably expensive" narrative

**The bear case:** AI inference is a money pit. [[OpenAI]] burned $8.5B in 2025 on $12-13B actual revenue. [[Anthropic]] burned $5.2B on $9B ARR. The whole industry is subsidized by venture capital.

**The bull case:** Per-token inference margins are 80-95% on API. The losses come from:
- Training ($100M-$1B+ per frontier model run)
- Idle capacity and over-provisioning
- Hyperscaler markup on cloud infrastructure  
- Below-cost consumer subscriptions for market share
- Massive R&D/safety headcount

As [[Anthropic]] scales toward $70B revenue by 2028, training costs become a smaller fraction of revenue, utilization improves, and the path to 77% gross margins becomes plausible. The per-token economics were never the problem — it's everything *around* the tokens.

**The key insight most people miss:** The narrative that "AI inference is unsustainably expensive" may serve incumbent interests by discouraging competition. If the raw compute margins are really 80-95%, the barriers to profitable inference are much lower than commonly believed. The cloud computing playbook repeated: hype the costs, lock in the customers, print money at scale.

*Industry-wide inference costs are declining ~10× per year — faster than PC compute during the microprocessor revolution or bandwidth during the dotcom boom.*

---

## Related

- [[NVIDIA]] — player (acquired Groq $20B for inference)
- [[Groq]] — acquired (LPUs for fast inference)
- [[OpenAI]] — exposed (GPT-5 $30/$60 vs [[DeepSeek]] $0.27/$1.10)
- [[Anthropic]] — exposed (API pricing pressure)
- [[Open source commoditization]] — driver ([[DeepSeek]], [[Llama]], [[Mistral]])
- [[Model lab economics]] — context (training vs inference margins)
- [[CUDA moat]] — context (NVIDIA trying to own inference)
