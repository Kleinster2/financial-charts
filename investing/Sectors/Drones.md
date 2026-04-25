---
aliases: [UAV, UAVs, Unmanned aerial vehicles, Drone sector]
---
#sector #drones #aerospace #logistics #defense

# Drones

Unmanned aerial vehicles (UAVs) — military, commercial, and consumer applications.

---

## Market segments

| Segment | Key players | Use cases |
|---------|-------------|-----------|
| **Military** | [[Anduril]], [[Shield AI]], [[General Atomics]], [[Northrop Grumman]], [[AeroVironment]], [[Kratos]], [[Norinco]], [[Helsing]], Baykar, [[Swarmer]] | ISR, strike, logistics, CCA, swarm autonomy |
| **Cargo/logistics** | [[Zipline]], [[Wing]], Amazon, [[Norinco]] | Delivery, resupply |
| **Commercial/industrial** | [[DJI]], [[Skydio]], [[Quantum Systems]], Autel | Inspection, mapping, ISR (dual-use) |
| **Consumer** | [[DJI]], Autel, Parrot | Photography, hobby |
| **Air taxi/eVTOL** | [[Ehang]], [[Joby Aviation]], [[Archer Aviation]], Lilium | Urban air mobility |

---

## Cargo drones / aerial logistics

Autonomous aerial delivery — ranges from last-mile (small packages) to heavy cargo (1+ ton payloads).

| Company | Country | Payload | Focus |
|---------|---------|---------|-------|
| [[Wing]] (Alphabet) | US | Small | Last-mile delivery |
| [[Zipline]] | US | Medical | Blood, vaccines (Africa, US) |
| **Amazon Prime Air** | US | Small | E-commerce delivery |
| [[Norinco]] (Tianma-1000) | China | **1 ton** | Heavy cargo, military logistics |
| [[Ehang]] | China | Passengers | Air taxi |

### Tianma-1000 (天马-1000) — Jan 2026

First flight January 11, 2026. Heavy cargo drone from [[Norinco]] subsidiary Xi'an ASN.

| Spec | Value |
|------|-------|
| Payload | 1 ton |
| Range | 1,800 km |
| Ceiling | 8,000 m |
| Takeoff | <200 m |

**Dual-use:** Civilian framing (remote resupply, disaster relief) but military-grade specs. Short-field, high-altitude, modular airdrop = battlefield logistics.

**Strategic divergence:** China building heavy cargo drone capability while US focuses on last-mile. Different use cases — China optimizing for contested/remote terrain logistics.

---

## Military drones

| Type | Examples | Role |
|------|----------|------|
| MALE (Medium-altitude long-endurance) | MQ-9 Reaper, Wing Loong | ISR, strike |
| HALE (High-altitude long-endurance) | RQ-4 Global Hawk | Strategic ISR |
| Tactical | Bayraktar TB2, Switchblade | Battlefield ISR, loitering munitions |
| Loitering munition | [[Shahed-136]], [[LUCAS]], [[LoongUAV]] M9 | Expendable strike, one-way attack |
| Cargo | Tianma-1000 | Logistics, resupply |

**Ukraine lessons:** Cheap drones (FPV, Bayraktar) reshaping warfare. See [[Ukraine war]].

---

## Software-first / autonomy stack

The defensible moat in modern drones is the autonomy software, not the airframe. Three platforms dominate:

| Platform | Owner | Function |
|----------|-------|----------|
| Lattice OS | [[Anduril]] | Sensor fusion, command & control across all Anduril products (Ghost, Altius, Roadrunner, Fury) |
| Hivemind | [[Shield AI]] | AI pilot for V-BAT and other airframes; GPS-denied autonomous flight, multi-aircraft coordination |
| Skydio Autonomy | [[Skydio]] | On-device flight autonomy for X10, X10D (commercial/military) |

European counterpart: [[Helsing]] (Munich) bundles AI battlefield analytics with own manufacturing (HX-2 drones, CA-1 Europa UGV). Quantum Systems / [[Stark]] split the ISR vs. strike sides of the same Munich founder ([[Florian Seibel]]).

