---
aliases: [range-payload tradeoff, range vs payload, missile range-payload curve, rocket equation tradeoff]
tags: [concept, defense, physics, missiles]
---

**Range-payload tradeoff** -- the fundamental constraint in ballistic missile design: increasing range requires reducing warhead mass, and vice versa. Governed by the Tsiolkovsky rocket equation, the tradeoff is exponential rather than linear -- doubling range does not halve payload, it reduces it by far more. For nuclear proliferators, this creates a hard ceiling: a first-generation nuclear device is heavy (750-1,000+ kg), and the missiles available to most states were designed for conventional warheads at regional distances. Stretching to intercontinental range with a nuclear payload requires either miniaturizing the warhead (which took the [[United States|US]] and [[Soviet Union|USSR]] years of testing) or building fundamentally larger rockets -- both of which are observable, sanctionable, and targetable.

---

## The story

The tradeoff is rooted in rocket physics. A missile's range depends on its total impulse (how much energy its engines deliver) minus what's needed to lift its own structure and payload. The Tsiolkovsky equation -- delta-v = Isp x g0 x ln(m0/mf) -- dictates that velocity change (and thus range) scales with the logarithm of the mass ratio. This means small reductions in payload yield disproportionately large range gains at the margin, but the relationship flattens: you cannot keep shaving payload to reach any distance. At some point, the structural mass of the rocket itself becomes the limiting factor.

For a single-stage missile like the [[Khorramshahr]], the practical tradeoff looks like this: at 1,800 kg payload, range is ~2,000 km. Reduce to 750 kg and range extends to ~3,000 km -- a 58% reduction in payload yields a 50% increase in range. Reduce further to 300 kg and the missile might reach 4,000 km -- but now the payload is too light for a nuclear device, and the guidance accuracy at that extreme range degrades because the missile was never designed for that flight profile. The airframe, guidance system, and reentry vehicle were all optimized for a particular envelope; operating outside it produces both reduced payload and reduced reliability.

Multi-staging changes the math. Adding a second stage lets the missile shed dead weight (the empty first stage) during flight, dramatically improving the mass ratio for the remaining burn. This is why ICBMs are multi-stage -- the Minuteman III has three stages. For proliferators, the transition from single-stage to multi-stage missiles is the critical technological leap. [[Iran]]'s [[Sejjil]] (two-stage solid-fuel) and [[Qaem-100]] (three-stage SLV) represent this pathway. A three-stage solid-fuel rocket optimized as a weapon could theoretically deliver 1,000 kg to 4,000+ km -- but "theoretically" is doing heavy lifting. Flight-testing, guidance accuracy, reentry vehicle survivability, and production reliability all need to be demonstrated, not assumed.

The tradeoff is why nuclear miniaturization matters so much for proliferators. The [[United States]] spent from 1945 to the mid-1950s reducing warhead weight from the 4,400 kg Fat Man to weapons under 500 kg that could fit on tactical missiles. [[Pakistan]] received Chinese warhead designs in the 1980s that weighed ~500-1,000 kg and has since miniaturized further. [[North Korea]] is widely assessed to have warheads in the 500-1,000 kg range but may not have achieved reliable miniaturization below 500 kg. Each kilogram matters: for the [[Khorramshahr]], every 100 kg of warhead weight reduction adds roughly 150-200 km of range.

The tradeoff also explains why missile defense works better at extended range. A missile stretched to its maximum range flies a higher, slower trajectory (lofted less efficiently), carries a lighter warhead (easier to deflect), and has less fuel margin for evasive maneuvers. The [[Diego Garcia attack 2026|March 21 Diego Garcia attack]] illustrated this: one of the two [[Iran]]ian missiles broke up mid-flight (structural failure at extreme range), and the other was intercepted by an [[SM-3]] -- a system designed to catch missiles on predictable ballistic arcs. At shorter ranges against heavier warheads, the intercept problem is harder.

---

## Reference

### Khorramshahr range-payload curve

| Payload (kg) | Range (km) | Range gain per 100 kg reduction |
|-------------|-----------|-------------------------------|
| 1,800 | ~2,000 | -- |
| 1,500 | ~2,300 | ~100 km |
| 1,000 | ~2,700 | ~80 km |
| 750 | ~3,000 | ~120 km |
| 500 | ~3,500 | ~200 km |
| 300 | ~4,000 | ~250 km |

Note: analyst estimates, not Iranian official data. The accelerating range gain per kg at lower payloads reflects the logarithmic nature of the rocket equation.

### Historical miniaturization timelines

| Country | First device weight | Miniaturized weight | Time to miniaturize |
|---------|-------------------|--------------------|--------------------|
| [[United States]] | 4,400 kg (1945) | <500 kg (mid-1950s) | ~10 years |
| [[Soviet Union]] | ~5,000 kg (1949) | <1,000 kg (late 1950s) | ~10 years |
| [[China]] | ~1,500 kg (1964) | ~500 kg (1970s) | ~10 years |
| [[Pakistan]] | ~500-1,000 kg (1998) | ~400-600 kg (est.) | Chinese designs accelerated |
| [[North Korea]] | ~1,000 kg (est.) | Unknown | Ongoing |
| [[Iran]] | N/A | N/A | No confirmed warhead |

---

## Related

- [[Iranian missile arsenal]] -- primary application of this constraint to Iran's program
- [[Diego Garcia attack 2026]] -- operational test of extended-range capability at the tradeoff's limit
- [[Khorramshahr]] -- Iran's longest-range ballistic missile, range-payload curve above
- [[Qaem-100]] -- multi-stage pathway to overcome single-stage limits
- [[SM-3]] -- missile defense that benefits from extended-range trajectory predictability
- [[North Korea]] -- parallel proliferator facing the same constraint
