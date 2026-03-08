---
aliases: [Iran war basket, Iran conflict basket 2026]
tags: [thesis, geopolitics, defense, oil, airlines, basket]
---

# Iran conflict long-short basket

Systematic long/short basket capturing idiosyncratic market dislocations from the [[2026 Iran conflict market impact|2026 Iran conflict]]. Weights derived from **market cap x trimmed sigma** (move amplitude measured in standard deviations of 1-year daily returns, winsorized at 90th percentile to strip earnings/event tail noise).

Methodology: every asset that moved idiosyncratically due to the conflict, weighted by the product of its market capitalization and the statistical unusualness of its move. No directional view -- purely event-driven.

---

## Long leg

| Ticker | Name | Move | Sigma | Weight |
|--------|------|------|-------|--------|
| [[Exxon|XOM]] | Exxon | +4.0% | 3.5 | 20.3% |
| [[RTX]] | RTX | +6.6% | 6.5 | 16.9% |
| [[Chevron|CVX]] | Chevron | +4.0% | 3.8 | 13.1% |
| [[Shell|SHEL]] | Shell | +5.2% | 5.3 | 11.5% |
| [[Lockheed Martin|LMT]] | Lockheed Martin | +6.7% | 6.1 | 8.6% |
| [[Saab|SAAB-B]] | Saab | +4.7% | 2.1 | 6.5% |
| [[Northrop Grumman|NOC]] | Northrop Grumman | +5.2% | 4.9 | 4.9% |
| [[L3Harris|LHX]] | L3Harris | +5.6% | 5.2 | 3.3% |
| [[ConocoPhillips|COP]] | ConocoPhillips | +3.5% | 2.3 | 3.0% |
| [[Newmont Mining|NEM]] | Newmont Mining | +3.0% | 1.6 | 2.0% |
| [[Agnico Eagle|AEM]] | Agnico Eagle | +3.0% | 1.7 | 1.9% |
| [[Thales|HO]] | Thales | +5.9% | 3.7 | 1.8% |
| [[Rheinmetall|RHM]] | Rheinmetall | +5.0% | 2.4 | 1.6% |
| [[Maersk|AMKBY]] | Maersk | +7.8% | 4.3 | 1.5% |
| [[Hapag-Lloyd|HPGLY]] | Hapag-Lloyd | +6.7% | 4.9 | 1.2% |
| [[Kratos Defense|KTOS]] | Kratos | +10% | 3.2 | 0.4% |
| [[AeroVironment|AVAV]] | AeroVironment | +10% | 3.6 | 0.3% |

Composition: 55% energy, 33% defense, 6% gold miners, 4% shipping, 2% drones.

---

## Short leg

| Ticker | Name | Move | Sigma | Weight |
|--------|------|------|-------|--------|
| [[Booking Holdings|BKNG]] | Booking Holdings | -4.0% | 3.0 | 33.3% |
| [[IAG]] | IAG | -13% | 8.1 | 12.2% |
| [[Ryanair|RYAAY]] | Ryanair | -5.0% | 3.7 | 10.5% |
| [[Singapore Airlines|SINGY]] | Singapore Airlines | -4.7% | 7.0 | 9.8% |
| [[Delta Air Lines|DAL]] | Delta Air Lines | -5.7% | 2.6 | 9.2% |
| [[United Airlines|UAL]] | United Airlines | -6.0% | 2.5 | 6.8% |
| [[Carnival|CCL]] | Carnival | -3.0% | 1.5 | 5.1% |
| [[Qantas|QAN]] | Qantas | -5.0% | 4.2 | 4.8% |
| [[Expedia|EXPE]] | Expedia | -3.0% | 1.6 | 3.5% |
| [[American Airlines|AAL]] | American Airlines | -6.0% | 2.5 | 1.7% |
| [[Hyatt|H]] | Hyatt | -2.0% | 1.3 | 1.6% |
| [[Norwegian Cruise Line|NCLH]] | Norwegian Cruise | -4.0% | 1.8 | 1.5% |

Composition: 48% airlines, 26% OTAs/travel, 14% cruise, 5% hotels.

---

## Methodology

