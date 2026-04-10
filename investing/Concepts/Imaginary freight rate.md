---
aliases: [imaginary rates, hypothetical freight assessment, imaginary TD3C, phantom freight rate]
tags: [concept, shipping, baltic-exchange, index-methodology, hormuz, oil]
---

# Imaginary freight rate

An "imaginary freight rate" is an index assessment that panellists publish for a physical shipping route that no vessels are actually sailing. The term was popularized during the [[2026 Strait of Hormuz crisis]] to describe the [[Baltic Exchange]]'s continued publication of TD3C ([[Ras Tanura]] → [[China]] [[VLCC]]) assessments while the [[Strait of Hormuz]] was effectively closed to Western-allied shipping. The rates were still being printed daily — they just reflected what panellists believed an owner *would* charge *if* they were willing to transit, applying a risk premium large enough to make the voyage worth the potential loss of a $100M vessel.

---

## Synthesis

The imaginary freight rate is what happens when a benchmark index continues to publish through a physical-market vacuum. It is not a data error — it is a deliberate methodology choice by the index provider to continue serving downstream financial instruments (futures contracts, ETFs, charter contracts) that need a daily print. The cost of that choice is that the benchmark stops reflecting reality and starts reflecting what reality *would* be under counterfactual conditions. In extreme disruptions — [[Strait of Hormuz|Hormuz]] closure, European power crises, April 2020 WTI — this gap between published number and physical transactability becomes the dominant driver of P&L for anyone holding instruments referenced to the benchmark.

The concept matters because these hypothetical assessments feed real financial instruments: TD3C futures cleared on [[ICE]], the settlement index for the [[BWET]] ETF, Worldscale benchmarking for physical fixtures, and owner-charterer negotiations for routes that actually can be sailed. When the reference rate is imaginary, the instruments built on top of it are too.

---

## Why the rate becomes imaginary

The [[Baltic Exchange]] publishes TD3C as a daily assessment from a panel of ship brokers. The panel is asked: *what rate would a standard Baltic VLCC command for a voyage loading at [[Ras Tanura]] today?* In normal markets, panellists reference actual fixtures — deals that closed yesterday, ships currently being negotiated — and submit their best estimate. The published index is a consensus of those estimates.

During the March 2026 Hormuz closure, no tankers were broadcasting AIS inside the strait (by March 2, midnight — [[IRGC]] confirmed closure); P&I clubs had withdrawn war-risk coverage effective March 5; commercial owners refused to transit regardless of price — "no longer bear that risk" (Baltic panellist commentary, hellenic shipping news, week of March 9); and [[Iran]] was charging up to $2M per alternate-channel transit, explicitly selecting vessels by flag and ownership.

