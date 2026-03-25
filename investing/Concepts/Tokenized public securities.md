---
aliases: [tokenized equities, tokenized stocks, exchange tokenization, 24/7 stock trading, blockchain equities]
tags: [concept, fintech, market-structure, blockchain, exchanges]
---

# Tokenized public securities

The migration of publicly traded equities and ETFs onto blockchain infrastructure — enabling 24/7 trading, instant settlement, fractional (dollar-denominated) orders, and stablecoin-based funding. Unlike [[Tokenized private shares]], these are **fungible with traditional shares**: same ticker, same CUSIP, same dividends and voting rights, same order book.

This is not crypto entering finance. This is the $126 trillion equity market absorbing blockchain as plumbing.

---

## The exchange race

Two competing architectures are racing to define the standard:

### Nasdaq — regulatory first-mover

- **SEC approved** Nasdaq's tokenized securities rule change on **March 18, 2026** (Release No. 34-105047)
- Initial scope: Russell 1000 stocks + major ETFs (S&P 500, Nasdaq 100 trackers)
- Built on a **DTC pilot** — the Depository Trust Company handles clearing/settlement of tokenized trades alongside traditional book-entry
- Tokenized shares trade on the **same order book** at the **same price** as traditional shares — identical rights, same ticker, same CUSIP
- Architecture: **layering tokenization onto existing clearing infrastructure** — evolutionary, not revolutionary
- Distribution partner: [[Kraken]] — crypto exchange distributing tokenized stocks globally
- Nasdaq also developing a framework for companies to **natively issue** blockchain-based shares

### NYSE / ICE — building from scratch

- **Announced January 19, 2026** — NYSE developing a separate Digital Trading Platform for tokenized equities and ETFs
- Architecture: **new blockchain-based venue built from scratch** — combines NYSE's Pillar matching engine with blockchain post-trade systems
- Features: 24/7 operations, instant settlement, dollar-denominated orders, stablecoin funding
- **Securitize** tapped as first digital transfer agent (MOU signed March 24, 2026) — will mint blockchain-native securities for corporate and ETF issuers
- Working with [[BNY Mellon|BNY]] and [[Citigroup|Citi]] on tokenized deposits at ICE clearinghouses — enabling margin calls and money transfers outside banking hours
- **OKX partnership** (March 5, 2026): ICE invested in crypto exchange OKX at $25B valuation. OKX will provide global distribution of NYSE tokenized equities; ICE will license OKX spot prices for regulated crypto futures
- Still requires **SEC and FINRA approval** — target: late 2026
- NYSE Group President Lynn Martin: "As we explore how tokenization can enhance capital markets, it is critical that new infrastructure is developed in a way that preserves the trust, transparency, and protections investors expect."

### Architectural difference

| | Nasdaq | NYSE |
|---|---|---|
| Approach | Tokenize within existing infrastructure | Build separate blockchain venue |
| Clearing | DTC pilot | New on-chain settlement |
| Settlement | Same timelines, blockchain optional | Instant, designed for 24/7 |
| Distribution | Kraken (crypto-native) | OKX (crypto-native) + broker-dealers |
| Funding | Traditional | Stablecoin-based |
| Status | SEC approved (Mar 18) | Seeking approval (target late 2026) |
| Risk | Incremental — less disruptive, less transformative | Higher — more ambitious, more regulatory hurdles |

Nasdaq is the tortoise (regulatory approval in hand, conservative architecture). NYSE is the hare (bolder design, not yet approved). Both partnered with crypto exchanges for global retail distribution — an acknowledgment that the demand is coming from outside the US.

---

## Key actors

### Securitize

The central infrastructure player in the NYSE ecosystem. [[BlackRock]]-backed and [[Ark Invest]]-backed.

| Metric | Detail |
|--------|--------|
| AUM | $4.6B tokenized (as of late 2025) |
| Revenue | 841% growth; $110M projected 2026 |
| IPO path | SPAC merger with Cantor Equity Partners II (CEPT). Post-merger ticker: **SECZ** on Nasdaq |
| Valuation | $1.25B (SPAC deal); $225M PIPE |
| Key product | Transfer agent for BlackRock's [[BUIDL]] fund ($1.9B — largest tokenized treasury fund) |
| Role | SEC-registered transfer agent, broker-dealer arm, issuance + trading infrastructure |
| Partners | BlackRock, Apollo, Hamilton Lane, KKR, VanEck |

Securitize is the picks-and-shovels play: regardless of which exchange wins, someone needs to mint, track, and settle tokenized securities. They're positioned on both sides — building NYSE's platform while potentially listing on Nasdaq.

### BlackRock

[[BlackRock]]'s BUIDL fund (BlackRock USD Institutional Digital Liquidity Fund) — $1.9B AUM, largest tokenized treasury product globally. Launched on Ethereum through Securitize partnership. BlackRock CEO [[Larry Fink]] has repeatedly called tokenization "the next generation for markets."

### Ondo Finance

Crypto-native tokenized securities platform. 250+ assets including BlackRock's IBIT, Galaxy Digital. Integrated with Bitget and Binance. Market cap of tokenized securities hit ~$27B (March 2026). Represents the DeFi-native approach competing with exchange-based tokenization.

---

## The broader RWA market

Tokenized real-world assets (RWAs) have surpassed **$21B in TVL** in early 2026, following 300%+ annual growth. This includes:

- **Treasuries/money markets**: BUIDL ($1.9B), Franklin Templeton's FOBXX, Ondo's USDY
- **Private credit**: Maple, Centrifuge, Goldfinch
- **Equities**: The NYSE/Nasdaq push — potentially the largest category if successful
- **Real estate**: Tokenized property funds