---

## Collaborative Combat Aircraft (CCA)

Largest US drone procurement program in history — ~$1.39B FY2025, ~$996.5M requested FY2027. Three Increment 1 contractors: [[General Atomics]] (YFQ-42A), [[Anduril]] (YFQ-44A Fury, production at Arsenal-1), [[Northrop Grumman]] (YFQ-48A Talon Blue). USMC parallel program uses [[Kratos]] XQ-58 Valkyrie. See [[Collaborative Combat Aircraft]] for full program structure.

---

## Replicator Initiative

DoD's parallel attritable-autonomous program. Replicator 1 (Aug 2023 → Aug 2025) targeted "thousands" of all-domain attritable autonomous (ADA2) systems and missed by an order of magnitude (only hundreds delivered) — but the procurement model survived and reorganized. Replicator 2 (Sept 2024 → present) consolidated under Joint Interagency Task Force 401 (Aug 2025); first contract Jan 2026 for Fortem DroneHunter F700; counter-drone marketplace IOC Feb 2026. Successor [[Defense Autonomous Warfare Group]] received $225.9M in FY2026; FY2027 autonomous-warfare request runs up to $54.6B — the budget signal that the experiment is being industrialized. Direct sector beneficiaries: [[AeroVironment]] (Switchblade 600 / LASSO), [[Anduril]] (Lattice OS + multiple platforms), [[Shield AI]] (Hivemind), [[Kratos]] (XQ-58 + tactical), [[Skydio]] (autonomy stack + sUAS), private autonomy peers. See [[Replicator Initiative]] for program structure and the cultural-vs-technical framing.

---

## Commercial/industrial

| Company | HQ | Specialty | Notes |
|---------|-----|-----------|-------|
| [[DJI]] | China | Consumer, commercial | ~70% global market share |
| [[Skydio]] | US | Autonomous flight | US government preferred |
| **Autel** | China | Consumer, enterprise | DJI competitor |
| **Parrot** | France | Defense pivot | Exiting consumer |

**DJI dominance:** Chinese company controls most of global drone market. US government agencies increasingly restricted from using DJI (security concerns).

**The American drone birthright (lost):** The drone is an American invention — Abe Karem designed the Predator at [[General Atomics]]. But ITAR export controls classified drones as flying missiles, and the FAA banned beyond-line-of-sight operations. This killed the domestic commercial drone market. [[Shyam Sankar]] ([[Palantir]], Apr 6, 2026): "There was a counterfactual world where General Atomics had a consumer subsidiary called DJI and the consumer drone market was entirely owned by the US." The consumer market would have written the US down the price-production curve for defense applications — instead China captured that volume and that learning curve.

---

## Regulatory landscape

| Region | Framework | Status |
|--------|-----------|--------|
| US | FAA Part 107, BVLOS waivers | Expanding commercial ops |
| EU | EASA drone regulations | Harmonized 2024 |
| China | CAAC | Permissive for domestic |

**Key barrier:** Beyond visual line of sight (BVLOS) approval still difficult in US/EU. Limits cargo drone scale.

---

## Sector benchmark: DRNZ

**[[REX Financial|REX]] Drone ETF (DRNZ)** — first pure-play drone ETF. Launched Oct 29, 2025 on NASDAQ.

| Metric | Value |
|--------|-------|
| **AUM** | ~$78M (Apr 2026) |
| **Holdings** | 51 |
| **Expense ratio** | 0.65% |
| **NAV** | $24.30 (Apr 1, 2026) |
| **Since inception** | –11.7% |

**Top 10 holdings (Apr 1, 2026):**