With no fixtures closing on TD3C-compliant terms, panellists had three options: stop publishing (the Baltic's emergency procedure for when "reference data are no longer available"); publish a nominal (a placeholder reflecting market absence, not a price); or continue to publish using hypothetical pricing — a risk premium applied to the last-known normal-market rate, or a reference fixture from [[Yanbu]] with a Hormuz transit premium added back in. The Baltic chose the third option.

---

## The Lloyd's List "imaginary" framing (March 2026)

Lloyd's List ran a piece titled **"How 'imaginary' Middle East VLCC rates are having real-world effects"** (mid-March 2026). The key findings:

- The Baltic Exchange issued a circular stating it was "consulting with its panellists and advisory councils as a routine part of how we respond to periods of heightened market uncertainty."
- A spokesperson confirmed that panellists "providing assessments for TD3C can reference Yanbu fixtures but they need to apply a risk premium that the owner could accept to transit inside the Strait."
- "All Baltic indexes are treated separately and the panellists providing data for TD3 are still able to provide daily assessments, so the Baltic continues to publish the TD3 daily."
- The Lloyd's List correspondent's assessment: "An index that measures what the freight rate is for a VLCC with insurance that will transit the Strait of Hormuz — at a time it cannot transit the strait due to war — is very hypothetical."

[[Frontline]] CEO [[Lars Barstad]] on the firm's March 4 conference call: *"The TD3C index, and indexes in general, have much wider market implications than they used to."* Barstad was making a structural point — freight indices are no longer just reporting tools, they are increasingly the referenced benchmarks for listed funds, derivatives, and charter contracts. When the benchmark's ability to reflect reality breaks down, the downstream instruments inherit that breakdown.

---

## The TD34 emergency alternative

By late March 2026, the Baltic Exchange acknowledged the problem by launching an emergency alternate route — TD34 — on public trial, defined as 270,000mt [[Gulf of Oman]] to China, loading outside the Strait of Hormuz. TD34 was designed to capture actual fixtures for Gulf-origin crude being shipped from rerouted loading points ([[Fujairah]], Yanbu via [[East-West Pipeline]]), bypassing the Hormuz closure entirely.

The launch of TD34 is an implicit admission that TD3C had become disconnected from physical reality. But it did not stop TD3C publication — the two indices now run in parallel, with TD3C functioning as a hypothetical "closed-route premium" index and TD34 as the actual reference for Gulf crude flows.

---

## Why the imaginary rate still moves markets

A reasonable question: if the rate is hypothetical and no one is actually chartering at it, why does it matter? Three reasons.

First, it settles futures. TD3C FFAs clear on [[ICE]] and settle against the Baltic assessment. Every $1,000/day move in the published index translates to P&L for futures holders regardless of whether any physical voyage occurs.

Second, it marks NAV for [[BWET]]. The [[Breakwave Advisors|Breakwave]] tanker ETF holds near-dated TD3C FFAs. Its daily NAV — and therefore the price retail investors buy and sell at — is driven by the published index, not by any actual fixture.

Third, it anchors negotiations. Physical charterers still need a reference point for negotiating alternative routes. Even when TD3C is imaginary, it becomes the baseline that TD34 and [[Yanbu]] fixtures are discussed against.

The result is a circular structure: the [[Baltic Exchange]] publishes an imaginary number → the FFA market prices against it → [[BWET]] marks to it → flows into [[BWET]] create hedging demand → panellists see that demand and adjust their assessments → a new imaginary number is published. During the March-April 2026 run, this structure compounded upward until BWET was up more than 8x YTD.

---

## Precedent and parallels

*Electricity during grid crises.* When European day-ahead power prices spiked in 2022 after the [[Ukraine]] invasion, some hubs printed extreme clearing prices on zero or near-zero actual volume. The published prices still settled derivatives and formed the basis for consumer tariffs, even though the physical spot market had thin to no liquidity at those levels.

*Dry bulk during COVID.* The 2020 BDI spike (and later the 2021-22 commodities run that drove [[BDRY]] up 390%) included brief periods where routes like C5 (West [[Australia]] → [[China]]) printed assessments during physical port closures. The pattern was less extreme than Hormuz 2026 but showed the same structure: index publication continuing through disruption.

*Oil benchmarks during 2020 WTI collapse.* The April 2020 [[WTI]] futures contract closed at -$37.63 on a day when deliverable storage at [[Cushing]] was effectively full and no meaningful physical trades could clear. The published price was technically "real" but was an artifact of contract mechanics, not physical scarcity — the mirror image of a route-closure imaginary rate, where the published number is an artifact of index mechanics during physical absence.

---

## The investment implication

For anyone holding instruments that reference chokepoint-exposed freight benchmarks, the imaginary rate phenomenon introduces a specific risk: benchmark mean-reversion can outpace physical mean-reversion. When Hormuz reopens, the Baltic will revert TD3C toward actual-fixture levels within days. But the underlying vessels will still be scattered across [[Atlantic basin]] voyages for weeks; physical rates (the rates owners actually capture) will not drop as quickly as the published index. The published index is what marks the FFAs and the ETF. Holders of [[BWET]] or long TD3C futures could see NAV collapse while the underlying shipping companies ([[Frontline]], DHT Holdings) still report record quarterly earnings from voyages already under way.

The inverse is also true during escalation: a published imaginary rate can rise faster than any owner could actually charge, because panellists can hypothesize risk premia without market-testing them. This is what drove BWET's 800%+ YTD move — the index led the physical market up, because the physical market had stopped trading.

---

## Related

- [[BWET]] — the ETF that trades against imaginary TD3C
- [[Breakwave Advisors]] — sub-advisor of BWET
- [[Baltic Exchange]] — publishes TD3C assessment
- [[VLCC]] — vessel class TD3C references
- [[Ras Tanura]] — TD3C loading port (inside Hormuz)
- [[Yanbu]] — alternative loading point via [[East-West Pipeline]]
- [[2026 Strait of Hormuz crisis]] — event producing the imaginary-rate regime
- [[Strait of Hormuz]] — the physical chokepoint
- [[Hormuz Permanent Risk Premium]] — structural thesis
- [[Hormuz Transit Regime]] — selective passage rules
- [[Frontline]] — [[Lars Barstad]] commentary on index methodology
- [[Shipping]] — sector hub
- [[Atlantic basin]] — alternative sourcing during Gulf closure

*Created 2026-04-09*