The SEC and CFTC have shifted from adversarial to accommodating under the Atkins SEC. The regulatory unlock is the key catalyst.

---

## What this changes

### For investors

- **24/7 trading** — no market hours, no settlement delay. Weekend and overnight events (like Trump's Truth Social posts during the Iran war) can be traded immediately instead of waiting for Monday's open
- **Fractional ownership** — dollar-denominated orders instead of whole shares. Buy $50 of Berkshire Hathaway
- **Instant settlement** — T+0 instead of T+1 (or T+2 for international). Eliminates settlement risk and frees collateral
- **Global access** — crypto exchange distribution (Kraken, OKX) gives non-US retail investors direct access to US equities without local brokerage accounts
- **Stablecoin funding** — USDC/USDT as settlement currency, enabling 24/7 capital movement

### For market structure

- **Clearing disruption** — if settlement is instant and on-chain, what role remains for DTCC? Nasdaq's approach preserves DTC; NYSE's potentially displaces it
- **Exchange competition** — exchanges competing on infrastructure quality, not just listings. Blockchain architecture becomes a differentiator
- **Market maker economics** — 24/7 markets require continuous liquidity provision. Current market makers are built around market-hours trading; overnight/weekend liquidity is a new problem
- **Regulatory arbitrage** — tokenized shares tradeable on crypto exchanges globally may create jurisdiction conflicts. A US-listed stock trading on Kraken in Singapore at 3 AM raises surveillance questions

### What it doesn't change

- **Fundamentals** — a tokenized share of Apple is still a share of Apple. Same earnings, same dividends, same governance
- **SEC jurisdiction** — tokenized or not, these are securities under US law
- **Market manipulation risk** — arguably increases with 24/7 thin-liquidity trading windows
- **Index inclusion** — unclear whether tokenized shares count toward float, index weighting, etc.

---

## Investment implications

| Play | Thesis | Ticker/entity |
|------|--------|---------------|
| Securitize | Picks-and-shovels for exchange tokenization | CEPT (pre-merger) → SECZ |
| ICE | Owner of NYSE; building the platform + OKX partnership | [[Intercontinental Exchange\|ICE]] |
| Nasdaq | First-mover regulatory approval | [[Nasdaq\|NDAQ]] |
| Kraken | Global distribution for Nasdaq tokenized stocks | Private (IPO filed) |
| OKX | Global distribution for NYSE tokenized stocks | Private |
| Coinbase | Incumbent US crypto exchange; potential distribution | [[Coinbase\|COIN]] |
| BlackRock | Largest asset manager; BUIDL fund; Securitize backer | [[BlackRock\|BLK]] |
| Ondo Finance | DeFi-native competitor | ONDO (crypto token) |

The exchange-level play (ICE vs NDAQ) is more about which tokenization architecture wins. The pure-play is Securitize — the only public(ish) company whose entire business is tokenization infrastructure.

---

## Timeline

| Date | Event |
|------|-------|
| Sep 2025 | Nasdaq files SEC application for tokenized securities trading |
| Oct 2025 | Securitize announces SPAC merger with CEPT at $1.25B valuation |
| Dec 2025 | Nasdaq reveals plans for 23-hour daily trading |
| Jan 19, 2026 | NYSE/ICE announces Digital Trading Platform for tokenized 24/7 trading |
| Jan 28, 2026 | Securitize/CEPT file S-4 registration |
| Jan 29, 2026 | Securitize reports 841% revenue growth |
| Mar 5, 2026 | ICE invests in OKX at $25B valuation; strategic partnership |
| Mar 18, 2026 | **SEC approves Nasdaq tokenized securities rule** (Release 34-105047) |
| Mar 24, 2026 | NYSE taps Securitize as first digital transfer agent (MOU) |
| Late 2026 | NYSE Digital Trading Platform launch target (pending SEC/FINRA approval) |

---

## Related

- [[Tokenized private shares]] — derivative/crypto approach (no shareholder rights)
- [[Intercontinental Exchange]] — NYSE parent, building blockchain venue
- [[Nasdaq]] — first SEC-approved tokenized trading
- [[BlackRock]] — BUIDL fund, Securitize backer
- [[Crypto]] — underlying technology
- [[Private markets]] — broader context
- [[Market structure]] — if it exists; otherwise general concept

---

## Sources

- ICE press release: "The New York Stock Exchange Develops Tokenized Securities Platform" (January 19, 2026)
- ICE press release: "ICE Makes Investment in OKX, Establishing Strategic Relationship" (March 5, 2026)
- Reuters: "NYSE teams up with Securitize to develop tokenized securities platform" (March 24, 2026)
- Reuters: "Nasdaq receives SEC nod for trading in tokenized securities" (March 18, 2026)
- SEC: Release No. 34-105047 — Nasdaq tokenized securities rule approval (March 18, 2026)
- CoinDesk: "NYSE to introduce 24/7 blockchain stock trading platform this year" (January 19, 2026)
- CoinDesk: "SEC approves Nasdaq's move to allow tokenized securities trading" (March 18, 2026)
- CoinDesk: "NYSE taps Securitize to build its tokenized stock platform" (March 24, 2026)
- Unchained: "NYSE Taps Securitize to Build Its 24/7 Tokenized Stock Trading Platform" (March 24, 2026)
- CoinDesk: "Tokenization firm Securitize reports 841% revenue growth" (January 29, 2026)
- PR Newswire: Securitize SPAC announcement (October 28, 2025)

---

*Created 2026-03-25.*
