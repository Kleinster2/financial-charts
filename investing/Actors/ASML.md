---
aliases: [ASML]
---
#actor #equipment #wfe #lithography 


Dutch semiconductor equipment company with a monopoly on EUV lithography. ASML is the most critical bottleneck in advanced semiconductor manufacturing. No EUV = no leading edge chips. 20+ years of R&D created an unassailable moat.

| Technology          | ASML position | Alternative             |
| ------------------- | ------------- | ----------------------- |
| [[EUV lithography]] | 100% share    | None                    |
| DUV lithography     | ~85% share    | Nikon, Canon (trailing) |
| High-NA EUV         | 100% share    | None                    |

Every leading edge chip (sub-7nm) requires ASML EUV machines. Period.

![[asml-price-chart.png]]
*ASML (blue) +330% vs WFE peers since 2020. [[KLA]] leads (+800%), [[Lam Research|LRCX]] (+600%), [[Applied Materials|AMAT]] (+450%). ASML trails despite monopoly — reflects different business models (EUV tools vs consumables/services).*

![[asml-fundamentals.png]]
*Quarterly revenue tripled from ~$3B (2020) to ~$10B (Q4 2025). Net income up 7x to ~$3B/quarter. 13 consecutive years of growth.*

---

## Sector correlation

| Sector | ETF | Correlation |
|--------|-----|-------------|
| [[Semiconductors]] | SMH | 0.85 |
| Technology | XLK | 0.76 |
| Industrials | XLI | 0.62 |
| *S&P 500* | *SPY* | *0.71* |

ASML trades as a core Semiconductors name (SMH r = 0.85).

---

## Why the moat is durable

- **20+ years of R&D**: Can't be replicated quickly
- **Supply chain control**: Key suppliers (Zeiss optics, Cymer light source) locked in
- **Institutional knowledge**: Thousands of engineers, decades of iteration
- **Customer co-development**: TSMC, [[Intel]], Samsung helped fund development

---

## High-NA EUV ramp (2024-2026)

**Next-generation EUV with 0.55 numerical aperture (vs 0.33 for Low-NA).**

| Model | Use case | Throughput | Price |
|-------|----------|------------|-------|
| **EXE:5000** | R&D | 185 WPH → 220 WPH | ~$350M |
| **EXE:5200B** | Volume production | 175 WPH → 200 WPH | $350-400M |

**Resolution:** 8nm, enables 1.7x smaller features, 2.9x higher transistor density vs Low-NA.

### Customer shipments

| Customer | Systems | Status | Use case |
|----------|---------|--------|----------|
| [[Intel Foundry Services\|Intel]] | 3× EXE:5000 (R&D), 1× EXE:5200B | EXE:5200B acceptance testing completed Dec 2025 | 14A node, HVM 2027 |
| [[Samsung]] | 1× EXE:5000, 2× EXE:5200B ordered | First EXE:5200B late 2025, second H1 2026 | 2nm logic, Tesla AI chips |
| [[TSMC]] | 1× EXE:5000 | Evaluation only | **Skipping High-NA for A14 (1.4nm)** — may adopt for A10 |
| [[SK Hynix]] | 1× EXE:5200B | Assembled at M16 fab Sep 2025 — industry's first for memory | HBM4/HBM5, next-gen DRAM |

**TSMC's cautious approach:** Senior VP Kevin Zhang confirmed TSMC will skip High-NA for A14 node, continuing with Low-NA EUV + multi-patterning. Maximizing ROI of existing fleet before transitioning.

**Production timeline:** CEO Fouquet expects High-NA HVM 2027-2028. 300,000+ wafers already processed at customer sites.

**High-NA update (Mar 2026):** 500,000 wafers processed, ~80% uptime (target 90% by year-end). Production-ready threshold crossed.

---

## Beyond EUV: Advanced packaging and larger chips (Mar 2026)

ASML is expanding beyond its EUV monopoly into three new vectors under new CTO **Marco Pieters** (promoted Oct 2025, replacing Martin van den Brink after ~40 years). Pieters' background is in ASML software development. Core thesis: chips are moving from flat to multi-level stacked architectures — the "chip skyscraper."

> "We look, not just for the next five years, we look at the next 10, maybe 15 years." — CTO Marco Pieters

