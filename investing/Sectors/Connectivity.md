---
aliases: [Connectivity cluster, Networking semiconductors]
---
#sector #semiconductor #networking #fabless

# Connectivity

Networking and connectivity semiconductor cluster. AVGO, QCOM, MRVL trade together (0.58 avg correlation), separate from AI/Compute cluster.

![[connectivity-sector-chart.png]]
*AVGO outperforming (+265% since 2024) on AI networking exposure. QCOM and MRVL lagging but moving together.*

---

## Key actors

| Company | Focus | Position |
|---------|-------|----------|
| [[Broadcom]] | Networking ASICs, switching | Diversified, [[Apple]] modem win |
| [[Qualcomm]] | Mobile modems, RF | Mobile connectivity leader |
| [[Marvell]] | Data center networking, storage | Cloud infrastructure |

---

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Avg correlation** | 0.58 | Moderate-strong (valid cluster) |
| Range | 0.55 - 0.63 | AVGO-QCOM to AVGO-MRVL |
| vs AI/Compute cluster | ~0.35 | Distinct clusters |
| Period | 2024-01 to present | |

Pairwise detail:
| Pair | Correlation |
|------|-------------|
| AVGO - MRVL | 0.63 |
| AVGO - QCOM | 0.55 |
| QCOM - MRVL | 0.55 |

---

## Why this cluster exists

Shared end markets:
- Data center networking (all three)
- 5G infrastructure (QCOM, MRVL)
- Enterprise connectivity (AVGO, MRVL)

Different from AI/Compute:
- Less tied to GPU/AI accelerator demand
- More diversified revenue (mobile, enterprise, auto)
- Different [[TSMC]] dependency (less cutting-edge)

---

## vs AI/Compute cluster

| Metric | AI/Compute | Connectivity |
|--------|------------|--------------|
| Avg correlation | 0.61 | 0.58 |
| [[TSMC]] dependency | Very high (N3, N4) | Moderate (N5, N7) |
| AI exposure | Direct (GPUs) | Indirect (networking) |
| Cross-cluster corr | — | ~0.35 |

The clusters are moderately separated — connectivity names don't move in lockstep with NVDA/[[AMD]] rallies.

---

## May 2026: Marvell AI networking acceleration

[[Marvell]]'s May 27, 2026 Q1 FY2027 report is the cleanest current signal that the connectivity cluster is being pulled deeper into the AI infrastructure cycle. Marvell reported record Q1 revenue of $2.418B, with data center revenue of $1.833B, roughly 76% of total revenue. The Q2 FY2027 guide of $2.7B at the midpoint beat [[Reuters]]/[[LSEG]] consensus and implies 35% YoY growth.

The important detail is the product mix: management tied the acceleration to 800G and 1.6T scale-out optics, 51.2T Ethernet scale-out switches, NPO/CPO scale-up optical solutions, scale-across datacenter interconnect modules, and custom XPU / XPU-attach solutions. That moves Marvell from "indirect AI networking beneficiary" toward a direct custom-silicon and optical-interconnect supplier to [[AI hyperscalers]].

Cluster read-through: the [[Connectivity]] child remains a looser trading cluster than [[AI Compute]], but the business exposure is converging. [[Broadcom]] and Marvell are now the two public names where custom AI silicon and networking sit in the same P&L, while [[Qualcomm]] keeps the cluster partly tied to mobile/RF cycles. Do not treat this as a new cluster-validation result until the correlations are rerun; treat it as a fundamental watch item.

*Sources: [Marvell Q1 FY2027 release](https://investor.marvell.com/news-events/press-releases/detail/1023/marvell-technology-inc-reports-first-quarter-of-fiscal-year-2027-financial-results), [Marvell Q1 FY2027 financial/business results presentation](https://d1io3yog0oux5.cloudfront.net/_6c98e153147f20a85f8f719ed2bcb520/marvell/db/3734/35382/presentation/2026_05_27_Marvell_Q1_FY27_financial_business_results_FINAL.pdf), [[Reuters]] via [StreetInsider](https://www.streetinsider.com/Reuters/Marvell%2Bforecasts%2Bquarterly%2Brevenue%2Babove%2Bestimates%2Bon%2BAI%2Bchip%2Bdemand/26557948.html), May 27 2026.*

---

## Related

### Parent
- [[Semiconductors]] — parent sector

### Sister clusters
- [[AI Compute]] — TSM, NVDA, [[AMD]] cluster
- [[WFE]] — equipment suppliers

### Actors
- [[Broadcom]] — networking ASICs
- [[Qualcomm]] — mobile connectivity
- [[Marvell]] — data center networking

### Context
- [[AI hyperscalers]] — indirect beneficiary (networking for AI clusters)
- [[5G]] — demand driver

*Created 2026-01-30*
