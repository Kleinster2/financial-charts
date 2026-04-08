---
aliases: [Investors Exchange, IEX Exchange, IEX Group]
---
#actor #exchange #fintech #market-structure #usa #private

**IEX** — Stock exchange founded by Brad Katsuyama in 2012 after discovering [[latency arbitrage]] in US equity markets. Built a 350-microsecond "speed bump" to neutralize HFT advantages. Origin story chronicled in Michael Lewis's [[Flash Boys]] (2014). Applied to the [[SEC]] to add options trading in 2025, sparking a fight with [[Citadel Securities]].

IEX represents the anti-speed thesis in US [[Market structure|market structure]]: that millisecond advantages serve trading firms, not capital formation. The exchange has won every regulatory fight against [[Citadel Securities]] so far — twice on equities, including on appeal — but hasn't reshaped equity markets as feared. The options application is a bigger test: options are more complex than equities (hundreds of strikes and expiries per stock), making [[latency arbitrage]] more profitable and the case for a speed bump stronger.

---

## Leadership

| Role | Name |
|------|------|
| Founder, CEO | Brad Katsuyama |

---

## Quick stats

| Metric | Value |
|--------|-------|
| Founded | 2012 |
| Exchange status | SEC-approved (2016) |
| Equity market share | ~3-4% |
| Founder | Brad Katsuyama |
| HQ | New York |
| Key innovation | Speed bump (350μs delay) |

---

## Origin: the latency arbitrage problem

Katsuyama, a trader at [[RBC]], discovered that HFT firms were front-running his orders by exploiting speed differentials between exchanges. His order would arrive at one exchange, HFT firms would see it, race to other exchanges, and buy available shares before his order reached them — then sell back at a higher price. The advantage was measured in milliseconds.

IEX's solution: a coil of fiber-optic cable that adds a 350-microsecond delay (the "speed bump"), neutralizing the speed advantage. No co-location, no payment for order flow, transparent rules.

---

## IEX vs [[Citadel]]: the equities rounds

[[Citadel Securities]] twice opposed IEX's equities exchange applications and lost both times — including losing on appeal. The core objection was that IEX's speed bump gave an unfair advantage to certain participants and complicated the best-execution framework under Reg NMS.

Despite fears, IEX's equities innovations did not reshape equity markets as opponents had predicted. IEX captures ~3-4% of equity volume — meaningful but not transformative.

---

## The options application (2025)

IEX applied to the [[SEC]] to add options to its existing stock exchange, entering a market with 18 existing platforms. Its proposed system would automatically delay, cancel, or reprice quotes from market makers if IEX software detects that the best price is about to change from a given quote — targeting [[latency arbitrage]] specifically in options, where the problem is amplified by complexity (a single stock can have hundreds of options with varying strikes and expiry dates).

Under Reg NMS best-execution rules, all market makers would have to route trades to IEX when its price looks the best — even if they believe IEX's software may cancel or modify the trade before completion. This is [[Citadel Securities]]' core objection.

### The comment letter battle

| Side | Position | Key actors |
|------|----------|------------|
| Opposing | Speed bump disrupts best execution; forces routing to a venue that may cancel trades | [[Citadel Securities]] (3 comment letters) |
| Supporting | Levels playing field; reduces [[latency arbitrage]] | [[Virtu Financial]], CTC |

The debate is a new riff on the decade-old question from [[Flash Boys]]: does shaving further milliseconds off trading times serve any public market function, or does it simply entrench the fastest firms?

*Source: [[Financial Times]] (Sep 1, 2025)*

---

## Cap table / Funding

| Round | Date | Amount | Lead / Notable |
|-------|------|--------|----------------|
| Seed | 2012 | Undisclosed | Brad Katsuyama, founding team |
| Subsequent rounds | 2013-2016 | Undisclosed | Various; details not public |

IEX is a private exchange. Detailed funding information is not publicly available. The company launched as a dark pool (2013) before receiving SEC approval as a national securities exchange (2016).

---

## Related

- [[Flash Boys]] — Michael Lewis book chronicling IEX's creation
- [[Citadel Securities]] — opponent in equities and options market structure fights
- [[Virtu Financial]] — supports IEX options application
- [[SEC]] — regulator reviewing options application
- [[CBOE]] — largest options exchange group (~30% share)
- [[Market structure]] — the regulatory and infrastructure context
- [[0DTE options]] — the options volume boom driving new platform interest
- [[HFT-hedge fund convergence]] — broader structural context for the speed vs fairness debate
