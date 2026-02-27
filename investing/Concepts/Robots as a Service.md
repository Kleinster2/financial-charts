---
aliases: [RaaS, Robot as a Service, Robotics as a Service]
---
#concept #robotics #business-model

**Robots as a Service** — Subscription or usage-based model where robotics companies lease robots to customers instead of selling outright. Shifts automation from capex to opex. The SaaS playbook applied to physical hardware — recurring revenue for vendors, lower adoption barrier for buyers.

---

## Why it matters for investors

Traditional industrial robotics is a capex sale: buy the robot, install it, maintain it. RaaS inverts this, creating recurring revenue streams and faster customer adoption. For robotics companies, it means lower upfront revenue but higher lifetime value and stickier relationships. For customers, it means warehouse automation without $2-4M upfront investment for a fleet.

The model is especially important for humanoid robots, where unit economics are unproven and customers won't commit to purchasing $100K+ machines with uncertain ROI. RaaS lets both sides de-risk.

---

## How it works

| Element | Detail |
|---------|--------|
| Hardware | Vendor owns the robot; customer leases |
| Pricing | Fixed monthly fee, per-task fee, or hybrid |
| Maintenance | Included — vendor handles repairs, updates |
| Software | Continuous updates, fleet management |
| Scaling | Add/remove robots with demand (seasonal flex) |
| Contract | Typically 12-36 months |

---

## Pricing models

| Model | How it works | Best for |
|-------|-------------|----------|
| Fixed subscription | Monthly/annual fee per robot | Steady-state operations |
| Time-based lease | Rent for a set period | Seasonal peaks, trials |
| Task-based (pay-per-pick) | Charged per task completed | Variable-volume warehouses |
| Hybrid | Base fee + usage overage | Most common in practice |

Typical range for warehouse AMRs: $1,000-5,000/robot/month. A fleet of 20 AMRs runs $50,000-80,000/month on a 24-month contract. Cobots for manufacturing: $500-2,500/month. Delivery robots: as low as $4/hour ([[Relay Robotics]]).

---

## Capex vs. RaaS comparison

| Factor | Traditional purchase | RaaS |
|--------|---------------------|------|
| Upfront cost | $2-4M for 50-100 robot fleet | Near zero |
| Budget approval | Capital expenditure (harder) | Operating expenditure (easier) |
| Time to deploy | Months (integration) | Days to weeks |
| Scaling | Buy more units | Add to subscription |
| Maintenance | Customer responsibility | Vendor-included |
| Obsolescence risk | Customer bears | Vendor bears |
| Total cost (5yr) | Lower if utilization high | Higher, but predictable |

The trade-off mirrors cloud vs. on-prem: RaaS costs more over the life of the asset but reduces risk and accelerates adoption. For customers with uncertain demand or evolving technology, RaaS is strictly better.

---

## Key RaaS providers

| Company | Robot type | Sector | Notes |
|---------|-----------|--------|-------|
| [[Reflex Robotics]] | Wheeled humanoid | Warehouse/manufacturing | ~$10K hardware + monthly sub; [[GXO Logistics]] pilot |
| [[Figure AI]] | Bipedal humanoid | Manufacturing/logistics | RaaS model announced; BMW partnership |
| [[Agility Robotics]] | Bipedal humanoid (Digit) | Warehouse | [[Amazon]] testing |
| Locus Robotics | AMR | Fulfillment/healthcare | Leading warehouse AMR provider |
| 6 River Systems | AMR (Chuck) | Fulfillment | Acquired by [[Shopify]], then sold to Ocado |
| Fetch Robotics | AMR | Warehouse | Acquired by [[Zebra Technologies]] |
| Cobalt Robotics | Security/patrol | Enterprise | Hourly pricing |
| inVia Robotics | AMR | Warehouse/e-commerce | Pick-and-place focus |
| [[Relay Robotics]] | Delivery | Hotels/healthcare | As low as $4/hour |
| [[Bear Robotics]] | Service (Servi) | Restaurants/hospitality | Food delivery robots |

---

## Market size

| Source | 2025 estimate | Projection | CAGR |
|--------|--------------|------------|------|
| Precedence Research | $2.1B | $12.4B by 2035 | 18% |
| Business Research Co. | — | $56.9B by 2029 | 10.6% |
| ABI Research | — | 1.3M deployments by 2026, $34B revenue | — |

Estimates vary widely depending on scope (some include software-only "service robotics," others are hardware-subscription only). The core trend is consistent: double-digit growth driven by labor shortages and falling robot costs.

---

## Why RaaS matters for humanoids specifically

Humanoid robots face a chicken-and-egg problem: customers won't buy expensive unproven hardware, and vendors can't prove ROI without deployments. RaaS solves this by:

1. Eliminating the purchase decision — customers trial with minimal commitment
2. Generating deployment data — every hour of operation feeds back into training (see [[Teleoperation as data collection]])
3. Allowing iterative improvement — vendor pushes software updates, replaces hardware as models improve
4. Building switching costs — once workflows depend on the robots, customers don't leave

For [[Reflex Robotics]] specifically, RaaS is doubly important: the teleoperation model means human operators are part of the service, not just the hardware. The monthly fee covers both the robot and the humans controlling it — a true managed service, not just a lease.

---

## Analogies

| RaaS parallel | SaaS parallel |
|---------------|---------------|
| Robot hardware | Server/infrastructure |
| Monthly subscription | SaaS license fee |
| Fleet management software | Cloud management tools |
| Vendor-managed maintenance | Managed hosting |
| Per-task pricing | Usage-based billing (AWS) |
| Seasonal scaling | Auto-scaling compute |

---

*Created 2026-02-26*

---

## Related

- [[Reflex Robotics]] — wheeled humanoid, RaaS model with teleoperation
- [[Figure AI]] — bipedal humanoid, announced RaaS
- [[Agility Robotics]] — Digit, RaaS with [[Amazon]]
- [[GXO Logistics]] — largest pure-play 3PL, evaluating multiple RaaS providers
- [[Teleoperation as data collection]] — RaaS deployments generate training data
- [[Robotics]] — sector overview
