---
aliases: [hedge, hedging strategy, hedge effectiveness, risk hedging]
tags: [concept, risk-management, derivatives]
---

# Hedging

Hedging is the practice of taking an offsetting position to reduce exposure to an unwanted risk. It transfers risk from the hedger to a counterparty willing to bear it — for a price. Hedging does not eliminate risk; it transforms one kind of risk (directional exposure) into others (basis risk, counterparty risk, opportunity cost). The foundational question is not whether to hedge, but what residual risks the hedge introduces and whether those are preferable to the original exposure.

---

## The story

The logic of hedging starts from a simple asymmetry: some entities can absorb a given risk cheaply, and others cannot. An airline can manage its route network, crew scheduling, and pricing — but a 50% spike in [[Jet fuel|jet fuel]] prices can wipe out a year's operating margin overnight. A gold miner can control extraction costs but not the price of [[Gold|gold]]. Hedging allows each to lock in a future price, converting an uncertain cost or revenue into a known one. The instrument differs — a forward contract for a commodity producer, a put option for a portfolio manager, a swap for a borrower — but the logic is the same: pay a known cost now to cap an unknown cost later. The [[Derivatives primer]] covers the mechanics of each instrument.

The cost of hedging is not just the premium or margin posted. It includes the opportunity cost of gains forgone. An airline that locks in jet fuel at $90/bbl is protected if fuel hits $200 — but if fuel drops to $60, it still pays $90 while unhedged competitors enjoy the windfall. This is not a failure of the hedge; it is the hedge working as designed. The mistake is evaluating a hedge by whether it "made money." A hedge that cost money but prevented a catastrophic loss performed exactly as intended. The confusion between hedging and speculation is one of the most common errors in corporate finance — and the slip from one to the other has destroyed companies. Metallgesellschaft in 1993, China Aviation Oil in 2004, and Amaranth Advisors in 2006 all started with hedging programs that morphed into speculative positions when managers began optimizing for P&L rather than risk reduction.

Basis risk is the core failure mode. A hedge works perfectly only if the hedging instrument moves in exact lockstep with the underlying exposure. In practice, it rarely does. The gap between the hedge and the exposure is basis risk, and it materializes most violently during crises — precisely when the hedge matters most. The 2026 [[Iran conflict airline disruption|Iran conflict]] exposed this with surgical clarity: [[Cathay Pacific]] hedged ~30% of its fuel consumption, but on crude oil rather than jet fuel. Under normal conditions the difference is small. But when the [[Strait of Hormuz]] closure drove the crack spread — the gap between crude oil and refined jet fuel — to roughly double its normal level, jet fuel prices rose about twice as much as crude. Cathay's hedge was active but failing to cover the actual exposure. The hedging instrument matched, but the basis did not. European budget carriers [[Ryanair]] and [[EasyJet]], hedged 70-80% on rolling 12-month contracts against jet fuel specifically, were far better positioned. The lesson is that hedging the wrong benchmark can be worse than not hedging at all, because it creates a false sense of security.

Timing is the second failure mode. Hedges expire. Rolling them — extending coverage by taking out new contracts as old ones mature — is a routine cost that becomes a crisis cost when volatility spikes. Airlines on 12-month rolling programs were well covered entering the Iran conflict. But with jet fuel at $150-200/bbl and volatility elevated, the cost of rolling into new hedges at the forward curve is prohibitive. Most airlines stopped taking new hedges. This means the carriers that were 70-80% covered in early 2026 may face 0% coverage in 2027 if the crisis persists — a delayed vulnerability that markets have not yet priced. The pattern repeats across asset classes: hedging is cheapest when volatility is low and nobody perceives the need, and most expensive when volatility is high and everyone wants protection simultaneously. Implied volatility pricing means the cost of an option reflects the crowd's fear, not the hedger's private risk tolerance.

Counterparty risk is the third. A hedge is a contract, and contracts require someone on the other side who can pay. [[AIG]] in 2008 had sold $440B in credit default swaps — insurance against bond defaults — without reserving capital to pay claims. When the housing market collapsed, AIG's counterparties discovered their hedges were worthless without a government bailout. The lesson reshaped derivatives regulation: central clearing, margin requirements, and capital reserves all exist because of the 2008 demonstration that uncleared bilateral hedges concentrate rather than distribute risk. Today, exchange-traded derivatives ([[CME Group|CME]], [[CBOE]]) and central counterparties absorb most of this risk. But over-the-counter instruments — bespoke swaps, structured products, reinsurance contracts — still carry counterparty exposure, and the question "who is on the other side?" remains fundamental.

