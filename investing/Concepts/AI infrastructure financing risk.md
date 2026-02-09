#concept #risk #ai #bear-case

# AI infrastructure financing risk

The $1.4T AI buildout may rely on circular capital flows — each player's solvency depends on others honoring commitments.

---

## Scale of buildout (Jan 2026)

Data center credit market:

| Metric | Value |
|--------|-------|
| US data center credit deals (2025) | $178.5B |
| New entrants | [[Crypto]] miners, sovereign wealth, PE firms |
| Off-balance-sheet demand | Growing ([[Meta]] $30B via Blue Owl) |

Source: Bloomberg (Jan 2026)

---

## Overbuild warnings

The bears:

| Source | Quote |
|--------|-------|
| Howard Marks (Oaktree) | Warns of potential overbuild |
| Charles Fitzgerald (platformonomics.com) | "Still waiting for a hyperscaler to launch an AI product that needs new data centers" |
| Satya Nadella ([[Microsoft]]) | "Excited to be a leaser" — outsourcing risk |
| [[Dario Amodei]] ([[Anthropic]]) | "Real dilemma" — supply-demand timing uncertainty |

Nadella's framing:
- Called potential "overbuild" a "luxury problem"
- But also signaling [[Microsoft]] wants to lease, not own
- Suggests hyperscalers cautious on own balance sheet exposure

---

## Circular deals / "Ouroboros Protocol"

*Source: Bloomberg explainer, Jan 22 2026*

Definition: Company A invests in Company B, which uses that capital to buy Company A's products — binding fortunes together. Distinct from fraudulent "round-trip" transactions (sham trades with no economic substance to inflate results).

```
[[Microsoft]] ─invest─→ [[OpenAI]] ─buys cloud─→ [[Microsoft]]
[[NVIDIA]] ─invest─→ AI labs ─buy GPUs─→ [[NVIDIA]]
[[SoftBank]] ─invest─→ OpenAI ─buys DC─→ [[Oracle]] ─buys chips─→ [[NVIDIA]]
[[Amazon]] ─invest─→ [[Anthropic]] ─buys AWS─→ [[Amazon]]
```

Bull case: Janus Henderson calls it a "virtuous circle" — lines up suppliers, builders, and customers for exploding compute demand. When chips are scarce, companies don't just place orders — they lock in supply by pairing purchase commitments with financing.

Bear case: If AI revenue doesn't grow fast enough, the flywheel reverses. Company B can't afford Company A's products → Company A's investment loses value → both cut spending → cascade.

### Chronology of circular entanglement

Bloomberg traces the evolution through five phases:

| Phase | Year | Key deals | Pattern |
|-------|------|-----------|---------|
| Cloud buys AI | 2023 | [[Microsoft]] $13B+ into [[OpenAI]] ($10B tranche early 2023) | Cloud provider funds AI lab → lab becomes cloud customer |
| Duplication | 2024 | [[Google]] up to $4B + [[Amazon]] $2B into [[Anthropic]] | Second cloud tier replicates MSFT-OpenAI template; Anthropic uses both AWS and Google chips/cloud |
| Chip vendor enters | 2025 | [[NVIDIA]] invests in [[OpenAI]], [[xAI]], [[Mistral]] | GPU maker finances customers who buy its GPUs — 3-way circularity |
| Neocloud layer | 2025 | [[NVIDIA]] 7% [[CoreWeave]] stake + $6.3B cloud purchase from CoreWeave; backs [[Nebius]], [[Nscale]] | NVIDIA invests in GPU resellers, then buys cloud from them |
| Mega-commitments | 2025-26 | OpenAI $250B [[Microsoft]] cloud + tens of billions [[AMD]] chips; [[NVIDIA]] up to $100B into OpenAI; MSFT + NVIDIA up to $15B into [[Anthropic]]; [[Amazon]] in talks for $10B+ into OpenAI | Commitment scale now exceeds most sovereign budgets |

The web tightened at each phase. By 2026, nearly every major AI transaction involves at least two of the same counterparties.

### Telecom parallel

1990s fiber-optic boom had the same dynamics. Carriers did "capacity swaps" — selling each other network capacity and recording transactions as revenue, even when deals largely washed out. Congressional investigators examined this at Qwest and Global Crossing; both restated revenue.

Paul Kedrosky (VC, former telecom analyst): AI capex is climbing toward levels last seen at the late-1990s fiber-optic peak.

Key difference from existing historical parallel section: The telecom circular deals weren't just overbuild — they involved *accounting manipulation* via swaps. The current AI deals are more transparent (public equity stakes, disclosed purchase commitments), but the economic circularity is structurally similar.

---

## Player-specific risks

| Player | Exposure | Red flag |
|--------|----------|----------|
| [[SoftBank]] | $40B OpenAI bet | 54.6% Arm concentration, margin call at -40% |
| Oracle | 57% backlog = OpenAI | CDS 124-139 bps (2008 levels), CEO selling |
| OpenAI | $115B losses through 2029 | $1.4T commitment, ~$140B secured |
| CoreWeave | 65% revenue = [[Microsoft]] | CDS 773 bps = 42% default probability |
| [[NVIDIA]] | Vendor financing | "Investment" = 3.5x GPU purchase multiplier |

---

## Infrastructure bottlenecks

| Constraint | Lead time |
|------------|-----------|
| Large power transformers | 120-210 weeks |
| Labor shortage | 300K demand vs 439K sector deficit |
| GPU obsolescence | Faster than depreciation assumptions |

See [[Power constraints]] for demand-side analysis.

---

## GPU depreciation risk (Jan 2026)

The accounting question: Are 5-6 year depreciation schedules overly optimistic?