| Ticker | Name | Weight |
|--------|------|--------|
| AVAV | [[AeroVironment]] | 11.4% |
| NXSN | Next Vision Stabilized Systems | 10.8% |
| ONDS | Ondas Holdings | 10.0% |
| DRO | DroneShield (ASX) | 7.5% |
| ELS | Elsight (ASX) | 4.7% |
| FLT | Volatus Aerospace (TSX) | 4.5% |
| EH | [[Ehang]] | 4.5% |
| RCAT | Red Cat Holdings | 4.0% |
| UMAC | [[Unusual Machines]] | 3.6% |
| 278A | Terra Drone (JPX) | 3.0% |

Modified free-float market cap weighting. "Pureplay" companies (≥50% revenue from drones) capped at 15% each; "Diversified" companies capped at 5%. Global coverage — US, Australia, Canada, Japan, Israel.

**Competitor:** UAV (AdvisorShares Drone Technology ETF) — functionally dead at ~$685K AUM.

---

## Investment vehicles

| Company | Ticker | Angle |
|---------|--------|-------|
| [[Joby Aviation]] | JOBY | Air taxi |
| [[Archer Aviation]] | ACHR | Air taxi |
| [[AeroVironment]] | AVAV | Military small UAVs, Switchblade |
| [[Ehang]] | EH | Air taxi (China) |
| [[Kratos]] | KTOS | XQ-58 Valkyrie, attritable drones |
| Red Cat Holdings | RCAT | Black Widow (US Army SRR winner); 4.0% of DRNZ — stub candidate |
| Ondas Holdings | ONDS | Military/industrial drones; 10.0% of DRNZ — stub candidate |
| DroneShield | DRO (ASX) | Counter-UAS detect/defeat; 7.5% of DRNZ — stub candidate |
| [[Powerus]] | PUSA (expected) | Heavy-lift UAS, defense roll-up; Trump family-backed |
| [[Unusual Machines]] | UMAC | Drone components; Trump Jr. adviser |
| [[XTEND]] | — (via JFB.O) | Israeli AI drones; Eric Trump-backed |

**ETF:** DRNZ (REX Drone ETF) — pure-play sector benchmark

**Private:** [[Anduril]] (~$31B, IPO discussed), [[Shield AI]] ($5.3B), [[Helsing]] (€12B), [[Quantum Systems]], [[Stark]], [[Zipline]], [[Wing]] (Alphabet), [[Skydio]], [[DJI]]

---

## Iran conflict — drone stocks lead defense rally (Mar 2, 2026)

Drone pure-plays were the biggest movers in the defense sector following Operation Epic Fury, outperforming even primes. The market is pricing munitions burn and the Ukraine-validated cost asymmetry thesis.

| Company | Mar 2 premarket | Notes |
|---------|-----------------|-------|
| [[AeroVironment]] | +10% | Switchblade loitering munitions, small UAS |
| [[Kratos Defense]] | +10% | Attritable drones, hypersonic targets |

vs primes at +5-7% and Defense IT flat. Drones led both the Feb 18 threat phase (+5-9%) and the Mar 2 kinetic phase (+10%), confirming the market thesis that drone/attritable munitions are the primary beneficiaries of active conflict.

See [[2026 Iran conflict market impact]] for full cross-sector reaction.

---

## LUCAS — first US long-range loitering munition combat use (Feb 28, 2026)

[[SpektreWorks]] (Phoenix, AZ) reverse-engineered [[Iran]]'s [[Shahed-136]] into [[LUCAS]] (Low-cost Uncrewed Combat Attack System) — a $35,000 one-way attack drone. First combat use confirmed by CENTCOM on February 28, 2026 during [[Operation Epic Fury]], fired by Task Force Scorpion Strike against IRGC targets.

| Spec | LUCAS | Shahed-136 | Tomahawk |
|------|-------|------------|----------|
| Unit cost | $35K | $20-50K est. | $2.5M |
| Range | 500 mi | 1,500+ km | 1,000+ mi |
| Weight | 81.5 kg | 200 kg | 1,440 kg |

18 months from concept to deployment. Government owns the IP — designed for multi-vendor production (up to 20 manufacturers). Part of the $1.1B Drone Dominance Program targeting 200,000+ drones by 2028.

