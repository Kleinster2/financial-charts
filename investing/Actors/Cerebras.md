---
aliases: [CBRS]
---
#actor #ai #semiconductor #usa #public

**Cerebras** — Wafer-scale AI chips. Entire wafer = one chip. Training + inference. Last independent SRAM player after NVIDIA-Groq deal. Listed on Nasdaq as CBRS on May 14, 2026 in the largest US tech IPO of 2026 — closed Day-1 at $311.07 (+68.1% vs $185 offer), fully diluted ~$94.8B market cap. See [[Cerebras securities note]] for the equity-market companion.

---

## Price

![[cerebras-price-chart.png]]

*CBRS Day-1 trading on Nasdaq, May 14, 2026 — close $311.07. Chart will fill in as multi-day price action develops.*

---

## Financials

![[cerebras-fundamentals-chart.png]]

*CBRS revenue + net income, FY2022-FY2025 (yfinance ingest May 14 2026). Revenue compounded $24.6M → $79M → $290M → $510M — an exponential ramp that explains the IPO underwriting confidence. Net income line shows the structural story the [[Cerebras IPO revival April 2026]] event note flagged: deeply negative through 2024 (operating loss + non-operating drag), GAAP-positive in 2025 only because of the $363.3M forward-contract extinguishment gain that bridged the still-negative -$145M operating loss into +$237.8M reported earnings. The 2024 dip to -$481.6M is the worst-print year, ~$380M of non-operating expense on top of the -$101.6M operating loss.*

![[cerebras-sankey.png]]

*FY2025 income statement Sankey. Revenue → COGS / OpEx / Op loss / Non-op income / NI flow. The non-operating wedge is the key visual — without it, FY2025 would have been another operating-loss year.*

S-1 disclosed annual income statement (full historical detail in [[Cerebras IPO revival April 2026]]):

| Year | Revenue | GAAP NI / (loss) | Operating income / (loss) | Note |
|------|---------|------------------|--------------------------|------|
| 2022 | $24.6M | -$177.7M | -$178.8M | Per yfinance ingest |
| 2023 | $78.7M | -$127.2M | -$133.9M | Per Sep 2024 S-1 |
| 2024 | $290.3M | -$481.6M | -$101.6M | Per Apr 2026 S-1; net-income trough on non-operating drag |
| 2025 | $510.0M | $237.8M | -$145.3M | $390.7M other income (mostly forward-contract extinguishment gain $363.3M) bridged operating loss to GAAP profit |

2025 customer concentration per S-1: [[MBZUAI]] 62%, [[UAE G42]] 24%, combined 86%. Hardware revenue $358.4M, cloud/services $151.6M. Gross margin 39.0% (2025) vs 42.3% (2024). Non-GAAP net loss -$75.7M shows operating economics before the non-operating wedge.

Remaining performance obligations at Apr 2026 filing: $24.6B. Recognition cadence is back-end loaded — ~15% through end of 2027, ~43% in months 25-48, the rest later. No [[OpenAI]] revenue recognized in 2025; the $20B+ commitment is forward-only.

---

## Why Cerebras matters

Post-NVIDIA-Groq positioning (per Gavin Baker):

> "Cerebras is now in a very interesting and highly strategic position as the last independent SRAM player that was ahead of Groq on all public benchmarks."

| Metric | Value |
|--------|-------|
| Valuation | ~$22B (Jan 2026 talks) |
| Previous valuation | $8.1B (Sep 2025) |
| Total raised | $2B+ |
| Founded | 2016 |
| Approach | Wafer-scale integration |
| Strategic position | Last independent SRAM player |
| Public ticker | CBRS (Nasdaq; IPO expected May 2026) |

---

## Wafer-scale engine (WSE)

One wafer = one chip:

| Spec | WSE-3 |
|------|-------|
| Transistors | 4 trillion |
| Cores | 900,000 |
| Size | 46,225 mm² |
| vs GPU | 56x larger than [[H100]] |

Biggest chip ever made.

---

## Why wafer-scale?

Eliminates interconnect bottleneck:
- No chip-to-chip communication
- Massive on-chip memory bandwidth
- Designed for large AI models
- Single chip = simpler programming

---

## CS-3 system

