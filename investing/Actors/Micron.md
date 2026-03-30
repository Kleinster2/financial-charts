---
aliases: [MU, MU Economics, Micron Economics, Micron Business Economics]
tags: [actor, memory, usa, dram, nand]
---
#actor #memory #usa #dram #nand

**Micron Technology** — U.S.-based memory and storage company, the last American DRAM manufacturer. Third of the Big 3 in DRAM/NAND alongside [[Samsung]] and [[SK Hynix]], and the only one listed on a U.S. exchange.

---

## Sector correlation

| Sector | ETF | Correlation |
|--------|-----|-------------|
| [[Semiconductors]] | SMH | 0.83 |
| Technology | XLK | 0.77 |
| Industrials | XLI | 0.63 |
| *S&P 500* | *SPY* | *0.69* |

MU trades as a core Semiconductors name (SMH r = 0.83).

![[mu-price-chart.png]]

---

Gross margin went from -9.1% (FY2023) to 81% (Q2 FY2026) in three years. Three dynamics are driving the company:

1. HBM lock-in. Unlike commodity DRAM, [[HBM]] requires 6-42 month [[Qualification cycles|qualification cycles]] with each customer. [[NVIDIA]]'s Blackwell uses HBM qualified in 2023; Vera Rubin uses HBM being qualified now. HBM production cannibalizes standard DRAM at a 3:1 wafer ratio — every HBM wafer denies three wafers to commodity DDR5. More HBM production creates a worse shortage in standard memory. Micron is #3 with 21% share behind [[SK Hynix]] (62%) and [[Samsung]] (17%), but HBM4 mass production was announced ahead of schedule in February 2026 and is qualified with [[NVIDIA]].

2. U.S. champion status. $200B domestic investment commitment ($150B manufacturing + $50B R&D), $6.165B in [[CHIPS Act]] grants plus 25% investment tax credit. The [[Trump administration]] has positioned Micron as the centerpiece of industrial policy, threatening Korean memory makers with 100% tariffs. The only pure-play U.S.-listed large-cap memory name.

3. AI memory demand. Inference is memory-bound, not compute-bound. A single [[NVIDIA]] NVL72 rack (13.4TB of [[HBM]], ~$3M) serves roughly 330 concurrent users at 128K-token context on a 70B-parameter model — the [[GPU memory scaling|memory scales linearly]] with users and context length. CEO [[Sanjay Mehrotra]] at Davos (Jan 2026): memory is now a "strategic asset, not just a component." Aggregate industry supply is "substantially short of demand for the foreseeable future."

Open questions: Memory has peaked at 59.6% gross margin before (2018) and cratered to -14.5% within five years — five boom-bust cycles in 25 years. What's structurally different now is that co-designed HBM is not fungible the way commodity DRAM was — "it is no longer possible to easily replace a rival's memory product" ([[SK Hynix]], August 2025) — and demand may be elastic to price declines (cheaper inference drives more consumption, unlike gadget cycles). What's historically consistent is that new fabs take 3-5 years to come online (Idaho Fab 1 mid-2027, Fab 2 end-2028, Syracuse 2030+), and the industry has never sustained margins above 50% for more than two years. Where the margin floor settles after this cycle — whether it's the old 30-40% band or something higher — depends on whether HBM qualification lock-ins hold as the product matures and competitors catch up.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | MU (NASDAQ) |
| HQ | Boise, Idaho, USA |
| CEO | [[Sanjay Mehrotra]] (since 2017, co-founded [[SanDisk]]) |
| DRAM position | #3 (behind [[Samsung]], [[SK Hynix]]) |
| NAND position | #4 (behind Samsung, SK Hynix, [[Kioxia]]) |
| [[HBM]] position | #3 (21% share — SK Hynix 62%, Samsung 17%) |
| FQ2 2026 revenue | $23.86B (+75% seq), 81% gross margin, EPS $12.20 |
| FQ3 2026 guide | $33.5B +/-$750M, ~81% gross margin, EPS $19.15 |
| US investment | $200B ($150B mfg + $50B R&D) |
| [[CHIPS Act]] | $6.165B grants + 25% ITC |

