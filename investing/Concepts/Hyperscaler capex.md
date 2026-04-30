#concept #demand #ai #datacenter

Capital expenditure by the Big 5 hyperscalers (Amazon, Google, Meta, Microsoft, Oracle) and Tier 2 neoclouds (CoreWeave, Lambda, Crusoe) on AI infrastructure — the primary demand signal for semiconductors.

---

## The chart

![[hyperscaler-capex.png]]
*[[Amazon]] · [[Google]] · [[Meta]] · [[Microsoft]] · [[Oracle]]*

*Solid lines = actual quarterly capex; dotted = forecasts based on company guidance and analyst estimates*

---

## Quarterly trajectory

| Hyperscaler | Q3 2019 | Q3 2025 | Multiple |
|-------------|---------|---------|----------|
| **AMZN** | $4.7B | $35.1B | **7.5x** |
| **GOOG** | $6.7B | $24.0B | **3.6x** |
| **META** | $3.5B | $18.8B | **5.4x** |
| **MSFT** | $3.4B | $19.4B | **5.7x** |
| **Big 4 Total** | $18.3B | **$97.3B** | **5.3x** |

Oracle not shown (fiscal year ends May, quarters don't align).

---

## 2025 guidance

| Hyperscaler | FY2025 Guidance | Notes |
|-------------|-----------------|-------|
| **AMZN** | $125B | Calendar year |
| **GOOG** | $91-93B | Calendar year, raised 3x |
| **META** | $70-72B | Calendar year |
| **MSFT** | ~$80B | Fiscal year ends June |
| **ORCL** | ~$50B | Fiscal year ends May, raised from $35B |

---

## 2026 forecasts

| Hyperscaler | 2026 Estimate | Source |
|-------------|---------------|--------|
| **AMZN** | ~$150B | CFO: "will grow in 2026" |
| **GOOG** | ~$115B (CFO Q4 2025 guide) → **$185B** (Apr 2026 forecast cited by [[FT]]) | CFO: "significant increase"; later [[Thomas Kurian]] confirmation around the [[Anthropic]] capacity deal |
| **META** | ~$100B | CFO: "notably larger" |
| **MSFT** | $121-140B | Jefferies, Cantor |
| **ORCL** | ~$50B+ | Already at $50B for FY26 |

The [[Alphabet]] guide moved up between the early-2026 CFO call ("significant increase," ~$115B) and the late-Apr 2026 reporting of ~$185B for the year. The bridge is the Apr 2026 [[Anthropic]] anchor commitment — 5 GW of [[Google Cloud]] capacity over five years with up to $40B in [[Google]] equity — which both pulls forward TPU/datacenter spend and gives [[Thomas Kurian]] the demand justification for a higher guide. See [[Google Cloud]], [[Google TPU Competitive Position]], and [[Anthropic hyperscaler financing surge April 2026]].

**Aggregate forecasts (Big 5 + broader AI infrastructure):**

| Source | 2025 | 2026 | YoY | Scope |
|--------|------|------|-----|-------|
| CreditSights | ~$443B | **~$602B** | +36% | Big 5 |
| [[Goldman Sachs]] | — | **$527B+** | — | Big 5 |
| Fortune/McKinsey | ~$400B | **$630-700B** | +62% | All AI DC capex (incl. neoclouds, startups) |

~75% of 2026 capex (~$450B) is AI infrastructure.

**Cumulative through 2030:** $5.2T in AI-ready data center capex (McKinsey, Apr 2025), driven largely by GPUs and energy infrastructure. Traditional (non-AI) DC capex adds $1.5T, for $6.7T total compute infrastructure spend.

### Total AI infrastructure market ([[Gartner]], Jan 2026)

| Metric | 2026 forecast |
|--------|---------------|
| **Total AI infrastructure spending** | **>$1.3 trillion** |

This includes hyperscalers, neoclouds, enterprises, and sovereign AI initiatives — not just Big 5.

**Context:** 2025 semiconductor industry = $793B (+21%). AI chips = ~1/3 of total. See [[Semiconductors]].

---

## Apr 29, 2026 print night — Big 4 capex resets again

The four-way Big Tech earnings print on Apr 29 reset the FY26 hyperscaler capex picture upward across all four names within a single 24-hour window. The cross-section is the most informative view:

| Name | Q1 capex | FY26 capex (new) | FY26 capex (prior) | Cloud / segment | After-hours move |
|------|---------|------------------|---------------------|------------------|------------------|
| [[Microsoft]] | $31.9B | **~$190B** (incl. ~$25B memory mark) | ~$80B FY25 implied; Street $121-140B | [[Azure]] +40% YoY | Roughly flat |
| [[Alphabet]] | $35.7B | $180-190B | $175-185B (Feb-quarter) | [[Google Cloud]] +63% YoY ($20.02B) | Modestly positive |
| [[Amazon]] | $44.2B | $200B (reaffirmed) | $200B (Feb-quarter); Q1 run-rate trending higher | [[AWS]] +28% YoY ($37.6B) | Modestly positive |
| [[Meta]] | (not detailed) | $125-145B | $115-135B | (no breakout) | -7% AH |

Big 4 FY26 capex now centers near **$700-720B** — up from the $600-630B framing entering print night, and a rough doubling of the $397B 2025 actual. Two structural changes from this print:

**1. Memory-cost capitalization is the new line item.** [[Microsoft]] explicitly tagged ~$25B of its FY26 capex as memory-cost markup; [[Meta]] attributed its $10B raise (midpoint to midpoint) to "higher component pricing this year." For the first time the [[Memory shortage 2025-2026|memory shortage]] is showing up in hyperscaler capex guidance rather than as a future-period margin warning. The marginal capex dollar is increasingly going to the [[SK Hynix]] / [[Samsung]] / [[Micron]] complex via [[NVIDIA]]-bundled HBM and discrete server DRAM, not just to merchant GPUs.

**2. The dispersion is now demand-vs-supply.** [[Sundar Pichai|Pichai]]'s "we are compute constrained in the near term" — *"our cloud revenue would have been higher if we were able to meet the demand"* — and the Google Cloud backlog roughly doubling to **$460B+** is the cleanest "supply-constrained" tell. AWS backlog $364B excludes >$100B from a new [[Anthropic]] deal. Demand is binding on supply at GOOGL and AMZN. The market rewarded those (modest AH gains) and punished the names where capex rose without an offsetting demand signal (META -7%).

**3. The [[2026 OpenAI revenue miss]] read-through.** The Apr 28 WSJ report on OpenAI revenue shortfalls primed the market to test the capex/revenue ratio. Twenty-four hours later, the print night gave a clean cross-sectional answer: backlog growth and AI-ARR run-rate disclosure (AWS $15B+, Google Cloud $460B+ backlog) were the metrics that decided the AH dispersion, not headline capex level.

The forward question for [[NVIDIA]], [[AMD]], [[Broadcom]], [[TSMC]], [[SK Hynix]] is whether the [[Memory shortage 2025-2026|memory mark]] increment crowds out merchant-GPU TAM (zero-sum) or stacks on top of it (additive). Microsoft's "two-thirds of Q3 capex on short-lived assets" disclosure suggests the GPU bill is still rising — the memory mark is layered, not substituted.

*Sources: per-actor sources in [[Microsoft]], [[Alphabet]], [[Amazon]], [[Meta]] Q1 sections, Apr 29 2026.*

---

## Kurian shakeout warning (Apr 2026)

[[Thomas Kurian]] ([[Google Cloud]] CEO) publicly forecast a multi-year shakeout in the AI provider layer, framing private capital markets as the binding constraint:

*"Those AI providers depend on private capital markets, which are reaching a saturation point. If you're going to go public, you can't be lossmaking forever. And if you stay private, you cannot raise venture money forever."*

He projected: *"Over the next year to two you will see some shakeout in the market. Whether particular providers are going to make it or not largely comes down to the economics."*

Why this matters for the capex picture: Kurian is a hyperscaler CEO whose own [[Google Cloud]] business is being underwritten by the same labs' compute commitments. The incentive structure is real:

- If [[OpenAI]] and [[Anthropic]] both clear the financing gap, the hyperscalers' $602B+ of 2026 capex looks well-placed.
- If one or more frontier labs runs out of private-market funding before reaching IPO scale, the demand validation behind the guide weakens — making the call out loud is partly an attempt to pre-position [[Anthropic]] (a Google customer / investee) as the survivor.

[[OpenAI]] and [[Anthropic]] together raised more than $150B in 2026, two of the largest private fundraises in history. The $185B Alphabet 2026 capex is partly contingent on whether that pace can continue without IPOs.

See [[AI infrastructure financing risk]], [[Anthropic vs OpenAI compute race]], and [[OpenAI Infrastructure Spend]].

*Source: FT, Apr 26 2026.*

---

## Oracle: fastest growth, most stress

Oracle is ramping fastest but showing financial strain:

| Metric | Value |
|--------|-------|
| FY25 capex | $21.2B |
| FY26 capex guidance | **$50B** (raised from $35B) |
| YoY growth | **2.4x** |
| Capital intensity | **57%** of revenue (highest) |
| Q2 FY26 FCF | **-$10B** |
| RPO backlog | $523B (+$68B in one quarter) |

**Credit concerns:** Oracle's CDS spreads widened to 125+ bps — levels not seen since 2009. Bonds trade like junk despite Baa2/BBB ratings.

**Why:** [[OpenAI]]/Stargate ($300B commitment), Meta and [[NVIDIA]] contracts driving backlog.

---

## Tier 2: Neoclouds

GPU-native cloud providers built for AI workloads. Smaller than hyperscalers but growing fast.

### CoreWeave (CRWV)

| Metric | Value |
|--------|-------|
| 2025 capex | $12-14B |
| 2026 capex | **$30B+** (doubling) |
| Revenue backlog | $55.6B |
| Contracted power | 2.9 GW |
| Debt/equity | **4.8x** |

Largest neocloud. GPU-collateralized debt model unprecedented in tech. $14B Meta deal anchors backlog.

### SemiAnalysis ClusterMAX tiers

| Tier | Players |
|------|---------|
| **[[Platinum]]** | CoreWeave (only) |
| **[[Gold]]** | [[Nebius]], Oracle, Azure, Crusoe, [[FluidStack]] |
| **[[Silver]]** | AWS, Lambda, [[Scaleway]] |

### Other neoclouds

| Player | Status | Notes |
|--------|--------|-------|
| **[[Lambda Labs]]** | Private | Developer-first, $480M Series D (Feb 2025) |
| **Crusoe** | Private | 45GW pipeline, flare gas / stranded renewables |
| **[[Nebius]]** | Public (NBIS) | [[Yandex]] spin-off, $750M-$1B ARR target |
| **[[FluidStack]]** | Private | [[Anthropic]] ops partner, [[Gold]] tier |
| **[[Nscale]]** | Private | [[NVIDIA]]-backed, Stargate Norway (100K GPUs by 2026) |
| **[[Voltage Park]]** | Private | Significant GPU capacity |
| **[[Together AI]]** | Private | Training/inference platform |
| **[[Vultr]]** | Private | Established, broad GPU offering |
| **[[Civo]]** | Private | [[UK]]-based |
| **[[Scaleway]]** | — | European, [[Silver]] tier |
| **[[RunPod]]** | Private | Budget ($1.74/hr H100) |
| **[[Vast.ai]]** | Private | Marketplace model |

**Pricing range:** H100 varies 4x across providers ($1.45-$6.15/hr). CoreWeave commands premium.

**Cost breakdown (per [[Nebius]]):**
- GPUs: **80%** of spending
- DC buildout: 18-20%
- Land/power: ~1%

### Neocloud risk

Early 2026 sentiment shifting from "build it and they will come" to [[ROIC]] focus. CoreWeave trading at discount to 2025 highs. Lambda/Together IPO windows narrowing.

**Market size:** GPU-as-a-service was $3.2B (2023) → projected $49.8B (2032), 36% CAGR.

See [[CoreWeave]] for detailed analysis.

---

## Sentiment shift (March 2026)

[[BofA]] fund manager survey (March 2026) signals institutional skepticism reaching critical mass:

| Finding | Detail |
|---------|--------|
| AI capex as credit crisis source | **30%** of fund managers (most popular answer) |
| "AI bubble" as top tail risk | **25%** of respondents |
| Semiconductor sector rating | **Downgraded to underweight** |

[[Savita Subramanian]]: "Monetization is to be determined, and power is the bottleneck and will take a while to build out." [[IBM]] CEO [[Arvind Krishna]] went further: hyperscaler spend is "economically unrecoverable at current scale."

The timing is brutal — this skepticism is arriving alongside an oil shock (WTI >$100 from [[2026 Iran conflict market impact|Iran conflict]]) that directly threatens the energy-intensive AI buildout. $650B in 2026 hyperscaler capex meets $100+ oil and -92K NFP. The stagflation collision makes the ROIC question impossible to dodge.

---

## Financing the buildout

Hyperscalers are using multiple structures:

| Structure | Example |
|-----------|---------|
| Corporate bonds | Meta $30B IG offering (2025) |
| [[Private credit]] | Meta $30B SPV with [[Blue Owl]] |
| Project finance | GPU leasing, DC sale-leasebacks |
| Off-balance-sheet | Meta Hyperion ($50B Louisiana DC) |

[[Morgan Stanley]] estimates $1.5T total AI financing needed, $800B via private credit by 2028.

See [[AI infrastructure financing]] for details.

---

## What it means

**For semiconductors:**
```
Hyperscaler $ → [[NVIDIA]]/[[AMD]] → [[TSMC]] → [[SK Hynix]] ([[HBM]]) → OSAT
```

Every dollar of capex flows through the chip supply chain. $600B in 2026 = unprecedented demand.

**For power:**
- 1GW data center costs ~$50B
- Big 5 adding 10+ GW capacity
- See [[Power constraints]], [[BYOP]]

**For credit markets:**
- Hyperscalers issuing record debt
- Oracle showing stress despite IG ratings
- Risk of overbuilding if AI demand disappoints

---

## For theses

- [[Long TSMC]] — hyperscaler capex = [[TSMC]] revenue
- [[Long memory]] — every GPU needs [[HBM]]
- [[AI infrastructure financing]] — credit market implications

---

## Related

- [[AI hyperscalers]] — the players
- [[Amazon]], [[Google]], [[Meta]], [[Microsoft]], [[Oracle]] — Big 5 notes
- [[CoreWeave]] — largest neocloud
- [[AI infrastructure financing]] — how it's funded
- [[Power constraints]] — physical limits
- [[BYOP]] — bring your own power trend
- [[GPU deployment bottleneck]] — shipped ≠ deployed
- [[Data center boomtown effect]] — community disruption from megaprojects
- [[Data center land competition]] — land bidding dynamics

*Created 2026-01-20*
