---
aliases: [SPAC, Special Purpose Acquisition Company, Blank check company, De-SPAC]
---
#concept #finance #capital-markets #ipo

# SPACs

A Special Purpose Acquisition Company is a shell company that IPOs with no operations, raises cash in a trust, then merges with a private company to take it public — bypassing the traditional IPO process. The 2020-2021 SPAC boom raised ~$245B across 860+ vehicles, destroyed the majority of that capital, bankrupted multiple targets, and triggered an SEC crackdown. The structure's fundamental flaw: it transfers wealth from retail shareholders to sponsors and hedge fund arbitrageurs through compounding dilution.

---

## The mechanics

### How a SPAC works

1. **IPO:** Sponsor creates a shell company, sells units at $10 (each unit = 1 share + fraction of a warrant). Cash goes into a trust earning T-bill rates
2. **Search:** Sponsor has 18-24 months to find and announce a merger target
3. **Vote/Redeem:** Shareholders vote on the deal. Anyone who dislikes it can redeem shares at ~$10 + accrued interest (essentially risk-free)
4. **Merge:** If approved, the SPAC merges with the target. The target becomes publicly traded
5. **Liquidate:** If no deal is found, the SPAC dissolves and returns cash to shareholders

### The dilution stack

Three layers of dilution compound to destroy non-redeeming shareholder value:

| Source | Mechanism | Impact |
|--------|-----------|--------|
| **Sponsor promote** | 20% of post-IPO shares purchased for ~$25,000 | On a $200M SPAC, ~$40M in free equity |
| **Warrants** | 5-year call options ($11.50 strike) included in IPO units | Dilute when exercised; kept even by redeemers |
| **Underwriting fees** | Paid on full IPO proceeds regardless of redemptions | Concentrated on remaining shareholders |

**Result:** Net cash per share at merger averages ~$6.67 vs. nominal $10 (Klausner, Stanford/Yale). Non-redeeming shareholders start 33% underwater before the target's stock even trades.

### The misaligned incentives

| Player | Incentive | Outcome |
|--------|-----------|---------|
| **Sponsor** | Gets nothing if SPAC liquidates; promote worth ~$40M+ even on bad deals | Prefers any deal over no deal |
| **Hedge fund IPO buyers** | Redeem at $10 + interest; keep warrants as free upside | Risk-free ~11.6% annualized; exit before merger |
| **PIPE investors** | Backstop redemptions; get preferred terms | Better entry than retail |
| **Retail shareholders** | Hold through merger; bear all dilution | Mean return: -64% (market-adjusted) |

---

## The boom-bust arc

### Phase 1: Niche vehicle (2003–2019)

SPACs existed as a small corner of capital markets. Modest volumes — 46 IPOs raised $10.7B in 2018, 59 raised $13.6B in 2019. Primarily used by serial acquirers and PE-adjacent sponsors for mid-market targets.

### Phase 2: The mania (2020–2021)

| Year | SPAC IPOs | Capital raised | % of all US IPOs |
|------|-----------|---------------|-----------------|
| 2020 | ~248 | ~$83B | >50% |
| 2021 | 613 | ~$162B | >60% |

**What fueled it:**
- Zero interest rates (trust accounts cost nothing to maintain)
- Pandemic stimulus + retail trading boom (Robinhood, r/SPACs)
- Celebrity sponsors (Shaq, A-Rod, Serena Williams, Jay-Z)
- Regulatory arbitrage: SPACs could publish forward projections that traditional IPOs cannot
- FOMO from a few early wins (DraftKings +380% from $10)

**Peak insanity:** In Q1 2021, 298 SPACs raised $87B in a single quarter. SPACs outnumbered traditional IPOs 4:1. Companies with zero revenue commanded multi-billion-dollar valuations via projections alone.

### Phase 3: The bust (2022–2023)

| Metric | Value |
|--------|-------|
| Redemption rates | 80-90%+ (vs. 12% in early 2021) |
| SPACs liquidated (2022) | ~145 |
| SPACs liquidated (2023) | ~200 |
| Liquidation rate | 67% of SPACs wound down without merging |
| De-SPAC performance | 77% traded below $10 within a year (Goldman) |

