---
aliases: [tokenization hub, asset tokenization, RWA tokenization, blockchain capital markets]
tags: [concept, fintech, market-structure, blockchain, hub]
---

# Tokenization

The migration of financial assets — equities, bonds, funds, real estate, commodities, private credit — onto blockchain infrastructure. Not crypto entering finance; finance absorbing blockchain as plumbing.

This is the hub note. Deep dives are linked below.

---

## Why now

Three forces converged in Q1 2026:

**1. Regulatory unlock.** The Gensler-era SEC treated every token as a potential unregistered security. The Atkins SEC reversed course:
- **March 17, 2026:** SEC and CFTC published a joint 68-page interpretive release establishing a five-category token taxonomy — digital commodities, digital collectibles, digital tools, stablecoins, and digital securities. Named 16 tokens (BTC, ETH, SOL, XRP...) as digital commodities not subject to securities law (confirmed, SEC/CFTC, Federal Register March 23).
- **March 18, 2026:** SEC approved [[Nasdaq]]'s rule change to trade tokenized securities (Release 34-105047).
- **March 25, 2026:** House Financial Services Committee hearing: "Tokenization and the Future of Securities: Modernizing Our Capital Markets." Witnesses: Kenneth Bentsen Jr. (SIFMA CEO) and Summer Mersinger (Blockchain Association CEO).
- **CLARITY Act:** Passed House July 2025 (294-134). Senate Banking Committee markup targeted late April 2026. Would draw statutory boundaries between digital commodities and digital securities for the first time. Sen. Bernie Moreno: if not on Senate floor by May, may not move for years.

**2. Institutional adoption.** [[BlackRock]], [[JPMorgan]], [[Franklin Templeton]], Goldman Sachs, and every major exchange now have tokenization initiatives in production — not pilots.

**3. Market demand.** Global investors want 24/7 access to US equities. The Iran war demonstrated why: Trump's Truth Social post at 7:02 AM on a Monday crashed oil 11% — anyone holding tokenized equities could have traded immediately; traditional equity holders waited for the opening bell.

---

## Taxonomy

Tokenization is not one thing. It is at least five distinct markets converging on the same infrastructure:

| Category | What it is | Key players | Status | Note |
|----------|-----------|-------------|--------|------|
| **Public equities** | NYSE/Nasdaq listing stocks and ETFs as blockchain tokens. Same rights, same CUSIP, 24/7 trading | NYSE/ICE, Nasdaq, Securitize, Kraken, OKX | Nasdaq SEC-approved; NYSE pending | [[Tokenized public securities]] |
| **Private shares** | Derivative tokens giving retail exposure to pre-IPO companies (OpenAI, SpaceX). No actual equity rights | Robinhood, Republic, Ventuals | Active in EU; US regulatory gray area | [[Tokenized private shares]] |
| **Treasuries & money markets** | Tokenized US Treasuries / money market funds on-chain. Yield-bearing, institutional-grade | BlackRock (BUIDL), Franklin Templeton (FOBXX), Ondo (USDY) | $12B+ on-chain; BUIDL at $1.9B | — |
| **Private credit** | Tokenized loans, trade receivables, real estate debt | Maple, Centrifuge, Goldfinch, Figure | Growing but fragmented | — |
| **Deposits & settlement** | Bank deposit tokens, tokenized collateral, intraday repo | JPMorgan (Kinexys/JPM Coin), BNY, Citi | $1.5T+ notional processed (Kinexys); $300B+ tokenized repo | — |

**Stablecoins** (USDC, USDT, PYUSD) are the connective tissue — settlement currency for all of the above. Stablecoin market cap ~$267B+ and growing. The CLARITY Act's stablecoin yield provisions are the current legislative battleground.

---

## Market size

| Metric | Value | Source |
|--------|-------|--------|
| Tokenized RWA on-chain value | $26.48B (Mar 23, 2026) | rwa.xyz |
| Represented asset value (incl. platform-locked) | $387.35B | rwa.xyz |
| Year-over-year growth | 260-300%+ | Multiple |
| BlackRock BUIDL (largest single product) | $1.9B AUM | Securitize |
| JPMorgan Kinexys notional processed | $1.5T+ cumulative | JPMorgan |
| JPMorgan tokenized repo | $300B+ cumulative | JPMorgan |
| Stablecoin market cap | ~$267B | CoinDesk |
| Total addressable market (global equities) | $126T | — |

Larry Fink (BlackRock CEO): "Every asset — every stock, every bond, every fund, every asset — can be tokenized. If we do, it will revolutionize investing."

---

## The exchange race

The two largest US exchanges are building competing tokenization architectures. This is the most immediate investable story.

| | [[Nasdaq]] | NYSE / [[Intercontinental Exchange\|ICE]] |
|---|---|---|
| **Architecture** | Tokenize within existing DTC infrastructure | Build separate blockchain venue from scratch |
| **SEC status** | ✅ Approved (March 18, 2026) | ⏳ Pending (target late 2026) |
| **Scope** | Russell 1000 + major ETFs | All NYSE-listed equities and ETFs |
| **Distribution** | [[Kraken]] (crypto-native global) | [[OKX]] ($25B valuation, ICE investor) |
| **Settlement** | DTC pilot, T+0 optional | Instant on-chain, stablecoin-funded |
| **Transfer agent** | — | [[Securitize]] (MOU March 24) |
| **Collateral** | — | BNY + Citi tokenized deposits at clearinghouses |
| **Hours** | Moving toward 23-hour trading | 24/7 from launch |

