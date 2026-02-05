---
aliases: [GOOGL, GOOG, [[Google DeepMind]], DeepMind, Alphabet]
---
#actor #hyperscaler #usa

**Google (Alphabet)** — Tier 1 AI hyperscaler. DeepMind/Gemini, TPU pioneer, Anthropic investor, [[Broadcom]] disintermediation in progress.

---

## Leadership

| Role | Name | Background |
|------|------|------------|
| CEO | [[Sundar Pichai]] | Google CEO since 2015, Alphabet CEO since 2019. Product-focused leader. |
| CFO | Anat Ashkenazi | Joined Jul 2024 from [[Eli Lilly]] (CFO). |
| President & CIO | [[Ruth Porat]] | Former CFO (2015-2024). Oversees Other Bets, infrastructure. |
| Cloud CEO | Thomas Kurian | Joined 2019, ex-Oracle. Grew GCP to #3 cloud. |

---

## Board of Directors

| Name | Role | Background |
|------|------|------------|
| [[John Hennessy]] | Chair | Former Stanford President (2000-2016). Chair since 2018. |
| [[Sundar Pichai]] | Director | CEO |
| [[Larry Page]] | Director | Co-founder. Controlling shareholder. |
| [[Sergey Brin]] | Director | Co-founder. Controlling shareholder. |
| [[John Doerr]] | Director | [[Kleiner Perkins]] partner. Early Google investor. |
| Robin Washington | Director | [[Gilead Sciences]] CFO. Joined 2018. |
| Ann Mather | Director | Former Pixar CFO. |
| Frances Arnold | Director | Nobel laureate (Chemistry, 2018). Caltech professor. |
| K. Ram Shriram | Director | Early Google investor. Founding board member. |

*11 directors total. Page & Brin retain majority voting control.*

---

## Why Google matters

Google is the most vertically integrated AI hyperscaler:

| Metric | Value |
|--------|-------|
| AI capex | $91B (2025), $175-185B guided (2026) |
| AI lab | DeepMind (Gemini) |
| Custom silicon | TPU (7 generations) |
| Cloud | GCP (#3 behind AWS, Azure) |
| AI investment | [[Anthropic]] ($2B+) |

---

## Charts

![[goog-90d.png]]

![[goog-vs-qqq.png]]
*[[Nasdaq|QQQ]]*

![[goog-fundamentals.png]]

---

## Financials

### Annual (10 years)

| Year | Revenue | Net Income | EPS | Stock Price |
|------|---------|------------|-----|-------------|
| 2016 | $90.3B | $19.5B | $28.32 | $792 |
| 2017 | $110.9B | $12.7B | $18.27 | $1,053 |
| 2018 | $136.8B | $30.7B | $43.70 | $1,045 |
| 2019 | $162.0B | $34.3B | $49.16 | $1,340 |
| 2020 | $182.5B | $40.3B | $58.61 | $1,752 |
| 2021 | $257.6B | $76.0B | $5.61 | $145 |
| 2022 | $283.0B | $60.0B | $4.56 | $89 |
| 2023 | $307.4B | $73.8B | $5.80 | $141 |
| 2024 | $350.0B | $100.1B | $8.04 | $192 |
| **2025** | **$403.0B** | **$112.4B** | **$10.70** | **$195** |

*Source: Company filings. Stock price = year-end close. 2021+ EPS reflects 20:1 stock split (Jul 2022). Pre-split years shown in original form.*

### Q4 2025 earnings (Feb 4, 2026)

| Metric | Actual | Estimate | YoY |
|--------|--------|----------|-----|
| Revenue | $113.8B | $111.4B | +18% |
| EPS | $2.82 | $2.63 | — |
| Net income | $34.46B | — | +30% |
| Cloud revenue | $17.66B | $16.18B | +48% |
| YouTube ads | $11.38B | $11.84B | Miss |
| Advertising total | $82.28B | — | +13.5% |
| Operating cash flow | $52.4B | — | Record |
| Free cash flow | $24.6B | — | — |

**First company to cross $400B annual revenue.**

**2026 capex guidance: $175-185B** — nearly double $91B spent in 2025, **55% above $119.5B consensus**. Primarily for AI compute, technical infrastructure, and cloud growth. Most aggressive AI spending commitment from any hyperscaler.

**Market reaction:** Stock whipsawed after hours — fell 6% on the capex shock, then recovered as Cloud +48% sank in. Settled -2.4% premarket Feb 5. YouTube ads the only miss ($11.4B vs $11.8B).

**Ripple effects:** [[Broadcom]] +5.6% premarket (provides custom TPU silicon for Google). Capex guide implies total Mag 7 AI spend heading well above $500B for 2026 — bullish for [[NVIDIA]], data center REITs, power infrastructure.

---

## DeepMind / Gemini

**Google's AI research arm:**
- Merged Google Brain + DeepMind (2023)
- Led by [[Demis Hassabis]]
- Gemini model family (competing with GPT-4, [[Claude]])

| Model | Tier | Notes |
|-------|------|-------|
| **Gemini 3** | Latest | Released Q1 2026, outperforms competitors on benchmarks |
| Gemini 2.0 | Previous gen | Agentic capabilities |
| Gemini Ultra | Flagship | Multimodal |
| Gemini Pro | Mid-tier | API access |
| Gemini Nano | On-device | Mobile/edge |

**Scale:** 750M MAU (up from 650M in Q3 2025). Serving unit costs down 78% over 2025 through model optimizations and efficiency improvements.

**Apple deal:** Multiyear agreement for [[Apple]] to use Gemini in revamped [[Siri]], expected late 2026. Major distribution win.

**Competitive position:** Roughly par with OpenAI, gaining on consumer mindshare. Gemini 3 benchmarks ahead of competitors.

---

## TPU strategy

**Custom AI silicon (7 generations):**

| Generation | Status | Notes |
|------------|--------|-------|
| TPU v1-v4 | Deployed | Internal + Cloud |
| TPU v5 | Current | Widely available |
| TPU v6 (Trillium) | Ramping | Latest generation |
| TPU v7 (Ironwood) | Shipping (Nov 2025) | Closes gap with NVIDIA |
| TPU v9 | Planned (2027) | Exploring [[Intel]] EMIB |

### TPU vs NVIDIA performance (BF16 Dense TFLOPs)

![[tpu-vs-nvidia-tflops.png]]
*[[NVIDIA]]. Source: [[SemiAnalysis]] — [TPUv7: Google Takes a Swing at the King](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)*

| Chip | Release | TFLOPs | Gap to NVIDIA |
|------|---------|--------|---------------|
| TPU v4 | Jun 2022 | ~275 | 3.6x behind H100 |
| TPU v5e | Jun 2023 | ~197 | Efficiency variant |
| TPU v5p | Dec 2023 | ~459 | 2.2x behind H100 |
| TPU v6 | Jun 2024 | ~918 | Still behind H100 |
| **TPU v7** | Dec 2025 | **~2,340** | **94% of GB200** |

**Key insight:** TPU v7 nearly closes the gap — first time Google has reached parity with NVIDIA's flagship. Previous generations were 2-3x behind.

### CoWoS bottleneck (Jan 2026)

**TPU production cut due to TSMC constraints:**

| Metric | Original | Revised |
|--------|----------|---------|
| 2026 TPU target | ~4M units | ~[[3M]] units |
| Cause | TSMC CoWoS shortage | — |
| Problem | NVIDIA locked >50% of CoWoS through 2027 | — |

**Google's response:**
- Exploring [[Intel]] EMIB packaging for TPU v9 (2027)
- Also sounding out [[Samsung]] facilities in Texas
- Forced to cut production despite strong internal demand

**The allocation problem:** TSMC's packaging capacity now determines who scales AI — Google is constrained by NVIDIA's priority access.

### Broadcom relationship

**Current: Broadcom partnership**
- TPUs designed by [[Broadcom]], fabbed at [[TSMC]]
- Broadcom takes ~55% gross margin (~$15B/yr "tax")

### TPUv8 dual path (disintermediation)

| Path | Partner | Strategy |
|------|---------|----------|
| **Sunfish** | Broadcom | Turnkey (status quo) |
| **Zebrafish** | Direct + [[MediaTek]] | Google sources directly |

Google attempting to escape Broadcom's margin capture. Must cut ASIC costs to compete with [[NVIDIA]] Blackwell unit economics in 2026.

See [[Hyperscaler disintermediation]] for broader trend.

---

## Anthropic investment

**Hedging AI lab risk:**

| Investment | Amount | Notes |
|------------|--------|-------|
| Anthropic stake | $2B+ | Minority investor |
| Cloud deal | $3B+ | GCP credits |

Google backs Anthropic while competing with [[Claude]] via Gemini — hedging like Microsoft backing both OpenAI and [[Mistral]].

**Anthropic TPU deal:** ~1M TPUv7 direct from [[Broadcom]], not through Google Cloud. See [[Anthropic]].

---

## Google Cloud (GCP)

**#3 cloud provider:**

| Provider | Market share |
|----------|--------------|
| AWS | ~32% |
| Azure | ~23% |
| **GCP** | ~11% |

**Q4 2025:** $17.66B revenue (+48% YoY). Backlog surged to $240B — up 55% sequentially and 2x YoY.

**AI differentiation:**
- TPU access (vs NVIDIA-only competitors)
- [[Vertex]] AI platform
- Gemini API
- BigQuery ML

---

## Power strategy

**The grid bottleneck (Jan 2026):**

Marsden Hanna (Global Head of Sustainability and Climate Policy): Grid connection wait times exceed **12 years** in some US areas — a major obstacle to data center expansion.

Amanda Peterson Corio (Global Head of DC Energy): "We're looking at siting next to power generation and creating these industrial parks — still connected to the grid at the substation or interconnection point, but removing the bottlenecks to bringing generation online and also loads online."

**Response: Vertical integration into power**

| Deal | Value | Strategy |
|------|-------|----------|
| [[Intersect Power]] acquisition | **$4.75B** (Dec 2025) | Co-located solar + storage + DC |
| [[Kairos Power]] SMR | 500MW | Nuclear baseload |
| [[TPG]] Rise Climate partnership | $20B target | Clean energy parks |

**Colocation model:**
- Data centers sited next to power plants
- Industrial parks with integrated generation + compute
- Connected at substation level — bypasses 12-year interconnection queue
- First co-located project: operational 2026, fully complete 2027

**Data centers:** Expanding globally, power constraints apply. See [[Power constraints]].

---

## Infrastructure investments

| Project | Details |
|---------|---------|
| Kairos Power | 500MW SMR development |
| Submarine cables | Multiple investments ([[Google Pacific Connect]]) |
| Data centers | Global expansion |

---

## Other Bets

**Alphabet structure separates:**

| Bet | Status | Valuation |
|-----|--------|-----------|
| [[Waymo]] | Leader in autonomous driving | $126B (Feb 2026), 6 cities |
| Verily | Life sciences | — |
| [[Wing]] | Drone delivery | — |
| Calico | Longevity research | — |

**Waymo** is the crown jewel — $16B raised Feb 2026 at $126B valuation (~6% of Alphabet market cap). Only 1/6th of [[OpenAI]]'s valuation despite commercial robotaxi operations in 6 cities. Alphabet owns >75% post-round.

20M+ fully autonomous trips completed. 400K+ weekly rides. Launched Miami (6th city) in Jan 2026. Took $2.1B stock-based compensation charge in Q4 2025 tied to funding round.

---

## Competitive position

| vs | Google advantage | Google disadvantage |
|----|------------------|---------------------|
| [[Microsoft]] | Custom silicon (TPU) | Cloud market share |
| [[Amazon]] | AI research depth | Cloud dominance |
| [[Meta]] | Cloud business | Open-source momentum |
| [[OpenAI]] | Distribution (Search, Android) | [[Consumer]] mindshare |

---

## Antitrust

**Jan 2026:** Federal judge ruled Google must face consumer antitrust lawsuit alleging illegal dominance in online search market. Adds to ongoing DOJ case.

---

## Project Vault

Signed up as founding member of [[Project Vault]], the $12B US [[critical minerals]] stockpile (Feb 2026). Alongside [[Lockheed Martin]], [[General Motors]], [[Clarios]], and 12+ other companies.

---

## TCJA repatriation (2018)

Alphabet repatriated ~$50B under the [[Tax Cuts and Jobs Act]] one-time tax holiday. Deployed primarily into buybacks.

---

## Short interest history (quarterly)

| Quarter | SI % float | Stock | Note |
|---------|------------|-------|------|
| **Q1 2026** | **1.12%** | ~$195 | Below peer avg (7.15%) |
| Q4 2025 | 1.22% | $— | Fell 8.2% |
| Q3 2025 | — | $— | |
| Q2 2025 | — | $— | |

See [[Short interest]] for interpretation framework.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | GOOG / GOOGL (NASDAQ) |
| Market cap | ~$2.0T |
| Revenue (2025) | $403B |
| EPS (2025) | $10.70 |
| AI capex (2025) | $91B |
| AI capex (2026 guided) | $175-185B |
| TPU generations | v1 through v7 |
| Cloud rank | #3 (GCP) |
| AI lab | DeepMind |
| Key model | Gemini |
| Foundry | [[TSMC]] (via Broadcom) |
| Anthropic stake | $2B+ |
| Short interest | **1.12%** (Jan 2026) |

*Updated 2026-02-04 — Q4 2025 earnings*

![[goog-price-chart.png]]

![[goog-fundamentals.png]]

*Notable: $175-185B 2026 capex guidance nearly doubles 2025 spend. Market selling the beat on capex concerns — same pattern as every hyperscaler this cycle.*

---

## For theses

**[[Long TSMC]]**: TPUs = TSMC capacity, regardless of Broadcom relationship
**[[Long Broadcom]]**: $15B/yr TPU revenue at risk from disintermediation
**[[AI hyperscalers]]**: Top 3 spender on AI infrastructure
**[[Nuclear power for AI]]**: Kairos Power deal validates nuclear for AI

---

## Related

### Products
- [[Gemini]] — AI model (750M MAU)
- [[Apple]] — Gemini-Siri deal (late 2026)

### Partners/Competitors
- [[Broadcom]] — TPU design partner (disintermediating)
- [[MediaTek]] — alternative chip partner (Zebrafish)
- [[TSMC]] — foundry (via Broadcom TPUs)
- [[Anthropic]] — AI lab investment ($2B+) and competitor
- [[NVIDIA]] — competitor (GPUs) and customer
- [[Microsoft]] — hyperscaler competitor
- [[Amazon]] — hyperscaler competitor
- [[Meta]] — hyperscaler competitor
- [[OpenAI]] — AI lab competitor
- [[AI hyperscalers]] — peer category
- [[Waymo]] — subsidiary (autonomous driving)
- [[Kairos Power]] — nuclear power partner
- [[Nuclear power for AI]] — power strategy
- [[BYOP]] — power strategy context
- [[Power constraints]] — infrastructure constraint
- [[Hyperscaler disintermediation]] — Broadcom risk
- [[Demis Hassabis]] — DeepMind CEO
- [[Tax Cuts and Jobs Act]] — ~$50B repatriation (2018)
- [[Hyperscaler chip roadmap]] — TPU generational roadmap, custom silicon competition
