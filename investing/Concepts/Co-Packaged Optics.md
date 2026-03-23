---
aliases: [CPO, co-packaged optics]
tags: [concept, networking, infrastructure, semiconductors, ai-infrastructure]
---

**Co-Packaged Optics** — integrating optical engines directly inside semiconductor packages alongside switch chips or GPUs, rather than using external pluggable transceivers. CPO promises 3x power reduction and dramatically lower latency, but faces brutal manufacturing, thermal, and yield challenges. The transition is real but contested: pluggable optics keep fighting back with LPO and XPO innovations, and the consensus inflection point sits at 3.2T+ speeds — somewhere between 2028 and 2030.

---

## The story

Everyone says CPO will replace copper and pluggable optics inside data centers. The direction is right. The timeline is what separates good investments from traps.

Start with the physics. Electrons are fermions — they repel each other, which makes them useful for computation (switching transistors on and off) but terrible for transmission. Pushing data through copper wires at high speeds requires enormous power, generates heat, and degrades the signal over distance. Photons are bosons — they don't interfere with each other, which means you can stack multiple wavelengths on a single channel (wavelength division multiplexing), send signals farther, and burn less energy doing it. The semiconductor industry's conclusion: electrons compute, photons transmit. This isn't a preference — it's a survival requirement as AI clusters scale to hundreds of thousands of GPUs.

CPO is the logical endpoint of that insight. Instead of converting electrical signals to light in a pluggable transceiver bolted onto the switch front panel — separated from the ASIC by tens of centimeters of lossy copper PCB trace — you put the optical engine inside the chip package itself. Signal travels millimeters, not centimeters. The DSP that conditions signals for long copper traces? Eliminated entirely. [[Broadcom]]'s numbers: 800Gbps port, pluggable at 15W versus CPO at 5.5W. That 3x power gap, multiplied across hundreds of thousands of connections in a hyperscale data center, translates to megawatts saved.

But knowing the destination doesn't tell you when you arrive. The story splits into two domains with different physics, different economics, and different timelines.

In scale-up — GPU-to-GPU communication within training clusters — copper isn't just surviving, it's dominating through 2027. [[NVIDIA]]'s roadmap tells the story precisely: Blackwell (2024-25) runs NVLink 5.0 at 1.8TB/s per GPU on copper. Vera Rubin (2026) doubles to 3.6TB/s by doubling lanes, not speed — the Oberon rack carries 5,000+ cables totaling 2 miles of copper. Rubin Ultra (2027) replaces cables with a PCB midplane but it's still copper electrical signaling. CPO enters scale-up only with Feynman in 2028. Jensen at GTC 2026: "Feynman has Kyber with copper and CPO scale-up." Not either/or — coexistence. Why copper hangs on this long: DAC cables cost 10x less, deliver sub-nanosecond latency, and have 20 years of proven field reliability. That's hard to displace with a technology that still struggles with 85% packaging yields on $10,000+ GPU packages.

The copper wall is approaching, though, and the physics of why is specific. SerDes (serializer/deserializer) speeds have carried the industry through five [[NVLink]] generations, but lane speed gains are exhausting. NVLink lane count barely moved from v1.0 to v5.0 — 32 to 36 lanes — so almost all bandwidth improvement came from faster signaling. The current 224G SerDes generation already uses bi-directional transmission (data flowing both ways on the same trace simultaneously). Scaling to 448G SerDes would require ~244 GBaud in PAM4 modulation, at which point power consumption and insertion loss become overwhelming. You can't just make lanes faster, and you can't easily add more lanes (routing complexity, power, package area). Copper is running out of tricks.

In scale-out — network switches connecting GPU clusters via Ethernet or InfiniBand — the problem is different. Here pluggable optical transceivers already dominate, but each one carries a DSP that consumes roughly half its total power. At 400G, that's ~4W per transceiver just for signal conditioning. A 128,000-GPU cluster needs hundreds of thousands of pluggables pulling 10-15W each — aggregate power hits megawatts. CPO eliminates the DSP entirely by shortening the electrical path to millimeters, making signal conditioning unnecessary. At 800G, pluggables work fine. At 3.2T and beyond, DSP power becomes physically unmanageable.

But here's where the simple narrative breaks: the CPO transition faces brutal engineering challenges that the hype glosses over.

