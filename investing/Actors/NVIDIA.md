---
aliases: [NVDA]
---
#actor #fabless #ai #gpu

NVIDIA — dominant AI accelerator company with hardware + software moat. First semiconductor company to cross $100B revenue (2025).

---

## Leadership

| Role | Name | Background |
|------|------|------------|
| President, CEO & Chair | [[Jensen Huang]] | Co-founder (1993). Net worth ~$164B (Jan 2026). IEEE Medal of Honor 2026. |
| CFO | Colette Kress | EVP & CFO since 2013. Ex-[[Microsoft]], [[Cisco]]. Prominent female CFO. |
| EVP Operations | Debora Shoquist | Joined 2007. Supply chain, manufacturing. |
| CTO | Michael Kagan | Chief Technology Officer. |
| General Counsel | Tim Teter | EVP, General Counsel & Secretary. |
| EVP Worldwide Field Ops | Jay Puri | Sales and field operations. |

---

## Board of Directors

| Name | Role | Background |
|------|------|------------|
| [[Jensen Huang]] | Chair & CEO | Founder |
| Stephen Neal | Lead Independent Director | Former [[Cooley LLP]] CEO and Chairman. |
| Harvey C. Jones | Director | Managing partner, Square Wave Ventures. |
| Melissa B. Lora | Director | Former President, Taco Bell International. |
| Brooke Seawell | Director | Venture partner, New Enterprise Associates. |
| Aarti Shah | Director | Former CIO, [[Eli Lilly]]. |
| Mark Stevens | Director | Managing partner, S-Cubed Capital. Early NVIDIA investor. |
| Dawn Hudson | Director | Former CEO, Academy of Motion Picture Arts. Ex-[[PepsiCo]]. |

*10 directors. Recent departures: Ellen Ochoa (Aug 2025), Persis Drell (Jan 2026, $26M stock).*

---

## 2025 milestone ([[Gartner]], Jan 2026)

| Metric | Value |
|--------|-------|
| 2025 revenue | >$100B (first semi company ever) |
| Lead over Samsung | +$53B |
| AI semi market share | Dominant |

NVIDIA now larger than [[Samsung Semiconductor]] by $53B — unprecedented dominance.

Context: Total 2025 semiconductor industry = $793B (+21% YoY). AI chips = ~1/3 of total. NVIDIA captures majority of AI semi spend.

---

## Financials

### Annual (10 years, fiscal year ends Jan)

| FY | Revenue | Net Income | EPS | Stock Price |
|----|---------|------------|-----|-------------|
| 2016 | $5.0B | $0.6B | $0.24 | $8 |
| 2017 | $6.9B | $1.7B | $0.64 | $27 |
| 2018 | $9.7B | $3.0B | $1.17 | $59 |
| 2019 | $11.7B | $4.1B | $1.56 | $36 |
| 2020 | $10.9B | $2.8B | $1.10 | $59 |
| 2021 | $16.7B | $4.3B | $1.73 | $130 |
| 2022 | $26.9B | $9.8B | $3.85 | $235 |
| 2023 | $27.0B | $4.4B | $0.17 | $145 |
| 2024 | $60.9B | $29.8B | $1.19 | $490 |
| 2025 | $130.5B | $72.9B | $2.94 | $135 |
| **2026** | **$215.9B** | **$120.1B** | **$4.90** | **$196** |

*Source: Company filings. Stock price = fiscal year-end close (Jan). Prices adjusted for 10:1 split (Jun 2024). FY2023 was crypto hangover. FY2026 = first $200B revenue year for any semiconductor company.*

---

## Core thesis

NVIDIA's moat isn't just GPUs — it's [[CUDA moat|CUDA]], the software ecosystem that locks in AI developers. Hardware can be challenged; rebuilding a decade of software tooling cannot.

---

## Charts

![[nvda-90d.png]]

![[nvda-vs-smh.png]]
*[[Semiconductors|SMH]]*

![[nvda-fundamentals.png]]

---


![[nvda-employees-chart.png]]
*Headcount: 36,000 (2025) — up 21.6% YoY*

## Key strengths

- CUDA ecosystem: 10+ years of libraries, tools, developer knowledge
- AI training dominance: >90% market share in data center AI
- Vertical integration: Hardware + software + networking (Mellanox)
- Customer lock-in: Switching costs are software, not silicon
- Infrastructure expansion: Acquiring layers competitors depend on (see below)

---

## Manufacturing relationships