Corporate hedging and portfolio hedging serve different purposes and should not be confused. A corporation hedges to stabilize cash flows — an airline wants fuel cost predictability, a multinational wants FX predictability, a miner wants revenue predictability. The goal is operating stability, not profit maximization. Portfolio hedging, by contrast, aims to reduce drawdown risk in an investment portfolio. The tools overlap (options, futures) but the objectives diverge. The most common portfolio "hedge" — diversification via a 60/40 stock/bond allocation — is not hedging at all. It relies on a negative stock-bond correlation that is regime-dependent, not structural. During the [[Iran conflict portfolio hedging|2026 Iran conflict]], both stocks and bonds sold off simultaneously (oil shock → inflation → rate expectations → bonds fall; uncertainty → equities fall), exposing the 60/40 portfolio as an unhedged bet on correlation stability. Actual portfolio hedges — tail-risk puts, commodity futures, explicit short positions — performed, but they required active management and cost money. Diversification is free and fragile; hedging is costly and reliable. The distinction matters.

Natural hedges arise from the structure of an entity's operations rather than from derivative contracts. The [[United States]] as a net energy producer is naturally hedged against oil price spikes in a way that [[Japan]] (95% Middle East crude dependency) is not — higher oil prices boost US producer revenues and tax receipts even as they burden consumers. [[Saudi Arabia]]'s position is even starker: oil revenue funds the state, so high prices are a windfall even as the country pursues green diversification with Chinese technology. Within corporations, a company that earns revenue in euros and pays costs in dollars has a natural FX hedge against euro depreciation if it also has euro-denominated debt. Identifying natural hedges is analytically prior to purchasing financial hedges — overlaying a derivative hedge on top of a natural one can inadvertently create a speculative position.

The paradox of hedging markets is that the system's aggregate risk does not decrease just because individual participants hedge. Risk is transferred, not destroyed. When an airline buys a jet fuel call option, the option seller (often a bank or trading firm) must manage the resulting exposure — typically through [[Gamma squeeze|delta hedging]], dynamically buying and selling the underlying commodity to stay neutral. This dealer hedging activity can itself amplify price moves: as prices rise, dealers buy more to maintain their hedge, pushing prices higher still. The 2021 [[GameStop]] episode and routine end-of-day [[0DTE options|0DTE]] pinning effects are extreme examples of hedging flow driving the very price the hedges are meant to protect against. At the system level, hedging redistributes risk toward entities that can bear it more efficiently — but concentrations can build in ways that are invisible until they aren't.

---

## Airline fuel hedging

Airlines are the textbook corporate hedging case. [[Jet fuel]] is 25-30% of operating costs (~$250B/yr globally), uncontrollable by management, and capable of swinging from $60 to $200/bbl within months. A 50% fuel price spike can erase an entire year's operating margin. The instruments are fuel swaps, call options, and collars — typically benchmarked to jet fuel (kerosene) futures, though some carriers hedge on crude oil as a proxy.

The industry divides along competitive lines. European ultra-low-cost carriers operate in the most price-sensitive market on earth — razor-thin margins, fierce competition, passengers who switch carriers over a few euros. This forces aggressive hedging discipline. [[Ryanair]] and [[EasyJet]] maintain 70-80% coverage on rolling 12-month contracts, locking in fuel costs a year ahead. This is not conservatism; it is survival — an unhedged ULCC that eats a fuel spike while competitors are covered will hemorrhage market share on price.

Asian carriers generally hedge less. The reasoning is symmetric: each hedge is itself a calibrated risk, and the counterparty charges for bearing it. In a period of stable or declining fuel prices, a carrier that hedges less has lower costs than one paying rolling premiums. [[Cathay Pacific]] hedges ~30% of near-term consumption. China's Big Three ([[Air China]], [[China Eastern Airlines|China Eastern]], [[China Southern Airlines|China Southern]]) and [[IndiGo]] are among the most exposed to fuel price swings ([[Bloomberg Intelligence]]).

The critical variable is not how much a carrier hedges but what it hedges against. Jet fuel and crude oil normally move together, but the crack spread — the refining margin between them — can blow out under stress. When the [[Strait of Hormuz]] closed in 2026, Gulf refineries went offline alongside crude supply. Jet fuel prices rose roughly twice as much as crude because the refining bottleneck compounded the supply disruption. Cathay Pacific, hedged on crude rather than jet fuel, discovered that its hedge was active but failing to cover the actual exposure. [[Ryanair]] and [[EasyJet]], hedged specifically on jet fuel, were protected. The lesson generalizes: hedging a correlated proxy rather than the actual exposure introduces basis risk that is invisible in calm markets and catastrophic in crises.

