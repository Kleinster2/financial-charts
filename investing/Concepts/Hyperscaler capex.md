#concept #demand #ai #datacenter

Capital expenditure by the Big 5 hyperscalers ([[Amazon]], [[Google]], [[Meta]], [[Microsoft]], [[Oracle]]) and Tier 2 neoclouds ([[CoreWeave]], [[Lambda Labs|Lambda]], [[Crusoe Energy|Crusoe]]) on AI infrastructure — the primary demand signal for semiconductors.

---

## Synthesis

Hyperscaler capex is the demand-side engine behind the semiconductor and memory stack, but it is no longer just a growth line item. The 2026 guide moved into the $700-725B range for the Big 4, with [[Microsoft]] explicitly adding about $25B of memory-cost markup and [[Meta]] raising guidance partly because component prices rose. That makes [[Memory]], [[HBM]], [[AI Compute]], and [[WFE]] the cleaner supplier-side expressions than the hyperscalers themselves. The financing side is now equally important: if cash flow, debt, SPVs, and equity issuance all fund the same buildout, then rates shocks and equity-window stress feed back into chip demand before any physical data-center project is canceled.

## The chart

![[hyperscaler-capex.png]]
*[[Amazon]] · [[Google]] · [[Meta]] · [[Microsoft]] · [[Oracle]]*

*Solid lines = actual quarterly capex; dotted = forecasts based on company guidance and analyst estimates*

---

## Quarterly trajectory

| Hyperscaler | Q3 2019 | Q3 2025 | Multiple |
|-------------|---------|---------|----------|
| **AMZN** | $4.7B | $35.1B | 7.5x |
| GOOG | $6.7B | $24.0B | 3.6x |
| META | $3.5B | $18.8B | 5.4x |
| MSFT | $3.4B | $19.4B | 5.7x |
| Big 4 Total | $18.3B | $97.3B | 5.3x |

