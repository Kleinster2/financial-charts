---
aliases:
  - Token economics
  - Token design
  - Token mechanics
tags:
  - concept
  - crypto
  - economics
  - token
---

#concept #crypto #economics

# Tokenomics

The set of design choices that determine how a crypto token's supply, distribution, and value-capture work. The core variables are supply schedule (cap, emissions curve, burn mechanisms), distribution (initial allocations, vesting, airdrops), and demand drivers (utility, staking yields, governance rights, fee accrual). Tokenomics is to crypto protocols what cap tables and capital structure are to equity-financed companies — the mechanism that decides who captures value as the network grows.

---

## Core dimensions

| Dimension | Question | Examples |
|-----------|----------|----------|
| Supply cap | Hard cap, soft cap, or uncapped? | [[Bitcoin]] 21M hard, [[Bittensor]] 21M hard, [[Morpheus]] 42M hard, [[Ethereum]] uncapped |
| Emissions curve | How fast new tokens enter circulation? | Bitcoin halving every ~4y; Bittensor symmetric halving model; Morpheus decreasing curve over ~16y |
| Distribution | Who got the initial supply? | Airdrop ([[Venice AI]] VVV), team + investors (most), fair launch ([[Bitcoin]]) |
| Vesting | Are insider tokens locked? | Standard 1y cliff + 4y linear for VC tokens; airdrop usually liquid |
| Burn mechanism | Are tokens removed from supply? | [[Venice AI]] revenue-funded buyback/burn, [[Akash Network]] $0.85 burned per $1 spent |
| Staking | Do holders earn yield? | [[Bittensor]] subnet staking, [[Morpheus]] Capital Provider stETH staking |
| Utility | What does the token actually do? | Pay for inference, govern protocol, secure network, mint credit ([[Venice AI]] DIEM) |

---

## Two archetypes in decentralized AI

The [[Decentralized AI landscape]] has converged on two clearly different tokenomics philosophies:

**Emissions-only designs** — token is minted on a fixed schedule, distributed to network contributors (miners, stakers, validators). Token value is purely a function of demand for utility minus emissions inflation. Most pre-2025 decentralized AI tokens follow this pattern. Examples: most [[Bittensor]] subnet alpha tokens, early [[Render Network]] (RNDR), [[ASI Alliance]]. Failure mode: if utility growth doesn't outrun emissions, token price decays.

**Revenue-funded buyback-and-burn** — protocol generates real product revenue (subscriptions, fees, access), and uses some portion of that revenue to buy tokens off the market and burn them. Creates structural buying pressure tied to product success. Examples: [[Venice AI]] (monthly burn started Nov 2025, 30K-50K VVV/month), [[Akash Network]] (burns $0.85 per $1 spent), [[Ridges AI]] (alpha-token buybacks proposed). 2026 is the test cycle for whether this design outperforms emissions-only.

---

## Common pathologies

- **Emissions cliffs** — pre-determined unlock dates where insider/early-investor tokens vest in bulk, producing predictable sell pressure. Often the proximate cause of token price drawdowns.
- **Utility-price decoupling** — protocol can have growing usage but falling token price if utility doesn't translate to token demand (e.g., users pay in [[Stablecoin|USDC]] not the native token).
- **Reflexive bubbles** — token price rises → more developer attention → more product → more usage → more price (the 2024-2025 agent-layer bubble). When the loop reverses, valuations crash 55-85% (most decentralized AI tokens by April 2026).
- **Speculation premium with no revenue** — token capitalized at $1B+ on a pre-revenue protocol because the "design" is bullish. [[Nous Research]]'s Paradigm-led $1B token valuation is the cleanest example — defensible only if Psyche actually produces a working distributed-training market.

---

## Why this matters for investors

In equity terms, tokenomics is the rough equivalent of a company's capital structure plus dividend policy plus share-buyback policy plus governance rules — all expressed in the protocol's smart contracts and treated as immutable (or immutable-by-default). A poorly designed cap table or unfavorable vesting schedule can damage equity returns even when the business does well; the same is true at the token level, just more transparent.

For decentralized AI specifically, the central question is whether revenue-backed designs win over emissions-only through a full cycle — see open question #1 in [[Decentralized AI landscape]].

---

## Related

- [[Decentralized AI landscape]] — context where this matters most
- [[Bittensor]] — programmable per-subnet alpha-token tokenomics via [[Dynamic TAO|dTAO]]
- [[Morpheus]] — 42M hard cap, deliberately Bitcoin-shaped
- [[Venice AI]] — leading example of revenue-funded buyback/burn
- [[Akash Network]] — $0.85 burned per $1 spent
- [[Bitcoin]] — original hard-cap + halving design
- [[Bonding curve]] — token-pricing primitive used in agent launchpads
- [[AI agent tokens]] — per-agent token primitive from [[Virtuals Protocol]]
