---
aliases:
  - Decentralized AI
  - Crypto AI
  - Tokenized AI
  - Decentralized AI protocols
tags:
  - concept
  - ai
  - crypto
  - decentralized
  - depin
  - landscape
---

# Decentralized AI landscape

The category of crypto protocols using token incentives to bootstrap AI infrastructure, inference, agents, or training data. Grew from ~$5B aggregate market cap in 2024 to $22-35B by Q1 2026, spanning roughly 900 projects. Tracked here as the coherent alternative to the centralized frontier-lab stack ([[OpenAI]], [[Anthropic]], [[Google]]).

Central claim of the category: token incentives let decentralized networks subsidize AI compute and agent development below the cost structure of centralized providers. The thesis splits the stack into four layers — compute, data, [[AI agents|agents]], and applications — each with its own incumbents, tokenomics designs, and failure modes.

---

## Synthesis

Four investable layers, each dominated by a different type of protocol. Compute-layer networks ([[Render Network]], [[Akash Network]], [[io.net]]) discount enterprise GPU pricing 60-80% by aggregating idle hardware, and compete on price and reliability against [[AWS]] and [[CoreWeave]]. Application layer is where consumer products live — [[Venice AI]] for privacy-first chat (~$417M token market cap, 1.3M users), and [[Ridges AI]] for autonomous coding agents (~$45M). Agent-platform layer ([[Virtuals Protocol]], [[ElizaOS]], [[AIXBT]]) commoditizes agent deployment and on-chain monetization — collectively $3-8B in peak market cap. Data layer ([[Grass]], [[Vana]], Ocean Protocol via [[ASI Alliance]]) compensates individuals for contributing bandwidth or personal data to AI training. The [[Bittensor]] protocol spans all four layers through its programmable subnet design.

Constraint: most tokens in the category trade 55-85% below their 2024-2025 all-time highs. Category valuation is real but volatile, and many projects are speculation vehicles with no durable revenue. Counter-example: [[Venice AI]] has begun revenue-funded buybacks and [[Ridges AI]] has posted benchmark results against SWE-Bench — evidence that some decentralized-AI projects are now generating cash flows rather than just emitting tokens. One-line: decentralized AI is moving from pure speculation to a real but narrow commercial category, and the 2026 test is whether revenue-backed token models (Venice, Ridges, Akash) outperform emissions-only designs through a full cycle.

---

## Four-layer stack

### 1. Compute layer (decentralized GPU / inference)

Networks that aggregate physical GPU capacity from miners, data centers, or idle consumer hardware.

| Protocol | Token | Chain | Focus | April 2026 market cap |
|----------|-------|-------|-------|-----------------------|
| [[Bittensor]] | TAO | Subtensor | Multi-market AI protocol | ~$3.4B |
| [[Render Network]] | RENDER | [[Solana]] | GPU rendering + AI video | Multi-B peak |
| [[Akash Network]] | AKT | [[Cosmos]] | Decentralized cloud, reverse auction | ~$500M-1B |
| [[io.net]] | IO | [[Solana]] | 300K+ GPU aggregation | Mid-hundreds M |
| [[Morpheus]] | MOR | [[Arbitrum]] | Inference routing (backs Venice) | Low-hundreds M |
| [[Aethir]] | ATH | [[Arbitrum]] | Enterprise GPU cloud | Mid-hundreds M |
| [[Nous Research]] (Psyche) | — (unlaunched) | [[Solana]] | Distributed *training* coordination | $1B token valuation (Paradigm Apr 2025) |
| Gensyn | — | — | Distributed ML training (pre-token) | Private |
| Prime Intellect | — | — | Decentralized training | Private |

Note: most compute-layer protocols target *inference* (serving trained models). [[Nous Research]]'s Psyche, Gensyn, and Prime Intellect target the harder problem of *distributed training* — coordinating gradient updates across untrusted GPU contributors. Training is the larger spend item for AI labs but technically much harder to decentralize.

Compute-layer claim: 60-80% cost reduction vs [[AWS]] on-demand GPU pricing. Primary risk: reliability / SLAs at enterprise scale.

### 2. Application layer (consumer-facing AI apps)

Branded products end-users interact with directly, routed over decentralized infrastructure.

| Protocol | Token | Chain | Focus |
|----------|-------|-------|-------|
| [[Venice AI]] | VVV | [[Base]] | Privacy-first chat + image (~1.3M users) |
| [[Ridges AI]] | SN62 alpha | [[Bittensor]] | Autonomous coding agents |
| [[Hermes Agent]] ([[Nous Research]]) | — (pre-token) | — | Persistent self-improving autonomous agent (36K GitHub stars) |

