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
| AI capex | $50B+ annually |
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
| 2025E | $385.5B | $124.3B | $10.10 | $195 |

*Source: Company filings. Stock price = year-end close. 2021+ EPS reflects 20:1 stock split (Jul 2022). Pre-split years shown in original form.*

---

## DeepMind / Gemini

**Google's AI research arm:**
- Merged Google Brain + DeepMind (2023)
- Led by [[Demis Hassabis]]
- Gemini model family (competing with GPT-4, [[Claude]])

| Model | Tier | Notes |
|-------|------|-------|
| Gemini Ultra | Flagship | Multimodal |
| Gemini Pro | Mid-tier | API access |
| Gemini Nano | On-device | Mobile/edge |
| Gemini 2.0 | Latest | Agentic capabilities |

**Competitive position:** Roughly par with OpenAI, catching up on consumer mindshare.

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
| [[Waymo]] | Leader in autonomous driving | $126B (Feb 2026) |
| Verily | Life sciences | — |
| [[Wing]] | Drone delivery | — |
| Calico | Longevity research | — |

**Waymo** is the crown jewel — $16B raised Feb 2026 at $126B valuation (~6% of Alphabet market cap). Only 1/6th of [[OpenAI]]'s valuation despite commercial robotaxi operations in 5 cities. Alphabet owns >75% post-round.

---

## Competitive position

| vs | Google advantage | Google disadvantage |
|----|------------------|---------------------|
| [[Microsoft]] | Custom silicon (TPU) | Cloud market share |
| [[Amazon]] | AI research depth | Cloud dominance |
| [[Meta]] | Cloud business | Open-source momentum |
| [[OpenAI]] | Distribution (Search, Android) | [[Consumer]] mindshare |

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
| Revenue (2025E) | $400B |
| Revenue (2026E) | $456B |
| EPS (2025E) | $10.57 |
| EPS (2026E) | $11.23 |
| AI capex | $50B+ annually |
| TPU generations | v1 through v7 |
| Cloud rank | #3 (GCP) |
| AI lab | DeepMind |
| Key model | Gemini |
| Foundry | [[TSMC]] (via Broadcom) |
| Anthropic stake | $2B+ |
| Short interest | **1.12%** (Jan 2026) |

*Updated 2026-01-20*

![[goog-price-chart.png]]

![[goog-fundamentals.png]]

*Notable: Revenue growing 14% but EPS only 6% in 2026 — margin compression from $50B+ AI capex.*

---

## For theses

**[[Long TSMC]]**: TPUs = TSMC capacity, regardless of Broadcom relationship
**[[Long Broadcom]]**: $15B/yr TPU revenue at risk from disintermediation
**[[AI hyperscalers]]**: Top 3 spender on AI infrastructure
**[[Nuclear power for AI]]**: Kairos Power deal validates nuclear for AI

---

## Related

### Products
- [[Gemini]] — AI model (650M MAU, #3 global)

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
