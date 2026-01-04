#concept #datacenter #infrastructure #ai

AI datacenters require fundamentally different architecture than legacy facilities. GPU density, liquid cooling, and network coherence drive purpose-built designs.

---

## Why AI DCs are different

| Requirement | Legacy DC | AI DC |
|-------------|-----------|-------|
| **Cooling** | Air | Liquid (required for Blackwell+) |
| **Power density** | 10-20 kW/rack | 100-130 kW/rack |
| **Rack weight** | ~1,000 lbs | ~3,000 lbs |
| **GPU proximity** | Not critical | Critical for network coherence |
| **Building design** | Spread out, 1-story | Ultra-dense, multi-story |

---

## Microsoft Fairwater design (case study)

**Per SemiAnalysis satellite analysis:**

| Building Type | Stories | Power | Cooling | Purpose |
|---------------|---------|-------|---------|---------|
| **GPU Building** | 2 | 300MW | Liquid | Ultra-dense GPU clusters |
| **CPU/Storage Building** | 1 | 48MW | Air | Storage, control plane, RL environments |

**Design rationale:**
- GPUs must be **physically close** for network coherence
- Optimal for training clusters that need fast interconnect
- 2-story design maximizes GPU density
- RL environments co-located for developer productivity (not strictly required)

---

## Network coherence requirement

**Why physical proximity matters:**

Training large models requires GPUs to communicate constantly:
- Gradient synchronization
- Tensor parallelism
- Pipeline parallelism
- All-reduce operations

**Latency sensitivity:**
- Nanoseconds matter at scale
- Longer cables = more latency
- Network switches add hops
- Physical distance = training slowdown

**Result:** Ultra-dense 2-story buildings, not spread-out campuses.

---

## Cooling architecture

**Air cooling (legacy):**
- Sufficient for CPUs, storage
- Works up to ~30 kW/rack
- Standard HVAC systems
- Hopper-class GPUs (barely)

**Liquid cooling (required for AI):**
- Direct-to-chip liquid cooling
- 100+ kW/rack capability
- Specialized plumbing infrastructure
- Blackwell, Rubin, and beyond

**Rear-door heat exchangers:**
- Intermediate solution
- Water-cooled doors on racks
- Still limited vs direct liquid

---

## Power architecture

**Traditional DC:**
- 10-20 MW total
- Shared across many tenants
- UPS and generator backup

**AI DC:**
- 100-500+ MW per facility
- Dedicated substations
- Often behind-the-meter generation
- Nuclear, gas, or solar partnerships

**Examples:**
- Meta Prometheus: 1GW
- Meta Hyperion: 5GW eventual
- xAI Colossus: 2GW target

---

## On-site power generation (BYOP)

See [[BYOP]] for full pattern. Hyperscalers increasingly generating their own power.

**Meta Socrates South (hybrid fleet design):**

| Equipment | Units | MW each | Total |
|-----------|-------|---------|-------|
| [[Solar Turbines]] Titan 250 IGT | 3 | 23 MW | 69 MW |
| [[Solar Turbines]] Titan 130 IGT | 9 | 16.5 MW | 148.5 MW |
| [[Siemens Energy]] SGT-400 IGT | 3 | 14.3 MW | 42.9 MW |
| Caterpillar 3520 fast-start | 15 | 3.1 MW | 46.5 MW |
| **Gross total** | | | **~307 MW** |

**N+1+1 design:** Redundancy yields 200MW+ operational capacity.

**Design philosophy:**
- **Hybrid fleet** — 4 turbine types diversifies supplier/technology risk
- **Fast-start engines** — Caterpillar 3520s can ramp in seconds (peaker role)
- **IGTs (industrial gas turbines)** — baseload power
- **Vendor diversification** — Solar Turbines (Caterpillar) + Siemens Energy

**Contrast with OpenAI UAE:**
- OpenAI: Single-vendor (4x Ansaldo Energia AE94.3)
- Meta: Multi-vendor hybrid fleet

Both valid — Meta prioritizes supply chain resilience, OpenAI prioritizes simplicity/scale

---

## Implications for GPU deployment

This explains [[GPU deployment bottleneck]]:

1. **Can't retrofit legacy DCs** — wrong architecture entirely
2. **Purpose-built takes 3 years** — Jensen's timeline quote
3. **GPUs ship before DCs ready** — creates CIP buildup
4. **Hyperscalers building new** — not expanding existing

---

## Structural beneficiaries

| Category | Companies |
|----------|-----------|
| **Liquid cooling** | Vertiv, Schneider Electric, Modine |
| **Power infrastructure** | GE Vernova, Siemens Energy |
| **DC construction** | Digital Realty, Equinix, CoreWeave |
| **Crypto miners (pivot)** | TeraWulf, Hut 8, Cipher Mining, IREN |

---

*Updated 2026-01-04*

---

## Related

- [[GPU deployment bottleneck]] — shipped ≠ deployed
- [[Power constraints]] — enabling constraint
- [[Microsoft]] — Fairwater campus design
- [[Meta]] — Prometheus, Hyperion DCs
- [[xAI]] — Colossus (Memphis)
- [[Thermal limits]] — cooling constraints
- [[Crypto-to-AI pivot]] — miners as DC providers
- [[Vertiv]] — cooling infrastructure
- [[Schneider Electric]] — power/cooling
- [[BYOP]] — on-site power generation pattern
- [[Solar Turbines]] — Meta Socrates South supplier
- [[Siemens Energy]] — Meta Socrates South supplier
- [[Ansaldo Energia]] — OpenAI UAE supplier