**What broke:**
- Rising rates made trust accounts expensive (opportunity cost)
- SEC scrutiny on projections and accounting
- Post-merger performance universally terrible
- PIPE market froze (no institutional backstop)
- Sponsor reputations collapsed

### Phase 4: SEC crackdown (Jan 2024)

Final rules adopted January 24, 2024 (effective July 1, 2024):

| Rule change | Impact |
|-------------|--------|
| Target must sign registration statement | Target liable for misstatements (like traditional IPO) |
| De-SPAC deemed a "sale" (Rule 145a) | Full Securities Act liability applies |
| Forward-looking safe harbor eliminated | No more speculative projections without legal risk |
| Enhanced dilution disclosures | Promote, warrants, conflicts on cover page |
| No Investment Company Act safe harbor | Slow-to-merge SPACs risk investment company classification |

### Phase 5: Tentative revival (2024–2025)

| Year | SPAC IPOs | Capital raised | Character |
|------|-----------|---------------|-----------|
| 2024 | 57 | $9.6B | Serial sponsors only |
| 2025 (through mid-year) | ~50+ | ~$11B | 70-80% repeat sponsors |

The 2025 vintage is structurally different: smaller raises, experienced sponsors, some with reduced promotes or performance-vesting economics. But the fundamental dilution math hasn't changed.

---

## The investor scorecard

### Retail investors (systematic losers)

| Metric | Value | Source |
|--------|-------|--------|
| Mean market-adjusted return | **-64%** | Klausner (Stanford/Yale) |
| Median market-adjusted return | **-88%** | Klausner |
| 2021-2022 merger cohort losses | -67% and -59% avg | Goldman Sachs |
| Worst annual underperformance vs market | -73.6% | Multiple studies |

### Hedge fund arbitrageurs (systematic winners)

| Strategy | Return | Risk |
|----------|--------|------|
| Buy at $10, redeem at merger | ~11.6% annualized | Essentially zero (trust-backed) |
| Keep warrants post-redemption | Free call option | Zero additional cost |
| Short post-merger | Profitable given dilution overhang | Some squeeze risk |

IPO investors are "almost entirely large institutional investment managers affiliated with hedge funds" (Klausner). They redeem before merger, capturing risk-free returns while retail bears the dilution.

### Sponsors (win regardless)

A $200M SPAC with 20% promote = ~$40M in equity for $25K investment. Even if the merged company drops 50%, the sponsor's shares retain ~$20M in value. The sponsor only loses if the SPAC liquidates without a deal — hence the incentive to merge at any cost.

**Chamath example:** Social Capital generated ~$750M in sponsor profits across 12 SPACs, despite median investor losses of 75%.

---

## Notable SPACs

### Failures

| Company | SPAC | Peak valuation | Outcome |
|---------|------|---------------|---------|
| **Nikola** (NKLA) | VectoIQ | $27.6B market cap | Fraud, CEO indicted, bankrupt Feb 2025 |
| **Lordstown Motors** | DiamondPeak | ~$5B | Fake pre-orders, bankrupt 2023 |
| **[[Bird]]** | Switchback II | $2.5B | Bankrupt Dec 2023, acquired $145M |
| **Clover Health** | Social Capital | ~$7B day-one | DOJ/SEC investigation, stock ~$0.80 |
| **IronNet** | LGL Systems | — | Bankrupt 2023 |
| **Polestar** | Gores Guggenheim | $20B EV | Down 90% from $10 |
| **Sonder** | Gores Metropoulos II | — | Down 99% from $10 |
| **MultiPlan** | Churchill III | — | Down 89% from $10 |
| **Lucid** | Churchill IV | $4.4B merger | Down 85% from debut |

### Successes (rare)

| Company | SPAC | Return from $10 |
|---------|------|----------------|
| **Vertiv** (VRT) | GS Acquisition | +1,175% |
| **Restaurant Brands** (QSR) | Justice Holdings | +533% |
| **DraftKings** (DKNG) | Diamond Eagle | +380% |
| **Symbotic** (SYM) | SVF Investment 3 | +374% |
| **SoFi** (SOFI) | Social Capital | +155% |