*Updated 2026-03-28*

---

## Evolution

The story of Micron is the story of the last American memory company — a Boise, Idaho outfit that survived a consolidation wave that killed every other U.S. DRAM manufacturer, then found itself the centerpiece of American industrial policy four decades later.

- 1978-1981: Founded in Boise by Ward Parkinson, Joe Parkinson, Dennis Wilson, and Doug Pitman as a semiconductor design consultancy. Started manufacturing DRAM in 1981 in a converted dentist's office. Boise was an improbable location — no semiconductor ecosystem, no Stanford pipeline, no VC culture. But cheap land and a workforce willing to work around the clock gave it a cost edge that mattered when memory margins were measured in pennies.

- 1980s-1990s: Survived the Japanese DRAM dumping crisis that destroyed most U.S. competitors. The 1986 Semiconductor Trade Agreement (pushed by [[Intel]] and others) imposed anti-dumping duties on Japanese DRAM, giving Micron breathing room. While Mostek, Intersil, and National Semiconductor exited memory, Micron stayed — the only U.S. DRAM maker standing by the late 1990s. The strategy was relentless cost reduction on commodity parts, funded by through-cycle capex discipline.

- 2008-2012: The financial crisis nearly killed the company. Memory prices collapsed, the stock fell below $2, and Micron was widely expected to merge or fail. What saved it was the death of competitors: Qimonda (Germany) went bankrupt in 2009, [[Elpida]] (Japan) filed for bankruptcy in 2012. Micron acquired Elpida for ~$2B in 2013 — the deal that transformed it from a niche U.S. player into a global #3. It gained Japanese DRAM technology, mobile DRAM market share, and the Hiroshima fab complex overnight.

- 2016: Acquired the remaining 67% of Inotera ([[Taiwan]] joint venture) for $5.3B, fully integrating Taiwan manufacturing. Combined with Elpida, Micron now had fabrication in the U.S., Japan, Taiwan, and Singapore — a global manufacturing footprint comparable to the Korean giants.

- 2017-2018: [[Sanjay Mehrotra]] became CEO (May 2017), recruited from [[SanDisk]] which he co-founded. The 2017-2018 DRAM supercycle — driven by smartphone growth and the first wave of cloud data center buildout — pushed revenue to $30.4B and net income to $14.1B. Gross margin peaked at 59.6%. Mehrotra used the cash to invest in NAND, aiming to balance the portfolio.

- 2019-2020: The classic memory bust. Prices crashed, revenue fell to $21.4B. COVID initially worsened the outlook before work-from-home created a PC/server demand surge. The lesson repeated: memory margins are cyclical, and every peak funds the next crash.

- 2021-2022: WFH-driven recovery pushed revenue back to $30.8B ($8.7B net income). But the seeds of the next bust were planted — everyone was building inventory for demand already peaking.

- FY2023: The worst downturn in company history. Revenue cratered to $15.5B, net loss of $5.8B, gross margin hit -14.5% at the trough. Crypto winter killed consumer demand, post-COVID destocking hit enterprise, and all three memory makers burned cash simultaneously. The industry came within quarters of financial crisis.

- FY2024-2025: Recovery started slowly ($25.1B in FY2024, margin still only 22.4%), then accelerated as AI demand changed the character of memory economics. [[HBM]] qualification lock-ins created switching costs that commodity DRAM never had. Revenue reached $37.4B in FY2025 with margins expanding every quarter.