Thermal management is the first wall. Silicon photonic modulators use micro-ring resonators (MRRs) — tiny ring-shaped waveguides that resonate at specific wavelengths. They're exquisitely temperature-sensitive: a 1°C shift moves the resonant wavelength ~0.1nm. In CWDM4 systems with 0.8nm channel spacing, just 8°C of thermal drift causes adjacent channels to overlap into crosstalk. GPU ASICs run at 90°C+. Putting MRRs in the same package means operating next to a furnace. The fix — individual micro-heaters on each ring for thermal control — burns back the power savings CPO was supposed to deliver. Liquid cooling isn't optional; it's a prerequisite.

Lasers compound the thermal problem. Semiconductor lasers (III-V compounds like InP and GaAs) degrade rapidly above 70°C. The industry workaround is External Laser Sources (ELS) — placing the laser outside the package and piping continuous-wave light in through polarization-maintaining fiber. It works, but adds routing complexity and insertion loss. And there's a power gap: current commercial O-band lasers at 50°C deliver ~80mW, while CPO applications need 286mW for WDM or 100mW+ for direct-detect.

Then there's yield. A scale-up CPO package bundles GPU or NVSwitch ASIC, HBM stacks, and multiple optical engines on one substrate — worth $10,000+. One bad optical engine post-assembly means scrapping the entire package. No rework possible; debonding optical components destroys the chip. Every optical die must be verified good before assembly (Known Good Die), but wafer-level optical testing — which requires fiber coupling to measure light in and light out, unlike electronic circuits you can probe with needles — remains immature. Packaging yields struggle past 85%. A 15% scrap rate on packages that expensive destroys the economics. This is where [[FormFactor]]'s acquisition of Keystone Photonics becomes significant: whoever solves wafer-level optical testing controls CPO's path to mass production.

And the pluggable camp isn't standing still. This is the part the CPO bulls consistently underestimate.

Linear Pluggable Optics (LPO) removes the DSP from inside the transceiver — the component that consumes half the power — and shifts signal conditioning to the switch chip, which already has powerful processing capability. Same pluggable form factor, 30-50% power reduction, already in production at [[NVIDIA]] Spectrum-X and [[Meta]]. The data point that matters: [[Arista Networks]]'s Andy Bechtolsheim showed at OFC 2025 that at 1.6Tbps, DSP pluggables consume 25W, CPO ~10W — but LPO also reaches ~10W. At the current transition generation, LPO matches CPO on power while keeping every structural advantage pluggables have.

Then Arista unveiled XPO (eXtra-dense Pluggable Optics) at OFC 2026: 12.8Tbps per module, 64 lanes at 200Gbps, 204.8Tbps per rack unit, integrated liquid cooling. 45 founding members in the MSA, [[Microsoft]] backing, volume production targeted 2027. In a 400MW data center with 128K GPUs, the 1,400+ OSFP switch racks would shrink by 75%. The "pluggable has a density ceiling" argument — one of CPO's strongest selling points — crumbles.

Beyond technology, pluggables have structural advantages hyperscalers viscerally prefer: pull a failed module and replace it in minutes (CPO means swapping the entire board); buy from dozens of MSA member vendors and play them against each other on price (CPO means vendor lock-in to specific ASIC/optical engine combinations); rely on 20 years of field data and a 50-million-unit annual supply chain (CPO shipment volume today is approximately zero).

The consensus timeline: 800G, pluggables handle it. 1.6T, LPO and XPO extend pluggable's life. 3.2T+ (the 400G-per-lane generation), DSP power and insertion loss push past what any pluggable variant can handle. That inflection sits at 2028-2030.

For investors, the timing question is everything. If CPO adoption accelerates, integrated semiconductor companies ([[Broadcom]], [[Marvell]]) benefit while traditional transceiver vendors ([[Coherent Corp]], [[Lumentum]]) face disruption risk. If pluggables successfully defend with LPO/XPO, the reverse occurs. Either way, the picks-and-shovels layer — test equipment ([[FormFactor]]), foundries ([[Tower Semiconductor]] on depreciated 65nm nodes), EDA tools ([[Synopsys]], [[Cadence]]), and laser suppliers ([[Coherent Corp]], [[Lumentum]]) — earns revenue regardless of which architecture prevails. The difference between a 2028 and a 2032 inflection point is the difference between a trade and a trap.

---

## Reference

### Architecture comparison

| Architecture | Signal path | Power | Latency | Serviceability |
|--------------|-------------|-------|---------|----------------|
| Pluggable | ASIC → PCB traces (cm) → module | Higher | Higher | Easy swap |
| CPO | ASIC → optical engine (mm) | 30-50% lower | Lower | Board-level |

