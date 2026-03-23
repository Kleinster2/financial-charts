---
aliases: [CPO, co-packaged optics]
tags: [concept, networking, infrastructure, semiconductors, ai-infrastructure]
---

**Co-Packaged Optics** — integrating optical engines directly inside semiconductor packages alongside switch chips or GPUs, rather than using external pluggable transceivers. The technology promises substantial power and latency benefits but faces manufacturing, thermal, and economic challenges that have kept adoption limited.

Instead of electrical signals traveling tens of centimeters across copper PCB traces to reach a pluggable module on the front panel, CPO moves that conversion point to just millimeters inside the package before converting to light. This architectural shift could reshape data center networking, but the transition timeline and competitive dynamics with enhanced pluggables remain hotly contested.

The CPO story splits into two domains: scale-up (GPU-to-GPU interconnect) where copper still dominates but faces physics limits, and scale-out (network switches) where pluggable optics reign but DSP power consumption is becoming unmanageable at higher speeds. Each domain has different economics, different players, and different timelines toward CPO adoption.

---

## What CPO is

Traditional data center architecture uses pluggable optical transceivers — modules that plug into switch front panels and convert electrical signals from the switch ASIC to optical signals for fiber transmission. This requires electrical signals to travel across long PCB traces, consuming power and adding latency.

**Co-packaged optics** places the optical engine inside the same semiconductor package as the switch chip or GPU. The electrical-to-optical conversion happens within millimeters of signal generation, eliminating long electrical traces and their associated losses.

| Architecture | Signal path | Power | Latency | Serviceability |
|--------------|-------------|-------|---------|----------------|
| **Pluggable** | ASIC → PCB traces (cm) → module | Higher | Higher | Easy swap |
| **CPO** | ASIC → optical engine (mm) | 30-50% lower | Lower | Board-level |

The power reduction comes from eliminating DSP (digital signal processing) chips that condition signals for long electrical traces, plus reduced losses from shorter signal paths.

---

## Scale-up domain

### [[NVIDIA]] roadmap and the copper wall

Scale-up refers to GPU-to-GPU communication within training clusters. [[NVIDIA]]'s roadmap shows copper's dominance extending longer than expected, but physical limits are approaching.

| Generation | Year | NVLink version | Bandwidth per GPU | Technology | Notes |
|------------|------|----------------|-------------------|------------|-------|
| **Blackwell** | 2024-25 | NVLink 5.0 | 1.8TB/s | Copper DAC | NVL72 rack |
| **Vera Rubin** | 2026 | NVLink 6.0 | 3.6TB/s | Copper | Doubled lanes, not speed. Oberon rack, 5,000+ cables (2 miles total) |
| **Rubin Ultra** | 2027 | NVLink 6.0+ | TBD | Copper | Kyber rack, 144 GPU packages (576 dies), PCB midplane |
| **Feynman** | 2028 | NVLink 8 | TBD | Copper + CPO | Jensen at GTC 2026: "Feynman has Kyber with copper and CPO scale-up" |

**The copper wall physics:** SerDes (serializer/deserializer) speeds are hitting fundamental limits. At 224G SerDes (current generation), the industry uses bi-directional transmission — sending data both ways on the same trace. This works once, but scaling to 448G SerDes would require ~244 GBaud in PAM4 modulation, creating overwhelming power consumption and insertion loss.

**Lane count stagnation:** NVLink lane count barely moved from v1.0 to 5.0 (32 to 36 lanes). Almost all bandwidth gains came from faster lanes rather than more lanes. If lane speed hits physics limits, copper scaling cannot continue without a different approach.

### Scale-up CPO challenges

**Micro-ring resonators (MRR):** CPO relies on silicon photonic components that are temperature-sensitive. A 1°C shift moves resonant wavelength ~0.1nm. With CWDM4 channel spacing at 0.8nm, an 8°C drift causes channel overlap. GPU ASICs run at 90°C+, requiring individual heaters for thermal control — burning back the power savings CPO was supposed to deliver. Liquid cooling becomes a prerequisite.

