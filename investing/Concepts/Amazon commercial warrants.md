---
aliases: [Amazon warrant playbook, purchase-contingent warrants, commercial arrangement warrants]
---
#concept #amazon #corporatefinance #dealstructure

**Amazon commercial warrants** — recurring [[Amazon]] deal structure using equity warrants tied to commercial commitments. Amazon deploys this on both sides of its business: as buyer (locking in suppliers) and as seller (locking in AWS customers).

*This note covers Amazon-specific deals. For the broader pattern (including AMD's equity-for-volume program), see [[Commercial warrants]].*

---

## How it works

Amazon ties equity to volume commitments. Warrants vest in tranches as purchase or spend thresholds are hit. If volume doesn't materialize, warrants don't vest — the equity "discount" disappears.

| Direction | Amazon's role | Equity flows | Commitment flows |
|-----------|---------------|-------------|-----------------|
| Amazon as buyer | Customer | Warrants → Amazon | Volume guarantee → supplier |
| Amazon as seller | Platform (AWS) | Cash/equity → partner | Cloud spend → AWS |

---

## Known deals

### Amazon as buyer (gets warrants)

| Partner | Year | Structure | Tied to |
|---------|------|-----------|---------|
| [[Rivian]] | 2019 | Warrants for ~20% of Rivian | 100K electric delivery van order |
| [[Stellantis]] | 2021 | Warrants | Ram ProMaster EV van purchases |
| [[Plug Power]] | 2017 | Warrants | Green hydrogen for fulfillment centers |
| [[STMicro]] | 2026 | 24.8M shares at $28.38, 7yr | Semiconductor supply for AWS infrastructure |

### Amazon as seller (invests equity)

| Partner | Year | Structure | Tied to |
|---------|------|-----------|---------|
| [[Anthropic]] | 2023-24 | Up to $4B equity investment | AWS as primary cloud provider |

---

## What the direction reveals

The equity always flows away from the party with fewer options. The warrant direction is a signal of relative leverage:

- **Supplier gives Amazon warrants** → Amazon is the scarce customer. Supplier needs the demand more than Amazon needs the supply. (STMicro in cyclical trough, Rivian pre-revenue, Plug Power pre-scale)
- **Amazon invests equity in partner** → Partner is the scarce workload. Amazon needs to lock in the customer more than the partner needs AWS specifically. (Anthropic could run on Azure/GCP)

A company at peak margins and full order books is unlikely to hand out warrants. The structure tends to appear when the supplier is capital-hungry or in a weak demand environment.

---

## Risk profile

### For the warrant issuer (supplier)

- **Roadmap distortion** — R&D and capacity allocated to Amazon-specific products
- **Customer concentration** — earnings tied to Amazon's capex cycles
- **Equity dilution at the wrong price** — if stock recovers, Amazon exercises at trough-level strike
- **Capacity crowding** — Amazon allocation may displace higher-margin customers

### For Amazon

- **Sunk cost lock-in** — incentivized to keep buying from underperforming supplier to vest warrants rather than switching
- **Underwater warrants** — if stock falls below strike, the discount mechanism fails and it's just a standard supply deal
- **Write-down risk** — [[Rivian]] warrants peaked at billions in paper value, then collapsed with the stock

### The Rivian cautionary tale

Amazon got warrants, Rivian built early production around the van order, stock peaked ~$170 then crashed to ~$10. Amazon wrote down billions. Rivian was locked into fulfilling a massive van contract at thin-to-negative margins while its consumer business starved for capacity. The alignment mechanism became a trap for both sides.

---

## Accounting treatment

Warrant fair value is typically recorded as a reduction to cost of revenue (for Amazon) or as a contra-revenue / selling expense (for the supplier). This means:
- Amazon's reported margins on the purchased goods/services appear lower than cash cost
- Supplier's reported revenue from Amazon is net of warrant amortization
- Vesting schedule creates non-cash volatility in both income statements

---

## Related

- [[Commercial warrants]] — broader concept (Amazon + AMD + general pattern)
- [[Amazon]] — architect of this playbook
- [[AWS]] — cloud side of the warrant strategy
- [[STMicro AWS deal]] — 2026 semiconductor warrant deal
- [[Rivian]] — cautionary example (van order + warrants)
- [[Anthropic]] — reverse direction (Amazon invests, Anthropic commits to AWS)
- [[Plug Power]] — hydrogen supply warrant deal
- [[Stellantis]] — EV delivery van warrant deal