**Organizational context (Jan 2026):** ASML reorganized its technology business to prioritize engineering over management roles, aligning with Fouquet's "engineers can be engineers again" push.

### 1. Advanced packaging tools — TWINSCAN XT:260

First product: i-line lithography scanner purpose-built for 3D chip packaging.

| Spec | Value |
|------|-------|
| Model | **TWINSCAN XT:260** |
| Type | i-line lithography scanner |
| Resolution | ~400nm |
| Overlay | Sub-40nm |
| Throughput | **200-270 WPH** |
| Speed advantage | **4x faster** than existing packaging lithography (likely vs [[Canon]] FPA-5520iV) |
| First shipment | Late 2025 |

Engineers are exploring additional machines for stacked chip manufacturing. [[SK Hynix]] plans revealed need for additional machines — SK Hynix is building a **$13B HBM packaging plant** targeting 2027 production.

**Market opportunity:**

| Metric | Value |
|--------|-------|
| Advanced packaging market (2025) | $42-51B |
| Advanced packaging market (2034) | $70-90B |
| ASML target share | 5-10% of tooling over a decade |

**Competition in packaging lithography:**

| Company | Position |
|---------|----------|
| [[Canon]] | i-line incumbent — 187 units shipped last year, 247 projected this year |
| [[Onto Innovation]] | JetStep platform |
| [[Applied Materials]] | Packaging equipment |
| [[KLA]] | Inspection/metrology |

### 2. Expanding reticle limit

ASML plans to determine whether maximum chip size can go beyond the current stamp-sized reticle limit. The existing reticle constraint forces multi-chip packaging solutions — [[NVIDIA]], [[AMD]], and other AI chip designers are hitting this ceiling, driving demand for advanced packaging as a workaround. Removing or expanding the limit could reshape the packaging vs monolithic tradeoff.

### 3. AI-powered machine software

Using AI to speed up machine control software and chip inspection. Aligns with the €1.3B [[Mistral]] investment (Sep 2025) and Pieters' software background.

### Financial context (2025 results)

| Metric | 2025 Actual | 2026 Guidance | 2030 Target |
|--------|-------------|---------------|-------------|
| Revenue | **€32.7B** | €34-39B | €44-60B |
| Gross margin | **52.8%** | 51-53% | 56-60% |
| Net income | **€9.6B** | — | — |
| R&D spend | €2.5B → **€4.7B** | Rising | — |

R&D nearly doubling from €2.5B to €4.7B signals the scale of ambition beyond EUV — packaging tools, reticle expansion, and AI software all require significant engineering investment.

*Source: Reuters exclusive, Mar 2, 2026.*

---

## Key customers

| Customer | Relationship |
|----------|--------------|
| [[TSMC]] | Largest — priority access to new tools |
| [[Samsung]] | Major — needs EUV for leading edge |
| [[Intel Foundry Services]] | Growing — 18A/20A ramp |
| [[SK Hynix]] | First memory customer for High-NA |
| Chinese fabs | Restricted — no EUV allowed |

---

## Mistral AI investment (Sep 2025)

**First-ever AI company investment for ASML.**

| Metric | Value |
|--------|-------|
| Investment | **€1.3B** |
| Stake | ~11% (fully diluted) |
| Mistral valuation | €11.7B ($13.8B) — 2x prior round |
| Round | Series C (€1.7B total) |

**Other investors:** [[NVIDIA]], [[DST Global]], [[Andreessen Horowitz|a16z]], Bpifrance, [[General Catalyst]], [[Index Ventures]], [[Lightspeed Venture Partners|Lightspeed]]

**Purpose:** Integrate AI models across ASML product portfolio, R&D, operations. CFO Roger Dassen joins Mistral Strategic Committee.

---

## [[China]] exposure / risk

### Export controls (tightening)

| Restriction | Status |
|-------------|--------|
| EUV systems | Completely banned |
| Immersion DUV (2100i, 2050i, etc.) | Dutch license required |
| Servicing/parts/software | License required (effective Apr 1, 2025) |
| Metrology/inspection | Added to restrictions |

**Revenue impact:**

| Period | China % of revenue | Notes |
|--------|-------------------|-------|
| Q2 2024 | 49% | Pre-restriction surge |
| Q4 2025 | 36% | Still largest market |
| 2025-2026 guidance | ~20% | "Significantly lower" |

