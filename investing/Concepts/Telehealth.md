---
aliases:
  - Telemedicine
  - Virtual care
  - Remote healthcare
  - Telehealth prescribing
---
#concept #healthcare #regulation #technology

# Telehealth

Remote delivery of healthcare services via telecommunications — video visits, phone consultations, asynchronous messaging, and remote patient monitoring. The defining healthcare delivery shift of the 2020s, accelerated by COVID-19 but settling into a structural niche (~6% of visits) anchored by behavioral health and chronic condition management.

> Telehealth didn't replace in-person care. It created a parallel channel that selectively dominates specific use cases — mental health (44% of visits), GLP-1 prescribing, and employer-sponsored primary care — while remaining marginal for most specialties.

---

## Market size

| Year | US market size | Source |
|------|---------------|--------|
| 2023 | ~$50B | Nova One Advisor |
| 2024 | $42-81B | Range reflects definitional differences (narrow vs broad scope) |
| 2025 | $53-75B | Towards Healthcare / Precedence Research |
| 2026 | $65-81B | Towards Healthcare / Fortune Business Insights |
| CAGR to 2030 | ~23-25% | Consensus across research firms |

Wide ranges reflect scope: narrow (virtual consultations only) vs broad (remote patient monitoring, digital therapeutics, software, hardware).

---

## How it works

### Visit types

| Type | Description | Examples |
|------|-------------|---------|
| Synchronous video | Real-time video consultation | [[Teladoc]], [[Amwell]] |
| Asynchronous/store-and-forward | Patient submits info, clinician responds later | [[Ro]], [[Hims & Hers]] (intake forms) |
| Audio-only | Phone consultations | Medicare-covered since COVID waivers |
| Remote patient monitoring | Connected devices transmit vitals | Chronic care management |

### Prescription fulfillment models

| Model | How it works | Who uses it |
|-------|-------------|-------------|
| E-prescribe to retail pharmacy | Clinician sends Rx via Surescripts to CVS/Walgreens | [[Teladoc]], [[Amwell]] |
| In-house pharmacy | Platform owns pharmacy, fills and ships directly | [[Ro]] (Ro Pharmacy), [[Hims & Hers]] |
| Compounding pharmacy | Platform partners with 503A/503B compounders | DTC platforms (pre-crackdown) |
| Direct pharma integration | Platform connects to manufacturer programs | [[Ro]] (NovoCare, LillyDirect), LifeMD |

---

## Regulatory framework

### Federal

| Law/Rule | Date | What it does |
|----------|------|-------------|
| Ryan Haight Act | 2008 | Requires at least one in-person evaluation before prescribing controlled substances via telehealth. Named after a teenager who died from online-purchased drugs. |
| COVID PHE waivers | Mar 2020 | DEA and HHS waived in-person requirement for controlled substance prescribing. PHE ended May 11, 2023. |
| 1st temporary extension | May 2023 | Extended COVID telehealth flexibilities post-PHE |
| 2nd temporary extension | Oct 2023 | Further extension |
| 3rd temporary extension | Nov 2024 | Further extension |
| 4th temporary extension | Jan 1, 2026 | Current: practitioners can prescribe Schedule II-V controlled substances via telehealth without in-person evaluation through Dec 31, 2026 |
| Biden proposed permanent rule | Jan 2025 | "Special Registrations for Telemedicine" — three pathways. Trump administration has not finalized. |

Nothing is permanent. All telehealth prescribing flexibilities for controlled substances expire December 31, 2026. The [[DEA]] has indicated it plans to finalize one of its previous proposed rules rather than issue a new one.

### State-level variation

States independently regulate telehealth prescribing, licensure, and reimbursement. The Interstate Medical Licensure Compact (IMLC) allows expedited licensing across 42 member states but does not create a universal telehealth license. Key restrictions:
- Some states require in-state licensing for telehealth prescribers
- Controlled substance prescribing rules vary by state
- [[California]] adopted strict compounding rules (Jun 2025)
- [[Florida]] passed weight-loss-specific compounding restrictions (SB 860)

---

## Utilization: the COVID spike and normalization

| Period | Telehealth as % of E&M visits | Notes |
|--------|-------------------------------|-------|
| Pre-pandemic | ~0.1% | Baseline |
| April 2020 peak | ~41% | Medicare FFS data |
| 2023-2024 stabilized | 5.7-7.0% | Medicare FFS |
| Q3 2023 | 54.7% below Q2 2020 peak | Trilliant Health |

### By specialty (post-pandemic)

| Specialty | Telehealth share |
|-----------|-----------------|
| Behavioral health | 43.8% (anchor use case) |
| Primary care | 8.4% |
| Orthopedic surgery | 1.2% |

Behavioral health rose from 41.4% of telehealth visits (Q1 2020) to 67.0% (Q3 2023). Mental health is the structural winner — everything else reverted largely to in-person.

### Failures and retreats

| Date | Event |
|------|-------|
| May 2024 | [[Optum]] Virtual Care shut down after 3 years |
| May 2024 | [[Walmart]] shuttered 51 health centers + virtual care — cited reimbursement and cost challenges |

---

## Business models

| Model | Description | Revenue source | Examples |
|-------|-------------|---------------|----------|
| B2B enterprise | Sell to employers, health plans, hospitals | PMPM fees, enterprise contracts | [[Teladoc]], [[Amwell]], Transcarent |
| DTC cash-pay | Sell directly to consumers, bypass insurance | Subscriptions, product/Rx markup | [[Ro]], [[Hims & Hers]], LifeMD |
| Marketplace/discount | Connect consumers to cheaper prescriptions | Transaction fees, advertising | [[GoodRx]] |
| Employer-sponsored DTC | Employer pays, employees use DTC-like interface | Per-employee fees | [[Amazon]] One Medical ($9/mo for Prime) |

The DTC cash-pay model has outperformed B2B on growth: [[Hims & Hers]] grew revenue +69% in 2024 vs [[Teladoc]] at -1%. But DTC faces higher churn (~50% annually) and regulatory risk from the [[GLP-1 receptor agonists|GLP-1]] compounding crackdown. See [[DTC Telehealth]] for the investment sector view.

---

## The GLP-1 catalyst

[[GLP-1 receptor agonists]] became the killer use case for DTC telehealth starting in 2022-2023. The compounding loophole (Section 503A/503B) allowed platforms to offer semaglutide at $100-300/mo vs $1,000+ branded. This drove explosive growth:
- [[Hims & Hers]]: GLP-1 weight loss guided ~$725M for 2025 (~31% of revenue)
- [[Ro]]: ~$370M GLP-1 revenue estimated (2024, Sacra)
- LifeMD: weight management >50% of revenue (Q3 2025)

The FDA resolved the semaglutide shortage (Feb 2025) and is closing the compounding loophole. See [[GLP-1 receptor agonists]] for the full enforcement timeline. Platforms are transitioning to branded partnerships (NovoCare, LillyDirect) at $149-449/mo, compressing the margin advantage that fueled growth.

---

## Related

- [[GLP-1 receptor agonists]] — the drug class driving DTC telehealth growth
- [[DTC Telehealth]] — investment sector grouping the cash-pay platforms
- [[Ro]] — vertically integrated telehealth, Novo's preferred partner
- [[Hims & Hers]] — largest public DTC telehealth platform
- [[Teladoc]] — largest B2B telehealth, down ~98% from peak
- [[Healthcare]] — parent sector
- [[Biopharma]] — drug supply chain context

---

*Created 2026-02-09*
