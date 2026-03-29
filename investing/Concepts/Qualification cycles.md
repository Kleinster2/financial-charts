---
aliases: [qualification cycle, supplier qualification, customer qualification, requalification, certification cycle]
tags: [concept, semiconductors, defense, pharma, moat]
---
#concept #semiconductors #defense #pharma #moat

**Qualification cycles** — the months-to-years process of testing and validating a component, material, or supplier before it can enter production. The timelines range from 6 months ([[HBM]] supplier qualification) to 10+ years (FDA drug approval), and they are largely irreducible because they depend on accumulated tacit knowledge and physical testing that cannot be compressed by capital alone. The economic consequence is the same across every domain: lock-in, pricing power, and concentration.

---

## The story

Every industry with long qualification cycles shares a structural pattern. A customer needs a component. Testing it takes months or years — not because anyone is slow, but because the validation process is physical and sequential. You cannot run a 12-month contamination test in 3 months by spending 4x as much. The testing itself is the irreducible constraint. Once a supplier passes, the customer will not switch unless forced, because switching means re-running the entire qualification from scratch. The supplier earns pricing power not from what it makes but from what it would cost the customer to replace it.

The mechanism is most visible in semiconductors. [[Photoresists]] — the light-sensitive chemicals used in chip lithography — require 12-24 months of customer qualification. The process involves contamination validation at sub-parts-per-billion levels, process recipe testing across 50-100+ lithography steps per chip, and equipment-specific tuning for each customer's fab. [[TSMC]], [[Samsung]], and [[Intel]] each have different process flows; a photoresist qualified for one may not work for another. This is why three Japanese companies ([[JSR]], [[Tokyo Ohka Kogyo]], [[Shin-Etsu Chemical]]) hold ~90% of the EUV photoresist market despite decades of attempted entry by others. When [[Japan]] briefly restricted photoresist exports to [[South Korea]] in 2019 over wartime labor disputes, [[Samsung]] and [[SK Hynix]] had no short-term alternative — the 12-24 month qualification wall made switching impossible on any timeline shorter than the diplomatic resolution itself.

The same dynamic operates in [[HBM]]. Qualification for a new HBM generation takes 6-9 months minimum, sometimes 18-42 months for custom configurations. [[NVIDIA]]'s Blackwell GPU uses HBM that was qualified in 2023; the Vera Rubin platform uses HBM being qualified now. Revenue that shows up in 2027 is being locked in during 2025's qualification cycles. When [[SK Hynix]] was the sole qualified HBM3E supplier for NVIDIA in 2024, it captured 62% market share and the pricing power that came with it. When [[Micron]] qualified HBM4 ahead of schedule in February 2026, it reshuffled the competitive landscape — but only for the next generation. The previous generation's lock-in was already set.

Semiconductor yield creates a related but distinct qualification dynamic. The gap between a 70% yield and a 50% yield translates to a 40% cost difference per chip ($143 vs $200 on a $10K wafer). But yield is accumulated, not purchased — it requires thousands of micro-optimizations in defect learning, operator expertise, and equipment tuning over 18-24 months minimum. TSMC's 2-year head start on 3nm gate-all-around means accumulated yield learning that [[Samsung]] cannot shortcut regardless of investment. Customers commit chip designs 18-24 months ahead and will not bet on a foundry with yield uncertainty. The qualification here is implicit: you earn customers by having already qualified yourself through years of accumulated learning.

Advanced packaging adds a physical infrastructure layer. Building a greenfield cleanroom takes 3-5 years (environmental assessments, power and water infrastructure, contamination validation). Converting an existing panel display fab saves months to years because the cleanroom shell already meets semiconductor cleanliness standards. This is why TSMC paid NT$17.14B ($538M) for [[Innolux]] Fab 4 and [[ChipMOS]] paid NT$880M ($28M) for Innolux Fab 2 — they were buying pre-qualified cleanroom space in a market with a 15-20% advanced packaging supply-demand gap (JPMorgan estimate). The display fabs are worth more dead (as cleanroom shells for [[CoWoS]] packaging) than alive (competing with [[China]] on LCD margins).

Defense supply chains face the same structure at different timescales. Testing and certification for munitions, explosives, and propellants takes 12-18 months per qualification cycle. The tolerance for defects is zero — these are life-critical applications. [[BAE Systems]]'s Radford propellant plant is effectively the sole source for U.S. propellant production, a single point of failure for the entire munitions industrial base. When the U.S. needed to scale from 93K to 1.2M 155mm shells per year, the qualification timeline for new suppliers was the binding constraint, not the capital. Upstream, critical raw materials like copper require 17-year mine-to-production timelines. The entire defense supply chain is a series of nested qualification bottlenecks.

