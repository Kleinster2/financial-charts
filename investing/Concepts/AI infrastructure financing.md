#concept #finance #datacenter #ai

The capital stack behind AI buildout. Hyperscalers need $100Bs — private credit and PE are filling the gap.

**Deep dives:**
- [[AI infrastructure deals]] — detailed capital stacks for 10 major deals
- [[GPU-as-collateral]] — CoreWeave model, 11-14% rates
- [[AI financing structures]] — Meta-Blue Owl template
- [[Neocloud financing]] — CRWV / NBIS / Google-Blackstone capital-provider map

---

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
| [[Private credit]] by 2028 | $800B |

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

See [[AI infrastructure deals]] for detailed capital stacks.

---

## May 2026 capital-provider split

The Google-Blackstone / CRWV / NBIS comparison is now part of the financing map, not just a competitive note. The same accelerated-cloud category is being funded through three different channels:

| Vehicle | Capital provider | Customer support | Risk location |
|---|---|---|---|
| [[Google-Blackstone TPU cloud venture 2026]] | [[Blackstone]] funds provide $5B initial equity; [[Alphabet|Google]] provides TPU hardware/software/services | Anchor customer not disclosed; [[Anthropic]] is the obvious candidate but not confirmed | Blackstone-backed operating-company risk, plus FT-only leverage uncertainty |
| [[CoreWeave]] / CRWV | [[NVIDIA]] equity + public equity + private credit; March 2026 $8.5B DDTL anchored by [[Blackstone]] Credit & Insurance | [[Microsoft]] concentration and backlog support the debt stack | Customer-contract / GPU-depreciation / refinancing risk |
| [[Nebius]] / NBIS | $700M strategic equity from [[Accel]], [[NVIDIA]], and [[Orbis Investments]]-managed accounts; ~$4.3375B convertible notes | [[Microsoft]] and [[Meta]] customer contracts support the buildout, but are not sponsor capital | Public-equity / convertible-market risk, with GPU-cloud execution risk |

The key distinction: Blackstone is an equity sponsor for the TPU JV but a debt/private-credit anchor around CoreWeave. Nebius is different again — it is using strategic equity and capital markets rather than a Blackstone-style infra JV. See [[Neocloud financing]] for the fuller side-by-side.

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
| [[Blackstone]] | $1.3T+ | [[QTS]], CoreWeave debt, Google-Blackstone TPU JV equity |
| [[Apollo]] | $650B+ | Meta, [[xAI]] debt |
| [[Brookfield]] | $900B+ | [[Infrastructure]] focus |

### Debt investors

| Firm | Role |
|------|------|
| [[Pimco]] | $18B anchor in Meta SPV |
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
| Private markets scale | JPMAM on Bloomberg cited ~$21T | Large enough to move the financing frontier, but not large enough to ignore manager selection and vintage risk |
| U.S./Europe power demand | JPMAM cited ~2.5% annual growth after 20 years flat | Confirms load growth is now an allocator thesis, not just a utility-planning issue |
| Infrastructure need | McKinsey's 2026 infrastructure report cites $106T global infrastructure need through 2040 and nearly $7T of data-center investment through 2030 | Capital stack must fund grids, generation, cooling, and digital infrastructure together |

No specific power plant, [[Power purchase agreement|PPA]], interconnection, grid region, or site was disclosed in the Bloomberg segment. The correct filing is therefore concept-level: private capital is crowding into the physical-services layer, but each actual deal still needs the [[Power constraints]] diligence checklist before being treated as executable capacity.

*Sources: Bloomberg Television / YouTube transcript, May 20 2026; McKinsey Global Infrastructure Report 2026; J.P. Morgan Asset Management "Why Alternatives?", data as of Mar 2026.*

---

## Hyperscaler FCF squeeze as financing catalyst (May 2026)

The May 8 FT / [[Visible Alpha]] hyperscaler cash-flow pass is now the bridge between [[Hyperscaler capex]] and this financing note. The Big 4 AI capex envelope is about $725B for 2026, but combined Q3 free cash flow is expected near $4B. That means the incremental funding question is no longer theoretical: even the strongest platform companies are funding the buildout by cutting or pausing buybacks, issuing debt, leaning on leases, and externalizing selected projects into SPVs.

| Financing pressure | Evidence | Read |
|---|---|---|
| Buyback deferral | [[Alphabet]] and [[Meta]] reported no Q1 2026 share repurchases | Cash is being retained for technical infrastructure |
| Corporate debt | Alphabet's Q1 10-Q shows $31.4B of debt proceeds; Meta's Q1 10-Q shows $59.0B senior notes outstanding | IG balance sheets are becoming part of the AI capacity stack |
| Project finance / SPVs | Meta-style off-balance-sheet data-center vehicles and Oracle/OpenAI project finance push exposure away from headline corporate debt | Reported leverage can understate economic risk |
| Metric discretion | [[Christian Leuz]] notes that free cash flow is not standardized under GAAP | FCF comparisons need lease/SBC/project-finance adjustments |

The key distinction is between a temporary cash-flow trough and a structural funding regime change. If AI revenue catches up in 2027, the trough is a working-capital bridge. If demand disappoints or component inflation persists, the same structures become the transmission channel into [[AI infrastructure financing risk]].

*Sources: [FT article](https://www.ft.com/content/b3dfaba9-17a2-4fac-90fe-4ab3ca7c9494), May 8 2026; Alphabet, Meta, and Amazon Q1 2026 10-Qs.*

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

*Updated 2026-05-19*

Sources:
- [[Bloomberg]] (Oct 31, 2025) — off-balance-sheet trend
- Morgan Stanley research

## Related

- [[AI infrastructure deals]] — detailed capital stacks (10 deals)
- [[GPU-as-collateral]] — financing concept
- [[AI financing structures]] — financing concept
- [[AI infrastructure financing risk]] — counterpoint (cascade risk)
- [[Blue Owl]] — key financier
- [[Blackstone]] — key financier
- [[CoreWeave]] — GPU-collateral pioneer
- [[Nebius]] — listed GPU neocloud capital-markets stack
- [[Google-Blackstone TPU cloud venture 2026]] — chip-backed TPU neocloud JV
- [[Neocloud financing]] — capital-provider map across CRWV / NBIS / TPU JV
- [[Meta]] — SPV template deal + Project Walleye (combined DC + power financing)
- [[EdgeConneX]] — Meta-backed DC operator, first combined DC + power loan ($3B, [[EQT]])
- [[OpenAI]] — 26 GW committed
- [[Significant risk transfer]] — banks offloading exposure
- [[Power constraints]] — capital alone isn't enough
