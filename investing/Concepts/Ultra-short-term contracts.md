---
aliases: [ultra-short contracts, 0DTE, zero-day options, 0DTE options, five-minute bets, 15-minute bets]
---
#concept #derivatives #market-structure

**Ultra-short-term contracts** — A structural shift across derivatives markets toward instruments with expiries measured in minutes to hours rather than days or months. Spans [[0DTE options]] on equity indices, 5/15-minute crypto binary bets on [[prediction markets]], and [[Nasdaq]]'s proposed binary options. The common thread: shortening the feedback loop until trading feels like a game.

---

## Synthesis

The convergence is the story. Three separate markets — listed options, crypto prediction markets, and now traditional exchange binary options — independently arrived at the same product design: ultra-short, binary or near-binary, instant-resolution contracts targeting retail flow. This isn't coincidence. It reflects a structural demand for lottery-ticket payoffs with instant gratification, enabled by mobile-first trading platforms and permissive regulators.

The instruments have no informational or hedging utility at their actual durations. Nobody hedges a portfolio with a 5-minute BTC binary or a 0DTE SPX put bought at 3:45 PM. The framing — [[CFTC]] chairman [[Michael Selig]] claiming event contracts allow investors to "hedge risk and manage portfolios" — is regulatory theater. The participants know what this is. [[Keyrock]] researcher Amir Hajian: "Let's just call it what it is: pure speculation."

What makes the trend analytically interesting is the three-party extraction structure that repeats across every venue:

| Participant | Incentive |
|---|---|
| Platforms/exchanges | Volume → fees. Shorter duration = more contracts per day = more turnover per dollar of capital |
| Sophisticated traders (HFT, dealers) | Arbitrage retail flow. Latency gaps, gamma hedging, microstructure inefficiencies are all monetizable |
| Retail | Binary outcome, instant resolution, small stakes. Dopamine cycle identical to slot machines and scratch-off tickets |

Each party's incentive reinforces the others. Retail provides flow. Platforms provide venue and earn fees. Sophisticated firms extract edge from both. The system is self-reinforcing until either regulation intervenes or retail capital exhausts.

---

## The instruments

### 0DTE equity options

Options expiring the same day they're traded. [[CBOE]] introduced daily SPX expirations in 2022 — previously only available on Mondays, Wednesdays, and Fridays. The result was explosive:

- 0DTE share of SPX options volume: ~5% (early 2022) → ~50% (2024)
- Notional value: trillions in daily notional turnover
- Retail-driven: platforms like Robinhood and Schwab made access frictionless

Concerns: dealer gamma hedging of large 0DTE positions can amplify intraday moves. When a wall of 0DTE puts expires near the money, dealer hedging (selling futures to stay delta-neutral) can accelerate selloffs. JPMorgan and others have flagged this as a structural fragility.

### Prediction market crypto bets

Both [[Kalshi]] and [[Polymarket]] launched 15-minute "up-down" bets on [[Bitcoin]], [[Ethereum]], [[Solana]], and [[XRP]] in late 2025. [[Polymarket]] subsequently added 5-minute contracts. Binary outcome: token price higher or lower at expiry.

- Combined daily volume: ~$70M across both platforms (Mar 2026)
- More than half of all crypto trading on both platforms
- Volume grew despite BTC down >40% from October 2025 peak and [[Polymarket]] fee introduction (Jan 2026, up to 1.56%)

HFT arbitrage was "rampant" on 15-minute markets before fees — latency gaps between Polymarket and [[Binance]] gave sophisticated traders free money. When fees compressed arb on 15-min, firms moved to 5-min markets where "microstructure inefficiencies" persist.

Source: FT (Mar 13, 2026)

### Nasdaq binary options (proposed)

[[Nasdaq]] filed with regulators (week of Mar 10, 2026) to introduce binary "yes-no" options on whether the [[Nasdaq 100]] trades at, above, or below a pre-determined price. Initial contracts would expire over a few days, with potential expansion to zero-day (24-hour) alternatives.

This is the tradfi version of the same impulse. Nasdaq watched Polymarket and Kalshi print volume with binary crypto contracts and filed its own. Amanda Fischer ([[Better Markets]], former SEC chief of staff): "Everyone is in a race to become the next super app to rule them all. Trad-fi is copying crypto, and vice versa."

---

## Why now

Several enablers converged:

- Mobile-first brokerages — [[Robinhood]], [[Charles Schwab|Schwab]], [[Kalshi]] apps make sub-minute trades frictionless
- Regulatory permissiveness — Trump-era [[CFTC]] (Selig) and [[SEC]] are pro-innovation; 0DTE proliferated under a [[CBOE]] that wanted volume
- Crypto volatility — BTC's 40%+ drawdown from October 2025 peak creates the exact conditions retail gamblers love: big moves, fast resolution
- AI trading rituals — retail traders using LLMs ([[Claude]], [[Gemini]], [[ChatGPT]]) to generate "odds" for 5-minute trades. Max Wojcik, an engineer, described running three chatbots that "converse" among themselves before he places bets. This dresses up noise trading in the language of analysis, lowering the psychological barrier to gambling. Source: FT (Mar 13, 2026)
- Post-election prediction market legitimacy — [[Polymarket]]'s 2024 election success gave prediction markets mainstream credibility, drawing capital into all contract types

---

## Structural risks

| Risk | Mechanism |
|---|---|
| Gamma amplification (0DTE) | Dealer hedging of near-expiry options amplifies intraday index moves |
| Retail capital destruction | House edge (fees, spread, latency disadvantage) compounds across hundreds of daily bets |
| Regulatory arbitrage | Platforms design around existing rules — crypto bets avoid securities classification, prediction markets avoid gambling classification |
| Contagion of design | Success of ultra-short contracts pressures all exchanges to shorten durations, racing toward pure gambling with derivatives wrappers |

---

## Related

- [[Prediction markets]] — 5/15-minute crypto bets as fastest-growing segment
- [[Polymarket]] — 5-min and 15-min crypto contracts, fee introduction
- [[Kalshi]] — 15-min crypto contracts, margin trading application
- [[Nasdaq]] — binary options filing (Mar 2026)
- [[CFTC]] — regulatory permissiveness enabling proliferation
- [[Michael Selig]] — CFTC chairman framing speculation as hedging
- [[Crypto]] — underlying asset class for prediction market ultra-short bets
- [[Derivatives]] — ultra-short contracts are derivatives by structure
