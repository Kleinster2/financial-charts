---
aliases: [Radiant, Ori Industries, Ori]
---
#actor #ai #infrastructure #gpucloud

**Radiant** — [[Brookfield]]'s vertically integrated AI infrastructure company, created Feb 2026 by merging UK cloud-computing startup **Ori Industries** (backed by [[Saudi Aramco]]'s venture arm) with Brookfield's infrastructure capabilities. Self-described as "the first infrastructure company engineered from the ground up to deliver integrated AI compute."

---

## What it does

Radiant builds and operates **AI factories** — vertically integrated facilities bundling GPU compute, data center space, power, and proprietary software into a single offering. Targets:

- **Sovereign governments** — data-sovereign compute (can't cross national borders)
- **Investment-grade enterprises** — long-term contracted capacity
- **Telecom providers** — edge AI infrastructure
- **Europe initially**, with Middle East expansion planned

Also operates the **Ori Global AI Cloud** for customers needing on-demand capacity and rapid deployment.

---

## Business model

| Element | Detail |
|---------|--------|
| Structure | GPU leasing — contracts lock in rents across ~5-year chip life |
| Risk model | "We will not be taking any technology risk" — Sikander Rashid |
| Contracts | Take-or-pay: customers pay full freight even if they stop using chips |
| Customers | Investment grade — sovereign governments, large enterprises, telcos |
| GPU supplier | [[NVIDIA]] Cloud Partner — [[Blackwell]], GB200 NVL72, [[Rubin]] when available |
| Architecture | [[NVIDIA]] DSX reference design |
| Parent fund | Brookfield AI Infrastructure Fund ($100B investment program) |
| Software | Proprietary AI infrastructure platform (from Ori) — bare metal, GPU instances, inference-as-a-service, K8s, fine-tuning, model registries, storage |

---

## Leadership

| Role | Name |
|------|------|
| Executive Chair | **Vishal Padiyar** (Managing Director, Brookfield) |
| President | **Mahdi Yahya** (Founder/CEO of Ori) |

**Padiyar:** "Radiant brings together the economics of infrastructure and the intelligence of software. By aligning long-term capital with leading edge innovation, we have created a unique platform that lowers the cost of compute while raising the standard of performance."

**Yahya:** "For more than seven years, our team has been building toward this moment... Radiant is building the infrastructure to enable a global age of abundance for AI."

**Rashid** (Brookfield Head of AI Infrastructure): "I think of it as a leasing business. Hopefully we are the first of many who will unlock large-scale capital to the theme."

---

## Why it matters

Radiant represents **alternative asset managers entering GPU economics** — a new layer between chip manufacturers ([[NVIDIA]]) and end users. The model:

1. Brookfield raises infrastructure capital at low cost of capital
2. Buys GPUs in bulk from NVIDIA
3. Leases them on take-or-pay contracts to investment-grade customers
4. Bundles with power (Brookfield owns renewables) + data center space + proprietary software

This is the **financialization of compute** — the same playbook that transformed aircraft (GECAS, AerCap), rolling stock, and power generation. GPU economics are converging with infrastructure finance.

Other firms have avoided GPU-as-a-service, fearing chips lose value or become obsolete. Brookfield is betting that take-or-pay contracts with investment-grade counterparties eliminates that risk.

### The Brookfield full-stack advantage

What makes Radiant unique vs. pure-play GPU cloud providers:

| Layer | Brookfield asset | Competitor gap |
|-------|-----------------|----------------|
| **Capital** | $100B AI investment program, low cost of capital | [[CoreWeave]] relies on $7.5B+ debt at higher rates |
| **Power** | Owns renewable portfolio (hydro, wind, solar) + $5B [[Bloom Energy]] fuel cells | Cloud GPU providers buy power at market rates |
| **Data centers** | Existing DC operator investments | Pure GPU plays lease space from others |
| **GPUs** | NVIDIA partnership (fund investor + supplier) | Most providers are just customers |
| **Software** | Ori's 7-year platform (orchestration, inference, K8s) | Some providers have minimal software layer |
| **Contracts** | Infrastructure-grade take-or-pay, 5-year terms | Cloud providers do monthly/hourly spot |

No other entity can bundle all six layers. This is why Brookfield calls Radiant the "first vertically integrated AI infrastructure company."

### The Goldman Sachs of AI infrastructure

Brookfield is positioning as the **financial intermediary** that makes the AI buildout possible. The thesis:

- AI needs **$7T in capital** — tech companies can't fund it all from cash flow
- **$3T** of that is computing infrastructure
- Infrastructure investors have the capital, risk frameworks, and contractual expertise
- Brookfield's edge: it already owns the power generation assets, data center operations, and now GPU orchestration software
- Every nation will need sovereign AI compute — creating a global, recurring demand base

This is analogous to how investment banks financed the railroad buildout, or how infrastructure funds financed the telecom buildout. The AI buildout is the largest infrastructure cycle since the internet, and Brookfield is betting it can be the central financial node.

---

## Ori Industries (acquired)

| Detail | Value |
|--------|-------|
| HQ | UK |
| Business | Cloud computing / GPU orchestration |
| Backers | Saudi Aramco Ventures |
| Acquired | Feb 24, 2026 |
| Terms | Undisclosed |
| Merged into | Radiant |

---

## Brookfield AI context

[[Brookfield]] estimates AI will require **$7 trillion** in total capital investment, with **$3 trillion** for computing infrastructure alone. Radiant is one of the first deployments from the AI infrastructure fund.

Other Brookfield AI bets:
- Up to **$5B in [[Bloom Energy]]** (fuel cells for data centers)
- Data center operators
- Utility stakes benefiting from surging power demand
- [[NVIDIA]] is an equity contributor to the AI fund *and* chip supplier to Radiant

---

## Competitive landscape

| Company | Model | Backing | Customers |
|---------|-------|---------|-----------|
| **Radiant** (Brookfield) | Full-stack AI factories, take-or-pay | $100B program | Sovereigns, enterprises, telcos |
| [[CoreWeave]] | GPU cloud (hyperscaler) | $7.5B+ debt | AI labs, enterprises |
| [[Lambda Labs]] | On-demand GPU cloud | VC-backed | Startups, researchers |
| [[SF Compute]] | Managed clusters, spot | Independent | AI labs |
| [[Vast.ai]] | GPU marketplace (P2P) | Independent | Individuals, small teams |
| Hyperscalers (AWS, Azure, GCP) | Full cloud stack | Balance sheet | Everyone |

Radiant's differentiation: infrastructure-grade contracts (take-or-pay, investment-grade customers) vs. spot/on-demand models of cloud GPU providers. Lower risk, lower return, but massive scale. The hyperscalers are the real competition — Radiant is betting that sovereign customers and enterprises want an alternative to US Big Tech cloud.

---

## Risks

- **GPU obsolescence:** 5-year chip life assumption may be aggressive — if newer architectures (Rubin → next gen) render H100/Blackwell uncompetitive in 3 years, take-or-pay contracts protect revenue but customer relationships sour
- **Sovereign demand may disappoint:** Governments talk big about AI sovereignty but procurement is slow and politically fraught
- **NVIDIA dependency:** Single GPU supplier creates concentration risk. If NVIDIA prioritizes hyperscalers over Radiant during allocation crunches, Radiant can't deliver
- **Competition from hyperscalers:** AWS, Azure, GCP can undercut on price and offer broader services. Sovereign cloud is a niche — it may stay niche
- **Execution complexity:** Bundling power + GPUs + data centers + software across multiple countries is operationally harder than any single layer

---

## Related

- [[Brookfield]] — parent company
- [[NVIDIA]] — GPU supplier, fund investor
- [[GPU rental price index]] — tracks the market Radiant operates in
- [[Tech equity-for-infrastructure deals]] — Brookfield/NVIDIA relationship
- [[Bloom Energy]] — Brookfield AI fund investment ($5B)
- [[Sovereign cloud]] — target market
- [[CoreWeave]] — competitor (GPU cloud)
- [[AI infrastructure financing]] — broader thesis