- 2026: The breakout. Q1 FY2026 delivered $13.6B revenue (+57% YoY) at 56.8% gross margin and the "largest ever supply-demand gap." Q2 FY2026 demolished expectations: $23.86B revenue (+75% sequential), 81% gross margin, $12.20 EPS vs $9.31 consensus. Q3 guided $33.5B — annualizing to $134B run rate, more revenue than [[Intel]] at peak. HBM4 mass production ahead of schedule. Syracuse groundbreaking for the largest private investment in [[New York]] state history. Exited Crucial consumer brand to redirect capacity to enterprise/AI. Micron became what it was never supposed to be: a growth company with pricing power.

---

## Business economics

Memory was a commodity business for forty years. The pattern: prices spike, everyone builds fabs, eighteen months later there's oversupply and another crash. Micron lived this cycle more violently than most — negative gross margins as recently as FY2023. All three survivors came within quarters of financial crisis.

The economics were brutal because memory was fungible. A DDR4 DIMM from [[Samsung]] worked identically to one from Micron. JEDEC standards ensured the same pinouts, the same performance. Switching suppliers took days.

| Period | TTM Gross Margin | What happened |
|--------|-----------------|---------------|
| Q4 2018 | 59.6% | Peak of 2017-2018 DRAM supercycle |
| Q2 2020 | 29.0% | Trough — oversupply after expansion |
| Q1 2022 | 45.8% | WFH demand + data center buildout |
| Q4 2023 | -14.5% | Worst in history — post-COVID crash |
| Q2 2025 | 34.7% | Recovery starting |
| Q1 2026 | 58.4% | Approaching 2018 peak — different composition |
| Q2 FY2026 | ~81% | Unprecedented for memory |

What changed is the character of demand. AI inference is memory-bound. A million concurrent users on a 128K-token context window require 40TB of working memory. Video generation consumes 25x more memory than equivalent image models. The workload shifted from "memory needs to be big enough" to "memory is the binding constraint."

[[HBM]] made the shift structural. Unlike commodity DRAM, HBM is a 3D stack of chips bonded directly to the GPU using through-silicon vias on a silicon interposer. Qualification takes 6-42 months. Revenue that shows up in 2027 is being locked in during 2025's qualification cycles. HBM production consumes roughly 3 wafers of capacity for every 1 wafer of output. As HBM production doubles (40%+ CAGR), standard DRAM supply tightens even as total wafer capacity grows. More production creates a worse shortage.

| Metric | Commodity DRAM era | HBM era (current) |
|--------|--------------------|--------------------|
| Gross margin range | -9% to 47% | 57% to 81% |
| Pricing mechanism | Spot/contract, quarterly reset | Multi-year LTAs, locked volumes |
| Customer switching cost | Days to weeks | 18-42 months (requalification) |
| Supply response time | 12-18 months | 3-5 years (new fabs) + 18-24 months ([[CoWoS]] packaging) |
| Revenue visibility | 1 quarter | 2-3 years |

Segment profitability reveals where the leverage is. In Q1 FY2026, gross margin fall-through (incremental gross profit per incremental dollar of revenue) hit +64.5% in mobile, +63.2% in automotive, +44.1% in cloud, and -127.2% in core data center (decelerating). Mobile's strength is counterintuitive — it reflects supply crunch from HBM cannibalization of consumer DRAM, not AI demand directly. Micron exited its Crucial consumer brand in February 2026, freeing capacity for enterprise. When a supplier voluntarily exits consumer, the shortage is severe.

---

## HBM status

Micron is #3 in [[HBM]] with approximately 21% market share (Q2 2025 data), behind [[SK Hynix]] (62%) and [[Samsung]] (17%). The competitive position resets with each generation — each qualification win reshuffles share.

HBM4 milestone (Feb 11, 2026): CFO Mark Murphy announced at Wolfe Research Conference that HBM4 is in mass production and shipping to customers — a full year ahead of schedule. Denied rumors of exclusion from [[NVIDIA]] next-gen supply chain.