**Deep dive:** [[Tokenized public securities]]

---

## Key actors

### Infrastructure / picks-and-shovels

| Actor | Role | Ticker | Notes |
|-------|------|--------|-------|
| **[[Securitize]]** | Transfer agent, issuance, broker-dealer. NYSE's partner. BlackRock-backed | CEPT → **SECZ** | SPAC at $1.25B; 841% revenue growth; $4.6B tokenized AUM; going public on Nasdaq |
| **[[JPMorgan]]** | Kinexys (ex-Onyx): tokenized deposits, JPM Coin, tokenized repo. $1.5T notional, $300B repo | **JPM** | Institutional infrastructure; permissioned Ethereum → now also Base (public chain) |
| **[[BNY Mellon\|BNY]]** | Tokenized deposits at ICE clearinghouses; custody | **BK** | World's largest custodian bank; critical for institutional adoption |
| **[[Citigroup\|Citi]]** | Tokenized deposits at ICE clearinghouses | **C** | Working with ICE on 24/7 margin/settlement |
| **DTCC** | Clearing/settlement for Nasdaq tokenized pilot | Private | Legacy clearinghouse adapting; existential risk if on-chain settlement displaces it |

### Exchanges

| Actor | Role | Ticker |
|-------|------|--------|
| **[[Intercontinental Exchange\|ICE]]** | NYSE parent; building Digital Trading Platform; OKX investment | **ICE** |
| **[[Nasdaq]]** | First SEC-approved tokenized trading; CLARITY Act beneficiary | **NDAQ** |
| **[[Kraken]]** | Global distribution for Nasdaq tokenized stocks | Private (IPO filed) |
| **OKX** | Global distribution for NYSE tokenized stocks | Private ($25B val) |
| **[[Coinbase]]** | Incumbent US crypto exchange; potential distribution layer | **COIN** |

### Asset managers

| Actor | Product | Ticker |
|-------|---------|--------|
| **[[BlackRock]]** | BUIDL ($1.9B tokenized treasuries); Securitize backer; "every asset can be tokenized" | **BLK** |
| **[[Franklin Templeton]]** | FOBXX (OnChain US Government Money Fund) — one of the first tokenized mutual funds | **BEN** |
| **Goldman Sachs** | Tokenized bond issuance; GS DAP platform | **GS** |
| **[[Apollo Global Management\|Apollo]]** | Tokenized private credit through Securitize | **APO** |
| **Hamilton Lane** | Tokenized PE fund access through Securitize | **HLNE** |
| **KKR** | Tokenized fund shares through Securitize | **KKR** |

### DeFi-native

| Actor | Product | Token/Ticker |
|-------|---------|-------------|
| **Ondo Finance** | Tokenized treasuries (USDY), tokenized stocks (250+ assets) | ONDO |
| **Maple** | Tokenized private credit | MPL |
| **Centrifuge** | Tokenized real-world credit | CFG |

---

## Regulatory timeline

| Date | Event | Significance |
|------|-------|-------------|
| Jul 2025 | CLARITY Act passes House (294-134) | First statutory digital asset framework |
| Sep 2025 | Nasdaq files SEC application for tokenized trading | Exchange-level commitment |
| Oct 2025 | Securitize announces SPAC at $1.25B | Pure-play goes public |
| Dec 2025 | Nasdaq reveals 23-hour trading plans | Market hours expanding regardless |
| Jan 2026 | NYSE/ICE announces Digital Trading Platform | Race formally starts |
| Jan 2026 | Senate Agriculture advances CLARITY Act portion | Senate moving |
| Mar 5 | ICE invests in OKX at $25B valuation | Exchange-crypto convergence |
| **Mar 17** | **SEC-CFTC joint crypto taxonomy** (68 pages, 5 categories, 16 named commodities) | Regulatory clarity — the unlock |
| **Mar 18** | **SEC approves Nasdaq tokenized securities rule** | First US exchange approved |
| Mar 24 | NYSE taps Securitize as transfer agent (MOU) | Infrastructure partner locked |
| **Mar 25** | **House Financial Services hearing on tokenization** | Congressional engagement |
| Apr 2026 | Senate Banking markup of CLARITY Act (targeted) | Statutory framework |
| May 2026 | Moreno deadline — if not on floor, may die | Legislative window closing |
| Late 2026 | NYSE Digital Trading Platform launch target | Second exchange live |

---

## Investment framework

Three tiers:

### Tier 1 — Picks and shovels (highest conviction)

Whoever wins the exchange race, someone needs to mint, track, settle, and custody tokenized securities. These companies benefit regardless of which architecture prevails.

