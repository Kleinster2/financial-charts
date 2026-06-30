#concept #finance #datacenter #ai

The capital stack behind AI buildout. Hyperscalers need $100Bs; [[Private Credit]], PE, debt markets, partner vehicles, customer offtake, and now common-equity issuance are filling the gap.

**Deep dives:**
- [[AI infrastructure deals]] — detailed capital stacks for 10 major deals
- [[GPU-as-collateral]] — CoreWeave model, 11-14% rates
- [[AI financing structures]] — Meta-Blue Owl template
- [[Neocloud financing]] — CRWV / NBIS / Google-Blackstone capital-provider map

---

## Synthesis

AI infrastructure financing has moved from a hyperscaler cash-flow question into a full capital-market regime. The buildout now uses corporate debt, project finance, GPU-collateralized credit, private-capital SPVs, customer offtake, IPO primary equity, and direct hyperscaler equity issuance. [[Alphabet equity raise June 2026]] and the [[Meta]] exploration show that common equity is now part of the stack, while the [[Nasdaq semiconductor selloff June 2026]] shows why that channel is fragile: higher rates can close the valuation window before the physical demand story changes. Capital is therefore necessary but not sufficient; each financing structure still has to clear [[Power constraints]], customer-concentration risk, and deployment timing.

Chart data not applicable: this note maps financing structures rather than a single tradeable price series. Market-window stress is tracked through [[QQQ]], [[SOXX]], [[SMH]], and the linked event tape.

## Gigawatt economics

Three different $-per-GW metrics — don't confuse them:

| Metric | $/GW | What it means |
|--------|------|---------------|
| Funding milestone | ~$10B | Capital unlocked per GW deployed |
| Revenue | ~$10B | Current revenue generated per GW (may not scale) |
| Build cost | $12-50B | Actual cost to construct 1 GW |

### Why funding < build cost

If it costs ~$30B to build 1 GW but investors commit ~$10B per GW, where's the gap?

| Source | Role |
|--------|------|
| [[Microsoft]] | Azure credits, existing investment |
| Revenue | $20B ARR funds some capex |
| Chip partner deals | [[NVIDIA]]/[[AMD]] provide hardware at favorable terms |
| [[AI financing structures]] | Sale-leasebacks, JVs |
| Debt | Bank financing, bonds |

The $10B/GW milestone is just one layer. Full builds use multiple capital sources.

### OpenAI capacity trajectory

| Year | Capacity | Revenue |
|------|----------|---------|
| 2023 | 0.2 GW | ~$2B |
| 2025 | 1.9 GW | $20B |
| [[Target]] | 26 GW | ? |

Critical question: Does the 1:1 compute-revenue relationship hold at 10x+ scale?

---

## The financing gap

| Metric | Value |
|--------|-------|
| 2025 hyperscaler AI capex | ~$300B |
| 2026 projected | $620B |
| Morgan Stanley DC spend by 2028 | $3T |
| Total external financing needed | $1.5T |
| [[Private Credit]] by 2028 | $800B |

Problem: Even hyperscalers don't want this on balance sheet. Enter private capital.

[[UBS]] warning (Oct 2025): "raises eyebrows for anyone that has seen credit cycles."

---

## Deal structures

