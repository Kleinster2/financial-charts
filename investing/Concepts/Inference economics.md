#concept #ai #economics #commoditization

# Inference economics

Training gets the headlines. Inference is where the money is - or isn't.

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

1. **Open source competition** - [[DeepSeek]], [[Llama]], [[Mistral]] at near-zero margin
2. **Hardware efficiency** - Each generation does more per dollar
3. **Quantization** - Smaller models, less compute
4. **Inference-specific chips** - Groq LPUs, [[Cerebras]], custom silicon
5. **Competition** - Too many providers, not enough differentiation

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

NVIDIA acquired **Groq for $20B** (Dec 2025) - inference-specific LPU chips.

- LPUs: 10x faster, 1/10th energy for inference
- NVIDIA entering non-GPU inference market
- Defensive move against inference commoditization

See [[CUDA moat]] - NVIDIA trying to own inference layer too.

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

Inference becomes like cloud compute - commodity pricing, winner-take-most at scale, margins compressed to infrastructure cost + small markup.

**Who survives:**
- Hyperscalers (scale + bundling)
- Self-hosted (enterprises owning their inference)
- Specialized chips (if efficiency gains continue)

**Who dies:**
- Pure-play API providers
- Premium-priced inference without differentiation

---

## True compute cost vs. API pricing (Feb 2026)

The gap between what providers *charge* and what inference *costs* is the central tension in AI economics. Everyone assumes AI inference is a money pit. The math suggests otherwise - at least for pure token generation. The losses come from elsewhere.

---

### GPU infrastructure: the cost floor

All inference runs on GPUs. The economics start here.

**H100 rental market (Feb 2026):**

| Provider type | Cost per H100/hr | Notes |
|---------------|-------------------|-------|
| Specialist (Hyperbolic, Hyperstack, Nebius) | $1.49-$1.90 | Lowest retail |
| Mid-tier (Lambda, Together.ai) | $1.85-$2.50 | Reserved capacity |
| Hyperscaler on-demand ([[AWS]], [[Google Cloud|GCP]], [[Microsoft|Azure]]) | $2.85-$6.98 | Highest retail |
| Spot/preemptible | $2.00-$2.50 | Interruptible |

H100 prices **declined 64-75% from peaks** and stabilized around $2.85-$3.50/hr for most providers. [[NVIDIA]] manufacturing cost per H100 is ~$3,320 - the markup to $25K-$40K retail reflects demand-driven margins.

**Full cluster economics:**
- Complete 8-GPU H100 server system: $200K-$400K (purchase)
- Power per H100: up to 700W under load
- Cooling/facilities upgrades: $15K-$100K depending on scale
- True operational cost for 8×H100 cluster: **$8-$15/hr** all-in (hardware, power, cooling, ops)

**Anthropic doesn't pay retail.** [[Anthropic]] runs on [[AWS]] infrastructure via a multi-billion-dollar partnership (Amazon invested $4B+ into Anthropic). They likely pay significantly below retail H100 rates, possibly 30-50% below public on-demand pricing. This is the critical unknown - Anthropic's actual negotiated rate determines whether their margins are good or amazing.

---

### First-principles cost per token

A detailed analysis by Martin Alderson models inference using [[DeepSeek]] R1's architecture (671B total params, 37B active via mixture of experts) as a proxy for frontier model economics. Setup: 72 H100s at $2/hr retail ($144/hr total), batch size 32, tensor parallelism across 8 GPUs per instance, 9 concurrent model instances.

**The input/output asymmetry:**

| Phase | How it works | Throughput (72× H100) | Cost per MTok |
|-------|-------------|----------------------|---------------|
| **Input (prefill)** | All tokens processed simultaneously in parallel. Each forward pass handles 32K tokens across the batch. Memory-bandwidth-bound. | ~46.8 billion tokens/hr | **~$0.003** |
| **Output (decode)** | Tokens generated sequentially - one token per sequence per forward pass. Memory-bandwidth-bound but 1,000× less parallel. | ~46.7 million tokens/hr | **~$3.08** |

**The asymmetry is ~1,000×.** Input processing is essentially free. Output generation has real costs. This single fact explains almost everything about AI pricing strategy.

**Why the asymmetry exists:** During prefill, a single forward pass processes ALL tokens in ALL sequences simultaneously - 32,000 tokens per pass. During decode, each forward pass produces only 32 tokens (one per sequence in the batch). Same GPU cost, 1,000× fewer tokens.