- **Universe:** all single-name equities with idiosyncratic moves attributable to the Iran conflict (Day 1-3 reaction, Feb 28 - Mar 2, 2026)
- **Volatility:** 1-year daily return standard deviation, winsorized at 10th/90th percentile to strip earnings and other non-conflict tail events
- **Sigma:** |event day move| / trimmed daily vol -- measures how unusual the move was relative to the stock's normal behavior
- **Score:** market cap ($B) x sigma -- captures both the economic significance (cap) and the idiosyncratic intensity (sigma) of each name's reaction
- **Weight:** score normalized within each leg

### Key observations

- **RTX (6.5 sigma) and LMT (6.1 sigma)** are the most statistically unusual defense moves -- their normal daily vol is ~1%, making a 6-7% day genuinely extreme
- **IAG (8.1 sigma)** is the single most idiosyncratic move in the basket -- a -13% day on a stock that normally does ~1.6%/day (trimmed)
- **Singapore Airlines (7.0 sigma)** is the second most extreme -- -4.7% looks modest until you see its trimmed daily vol is only 0.67%
- **AVAV and KTOS** rank low despite +10% moves because their daily vol is structurally ~3-4% -- a 10% day is only ~3 sigma, not unusual for these names
- **BKNG dominates the short side (33%)** through sheer cap weight ($135B) despite a moderate 3.0 sigma move

---

## Related

- [[2026 Iran conflict market impact]] -- full market reaction narrative
- [[US-Iran nuclear escalation February 2026]] -- pre-strike scenario analysis and market impact
- [[Iran]] -- country actor
- [[Strait of Hormuz]] -- the key supply disruption variable
- [[Defense]] -- sector hub
- [[Oil]] -- commodity context

---

## Day 9 update — basket implications at $92 Brent (March 7)

The basket's initial construction used Day 1-3 moves (Feb 28 – Mar 2) when Brent was ~$72-79. At $92.69 (Mar 7), the thesis assumptions need reassessment:

### Long leg — still working, but composition matters

- **Energy (55% of long):** Oil majors initially lagged crude (Day 4-5 divergence), but at $92 Brent the duration trade has shifted. Equity investors can no longer price a "quick resolution" — oil has stayed bid for 9 days while equities sold. The disconnect between crude (+33% from pre-strike) and major equities (XOM/CVX much smaller cumulative moves) may be compressing. **US LNG pure-plays** ([[Cheniere]], [[Venture Global]]) are the new beneficiaries not in the original basket — [[QatarEnergy]] force majeure created a structural supply gap that US exporters fill regardless of war duration.
- **Defense (33%):** Primes gave back conflict premium on Days 4-5 as "quick war" narrative took hold. If the war extends (Trump demanding unconditional surrender), the premium returns. AVAV/KTOS more volatile but less statistically unusual (3 sigma vs RTX's 6.5 sigma).
- **Gold miners (6%):** Gold had a -4.48% reversal on Day 4 (profit-taking after +23% run). At $92 oil with stagflation narrative, gold's safe-haven bid should return.
- **Shipping (4%):** VLCC rates quadrupled to >$400K/day by Day 4. Tankers remain the purest play on Hormuz duration.

### Short leg — more pain ahead

- **Airlines (48%):** Fuel is the largest variable cost. At $92 Brent (vs ~$70 pre-strike), unhedged airlines face margin destruction. Route disruptions (Middle East airspace closures) compound. DAL's brief recovery on Day 4 is unlikely to hold.
- **Travel/OTAs (26%):** Stagflation narrative + consumer spending weakness (retail sales miss) = discretionary pullback. BKNG's 33% basket weight is well-placed.
- **Cruise (14%):** Fuel-intensive, unhedged, and consumer discretionary — worst of both worlds.

### Potential additions

Consider adding to long leg: [[Cheniere]] (LNG), [[Venture Global]] (VG) — structurally benefiting from Qatar's absence. Consider adding to short leg: Russell 2000 / IWM as a small-cap stagflation proxy.

### Key risk

If a ceasefire materializes (Iran peace feelers on Day 5 briefly moved markets), the entire basket unwinds violently. The basket is a duration bet: it pays if the conflict extends, and reverses if it resolves. At Day 9 with Trump demanding unconditional surrender, duration probability has increased.

---

*Created 2026-03-03. Updated 2026-03-07.*
