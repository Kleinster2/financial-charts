---
aliases: [equity-for-volume deals, purchase-contingent warrants, commercial arrangement warrants, commercial warrants]
---
#concept #corporatefinance #dealstructure

**Commercial warrants** — equity instruments tied to commercial commitments between companies. Warrants vest in tranches as volume, spend, or deployment thresholds are hit. If commitments aren't met, warrants expire worthless — the equity "discount" disappears.

A recurring pattern in industries where one side of a deal has significantly more leverage than the other. The **direction of equity flow reveals who needs the deal more.**

---

## Core mechanic

| Element | How it works |
|---------|--------------|
| **Trigger** | One party needs to lock in the other's commitment |
| **Structure** | Warrants (or equity) granted in tranches |
| **Vesting** | Tied to purchase volume, deployment milestones, or spend thresholds |
| **Alignment** | Both sides profit only if the commercial relationship succeeds |
| **Expiry** | Unmet milestones → warrants die → no dilution |

---

## What the direction reveals

The equity always flows **away from the party with fewer options**. The warrant direction is a leverage signal:

| Direction | What it means | Examples |
|-----------|---------------|---------|
| **Supplier grants warrants to buyer** | Buyer is the scarce customer. Supplier needs demand more than buyer needs supply. | [[AMD]] → [[Meta]], [[AMD]] → [[OpenAI]], [[STMicro]] → [[Amazon]], [[Rivian]] → [[Amazon]] |
| **Buyer invests equity in supplier** | Supplier is the scarce workload/product. Buyer needs to lock in the partner. | [[Amazon]] → [[Anthropic]], [[Microsoft]] → [[OpenAI]] |

A company at peak margins and full order books doesn't hand out warrants. The structure appears when the grantor is capital-hungry, in a weak demand environment, or trying to buy credibility in a market dominated by someone else.

---

## The Amazon playbook

[[Amazon]] pioneered commercial warrants at scale, deploying them on both sides of its business. See [[Amazon commercial warrants]] for the full case study.

**Amazon as buyer (receives warrants):** [[Rivian]] (100K van order, ~20% equity), [[Stellantis]] (EV vans), [[Plug Power]] (hydrogen), [[STMicro]] (semiconductors for AWS, 24.8M shares at $28.38).

**Amazon as seller (grants equity):** [[Anthropic]] ($4B investment tied to AWS as primary cloud).

**Cautionary tale:** The [[Rivian]] deal showed how the alignment mechanism becomes a trap when the supplier's business deteriorates. Rivian built production around Amazon's van order, stock crashed from ~$170 to ~$10, Amazon wrote down billions, and Rivian was locked into fulfilling a massive contract at negative margins while its consumer business starved.

---

## The AMD playbook (2025-2026)

[[AMD]] is running a standardized equity-for-volume program to break [[NVIDIA]]'s ~90% AI GPU monopoly. AMD is the **supplier granting warrants to buyers** — the mirror image of Amazon's supplier deals.

| Deal | Date | Warrants | Vesting |
|------|------|----------|---------|
| [[OpenAI]] | Oct 2025 | 160M AMD shares (~10%) | Deployment + stock price thresholds |
| [[Meta]] | Feb 24, 2026 | 160M AMD shares (~10%) | 1GW → 6GW deployment milestones + stock price thresholds |

**Total potential dilution:** 320M shares (~20% of AMD) if both deals fully vest.

### Why AMD is paying with equity

AMD's problem isn't hardware — the [[Helios]] rack is competitive with NVIDIA's NVL72. The problem is the [[CUDA moat]]: no hyperscaler will bet billions on AMD GPUs without confidence the software ecosystem works at scale. AMD can't buy software credibility with marketing — it needs **deployed volume** that forces the ecosystem to mature.

The warrants are the cost of bootstrapping a duopoly. By giving Meta and OpenAI skin in AMD's success, Lisa Su ensures:
1. **Committed volume** — hyperscalers won't quietly deprioritize AMD hardware
2. **Software co-development** — Meta/OpenAI will invest engineering to make AMD work (they're now equity holders)
3. **Market signal** — other customers see Meta + OpenAI validation and follow
4. **Self-selecting dilution** — warrants only vest if AMD delivers, meaning revenue would justify the equity cost

### The dilution math

If AMD fully delivers on both deals, ~20% dilution sounds painful. But consider: 6GW to Meta alone could represent **tens of billions in revenue** over the deal's lifetime. AMD's entire data center segment did $5.4B in Q4 2025. The warrants are cheap if they buy AMD a permanent seat at the table.

If AMD *doesn't* deliver, warrants expire worthless — no harm done.

### Key risk: Rivian parallel

The Rivian cautionary tale applies here too. If AMD's MI450/Helios underperforms, Meta and OpenAI could deprioritize deployments — but the committed volume agreements may force AMD to allocate capacity to deals generating thin margins. The alignment mechanism only works when the supplier can actually execute.

---

## Risk profile

### For the warrant issuer (grantor)

- **Equity dilution at the wrong price** — if stock recovers, warrants exercise at trough-level strike
- **Roadmap distortion** — R&D and capacity warped toward one customer's needs
- **Customer concentration** — earnings tied to one buyer's capex cycles
- **Capacity crowding** — committed allocation may displace higher-margin customers

### For the warrant recipient

- **Sunk cost lock-in** — incentivized to keep buying from underperforming supplier to vest warrants rather than switching
- **Underwater warrants** — if stock falls below strike, the alignment mechanism fails
- **Write-down risk** — paper gains can reverse dramatically (Rivian: billions in write-downs)

---

## Accounting treatment

Warrant fair value is typically recorded as:
- **Recipient:** reduction to cost of revenue (goods/services appear cheaper)
- **Grantor:** contra-revenue or selling expense (reported revenue is net of warrant amortization)
- Vesting schedule creates **non-cash volatility** in both income statements

---

## Where to watch for this pattern

Commercial warrants tend to appear at **inflection points** — when an industry is shifting and one side needs to lock in the other before the window closes:

- **AI compute** — AMD breaking NVIDIA's monopoly (2025-26)
- **EV transition** — Amazon locking in delivery fleet supply (2019-21)
- **Cloud** — hyperscalers competing for AI workloads (Amazon → Anthropic)
- **Semiconductors** — capacity constrained fabs (STMicro → Amazon)

Expect more as AI capex scales — any GPU/chip company trying to compete with NVIDIA will likely deploy similar structures.

---

## Related

- [[Tech equity-for-infrastructure deals]] — why this pattern is uniquely powerful in tech (switching costs, ecosystem lock-in, reflexivity)
- [[Amazon commercial warrants]] — deepest case study, both directions
- [[AMD]] — equity-for-volume to break CUDA moat
- [[Meta-AMD 6GW deal]] — Feb 24, 2026
- [[OpenAI]] — AMD's first warrant deal (Oct 2025)
- [[CUDA moat]] — the competitive barrier AMD's warrants are designed to overcome
- [[Rivian]] — cautionary tale of warrant-linked commercial relationship
- [[STMicro AWS deal]] — semiconductor warrant deal
- [[Anthropic]] — reverse direction (Amazon invests equity)