| Foundry | Relationship |
|---------|--------------|
| [[TSMC]] | Primary — locks capacity at leading edge |
| [[Samsung]] | Secondary — some legacy nodes |

NVIDIA + [[Apple]] locking [[TSMC]] 2nm capacity forces [[AMD]] and others to alternatives.

---

## Competitive position

| Competitor                          | Threat level | Notes                                 |
| ----------------------------------- | ------------ | ------------------------------------- |
| [[AMD]]                             | Rising       | NodAI acquisition, software improving |
| [[Intel]]                           | Low          | Far behind on AI accelerators         |
| Custom silicon ([[Google]] TPU, [[Amazon]]) | Medium       | Hyperscalers building own chips       |

### TPU catching up (Jan 2026)

![[tpu-vs-nvidia-tflops.png]]
*[[Google]] TPU. Source: [[SemiAnalysis]] — [TPUv7: Google Takes a Swing at the King](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)*

| Chip | Release | BF16 TFLOPs |
|------|---------|-------------|
| A100 | Jun 2020 | ~312 |
| H100 | Jun 2022 | ~1,000 |
| GB200 | Jun 2025 | ~2,500 |
| TPU v7 | Dec 2025 | ~2,340 |

TPU v7 reaches 94% of GB200 performance — first time Google has achieved near-parity. Previous TPU generations were 2-3x behind NVIDIA flagships. However:
- CUDA ecosystem still dominant
- GB200 shipping at scale; TPU v7 constrained by CoWoS
- Vera Rubin (H2 2026) will extend lead again

---

## Moat expansion strategy

NVIDIA actively acquires infrastructure that competitors also depend on:

| Acquisition | What | Why it matters |
|-------------|------|----------------|
| [[Groq]] ($20B, Dec 2025) | LPU inference chips | Largest deal ever. 10x faster, 1/10th energy for inference. Entering non-GPU market. |
| SchedMD (Dec 2025) | SLURM workload scheduler | AMD/Intel users rely on it |
| Run:AI | Kubernetes orchestration | AI cluster management |
| Mellanox | Networking | AI cluster connectivity |

Pattern: buying "neutral" infrastructure + potential competitors, raising switching costs beyond CUDA.

---

## [[China]] market dynamics

See [[Export controls]] for full context.

Before controls: 95% [[China]] AI chip share
After controls: ~0% (tight restrictions)
H200 approved (Jan 14, 2026): Section 232 proclamation formalizes "managed access" framework. NVIDIA can sell H200 to [[China]] with conditions.

Section 232 tariff (Jan 14, 2026):

| Detail | Value |
|--------|-------|
| Rate | 25% on advanced AI chips (H200, MI325X) |
| Authority | Section 232 (not IEEPA — firmer legal ground) |
| Revenue | $4-6B/year → funds domestic manufacturing |
| Named future chips | Rubin R100 (3nm/HBM4), AMD MI455X |
| Exemptions | US data centers, R&D, startups, public sector |

[[China]] sales conditions:

| Requirement | Detail |
|-------------|--------|
| Framework | "Managed access" (replaces "presumption of denial") |
| Volume cap | ≤50% of US domestic sales |
| Verification | Every shipment → US third-party lab |
| Routing | [[Taiwan]] → US → [[China]] (detour required) |
| First shipment | 82,000 H200 GPUs, mid-February 2026 |
| Tariff bearer | NVIDIA (can pass to Chinese buyers) |

NVIDIA reaction: "Applauds President Trump's decision to allow America's chip industry to compete."

Escalation risk: Tariff could rise to 100% if domestic manufacturing milestones not met. Phase 3 (Jun 2027) folds in legacy chips.

[[China]] response: Global Times dismissed as "discriminatory" — targeted specifically at [[China]] vs other trading partners.

Jan 14, 2026 — [[China]] blocks H200:

| Development | Detail |
|-------------|--------|
| Customs directive | Agents told H200 chips "not permitted" |
| Company meetings | Tech firms summoned, told not to purchase "unless necessary" |
| Exceptions | "Special circumstances" only — university R&D labs |
| Source quote | "Wording so severe that it is basically a ban for now" |

Strategic logic: Beijing needs domestic chip demand to fund Huawei [[Ascend]] development. H200 was allowed initially because [[Ascend]] threatens "dominance of American tech stack" — now blocking it to force reliance on Chinese alternatives.

US strategic calculus:
- H200 is "previous gen" — B200 (Blackwell) is 3.1x faster
- Rubin (2026) widens gap further
- Release old tech while monopolizing cutting edge
- Build ecosystem defense against Chinese chip makers
- H200 approved because US expects [[Huawei]] to produce millions of 910C units in 2026