**Caveats and real-world adjustments:**
- MoE routing diversity can reduce throughput 30-50% (different tokens need different experts)
- Context length >128K shifts from memory-bound to compute-bound (attention scales quadratically), increasing costs 2-10×
- KV cache memory grows with context length and concurrent requests, limiting throughput
- These estimates assume retail H100 pricing - Anthropic/OpenAI likely pay 30-50% less

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
- [[DeepSeek]]'s pricing is close to or below true cost at retail GPU rates - they're either subsidizing or have dramatically lower infrastructure costs (Chinese GPU/power pricing)
- Opus 4.5's pricing ($5/$25) vs. Opus 4.1 ($15/$75) represents a 67% price cut with likely similar or lower true cost - margin compression by choice to drive volume

**Prompt caching further improves margins:**
- Cache writes: 1.25× base input price (5-min) or 2× (1-hr)
- Cache reads: 0.1× base input price (90% discount)
- Heavy caching users (RAG systems, agents) pay even less in true compute while paying more on initial cache writes
- Break-even: 2 reads for 5-min cache, 8 reads for 1-hr cache

**Batch API:** 50% discount on all token prices, with 24-hour turnaround. Still profitable given the true cost structure - batching improves GPU utilization, so the discount costs Anthropic less than 50%.

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

1. **Training costs** - frontier model training runs cost hundreds of millions to billions per run, amortized across the revenue base
2. **Idle capacity** - GPUs reserved for inference that aren't running at full utilization (the utilization equation is critical: 50%+ utilization needed to break even on 7B models, 10%+ for 13B)
3. **Third-party cloud markup** - Anthropic runs on [[AWS]]/[[Google Cloud|GCP]] infrastructure, not owned hardware. The hyperscaler takes a cut
4. **Extended thinking overhead** - thinking tokens are billed as output but the model generates far more internal tokens than visible output (see below)
5. **Safety/alignment R&D** - significant engineering spend on RLHF, constitutional AI, red-teaming
6. **Subscription subsidies** - consumer plans (Pro, Max) are priced below API-equivalent value
7. **Headcount** - ~1,500+ employees at AI-lab compensation levels

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

[[Anthropic]]'s consumer subscriptions are a fascinating case study in AI unit economics, because the "value" a subscriber gets at API rates vastly exceeds their subscription fee - but the actual compute cost is a fraction of both.

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

1. **Most subscribers are casual** - the median Pro user probably costs Anthropic $1-3/mo in compute
2. **Coding agents have asymmetric I/O** - massive context input (essentially free) with small code output. [[Claude Code]]'s 10M input + 30K output per day costs almost nothing in compute
3. **Rate limits cap the whales** - the 5-hour rolling window and weekly cap specifically prevent users from generating unlimited output tokens
4. **The "API-equivalent value" is marketing** - comparing subscription value to API prices is misleading because API prices have 80-95% margins built in. The real comparison is subscription price vs. compute cost
5. **Classic insurance model** - you pay for the *option* of high usage, most people don't exercise it fully