| Structure | How it works | Example |
|-----------|--------------|---------|
| [[AI financing structures]] | PE takes 80%, hyperscaler leases back | Meta-Blue Owl $60B |
| [[GPU-as-collateral]] | GPUs secure debt, 11-14% rates | CoreWeave $7.5B ("The [[Box]]") |
| Construction JV | Bank finances build, long-term lease | Crusoe-JPMorgan $15B |
| Combined DC + power | Single loan covers building and on-site generation | Meta/[[EdgeConneX]] "Walleye" $3B |
| Chip vendor equity | [[NVIDIA]]/[[AMD]] invest for supply lock | OpenAI-[[NVIDIA]] $100B |
| Strategic cloud equity + offtake | Cloud provider invests in frontier lab while lab commits to buy cloud/chip capacity | [[Anthropic hyperscaler financing surge April 2026]] ([[Amazon]] + [[Google]]) |
| Chip-backed neocloud JV | Chip vendor supplies silicon/software while private capital funds a separate operating company | [[Google-Blackstone TPU cloud venture 2026]] |
| Listed neocloud capital markets | Strategic equity + convertible notes fund GPU-cloud buildout; customers provide demand anchors | [[Nebius]] $700M strategic equity + ~$4.3375B convertibles |
| Hyperscaler equity issuance | Mega-cap issuer sells stock / equity-linked securities to fund AI infrastructure and tax/share-compensation mechanics | [[Alphabet equity raise June 2026]] ($85B per FT after upsizing); [[Meta]] exploration |
| IPO primary equity | Private platform sells public common stock to fund AI compute plus launch/satellite capacity | [[SpaceX IPO 2026]] |
| Compute-capacity offtake | AI lab or hyperscaler signs multi-year lease for GPU capacity; contract supports utilization but is not sponsor capital | [[SpaceX]] / [[Google Cloud]] Jun. 2026 lease; [[Anthropic]] Colossus capacity |
| Data-center lease-backed HY note | Note secured by a pre-arranged data-center lease (often to a hyperscaler, sometimes agreed before construction); construction-loan-inspired structures sold to high-yield investors | [[Stingray Compute]] (Cipher Digital) $810M, Jun 2026 — 9× oversubscribed, lease backed by [[Amazon]] |

See [[AI infrastructure deals]] for detailed capital stacks.

---

### SpaceX IPO primary equity (Jun. 2026)

The Jun. 4 [[SpaceX IPO 2026]] FWP adds public IPO equity to the AI-infrastructure financing map. [[SpaceX]] is offering 555.6M primary Class A shares at an expected $135/share, or roughly $75.0B of base gross proceeds, with a 15% primary over-allotment that would add about $11.25B at that price. The use-of-proceeds language explicitly includes AI compute infrastructure, but it also includes launch infrastructure and vehicles, satellite-constellation scale/capacity, and general corporate purposes.

That makes the structure different from a clean data-center SPV. Public investors are funding the integrated stack: terrestrial compute, [[xAI]] / [[Grok]] distribution, [[Starlink]] constellation expansion, and the launch infrastructure needed to scale V3 satellites, V2 mobile, and future orbital compute. The financing read is therefore broader than "AI data center capital raise." It is common-equity funding for a vertically integrated AI / space platform whose bottlenecks sit across chips, power, launch cadence, satellites, and balance-sheet leverage.

*Sources: [[SEC]] S-1/A filed Jun. 3 2026; [[SEC]] FWP filed Jun. 4 2026; see [[SpaceX IPO 2026]].*

### Customer offtake as IPO de-risking (Jun. 2026)

FT's Jun. 5 Google update adds a second, non-equity support channel to the SpaceX IPO financing story: customer offtake. [[Google Cloud]] is paying $920M/month for access to 110,000 [[NVIDIA]] GPUs plus supporting components through Jun. 2029 unless canceled earlier, while FT says [[Anthropic]]'s SpaceX capacity agreements include 325,000 [[NVIDIA]] GPUs at [[Colossus]] facilities in Tennessee. Together, the Google and Anthropic agreements would contribute >$26B of annual SpaceX revenue.

This is not capital raised by SpaceX, but it can serve the same underwriting function: it shows public investors that new AI compute capacity has identifiable external buyers. The risk is cancellation/customer concentration and the fact that the economics still depend on [[NVIDIA]] GPU capacity rather than proprietary [[TERAFAB]] chips.

*Source: FT, Jun. 5 2026: https://www.ft.com/content/77982a06-7d75-45a4-a64f-f8dc89a6a626.*

---

## May 2026 capital-provider split

The Google-Blackstone / CRWV / NBIS comparison is now part of the financing map, not just a competitive note. The same accelerated-cloud category is being funded through three different channels:

| Vehicle | Capital provider | Customer support | Risk location |
|---|---|---|---|
| [[Google-Blackstone TPU cloud venture 2026]] | [[Blackstone]] funds provide $5B initial equity; [[Google]] provides [[TPU]] hardware/software/services | Anchor customer not disclosed; [[Anthropic]] is the obvious candidate but not confirmed | Blackstone-backed operating-company risk, plus FT-only leverage uncertainty |
| [[CoreWeave]] / CRWV | [[NVIDIA]] equity + public equity + private credit; March 2026 $8.5B DDTL anchored by [[Blackstone]] Credit & [[Insurance]] | [[Microsoft]] concentration and backlog support the debt stack | Customer-contract / GPU-depreciation / refinancing risk |
| [[Nebius]] / NBIS | $700M strategic equity from [[Accel]], [[NVIDIA]], and [[Orbis Investments]]-managed accounts; ~$4.3375B convertible notes | [[Microsoft]] and [[Meta]] customer contracts support the buildout, but are not sponsor capital | Public-equity / convertible-market risk, with GPU-cloud execution risk |

The key distinction: Blackstone is an equity sponsor for the [[TPU]] JV but a debt/private-credit anchor around CoreWeave. Nebius is different again — it is using strategic equity and capital markets rather than a Blackstone-style infra JV. See [[Neocloud financing]] for the fuller side-by-side.

---

## CoreWeave's "[[Box]]" structure (Davos, Jan 2026)

Mike Intrator explained the neocloud financing innovation:

| Component | What goes in "The [[Box]]" (SPV) |
|-----------|------------------------------|
| Collateral | GPUs |
| Revenue | Offtake contract (e.g., 5-year Microsoft deal) |
| Costs | Data center contract + PPA |

Waterfall:
1. Power costs
2. Data center costs
3. Principal + interest
4. Then CoreWeave gets paid

Key insight: "Pay me my goddamn money back" — Intrator's summary of East Coast capital's only rule. CoreWeave doesn't touch revenue until obligations cleared.

The "equity slug": After contract term (5 years), debt is paid off and CoreWeave owns GPUs outright. Intrator believes residual value exists despite depreciation concerns.

Not speculative: GPUs are pre-sold to counterparties before purchase. Only the "long pole" (physical data centers) is risk capital.

See [[CoreWeave]] for full business model.

---

## Key players

### PE / Alternative managers

| Firm | AUM | AI infra exposure |
|------|-----|-------------------|
| [[Blue Owl]] | $273B | Meta $27B, Crusoe — largest AI infra financier |
| [[Blackstone]] | $1.3T+ | [[QTS]], CoreWeave debt, Google-Blackstone [[TPU]] JV equity |
| [[Apollo]] | $650B+ | Meta, [[xAI]] debt |
| [[Brookfield]] | $900B+ | [[Infrastructure]] focus |

### Debt investors

| Firm | Role |
|------|------|
| [[PIMCO]] | $18B anchor in Meta SPV |
| [[BlackRock]] | $3B+ Meta, infrastructure fund |

### [[Banks]]

| Bank | Role |
|------|------|
| [[Morgan Stanley]] | SPV structuring (Meta, [[xAI]]) |
| [[JPMorgan Chase]] | Construction loans (Crusoe $9.6B) |

---

## OpenAI Deployment Company (May 2026)

The [[Brookfield OpenAI deployment platform May 2026]] event adds a services/deployment layer to the AI financing stack. Brookfield agreed to invest $500M in The OpenAI Deployment Company, a new platform built with [[OpenAI]] and global investors to move enterprises from AI pilots to scaled workflow redesign.

This is not data-center project finance, but it belongs in the financing map because it is the demand-conversion layer for the same capex cycle. If model labs and hyperscalers keep spending hundreds of billions on compute, someone has to turn that capacity into enterprise productivity. The Deployment Company is an attempt to securitize/industrialize the messy adoption work through forward-deployed engineers, consulting partners, and private-equity portfolio access.

| Layer | Financing question | May 2026 data point |
|-------|--------------------|---------------------|
| Physical AI infra | Who funds chips, power, data centers? | Blue Owl, Brookfield, banks, SPVs |
| Enterprise adoption | Who converts compute into ROI? | OpenAI Deployment Company |
| Investor return | Who captures productivity gains? | PE operating partners + OpenAI majority economics |