Chinese competition:
- Huawei 910C: 76% of H200 compute, 2/3 memory bandwidth
- Huawei CloudMatrix 384 performs as well as NVL72 (Blackwell)
- US estimates Huawei can make millions of [[Ascend]] 910C in 2026 (vs 200K in 2025)
- Cambricon, Hygon even further behind
- Even "outdated" H200 beats all Chinese alternatives

Jan 23, 2026 — Jensen Huang planning [[China]] visit:

Jensen Huang plans to visit [[China]] in coming days ahead of mid-February Lunar New Year. Context:
- Reports that Chinese officials told major tech firms to "begin preparing orders" for H200
- First H200 shipment expected mid-February (82K GPUs) — timing aligns with visit
- Chinese regulators haven't officially approved H200 imports on their side
- Unclear whether Beijing's Jan 14 "effective ban" directive has softened
- Stock +1.6% on Jan 23 on the [[China]] order preparation reports

*Source: CNBC, Jan 23 2026*

Feb 6, 2026 — Bloomberg explainer update:

- [[China]] restricted H20 chip in Aug 2025 — security risk of embedding US tech in sensitive systems
- Beijing will allow limited H200 access but block use in military, government agencies, critical infrastructure
- Paired purchase mandate: Chinese customers must also buy domestic chips alongside NVIDIA purchases — protects [[Huawei]], [[Cambricon]], [[Moore Threads]]
- [[China]] chip market = $229B annual revenue (1/3 of global total) in 2024
- Jensen expects Chinese AI chip spending to reach $50B/year within 2-3 years
- [[Moore Threads]], MetaX surged several-fold in IPOs — bets on Beijing self-sufficiency policy
- Bernstein: H200 still significantly better than Chinese alternatives
- [[David Sacks]] (White House AI Czar) backed Huang's arguments in Washington

*Source: Bloomberg, Feb 6 2026*

Dual ecosystem forming:
- Training: NVIDIA (high barriers)
- Inference: Chinese chips (cost sensitive, volume)

---

## Ecosystem control (bear case)

The allegation: NVIDIA controls both supply AND demand, creating a self-sustaining cycle.

Supply side:
- Locks TSMC wafers before demand exists (like booking airplane before selling tickets)
- Jensen knows exactly what numbers Wall Street expects
- "Beat and Raise" requires ever-larger tricks as company grows

Demand side — Neocloud financing:
NVIDIA finances GPU buyers who absorb inventory when needed:

| Company | NVIDIA role | [[Microsoft]] ties |
|---------|-------------|----------------|
| [[CoreWeave]] | Investor, priority allocation | 65% revenue from MSFT |
| [[Lambda Labs]] | Financing involved | — |
| [[IREN]] | Deal facilitation | [[Microsoft]] ties |
| [[Nebius]] | Deal facilitation | [[Microsoft]] ties |
| [[Scale AI]] | — | [[Microsoft]] ties |

The phone call model: "Take the chips now — I'll assign you clients later."

Evidence of idle inventory:
- Satya (Nov 2025): "chips sitting in inventory that I can't plug in"
- [[Elon Musk]]: "racks of GPUs waiting for datacenters to be built"

The question: Are neoclouds real businesses or NVIDIA inventory management vehicles?

See [[Neocloud financing]] for full analysis.

---

## Gray market [[China]] revenue

The reality: NVIDIA's "zero [[China]] forecast" is public narrative, but Chinese companies are major buyers — this is current tailwind, future risk.

Chinese customers are huge (2024 Hopper shipments, [[Omdia]]):

| Customer | GPUs (000s) | Notes |
|----------|-------------|-------|
| [[Microsoft]] | ~485K | \#1 overall |
| ByteDance | ~250K | \#2 overall, Chinese |
| Tencent | ~220K | \#3 overall, Chinese |
| Meta | ~200K | |
| [[Tesla]]/[[xAI]] | ~170K | |
| [[Amazon]] | ~130K | |
| [[Google]] | ~100K | |

ByteDance + Tencent = ~470K Hopper GPUs in 2024 — nearly as much as [[Microsoft]], despite "export controls."

Jensen quotes (Dec 2025 Bloomberg interview):
- "Our forecast for [[China]] is zero. All of our guidance starts at zero."
- "The Chinese market is very large this year. My guess is probably about $50 billion."

