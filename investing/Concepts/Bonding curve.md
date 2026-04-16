---
aliases:
  - Bonding curves
  - Token bonding curve
tags:
  - concept
  - crypto
  - economics
  - market-structure
---

#concept #crypto #economics

# Bonding curve

A smart-contract pricing mechanism that algorithmically prices a token as a continuous function of its circulating supply. Buyers send collateral (usually [[Ethereum|ETH]], [[Solana|SOL]], or a stablecoin) into the contract; the contract mints new tokens at a price set by the curve and adjusts the price upward as more tokens are minted. Sellers receive collateral back at the prevailing curve price, which decreases as supply decreases. The curve provides instant on-chain liquidity for tokens that would otherwise have no market.

---

## How it works

| Step | Action |
|------|--------|
| 1 | Contract deployed with a pricing formula (linear, quadratic, exponential, sigmoid) |
| 2 | Buyer sends collateral; contract mints tokens at the current curve price |
| 3 | Each mint moves price up the curve — early buyers get better prices |
| 4 | Seller burns tokens; contract returns collateral at the (now lower) curve price |
| 5 | At a threshold (e.g., $X collateral raised), curve graduates to a regular AMM pool ([[Uniswap]] / Raydium) and trading moves there |

This is the same primitive that powers Pump.fun for memecoins on [[Solana]]. The 2024-2025 generalization to AI agents was the [[Virtuals Protocol]] innovation: every agent gets its own bonding-curve token at launch.

---

## Where it shows up in the decentralized AI landscape

| Protocol | Use of bonding curve |
|----------|----------------------|
| [[Virtuals Protocol]] | Each launched [[AI agent tokens|AI agent]] gets its own bonding-curve token; graduates to AMM after raising target collateral |
| [[Bittensor]] [[Dynamic TAO|dTAO]] subnets | Each subnet has an internal AMM that functions like a bonding curve for the subnet's alpha token |
| Pump.fun (memecoins) | Original mass-market deployment on Solana |

---

## Why it matters

Bonding curves transform token launches from a marketing problem ("how do we price our IDO?") into a market-structure problem ("what's the slope and shape of the curve?"). They give early supporters mathematically guaranteed price advantage, create instant liquidity without an order book, and make rug-pulls structurally harder (collateral is locked in the contract, so creators can't simply take buyer funds).

The downside is reflexivity: bonding curves amplify both upward and downward moves, because every buy mints new supply and every sell burns supply. Combined with social-momentum dynamics, this produces the rapid pump-and-collapse pattern visible across Pump.fun memes and most [[Virtuals Protocol]] agent tokens. The 2024-2025 [[AIXBT]] arc — peaked at $500M+ FDV, currently $80M-150M — is the canonical bonding-curve agent-token reflexive cycle.

---

## Related

- [[Virtuals Protocol]] — primary AI-agent application
- [[AI agent tokens]] — the broader primitive bonding curves enable
- [[Dynamic TAO]] — Bittensor's per-subnet alpha-token AMM (functionally similar)
- [[Tokenomics]] — parent topic
- [[Decentralized AI landscape]] — context
- [[Solana]] — host chain for Pump.fun and the original bonding-curve memecoin wave
- [[Base]] — host chain for Virtuals agent bonding curves