Bank of America: 20% guidance implies 48% YoY decline from China.

### China rare earth retaliation (Oct 2025)

**October 9, 2025:** China issued MOFCOM Notice 2025-61 requiring export licenses when Chinese rare earths make up 0.1%+ of foreign products — first use of "foreign direct product rule" by China.

**ASML response:** CFO Dassen said company "short-term prepared" with inventory, but warned of potential weeks-long shipment delays.

**De-escalation (Nov 2025):** Following Xi-Trump meeting in Busan (Oct 30), China suspended enforcement of rare earth restrictions until November 2026.

### Chinese domestic alternatives

**SMEE (Shanghai Micro Electronics):**
- 600 series: Mass production at 90nm (May 2025)
- 28nm-capable immersion DUV in development
- Gap with ASML: reduced from ~20 years to several years
- EUV prototype targeting functional chips by 2028-2030

**AMIES (SMEE spinoff, Feb 2025):**
- 35% global advanced packaging lithography share
- 90% China domestic market share
- Shipped 500th stepper (Aug 2025)
- Potential standalone IPO path

---

## Competitive dynamics

**ASML market position:** 94% lithography equipment share (2024), 83% of worldwide litho machine sales (2025). Near-monopoly in EUV — no competitor close.

### Why the moat holds

- **Zeiss partnership:** Zeiss makes EUV mirrors, does not sell to rivals
- **Supplier network:** 5,000 suppliers, many cannot provide to competitors
- Both Nikon and Canon misjudged technology routes (157nm wavelength, DUV-to-EUV transition)

### Nikon

- **DSP-100:** Maskless lithography for backend packaging, orders open, launch FY2026
- 1μm resolution, targets fan-out panel-level packaging (FOPLP)
- Not competing at leading edge — gave up on EUV

### Canon

- **ArF re-entry:** First new ArF products in 22 years, planned H2 2025
- **Nanoimprint lithography (NIL):** FPA-1200NZ2C launched Oct 2023
- NIL uses physical imprinting for sub-5nm resolution, 130 WPH → 180 WPH target by 2026
- First tool delivered to Texas Advanced Research Institute Sep 2024
- Not a threat to EUV — niche applications only

---

## Capacity expansion

**Production targets:**

| System | Current | 2025-2026 | 2027-2028 |
|--------|---------|-----------|-----------|
| Low-NA EUV | — | 90/year | — |
| High-NA EUV | — | — | 20/year |
| DUV | 300+ | 500-600/year | — |

**Veldhoven expansion:**
- New campus: 50 football fields, near existing HQ
- Construction full swing in 2025, first phase operational before end of decade
- Brainport Industries Campus: employees moving in by 2028 (accelerated)

**2030 targets:** €44-60B revenue, 56-60% gross margin, double EUV output.

---

## Rare earth supply chain risk

High-NA EUV machines require precision magnets made with [[Dysprosium]] and [[Terbium]]:

| Component | REE dependency |
|-----------|----------------|
| Wafer stage | Dy/Tb magnets for nm-precision positioning |
| Reticle stage | Dy/Tb magnets for mask alignment |
| Actuators | High-temp stable permanent magnets |

**Risk**: [[China]] controls 99% of Dy/Tb processing. Export restrictions could bottleneck ASML's High-NA production — creating a second chokepoint beyond ASML's own monopoly.

**Mitigation (Dec 2025)**: REAlloys $21M SRC deal to scale North American heavy REE output 300% by 2027 — specifically targeting semiconductor equipment magnets.

See [[Rare earth leverage]] for geopolitical context.

---

## Q4 2025 earnings (Jan 28, 2026)

**Record bookings smash estimates on AI infrastructure demand.**

| Metric | Q4 2025 | vs Estimate |
|--------|---------|-------------|
| Bookings | **€13.2B** | €6.32B (109% beat) |
| EUV bookings | **€7.4B** | >50% of total |
| Net sales | **€9.7B** | €9.6B expected |
| Net income | **€2.84B** | €3.01B expected |
| Order backlog | **€38.8B** | — |
| Prior Q bookings | €5.4B | (Q3 2025) |

