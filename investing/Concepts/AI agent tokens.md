---
aliases:
  - Agent tokens
  - Agent-as-token
  - Tokenized AI agents
tags:
  - concept
  - ai
  - crypto
  - agents
  - tokenomics
---

#concept #ai #crypto #agents

# AI agent tokens

The primitive of issuing a unique cryptocurrency token to represent a single autonomous AI agent — its identity, its ownership, its governance, and its share of revenue or output. Distinct from [[AI agents]] (the broader category of autonomous software agents) and from [[Tokenomics]] (the general topic of token design): AI agent tokens are the specific "one agent, one token" pattern pioneered by [[Virtuals Protocol]] in late 2024 and rapidly cloned across the 2024-2025 cycle.

---

## Mechanism

Each agent gets its own [[Bonding curve|bonding-curve]] token at launch on an L2 (typically [[Base]] or [[Solana]]). Holders can:

- Treat the token as economic exposure to the agent's success (price moves with usage / mindshare / revenue)
- Govern the agent via on-chain proposals (model upgrades, fee changes, treasury allocation)
- Receive distributions from the agent's revenue (when the agent generates fees or content)
- Stake the token to receive priority access or rewards from the agent's activities

The agent itself uses its token treasury to pay for inference, storage, marketing, and any other operational costs. This produces a closed economic loop: the agent works, generates revenue, distributes value to token holders, and continues operating from treasury.

---

## Canonical examples

| Agent | Launchpad | Function | Peak FDV |
|-------|-----------|----------|----------|
| [[AIXBT]] | [[Virtuals Protocol]] | Crypto market sentiment + signal | $500M+ |
| Various Virtuals agents | [[Virtuals Protocol]] | Chatbots, traders, content | Tens to hundreds of $M each |
| ai16z (now [[ElizaOS]]) | DAO model | DAO-managed investment fund agent | $2.5B+ |

[[Virtuals Protocol]] is the launchpad — the issuance and bonding-curve infrastructure. [[ElizaOS]] is the framework — the developer toolkit for building agents. Together they form the agent-platform layer of the [[Decentralized AI landscape]].

---

## What it tries to solve

The pre-token agent landscape had two deficiencies. First, no clean way for an agent to own assets, pay for compute, or compensate contributors without going through a corporate intermediary. Second, no clean way for users / fans / customers to share in an agent's success. Tokens solve both by giving the agent a treasury and giving supporters tradeable economic exposure.

---

## What broke

Most 2024-2025 agent tokens crashed 55-85% from peak. The reflexive bonding-curve dynamics that produced rapid early appreciation also produced rapid declines once mindshare faded, and most launched agents had no actual revenue to back the token. Agents that produced consistent value ([[AIXBT]]'s sentiment signal, a small number of Virtuals tokens with usage) survived at lower valuations; the long tail effectively went to zero.

The 2026 rebuild emphasizes revenue-producing agents over speculative ones — agents that charge for actual services and use that revenue to fund buybacks. Whether this produces a category of durable value or another reflexive cycle is the open question for the agent-platform layer.

---

## Limitations vs traditional equity

| Dimension | AI agent token | Equity |
|-----------|----------------|--------|
| Governance | On-chain votes (low participation typical) | Board + shareholder votes |
| Revenue claim | Whatever protocol writes into the contract | Dividend + buyback + residual claim |
| Liquidity | Continuous on-chain | Listed (public) or restricted (private) |
| Legal status | Unclear in most jurisdictions | Well-defined |
| Disclosure | On-chain transparency, off-chain opacity | Mandatory periodic reporting (public) |
| Exit | Sell into curve / DEX | M&A, IPO, secondary |

The legal and disclosure deltas are the binding constraints on whether agent tokens can ever attract institutional capital at scale.

---

## Related

- [[Virtuals Protocol]] — primary launchpad
- [[ElizaOS]] — primary framework
- [[AIXBT]] — case study
- [[AI agents]] — parent category (broader)
- [[Bonding curve]] — pricing primitive
- [[Tokenomics]] — parent topic
- [[Decentralized AI landscape]] — agent-platform layer
- [[Base]] / [[Solana]] — primary host chains