SEA chip flows (Jan-Oct 2025):

| Route | Imports | Notes |
|-------|---------|-------|
| Malaysia | $12B | Largest corridor |
| Singapore | $7B | Removed from geographic reporting |
| Thailand | $3B | Growing |
| Indonesia | $1.2B | Growing |
| SEA Total | $23B | 17.5% of DC revenue |

How to interpret this:

| Lens | Interpretation |
|------|----------------|
| Bull | Extra ~15-20% revenue; if legalized, converts to clean sales |
| Bear | Revenue NVIDIA can't acknowledge; could vanish if crackdown succeeds |
| Neutral | Legal [[China]] sales wouldn't *increase* revenue — just relabel it |

The "zero forecast" game: Creates upside surprise optics for investors when gray market revenue is already baked in.

Embedded risks:
- Legal exposure if NVIDIA found complicit (US District Court charges, Jan 2026)
- Revenue dependent on enforcement staying lax
- Accounting opacity (geographic reporting changed twice in <1 year)
- Investor trust risk if it becomes scandal

Post-[[DeepSeek]] shift: Chinese firms now building DCs directly in SEA instead of smuggling to mainland — dozens of data centers across Malaysia, Thailand, Indonesia. Chips stay "in SEA" technically.

See [[SEA chip diversion]] for full analysis.

---

## Key vulnerabilities

- CUDA moat eroding if alternatives mature (ROCm, Triton, JAX)
- Customer concentration in hyperscalers who want alternatives
- Valuation assumes continued dominance
- Supply constrained by [[TSMC]] and [[Advanced packaging|CoWoS]]
- [[China]] revenue capped by export controls (but H200 + gray market provide partial recovery)
- Gray market dependence — ~15-20% revenue through SEA, legal/reputation risk (see above)
- Jensen admits 3 years to build datacenter — selling more GPUs than can be deployed
- 36k employees hold $630B in RSUs ($17.5M per person average)
- Ecosystem control — financing neoclouds to absorb inventory (see above)

---

## Deployment vs shipment risk

"Shipped" ≠ "Deployed" — a growing gap between NVIDIA's revenue recognition and actual GPU utilization.

Key data points:
- Satya (Nov 2025): [[Microsoft]] has "chips sitting in inventory that I can't plug in"
- Gavin Baker (Atreides): Blackwell deployment only truly started Aug-Oct 2025
- Jensen (Dec 2025): Building a major AI DC takes ~3 years (permitting, construction, power)

The math problem:
- 10M+ Blackwell/Rubin chips targeted by end of 2026
- Requires 17-23GW of power capacity
- Jensen: 6M GPUs "shipped" by Oct 2025
- But Blackwell deployment only started 3-4 months prior

Blackwell deployment challenges:
| Factor | Change from Hopper |
|--------|--------------------|
| Cooling | Air → liquid |
| Rack weight | 1,000 lbs → 3,000 lbs |
| Power per rack | 30 kW → 130 kW |
| Legacy DC retrofit | Extremely difficult |

Bear case (Kakashiii analysis):
- Bill-and-hold arrangements may allow revenue recognition on undeployed GPUs
- Customers stockpiling in CIP (Construction in Progress) accounting
- "Buy Now, Deploy Later" pattern — customers FOMO order GPUs before DCs ready
- [[Meta]] example: ~400K Blackwell GPUs purchased, stored waiting for Prometheus (1GW, 2026)

Why it matters:
- Revenue quality question — are "shipments" actually utilization?
- Depreciation spike coming when CIP assets activate
- If DC buildout slows, GPU demand could hit a wall
- Creates [[GPU deployment bottleneck]]

See [[GPU deployment bottleneck]] for full analysis.

---

## Short interest history (quarterly)

| Quarter | SI % float | Stock | Note |
|---------|------------|-------|------|
| Q1 2026 | 1.1% | ~$140 | $5T market cap, fell from 264M to 257M shares |
| Q4 2025 | 1.15% | $— | |
| Q3 2025 | — | $— | |
| Q2 2025 | — | $— | |

Pattern: Like [[TSMC]], SI stayed low despite parabolic AI run. Shorts capitulated.

See [[Short interest]] for interpretation framework.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Stock price | ~$196 |
| Market cap | ~$4.8T |
| FY2026 revenue | $215.9B (+65% Y/Y) |
| FY2026 net income | $120.1B |
| FY2026 FCF | $96.6B |
| Q1 FY27 guide | $78B ±2% (beat $72.6B est.) |
| AI training share | >90% |
| Primary foundry | [[TSMC]] |
| Packaging | [[TSMC]] CoWoS (constrained) |
| Supply commitments | $95.2B (up from $50.3B end Q3) |
| Cash + securities | $62.6B |
| Inventories | $21.4B |
| Short interest | 1.1% (Jan 2026) |