| FY Metric | 2025 Actual | 2026 Guidance |
|-----------|-------------|---------------|
| Revenue | **€32.7B** | €34-39B (raised) |
| Net income | **€9.6B** | — |
| Gross margin | **52.8%** | — |
| Q1 2026 guidance | — | €8.2-8.9B |
| Consecutive growth years | **13** | — |

**CEO Christophe Fouquet:**
> "In the last months, many of our customers have shared a notably more positive assessment of the medium-term market situation, primarily based on more robust expectations of the sustainability of AI-related demand."

**Stock reaction:** +7.5% to **€1,309** (record high), YTD 2026 now **+41%**.

**China exposure:** 36% of Q4 net system sales (largest market), expected to fall to ~20% going forward as export controls tighten. All China sales are DUV (8 generations behind cutting edge) — no EUV allowed.

![[asml-regional-sales-q4-2025.png]]
*China (black) remained largest market at 36% in Q4 2025; expected to normalize to ~20%.*

![[asml-13-year-sales-growth.png]]
*13 consecutive years of sales growth; 2026 guidance €34-39B (raised).*

**Shareholder returns:**
- Dividend: €7.50/share for 2025 (17% increase YoY), interim €1.60 payable Feb 18, 2026
- Buyback: €12B program through Dec 2028

**Analyst reactions:**
- [[Morgan Stanley]] named ASML top European semiconductor pick ahead of results
- [[UBS]], [[JPMorgan Chase|JPMorgan]] raised price targets
- [[Barclays]] expects [[SK Hynix]] to take 12 EUV machines in 2026
- Memory shortage driving price increases → Samsung, SK Hynix expected to expand capacity

**Reporting change:** ASML will stop reporting bookings in future quarters, arguing the metric doesn't accurately capture business momentum.

---

## Workforce restructuring (Jan 2026)

~1,700 job cuts (4% of workforce), mostly in Netherlands (Technology and IT orgs), some US.

**Fouquet:** "Even a great company needs to improve... we want to make sure engineers can be engineers again."

**CFO Roger Dassen:** Feedback indicated "complex organization" with too much time spent coordinating processes. Restructuring to dedicate most engineers to specific products and modules.

**Context:** Cuts come despite record orders and >$500B market cap. Aiming for agility, not cost reduction.

**Meanwhile:** Planning second Eindhoven campus for 20,000 staff (first phase 2028).

---

## $500B milestone (Jan 2026)

**Third European company ever to reach $500B market cap:**

| Rank | Company | Sector |
|------|---------|--------|
| 1 | [[LVMH]] | [[Luxury]] |
| 2 | [[Novo Nordisk]] | Pharma |
| 3 | **ASML** | [[Semiconductors]] |

| Metric | Value |
|--------|-------|
| Market cap | **€1,309 × shares** (~$550B) |
| YTD 2026 | **+41%** |
| Status | Record high, [[Europe]]'s most valuable |

**Catalyst:** [[TSMC]] 2026 capex guidance of $56B (above expectations) — validates sustained AI spending.

**[[Barclays]] (Emmanuel Cau):**
> "The milestone means a lot for the market sentimentally. [[Europe]] is a small market, so if ASML as a major stock goes up, the broader market will automatically benefit. The rally in ASML also gives European investors a gateway to play the mainstream AI trade."

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | ASML (NASDAQ, Euronext) |
| Market cap | **~$550B** (Jan 28, 2026) |
| Share price | **€1,309** (record high) |
| 2025 revenue | **€32.7B** |
| 2025 net income | **€9.6B** |
| 2026 guidance | **€34-39B** |
| Order backlog | **€38.8B** (€25.5B EUV) |
| EUV share | 100% |
| Low-NA EUV price | ~€170M |
| High-NA EUV price | $350-400M |
| EUV capacity | 90/year (2025-26 target) |
| High-NA capacity | 20/year (2027-28 target) |

---

## For theses

- [[Long WFE]] — crown jewel, monopoly position
- [[Long TSMC]] — ASML enables TSMC's leading edge moat
- [[Short TSMC long Korea]] — Samsung needs ASML too; equipment is neutral

---

## Related

**Customers:**
- [[TSMC]] — largest customer, priority EUV access, skipping High-NA for A14
- [[Samsung]] — major customer, 2× High-NA ordered for 2nm
- [[SK Hynix]] — first memory High-NA customer, 12 EUV machines expected 2026
- [[Intel Foundry Services]] — growing customer, 14A ramp, 4× High-NA
- [[Micron]] — memory customer, capacity expansion

