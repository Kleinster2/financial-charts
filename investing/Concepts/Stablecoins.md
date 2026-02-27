---
aliases: [stablecoin, stablecoins, stable coins]
tags:
  - concept
  - crypto
  - payments
  - fintech
---

# Stablecoins

Tokens pegged to a reference asset (usually USD or a local currency), designed to minimize crypto volatility. The plumbing layer of crypto — used for payments, remittances, trading settlement, and increasingly as a parallel dollar system in emerging markets.

Global market cap: ~$299B (Feb 2026). [[Tether|USDT]] dominates (~60% share, ~$187B). Stablecoins now account for ~45% of global crypto activity — higher in LatAm (Brazil 60%, Argentina 62%).

**2026 inflection:** Stablecoins are crossing from crypto plumbing into mainstream payments. [[Meta]]'s planned integration (H2 2026) via [[Stripe]]/Bridge would put stablecoin rails under 3.5B daily active users — the largest potential deployment in history.

---

## How they work

| Model | Backing | Examples | Risk |
|-------|---------|----------|------|
| Fiat-backed | 1:1 reserves in cash / T-bills | [[Tether|USDT]], [[Circle|USDC]], [[PayPal|PYUSD]] | Issuer solvency, reserve opacity |
| Yield-bearing | Reserves earn interest, shared with holders | [[BRD]] | Regulatory (may be classified as security) |
| Algorithmic | No full reserves — uses arbitrage mechanics | UST (collapsed May 2022) | Death spiral risk |
| CBDC | Central bank issued | [[Digital Yuan]], Drex (shelved) | State control, privacy concerns |

The yield question is structural: [[Tether]] earns ~$7B/year on reserves and keeps it all. [[Circle]] keeps its yield. [[BRD]] passes yield through. The [[GENIUS Act]] explicitly prohibits US stablecoins from paying yield — creating a regulatory gap that jurisdictions like [[Brazil]] are exploiting.

---

## Reserve economics

Stablecoin issuers are among the largest buyers of US Treasuries globally. [[Tether]] holds more T-bills than many sovereign nations. This creates a symbiotic relationship with US fiscal policy — stablecoins generate sustained demand for short-term government debt.

| Issuer | Estimated T-bill holdings | Reserve transparency |
|--------|--------------------------|---------------------|
| [[Tether]] | ~$90B+ | Quarterly attestation (not full audit) |
| [[Circle]] | ~$30B+ | Monthly attestation, Deloitte audited |
| [[PayPal]] | Undisclosed | Regulated by NYDFS |

---

## Regulatory landscape

| Jurisdiction | Framework | Key feature |
|-------------|-----------|-------------|
| US | [[GENIUS Act]] (July 2025) | 1:1 reserves required. No yield. Monthly attestation. AML/KYC. |
| EU | [[MiCA]] (2024) | Licensing regime. Reserve requirements. |
| [[Brazil]] | BCB resolutions (Feb 2026) | Classified as FX operations. Yield-bearing allowed. |
| Offshore | Minimal | [[Tether]] operates from BVI/El Salvador |

The US-Brazil regulatory divergence on yield is a key structural tension. US framework treats stablecoins as payment instruments (no yield = not a security). Brazil's FX classification enables yield-bearing models like [[BRD]].

---

## Use cases

| Use case | Driver | Example |
|----------|--------|---------|
| Remittances | Cheaper/faster than SWIFT | Brazil: 90% of crypto flows are stablecoin remittances |
| Dollar access | Inflation hedge in EM | Argentina, Turkey, Nigeria |
| Trading settlement | Crypto exchange liquidity | USDT pairs dominate |
| B2B payments | FX risk reduction | $3B/mo in Brazil (2025) |
| DeFi collateral | Programmable money | Lending, yield farming |

---

## Stablecoins as payment rails

Stablecoins are gaining traction as payment infrastructure — not by replacing card networks, but by filling gaps where cards are absent or extractive.

### Cost reference