Complete AI system:
- WSE-3 chip
- 44GB on-chip SRAM
- 125 petaflops FP16
- Inference + training

---

## Business model

Systems + cloud:
- Sell complete systems ($2-[[3M]]+)
- Cerebras Cloud inference
- Condor Galaxy supercomputer (with [[G42]])
- Enterprise + sovereign AI

---

## Customers

| Customer | Use Case |
|----------|----------|
| [[G42]] ([[UAE]]) | Condor Galaxy cluster |
| [[GSK]] | Drug discovery |
| [[AstraZeneca]] | Pharma AI |
| National labs | Research |

---

## January 2026 developments

### $1B raise at $22B valuation

| Metric | Value |
|--------|-------|
| Round size | ~$1B (in talks) |
| Pre-money valuation | $22B |
| Previous (Sep 2025) | $8.1B |
| Increase | 2.7x in 4 months |
| IPO target | Q2 2026 |

Significance: Among largest private AI hardware raises ever. Validates "last independent SRAM player" thesis.

### OpenAI $10B+ compute deal (Jan 14, 2026)

| Detail | Value |
|--------|-------|
| Deal value | $10B+ |
| Compute | 750 MW |
| Duration | 2026-2028 (multi-year) |
| Customer | [[OpenAI]] |

Game-changer: OpenAI diversifying beyond NVIDIA. Cerebras now has two mega-customers (OpenAI + [[G42]]).

Why OpenAI chose Cerebras:
- Inference cost advantage (SRAM)
- Reduce NVIDIA dependency
- Capacity availability
- [[Sam Altman]] was early Cerebras investor
- 15x faster responses than GPU-based systems

---

## [[GPT]]-5.3-[[Codex]]-Spark: first non-NVIDIA [[GPT]] model (Feb 2026)

The OpenAI deal's first concrete output — and a landmark for the inference market:

| Detail | Value |
|--------|-------|
| Model | [[GPT]]-5.3-[[Codex]]-Spark |
| Hardware | Cerebras Wafer Scale Engine 3 |
| Speed | 1,000+ tokens/sec |
| Benchmark | 77.3% on [[Terminal-Bench]] 2.0 (vs 64% for [[GPT]]-5.2-[[Codex]]) |
| Context | 128K, text-only |
| Availability | [[ChatGPT]] Pro, [[Codex]] app/CLI/VS Code |
| Significance | OpenAI's first [[GPT]] model that does not run on [[NVIDIA]] |

The model is optimized for real-time code editing — developers get immediate feedback on targeted edits to code, logic, or interfaces. Complements long-running frontier models (which work autonomously for hours/days) with a latency-first tier for interactive work.

[[Infrastructure]] integration: Cerebras's low-latency path was integrated into OpenAI's production serving stack alongside GPU infrastructure. OpenAI's framing: GPUs remain fundamental for training and broad inference; Cerebras excels where extremely low latency matters. Not a replacement — a dedicated tier.

Latency improvements shipped alongside [[Codex]]-Spark:
- WebSocket connection reduced per-roundtrip overhead by 80%
- Per-token overhead down 30%
- Time-to-first-token cut in half
- WebSocket path default for [[Codex]]-Spark, rolling out to all models