| Estimate | Source |
|----------|--------|
| Industry standard | 5-6 years |
| Some debt deals | 10 years |
| Burry estimate (understated) | $176B (2026-2028) |

Michael Burry (of *Big Short* fame) estimates hyperscalers understating depreciation by $176B through 2028.

Industry defense:
- OpenAI CFO Sarah Friar: "confident GPUs useful for at least 5 years"
- OpenAI still using Ampere chips (released 2020) for inference
- [[NVIDIA]] CFO Colette Kress (Nov 2025): useful life "getting longer," still selling Hopper (2022)
- CoreWeave CEO: "every data point is telling a different story" — Ampere fully booked

Counterarguments:
- Older chips still useful for inference (not just training)
- Shortages force customers to take whatever available
- Secondary market exists (like used cars)

Risks if wrong:
- Write-downs on obsolete equipment
- Collateralized loans complicated
- Earlier-than-expected capex needs
- "Even a small change of several months can change earnings by billions" — Olga Usvyatsky

SEC under Trump: "Out to lunch" on scrutinizing aggressive assumptions (Francine McKenna, Montclair State).

Most exposed: Neoclouds (CoreWeave, [[Nebius]]) — smaller, often unprofitable, higher interest rates, debt-financed.

---

## New entrants rushing in (Jan 2026)

Who's building:

| Type | Examples | Strategy |
|------|----------|----------|
| [[Crypto]] miners | [[Bitdeer]], [[Nscale]], [[IREN]] | Converting mining infrastructure |
| PE/Infrastructure | [[Blue Owl]], [[Blackstone]] | Off-balance-sheet financing |
| Newcomers | [[Adriatic DC]], [[Fermi Inc]] | Greenfield mega-projects |
| Sovereign | [[GCC]] funds | National AI ambitions |

Scale of projects:
- Adriatic DC: €50B, 2GW Puglia
- [[Fermi]] Inc: 11GW Texas (Rick Perry)
- O'Leary Alberta: 17GW [[Canada]]

Many lack hyperscaler anchor tenants — speculative buildout risk.

---

## Historical parallel

1999-2001 fiber optic bubble:
- $1.7T invested
- 2.7% utilization rates
- $2T market cap destruction

Key difference: GPUs depreciate faster than fiber — compressed timeline for demand realization.

---

## Implications for theses

Adds risk to:
- [[AI hyperscalers]] — capex sustainability questioned
- [[Long Broadcom]] — depends on hyperscaler spending
- [[Long WFE]] — fab buildout tied to financing

Reinforces:
- [[Long Anthropic]] — capital efficiency matters if music stops
- [[Power constraints]] — infrastructure can't keep pace

Neutral:
- [[Long memory]] — shortage is real regardless of financing
- [[Short TSMC long Korea]] — relative value less affected

---

## Software debt disruption (Feb 2026)

*Source: Bloomberg Credit Weekly, Feb 7 2026*

AI disruption fears have moved from equity to credit markets:

| Metric | Value |
|--------|-------|
| Software leveraged loan prices | -4% YTD (through Feb 6) |
| BDC equity index | -4.6% (week of Feb 3) |
| BDC avg software portfolio exposure | >20% (Barclays) |
| Private credit default rate if aggressive AI disruption | Up to 13% (UBS) |
| Deutsche Bank failed loan sale | ~$1.2B (software acquisition) |

PE firms questioning whether SaaS debt-fueled buyout model is viable. Two European software companies shelved loan offerings amid investor unease. HSBC strategists warn against "AI exuberance" downside risks in credit.

BlackRock's Rick Rieder reducing IG and HY exposure, shifting to EM debt.

---

## What to watch

- [ ] CoreWeave refinancing success
- [ ] Oracle debt trajectory ($25B single-day issuance Feb 3)
- [ ] [[SoftBank]] margin situation
- [ ] OpenAI revenue vs burn updates
- [ ] [[Hyperscaler capex]] guidance cuts
- [ ] Software leveraged loan prices (4% YTD decline accelerating?)
- [ ] BDC earnings — software write-downs appearing?
- [ ] Private credit default rates vs UBS 13% stress scenario

---

## Counter-argument

Bulls would say:
- Hyperscalers ([[Microsoft]], [[Google]], [[Amazon]]) have balance sheets to absorb losses
- AI demand is real (coding, agents working)
- Infrastructure constraints = pricing power for winners
- Not all players are equally fragile

The risk is concentrated in second-tier players (Oracle, CoreWeave, [[SoftBank]]) — Tier 1 hyperscalers may survive while others fail.

---

## Related

- [[AI infrastructure financing]] — mechanism (how the capital flows)
- [[CoreWeave]] — fragile (CDS 773 bps, 42% default probability)
- [[Oracle]] — fragile (CDS 124-139 bps, CEO selling)
- [[Masayoshi Son]] — exposed (54.6% Arm concentration)
- [[OpenAI]] — exposed ($115B losses through 2029)
- [[Blue Owl]] — financier ([[Meta]] $30B deal, pulling from Oracle)
- [[Blackstone]] — financier (CoreWeave debt)
- [[Adriatic DC]] — new entrant (€50B Puglia, speculative)
- [[Fermi Inc]] — new entrant (11GW Texas, lost anchor tenant)
- [[Nscale]] — crypto pivot ($23B [[Microsoft]] deal)
- [[Bitdeer]] — crypto pivot (570MW Ohio)
- [[Power constraints]] — bottleneck (transformer lead times 120-210 weeks)
- [[AI hyperscalers]] — context (capex sustainability questioned)
- [[Crypto-to-AI pivot]] — conversion pattern
