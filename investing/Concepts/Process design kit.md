#concept #technical #foundry

A **Process Design Kit (PDK)** is the interface between a chip designer and a foundry's manufacturing process.

## What it contains

- Transistor models (how devices behave electrically)
- Design rules (minimum spacing, widths, layer stackup)
- Standard cell libraries (pre-built logic gates)
- Timing models (signal propagation delays)
- SPICE parameters (simulation accuracy)

## Why it creates lock-in

Chip architects don't design for "2nm" generically — they design for **TSMC N2** or **Samsung SF2** specifically.

- Years of learning a PDK's quirks, corner cases, and workarounds
- Designs optimized for one PDK don't port cleanly to another
- Re-verification takes months and risks new bugs
- EDA tools ([[Synopsys]], [[Cadence]]) calibrate to each PDK separately

## Switching cost

Moving from [[TSMC]] to [[Samsung]] isn't just "send the files over." It requires:

1. Re-characterizing timing across all logic paths
2. Re-validating IP blocks (Arm cores, PHYs, memory interfaces)
3. Re-running physical design (place and route)
4. New test chips and silicon validation
5. Months of engineering time

This is why [[Customer lock-in via co-design]] is so sticky. The PDK is the technical root of the moat.

---

## Related

- [[TSMC]] — beneficiary (years of customer learning)
- [[Samsung]] — disadvantage (switching costs protect TSMC)
- [[Customer lock-in via co-design]] — mechanism (PDK is technical root)
- [[CUDA moat]] — analogy (same switching cost dynamic)
