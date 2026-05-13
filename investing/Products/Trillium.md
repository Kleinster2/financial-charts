---
aliases: [TPU v6e, Cloud TPU v6e, Trillium TPU]
---
#product #ai #chip #tpu #google

**Trillium** — [[Google]]'s sixth-generation [[TPU]] (v6e), the Cloud TPU class powering [[Google Cloud]] AI training and inference workloads through 2025-2026 and the chip selected for [[Project Suncatcher]] orbital deployment. Marketed as Cloud TPU v6e; named "Trillium" for the public-product brand.

---

## Quick stats

| Detail | Value |
|---|---|
| Generation | TPU v6e |
| Operator | [[Google]] / [[Google Cloud]] |
| Foundry | [[TSMC]] |
| Primary terrestrial deployment | Google Cloud AI Hypercomputer |
| Orbital deployment | [[Project Suncatcher]] (radiation-tested Nov 2025) |
| Radiation profile (Suncatcher SSO) | 67 MeV proton beam tested; HBM first-irregularity at 2 krad(Si) vs 750 rad(Si) expected 5-year shielded mission dose |
| Maximum cumulative dose tested | 15 krad(Si) on a single chip |

---

## Why it matters

Trillium is the silicon substrate that anchors three of [[Alphabet]]'s most significant 2026 commitments simultaneously:

1. **[[Anthropic]] $200B / 5 GW capacity deal (Apr 2026).** The [[Google Cloud]] capacity that Anthropic is buying through 2030 is provisioned predominantly on Trillium and successor TPU generations. The economic flywheel runs Anthropic compute spend through TPU rentals, which is what makes the $40B equity commitment cash-flow-positive on a multi-year horizon for Alphabet.
2. **[[Project Suncatcher]] orbital deployment (announced Nov 2025).** The Suncatcher research paper specifically validated Trillium in the 67 MeV proton beam test that demonstrated "surprisingly radiation-hard" behavior — HBM irregularities only began at roughly 2.7x the expected 5-year mission dose, and single chips tolerated up to 20x mission dose before total failure. This is the technical claim that makes consumer/DC-grade silicon plausible for LEO without rad-hardening cost penalties.
3. **TPU competitive position vs [[NVIDIA]].** Trillium is the generation where Google began publicly claiming meaningful performance-per-dollar advantages on transformer workloads vs [[NVIDIA H100]] / [[NVIDIA Blackwell|Blackwell]] for specific Anthropic-class workloads. See [[Google TPU Competitive Position]] for the cross-generation comparison frame.

---

## Memory subsystem

The Suncatcher radiation testing flagged HBM (high-bandwidth memory) as the most radiation-sensitive component on the chip — consistent with the broader [[Memory|memory]] industry's view that stacked HBM is the weakest link in modern accelerator packaging. The 2 krad(Si) first-irregularity threshold against a 750 rad(Si) mission dose still leaves a ~2.7x margin without specialized shielding, which is the basis for Google's claim that production-grade silicon can survive multi-year LEO missions under standard aluminum enclosures.

This matters beyond Suncatcher: the same HBM-sensitivity result has implications for any operator (including [[SpaceX]] [[TERAFAB]] / [[xAI]], [[NVIDIA]] [[Vera Rubin Space 1]], [[Blue Origin]] [[Project Sunrise]]) attempting to deploy modern accelerator silicon in LEO.

---

## Related

- [[TPU]] — full TPU family lineage
- [[Google]] — operator
- [[Alphabet]] — parent
- [[Google Cloud]] — terrestrial deployment vehicle
- [[Project Suncatcher]] — orbital deployment program
- [[Anthropic]] — largest external compute customer (TPU monetization)
- [[TSMC]] — foundry
- [[Google TPU Competitive Position]] — vs NVIDIA framing
- [[NVIDIA H100]] — competitive baseline
- [[Memory]] — HBM sensitivity context

*Stub created 2026-05-13 to close [[Project Suncatcher]] / [[Alphabet]] dead-link from Suncatcher / SpaceX-talks ingestion*