Rolling dynamics create a second timing vulnerability. A 12-month hedge taken at $90/bbl expires in 12 months. Renewing it requires taking a new position at the prevailing forward price. During the 2026 crisis, with jet fuel at $150-200/bbl and implied volatility elevated, the cost of new hedges became prohibitive. Most carriers stopped rolling. This means well-hedged airlines face a coverage cliff: 70-80% protected in 2026, potentially 0% in 2027 if the crisis persists and hedges expire without renewal. The market has not yet priced this delayed exposure. See [[Iran conflict airline disruption]] for the crisis-specific data.

---

## Reference — hedging instruments

See [[Derivatives primer]] for full mechanics. This table frames hedging-specific use cases.

| Instrument | Hedging use | Cost structure | Key risk |
|------------|------------|----------------|----------|
| Forwards | Lock future price (commodities, FX) | No upfront premium; margin/collateral | Counterparty risk (bilateral); opportunity cost |
| Futures | Same as forwards, exchange-traded | Margin; daily mark-to-market | Basis risk (standardized vs. actual exposure); roll cost |
| Put options | Floor on asset value; cap on cost | Upfront premium | Premium lost if hedge unnecessary; time decay |
| Call options | Cap on purchase cost (e.g., fuel) | Upfront premium | Same as puts |
| Collars | Floor + cap (buy put, sell call) | Zero-cost or low-cost (call premium offsets put) | Capped upside; complexity |
| Swaps | Exchange floating for fixed (rates, commodities) | Spread embedded in fixed rate | Counterparty risk; mark-to-market volatility |
| [[Cross-currency swaps]] | Hedge FX + interest rate simultaneously | Basis spread | Cross-currency basis blowout in crises |

---

## Reference — failure modes

| Failure mode | Mechanism | Vault example |
|-------------|-----------|---------------|
| Basis risk | Hedge instrument diverges from actual exposure | [[Cathay Pacific]]: hedged crude, exposed to jet fuel; crack spread blew out ~2x during Iran conflict |
| Roll risk | Hedges expire; renewal cost spikes during crisis | Airlines unlikely to roll at $150-200/bbl jet fuel → 2027 gap ([[Iran conflict airline disruption]]) |
| Counterparty failure | Hedge writer unable to pay | [[AIG]] 2008: $440B CDS exposure, government bailout required |
| Correlation breakdown | Diversification "hedge" fails when correlations converge | 60/40 portfolios during Iran conflict — stocks and bonds fell together ([[Iran conflict portfolio hedging]]) |
| Hedge-to-speculation drift | Hedging program becomes profit center | Metallgesellschaft 1993 (oil forwards), China Aviation Oil 2004 |
| Over-hedging | Hedge exceeds underlying exposure → net speculative | Airlines locking fuel above consumption needs |
| Wrong tenor | Hedge maturity mismatches exposure duration | Short-dated hedges on long-duration liabilities |

---

## Reference — corporate hedging patterns

| Sector | What's hedged | Typical instruments | Coverage horizon |
|--------|--------------|--------------------|--------------------|
| Airlines | Jet fuel price | Fuel swaps, call options, collars | 6-18 months rolling |
| Oil producers | Crude oil price (downside) | Put options, three-way collars, swaps | 1-3 years |
| Miners | Metal prices (gold, copper) | Forward sales, put options | 1-2 years |
| Multinationals | FX exposure | FX forwards, options | Quarterly rolling |
| Banks | Interest rate risk | Interest rate swaps, swaptions | Duration-matched |
| Utilities | Natural gas, power prices | Commodity swaps, forward purchases | 1-5 years |
| Reinsurers | Catastrophe exposure | [[Reinsurance sidecars]], ILS, cat bonds | Annual |

---

## Related

- [[Derivatives primer]] — instrument mechanics (options, futures, swaps, Greeks)
- [[Iran conflict portfolio hedging]] — live case study: 60/40 failure, manager strategies
- [[Iran conflict airline disruption]] — airline fuel hedging, crack spread basis risk, European vs. Asian coverage
- [[Gamma squeeze]] — dealer delta/gamma hedging feedback loops
- [[0DTE options]] — ultra-short hedging and pinning effects
- [[Jet fuel]] — crack spread, SAF hedging dynamics
- [[Cross-currency swaps]] — FX + rate hedging
- [[Commodities]] — hedging patterns in physical markets
- [[Physical Oil Trading]] — CFD basis risk hedging
- [[Risk Parity]] — alternative to traditional diversification "hedging"
- [[Market Sentiment Indicators]] — VIX as hedge cost proxy
- [[Cathay Pacific]] — basis risk case study (crude vs. jet fuel hedge)
- [[Ryanair]], [[EasyJet]] — well-hedged budget carriers (70-80%)
- [[Wizz Air]] — unhedged exposure example
- [[AIG]] — counterparty risk failure (2008)
- [[Reinsurance sidecars]] — catastrophe risk transfer

---

*Created 2026-03-28.*