| Rail | Merchant cost | Settlement | Cross-border |
|------|--------------|------------|--------------|
| [[Visa]]/[[Mastercard]] | 1.5-3.5% interchange | T+2 business days | 3-5% FX markup |
| Stablecoin (USDC on L2) | <$0.01 per transaction | Near-instant | Same cost as domestic |
| ACH/wire | $0.20-$30 per transaction | Same day to T+1 | $15-50 wire fee |
| [[Pix]] (Brazil) | Free (merchant) | Instant | Domestic only |

### Where stablecoins have traction

| Segment | Why | Current scale |
|---------|-----|--------------|
| Cross-border remittances | 80-90% cheaper than SWIFT/Western Union | Brazil: 90% of crypto flows are stablecoin remittances |
| Creator payouts | Instant, no 30-day net terms, no PayPal holds | [[Meta]] targeting this for H2 2026 |
| B2B / invoice settlement | No interchange, programmable | $3B/mo in Brazil (2025) |
| Emerging market dollar access | No bank account needed, inflation hedge | Argentina, Turkey, Nigeria — 534M [[Tether]] MAU |

These segments share a pattern: either cards don't work (unbanked EM users, cross-border micro-transfers) or cards are needlessly expensive (creator payouts, B2B invoicing). Stablecoins aren't competing with [[Visa]] for consumer checkout — they're serving markets cards never reached well.

### Why this isn't a card network threat

The $150B+ annual interchange pool is protected by structural advantages stablecoins can't replicate: consumer credit (cards extend it, stablecoins don't), chargebacks and fraud protection (stablecoins are irrevocable bearer instruments), 4B+ cards in circulation, and decades of merchant integration. The [[Payments Networks]] sector note rates the stablecoin threat as low — correctly, for the core business.

### Adoption pattern

1. **Crypto-native** (2017-2024): Exchange settlement, DeFi collateral
2. **Cross-border** (2023-2025): Remittances, B2B payments, EM dollar access
3. **Platform payments** (2026+): Creator payouts, social commerce ([[Meta]]/[[Stripe]])

Each layer expands USDC/USDT circulation and reserve-based revenue for issuers ([[Circle]], [[Tether]]).

### Agentic commerce

One genuinely novel use case: AI agents executing autonomous transactions. No card number to store, no 3D Secure friction, programmable on-chain logic, sub-cent fees for high-frequency micro-transactions. [[Coinbase]]'s AgentKit and x402 protocol (Feb 2026) target this. No incumbent rail exists for agent-to-agent payments. See [[Agentic AI]].

---

## Key players

### USD-pegged (global)

| Token | Issuer | Market cap | Notes |
|-------|--------|-----------|-------|
| [[Tether|USDT]] | [[Tether]] | ~$187B | Dominant. Offshore. Opaque reserves. |
| [[Circle|USDC]] | [[Circle]] | ~$45B | US-regulated. Circle IPO path. |
| [[PayPal|PYUSD]] | [[PayPal]] | ~$1B | Traditional fintech entry. |

### BRL-pegged (Brazil)

See [[Brazilian real stablecoins]] for the full landscape — 7 active tokens, ~$23M total circulation but $906M H1 2025 trading volume. Fastest-growing local stablecoin ecosystem globally (230x transaction growth since 2021).

---

## Big Tech integration (Feb 2026)

The stablecoin market is shifting from crypto-native to mainstream payments infrastructure. The catalyst: [[Meta]] announced it's testing stablecoin-based payments across Facebook, Instagram, and WhatsApp for H2 2026.

### The value chain

| Layer | Player | Role | Economics |
|-------|--------|------|-----------|
| Distribution | [[Meta]] | 3.5B DAU, creator payouts, ~$100 cross-border transfers | Transaction fees, engagement |
| Infrastructure | [[Stripe]] (Bridge) | Stablecoin orchestration, OCC bank charter (Feb 2026) | Processing fees |
| Token issuer | [[Circle]] (USDC) | Likely primary stablecoin routed through Bridge | Interest on reserves (~$30B+ T-bills) |
| Revenue share | [[Coinbase]] | USDC co-creator, earns share of reserve yield | $364M stablecoin revenue Q4 2025 |
| Regulatory | [[GENIUS Act]] | Federal framework enabling compliant deployment | — |

### Why USDC wins this round

