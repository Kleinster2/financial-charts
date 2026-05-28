#concept #nvidia #semiconductors #ai

**Blackwell** — [[NVIDIA]]'s AI GPU architecture (2024-). B100/B200/GB200 chips. First to use CoWoS-L packaging — which caused yield issues requiring B200A rework.

---

## Synthesis

Blackwell is the first NVIDIA architecture where the deployment bottleneck is as visible as the chip bottleneck. The silicon matters, but the tradeable constraint has moved into rack power, cooling, site readiness, power smoothing, integration, and customer-specific commissioning. That is why the note spans both the architecture and deployments such as IREN's Childress buildout.

---

## Architecture

| Chip | Specs | Status |
|------|-------|--------|
| B100 | 208B transistors, 4nm | Shipping |
| B200 | Dual-die design, 8 HBM stacks | Limited (packaging issues) |
| B200A | Single B102 die, 4 HBM stacks | Rework — main volume |
| GB200 | Grace Blackwell superchip | Shipping |
| NVL72 | 72-GPU rack system | Shipping |

---

## Performance vs Hopper

| Metric | Improvement |
|--------|-------------|
| Inference | 4x |
| Training | 2.5x |
| Energy efficiency | 25x |

---

## Timeline

| Date | Event |
|------|-------|
| Mar 2024 | Announced at GTC |
| Sep 2024 | Packaging issues surface; B200A rework |
| Late 2024 | Volume shipping begins |
| Jan 2025 | 6M GPUs shipped (per Jensen) |

---

## Packaging issues & rework (Sep 2024)

Per [[SemiAnalysis]]: Blackwell had significant packaging problems requiring design changes.

| Issue | Detail |
|-------|--------|
| Root cause | First high-volume design using [[TSMC]]'s CoWoS-L technology |
| Problems | Packaging issues at TSMC + NVIDIA design flaws |
| Cancelled | HGX form-factors (B100/B200) outside initial lower volumes |
| Rework | B200A introduced — single monolithic B102 die + 4 HBM stacks |

### B200A vs original B200

| Spec | B200 (original) | B200A (rework) |
|------|-----------------|----------------|
| Die | Dual-die design | Single monolithic B102 |
| HBM stacks | 8 | 4 |
| Complexity | Higher | Simplified |
| CoWoS-L | Yes | Reduced requirements |

Why it matters: CoWoS-L was supposed to be NVIDIA's packaging upgrade, but yield issues forced a simpler design. This validated concerns about [[Advanced packaging]] as the binding constraint on AI chips, not fab capacity.

Source: [[SemiAnalysis]] — [Blackwell Reworked](https://newsletter.semianalysis.com/p/nvidias-blackwell-reworked-shipment)

---

## Deployment challenges

| Factor | Change from Hopper |
|--------|--------------------|
| Cooling | Air → liquid |
| Rack weight | 1,000 lbs → 3,000 lbs |
| Power per rack | 30 kW → 130 kW |
| Power profile | Aggressive draw spikes — requires hardware power smoothing (see below) |
| Software stack | Hopper-era stacks can damage GB200 silicon under irregular loads |
| Legacy DC retrofit | Extremely difficult |

Most existing data centers can't deploy Blackwell without major infrastructure upgrades. See [[GPU deployment bottleneck]].

### Power smoothing as hardware feature

[[NVIDIA]] documents power smoothing as an explicit hardware feature on GB200 (and the GB300 successor) because Blackwell silicon draws power so aggressively that bulk-synchronous workloads (training step boundaries, batch processing) create coordinated multi-megawatt swings at the rack and grid level. Without smoothing, those swings cause failures at utility, transformer, and UPS layers. The GB300 NVL72 ships with PSUs containing energy storage that smooths grid demand peaks by up to 30%; the same feature is being backported to GB200 NVL72 deployments (per [[NVIDIA]] technical blog).

The operational consequence — relevant for any operator running mixed [[Hopper]] / Blackwell clusters — is that software stacks optimized for the smoother Hopper power profile do not understand the GB200 hardware features. Zeeshan Patel (formerly head of multimodal pre-training at [[xAI]]) reported observed cases of GB200s being physically destroyed (chip-level damage) when xAI's Hopper-era stack imposed irregular loads. The implication: deploying GB200 in a mixed-architecture cluster (e.g., [[Colossus|Colossus 1]]) requires stack-level rewrites to avoid silicon damage, on top of the standard cooling/power infrastructure upgrades.

Mitigation work is ongoing across [[Meta]], [[Google]], and [[NVIDIA]]'s reference implementations. The thermal/overheating headlines from late 2025 ("Blackwell servers overheating, customers cutting orders") have been largely addressed per [[SemiAnalysis]] coverage, but the power-management dimension is a separate and ongoing problem class.

---

## Market impact

| Effect | Description |
|--------|-------------|
| NVIDIA stock | Rally on announcement, volatility on rework reports |
| Hyperscaler orders | Massive pre-orders ($500B+ booked through 2028) |
| Competition | [[AMD]], [[Intel]] further behind |
| Supply chain | [[TSMC]] CoWoS constraints — validated by rework |

---

## IREN Childress deployment (May 2026)

[[IREN]]'s May 2026 Childress sequence is a useful deployment marker because it is an air-cooled Blackwell build outside the classic hyperscaler owned-campus model. IREN signed a five-year, ~$3.4B managed GPU cloud contract with [[NVIDIA]] for internal AI and research workloads, then agreed to buy about $1.6B of Dell-supplied Blackwell systems for the same Childress, Texas deployment.

The systems are scheduled for existing IREN data centers, with commissioning targeted for early 2027. The disclosure did not identify a specific Blackwell SKU in the May 26 release, but the May 7 IREN materials said the NVIDIA contract would be serviced by air-cooled Blackwell platform systems across roughly 60MW. The operational read-through is that Blackwell deployment bottlenecks are spreading from hyperscaler campuses into the crypto-to-AI cohort: procurement, integration services, post-shipment payment terms, and site readiness are now part of the tradeable story.

---

## Successor: Rubin

| Chip | Timeline | Notes |
|------|----------|-------|
| Vera Rubin | H2 2026 | 5x inference vs Blackwell |
| Rubin Ultra | 2027 | Next-gen after Vera |

---

## Related

### Actors
- [[NVIDIA]] — chip maker
- [[TSMC]] — manufacturer (CoWoS-L issues)
- [[SK Hynix]] — [[HBM]] supplier
- [[SemiAnalysis]] — broke rework story

### Concepts
- [[Advanced packaging]] — CoWoS (binding constraint)
- [[GPU deployment bottleneck]] — infrastructure constraints
- [[AI datacenter architecture]] — infrastructure requirements
- [[HBM]] — memory technology
- [[IREN]] — May 2026 air-cooled Blackwell deployment at Childress
- [[Dell]] — system supplier for IREN's Childress Blackwell purchase

---

*Updated 2026-05-26*