| Metric | Value |
|--------|-------|
| HBM share of DRAM bits (2023) | ~1.5% |
| HBM share of DRAM bits (2025) | ~6% |
| HBM TAM (2025) | $35B |
| HBM TAM (2028E) | $100B |
| HBM CAGR | ~40% |
| HBM4 premium over HBM3E | ~50% |
| Wafer cannibalization ratio | ~3:1 (HBM vs standard) |
| Qualification timeline | 6-42 months |
| 2026 supply | Fully contracted (price and volume) |

DRAM pricing (2025-2026):

| Period | Contract price change |
|--------|-----------------------|
| Q4 2025 | +45-50% QoQ |
| Q1 2026E | +55-60% QoQ |
| LPDDR4X/5X Q1 2026 | +90% QoQ |
| NAND Q1 2026 | +33-38% QoQ |

CEO [[Sanjay Mehrotra]] at Davos (Jan 2026):
- Memory is now a "strategic asset, not just a component in the system"
- AI demand is "accelerating and irreversible"
- Customers "concerned about long-term access to memory" — multi-year contracts
- Aggregate industry supply "substantially short of demand for the foreseeable future"
- Bernstein's Mark Li raised PT to $330, forecasting 20-25% sequential DRAM price increase

---

## Financials

### Annual (fiscal year ends August)

| FY | Revenue | Gross Margin | Net Income | EPS | FCF |
|----|---------|-------------|------------|-----|-----|
| 2016 | $12.4B | -- | -$0.3B | -$0.27 | -- |
| 2017 | $17.1B | -- | $2.7B | $2.32 | -- |
| 2018 | $30.4B | 59.6% | $14.1B | $11.51 | -- |
| 2019 | $23.4B | 45.7% | $6.3B | $5.51 | -- |
| 2020 | $21.4B | 30.6% | $2.7B | $2.42 | -- |
| 2021 | $27.7B | 37.6% | $5.9B | $5.14 | $2.4B |
| 2022 | $30.8B | 45.2% | $8.7B | $7.75 | $3.1B |
| 2023 | $15.5B | -9.1% | -$5.8B | -$5.34 | -$6.1B |
| 2024 | $25.1B | 22.4% | $0.8B | $0.70 | $0.1B |
| 2025 | $37.4B | 39.8% | $8.5B | $7.59 | $1.7B |
| TTM Feb 2026 | $58.1B | 58.4% | $24.1B | $21.53 | $10.3B |

*Source: Company filings. FY2023 was memory downturn; FY2025-2026 is AI-driven boom.*

### Recent quarters

| Quarter | Revenue | Gross Margin | EPS | Guide (next Q) |
|---------|---------|-----|-----|----------------|
| Q1 FY2026 (Dec 2025) | $13.6B (+57% YoY) | 56.8% | -- | $18.7B |
| Q2 FY2026 (Mar 2026) | $23.86B (+75% seq) | ~81% | $12.20 | $33.5B +/-$750M |

Q2 FY2026 demolished consensus: revenue beat by $3.79B (+19% vs $20.07B est), EPS beat by $2.89 (+31% vs $9.31 est). Largest sequential revenue jump in Micron's history. Record across DRAM, NAND, and HBM. Three drivers: HBM revenue accelerating (HBM4 mass production flowing into revenue), DRAM pricing power deepening as [[Memory shortage 2025-2026]] worsens, and AI demand broadening beyond training to inference, edge, and automotive.

Q1 FY2026 key quotes: "Largest ever seen supply-demand gap." Only meeting 50-67% of demand from key customers. Tightness to persist through and beyond CY2026.

![[mu-fundamentals-chart.png]]

![[mu-sankey-q2fy2026.png]]

![[mu-sankey.png]]

![[mu-sankey-fy2024.png]]

---

## Capex and capacity

FY2024-FY2027 marks the first four consecutive years of capex growth in 25+ years. Capital intensity is dropping below 30% (vs 35% through-cycle guidance) — revenue growing faster than capex.