### Scale-up domain

### [[NVIDIA]] roadmap

| Generation | Year | NVLink version | Bandwidth per GPU | Technology | Notes |
|------------|------|----------------|-------------------|------------|-------|
| **Blackwell** | 2024-25 | NVLink 5.0 | 1.8TB/s | Copper DAC | NVL72 rack |
| **Vera Rubin** | 2026 | NVLink 6.0 | 3.6TB/s | Copper | Doubled lanes, not speed. Oberon rack, 5,000+ cables (2 miles total) |
| **Rubin Ultra** | 2027 | NVLink 6.0+ | TBD | Copper | Kyber rack, 144 GPU packages (576 dies), PCB midplane |
| **Feynman** | 2028 | NVLink 8 | TBD | Copper + CPO | Jensen at GTC 2026: "Feynman has Kyber with copper and CPO scale-up" |

### Scale-out power comparison

| Speed | DSP pluggable | LPO | CPO |
|-------|--------------|-----|-----|
| 800Gbps | 15W | — | 5.5W |
| 1.6Tbps | 25W | ~10W | ~10W |
| 3.2T+ | Unmanageable | TBD | Required |

Source: [[Broadcom]] (800G), Andy Bechtolsheim/[[Arista Networks]] OFC 2025 (1.6T).

### XPO specifications ([[Arista Networks]], OFC 2026)

| Spec | Value |
|------|-------|
| Bandwidth per module | 12.8Tbps (8× OSFP) |
| Lanes | 64 at 200Gbps |
| Bandwidth per RU | 204.8Tbps |
| Cooling | Integrated liquid cold plate (400W/module) |
| MSA members | 45 founding members |
| Key backer | [[Microsoft]] |
| Volume production | 2027 target |
| System impact | 75% reduction in OSFP switch racks (128K GPU / 400MW DC) |

### Key quotes

- [[Broadcom]] CEO Hock Tan, March 2026 earnings: "We're not quite there yet."
- Jensen Huang, GTC 2026: "Is copper still important? Yes. Are we doing scale-up optical? Yes. We need more copper, more optics, more CPO."
- Jensen Huang, GTC 2026: "Feynman has Kyber with copper and CPO scale-up."
- SemiAnalysis on scale-out CPO: TCO advantage "not compelling enough for customers to dive headfirst into an entirely different deployment paradigm."
- Cignal AI, February 2025 report: "Inevitable but Not Imminent." Mass deployment 3-5 years away.

### Industry players

| Company | CPO role | Key product/move |
|---------|----------|------------------|
| [[NVIDIA]] | Scale-up + scale-out | Spectrum-X Photonics (full production GTC 2026), Quantum-X Photonics, Feynman 2028 |
| [[Broadcom]] | Scale-out | Bailly CPO switch (8 optical engines, Tomahawk 5, 51.2Tbps) — first volume production |
| [[Marvell]] | Custom silicon | Acquired [[Celestial AI]] for $3.25B |
| [[Ayar Labs]] | Chiplet approach | $500M Series E, ~$870M total funding, [[NVIDIA]]/[[MediaTek]] backing |
| [[Lightmatter]] | Photonic fabric | $4.4B valuation |
| [[Arista Networks]] | Pluggable defense | XPO (2027), LPO in production |

### Adoption timeline

| Speed generation | Status |
|-----------------|--------|
| 800G | Pluggables adequate |
| 1.6T | LPO/XPO extend pluggable viability |
| 3.2T+ (400G/lane) | DSP power/insertion loss exceed pluggable limits |
| Inflection | 2028-2030 |

---

## Related

- [[Optical networking primer]] — foundational technology concepts
- [[NVLink]] — scale-up interconnect roadmap and copper limits
- [[NVIDIA]] — leader in both scale-up (NVLink) and scale-out (Spectrum-X) CPO
- [[Broadcom]] — Bailly CPO switch pioneer, Tomahawk 5 integration  
- [[Arista Networks]] — XPO pluggable density breakthrough, LPO power data
- [[Marvell]] — Celestial AI acquisition, custom silicon bet
- [[Coherent Corp]] — incumbent transceiver leader, CPO disruption risk
- [[Lumentum]] — laser supplier, could benefit from CPO laser demand
- [[Lightmatter]] — photonic fabric alternative approach
- [[Ayar Labs]] — chiplet-based CPO architecture
- [[Hyperscaler capex]] — demand driver for data center interconnect upgrades