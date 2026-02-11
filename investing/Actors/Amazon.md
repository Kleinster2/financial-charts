---
aliases: [AMZN]
---
#actor #hyperscaler #usa

# Amazon (AWS)

Tier 1 AI hyperscaler, largest cloud provider, major custom silicon player (Trainium, Graviton). [[Anthropic]]'s primary cloud partner.

---

## Why it matters

Amazon is central to multiple vault theses:
- **Anthropic investor**: $8B total, primary cloud/training partner
- **Custom silicon**: Trainium competing with NVIDIA for training
- **Infrastructure scale**: $200B AWS backlog, multi-GW buildouts
- **Foundry customer**: [[TSMC]] 3nm for Trainium3

---

## Leadership

| Role | Name | Since |
|------|------|-------|
| CEO | **Andy Jassy** | Jul 2021 |
| CFO | Brian Olsavsky | 2015 |
| CEO, AWS | Matt Garman | Jun 2024 |
| CEO, Worldwide Stores | Doug Herrington | 2022 |
| Founder & Exec Chairman | Jeff Bezos | 1994 |

Jassy promoted from AWS CEO when Bezos stepped back. New "shadow" advisor: Dharmesh Mehta (Feb 2026).

---

## Charts

![[amzn-90d.png]]
*AMZN 90-day price*

![[amzn-vs-qqq.png]]
*AMZN vs [[Nasdaq|QQQ]]*

![[amzn-fundamentals.png]]
*AMZN revenue and net income*

---

## Financials

### Annual (10 years)

| Year | Revenue | Net Income | EPS | Stock Price |
|------|---------|------------|-----|-------------|
| 2016 | $136.0B | $2.4B | $4.90 | $750 |
| 2017 | $177.9B | $3.0B | $6.15 | $1,169 |
| 2018 | $232.9B | $10.1B | $20.14 | $1,502 |
| 2019 | $280.5B | $11.6B | $23.01 | $1,848 |
| 2020 | $386.1B | $21.3B | $41.83 | $3,257 |
| 2021 | $469.8B | $33.4B | $64.81 | $3,334 |
| 2022 | $514.0B | -$2.7B | -$0.27 | $84 |
| 2023 | $574.8B | $30.4B | $2.90 | $152 |
| 2024 | $638.0B | $59.2B | $5.53 | $220 |
| **2025** | **$716.9B** | **$62.0B** | **$5.78** | **$230** |

*Source: Company filings. Stock price = year-end close. 2022 reflects Rivian investment losses. Post-2022 EPS reflects 20:1 stock split (Jun 2022).*

---

## Custom chip portfolio

### Trainium (AI training/inference)
| Generation    | Node    | Status                  | Key specs                              |
| ------------- | ------- | ----------------------- | -------------------------------------- |
| Trainium1     | 7nm     | Legacy                  | First gen                              |
| Trainium2     | 5nm     | [[Shipping]] (Dec 2024)     | NeuronCore-v3                          |
| **Trainium3** | **3nm** | **[[Shipping]] (Dec 2025)** | 2.52 PFLOPs FP8, 144GB HBM3e, 4.9 TB/s |
| Trainium4     | TBD     | Development             | [[NVLink]] Fusion support              |

**Trainium3 UltraServer**: 144 chips per server, scales to 1M chips (10x previous gen), 40% more energy efficient.

**Trainium4**: First hyperscaler custom chip with **NVIDIA NVLink Fusion** compatibility — can interoperate with NVIDIA GPUs.

### Inferentia (inference — discontinued)
- Inferentia2 was last generation
- Stopped development — inference converging with training workloads
- Trainium now handles both

### Graviton (general compute)
| Generation | Status |
|------------|--------|
| Graviton4 | [[Shipping]] |
| **Graviton5** | **Announced Dec 2025** — most powerful AWS CPU |

---

## Anthropic partnership

| Metric | Value |
|--------|-------|
| Total investment | $8B (minority stake) |
| Q3 2025 unrealized gain | $9.5B (mark-to-market at $183B valuation) |
| Infrastructure | Project Rainier ($11B Indiana DC) |
| Chip commitment | 1M Trainium chips for Anthropic |
| Relationship | "Primary cloud and training partner" |

Anthropic using Trainium2/3 to train and deploy [[Claude]] models. Strategic alignment: Amazon needs AI differentiation, Anthropic needs compute scale.

---

## Infrastructure investments

| Project | Amount | Capacity | Timeline |
|---------|--------|----------|----------|
| Project Rainier (Indiana) | $11B | — | Opened Oct 2025 |
| Northern Indiana expansion | $15B | 2.4 GW | Announced Dec 2025 |
| Government AI/supercomputing | $50B | 1.3 GW | Breaking ground 2026 |
| **AWS backlog** | **$200B** | — | — |

**Total new capacity**: 3.7 GW committed