SpektreWorks is private, ~5-15 employees, ~$2M pre-LUCAS revenue. Not investable directly, but validates the cheap-drone thesis that benefits [[AeroVironment]], [[Kratos]], and the broader attritable munitions supply chain.

---

## Related

### Military
- [[Anduril]] — Lattice OS, Ghost, Altius, Fury, Roadrunner; $20B Army contract; Arsenal-1 factory
- [[Shield AI]] — V-BAT, Hivemind autonomy ($5.3B valuation)
- [[General Atomics]] — MQ-9 Reaper, dominant US military drones; YFQ-42A CCA contender
- [[AeroVironment]] — Switchblade, small UAS (AVAV)
- [[Kratos]] — XQ-58 Valkyrie, attritable drones (KTOS)
- [[Helsing]] — Europe's defense AI leader, HX-2 drones (€12B, Munich)
- [[Quantum Systems]] / [[Stark]] — German ISR (Quantum) and strike (Stark) sister companies
- [[Norinco]] — Tianma-1000 heavy cargo drone
- [[Northrop Grumman]] — Global Hawk; YFQ-48A Talon Blue CCA entrant

### Commercial/Consumer
- [[DJI]] — ~70% global market share
- [[Skydio]] — US alternative to DJI

### Cargo/Logistics
- [[Zipline]] — medical delivery pioneer
- [[Wing]] — Alphabet last-mile delivery

### Air Taxi/eVTOL
- [[Joby Aviation]] — US leader (JOBY)
- [[Archer Aviation]] — US competitor (ACHR)
- [[Ehang]] — Chinese, first certified (EH)

### Trump family drone investments
- [[Powerus]] — roll-up targeting Pentagon contracts (PUSA, expected summer 2026)
- [[XTEND]] — Israeli AI drone maker, $1.5B reverse merger (Feb 2026)
- [[Unusual Machines]] — drone components, Trump Jr. adviser (UMAC)
- **Aureus Greenway Holdings** (AGH) — golf club operator announced merger with unnamed Pentagon drone company (Mar 10, 2026). Trump Jr. and Eric Trump described as "notable investors." Dominari Securities and Revere Securities advising — both firms simultaneously under [[House China Committee]] probe for underwriting Chinese pump-and-dump IPOs

### US low-cost / one-way attack
- [[SpektreWorks]] — LUCAS manufacturer (private, Phoenix AZ)
- [[LUCAS]] — $35K one-way attack drone, reverse-engineered Shahed-136
- [[Griffon Aerospace]] — MQM-172 Arrowhead (competing Shahed derivative)

### Chinese drone proliferation
- [[LoongUAV]] — private tactical drone/loitering munition maker (LOONG M9)
- [[AVIC]] — state-owned, Wing Loong MALE/HALE family (688297.SS)
- [[Shahed-136]] — Iranian loitering munition (comparator class)

### Maritime/Surface
- [[Saronic]] — autonomous surface vessels for US Navy ($9.25B, 7 hull classes)
- [[Exail Technologies]] — European MCM drones (K-STER C, Inspector USV, DriX)

### Counter-drone
- [[Counter-UAS]] — detection, defeat, directed energy market
- [[Anduril]] Roadrunner — jet-powered reusable interceptor; $642M Marine Corps contract (Mar 2025)
- [[Dedrone]] — airspace security (now [[Axon]])
- [[Epirus]] — Leonidas high-power microwave
- DroneShield (DRO, ASX) — RF detection / defeat (7.5% of DRNZ)

### Ground
- [[Unmanned ground vehicles]] — military UGVs, autonomy software

### Context
- [[Aerospace]] — parent sector
- [[Defense]] — military drone applications
- [[Logistics]] — cargo drone use case
- [[Collaborative Combat Aircraft]] — CCA/loyal wingman programs
- [[Ukraine war]] — drone warfare lessons
- [[China defense]] — Chinese military UAV development