*Updated 2026-02-25*

![[nvda-price-chart.png]]

![[nvda-fundamentals.png]]

---

## Recent developments (Jan 2026)

Jan 27-29 — DeepSeek selloff + allegations:
- Chinese AI breakthroughs triggered ~$1T tech selloff on Jan 27
- NVIDIA alone lost ~$600B in single session
- Two Chinese models matched/surpassed US rivals at fraction of cost
- Stock fell from $5T+ record (Jan 8) to ~$190 ($4.7T cap)

Moolenaar letter (Jan 28):
- [[John Moolenaar]] (R-MI), chair of House Select Committee on [[China]], sent letter to Commerce Secretary Lutnick
- Documents obtained from NVIDIA show technical assistance helped [[DeepSeek]] achieve training efficiency
- Internal docs: "DeepSeek-V3 requires only 2.788M H800 GPU hours for its full training — less than what US developers typically require"
- Moolenaar acknowledged NVIDIA treated DeepSeek "as a legitimate commercial partner" (no military indication at time)
- But argues: if even NVIDIA "cannot rule out military use," rigorous export licensing essential
- NVIDIA response: "China has more than enough domestic chips for all of its military applications... it makes no sense for the Chinese military to depend on American technology"

H200 China orders confirmed (late Jan):
- Reuters: Chinese tech firms ordered 2M+ H200 GPUs for 2026
- Orders placed after Trump administration approved China sales
- Aligns with Jensen's planned China visit ahead of Lunar New Year
- First shipment still expected mid-February (82K GPUs)

Next earnings: Feb 25, 2026

NVIDIA hits $5 trillion (Jan 8, 2026):
- First company ever to reach $5T market cap
- Passed [[Apple]], [[Microsoft]], Alphabet
- AI dominance + strategic dealmaking

Intel partnership (Jan 2026):
- $5B investment in Intel stock @ $23.28/share (~217.4M shares)
- FTC approved
- Joint development of custom data center + PC products
- NVLink integration with Intel architectures
- Potential Intel Foundry relationship
- EMIB packaging as CoWoS alternative
- US manufacturing hedge (reduce TSMC dependency)

See [[NVIDIA-Intel partnership]] for full analysis.