| Facility | Status | Timeline |
|----------|--------|----------|
| Idaho Fab 1 | Under construction | Mid-2027 |
| Idaho Fab 2 | Construction starting 2026 | End of 2028 |
| New York (Clay, Syracuse) | Groundbreaking Jan 2026 | 2030+ |
| [[Taiwan]] (Tongluo) | Acquired from [[Powerchip Semiconductor]] ($1.8B) | Construction start end FY2026 |
| Singapore HBM packaging | On track | CY2027 |
| [[India]] back-end | Ramping | 2026 |

Total US investment: $200B ($150B manufacturing + $50B R&D). [[CHIPS Act]]: $6.165B grants + 25% ITC.

Syracuse (Jan 17, 2026): largest private investment in [[New York]] state history. Four chip fabrication plants planned, 50,000 jobs expected. Attendees: Commerce Secretary Howard Lutnick, Gov. Hochul, Chuck Schumer, CEO [[Sanjay Mehrotra]].

[[Taiwan]] expansion (Mar 16, 2026): second manufacturing facility at Tongluo site for advanced DRAM production including [[HBM]]. Acquired from [[Powerchip Semiconductor]] for $1.8B.

---

## Apple MacBook price hikes validate memory crunch (Mar 3, 2026)

[[Apple]] raised MacBook Air/Pro prices by $100-$400, explicitly driven by memory costs — the most visible consumer-facing confirmation of the [[Memory shortage 2025-2026]]:

- Q1 2026 contract DRAM prices: +55-60% QoQ
- LPDDR4X/5X: +90% QoQ
- NAND: +33-38% QoQ
- Demand growing ~35% in 2026 vs supply growth ~23% — widest gap in decades
- AI forecast to consume 20% of global DRAM wafer capacity in 2026
- Gartner: memory = 23% of PC BOM in 2026 (vs 16% in 2025), average PC prices +17% YoY
- Consumer relief not expected until 2028-2029

Micron exiting Crucial + [[Apple]] passing costs to consumers = the squeeze is real. Every HBM wafer for an [[NVIDIA]] GPU is a wafer denied to LPDDR5X for consumer devices.

---

## Competitive dynamics

| vs Competitor | Status |
|---------------|--------|
| [[SK Hynix]] | Behind on HBM (62% vs 21% share), similar DRAM exposure |
| [[Samsung]] | Behind on scale, similar shortage benefit, ahead on HBM (21% vs 17%) |
| [[CXMT]] | Ahead, but CXMT catching up via [[IP leakage risk]] |

---

## For theses

[[Long memory]]:
- Benefits from shortage dynamics
- U.S.-based = geopolitical diversification
- #3 HBM but ramping

[[Memory squeeze thesis]]:
- Exited Crucial consumer brand (Feb 2026) — validates squeeze
- Full pivot to enterprise/AI memory
- HBM supply locked to hyperscalers

---

## Related

### Securities
- [[Micron securities]] — price history, relative value, ETF exposure, charts, analyst coverage

### Sectors
- [[US Memory]] — sub-sector
- [[Memory]] — parent sector
- [[Semiconductors]] — broad sector

### People
- [[Sanjay Mehrotra]] — CEO since 2017

### Competitors
- [[SK Hynix]] — #1 HBM
- [[Samsung]] — #2 HBM
- [[CXMT]] — [[China]] competitor
- [[SanDisk]] — US memory peer (NAND)

### Customers
- [[NVIDIA]] — HBM for GPUs

### Context
- [[Memory shortage 2025-2026]] — supply-demand crisis
- [[Export controls]] — less exposed than Korea
- [[HBM economics]] — structural shift
- [[HBM]] — the product
- [[Trump administration]] — industrial policy positioning
- [[China Micron ban June 2023]] — China risk event
- [[Applied Materials]] — EPIC Center founding partner
