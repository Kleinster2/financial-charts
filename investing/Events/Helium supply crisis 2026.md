---
aliases: [helium shortage 2026, helium crisis, Qatar helium shutdown, Hormuz helium disruption]
tags: [event, supply-chain, semiconductor, iran, helium]
---

# Helium supply crisis 2026

The removal of ~30% of global commercial [[Helium]] supply following [[QatarEnergy]]'s [[Ras Laffan]] shutdown (March 2) and the [[Strait of Hormuz]] closure. [[Helium]] is a byproduct of natural gas processing — when LNG stops, helium stops. The semiconductor industry is now helium's largest consumer (surpassing MRI), making this a direct supply chain threat to AI chip fabrication.

---

## Synthesis

This is the semiconductor supply chain's version of the [[Nitrogen Trap]] — a critical input that nobody hedged because it was always abundant and cheap. Helium accounts for <1% of wafer processing cost, so fabs will pay any price to keep running ([[Linx Consulting]]'s Mike Corbett: *"You're not going to shut down a fab because you have to double your helium price"*). But the constraint is physical, not financial: 30% of global supply is offline with no restart timeline, ~2,000 cryogenic containers are stuck in [[Qatar]] or in transit, and the containers themselves leak 0.1-1% per month — stranded inventory is a wasting asset.

The market is not yet pricing the duration risk. Phil Kornbluth (Kornbluth Helium Consulting, 30-year veteran) frames it: *"It's kind of like a nice sunny day on the beach, but you heard there's a tsunami out there."* Helium shipped before the war is still arriving at customers. The real shortfall hits in weeks, not months — and the minimum recovery time is 2+ months even if [[Strait of Hormuz|Hormuz]] reopened today. Only two plants globally produce semiconductor-grade helium; one is in Qatar.

The most exposed nodes are [[TSMC]], [[SK Hynix]], [[Samsung Electronics|Samsung]], and other fabs in Japan, Singapore, South Korea, and Taiwan — all dependent on Qatar supply. Helium recycling is not implemented in chipmaking (historically deemed economically unnecessary). The crisis may force a structural shift toward recycling and supply diversification that should have happened after Helium Shortages 3.0 (2019) but never did.

Cross-link: this compounds the [[Iran conflict economic disruption]] story beyond oil, LNG, and fertilizer. The helium channel is the most direct transmission mechanism from the Gulf conflict to AI infrastructure.

---

## Why this crisis is different