*Sources: OpenAI announcement and Brookfield 8-K / GlobeNewswire, May 11 2026; Axios DeployCo valuation reporting, May 11 2026.*

---

## Private-market power constraint read (May 20, 2026)

The JPMorgan Asset Management private-markets segment on Bloomberg adds a useful allocator-side confirmation to the financing map. The "AI infrastructure" trade is not just GPU debt, neocloud SPVs, or data-center real estate. It is also the regulated and quasi-regulated power/water/utility layer that converts capital into powered capacity.

Three data anchors:

| Data point | Source / attribution | Read |
|------------|----------------------|------|
| [[Private markets]] scale | JPMAM on Bloomberg cited ~$21T | Large enough to move the financing frontier, but not large enough to ignore manager selection and vintage risk |
| U.S./[[Europe]] power demand | JPMAM cited ~2.5% annual growth after 20 years flat | Confirms load growth is now an allocator thesis, not just a utility-planning issue |
| Infrastructure need | [[McKinsey]]'s 2026 infrastructure report cites $106T global infrastructure need through 2040 and nearly $7T of data-center investment through 2030 | Capital stack must fund grids, generation, cooling, and digital infrastructure together |

No specific power plant, [[Power purchase agreement|PPA]], interconnection, grid region, or site was disclosed in the Bloomberg segment. The correct filing is therefore concept-level: private capital is crowding into the physical-services layer, but each actual deal still needs the [[Power constraints]] diligence checklist before being treated as executable capacity.

*Sources: Bloomberg Television / [[YouTube]] transcript, May 20 2026; [[McKinsey]] Global Infrastructure Report 2026; J.P. Morgan Asset Management "Why Alternatives?", data as of Mar 2026.*

---

## Hyperscaler FCF squeeze as financing catalyst (May 2026)

The May 8 FT / [[Visible Alpha]] hyperscaler cash-flow pass is now the bridge between [[Hyperscaler capex]] and this financing note. The Big 4 AI capex envelope is about $725B for 2026, but combined Q3 free cash flow is expected near $4B. That means the incremental funding question is no longer theoretical: even the strongest platform companies are funding the buildout by cutting or pausing buybacks, issuing debt, leaning on leases, and externalizing selected projects into SPVs.

| Financing pressure | Evidence | Read |
|---|---|---|
| Buyback deferral | [[Alphabet]] and [[Meta]] reported no Q1 2026 share repurchases | Cash is being retained for technical infrastructure |
| Corporate debt | Alphabet's Q1 10-Q shows $31.4B of debt proceeds; Meta's Q1 10-Q shows $59.0B senior notes outstanding | IG balance sheets are becoming part of the AI capacity stack |
| Project finance / SPVs | Meta-style off-balance-sheet data-center vehicles and Oracle/OpenAI project finance push exposure away from headline corporate debt | Reported leverage can understate economic risk |
| Metric discretion | [[Christian Leuz]] notes that free cash flow is not standardized under [[GAAP]] | FCF comparisons need lease/SBC/project-finance adjustments |

The key distinction is between a temporary cash-flow trough and a structural funding regime change. If AI revenue catches up in 2027, the trough is a working-capital bridge. If demand disappoints or component inflation persists, the same structures become the transmission channel into [[AI infrastructure financing risk]].

