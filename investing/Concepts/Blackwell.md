#concept #nvidia #semiconductors #ai

**Blackwell** — [[NVIDIA]]'s AI GPU architecture (2024-). B100/B200/GB200 chips. First to use CoWoS-L packaging — which caused yield issues requiring B200A rework.

---

## Architecture

| Chip | Specs | Status |
|------|-------|--------|
| B100 | 208B transistors, 4nm | Shipping |
| B200 | Dual-die design, 8 HBM stacks | Limited (packaging issues) |
| **B200A** | Single B102 die, 4 HBM stacks | Rework — main volume |
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

**Per [[SemiAnalysis]]:** Blackwell had significant packaging problems requiring design changes.

| Issue | Detail |
|-------|--------|
| Root cause | First high-volume design using [[TSMC]]'s CoWoS-L technology |
| Problems | Packaging issues at TSMC + NVIDIA design flaws |
| Cancelled | HGX form-factors (B100/B200) outside initial lower volumes |
| Rework | **B200A** introduced — single monolithic B102 die + 4 HBM stacks |

### B200A vs original B200

| Spec | B200 (original) | B200A (rework) |
|------|-----------------|----------------|
| Die | Dual-die design | Single monolithic B102 |
| HBM stacks | 8 | 4 |
| Complexity | Higher | Simplified |
| CoWoS-L | Yes | Reduced requirements |

**Why it matters:** CoWoS-L was supposed to be NVIDIA's packaging upgrade, but yield issues forced a simpler design. This validated concerns about [[Advanced packaging]] as the binding constraint on AI chips, not fab capacity.

Source: [[SemiAnalysis]] — [Blackwell Reworked](https://newsletter.semianalysis.com/p/nvidias-blackwell-reworked-shipment)

---

## Deployment challenges

| Factor | Change from Hopper |
|--------|--------------------|
| Cooling | Air → liquid |
| Rack weight | 1,000 lbs → 3,000 lbs |
| Power per rack | 30 kW → 130 kW |
| Legacy DC retrofit | Extremely difficult |

Most existing data centers can't deploy Blackwell without major infrastructure upgrades. See [[GPU deployment bottleneck]].

---

## Market impact

| Effect | Description |
|--------|-------------|
| NVIDIA stock | Rally on announcement, volatility on rework reports |
| Hyperscaler orders | Massive pre-orders ($500B+ booked through 2028) |
| Competition | [[AMD]], [[Intel]] further behind |
| Supply chain | [[TSMC]] CoWoS constraints — validated by rework |

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

---

*Updated 2026-02-01*
