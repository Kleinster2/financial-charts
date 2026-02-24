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

- [[Brazilian real stablecoins]] — BRL-pegged ecosystem
- [[Tether]] — dominant issuer (USDT)
- [[Circle]] — USDC issuer, IPO candidate
- [[PayPal]] — PYUSD
- [[GENIUS Act]] — US regulatory framework
- [[MiCA]] — EU regulatory framework
- [[Crypto]] — parent sector
- [[Digital Yuan]] — CBDC competitor
- [[Fintech]] — infrastructure overlap
- [[Payments Networks]] — traditional rails being disrupted

---

*Created 2026-02-23*