Baseten investment ($150M, Jan 20):
- $150M into AI inference startup [[Baseten]] as part of $300M round at $5B valuation
- Round co-led by [[IVP]], [[CapitalG]] (Alphabet's growth fund)
- Baseten = "AWS for inference" — serves [[Cursor]], [[Notion]]
- Continues pattern of investing in inference customers (see [[NVIDIA as kingmaker]])
- Same week as Groq deal ($20B) — NVIDIA now backing multiple inference plays

CES 2026 announcements:
- Vera Rubin NVL72: 5x inference vs Blackwell, 10x lower cost/token, H2 2026
- Alpamayo: Open reasoning models for autonomous vehicles
- Cosmos AI: Physics simulation foundation model
- Full-stack robotics platform
- Mercedes partnership (Alpamayo in 2025 CLA)
- [[Archer Aviation]] partnership (IGX Thor for eVTOL)

See [[CES 2026]] for event details.

---

## Meta multiyear chip deal (Feb 17, 2026)

[[Meta]] signed multiyear pact to deploy "millions" of NVIDIA processors — Blackwell, Vera Rubin, Grace/Vera CPUs, and networking equipment. Meta becomes first large DC operator to use Grace CPUs in standalone servers, encroaching on [[Intel]]/[[AMD]] CPU territory. NVIDIA's Ian Buck: Grace delivers 2x performance/watt on backend workloads. No dollar figure disclosed. Meta (~9% of NVIDIA revenue) also developing in-house chips and exploring [[Google]] TPUs — deal signals NVIDIA retaining dominant share. [[AMD]] fell 3%+ on the news.

*Source: [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-17/meta-deepens-nvidia-ties-with-pact-to-use-millions-of-chips)*

---

## Jensen Huang defends AI capex (Feb 2026)

Two Bloomberg interviews in one week — Huang pushing back on capex fears and software selloff:

### Feb 4 — Software selloff response (Cisco event)

Called AI-driven software stock selloff "the most illogical thing in the world." Argued software products are tools that AI will use, not replace: "Would you use a screwdriver or invent a new screwdriver?"

Said [[NVIDIA]] itself adopted AI tools extensively — result was freeing employees to focus on core work (chip design, systems), not headcount reduction. Directly counters narrative that [[Anthropic]] tools will destroy software companies.

*Source: Bloomberg (Ian King), Feb 4 2026*

### Feb 6 — AI capex is sustainable (CNBC)

| Claim | Detail |
|-------|--------|
| Buildout timeline | 7-8 years of AI infrastructure spending ahead |
| Demand | "Just incredibly high" |
| Idle capacity | No infrastructure sitting idle (unlike dot-com) |
| Revenue quality | [[Anthropic]], [[OpenAI]] generating profitable revenue |
| Big Tech reaction | Amazon, Alphabet, Meta, Microsoft lost ~$1T combined on capex fears |
| 2026 Big Tech AI capex | ~$650B total |

Context: Earnings week saw Amazon ($200B), Alphabet ($175-185B), Meta ($115-135B) all guide above Street on 2026 capex. Investors panicked. Huang's response: demand justifies spend, customers would do even better with more data centers.

Directly contradicts the "deployment vs shipment" bear case in this note — Huang claims no idle capacity exists.

*Source: Bloomberg (Ian King), Feb 6 2026*

---

## OpenAI inference concerns (Feb 2026)

[[Reuters]] exclusive revealed tension with biggest AI customer:

| Issue | Detail |
|-------|--------|
| Customer | [[OpenAI]] |
| Problem | Inference speed for specific workloads |
| Affected | [[Codex]] (coding), agent-to-agent comms |
| Scale | ~10% of OpenAI's inference compute needs |

What OpenAI wants: SRAM-heavy chips (memory on silicon) for faster inference. Traditional GPUs use external memory → slower fetch times.

Alternatives OpenAI explored:
- [[AMD]] — purchased GPUs
- [[Cerebras]] — commercial deal signed (Jan 2026)
- [[Groq]] — talks shut down after NVIDIA acquisition

The $100B investment:
- NVIDIA proposed investing up to $100B in OpenAI (Sept 2025)
- Expected to close "within weeks" — still in negotiations
- Jensen Huang (Bloomberg): Investment "was never a commitment"
- Huang (CNBC, Feb 3): "There's no drama involved"

Sam Altman response: NVIDIA makes "the best AI chips in the world." OpenAI hopes to remain "gigantic customer for a very long time."

NVIDIA's defensive moves:
- Acquired [[Groq]] IP for $20B (Dec 2025) — hired chip designers
- Non-exclusive licensing deal — Groq pivoting to cloud software
- Pattern: buy potential alternatives before customers can switch

Stock reaction (Feb 3): Modest; market treating as manageable. Inference is smaller market than training where NVIDIA dominates.

*Updated 2026-02-04*

---

## Recent developments (Dec 2025)

Groq acquisition details:
- Paid 3X Groq's September valuation (~$20B deal)
- Non-exclusive licensing agreement — Groq operates independently
- Jonathan Ross (founder) + Sunny Madra (president) joining NVIDIA
- Simon Edwards becomes new Groq CEO; GroqCloud continues
- Strategic hedge against DRAM prices — Groq uses in-chip SRAM, not [[HBM]]
- Political angle: [[David Sacks]] promoted Groq, Chamath banking $4B, Jensen got AI Diffusion framework canceled + H200s approved for [[China]]

Revenue dominance ([[UBS]] Research):
- Hopper (previous gen) generates more revenue than ALL compute peers combined (AMD, [[Broadcom]], [[Marvell]])
- "Not a cycle. A structural monopoly with a roadmap"
- Blackwell, Rubin, Feynman not even shipping at scale yet
- $500B+ Blackwell + Rubin revenue through CY2028 (booked so far)
- 5X Hopper's lifetime revenue
- 6 million Blackwell GPUs shipped
- [[Morgan Stanley]]: NVDA top stock pick for 2026

CUDA moat strengthening:
- Devs openly admitting they can't reproduce results off CUDA
- "Once your stack depends on B200 + CUDA + Torch, [[Google]] TPU/JAX is a downgrade"
- Andrew Feldman: CUDA wasn't the moat — the "mental moat" (perception that only NVIDIA works) was

GPU price increases (Q1 2026):
- AMD + NVDA raising graphics card prices 10-20%
- AMD notified partners: $10 increase per 8GB VRAM
- Driven by DRAM price explosion ($6 to $30 in 6 months)

SchedMD acquisition (Dec 15):
- Acquired Slurm developer (HPC/AI workload manager)
- Continuing vendor-neutral open-source distribution

CES 2026 preview (Jan 6):
- Blackwell Ultra ramp update
- Rubin architecture roadmap (next-gen after Blackwell)
- Jensen Huang keynote

Major orders:
- ByteDance $14B NVIDIA order for 2026 (H200s, HBM3E 8Hi)
- [[Oracle]] RPO increased $68B to $523B — driven by Meta, NVIDIA commitments
- Continued hyperscaler demand

Foundry diversification:
- Exploring [[Samsung]] as second foundry (post-Groq deal)
- Would reduce TSMC dependency

[[RTX]] PRO 5000:
- Blackwell workstation GPU: 72GB GDDR7, 2,142 TOPS

[[Southeast Asia]] chip surge:
- [[Taiwan]] chip exports to Indonesia at all-time high
- $400M+ of NVIDIA chips to Indonesia in November alone
- 26,900% growth vs November 2023
- Indonesia leads SEA imports (~$12B Jan-Oct 2025)

---

## Market expectations

Priced in:
- Continued AI training dominance
- CUDA moat holds
- [[TSMC]] supply secured

Not priced in (potential surprises):
- AMD software reaches parity (CUDA moat cracks)
- Hyperscaler defection to custom silicon
- [[TSMC]] packaging constraints limit shipments

Market positioning (Dec 2025):
- Michael Burry: put positions disclosed Nov 2025, calling for pics of warehoused GPUs
- Insider selling: $496M in 90 days, zero buying
- Sentiment indicator — insiders cashing out at highs
- Ed Zitron: questioning why NVIDIA backstopping $26B for Lambda/[[Oracle]]/CoreWeave
- Stock +37% YTD vs [[Micron]] +229%, SK Hynix +220% — memory outperforming GPU

---

## For theses

- [[Long TSMC]] — NVIDIA locks TSMC capacity, reinforces moat
- [[Long memory]] — every GPU needs [[HBM]] from SK Hynix/Samsung
- [[Long OSAT and test equipment]] — GPU testing drives [[ASE]]/[[Cohu]] demand

---

## Q4 FY2026 earnings (Feb 25, 2026)

First $200B revenue year. Q4 revenue $68.1B (+73% Y/Y, +20% Q/Q), beating $66.2B consensus. Data Center $62.3B (+75% Y/Y) = 91.5% of total. Non-GAAP EPS $1.62 (beat $1.53). Gross margins recovered to 75.0% after H20 charges depressed H1.

| Segment | Q4 FY26 | Y/Y |
|---------|---------|-----|
| Data Center | $62.3B | +75% |
| Gaming & AI PC | $3.7B | +47% |
| Pro Visualization | $1.32B | +159% |
| Automotive | $604M | +6% (miss) |

**Q1 FY27 guidance: $78B ±2% vs $72.6B consensus (+7.4% beat).** Zero China DC compute revenue assumed. SBC reclassification starting Q1 will mechanically reduce non-GAAP EPS by ~$0.08/quarter.

**Vera Rubin:** First samples shipped to customers this week. Production H2 2026. 10x token cost reduction vs Blackwell. 10x perf/watt. Six new chips. First deployers: [[AWS]], [[Google]], [[Microsoft]], [[Oracle]], [[CoreWeave]], [[Lambda Labs]], [[Nebius]].

**Blackwell:** Supply commitments $95.2B (up from $50.3B Q3). Expects to EXCEED $500B combined Blackwell+Rubin manufacturing CY2025-2026. Blackwell Ultra: 50x perf, 35x lower cost for agentic AI vs Hopper.

**Networking:** $10.98B (+263% Y/Y) on NVLink and Spectrum-X.

**Customer mix:** Hyperscalers "slightly over 50%" of DC revenue; growth led by non-hyperscaler customers (AI model makers, enterprises, sovereigns).

**Supply chain diversification:** Blackwell GPUs at [[TSMC]] Arizona. Rack systems at new [[Foxconn]] Mexico plant. Memory shortage headwind to Gaming.

**FY26 totals:** Revenue $215.9B, net income $120.1B, FCF $96.6B, shareholder returns $41.1B, $17.5B invested in private companies.

Jensen's "1000x manifesto" (final 7 min of call): Old compute = $350B/year of static "DVD-like" software. AI = real-time, generative, 1,000x more valuable → $350B × 1,000 = massive TAM. "The need is a lot more than $700 billion." See [[Jensen 1000x compute thesis]].

Other Jensen quotes: "Our strategy is to introduce an entirely new AI infrastructure every single year." / OpenAI deal: "We continue to work with OpenAI toward a partnership agreement and believe we are close."

**[[Gene Munster]] ([[Deepwater Asset Management]]) post-call:** Accelerating growth + flat stock mirrors [[Apple]]'s beat-and-fade pattern. Flagged [[Colette Kress]]'s supply/demand equilibrium confirmation as paradoxically negative — at equilibrium, "the numbers you see are what you get," removing the dream-bigger optics of supply constraints. CY2027 Street estimate of 28% "too conservative" — expects 50%+. Deepwater owns NVDA. Cited using [[OpenClaw]] and Claude Code agents as evidence AI utility has had "a meaningful step forward."

Stock: +3.5% AH initially, settled ~+0.7%. 63 analysts: 60 Buy. Consensus PT $261.54.

---

## February 2026: India AI summit withdrawal

[[Jensen Huang]] withdrew from the [[India AI Impact Summit 2026]] on Feb 14, citing "unforeseen circumstances." He had been expected to deliver a keynote at the first [[Global South]] AI summit. The absence was notable given the scale of AI investment commitments announced at the event.

---

## Related

- [[Jensen Huang]] — CEO and founder
- [[TSMC]] — primary foundry
- [[Intel]] — partner ($5B investment, Jan 2026)
- [[NVIDIA-Intel partnership]] — strategic collaboration
- [[SK Hynix]] — [[HBM]] supplier
- [[Samsung]] — secondary foundry, [[HBM]] supplier
- [[AMD]] — competitor (GPU/AI)
- [[Groq]] — acquired (inference ASICs, $20B backdoor acquisition)
- [[AI consolidation]] — Groq deal exemplifies Big Tech acqui-hire pattern
- [[CUDA moat]] — key competitive advantage
- [[Advanced packaging]] — constraint (CoWoS)
- [[Export controls]] — [[China]] market constraint
- [[Long NVIDIA]] — thesis
- [[Long memory]] — thesis ([[HBM]] demand)
- [[Stacy Rasgon]] — Bernstein analyst (Outperform, $275 PT)
- [[Hans Mosesmann]] — Rosenblatt analyst (first $1K+ PT)
- [[NVIDIA as kingmaker]] — concept (strategic investments)
- [[Jevons Paradox]] — concept (efficiency → more demand)
- [[Training-inference convergence]] — concept (unified architectures win)
- [[Foundry Wars]] — manufacturing context
- [[GPU deployment bottleneck]] — demand risk (shipped ≠ deployed)
- [[Power constraints]] — infrastructure constraint
- [[Neocloud financing]] — ecosystem control (bear case)
- [[CoreWeave]] — NVIDIA-backed neocloud
- [[Lambda Labs]] — NVIDIA-financed neocloud
- [[SEA chip diversion]] — gray market [[China]] revenue (tailwind + risk)
- [[Southeast Asia]] tech race — Chinese DC buildout destination
- [[Meta]] — "multigenerational" deal: GPUs (Blackwell + Rubin) + CPUs (Vera) + networking. Full-stack standardization, millions of chips. Pushes into [[Intel]]/[[AMD]] CPU turf (Feb 2026)
- [[ByteDance]] — \#2 GPU customer (~250K Hopper, 2024)
- [[Tencent]] — \#3 GPU customer (~220K Hopper, 2024)
- [[Archer Aviation]] — eVTOL partner (IGX Thor, CES 2026)
- [[Baseten]] — inference infrastructure investment ($150M, Jan 2026)
- [[CES 2026]] — Vera Rubin, Alpamayo, Cosmos, robotics
- [[DeepSeek]] — Chinese AI lab; technical assistance allegations (Jan 2026)
- [[John Moolenaar]] — House China Committee chair; Jan 2026 investigation
- [[Hyperscaler chip roadmap]] — custom silicon competition (TPU, Trainium, Maia)
- [[India AI Impact Summit 2026]] — [[Jensen Huang]] withdrew Feb 14 ("unforeseen circumstances")
- [[Deepwater Asset Management]] — [[Gene Munster]]'s firm, owns NVDA, Pressure Points podcast
- [[Jensen 1000x compute thesis]] — 1,000x compute demand vs traditional infrastructure (Q4 FY26 call)