[[Meta]] is not issuing its own token (unlike the failed Libra/Diem project, wound down 2022). It's using third-party infrastructure "at arm's length." [[Stripe]]'s Bridge subsidiary — which received a conditional OCC national trust bank charter in Feb 2026 — is the leading partner. Bridge's compliance-first design favors USDC over alternatives:

- [[Tether|USDT]]: Banned in EU ([[MiCA]]), never audited, offshore — too much regulatory risk for a public company like Meta
- [[PayPal|PYUSD]]: ~$870M market cap, captive to PayPal's 439M accounts, no third-party distribution
- [[MakerDAO|USDS]]: Crypto-collateralized, not suitable for mainstream payments

### Scale implications

| Metric | Value |
|--------|-------|
| Meta DAU | 3.5B |
| Creator economy (annual) | ~$50B across platforms |
| Current USDC market cap | ~$75B |
| Current stablecoin market | ~$299B |

Even a fraction of Meta's transaction volume denominated in USDC would materially expand circulation, increasing both [[Circle]]'s reserve-based interest income and [[Coinbase]]'s revenue share.

### Structural significance

This is the first time a non-crypto company with billions of users is deploying stablecoin rails for everyday payments. Previous adoption was crypto-native (exchange settlement, DeFi, remittances). Meta's integration — if executed — validates stablecoins as mainstream payment infrastructure and creates a template for other Big Tech platforms.

**Regulatory tailwind:** The [[GENIUS Act]] (Jul 2025) created the legal framework. OCC is actively granting bank charters. Congress is friendlier to crypto under Trump. The timing aligns.

**Patrick Collison** ([[Stripe]] CEO) joined [[Meta]]'s board in April 2025, deepening the strategic relationship before the stablecoin announcement.

Source: [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-24/meta-testing-stablecoin-payments-as-digital-currencies-take-off), [CoinDesk](https://www.coindesk.com/business/2026/02/24/mark-zuckerberg-s-meta-is-planning-stablecoin-comeback-in-the-second-half-of-this-year)

---

## Risks

| Risk | Description |
|------|-------------|
| Reserve opacity | [[Tether]] has never had a full audit |
| Regulatory fragmentation | US, EU, Brazil all different frameworks |
| De-peg events | UST collapse (May 2022) destroyed ~$40B |
| Concentration | [[Tether]] = 60% of market |
| Geopolitical | USD stablecoins as [[US-China financial war]] tool |
| Yield competition | If yield-bearing models scale, non-yield stablecoins lose appeal |

---

## Related

### Issuers
- [[Tether]] — USDT (~$187B), dominant but offshore/unaudited
- [[Circle]] — USDC (~$75B), US-regulated, IPO'd Jun 2025
- [[PayPal]] — PYUSD (~$870M), distant third, captive distribution
- [[MakerDAO]] — DAI/USDS (~$3.6B), decentralized/crypto-collateralized

### Infrastructure & distribution
- [[Meta]] — testing stablecoin payments for 3.5B users (H2 2026)
- [[Stripe]] — Bridge subsidiary (acquired $1.1B, Oct 2024), OCC charter, Meta's likely partner
- [[Coinbase]] — USDC co-creator, earns revenue share ($364M Q4 2025)

### Regulatory
- [[GENIUS Act]] — US federal framework (Jul 2025). No yield. 1:1 reserves. Enabled Circle IPO and OCC charters
- [[MiCA]] — EU framework (Dec 2024). 60% EU bank reserves. Forced USDT delisting
- [[Anchorage Digital Bank]] — issues Tether's USAT (US-compliant alternative to USDT)

### Local currency stablecoins
- [[Brazilian real stablecoins]] — 7 active BRL tokens, 230x growth since 2021
- [[BRD]] — yield-bearing BRL stablecoin (regulatory arbitrage vs US no-yield rule)

### Geopolitical
- [[Digital Yuan]] — CBDC competitor
- [[US-China financial war]] — USD stablecoins as dollar hegemony tool

### Sector
- [[Crypto]] — parent ecosystem
- [[Fintech]] — infrastructure overlap
- [[Payments Networks]] — traditional V/MA rails being challenged
- [[Checkout wars]] — stablecoins as alternative to card interchange

---

*Updated 2026-02-26*