Three prior [[Helium#Shortage history|helium shortages]] (2006, 2011, 2019) were maintenance hiccups — each resolved without structural reform. The 2026 crisis is wartime destruction of production and shipping infrastructure, with no strategic buffer anywhere (the US [[Helium#US National Helium Reserve — and its liquidation|sold off its reserve]] in 1996). The policy failure that started three decades ago has arrived at its logical conclusion.

For helium's physical properties, industrial uses, [[Helium#Global supply structure|supply structure]], and [[Helium#Pricing|pricing]], see [[Helium]].

---

## Crisis timeline

| Date | Event |
|------|-------|
| Feb 28 | US-Israeli strikes on [[Iran]]; [[IRGC]] declares [[Strait of Hormuz]] closed |
| Mar 2 | [[QatarEnergy]] halts all LNG and associated production at [[Ras Laffan]] |
| Mar 4 | [[QatarEnergy]] declares force majeure to affected buyers |
| Mar 6 | C&EN reports ~33% of global helium removed from market; spot prices already rising |
| Mar 16 | Spot prices up 70-100% from pre-war levels; [[SK Hynix]] begins emergency diversification |
| Mar 18 | Iranian missiles hit Ras Laffan (1 of 5 struck); [[Shell]] Pearl GTL and [[QatarEnergy]] condensate refinery "extensively damaged"; physical damage extends restart timeline to potentially 1+ year |
| Mar 19 | [[QatarEnergy]] CEO quantifies: helium output down 14%, two LNG trains (S4, S6) offline 3-5 years, North Field expansion halted. Force majeure extended to multi-year on Italy/Belgium/South Korea/China contracts |
| Mar 19 | CNBC deep-dive: spot prices +70-100% (Kornbluth); [[Barclays]] reports South Korea 55% / Taiwan 69% GCC helium dependency; [[JPMorgan]] upgrades [[Linde]], [[Wells Fargo]] upgrades [[Air Products]]; contract prices "have not really moved yet" but force majeure declarations imminent |
| Late Mar | Airgas ([[Air Liquide]] subsidiary) declares force majeure: allocation capped at 50% of normal monthly demand, $13.50/100cf surcharge (letter reviewed by WSJ, Mar 30) |
| Late Mar | [[South Korea]] KOTRA (Korea Trade-Investment Promotion Agency) approaches US helium suppliers for additional volumes (email reviewed by WSJ, Mar 30) |
| Late Mar | Helium buyers in [[India]] and [[Brazil]] receive force majeure notices from suppliers (Cliff Cain, Pulsar Helium, Mar 30) |
| Late Mar | German chemical industry group VCI flags raw material supply bottleneck concerns including helium (WSJ, Mar 30) |
| Late Mar | Spot prices more than doubled from pre-war levels; buyers scrambling for scarce spot market cargoes (WSJ, Mar 30) |
| Late Mar | [[Peng Shaozong]] (former [[NDRC]] official, vice-president [[China Society for Economic Reform]]) warns risk to high-end manufacturing from industrial gas shortages, naming semiconductors and medical technology ([[FT]], Apr 11) |
| Apr 11 | [[Trivium China]] reports domestic Chinese spot prices for high-grade helium +110% since Iran strikes; lower-grade liquid helium tracking +65% YTD ([[FT]]) |

Pre-crisis buffer: ~15% global supply surplus existed before the shutdown. With 30% capacity removed, the net shortage is ~15%.

Monthly shortfall: estimated 5.2M cubic meters/month offline.

South Korean chipmakers reportedly have around six months of helium supplies on hand (FT, Parikh, Mar 22) — a more comfortable buffer than Taiwan's 11-day LNG reserve, but finite. The asymmetry matters: helium buffers buy time for fab operations; LNG buffers buy time for everything else (power generation, industrial processes, heating).

---

## Supply chain mechanics

Three plants in [[Qatar]] produce helium:
- Two extract helium from waste gas during LNG liquefaction — when LNG stops, helium stops
- Third plant has independent feedstock but still ships through [[Strait of Hormuz]]

Transit: standard delivery from Qatar container stations to customers takes ~3 weeks. Helium shipped before March 2 is still arriving. The real shortage begins in late March/early April.

Container crisis: hundreds of specialized cryogenic containers (~$1M each, 11,000-gallon capacity) stuck in the Middle East (Phil Kornbluth, Mar 30). Hold time before excessive boil-off: 35-48 days (Kornbluth) — meaning containers filled at the shutdown (Mar 2) are now approaching or past their effective shelf life. Containers leak 0.1-1% per month (TECHCET CEO Lita Shon-Roy), but the binding constraint is maximum pressure buildup, not slow leakage.

Allocation hierarchy during shortage:
1. Medical applications (MRI magnet cooling) — highest priority
2. Semiconductor manufacturing — high allocation
3. Industrial (welding, fiber optics) — rationed
4. Party balloons — lowest priority, cut first

---

## Semiconductor exposure

| Company | Country | Exposure | Notes |
|---------|---------|----------|-------|
| [[TSMC]] | [[Taiwan]] | High | World's largest contract chipmaker; advanced node fabs use helium for etching |
| [[SK Hynix]] | [[South Korea]] | High | Already forced into emergency supply diversification (Mar 16) |
| [[Samsung Electronics]] | [[South Korea]] | High | Memory + foundry operations |
| [[GlobalFoundries]] | [[United States]]/[[Europe]]/[[Asia]] | Moderate | "Actively monitoring" but doesn't anticipate near-term impact; US/European footprint partially buffers (Mar 30) |
| [[Intel]] | [[United States]] | Moderate | US-sourced helium partially buffers |
| Japanese fabs | [[Japan]] | High | Dependent on Qatar supply chain |

GCC sourcing dependency:

| Country | GCC helium share | Source | Year |
|---------|-----------------|--------|------|
| [[South Korea]] | 55% | [[Barclays]] | 2025 |
| [[South Korea]] | ~67% (from Qatar alone) | [[Fitch Ratings]] | 2025 |
| [[Taiwan]] | 69% | [[Barclays]] | 2024 |
| [[Taiwan]] | "large chunk" from Qatar | [[Fitch Ratings]] | — |

South Korea and Taiwan account for 18% of global semiconductor production capacity each. Their combined GCC helium dependency makes them the most structurally exposed nodes.

Semiconductor industry recently became helium's largest consumer, surpassing MRI scanners (confirmed Oct 2025, Gasworld Helium Super Summit — [[TechCET]] CEO Lita Shon-Roy). Advanced AI chips (with tens of billions of transistors) require precise thermal control during etching — helium enables superior throughput that no cheaper substitute can match.

Recycling gap: helium recycling is technically feasible but not implemented in chipmaking. When helium was cheap and abundant, the economics never justified the capital investment. This crisis may force structural adoption of recycling systems — a multi-year retrofit cycle.

---

## Industrial gas distributor positioning

[[Helium#Industrial gas distributors|Major distributors]] ([[Linde]], [[Air Liquide]], [[Air Products]], Iwatani) benefit from pricing power during shortages but face physical allocation challenges. Surcharges already being assessed.

Wall Street positioning (Mar 2026):
- [[JPMorgan]] upgraded [[Linde]] (Jeffrey Zekauskas) — LIN +15% YTD through Mar 19, vs S&P -3%
- [[Wells Fargo]] upgraded [[Air Products]] to overweight (Michael Sison) — APD +14% YTD
- [[Deutsche Bank]], [[Wells Fargo]], [[JPMorgan]] all pointed to tightening helium as positive catalyst for industrial gas suppliers
- [[Bank of America]]: helium typically low-to-mid single digit % of gas company revenues; shortage is "neutral to modest net positive" for a few weeks, "more earnings upside" if longer
- [[UBS]] Global Wealth Management: "Any lengthy disruption will not only impact energy prices, but also food prices and industrial production"

*Source: CNBC, Mar 19 2026*

---

## Duration scenarios

| Duration | Outcome |
|----------|---------|
| <2 weeks | Market recovers easily; inventory buffers sufficient |
| 2-8 weeks | Industrial gas firms forced to rework logistics, contracts, relocate containers; fabs begin rationing |
| 2-6 months | Severe shortage; fab throughput reductions possible; recycling investment accelerates |
| 6+ months / physical damage | Equipment repair at Ras Laffan could take 1+ year; structural supply deficit; new non-Gulf capacity needed |
| 3-5 years (confirmed) | Al-Kaabi's Mar 19 damage assessment: two trains offline 3-5 years, helium output -14%. This is now the base case, not a tail scenario. |

The March 18 missile strike on Ras Laffan shifts the scenario distribution toward the longer end. Physical damage to liquefaction infrastructure is fundamentally different from a temporary production halt — equipment must be rebuilt, not just restarted.

---

## Historical context

This is Shortage 4.0 — the first driven by geopolitical destruction rather than maintenance. See [[Helium#Shortage history]] for the full 1.0-3.0 cycle.

---

## Key quotes

[[Kornbluth Helium Consulting]] president Phil Kornbluth (Mar 6): *"The world can't compensate for the loss of a third of its helium supply."*

Phil Kornbluth (Mar 18): *"Depending on how long this lasts, it could become a severe shortage, and prices could go up a lot."*

Phil Kornbluth (Mar 22, FT): Even if the conflict ended tomorrow, it would take "four to five weeks" for [[Qatar]] to resume gas and helium production from its plants, and "an additional two to three months after that to restore the helium supply chain to what it was pre-crisis." This sets the minimum recovery timeline at ~3.5-4 months from ceasefire — well into July/August 2026 even in the best case.

Phil Kornbluth (Mar 30, WSJ): Most cryogenic containers have a hold time of 35-48 days before too much gas is lost to boil-off. Hundreds of containers (~$1M each) now stuck in the Middle East.

Cliff Cain, manager of commercial and external affairs at Pulsar Helium (exploration projects in Minnesota and Greenland, Mar 30): *"This is the big one that we always feared would happen, it's the black swan event. It is just going to be a building crescendo of who's going to be able to get their molecules and who is not."* Also reported India and Brazil buyers receiving force majeure notices.

[[S&P Global]] Energy research director Ralf Gubler (Mar 30): *"The helium shock highlights a deeper vulnerability in the AI build-out: extreme dependence on a small number of geopolitically exposed nodes."*

Anish Kapadia, founder of UK-based AKAP Energy (Mar 30): Clients inundating with calls about impending impacts; gas suppliers likely to prioritize chipmakers and medical imaging. *"The first victims are party balloons: you can quite easily allocate less there and deal with a few angry parents. But clearly when you take a third of global supply off the market overnight, there's going to be a significant impact across the board."*

TECHCET CEO Lita Shon-Roy: *"Helium can leak out about 0.1 to 1 percent per month, depending on how good the gaskets are."*

[[Linx Consulting]]'s Mike Corbett on fab economics: *"So you're not going to shut down a fab because you have to double your helium price."*

---

## All-In E222 update (Apr 3)

*Data from All-In Podcast Episode 222, April 3, 2026*

**Qatar helium concentration:** 1/3 of world helium production from [[Qatar]], now disrupted — confirms the ~30% supply removal estimate from earlier analysis.

**Critical industry applications:**
- **MRI machines:** Magnetic resonance imaging requires liquid helium for superconducting magnets cooling
- **Semiconductor manufacturing:** Essential for advanced chip fabrication processes and etching
- **Mass spectrometry:** Laboratory analysis equipment requires helium as carrier gas

**No substitute availability:** "No quick substitute" for helium in these critical applications — unlike other industrial gases where alternatives exist, helium's unique properties (lowest boiling point, inert, small molecular size) make it irreplaceable in high-tech manufacturing and medical applications.

**Compounding effect:** Helium supply crisis compounds the broader energy crisis, creating multiple simultaneous supply chain pressures beyond oil and gas — affecting healthcare (MRI availability), technology manufacturing (chip production), and research capabilities (laboratory equipment).

---

## Related

- [[Helium]] — the commodity: properties, supply structure, shortage history, reserve liquidation
- [[Nitrogen Trap]] — parallel chokepoint analysis for fertilizer inputs through [[Strait of Hormuz]]
- [[Iran conflict economic disruption]] — parent disruption hub covering oil, LNG, fertilizer, shipping
- [[2026 Iran conflict market impact]] — market reaction hub
- [[Strait of Hormuz]] — transit chokepoint; ~86% traffic decline as of Mar 7
- [[QatarEnergy]] — operator of Ras Laffan; declared force majeure Mar 4
- [[SK Hynix]] — first chipmaker publicly forced into supply diversification
- [[TSMC]], [[Samsung Electronics]] — exposed advanced node fabs
- [[Linde]], [[Air Liquide]], [[Air Products]] — industrial gas distributors managing allocation