Oracle not shown (fiscal year ends May, quarters don't align).

---

## 2025 guidance

| Hyperscaler | FY2025 Guidance | Notes |
|-------------|-----------------|-------|
| AMZN | $125B | Calendar year |
| GOOG | $91-93B | Calendar year, raised 3x |
| META | $70-72B | Calendar year |
| MSFT | ~$80B | Fiscal year ends June |
| ORCL | ~$50B | Fiscal year ends May, raised from $35B |

---

## 2026 forecasts

| Hyperscaler | 2026 Estimate | Source |
|-------------|---------------|--------|
| AMZN | ~$150B | CFO: "will grow in 2026" |
| GOOG | ~$115B (CFO Q4 2025 guide) → $180-190B (Apr 2026 guide / FT context) | CFO: "significant increase"; later [[Thomas Kurian]] confirmation around the [[Anthropic]] capacity deal |
| META | ~$100B | CFO: "notably larger" |
| MSFT | $121-140B | [[Jefferies]], Cantor |
| ORCL | ~$50B+ | Already at $50B for FY26 |

The [[Alphabet]] guide moved up between the early-2026 CFO call ("significant increase," ~$115B) and the late-Apr 2026 reporting of ~$185B for the year. The bridge is the Apr 2026 [[Anthropic]] anchor commitment — 5 GW of [[Google Cloud]] capacity over five years with up to $40B in [[Google]] equity — which both pulls forward [[TPU]]/datacenter spend and gives [[Thomas Kurian]] the demand justification for a higher guide. See [[Google Cloud]], [[Google TPU Competitive Position]], and [[Anthropic hyperscaler financing surge April 2026]].

Aggregate forecasts (Big 5 + broader AI infrastructure):

| Source | 2025 | 2026 | YoY | Scope |
|--------|------|------|-----|-------|
| [[CreditSights]] | ~$443B | ~$602B | +36% | Big 5 |
| [[Goldman Sachs]] | — | $527B+ | — | Big 5 |
| [[Fortune]]/[[McKinsey]] | ~$400B | $630-700B | +62% | All AI DC capex (incl. neoclouds, startups) |

~75% of 2026 capex (~$450B) is AI infrastructure.

Cumulative through 2030: $5.2T in AI-ready data center capex ([[McKinsey]], Apr 2025), driven largely by GPUs and energy infrastructure. Traditional (non-AI) DC capex adds $1.5T, for $6.7T total compute infrastructure spend.

### Total AI infrastructure market ([[Gartner]], Jan 2026)

| Metric | 2026 forecast |
|--------|---------------|
| Total AI infrastructure spending | >$1.3 trillion |

This includes hyperscalers, neoclouds, enterprises, and sovereign AI initiatives — not just Big 5.

Context: 2025 semiconductor industry = $793B (+21%). AI chips = ~1/3 of total. See [[Semiconductors]].

---

## Apr 29, 2026 print night — Big 4 capex resets again

The four-way Big Tech earnings print on Apr 29 reset the FY26 hyperscaler capex picture upward across all four names within a single 24-hour window. The cross-section is the most informative view:

| Name | Q1 capex | FY26 capex (new) | FY26 capex (prior) | Cloud / segment | After-hours move |
|------|---------|------------------|---------------------|------------------|------------------|
| [[Microsoft]] | $31.9B | ~$190B (incl. ~$25B memory mark) | ~$80B FY25 implied; Street $121-140B | [[Microsoft]] Azure +40% YoY | Roughly flat |
| [[Alphabet]] | $35.7B | $180-190B | $175-185B (Feb-quarter) | [[Google Cloud]] +63% YoY ($20.02B) | Modestly positive |
| [[Amazon]] | $44.2B | $200B (reaffirmed) | $200B (Feb-quarter); Q1 run-rate trending higher | [[AWS]] +28% YoY ($37.6B) | Modestly positive |
| [[Meta]] | (not detailed) | $125-145B | $115-135B | (no breakout) | -7% AH |

Big 4 FY26 capex now centers near $700-725B — up from the $600-630B framing entering print night, and a rough doubling of the $397B 2025 actual. Two structural changes from this print:

1. [[Memory]]-cost capitalization is the new line item. [[Microsoft]] explicitly tagged ~$25B of its FY26 capex as memory-cost markup; [[Meta]] attributed its $10B raise (midpoint to midpoint) to "higher component pricing this year." For the first time the [[Memory shortage 2025-2026|memory shortage]] is showing up in hyperscaler capex guidance rather than as a future-period margin warning. The marginal capex dollar is increasingly going to the [[SK Hynix]] / [[Samsung]] / [[Micron]] complex via [[NVIDIA]]-bundled HBM and discrete server DRAM, not just to merchant GPUs.

2. The dispersion is now demand-vs-supply. [[Sundar Pichai|Pichai]]'s "we are compute constrained in the near term" — *"our cloud revenue would have been higher if we were able to meet the demand"* — and the Google Cloud backlog roughly doubling to $460B+ is the cleanest "supply-constrained" tell. AWS backlog $364B excludes >$100B from a new [[Anthropic]] deal. Demand is binding on supply at GOOGL and AMZN. The market rewarded those (modest AH gains) and punished the names where capex rose without an offsetting demand signal (META -7%).

3. The [[2026 OpenAI revenue miss]] read-through. The Apr 28 WSJ report on OpenAI revenue shortfalls primed the market to test the capex/revenue ratio. Twenty-four hours later, the print night gave a clean cross-sectional answer: backlog growth and AI-ARR run-rate disclosure (AWS $15B+, Google Cloud $460B+ backlog) were the metrics that decided the AH dispersion, not headline capex level.

The forward question for [[NVIDIA]], [[AMD]], [[Broadcom]], [[TSMC]], [[SK Hynix]] is whether the [[Memory shortage 2025-2026|memory mark]] increment crowds out merchant-GPU TAM (zero-sum) or stacks on top of it (additive). Microsoft's "two-thirds of Q3 capex on short-lived assets" disclosure suggests the GPU bill is still rising — the memory mark is layered, not substituted.

*Sources: per-actor sources in [[Microsoft]], [[Alphabet]], [[Amazon]], [[Meta]] Q1 sections, Apr 29 2026.*

---

## May 8, 2026 FT / Visible Alpha free-cash-flow trough

The May 8 [[Financial Times]] / [[Visible Alpha]] pass turns the Apr 29 capex reset into a cash-flow story. [[Amazon]], [[Alphabet]], [[Microsoft]], and [[Meta]] are expected to spend roughly $725B on AI infrastructure in 2026, while combined free cash flow is projected to fall toward about $4B in Q3 2026, versus a post-Covid quarterly run-rate around $45B. The full-year free-cash-flow line is now expected to be the weakest since 2014, even though the revenue base is many times larger.

The company-level read is now:

| Company | FT / filing datapoint | Capex-cycle read |
|---|---|---|
| [[Amazon]] | Q1 2026 cash capex was $43.2B, almost 2x Q1 2025; Amazon's filing says it expects those investments to increase in 2026 and financing inflows rose sharply | Largest single-company outlay; expected to burn cash for the year unless AWS monetization catches up quickly |
| [[Alphabet]] | Q1 2026 OCF was $45.8B, PP&E purchases were $35.7B, debt proceeds were $31.4B, and the 10-Q shows no Class A/C share repurchases | Still FCF-positive, but capital returns are now the pressure valve |
| [[Microsoft]] | FY26 calendar capex guide is roughly $190B, including about $25B from higher component pricing | Strongest balance sheet, but even MSFT is letting component inflation flow through capex |
| [[Meta]] | Q1 2026 10-Q shows no share repurchases and $59.0B of senior notes outstanding | Ad cash flows still strong, but buybacks are no longer the default use of cash while capex ramps |
| [[Oracle]] | Outside the Big 4 chart, but FT frames Oracle as the most stressed cloud builder, with cash burn tied to the OpenAI capacity buildout | More direct credit-risk expression of the same cycle |

Provided-chart disposition from the user screenshots:

| FT chart | Extracted vault datapoint | Destination |
|---|---|---|
| Big 4 total capex vs free cash flow | Projected capex keeps rising into 2026 while combined free cash flow compresses toward the article's roughly $4B Q3 trough estimate | This section; [[AI capex arms race]] |
| [[Microsoft]] tab | Microsoft remains in the group FCF squeeze despite the cleanest balance sheet; capex is still expected to outpace near-term cash conversion | [[Microsoft]]; [[AI hyperscalers]] |
| [[Meta]] tab | Meta's projected period shows capex pushing above historical run-rate while free cash flow dips under pressure | [[Meta]]; [[AI infrastructure financing]] |
| [[Alphabet]] / Google tab | Alphabet stays healthier than Meta but the chart still shows capex steepening while FCF becomes volatile and much thinner than the pre-2026 run-rate | [[Alphabet]]; [[Hyperscaler bond issuance]] |
| [[Amazon]] tab | Amazon shows the largest single-company capex ramp and the article's expected full-year cash burn risk | [[Amazon]]; this section |
| Big 4 capex-plan stack | The screenshot shows companies adding about $65B to 2026 capex plans between Dec 2025 and Mar 2026, taking the stack from roughly $665B to roughly $730B | This section; [[AI capex arms race]] |
| Debt and lease-liability stack | The screenshot shows Big Tech total debt and lease liabilities rising from roughly $220B in 2021 to roughly $360B in 2025 | [[Hyperscaler bond issuance]]; [[AI infrastructure financing risk]] |

The FT screenshots were ingested as extracted chart data rather than copied images because the source is copyrighted and the article itself instructs readers to use FT sharing tools rather than copying. Values read directly from the screenshots are treated as visual estimates; exact numbers above come from the article text or official filings where available.

Two caveats matter. First, free cash flow is not a [[GAAP]]-defined metric; leased data centers, share-based compensation treatment, and project-finance vehicles can make the economic exposure worse than headline FCF suggests. Second, charts that show liabilities or FCF under publisher methodology need reconciliation against filings before being reused as standalone hard data.

*Sources: [FT article](https://www.ft.com/content/b3dfaba9-17a2-4fac-90fe-4ab3ca7c9494), May 8 2026; [Alphabet Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm); [Amazon Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/amzn-20260331.htm); [Meta Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm); [Microsoft FY26 Q3 earnings transcript](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3).*

---

## Jun 1, 2026 Alphabet equity raise - common equity enters the stack

[[Alphabet]]'s equity raise is the cleanest evidence that the hyperscaler capex cycle has moved beyond the "free cash flow trough" framing. The May 8 FT / [[Visible Alpha]] story showed the Big 4 capex and FCF lines crossing uncomfortably; the Jun 1 FT report and Jun 2 [[SEC]] supplements show the next funding instrument. Alphabet's initial package was up to $80B, and FT's Jun. 5 Meta follow-up described it as $85B after a $5B demand upsizing. The components include $15B of common stock, $15B of mandatory-convertible preferred/depositary shares, a $40B ATM program, and a $10B [[Berkshire Hathaway]] private placement.

The capex read-through is that 2026's $180-190B guide is not the endpoint. FT reported Alphabet expects capex to rise significantly in 2027 and that Big Tech expects to spend about $725B on AI this year. The immediate physical bottleneck is still undisclosed - no new data-center site, PPA, interconnection, grid region, or MW target came with the financing - so the right filing is funding-side, not power-asset-side. See [[Alphabet equity raise June 2026]], [[AI infrastructure financing]], and [[AI infrastructure financing risk]].

*Sources: [FT - Alphabet to sell $80bn in stock to fund AI spending spree](https://www.ft.com/content/341f151b-f472-4530-8579-d4b803519257), Jun 1 2026; Alphabet 424B5 supplements, Jun 2 2026; [FT](https://www.ft.com/content/e6df645d-1709-4a77-b15d-aa43a0209efd), Jun. 5 2026.*

---

## Jun 5, 2026 Meta equity-raise exploration - peer validation

FT's Jun. 5 report that [[Meta]] is considering a tens-of-billions stock sale is the first peer-validation datapoint after the [[Alphabet equity raise June 2026]]. The capex backdrop is already in this note: Meta raised 2026 capex guidance to $125-145B, up $10B at the midpoint from the prior guide, while FT says 2027 could be higher. The new information is not more spend; it is the financing instrument Meta may use if debt, buyback suspension, the [[Blue Owl]] / Hyperion structure, and cost cuts are not enough.

The market reaction fits the capex-skepticism frame. META closed Jun. 5 down 5.51%, versus [[XLC]] -1.27% and QQQ -4.80%. The QQQ comparison makes the day look mostly like a tech selloff, but the communications-services comparison shows a Meta-specific dilution penalty.

No new physical capacity was disclosed: no data-center site, PPA, interconnection, grid region, or MW target. This belongs in [[AI infrastructure financing]] and [[AI infrastructure financing risk]] as funding-side pressure, not in the power-asset map.

*Source: [FT](https://www.ft.com/content/e6df645d-1709-4a77-b15d-aa43a0209efd), Jun. 5 2026; price source: local `prices_long` closes through Jun. 5 2026.*

## Jun 5, 2026 [[Nasdaq]]/SOX selloff - capex funding window stress

The [[Nasdaq semiconductor selloff June 2026]] turns the Meta/Alphabet equity-funding thread into a broader capex-window test. FT tied the selloff to a strong payrolls report, a 2-year Treasury yield move to 4.17%, and market pricing for a December Fed hike. Local close data shows the impact on the AI-capex beneficiary basket: [[Nasdaq]] Composite -4.18%, [[QQQ]] -4.80%, [[XLK]] -6.66%, [[SOXX]] -10.44%, and [[SMH]] -9.22%.

The capex implication is not that hyperscalers will stop spending. It is that the funding narrative becomes more fragile when the supplier complex that validates the buildout reprices at the same time as [[Alphabet equity raise June 2026]], Meta's exploratory equity discussion, and the [[SpaceX IPO 2026]] roadshow. If AI infrastructure is funded by cash flow plus debt plus equity-market absorption, then rates shocks matter even before any data-center demand datapoint weakens.

No new physical capacity was disclosed: no data-center site, PPA, interconnection, grid region, or MW target. This is a capex-financing and market-tape update, not a power-asset update.

*Sources: [FT](https://www.ft.com/content/2929bbd3-1f71-4424-a577-f016c3c65603), Jun. 5 2026; local `prices_long` closes through Jun. 5 2026.*

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
| FY26 capex guidance | $50B (raised from $35B) |
| YoY growth | 2.4x |
| Capital intensity | 57% of revenue (highest) |
| Q2 FY26 FCF | -$10B |
| RPO backlog | $523B (+$68B in one quarter) |

Credit concerns: Oracle's CDS spreads widened to 125+ bps — levels not seen since 2009. Bonds trade like junk despite Baa2/BBB ratings.

Why: [[OpenAI]]/Stargate ($300B commitment), Meta and [[NVIDIA]] contracts driving backlog.

---

## Tier 2: Neoclouds

GPU-native cloud providers built for AI workloads. Smaller than hyperscalers but growing fast.

### CoreWeave (CRWV)

| Metric | Value |
|--------|-------|
| 2025 capex | $12-14B |
| 2026 capex | $30B+ (doubling) |
| Revenue backlog | $55.6B |
| Contracted power | 2.9 GW |
| Debt/equity | 4.8x |

Largest neocloud. GPU-collateralized debt model unprecedented in tech. $14B Meta deal anchors backlog.

### [[SemiAnalysis]] ClusterMAX tiers

| Tier | Players |
|------|---------|
| [[Platinum]] | CoreWeave (only) |
| [[Gold]] | [[Nebius]], Oracle, Azure, Crusoe, [[FluidStack]] |
| [[Silver]] | AWS, Lambda, [[Scaleway]] |

### Other neoclouds

| Player | Status | Notes |
|--------|--------|-------|
| [[Lambda Labs]] | Private | Developer-first, $480M Series D (Feb 2025) |
| Crusoe | Private | 45GW pipeline, flare gas / stranded renewables |
| [[Nebius]] | Public (NBIS) | [[Yandex]] spin-off, $750M-$1B ARR target |
| [[FluidStack]] | Private | [[Anthropic]] ops partner, [[Gold]] tier |
| [[Nscale]] | Private | [[NVIDIA]]-backed, Stargate [[Norway]] (100K GPUs by 2026) |
| [[Voltage Park]] | Private | Significant GPU capacity |
| [[Together AI]] | Private | Training/inference platform |
| [[Vultr]] | Private | Established, broad GPU offering |
| [[Civo]] | Private | [[UK]]-based |
| [[Scaleway]] | — | European, [[Silver]] tier |
| [[RunPod]] | Private | Budget ($1.74/hr [[H100]]) |
| [[Vast.ai]] | Private | Marketplace model |

Pricing range: [[H100]] varies 4x across providers ($1.45-$6.15/hr). CoreWeave commands premium.

Cost breakdown (per [[Nebius]]):
- GPUs: 80% of spending
- DC buildout: 18-20%
- Land/power: ~1%

### Neocloud risk

Early 2026 sentiment shifting from "build it and they will come" to [[ROIC]] focus. CoreWeave trading at discount to 2025 highs. Lambda/Together IPO windows narrowing.

Market size: GPU-as-a-service was $3.2B (2023) → projected $49.8B (2032), 36% CAGR.

See [[CoreWeave]] for detailed analysis.

---

## Sentiment shift (March 2026)

[[Bank of America]] fund manager survey (March 2026) signals institutional skepticism reaching critical mass:

| Finding | Detail |
|---------|--------|
| AI capex as credit crisis source | 30% of fund managers (most popular answer) |
| "AI bubble" as top tail risk | 25% of respondents |
| Semiconductor sector rating | Downgraded to underweight |

[[Savita Subramanian]]: "Monetization is to be determined, and power is the bottleneck and will take a while to build out." [[IBM]] CEO [[Arvind Krishna]] went further: hyperscaler spend is "economically unrecoverable at current scale."

The timing is brutal — this skepticism is arriving alongside an oil shock ([[WTI]] >$100 from [[2026 Iran conflict market impact|Iran conflict]]) that directly threatens the energy-intensive AI buildout. $650B in 2026 hyperscaler capex meets $100+ oil and -92K NFP. The stagflation collision makes the ROIC question impossible to dodge.

---

## Monetization per GW (Mar 2026)

The revenue-side pressure test of the $700B+ guide: [[Clark Tang]] ([[Altimeter Capital]], Mar 1 2026) built a cross-stack revenue-and-operating-profit-per-GW framework — infrastructure at $8-12B/GW (10-20% core rental operating margins), model providers at $22-31B/GW (50-70% estimated gross margins, inference-allocated), [[Google]]/[[Meta]] at $41-57B/GW (32-41% operating margins). Against a ~$8.5B/yr annualized cost per GW ([[Epoch AI]]), the stack clears its hurdle only through the monetization layers above raw rental — the same reason [[AWS]] had to climb from 17% operating margin (first segment disclosure, Q1 2015) to ~40% via software attach. Full numbers, methodology, and falsifiers: [[Revenue per GW]].

---

## Financing the buildout

Hyperscalers are using multiple structures:

| Structure | Example |
|-----------|---------|
| Corporate bonds | Meta $30B IG offering (2025) |
| [[Private Credit]] | Meta $30B SPV with [[Blue Owl]] |
| Project finance | GPU leasing, DC sale-leasebacks |
| Off-balance-sheet | Meta Hyperion ($50B Louisiana DC) |

[[Morgan Stanley]] estimates $1.5T total AI financing needed, $800B via private credit by 2028.

See [[AI infrastructure financing]] for details.

---

## What it means

For semiconductors:
```
Hyperscaler $ → [[NVIDIA]]/[[AMD]] → [[TSMC]] → [[SK Hynix]] ([[HBM]]) → OSAT
```

Every dollar of capex flows through the chip supply chain. $600B in 2026 = unprecedented demand.

For power:
- 1GW data center costs ~$50B
- Big 5 adding 10+ GW capacity
- See [[Power constraints]], [[BYOP]]

For credit markets:
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
- [[Revenue per GW]] — the monetization-side answer to "how is this paid for" ([[Clark Tang]], Mar 2026)
- [[Amazon]], [[Google]], [[Meta]], [[Microsoft]], [[Oracle]] — Big 5 notes
- [[CoreWeave]] — largest neocloud
- [[AI infrastructure financing]] — how it's funded
- [[Power constraints]] — physical limits
- [[BYOP]] — bring your own power trend
- [[GPU deployment bottleneck]] — shipped ≠ deployed
- [[Data center boomtown effect]] — community disruption from megaprojects
- [[Data center land competition]] — land bidding dynamics

*Created 2026-01-20*