### AWS AI Factories (Dec 2025)
- On-premises AI infrastructure for enterprises/government
- NVIDIA + Trainium + AWS networking
- Operates like private AWS Region
- Targets compliance/sovereignty requirements

---

## Project LEO (satellite broadband)

**Rebranded from Project Kuiper** — Amazon's LEO satellite constellation targeting broadband, enterprise, and public safety.

| Metric | Value |
|--------|-------|
| Constellation | 3,236 satellites planned |
| FCC deadline | Half launched by July 30, 2026 |
| TAM estimate | $20-34B by 2030 |
| Launch providers | [[Blue Origin]], [[SpaceX]], Arianespace, ULA |

### AT&T partnership (Feb 2026)

AT&T selected Amazon LEO as primary satellite layer for enterprise and public safety fixed broadband. Deal includes:
- AWS hybrid cloud migration of major AT&T workloads
- High-capacity AT&T fiber connecting AWS data centers
- Fixed broadband for enterprise clients — **not** direct-to-cell

**Stock impact:** Announcement hammered satellite pure-plays — [[AST SpaceMobile]] fell ~11%, [[Globalstar]] fell ~7%. Market feared vertically integrated "super-platforms" (rockets + satellites + cloud + AI) would erode smaller players' moats.

**Clarification:** AT&T stated the Amazon LEO deal does not impact plans with [[AST SpaceMobile]] for direct-to-cell. Different use cases: Amazon LEO = fixed broadband/backhaul; AST = "cell tower in the sky" for smartphones.

**Strategic significance:** Secures guaranteed revenue base for LEO constellation during deployment. Serves as counterweight to [[Starlink]] dominance — Amazon betting on "high-integration" model vs SpaceX's satellite-count lead.

---

## Partnerships

| Partner       | Relationship                                |
| ------------- | ------------------------------------------- |
| [[Anthropic]] | $8B investor, cloud partner, 1M chips       |
| [[NVIDIA]]    | 15-year collaboration, NVLink Fusion coming |
| [[Marvell]]   | Trainium/Inferentia design partner          |
| [[OpenAI]]    | Potential $10B investment (reported)        |
| [[AT&T]]      | Project LEO satellite broadband + AWS cloud |

---

## Saks investment loss

**A rare strategic misfire** — Amazon lost $475M backing a luxury retail merger that collapsed in 14 months.

| Metric | Value |
|--------|-------|
| Investment | $475M preferred equity (Dec 2024) |
| Stake | 23% of [[Saks Global]] |
| Current value | "Presumptively worthless" |
| Lost commercial agreement | $900M over 8 years |

**The deal:** Amazon invested to facilitate the [[Saks-Neiman merger]], gaining consent rights over financing and a commercial agreement to launch "Saks on Amazon."

**What went wrong:**
- "Saks on Amazon" platform never launched
- Saks burned through cash, failed to meet budgets
- In Aug 2024, Saks raised $600M using flagship as collateral — without Amazon's consent
- In [[Saks bankruptcy]] (Jan 2026), Saks pledged the $3.6B Fifth Avenue flagship for [[DIP financing]], subordinating Amazon behind bondholders
- Amazon challenged in court but lost after 7.5-hour hearing

**Amazon's response:** Reserved rights to "seek more drastic remedies" including appointment of examiner or trustee. Claims Saks "violated consent rights under the LLC agreement."

**Significance:** Contrasts with Amazon's successful Anthropic bet ($8B → $9.5B unrealized gain). Retail M&A judgment vs tech infrastructure judgment.

---

## Thesis implications

| Thesis | Impact |
|--------|--------|
| [[Long Anthropic]] | Amazon's $9.5B gain validates valuation |
| [[Long TSMC]] | Trainium3 = 3nm TSMC demand |
| [[Power constraints]] | +3.7 GW capacity additions |
| [[Hyperscaler chip roadmap]] | Trainium3/4 major custom silicon milestone |

---

## Wearable AI (Bee)

**Acquired**: September 2024 (8-person team)

Bee is a $50 always-listening wearable that records/transcribes daily activities, creating to-do lists and conversation recaps via companion app. No display or camera — "ambient AI" hardware with week-long battery life.

**Privacy model**: Audio processed in real-time, deleted after processing, never stored.

**Recent features** (Jan 2025):
- Voice notes (quick button press capture)
- Daily insights (mood/relationship trends)
- "Actions" — email drafts, calendar invites via Gmail/calendar integration

**Strategic context**: Part of broader Alexa+ strategy. Daniel Rausch (VP Alexa/Echo) hinted at larger product revamp — likely full Amazon branding coming. Co-founder Maria de Lourdes Zollo sees future "constellation of devices" including camera-equipped wearables.

**History**: Amazon's wearable track record is weak (Halo discontinued 2023, earbuds stale). Bee represents fresh approach via acquisition rather than internal build.