*Source: [Techzine](https://www.techzine.eu/news/analytics/138754/openai-swaps-nvidia-for-cerebras-with-gpt-5-3-codex-spark/) (Feb 2026), [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-lauches-gpt-53-codes-spark-on-cerebras-chips) (Feb 2026)*

---

## Andrew Feldman vs NVIDIA (Mar 2026)

Cerebras CEO has been publicly attacking [[NVIDIA]]'s inference position on [[LinkedIn]] for months:

Core argument: [[CUDA moat|CUDA]] is only needed for training, not inference. As the industry shifts to inference-dominant workloads, NVIDIA's software lock-in dissolves. The mental moat that kept enterprises on GPUs doesn't apply when the workload is fundamentally different.

This is aggressive positioning ahead of GTC, where NVIDIA plans to unveil its [[Groq]]-based inference platform — a direct competitive response to Cerebras's OpenAI wins.

---

## Apr 17, 2026 — OpenAI commitment expands, IPO revived

The renewed US IPO filing and the same-day reporting on the enlarged [[OpenAI]] relationship turned Cerebras from an architecture story into a public-markets underwriting question. The core issue is no longer whether the product is differentiated. It is whether investors are willing to fund a business whose forward demand looks enormous while the disclosed 2025 base was still concentrated in Abu Dhabi-linked customers and GAAP profitability depended on non-operating income.

See [[Cerebras IPO revival April 2026]] for the full event note, including the customer-concentration math, the operating-loss to net-income bridge, and the split between realized 2025 economics and the forward OpenAI story.

---

## May 11-12, 2026 - upsized CBRS IPO

Cerebras upsized the IPO on May 11-12 as AI-chip demand accelerated:

| Term | Updated IPO term |
|------|------------------|
| Shares offered | 30M |
| Price range | $150-$160 |
| Gross proceeds at high end | Up to $4.8B |
| Market value at high end | Around $34.4B |
| Prior range | 28M shares at $115-$125 |
| Expected pricing | May 13, 2026 |
| Expected trading | May 14, 2026, Nasdaq: CBRS |

The upsize is a live public-market test of the [[Cerebras IPO revival April 2026]] underwriting tension. Investors are no longer only underwriting the wafer-scale architecture; they are underwriting the idea that inference demand, [[OpenAI]] commitments, and AI-infrastructure scarcity justify a public valuation far above the last private mark.

*Sources: Investors Business Daily, WSJ, Bloomberg-linked reports and amended SEC filing coverage, May 11-12 2026.*

### May 13 pricing print

Cerebras priced CBRS at $185/share on May 13, 2026 — a full $25 above the top of the marketed $150-$160 range and $60 above the midpoint of the prior $115-$125 range disclosed in the May 4 amended S-1. The deal raised $5.55B at the offering size of 30M shares, $750M above the $4.8B high-end target the road show was anchored on. Fully diluted market cap at the IPO price came in at $56.4B, ~64% above the $34.4B implied at the upsized range's high end and ~2.6x the ~$22B last private mark from January 2026 talks.

| Term | Pricing print | Vs marketed |
|------|---------------|-------------|
| Final price | $185/share | +15.6% above the $160 high end |
| Shares offered | 30M | At marketed size (no second upsize) |
| Gross proceeds | $5.55B | +$750M vs $4.8B high-end target |
| Fully diluted market cap | $56.4B | +64% vs $34.4B at $160 high end |
| Vs January 2026 private mark (~$22B) | ~2.6x | Two-and-a-half-bagger before the first trade |
| First trade | Thursday May 14, Nasdaq: CBRS | As guided May 11-12 |
| Reported demand | Book reportedly >20x oversubscribed | Confirms above-range pricing reflects deep demand, not just a tight float |
| Green shoe / over-allotment exercise | Not yet disclosed | Watch the closing-of-the-offering 8-K |
| Allocation skew (institutional vs retail) | Not yet disclosed | Watch DTC + clearing-firm reporting next week |
| [[NVIDIA]] same-day reaction | NVDA $225.57 close (intraday range $221.57–$227.84), small net move | No incumbent-rotation read; CBRS demand priced as additive AI-infra signal, not GPU-share threat |

Disclosed top equity holders at IPO (Class B common):

| Holder | Stake |
|--------|-------|
| [[Fidelity]] | 11.3% |
| [[Benchmark]] | 9.5% |
| [[Foundation Capital]] | 8.3% |
| [[Eclipse Ventures]] | 7.3% |
| [[Alpha Wave Global]] | 6.5% |

Worth flagging: [[UAE G42]] is not in the disclosed top-5 holders despite its strategic-customer / Condor Galaxy partnership, and [[MBZUAI]] is not on the equity register at all — the 86% combined revenue concentration documented in [[Cerebras IPO revival April 2026]] is a *customer* concentration, not an equity-ownership overlap.

The pricing settles the live underwriting question opened by the April 17 S-1 in favor of demand: investors funded the forward [[OpenAI]] story and AI-infrastructure scarcity narrative at a valuation 2.6x the last private mark, with no equity-side governance link to the Abu Dhabi customer concentration. The inverse risk now flips to the aftermarket — every basis point above the $185 offer price compounds the earnings-quality gap that the S-1 made unavoidable. Aftermarket trading May 14 is the first independent read on whether the buyside that took allocation believes the same $56.4B fully diluted valuation that the underwriters cleared the book at.

*Sources: Reuters, Bloomberg, MarketScreener, Crunchbase News, May 13 2026.*

---

## May 14, 2026 — Day-1 trading print

CBRS opened on Nasdaq at $350.00 (+89.2% vs the $185 offer), reached an intraday high of $386.34 (+108.8%), and closed at $311.07 (+68.1%) on 32.68M shares — more than the entire 30M IPO float turned over in 6.5 hours. The session printed a full 28% intraday range from a $300.07 low. After-hours trading lifted to $329.57 (+78.1%) as buyers absorbed the close-of-day fade overnight.

| Print | Price | Vs $185 offer |
|-------|-------|---------------|
| Open | $350.00 | +89.2% |
| High | $386.34 | +108.8% |
| Low | $300.07 | +62.2% |
| Close | $311.07 | +68.1% |
| After-hours | $329.57 | +78.1% |
| Volume | 32.68M | >100% of 30M IPO float |

At $311.07 close, the implied fully diluted market cap is ~$94.8B (~305M shares × $311.07), ~68% above the $56.4B IPO mark and ~4.3× the ~$22B January 2026 private mark. Intraday high marked the company at ~$117.8B fully diluted.

The Day-1 print resolves the demand side of the [[Cerebras IPO revival April 2026]] underwriting tension. Investors paid up for the forward [[OpenAI]] demand story and AI-infrastructure scarcity premium; the S-1 customer-concentration math ([[MBZUAI]] 62%, [[UAE G42]] 24%) was assigned ~zero implicit weight in the public mark. What did not get resolved: the gap between the +89% open and the -19.5% close-vs-high fade. May 15 regular-hours trading is the first independent read on whether the print holds once the IPO-allocation cohort is no longer the only relevant buyer.

The May 25 [[Reuters]] [[SpaceX IPO 2026]] screen kept [[Cerebras]] in the positive-comp column, but with a warning embedded: by the May 21 cutoff, CBRS was still up 52% from the May 14 offer price, while already down about 27% from its first intraday high. That makes Cerebras a useful bridge between the bull and bear versions of the [[2026 IPO pipeline]]: public buyers are still paying for AI-chip scarcity, but the first-day squeeze is no longer enough evidence by itself.

See [[Cerebras securities note]] for full equity-market detail (peer comparisons, holder list, ticker-side notes). See [[Cerebras IPO revival April 2026]] for the full S-1-to-Day-1 timeline.

*Sources: Reuters, Bloomberg, StockAnalysis.com, VentureBeat, May 14 2026 close data; local market_data.db CBRS row.*

---

## IPO filing

Filed September 2024:
- First major AI chip IPO attempt
- Revealed $136M revenue (2023)
- Heavy losses
- [[G42]] concentration risk flagged
- IPO now targeting Q2 2026

---

## Post-NVIDIA-Groq landscape

After NVIDIA licensed [[Groq]]'s architecture (Dec 2025):

| Player | Status |
|--------|--------|
| [[Groq]] | NVIDIA partner, continues cloud |
| [[SambaNova]] | [[Acquired]] by [[Intel]] |
| Cerebras | Last independent SRAM player |

Why Cerebras wasn't acquired:

| Factor | Groq | Cerebras |
|--------|------|----------|
| Integration | Many-chip rack, fits [[NVLink]] | WSE = independent rack |
| Architecture | Easier to integrate | Harder to merge |
| Benchmarks | Strong | Ahead of Groq (public) |

Cerebras's wafer-scale approach makes integration harder — but may preserve independence.

---

## Strategic options

1. Stay independent — IPO, compete with [[Rubin]] SRAM
2. Hyperscaler acquisition — [[Google]], [[Amazon]], [[Microsoft]]
3. NVIDIA deal — Similar to Groq (licensing)
4. Sovereign AI focus — [[G42]] relationship, geopolitics

The bull case: Being last independent SRAM player = strategic scarcity value.

---

## Investment case

Bull:
- Last independent SRAM player — strategic scarcity
- Ahead of Groq on public benchmarks
- Differentiated architecture (wafer-scale)
- Large model specialist
- IPO = liquidity event
- Potential acquisition target

Bear:
- NVIDIA [[Rubin]] SRAM competes directly
- Customer concentration ([[G42]])
- High system costs
- Integration difficulty limits partnerships
- Unproven at scale

---

## Cap table / Investors

| Round | Amount | Valuation |
|-------|--------|-----------|
| Series A | $25M | — |
| Series B | $60M | — |
| Series C | $112M | — |
| Series D | $250M | — |
| Series E | $250M | ~$4B |
| Sep 2025 | — | $8.1B |
| Jan 2026 (talks) | ~$1B | $22B |
| Total | $2B+ | |

Key investors:

| Investor | Notes |
|----------|-------|
| [[Benchmark]] | Early (Series A) |
| [[Eclipse Ventures]] | Early |
| Alpha Wave Global | Growth (Series F) |
| [[Altimeter Capital]] | Growth |
| [[Coatue]] | Growth |
| [[UAE G42]] | Strategic (Condor Galaxy) |

[[G42]] relationship: Strategic partner and customer — built Condor Galaxy supercomputer together.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | Nasdaq: CBRS (listed May 14, 2026) |
| IPO price | $185 / share |
| Gross proceeds | $5.55B (30M shares) |
| Day-1 close | $311.07 (+68.1% vs offer) |
| Implied fully diluted mkt cap (close) | ~$94.8B |
| Total raised pre-IPO | $2B+ |
| Approach | Wafer-scale chips |
| Product | WSE-3, CS-3 |
| Position | Last independent SRAM player |
| Key customers | [[OpenAI]] ($20B+ multi-year), [[UAE G42]], [[MBZUAI]] |

*Updated 2026-05-14*

---

## Related

### Securities
- [[Cerebras securities note]] — Nasdaq: CBRS equity-market companion

### IPO event
- [[Cerebras IPO revival April 2026]] — S-1-to-Day-1 timeline, customer-concentration math, demand-side resolution

### Customers
- [[OpenAI]] — $20B+ potential multi-year compute commitment (Apr 2026 update)
- [[UAE G42]] — [[Condor Galaxy]] strategic partner, 24% of 2025 revenue per S-1
- [[MBZUAI]] — 62% of 2025 revenue per S-1

### Products / deployments
- [[Condor Galaxy]] — strategic AI supercomputer cluster with [[UAE G42]]

### Competitors
- [[NVIDIA]] — competitor, potential acquirer
- [[Groq]] — former competitor (now NVIDIA partner)
- [[SambaNova]] — former competitor ([[Intel]]-acquired)
- [[Tenstorrent]] — AI chip peer

### Top IPO holders (disclosed Class B)
- [[Fidelity]] (11.3%)
- [[Benchmark]] (9.5%)
- [[Foundation Capital]] (8.3%)
- [[Eclipse Ventures]] (7.3%)
- [[Alpha Wave Global]] (6.5%)

### Concepts
- [[2026 IPO pipeline]] — May 2026 live test of AI-infrastructure equity demand
- [[Inference disaggregation]] — market context (SRAM for decode)
- [[OpenAI Infrastructure Spend]] — forward demand framework
- [[AI infrastructure financing risk]] — financing-lens framing
- [[Long Cerebras]] — equity-story thesis

### Sources
- [Bloomberg: Cerebras $22B Valuation](https://www.bloomberg.com/news/articles/2026-01-13/cerebras-in-discussions-to-raise-funds-at-22-billion-valuation)
- [TechCrunch: OpenAI Cerebras Deal](https://techcrunch.com/2026/01/14/openai-signs-deal-reportedly-worth-10-billion-for-compute-from-cerebras/)
- [Reuters: Cerebras discloses US IPO filing](https://www.reuters.com/technology/nvidia-rival-cerebras-reveals-us-ipo-filing-ai-boom-drives-listings-2026-04-17/)
- [Reuters: OpenAI to spend more than $20 billion on Cerebras chips](https://www.reuters.com/technology/openai-spend-more-than-20-billion-cerebras-chips-receive-equity-stake-2026-04-17/)