*Sources: [FT article](https://www.ft.com/content/b3dfaba9-17a2-4fac-90fe-4ab3ca7c9494), May 8 2026; Alphabet, Meta, and Amazon Q1 2026 10-Qs.*

### Alphabet equity issuance as new funding channel (Jun 2026)

The Jun 1 [[Alphabet equity raise June 2026]] turns the May 2026 FCF squeeze into an explicit equity-market financing channel. Alphabet's initial package was up to $80B of equity funding: $15B of Class A / Class C common stock, $15B of mandatory-convertible preferred/depositary shares, a $40B at-the-market Class A / Class C program, and $10B privately placed with [[Berkshire Hathaway]]. FT's Jun. 5 Meta follow-up described the transaction as a record $85B share deal after a $5B increase on strong demand. That sits beside the existing debt stack rather than replacing it; FT also reported $85B of fresh debt and more than $100B of total debt.

The taxonomy implication is important: the AI infrastructure funding map no longer stops at "hyperscaler balance sheet vs private-credit SPV." It now includes direct dilution at the mega-cap platform layer. That is still cheaper and cleaner than distressed borrowing, but it changes the investor bargain: shareholders are funding capacity in exchange for future AI revenue, not merely accepting lower buybacks while operating cash flow covers the build.

*Sources: [FT - Alphabet to sell $80bn in stock to fund AI spending spree](https://www.ft.com/content/341f151b-f472-4530-8579-d4b803519257), Jun 1 2026; Alphabet 424B5 supplements, Jun 2 2026; [FT](https://www.ft.com/content/e6df645d-1709-4a77-b15d-aa43a0209efd), Jun. 5 2026.*

### Meta peer follow-through watch (Jun 2026)

FT's Jun. 5 [[Meta]] report turns Alphabet's stock offering from an idiosyncratic Google funding event into a possible peer category. Meta is considering a tens-of-billions stock sale after Alphabet's $85B deal was upsized by $5B on demand, with [[Susan Li]] and [[Dina Powell McCormick]] leading internal talks. The important caveat is status: Meta has not hired banks and may not issue equity.

If Meta proceeds, the funding taxonomy changes again. The AI buildout would have moved through four listed-hyperscaler pressure valves in sequence: debt issuance, buyback suspension, off-balance-sheet / private-capital data-center vehicles, and then direct common-equity or equity-linked issuance. That means dilution is no longer just an Alphabet-specific implementation detail; it becomes a live funding channel for any hyperscaler whose capex guide is outrunning operating cash flow and investor tolerance.

No new power plant, [[Power purchase agreement]], interconnection, grid region, or MW target was disclosed. This is a capital-stack story, not a new physical-capacity asset.

*Source: [FT](https://www.ft.com/content/e6df645d-1709-4a77-b15d-aa43a0209efd), Jun. 5 2026.*

### Market-window stress test (Jun 5 2026)

The Jun. 5 [[Nasdaq semiconductor selloff June 2026]] adds the market-window side of the same funding story. The day was not an announced financing failure: it was a rates shock after a strong payrolls report. But it hit exactly the assets whose valuations make the AI buildout financeable: [[Nasdaq]] Composite -4.18%, [[QQQ]] -4.80%, [[SOXX]] -10.44%, and [[SMH]] -9.22% in local close data.

The financing implication is that common equity is now both a solution and a vulnerability. [[Alphabet]] showed the market can absorb an $85B AI-infrastructure raise; [[Meta]] showed a second hyperscaler may test the same channel; the Jun. 5 tape shows that the same channel can become expensive quickly if higher yields compress AI-duration multiples before issuers launch.

For deal taxonomy, this does not create a new structure. It changes the risk attached to the existing structures: IPO primary equity, hyperscaler equity issuance, convertibles, ATMs, and equity-linked securities all depend on a friendly market window. When that window weakens, the buildout leans harder on debt, private credit, leases, and customer offtake.

*Sources: [FT](https://www.ft.com/content/2929bbd3-1f71-4424-a577-f016c3c65603), Jun. 5 2026; local `prices_long` closes through Jun. 5 2026.*

---

## June 2026 — currency diversification and the lease-backed HY note

A [[Reuters]] round-up (Tatiana Bautzer, Gertrude Chavez-Dreyfuss, Jun 29 2026) marks the point at which AI-debt volume forced two structural shifts: currency diversification to avoid dollar saturation, and a new high-yield structure built around pre-arranged data-center leases.

| Data point | Figure | Source |
|---|---|---|
| AI-related share of US IG issuance | ~15% of total IG this year | [[Barclays]] |
| Hyperscaler 2026 capex | ~$725B, nearly double mid-2025 | [[BNP Paribas]] |
| 2026 hyperscaler IG debt forecast | $250B | [[BNP Paribas]] |
| Potential 2026 total IG issuance | >$2T (first time ever) | [[Morgan Stanley]] |
| Amazon + Alphabet multi-currency bonds (last 12 mo) | $60B across currencies | [[Reuters]]/[[LSEG]] |
| Amazon euro deal (Mar 2026) | €14.5B / $16.56B, 8-part — largest euro corporate bond ever | [[LSEG]] |
| Alphabet multi-currency records | Yen, CAD, CHF, GBP all set borrowing records; first 100-year tech bond since 1997 | [[LSEG]] |
| Alphabet outstanding debt | $100B across six major currencies | Anat Ashkenazi (CFO) |

The new structure is the data-center lease-backed HY note. The marquee example is [[Stingray Compute]] (owned by Cipher Digital, CIFR.O), which issued an $810M note in June backed by its data-center lease to [[Amazon]] — 9× oversubscribed, per Morgan Stanley's Cody Gunsch. Roughly 15 such construction-loan-inspired deals have been sold to high-yield investors since the structure began last year. The economic logic mirrors the [[CoreWeave]] "Box": a pre-arranged hyperscaler lease converts an uncertain future cash flow into securitizable collateral, letting sub-IG operators fund builds that would otherwise sit on a hyperscaler's balance sheet.

Demand still holds despite the supply surge. IG hyperscaler deals have already surpassed their full-year 2025 total and are on pace for BNP Paribas' $250B forecast. Barclays' Scott Schulte flagged the offset: AI debt is ~15% of recent IG issuance but still a small share of total debt in the broader IG credit indices, so concentration risk is rising but not yet index-breaking. The open question (Morgan Stanley's Hodgson) is whether equity issuance — Alphabet's $80–85B raise, Meta's exploration — previews a parallel jump in debt needs, since capex is outrunning operating cash flow (the May FCF-squeeze dynamic above). Jeff Given (Manulife) framed the durability test: demand stays as long as hyperscalers and data centers keep raising spend.

*Source: [[Reuters]] (Tatiana Bautzer, Gertrude Chavez-Dreyfuss), "Banks get creative and look further afield as AI-fueled debt soars," Jun 29 2026; underlying data from [[LSEG]], [[Barclays]], [[BNP Paribas]], [[Morgan Stanley]].*

---

## Risks

### The dot-com comparison

| Era | How financed | What happened |
|-----|--------------|---------------|
| Dot-com (2000) | Equity | Burst had limited economic impact |
| AI (2025) | Debt (off-balance-sheet) | TBD — credit cycles hit harder |

Off-balance-sheet history:
- 2001: [[Enron]] — SPVs hid liabilities
- 2008: [[Banks]] moved mortgages off-balance-sheet
- 2025: Tech companies using SPVs for AI infrastructure

### Bank concentration risk

[[Banks]] becoming overexposed to few AI borrowers:
- [[Oracle]] CDS spike — lenders buying protection
- SRT exploration — Morgan Stanley considering offload

See [[Significant risk transfer]], [[AI infrastructure financing risk]].

---

## Investment implications

Direct plays:
- [[Blue Owl]] (OWL) — largest AI infra financier
- Blackstone (BX) — diversified, big DC exposure
- Data center [[REITs]] (EQIX, DLR)

Indirect beneficiaries:
- Power providers ([[Constellation Energy]], [[Vistra]])
- Hyperscalers preserving balance sheet flexibility

Who loses:
- Hyperscalers who can't access financing (weaker credit)
- Smaller AI companies competing for limited capital

---

## For theses

- [[AI hyperscalers]] — financing enables buildout
- [[Power constraints]] — capital alone isn't enough
- [[Long memory]], [[Long TSMC]] — financing enables chip demand

---

*Updated 2026-06-06*

Sources:
- [[Bloomberg]] (Oct 31, 2025) — off-balance-sheet trend
- Morgan Stanley research

---

## The borrower's-eye view (Friar, Jun 2026)

[[Sarah Friar]] ([[OpenAI]] CFO) described the structure from the inside at [[Liquidity 2026]] (All-In, Jun 2 2026): "what CSPs do for us, in effect, is they shift capex into opex. You pay as you get the revenue... we are riding somewhat on their ability to build and have capex and financing." The stated reason is credit, not preference: "I'm not yet an investment-grade type of entity where I can go get lower-cost debt financing" — so OpenAI rents investment-grade balance sheets ([[Oracle]], [[Microsoft]], [[Amazon]], [[Google]], [[CoreWeave]]) instead of borrowing on its own. The first step back toward owned capex is built-to-suit: a [[SoftBank]] (SB Energy) data center in Texas — "a little bit more capex required there." This is the same structure [[AI infrastructure financing risk]] describes from the outside: the buildout's credit risk concentrates on CSP balance sheets precisely because the anchor customer is sub-investment-grade.

## Demand-side counter: RPO outpacing capex (Baratte, TechStock01, Jun 29)

[[Nicolas Baratte]] (TechStock01, Jun 29 2026) makes the demand-side case against the "AI peak / FCF squeeze → capex cut" framing that drove the late-June drawdown. The valuation point first: AI semis trade at ~17.7x forward earnings (around their average), and hyperscalers at ~21.1x (-1 standard deviation). The rally is earnings growth, not multiple expansion — Micron's Jun 24 blowout is the canonical example. The FCF squeeze is real (combined Alphabet/Amazon/Meta/Microsoft FCF near zero, net cash near zero, debt issuance started), but it sits alongside accelerating cloud revenue (~22% YoY in 2024 → ~35% now), expanding margins, and combined hyperscaler EBITDA around $700B and rising.

The distinctive data point is Remaining Performance Obligations (RPO) — hyperscalers' committed future cloud revenue. Baratte's ratio: $1 of capex used to generate ~$0.5 of committed future revenue; the current ratio is ~$1 capex → ~$3 committed future revenue. Even allowing for a possibly-extended RPO time-horizon and new-product effects, committed future revenues are growing materially faster than capex.

The read-through for the financing map is that the FCF-squeeze "long and variable lag" between capex and revenue is resolving in the hyperscalers' favor: demand is arriving faster than the bear case assumes, which is why debt issuance is absorption rather than distress. This is the demand-side counterpart to the supply-wall threads (Korea $576B, CXMT doubling) ingested the same day — together they frame 2026–27 as a race between demand-pull and supply-delivery rather than a glut forming in a weakening market. The risk the framework does not resolve: RPO is a commitment, not booked revenue, and a demand air-pocket would still leave the debt stack exposed (the [[AI infrastructure financing risk|financing-risk]] counterpoint).

*Source: [[Nicolas Baratte]] / TechStock01, "AI is a fake, AI is a bubble, again? Hyperscalers' committed future revenue (RPO) tells a different story," Jun 29 2026.*

## Related

- [[AI infrastructure deals]] — detailed capital stacks (10 deals)
- [[GPU-as-collateral]] — financing concept
- [[AI financing structures]] — financing concept
- [[AI infrastructure financing risk]] — counterpoint (cascade risk)
- [[Hyperscaler capex]] — demand-side capex envelope that creates the funding need
- [[Revenue per GW]] — whether the financed capacity earns its hurdle (monetization per GW by layer)
- [[Blue Owl]] — key financier
- [[Blackstone]] — key financier
- [[CoreWeave]] — GPU-collateral pioneer
- [[Nebius]] — listed GPU neocloud capital-markets stack
- [[Google-Blackstone TPU cloud venture 2026]] — chip-backed [[TPU]] neocloud JV
- [[Neocloud financing]] — capital-provider map across CRWV / NBIS / [[TPU]] JV
- [[SpaceX IPO 2026]] — IPO primary equity and customer-offtake case
- [[HOF Capital]] — private VC / LP-network platform with AI infrastructure and frontier-tech portfolio exposure
- [[Extropic]] — thermodynamic-computing option on the AI compute supply curve
- [[Meta]] — SPV template deal + Project Walleye (combined DC + power financing)
- [[EdgeConneX]] — Meta-backed DC operator, first combined DC + power loan ($3B, [[EQT]])
- [[OpenAI]] — 26 GW committed
- [[Significant risk transfer]] — banks offloading exposure
- [[Power constraints]] — capital alone isn't enough
- [[AI hyperscalers]]
