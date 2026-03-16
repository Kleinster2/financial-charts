---
aliases: [event contracts, event contract markets, prediction market]
---
#concept #fintech #derivatives

**Prediction markets** — Platforms where participants trade contracts on future event outcomes. Prices aggregate dispersed information into probability estimates. Regulatory status contested: [[CFTC]] classifies as derivatives; states argue they're unlicensed gambling.

---

## Why it works

Prediction markets operationalize [[Friedrich Hayek]]'s insight that prices aggregate dispersed knowledge. Each trader brings private information — the market synthesizes it into a probability.

| Mechanism | Description |
|-----------|-------------|
| **Skin in the game** | Financial stakes force honest probability assessment |
| **Continuous updating** | Prices adjust as new information arrives |
| **Diverse perspectives** | Aggregates specialists, insiders, generalists |
| **No authority required** | Decentralized — no single expert needed |

The Iowa Electronic Markets (1988) demonstrated prediction markets outperform polls for elections. Corporate applications followed — [[Google]] used internal markets for product launch forecasting.

---

## Market structure

| Contract type | Example | Payout |
|---------------|---------|--------|
| **Binary** | "Will Fed cut rates in March?" | $1 if yes, $0 if no |
| **Scalar** | "What will unemployment be?" | Linear payout based on outcome |
| **Conditional** | "GDP growth if Trump wins" | Isolates causal effects |

Prices = implied probabilities. A contract trading at $0.65 implies 65% probability.

---

## US regulatory landscape

### Federal: CFTC jurisdiction

The [[CFTC]] regulates prediction markets as **event contracts** under the Commodity Exchange Act. [[Kalshi]] became the first federally licensed exchange in 2020, designated as a DCM (Designated Contract Market).

**Jan 2026 shift:** Chairman [[Michael Selig]] announced formal event contracts rulemaking:
- Withdrew Biden-era proposed ban on sports contracts
- Directed staff to draft new rules (February 2026)
- Language may preempt state laws
- Philosophy: "minimum effective dose of regulation"

### State: Gambling classification

States argue prediction markets on sports = unlicensed sports betting, regardless of federal classification.

| State | Action | Status |
|-------|--------|--------|
| **Massachusetts** | Preliminary injunction (Jan 20, 2026) | First court to block Kalshi sports contracts |
| **Nevada** | Injunction dissolved (Nov 2025) | State can enforce gambling laws |
| **Ohio** | Cease-and-desist (Apr 2025) | Citing MA ruling |
| **New Jersey** | Cease-and-desist | Coordinating with Ohio |

**Core question:** Does a CFTC license provide nationwide permission, or can states use police powers to classify as gambling?

Likely headed to Supreme Court given circuit split.

---

## Key platforms

| Platform | Status | Valuation | Notes |
|----------|--------|-----------|-------|
| [[Kalshi]] | CFTC-regulated (US) | $11B | First federally licensed; sports = 90% of volume |
| [[Polymarket]] | Offshore (crypto-based) | $9B | ICE investment; settled 2022 CFTC probe; US users technically prohibited |
| [[Crypto.com]] | CFTC-regulated (CDNA) | — | [[Truth Social]] partnership; sports focus |
| Robinhood | Sports contracts | — | Facing Ohio cease-and-desist |

---

## Economics

**Why prediction markets matter for investors:**

| Application | Example |
|-------------|---------|
| **Policy uncertainty** | Fed rate probabilities affect asset allocation |
| **Election hedging** | Tariff risk, regulatory change |
| **Earnings signals** | Some markets track company events |
| **Macro forecasting** | GDP, inflation expectations |

Prediction markets often lead traditional indicators — they incorporate information faster than polls or surveys.

---

## Historical context

- **1503:** Papal succession betting (documented)
- **1880s-1940s:** Wall Street election betting markets
- **1988:** Iowa Electronic Markets (academic)
- **2003:** DARPA Policy Analysis Market cancelled after political backlash
- **2014:** Augur (blockchain-based)
- **2020:** [[Polymarket]] founded; [[Kalshi]] gets CFTC license
- **2024:** 2024 election — Polymarket/Kalshi surge; Trump win validated markets vs polls

---

## 2024-2025: Breakout moment

The 2024 US election was prediction markets' public validation:

- [[Polymarket]] showed Trump leading when polls showed toss-up
- Final Polymarket: Trump 60-65% vs polling aggregates ~50%
- Trump won — markets were right, polls were wrong
- Polymarket volume: $3.7B on election alone

**Result:** Mainstream legitimacy, massive capital inflows, regulatory attention.

---

## 2025-2026: Ultra-short-term crypto contracts