**AI investment:**
- [[Mistral]] — €1.3B investment (Sep 2025), 11% stake

**Competitors:**
- [[Canon]] — nanoimprint lithography (niche)
- [[Nikon]] — maskless packaging lithography (niche)
- SMEE — Chinese domestic alternative (90nm, developing 28nm)
- AMIES — SMEE spinoff, 90% China packaging market

**Supply chain:**
- [[Zeiss]] — EUV mirror supplier (exclusive)
- [[Dysprosium]] — REE supply risk for High-NA magnets
- [[Rare earth leverage]] — [[China]] control of magnet materials

**Ecosystem:**
- [[Tokyo Electron]] — Japanese supplier, beneficiary
- [[Lasertec]] — Japanese supplier, beneficiary
- [[Screen Holdings]] — Japanese supplier, beneficiary

**AI capex drivers:**
- [[Meta]], [[Microsoft]], [[Amazon]], [[Google]] — hyperscaler spending
- [[NVIDIA]] — AI accelerators require ASML EUV

**Regulatory:**
- [[Export controls]] — blocks [[China]] EUV/advanced DUV sales
- [[EU Made in Europe Tech Rules 2026]] — EU industrial policy affecting semiconductor equipment supply chains

**Theses:**
- [[Long WFE]] — crown jewel position
- [[Foundry Wars]] — enables leading edge

**Analysts:**
- [[Morgan Stanley]] — top European semi pick

*Updated 2026-03-03*

---

## Beyond EUV strategy (Reuters exclusive, Mar 2, 2026)

New CTO **Marco Pieters** (promoted Oct 2025, succeeding Martin van den Brink) is expanding ASML from sole EUV supplier into a broader AI-era chipmaking tool platform. Three pillars on a 10-15 year horizon:

### 1. Advanced packaging tools — TWINSCAN XT:260

New scanning tool for advanced 3D chip packaging (disclosed Q3 2025 earnings):

| Spec | Value |
|------|-------|
| Wavelength | i-line (365nm) step-and-scan |
| Wafer size | 300mm |
| Throughput | **270 WPH** (4x previous packaging solutions) |
| Image field | 52mm × 66mm — interposers up to **3,432 mm²** without stitching |
| Dose | 340 mJ |
| Target market | [[HBM]] wafer-based and hybrid-bonding for AI chips |

Advanced packaging market: $42-51B (2025) → $70-90B by 2034. Analysts project ASML could capture 5-10% tooling share over a decade. Threatens [[Onto Innovation]] (incumbent).

### 2. Larger chip field size

Engineers exploring optical and mechanical redesigns to expand the printable field beyond current postage-stamp limit. AI chips have grown significantly in physical size.

### 3. Next-gen EUV wavelengths

Exploring novel optics, potential next-generation wavelengths, and auxiliary systems that could work alongside or eventually succeed EUV in HVM.

### 1000W EUV light source breakthrough (Feb 24, 2026)

Demonstrated **1,000W EUV light source** under factory-ready conditions (up from current 600W):

| Metric | Current | 1000W |
|--------|---------|-------|
| Tin droplet rate | ~50K/sec | **100K/sec** |
| Laser sequences | 1 | **2 distinct sequences, 3 lasers** |
| Throughput | ~220 WPH | **330 WPH** (+50%) |
| Deployment | — | **~2030** |

### EUV roadmap to Hyper-NA

| System | NA | Timeline | Cost | Capability |
|--------|-----|----------|------|------------|
| Low-NA EUV | 0.33 | Current | ~€170M | Production workhorse |
| High-NA EUV (EXE:5000/5200B) | 0.55 | 2025-2026 | $350-400M | 1nm production |
| EXE:5400 | 0.55 | ~2028 | — | 3rd gen High-NA |
| EXE:5600 | 0.55 | ~2030 | — | 4th gen, flexible illuminators |
| **Hyper-NA EUV** | **0.75-0.85** | **~2030** | **~$720M** | Below 0.2nm (2 angstroms) |

With multi-patterning, EXE series can reach 0.5nm (5 angstroms) by 2033. Hyper-NA targets nodes below 0.2nm.

10-year vision: unified EUV platform spanning Low-NA → High-NA → Hyper-NA.