Pharmaceutical qualification operates on the longest timescales. Traditional drug development costs $2.6B and takes 10-15 years from discovery to approval. AI is compressing the early stages — Phase 1 success rates have improved from ~40% to 80-90% for AI-designed molecules, and the timeline may shorten by 25-50% — but it cannot eliminate the clinical trial sequence. Phase 1, Phase 2, and Phase 3 must run in order, each requiring years of patient data. The first AI drug development tool ([[PathAI]]'s AIM-NASH) was only FDA-qualified in December 2025. As of March 2026, zero AI-discovered drugs have received full FDA approval. [[Insilico Medicine]]'s Rentosertib, the furthest along, completed Phase 2a in May 2025 — earliest approval likely 2027-2029. The qualification cycle is the floor, and no amount of computational power raises it.

The investment pattern across all these domains is consistent. Long qualification cycles create concentration — Japan's 90% share in EUV photoresists, SK Hynix's 62% in HBM, TSMC's 50%+ in advanced foundry, BAE's near-monopoly in U.S. propellant. New entrants need both capital and time, and time cannot be bought. [[China]]'s semiconductor localization effort illustrates this: despite billions in investment and government priority, EUV photoresist localization remains ~0%, HBM qualification is years behind, and advanced foundry yield lags by at least two process generations. The qualification wall is the binding constraint on catching up, not the capital.

When qualification cycles are disrupted — a power outage destroys wafers in process ($50-150M per fab event), a conflict closes the [[Strait of Hormuz]] and cuts chemical supply chains, or a geopolitical dispute restricts material exports — the requalification timeline creates an amplified economic impact. Cleanrooms must be requalified after extended downtime. Chemical supply chains through Hormuz (half of global seaborne sulphur, key bromine sources) take 4-5 weeks to restore plus 2-3 months to normalize production. The disruption duration is not the crisis duration — it is the crisis duration plus the requalification timeline.

---

## Reference

### Qualification timelines by domain

| Domain | Timeline | Process | Lock-in effect |
|--------|----------|---------|----------------|
| [[HBM]] supplier | 6-42 months | Customer-specific validation, interposer testing, thermal/electrical qualification | Generation-locked; reshuffles only at new HBM generation |
| [[Photoresists]] / semiconductor materials | 12-24 months | Sub-ppb contamination validation, process recipe testing, equipment-specific tuning | Japan 90% EUV share; 5-10+ year localization lag for entrants |
| Semiconductor [[Yield as competitive moat|yield]] | 18-24 months (implicit) | Defect learning, operator expertise, thousands of micro-optimizations | 20pp yield gap = 40% cost difference; customers commit designs 18-24 months ahead |
| Defense certification | 12-18 months | Testing, facility validation, sole-source approval | Single points of failure (BAE Radford); 17-year mine-to-production upstream |
| Advanced packaging (greenfield) | 3-5 years | Environmental permitting, infrastructure build, cleanroom validation | Pre-qualified cleanroom shells command acquisition premiums |
| Cleanroom restart (post-disruption) | Days to weeks | Re-qualification after power outage or extended downtime | $50-150M per fab event; extends lead times 3-6 months |
| Chemical supply restoration | 4-5 weeks + 2-3 months | Supply chain re-validation after Hormuz/logistics disruption | Cascades through entire semiconductor supply chain |
| FDA drug approval | 5-15 years | Phase 1/2/3 clinical trials, manufacturing process validation | AI shortens 25-50% but cannot eliminate sequential trial requirement |

### Concentration created by qualification barriers

| Domain | Concentration | Dominant players |
|--------|--------------|-----------------|
| EUV photoresists | Top 3 = ~90% | [[JSR]], [[Tokyo Ohka Kogyo]], [[Shin-Etsu Chemical]] |
| HBM | Top 1 = 62% | [[SK Hynix]] (then [[Micron]] 21%, [[Samsung]] 17%) |
| Advanced foundry (<7nm) | Top 1 = ~50%+ | [[TSMC]] |
| U.S. propellant | Sole source | [[BAE Systems]] (Radford) |
| Global wafer transport | Top 1 = ~30% | [[Cathay Pacific]] |

### Key episodes

| Event | Year | What happened |
|-------|------|---------------|
| [[Japan]]-[[South Korea]] photoresist restriction | 2019 | Brief export controls disrupted Samsung/SK Hynix; no short-term alternative existed |
| [[SK Hynix]] sole HBM3E qualification | 2024 | Captured 62% share and pricing power; competitors locked out for that generation |
| [[Micron]] HBM4 ahead of schedule | Feb 2026 | Reshuffled next-generation competitive position; previous generation lock-in unchanged |
| [[China Micron ban June 2023]] | 2023 | China banned Micron from critical infrastructure; requalifying domestic alternatives still in progress |
| [[Taiwan]] panel fab conversions | 2025-2026 | TSMC, ChipMOS acquiring display fabs for pre-qualified cleanroom space; 3-5 year greenfield alternative |

---

## Related

- [[Photoresists]] — 12-24 month qualification; Japan concentration
- [[HBM]] — 6-42 month qualification; generation-locked competition
- [[Micron]] — HBM4 qualification ahead of schedule (Feb 2026)
- [[SK Hynix]] — sole HBM3E qualified supplier for [[NVIDIA]] (2024)
- [[Yield as competitive moat]] — implicit qualification through accumulated learning
- [[Defense supply chain]] — 12-18 month certification; sole-source bottlenecks
- [[Taiwan panel-to-packaging conversion]] — pre-qualified cleanroom economics
- [[Iran conflict semiconductor energy risk]] — requalification after disruption
- [[AI drug discovery]] — FDA qualification timelines
- [[Semiconductor Materials]] — customer qualification across materials categories
- [[Long Japan photoresists]] — thesis built on qualification barriers

*Created 2026-03-28*