The successes share a common trait: they were real businesses with real revenue at merger time, not pre-revenue concept companies selling projections.

---

## Key sponsors

### [[Chamath Palihapitiya]] (Social Capital)

12 SPACs launched. Face of the SPAC boom. Mergers: Virgin Galactic (down 98%), Opendoor (down 65%), Clover Health (down 74%), SoFi (up 155%), ProKidney (down 74%). Median investor loss: 75%. Firm still generated ~$750M in sponsor profits.

Launched new SPAC (American Exceptionalism Acquisition Corp, $345M) in Sep 2025 — no warrants, compensation vests only if shares rise 50%+. Five times oversubscribed.

### Michael Klein (Churchill Capital)

Former Citigroup investment banker. Churchill IV merged with Lucid (now down 85%). Churchill III merged with MultiPlan (down 89%). Filed Churchill XI ($300M) in late 2025. Continues launching despite track record.

### Gores Group (Alec Gores)

13+ SPACs — more than any single investor. Started the modern SPAC revival via Hostess Brands (2016). Key mergers: United Wholesale Mortgage ($16.1B), Polestar ($20B, down 90%), Sonder (down 99%). Filed Gores X ($260M) — still active.

### Bill Ackman ([[Pershing Square]])

Raised $4B — the largest SPAC ever (Pershing Square Tontine Holdings). Attempted to buy 10% of Universal Music Group; SEC objected. Discussions with Airbnb and Stripe failed. Liquidated Jul 2022, returned $4B. Proposed "SPARC" structure (investors commit capital only after target announced) — regulatorily uncertain.

---

## Vault examples

SPACs appear throughout the vault as a funding mechanism, usually in cautionary contexts:

| Actor | SPAC detail |
|-------|-------------|
| [[Bird]] | $2.5B SPAC → bankrupt → $145M acquisition |
| [[Gogoro]] | NASDAQ: GGR via SPAC, Apr 2022; now $50M market cap |
| [[QuantumScape]] | 2020 SPAC; peaked ~$130, now ~$5 |
| [[Joby Aviation]] | eVTOL; still pre-revenue post-SPAC |
| [[Chamath Palihapitiya]] | 12 SPACs, ~$750M sponsor profits, median investor loss 75% |

---

## Lessons

1. **Structure creates outcome.** The 20% promote + warrants + underwriting fees reduce net cash to ~$6.67 per nominal $10 share. Non-redeemers start 33% underwater — the math guarantees median losses
2. **Misaligned incentives produce bad deals.** Sponsors prefer a -50% merger over liquidation. The result: 77% of de-SPACed companies traded below $10 within a year
3. **Projections without liability = fraud.** Pre-2024 SPACs could publish wildly optimistic projections with no legal consequence. Nikola ($27.6B valuation with no trucks), Lordstown (fake pre-orders), Bird (overstated revenue) — the pattern is consistent
4. **Retail systematically subsidized institutions.** Hedge funds earned risk-free 11.6% by redeeming; retail bore -64% mean losses. The structure is a wealth transfer mechanism, not a capital formation tool
5. **Celebrity and hype are inversely correlated with returns.** The most promoted SPACs (Chamath's, Gores's high-profile mergers) produced the worst outcomes. The quiet, boring deals (Vertiv, Restaurant Brands) actually worked

---

## Related

- [[Bird]] — SPAC cautionary tale ($2.5B → bankrupt)
- [[Gogoro]] — SPAC-listed, 99% value destruction
- [[QuantumScape]] — SPAC-listed, -95% from peak
- [[Chamath Palihapitiya]] — SPAC promoter, 12 vehicles
- [[Pershing Square]] — largest SPAC ever ($4B), liquidated
- [[Joby Aviation]] — eVTOL, SPAC-listed
- [[Micromobility]] — sector where SPACs funded multiple failures
- [[Fintech boom (2020-2021)]] — parallel bubble, similar timing and drivers

---

*Created 2026-01-24*