Consumer apps are where revenue flows are most visible. Venice's monthly buy-and-burn is funded by subscription/access revenue; Ridges' v1 product sells at ~$12/mo. Hermes Agent is open-source and pre-token — competes with [[OpenClaw]] as a general-purpose persistent agent.

### 3. Agent platform layer (agent launchpads, frameworks, meta-protocols)

Infrastructure for creating, launching, and monetizing autonomous AI agents with their own tokens.

| Protocol | Token | Chain | Focus | Peak market cap |
|----------|-------|-------|-------|-----------------|
| [[Virtuals Protocol]] | VIRTUAL | [[Base]] | Agent launchpad, tokenized agents | $5B+ peak |
| [[ElizaOS]] (ai16z) | AI16Z / ELIZAOS | [[Solana]] | Agent framework + DAO-managed fund | $2.5B+ peak |
| [[AIXBT]] | [[AIXBT]] | [[Base]] | Trading-signal agent | $80M-500M |

Agent-layer thesis: each agent is its own economic entity that issues a token representing its capabilities/services. Most of the 2024-2025 agent-layer market cap has evaporated; the category is rebuilding in 2026 on narrower, revenue-producing designs.

### 4. Data layer (user-owned data for AI training)

Networks that compensate individuals for contributing bandwidth or personal data, then monetize data access to AI labs.

| Protocol | Token | Chain | Focus | April 2026 |
|----------|-------|-------|-------|------------|
| [[Grass]] | GRASS | [[Solana]] | Bandwidth-for-data (8.5M MAU) | ~$247M |
| [[Vana]] | VANA | Vana L1 | User-owned data DAOs | Mid-hundreds M |
| [[ASI Alliance]] | FET | Multi-chain | [[Fetch.ai]] + SingularityNET + Ocean merger | ~$518M |
| Nillion | NIL | Nillion L1 | Privacy-preserving compute on data | Mid-hundreds M |

Data-layer claim: AI training data should compensate the humans who produced it. Primary customer: AI labs needing high-quality training data that doesn't violate IP / privacy norms.

---

## Categorical similarities and differences

| Dimension | Centralized AI (OpenAI, Anthropic) | Decentralized AI (this category) |
|-----------|-------------------------------------|----------------------------------|
| Capital formation | Equity (venture rounds) | Token emissions + (increasingly) revenue buybacks |
| Compute sourcing | Own data centers / [[AWS]] / [[NVIDIA]] contracts | Aggregated GPU marketplaces |
| Model development | In-house R&D at single lab | Crowdsourced (Bittensor) or use open-weight models (Venice) |
| Moat | Frontier model quality | Cost structure + privacy + composability |
| Customer | Enterprise + consumer | Enterprise-light, crypto-native consumer, long-tail developer |

---

## What drives token performance in the category

- Actual product revenue feeding buybacks/burns ([[Venice AI]] model)
- Benchmark milestones ([[Ridges AI]] → [[SWE-Bench]])
- Integration / partnership with major apps ([[Morpheus]] ↔ [[Venice AI]])
- ETF / institutional vehicle approval ([[Grayscale]] GTAO filing for [[Bittensor]])
- AI-category beta (whole sector moves with broad AI sentiment)
- Emissions cliffs / staking unlocks (negative pressure)

Tokens without any of the first four usually give back most gains over a full cycle.

---

## Open questions for 2026-2027

1. Can revenue-backed designs (Venice, Ridges, Akash) outperform emission-only protocols once the full cycle plays out?
2. Does the [[Grayscale]] GTAO ETP actually launch, and does it open a second wave of altcoin-AI ETP filings?
3. Does [[Bittensor]]'s "programmable subnet" architecture beat narrower single-market protocols ([[Morpheus]]), or does the long tail of low-quality subnets dilute TAO's value capture?
4. Do enterprise buyers accept decentralized inference for production workloads, or does decentralized AI stay retail / crypto-native?

---

## Related

- [[Bittensor]] — spans compute + agent layers via programmable subnets
- [[Morpheus]] — narrow-focus inference network (powers Venice)
- [[Venice AI]] — flagship consumer app in category
- [[Ridges AI]] — flagship coding-agent subnet
- [[Render Network]] / [[Akash Network]] / [[io.net]] / [[Aethir]] — compute layer (inference)
- [[Nous Research]] / [[Hermes Agent]] — distributed training + open-weight models + agent harness (multi-layer)
- [[Virtuals Protocol]] / [[ElizaOS]] / [[AIXBT]] — agent layer
- [[Grass]] / [[Vana]] / [[ASI Alliance]] — data layer
- [[DePIN]] — parent category
- [[Crypto-to-AI pivot]] — adjacent but distinct thesis (Bitcoin miners going AI)
- [[Grayscale]] — GTAO ETP filer, opens institutional access