**Laser degradation:** Lasers lose efficiency rapidly above 70°C with accelerated component degradation. The External Laser Source (ELS) standard addresses this by placing lasers outside the package and sending CW (continuous wave) light via polarization-maintaining fiber. Current O-band lasers at 50°C top out at ~80mW output power, but CPO needs 286mW for WDM (wavelength division multiplexing) or 100mW+ for DR (direct detect) applications.

**Yield economics:** One failed optical engine destroys an entire $10,000+ GPU package. Known Good Die (KGD) verification is critical, but wafer-level optical testing remains immature. Packaging yields struggle to exceed 85% — a 15% scrap rate devastates economics compared to copper DAC that costs 10x less, delivers sub-nanosecond latency, and has 20+ years of field data.

---

## Scale-out domain

### DSP power wall

Scale-out networking (Ethernet/InfiniBand switches) faces a different challenge: DSP power consumption in pluggable transceivers. At 400G speeds, the DSP alone consumes ~4W — roughly half the total transceiver power. A 128,000-GPU cluster requires hundreds of thousands of pluggables, each drawing 10-15W, aggregating to megawatts of power.

**[[Broadcom]] numbers:** For an 800Gbps port, pluggable transceivers consume 15W versus CPO at 5.5W — roughly a 3x power reduction. At 800G, pluggables work acceptably. At 3.2T and beyond, DSP power becomes unmanageable, making CPO inevitable.

**CPO's advantage:** Eliminating the DSP entirely by moving signal processing to the switch ASIC, which already handles complex digital operations efficiently.

### Current scale-out CPO status

Products exist but adoption remains limited. SemiAnalysis assessment: TCO advantage "not compelling enough for customers to dive headfirst into an entirely different deployment paradigm." Cignal AI's February 2025 report titled "Inevitable but Not Imminent" projects mass deployment 3-5 years away.

---

## Technical challenges

**Thermal management:** Micro-ring resonators require precise temperature control. Every 1°C variation shifts optical wavelength 0.1nm. In CWDM systems with 0.8nm channel spacing, 8°C of thermal drift causes channel crosstalk. GPU packages running at 90°C+ need individual heating elements for each optical component — consuming power that CPO was supposed to save.

**Laser integration:** Direct integration of lasers with silicon photonics remains problematic above 70°C. External Laser Sources (ELS) move lasers outside the package and pipe continuous-wave light through polarization-maintaining fiber. Current commercial O-band lasers deliver ~80mW at 50°C, while CPO applications need 100mW+ for direct-detect or 286mW for WDM applications.

**Manufacturing yield:** Optical engines integrate multiple components (modulators, photodetectors, waveguides) whose individual failures doom the entire package. Known Good Die verification requires wafer-level optical testing that remains technically immature. When packaging yields exceed 85%, a 15% scrap rate on $10,000+ packages destroys cost competitiveness versus copper alternatives.

**Cost structure:** Copper DAC cables cost 10x+ less than CPO equivalents, deliver sub-nanosecond latency, and benefit from 20+ years of field deployment data. [[Broadcom]] CEO Hock Tan, March 2026 earnings: "We're not quite there yet."

---

## The pluggable counterpunch

### Linear Pluggable Optics (LPO)

Rather than concede to CPO, the pluggable industry fights back with LPO — removing DSP from the pluggable module and shifting signal conditioning to the switch chip. Same form factor, 30-50% power reduction. Already in production at [[NVIDIA]] Spectrum-X and [[Meta]] deployments.

**Performance parity:** Data from [[Arista Networks]]'s Andy Bechtolsheim at OFC 2025 shows at 1.6Tbps, DSP pluggables consume 25W, CPO ~10W, but LPO also reaches ~10W. LPO matches CPO on power at 1.6T speeds while preserving pluggable's serviceability advantages.

### eXtra-dense Pluggable Optics (XPO)

[[Arista Networks]] unveiled XPO at OFC 2026 (March 13, ten days before this analysis), directly attacking CPO's density narrative:

**Specifications:**
- 12.8Tbps per module (8x current OSFP capacity)
- 64 lanes at 200Gbps per lane  
- 204.8Tbps per rack unit (4x OSFP per RU)
- Integrated liquid cooling cold plate (400W per module)
- 45 founding members in the Multi-Source Agreement
- [[Microsoft]] backing provides hyperscaler credibility
- Volume production targeted for 2027

**System impact:** In a 400MW data center with 128,000 GPUs, the typical 1,400+ OSFP switch racks would shrink by 75% with XPO density improvements. This destroys the "pluggable has a density ceiling" argument that CPO proponents rely on.

### Pluggable structural advantages

**Serviceability:** Pull and replace a failed module in minutes versus swapping an entire switch board for CPO failures. In hyperscale environments where component failures are routine, this operational difference matters enormously.

**Supply chain diversity:** The OSFP Multi-Source Agreement has dozens of participating vendors. Hyperscalers explicitly avoid vendor lock-in situations. CPO packages tie customers to specific ASIC/optical engine combinations.

**Proven field data:** Current CPO shipment volume approaches zero while next year's projected OSFP shipments exceed 50 million units. [[Broadcom]] and [[Meta]] announced "1 million hours flap-free" operation (October 2025), but this pales against 20 years of pluggable field experience.

**Design flexibility:** [[NVIDIA]] designed removable OSA (Optical Sub-Assembly) interfaces for Quantum-X CPO products, acknowledging serviceability concerns, but field validation remains incomplete.

---

## Companies and timeline

### Industry players

**[[NVIDIA]]:** Spectrum-X Photonics (Ethernet CPO) and Quantum-X Photonics (InfiniBand CPO) announced at GTC 2025. Spectrum-X CPO reached "full production" status at GTC 2026, making [[NVIDIA]] the first major networking vendor with volume CPO deployment.

**[[Broadcom]]:** Bailly CPO switch integrates 8 optical engines with Tomahawk 5 silicon for 51.2Tbps aggregate bandwidth. This represents the industry's first volume production CPO switching platform.

**[[Marvell]]:** Acquired Celestial AI for $3.25B, signaling major commitment to CPO technology and custom silicon integration.

**[[Ayar Labs]]:** Raised $500M Series E with [[NVIDIA]] and MediaTek participation. This brings their total verified funding to ~$870M (note: article claims "cumulative funding past $2.6B" but this conflicts with verified data).

**[[Lightmatter]]:** $4.4B valuation with their photonic fabric approach, targeting both training and inference workloads with optical interconnection.

### Adoption timeline

**Consensus view:**
- **800G generation:** Pluggables handle requirements adequately
- **1.6T generation:** LPO and XPO extend pluggable viability
- **3.2T+ generation** (400G-per-lane): DSP power and insertion loss push beyond pluggable limits
- **Inflection point:** 2028-2030

**[[NVIDIA]]'s perspective:** Jensen at GTC 2026: "Is copper still important? Yes. Are we doing scale-up optical? Yes. We need more copper, more optics, more CPO." Coexistence continues through 2028.

---

## Investment implications

**CPO bulls argue:** Physics limits force the transition. Power consumption at 3.2T+ speeds makes pluggables uneconomical. Early movers like [[Broadcom]] and [[NVIDIA]] will capture outsized returns during the transition.

**CPO bears counter:** Pluggables fight back effectively with LPO/XPO innovations. Manufacturing challenges (yield, thermal, cost) remain unsolved. Hyperscaler resistance to vendor lock-in favors pluggable diversity.

**Sector rotation risk:** If CPO adoption accelerates faster than expected, traditional transceiver vendors ([[Coherent Corp]], [[Lumentum]]) face disruption while integrated semiconductor companies ([[Broadcom]], [[Marvell]]) benefit. If pluggables successfully defend with LPO/XPO, the reverse occurs.

**Timeline sensitivity:** Investment thesis depends heavily on adoption inflection timing. 2028 versus 2032 makes enormous difference for competitive positioning and capital allocation.

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