*Source: [Reddit analysis](https://www.reddit.com/r/ClaudeAI/comments/1ppkhat/) (Dec 2025), [Martin Alderson](https://martinalderson.com/posts/are-openai-and-anthropic-really-losing-money-on-inference/) (Aug 2025)*

---

### Extended thinking: the hidden cost multiplier

Extended thinking (chain-of-thought reasoning) is one of the most impactful - and most expensive - features in modern AI. **Thinking tokens are billed as output tokens** on the API, but their cost implications for subscription plans are enormous.

**How it works:** When extended thinking is enabled, [[Claude]] generates internal reasoning blocks before producing visible output. The model "thinks through" the problem step-by-step. These thinking tokens are invisible to the user but are real output tokens that consume the same GPU resources.

**Pricing (API):**
- Thinking tokens charged at standard output rates ($25/MTok for Opus 4.5, $15/MTok for Sonnet 4.5, $5/MTok for Haiku 4.5)
- Minimum budget: 1,024 tokens
- Typical thinking usage: 2,000-50,000+ tokens depending on task complexity

**Example - complex coding task on Sonnet 4.5:**
- Standard mode: 50K output tokens = $0.75
- Extended thinking: 8K thinking + 50K output = $0.87 (16% premium)
- But for hard reasoning tasks, thinking can be 100K+ tokens - doubling or tripling the cost

**Why this matters for subscriptions:** A Max subscriber using extended thinking on every query could be generating 5-10× more output tokens than their visible responses suggest. This is the real "nightmare scenario" - not someone typing messages all day, but someone running complex reasoning tasks that generate massive invisible token streams.

**Why this matters for Anthropic's margins:** Extended thinking is a key differentiator (it makes Claude better at hard problems), but it's also one of the most compute-intensive features to offer. Every thinking token costs the same as an output token to generate. On subscription plans where users pay a flat fee, heavy thinking usage directly erodes margins.

---

### Why coding agents are wildly profitable

[[Claude Code]], [[Cursor]], [[GitHub Copilot]], [[Windsurf]] - coding use cases have the most favorable I/O ratio in all of AI.

**Typical coding agent session:**
- Input: entire codebase (100K-1M tokens), docs, stack traces, error logs, file trees
- Output: a few code snippets, explanations, diff patches (1K-10K tokens)
- **I/O ratio: 100:1 to 1,000:1**

At true compute costs, a coding session that ingests 500K input tokens and generates 5K output tokens costs:
- Input: 0.5M × $0.003/MTok = $0.0015 (literally fractions of a penny)
- Output: 0.005M × $3/MTok = $0.015
- **Total: ~$0.017 per session**

A developer doing 50 such sessions per day costs Anthropic ~$0.85/day or **~$25/month** in compute - while paying $100-200/month for Max. And [[Claude Code]] is already generating >$2.5B ARR.

This is why every AI company is racing into coding tools. The unit economics are structurally superior to every other use case.

---

### The use cases that actually lose money

Not all inference is equal. Some patterns invert the favorable I/O ratio:

| Use case | I/O pattern | Why it's expensive |
|----------|-------------|-------------------|
| **Video generation** | Tiny text prompt → millions of output tokens (frames) | Inverted ratio - massive output from minimal input |
| **Extended thinking on hard problems** | Moderate input → enormous hidden output | 10-100K+ invisible thinking tokens per query |
| **ChatGPT Pro $200/mo power users** | Long conversational sessions with huge output | High output volume, no rate limits (OpenAI initially had none) |
| **Image generation** | Text → dense visual output | Different compute profile entirely (diffusion models) |
| **Real-time voice/audio** | Continuous streaming output | Sustained high-throughput output generation |

[[OpenAI]] CEO Sam Altman admitted the $200/mo ChatGPT Pro plan was "losing money" on some users - this is why. When users generate massive output without corresponding input, the favorable asymmetry inverts.

---

### The "AI is unsustainably expensive" narrative

**The bear case:** AI inference is a money pit. [[OpenAI]] burned $8.5B in 2025 on $12-13B actual revenue. [[Anthropic]] burned $5.2B on $9B ARR. The whole industry is subsidized by venture capital.

**The bull case:** Per-token inference margins are 80-95% on API. The losses come from:
- Training ($100M-$1B+ per frontier model run)
- Idle capacity and over-provisioning
- Hyperscaler markup on cloud infrastructure
- Below-cost consumer subscriptions for market share
- Massive R&D/safety headcount

As [[Anthropic]] scales toward $70B revenue by 2028, training costs become a smaller fraction of revenue, utilization improves, and the path to 77% gross margins becomes plausible. The per-token economics were never the problem - it's everything *around* the tokens.

**The key insight most people miss:** The narrative that "AI inference is unsustainably expensive" may serve incumbent interests by discouraging competition. If the raw compute margins are really 80-95%, the barriers to profitable inference are much lower than commonly believed. The cloud computing playbook repeated: hype the costs, lock in the customers, print money at scale.

*Industry-wide inference costs are declining ~10× per year - faster than PC compute during the microprocessor revolution or bandwidth during the dotcom boom.*

---

## Token price deflation curve (March 2026)

[[Epoch AI]] tracks the fastest sustained price collapse in computing history:

| Metric | Rate |
|--------|------|
| Median price decline (all benchmarks) | **50× per year** |
| Median post-Jan 2024 | **200× per year** |
| Range across benchmarks | 9× to 900× per year |
| GPQA Diamond (PhD-level science) | 40× per year |
| GPT-3.5-equivalent performance | $20/MTok (Nov 2022) → $0.07/MTok (Oct 2024) = **280×** in 18 months |
| Frontier-equivalent performance | $60/MTok (2021) → $0.06/MTok (2025) |

The fastest trends (900×/yr) emerged after January 2024 — driven by [[DeepSeek]], mixture-of-experts architectures, quantization advances, and hyperscaler competition. [[Epoch AI]] flags uncertainty on whether these rates persist.

Reasoning models are excluded from per-token price comparisons because they generate far more tokens than standard models — making headline $/MTok misleading for the actual cost of a task.

*Source: [Epoch AI inference price trends](https://epoch.ai/data-insights/llm-inference-price-trends)*

---

## The Jevons paradox in AI (March 2026)

Despite token prices falling ~1,000×, total enterprise AI spending surged **320% in 2025**. This is the textbook [[Jevons paradox]] — efficiency gains expand the addressable market faster than they reduce unit costs.

The mechanism: at $20/MTok, only high-value enterprise applications justified LLM deployment. At $0.40/MTok, every SaaS product, internal tool, and consumer app embeds AI. The addressable market expanded by orders of magnitude.

Structural amplifier: as prices fall, firms increase architectural complexity — reasoning depth, agentic loops, multi-step chains. Token intensity per task rises even as cost per token falls. The architecture-induced demand growth dominates the price effect.

[[Microsoft]] CEO [[Satya Nadella]] acknowledged this when [[DeepSeek]] launched its low-cost model: "Jevons paradox strikes again."

The implication for sovereign AI consumption: falling prices don't mean falling spend. Countries that build inference capacity will consume more, not less. The question isn't whether nations can afford tokens — it's whether they're building the capacity to consume them at the scale the technology demands.

---

## Global inference market by region (March 2026)

### Market sizing

| Region | 2024 | 2034 est. | Share (2024) |
|--------|------|-----------|-------------|
| North America | $35.4B | $123.9B | **38-45%** |
| Asia-Pacific | $20.4B | $71.6B | **22-29%** |
| Europe | $17.3B | $60.6B | **19-28%** |
| Global total | $97.2B (2024) → $113.5B (2025) → **$255B (2030)** | | |

*Sources: MarketsandMarkets, Polaris, Grand View Research (ranges reflect differing methodologies)*

### Country-level token consumption (OpenRouter, 100T token study)

The best empirical proxy for country-level consumption comes from [[OpenRouter]], which routes traffic across 300+ models from 60+ providers and processes 100+ trillion tokens. Their data captures ~1% of global inference. Billing-address-based geography:

| Rank | Country | Share of token volume |
|------|---------|----------------------|
| 1 | United States | **47.17%** |
| 2 | [[Singapore]] | **9.21%** |
| 3 | [[Germany]] | **7.51%** |
| 4 | [[China]] | **6.01%** |
| 5 | [[South Korea]] | **2.88%** |
| 6 | Netherlands | **2.65%** |
| 7 | [[United Kingdom]] | **2.52%** |
| 8 | Canada | **1.90%** |
| 9 | [[Japan]] | **1.77%** |
| 10 | [[India]] | **1.62%** |

Regional trend: Asia's share doubled from ~13% (early 2024) to ~31% (late 2025).

**Continental breakdown:** North America 47.22%, Asia 28.61%, Europe 21.32%, South America 1.21%, Oceania 1.18%, Africa 0.46%.

**Caveats:** OpenRouter skews developer/startup. Enterprise consumption via direct API contracts (OpenAI, Anthropic, Google) is invisible here. China's domestic consumption (via [[DeepSeek]], [[Qwen]], [[Baidu]]) is massively undercounted — most Chinese inference never touches Western routers. Singapore's outsized share likely reflects regional corporate billing addresses, not per-capita AI usage.

*Source: [OpenRouter State of AI 2025](https://openrouter.ai/state-of-ai), [a16z analysis](https://a16z.com/state-of-ai/)*

### Model ecosystem share

| Model family | Tokens processed (Nov 2024-Nov 2025) | Origin |
|-------------|---------------------------------------|--------|
| [[DeepSeek]] | **14.37T** | China |
| [[Qwen]] (Alibaba) | **5.59T** | China |
| [[Llama]] (Meta) | 3.96T | US |
| [[Mistral]] | 2.92T | France |
| [[OpenAI]] | 1.65T | US |

Chinese open-source models grew from ~1.2% of global usage (late 2024) to **~30%** (late 2025). [[Qwen]] surpassed 700M downloads on Hugging Face by January 2026. Simplified Chinese is the second-largest language by token volume (~5%), after English (82.87%).

Proprietary models still handle ~70% of total tokens. Open-source ~30%, of which Chinese OSS averages ~13% (spiking to 30% some weeks when new models drop).

Programming became the largest and fastest-growing use category — from ~11% of tokens (early 2025) to exceeding 50% by late 2025. Reasoning models crossed 50% of all token usage by year-end 2025.

---

## China's invisible inference (March 2026)

China's domestic AI inference consumption is largely invisible to Western measurement:

| What's visible | What's not |
|---------------|------------|
| OpenRouter routes (6% share) | Domestic API consumption (Baidu, Alibaba, ByteDance) |
| Hugging Face downloads (Qwen 700M+) | On-premise enterprise deployments |
| Export-facing API pricing | Government/military AI inference |
| State grid expansion plans ($722B) | Actual GPU utilization rates |

Self-hosting economics favor China: [[DeepSeek]] V3 breaks even on self-hosting at 15-40M tokens/month. Below that threshold, their APIs are already 10-30× cheaper than [[OpenAI]]. Chinese enterprises with even moderate volume have strong incentives to self-host, making their consumption permanently invisible to API-based trackers.

[[Alibaba]] committed RMB 380B (~$53B) over three years for AI and cloud. [[ByteDance]] targeting RMB 160B (~$23B) in 2026 capex, with ~$13B earmarked for AI processors. These are capacity commitments — the consumption they enable is untracked.

China's AI compute self-sufficiency could improve from ~33% (2024) to **90% by 2029**, translating to an $81B localization opportunity (from $6B). As domestic chips improve, the inference they power becomes even harder to track externally.

---

## Sovereign AI: capex vs. consumption (March 2026)

Nobody is systematically tracking "Country X consumed Y tokens at $Z cost." The entire sovereign AI discourse is supply-side — who's building what, for how much — not demand-side (who's burning how many tokens, for what purpose).

### What sovereign commitments look like

| Country | Commitment | % of GDP | Type |
|---------|------------|----------|------|
| China | $722B grid expansion | ~4% | Infrastructure |
| [[Saudi Arabia]] | $100B+ across initiatives | ~10% | Capex + partnerships |
| [[Qatar]] | $20B AI data centers | **9%** | Capex |
| [[South Korea]] | SWF targeting AI/chips | 5.7% (over 5 yrs) | Investment vehicle |
| [[India]] | $1.2B AI Mission | <0.1% | Government program |
| [[Japan]] | $50B+ semiconductors | ~1% | Industrial policy |
| [[Brazil]] | $4B AI initiative | <0.1% | Government program |

*Source: [Moody's sovereign AI fiscal risk analysis](https://fortune.com/2026/02/27/ai-spending-fiscal-risk-productivity-moodys/) (Feb 2026)*

### The measurement gap

Why nobody tracks sovereign token consumption:
1. API providers don't disclose by geography
2. Self-hosted inference generates no billing trail
3. Capex ≠ consumption — a $20B data center at 10% utilization consumes far fewer tokens than the investment implies
4. Token prices falling 50-200×/yr make spending a moving target even if volume were known
5. Military and government AI inference is classified in most countries

[[Gartner]] projects sovereign cloud IaaS at $80B globally in 2026 (+35.6% YoY). [[McKinsey]] estimates sovereign AI could be a $600B market by 2030, with 30-40% of all AI workloads pushed to sovereign environments by regulation. But these are infrastructure estimates, not consumption metrics.

The closest thing to a country-level token consumption tracker would combine:
- Cloud provider regional revenue splits (AWS, Azure, GCP)
- [[Epoch AI]] GPU cluster database (500+ clusters by country)
- OpenRouter-style routing data (developer segment only)
- Electricity consumption by AI data centers, by geography
- Enterprise surveys (Gartner, IDC)

Nobody has assembled this. It's a thesis-worthy research gap.

---

## Permanent-underclass thesis (Patel, Apr 2026)

[[Dylan Patel]] on [[Invest Like the Best]] (Apr 23, 2026) framed the supply/demand of tokens not as a pricing question but as a capacity-allocation question with distributional consequences. The argument runs in three steps:

| Step | Claim |
|---|---|
| 1. Tokens are demand-bound | [[Anthropic]] could double prices on [[Claude Opus|Opus]] and "most users would continue to pay." Demand exceeds available compute at every price point the labs are willing to charge. The constraint is capacity, not willingness to pay |
| 2. Allocation runs through enterprise contracts and relationships | "What really matters is having an [[Anthropic]] rep and having an enterprise contract with them and getting the rate limit increases that you need because otherwise tokens are ultimately super super in demand." Subscription tiers and rate-limit caps push power users toward per-token pricing relationships, making capacity access non-uniform across buyers |
| 3. Concentration follows | Frontier-tier access concentrates among well-capitalized buyers with [[Anthropic]]/[[OpenAI]] relationships. Patel illustrates with a hypothetical: "[[Ken Griffin]] of [[Citadel]] is super well-connected and super rich and he's like he just signs, you know, who knows? He goes and signs a deal with Open[[Anthropic]] that's like, 'Yeah, I'm going to get access to your models. Um, and I'll buy the first $10 billion worth of tokens each year.' ... Now he's going to crush everyone in the market." Hypothetical, not actual deal |

The strategic conclusion Patel labels the "permanent underclass" thesis: "Either you use more tokens and you generate economic value outsized economic value for the use of those tokens... There's three different problems here. Using more tokens, generating value from those tokens and capturing value from those tokens. If you don't do these three things, you'll never escape the permanent underclass."

### The three-problem structure

| Problem | Question | Failure mode |
|---|---|---|
| Use more tokens | Are you getting frontier-tier access at all? | Subscription-tier rate limits cap effective compute below what high-leverage tasks require |
| Generate value from tokens | Is the work the tokens do creating real surplus? | "Boring lazy" use case Patel rejects: "I'll just work one hour a day instead of eight." Lower output, no surplus |
| Capture value from tokens | Are you the principal or the contractor? | If you sell the AI-generated output at a price competitor AI-using firms can match, the surplus accrues to your customer, not you |

This is the demand-side counterpart to [[Idea-execution inversion|the idea-execution inversion]]. The inversion makes execution cheap; the permanent-underclass thesis says capacity to execute at the frontier is rationed and the rationing favors the already-large.

### Mythos as evidence of selective deployment

[[Claude Mythos]] is Patel's leading example. Internally available since Feb 2026, released only via [[Project Glasswing]] to ~40 cyber and critical-infrastructure customers. Patel's running joke nickname is "earwig" / "glasswig." Patel's framing: "I don't have Mythos. You know who has Mythos? Top freaking banks." The selective release pattern, in his read, generalizes — frontier access narrows as model capability expands.

### Anthropic margin debate (April 2026)

Patel calculated [[Anthropic]] gross margins at "a floor of 72%" by assuming all incremental compute went to inference. The calculation appears to contradict [The Information](https://www.theinformation.com/articles/anthropic-lowers-profit-margin-projection-revenue-skyrockets) (Jan 2026), which reported actual gross margin at ~40% for 2025, revised down from 50%, with inference costs 23% above plan and a 77% target by 2028. The discrepancy is large enough to matter for [[Long Anthropic|Anthropic equity-thesis]] modeling. Two interpretations:

- Patel's calculation models per-token margin (high) and treats prior period's R&D compute as sunk; his 72% is closer to a unit-margin floor than to GAAP gross margin
- The Information's figure is the GAAP-gross-margin reality including amortized training compute, third-party cloud markup, idle capacity, and consumer-subscription subsidies — all of which the per-token analysis in the Anthropic-margins section above already explains

Either interpretation can be true simultaneously. The vault carries both attributions until further disclosure.

*Source: [[Dylan Patel]] on [[Invest Like the Best]] (Apr 23, 2026)*

---

## Related

- [[NVIDIA]] - player (acquired Groq $20B for inference)
- [[Groq]] - acquired (LPUs for fast inference)
- [[OpenAI]] - exposed (GPT-5 $30/$60 vs [[DeepSeek]] $0.27/$1.10)
- [[Anthropic]] - exposed (API pricing pressure)
- [[Open source commoditization]] - driver ([[DeepSeek]], [[Llama]], [[Mistral]])
- [[Model lab economics]] - context (training vs inference margins)
- [[CUDA moat]] - context (NVIDIA trying to own inference)
- [[Separately Managed Accounts]] - parallel unit economics (fee structure vs true cost-to-serve)
- [[Sovereign AI race]] - context (national strategies, GPU stockpiling)
- [[Hyperscaler capex]] - supply side ($600B+ in 2026)
- [[AI infrastructure financing risk]] - bear case (circular capital flows)
- [[DeepSeek]] - disruptor (14.37T tokens on OpenRouter, 10-30× cheaper than OpenAI)
- [[Qwen]] - disruptor (700M+ downloads, Alibaba-backed)
- [[Phantom GDP]] - measurement consequence of token-cost collapse
- [[Idea-execution inversion]] - structural counterpart; demand-side mechanism
- [[Claude Mythos]] - selective-deployment example
- [[Project Glasswing]] - rationing mechanism for frontier access