Both [[Kalshi]] and [[Polymarket]] began offering 15-minute "up-down" bets on [[Bitcoin]], [[Ethereum]], [[Solana]], and [[XRP]] in late 2025 — binary contracts on whether a token's price will be higher or lower in 15 minutes. [[Polymarket]] subsequently added 5-minute contracts on the same tokens.

**Scale:** ~$70M combined daily volume across both platforms by March 2026. These contracts now represent more than half of all crypto trading on both platforms.

![[kalshi-15min-crypto-volume-ft-mar26.png]]
*Kalshi: 15-minute crypto markets approaching half of all crypto volume. Source: Kalshi, FT Analysis (Mar 13, 2026)*

![[polymarket-short-term-crypto-volume-ft-mar26.png]]
*Polymarket: short-term crypto volume grew rapidly despite January 2026 fee introduction. Source: Polymarket, FT Analysis (Mar 13, 2026)*

**Retail demand persists despite headwinds.** Volume continues to grow even with BTC down >40% from its October 2025 peak and despite [[Polymarket]]'s introduction of fees on 15-minute crypto in January 2026 (later expanded to all crypto contracts, up to 1.56% per trade).

**HFT arbitrage:** [[Keyrock]] researcher Amir Hajian: latency arbitrage was "rampant" on 15-minute markets before [[Polymarket]] added fees. Sophisticated traders exploit tiny time lags between Polymarket price signals and [[Binance]]. Five-minute markets still show "microstructure inefficiencies" that large trading firms target.

**Tradfi convergence:** [[Nasdaq]] filed with regulators (week of Mar 10, 2026) to introduce binary "yes-no" options on whether the [[Nasdaq 100]] trades at, above, or below a pre-determined price. Initial contracts would expire over a few days, with potential expansion to zero-day (24-hour) alternatives. Amanda Fischer ([[Better Markets]], former SEC chief of staff): "Everyone is in a race to become the next super app to rule them all. Trad-fi is copying crypto, and vice versa."

**AI-assisted trading:** Retail traders are using LLMs to inform ultra-short bets. Max Wojcik, an engineer, described using three AI chatbots (Claude, Gemini, ChatGPT) to scrape price data, "converse" among themselves, and generate odds — claims to have doubled his money over two months.

**Margin trading:** [[Kalshi]] is seeking US regulatory approval to allow margin trading on its platform, though no current plans for leveraged 15-minute crypto contracts specifically. Source: FT (Mar 13, 2026).

See [[Ultra-short-term contracts]] for the full analytical framework — the three-party extraction structure (platforms, HFT, retail), the [[0DTE options]] parallel, and why these instruments have no informational or hedging utility at their actual durations.

---

## Risks and critiques

| Risk | Description |
|------|-------------|
| **Manipulation** | Wealthy actors can move thin markets |
| **Liquidity** | Obscure contracts have wide spreads |
| **Regulatory** | Federal vs state conflict unresolved |
| **Self-fulfilling** | Can markets influence outcomes they predict? |

---

## Brazil

[[Brazil]] is emerging as a major prediction markets jurisdiction (2026). Multiple entrants:

| Platform | Approach |
|----------|----------|
| [[B3]] | [[CVM]]-approved event contract derivatives (Feb 2026). Professional investors only (>R$10M) |
| [[Kalshi]] | Launched March 9, 2026 via [[XP]] International/Clear Corretora. Offshore accounts, sidesteps domestic regulation |
| [[VoxFi]] | Domestic startup (beta). Founded by [[Fernando Carvalho]] (ex-[[QR Capital]], first LatAm crypto ETF) |
| Previas | Structuring under CVM Resolution 88 (collective investment contracts) |
| Futuriza | B2C/B2B model, announced March 2026 launch |
| [[Polymarket]] | Already live (crypto-based). 217 active Brazil markets |

Regulatory jurisdiction unresolved: SPA (sports betting regulator under [[Lei das Bets]]) vs [[CVM]] (securities/derivatives). The CVM's B3 approval suggests it may claim prediction markets as derivatives, not gambling.

---

## Related

- [[Kalshi]] — first CFTC-regulated prediction market
- [[Polymarket]] — largest crypto-based platform
- [[VoxFi]] — Brazilian prediction market startup
- [[Crypto.com]] — sports event contracts via CDNA
- [[CFTC]] — federal regulator
- [[Michael Selig]] — CFTC chairman driving rulemaking
- [[Crypto]] — blockchain infrastructure for Polymarket
- [[Ultra-short-term contracts]] — 5/15-minute crypto bets, 0DTE parallel, three-party extraction framework
- [[Derivatives]] — prediction markets are a form of derivative
- [[Brazil]] — emerging prediction markets jurisdiction (2026)
- [[Lei das Bets]] — Brazilian sports betting law, regulatory overlap