| Play | Thesis | Ticker |
|------|--------|--------|
| Securitize | Only public pure-play tokenization infrastructure; NYSE + BlackRock + Apollo backing | CEPT → SECZ |
| JPMorgan | Kinexys already processing $2B/day; tokenized repo at scale; institutional trust | JPM |
| BNY Mellon | World's largest custodian; tokenized deposits for ICE clearinghouses | BK |

### Tier 2 — Platform plays

The exchanges building the venues. Tokenization is additive revenue on top of existing franchise.

| Play | Thesis | Ticker |
|------|--------|--------|
| ICE | NYSE + OKX distribution + new blockchain venue; more ambitious architecture | ICE |
| Nasdaq | First-mover regulatory approval; conservative but de-risked | NDAQ |
| Coinbase | Incumbent crypto infrastructure; potential distribution partner for either exchange | COIN |

### Tier 3 — Asset plays

Companies whose tokenized products could capture significant AUM if the infrastructure succeeds.

| Play | Thesis | Ticker |
|------|--------|--------|
| BlackRock | BUIDL already dominant; will likely launch tokenized ETFs | BLK |
| Franklin Templeton | Early mover in tokenized funds (FOBXX) | BEN |
| Ondo Finance | DeFi-native tokenized treasury/equity platform; 250+ assets | ONDO |

---

## What could go wrong

| Risk | Detail |
|------|--------|
| **Legislative failure** | CLARITY Act dies in Senate → regulatory clarity reverts to case-by-case enforcement. Moreno's May deadline is real. |
| **24/7 liquidity** | Continuous markets require continuous market-making. Overnight/weekend liquidity in tokenized equities may be razor-thin, creating flash crash risk |
| **Settlement fragmentation** | If NYSE and Nasdaq use different blockchain architectures, fungibility breaks — a tokenized Apple share on one venue may not transfer seamlessly to the other |
| **Stablecoin risk** | The entire settlement layer depends on USDC/USDT maintaining their peg. A stablecoin crisis (Tether audit, Circle bank run) would freeze tokenized markets |
| **Regulatory reversal** | Atkins SEC is pro-tokenization; a future administration could reverse course |
| **Incumbent resistance** | DTCC, traditional custodians, existing market makers all face displacement risk — they will lobby and litigate |
| **Market manipulation** | 24/7 thin-liquidity windows + presidential Truth Social posts = manipulation surface. The Iran war oil trading pattern previews this |

---

## The big picture

The $126 trillion US equity market is being re-platformed onto blockchain infrastructure. This is not a fintech trend — it is a market structure transformation comparable to the shift from floor trading to electronic markets in the 1990s-2000s.

The analogy: when NYSE went electronic, the floor didn't disappear overnight. Hybrid trading coexisted for years. The same will happen here — tokenized and traditional shares will trade side by side on the same order books, at the same prices, with the same rights. The blockchain layer is invisible to most investors.

But the structural consequences compound: instant settlement frees trillions in collateral currently locked in T+1 clearing. 24/7 markets eliminate the overnight gap that costs billions in hedging. Dollar-denominated fractional orders open US markets to global retail. Stablecoin funding decouples capital movement from banking hours.

None of this requires the investor to understand blockchain. That is the point.

---

## Related

### Spoke notes
- [[Tokenized public securities]] — NYSE/Nasdaq exchange race (deep dive)
- [[Tokenized private shares]] — derivative/crypto approach (no shareholder rights)

### Actors
- [[Intercontinental Exchange]] — NYSE parent
- [[Nasdaq]] — first SEC-approved tokenized trading
- [[BlackRock]] — BUIDL fund, Securitize backer, institutional anchor
- [[JPMorgan]] — Kinexys, JPM Coin, tokenized repo
- [[Coinbase]] — crypto infrastructure incumbent
- [[Franklin Templeton]] — FOBXX tokenized fund

### Concepts
- [[Crypto]] — underlying technology
- [[Stablecoins]] — settlement layer (if note exists)
- [[Private markets]] — tokenization expands access
- [[Market structure]] — broader context

---

## Sources

- FinTech Weekly: "Congress Is Holding Its Most Important Tokenization Hearing on Wednesday" (March 23, 2026)
- SEC/CFTC: Joint Interpretive Release on crypto asset taxonomy (March 17, 2026; Federal Register March 23)
- SEC: Release No. 34-105047 — Nasdaq tokenized securities rule approval (March 18, 2026)
- Forbes: "SEC And CFTC Deliver Landmark Crypto Clarity" (March 17, 2026)
- Reuters: "NYSE teams up with Securitize" (March 24, 2026)
- Reuters: "Nasdaq receives SEC nod for tokenized securities" (March 18, 2026)
- ICE press release: Digital Trading Platform (January 19, 2026)
- ICE press release: OKX investment (March 5, 2026)
- CoinDesk: "Securitize reports 841% revenue growth" (January 29, 2026)
- JPMorgan: Kinexys platform documentation
- rwa.xyz: RWA market data (March 23, 2026)
- Larry Fink annual letter / public statements on tokenization

---

*Created 2026-03-25. Hub note — spoke notes linked above for deep dives.*