---

## What to watch

- [ ] Bee rebranding/integration into Alexa ecosystem
- [ ] Trainium3 customer adoption beyond Anthropic
- [ ] Trainium4 NVLink Fusion benchmarks (expected 2026)
- [ ] Anthropic IPO timing and Amazon's stake value
- [ ] AWS AI Factories enterprise traction
- [ ] Project Rainier utilization rates
- [ ] Project LEO satellite deployment pace vs July 2026 FCC deadline
- [ ] LEO competitive traction vs [[Starlink]]

---

## Short interest history (quarterly)

| Quarter | SI % float | Stock | Note |
|---------|------------|-------|------|
| **Q1 2026** | **0.76%** | ~$230 | Rose from 70.6M to 73.[[3M]] shares |
| Q4 2025 | 0.73% | $— | |
| Q3 2025 | — | $— | |
| Q2 2025 | — | $— | |

See [[Short interest]] for interpretation framework.

---

## Q4 2025 earnings (Feb 5, 2026)

**Strong beat on revenue and AWS, EPS slight miss, capex shocked the Street:**

| Metric | Actual | Expected |
|--------|--------|----------|
| Revenue | **$213.4B** | $211.3B |
| EPS | $1.95 | $1.97 (miss) |
| YoY revenue | +14% | — |
| AWS revenue | **$35B** (+24%) | +21.4% |
| AWS growth | Fastest in 13 quarters | — |
| AWS backlog | **$244B** (+40% YoY, +22% QoQ) | — |
| Custom chips run rate | **$10B** (triple-digit YoY growth) | — |
| FY 2025 revenue | **$716.9B** (+12% YoY) | — |
| FY 2025 capex | $131.8B | — |
| **2026 capex guidance** | **$200B** | **$146.6B** |

**Custom silicon milestone:** Trainium/Inferentia chips hit **$10B annual run rate** — first hyperscaler custom chip business at this scale.

**Jassy commentary:** "With such strong demand for our existing offerings and seminal opportunities like AI, chips, robotics, low earth orbit satellites, we expect to invest about $200B in capital expenditures across Amazon in 2026." Spending "predominantly" goes to AWS.

**Q1 2026 guidance:** Revenue $173.5B-$178.5B (+11-15% YoY), roughly in line.

**Stock reaction:** -10%+ after hours on $200B capex shock (37% above Street).

---

## Debt profile

$68.8B face value outstanding (Dec 2025), weighted-average life 14.1 years. Rated AA/AA-/A1 (Moody's positive outlook). May 2021 $18.5B deal set record for lowest-ever corporate bond spread. New shelf registration (S-3ASR) filed Feb 2026 signaling more issuance. $30B CP program, $15B revolver, $5B short-term revolver — all undrawn. See [[Amazon bonds]] for full inventory.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | AMZN (NASDAQ) |
| Market cap | ~$2.2T |
| Revenue (FY 2025) | **$716.9B** |
| AWS revenue (Q4 ann.) | ~$140B/year |
| AWS backlog | **$244B** |
| Custom chips run rate | **$10B** |
| AI capex (2025) | $131.8B |
| **AI capex (2026 guided)** | **$200B** |
| P/E | ~40x |
| Long-term debt | $68.8B face (Dec 2025). See [[Amazon bonds]] |
| Short interest | **0.76%** (Jan 2026) |

*Updated 2026-02-10*

## Related

- [[Anthropic]] — $8B investor, primary cloud partner
- [[Adept]] — acqui-hired team (June 2024), now Amazon AGI SF Lab
- [[NVIDIA]] — chip supplier, NVLink Fusion partner
- [[Marvell]] — Trainium design partner
- [[TSMC]] — foundry for Trainium3 (3nm)
- [[Google]] — hyperscaler competitor
- [[Microsoft]] — hyperscaler competitor
- [[Meta]] — hyperscaler competitor
- [[AI hyperscalers]] — peer category
- [[Hyperscaler chip roadmap]] — custom silicon context
- [[Nuclear power for AI]] — power strategy
- [[Saks Global]] — $475M equity investment (wiped in bankruptcy)
- [[Saks-Neiman merger]] — the deal Amazon backed
- [[Saks bankruptcy]] — Jan 2026, flagship collateral fight
- [[Minority investor subordination]] — consent rights failed in distress
- [[AT&T]] — Project LEO satellite broadband partner
- [[AST SpaceMobile]] — AT&T's direct-to-cell partner (different from LEO)
- [[Globalstar]] — Apple's satellite partner, competitor
- [[Starlink]] — primary LEO broadband competitor
- [[Blue Origin]] — Bezos-owned, Project LEO launch provider
- [[Satellite primer]] — industry context
- [[Amazon bonds]] — $68.8B bond inventory (AA, record-low spreads)
