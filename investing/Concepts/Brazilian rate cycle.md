---
aliases: [Brazilian rate cycle, Selic cycle, Brazil Selic cycle, Brazil rate factor, Selic factor]
tags: [concept, macro, rates, brazil]
---
#concept #macro #rates #brazil

# Brazilian rate cycle

The Selic policy-rate cycle is the master factor for liquid Brazilian assets. A change in expectations for Selic re-rates Brazilian equities (a lower discount rate and an easier domestic economy) and long bonds (lower yields → higher prices) at the same time — so the two co-move, and the strength of that co-movement is governed almost entirely by an asset's duration / rate-sensitivity. This note maps how each Brazilian asset class loads on the cycle, using the cross-asset correlation work behind the [[Brazilian fixed-income ETFs]], [[FII]], and Brazilian equity notes.

## The cross-asset correlation map

Daily-return correlation, last ~2 years, to [[EWZ]] (Brazilian equities) and to [[IMAB11]] (IPCA government bonds — a clean "rate factor" proxy):

| Asset | vs [[EWZ]] | vs [[IMAB11]] | On the rate factor? |
|-------|-----------|--------------|---------------------|
| Cash — Tesouro Selic ([[LFTS11]]) | 0.08 | 0.09 | No (zero duration) |
| FIIs ([[HGLG11]], [[XPML11]], [[RECR11]]) | 0.00–0.12 | ~0.07 | No (illiquid / segmented) |
| Short IPCA ([[B5P211]]) | 0.41 | high | Yes |
| Full IPCA ([[IMAB11]]) | 0.39 | 1.00 | Yes |
| Long IPCA ([[IB5M11]]) | 0.47 | 0.71 | Yes (most) |
| Prefixado ([[IRFM11]]) | 0.39 | — | Yes |
| Utilities ([[Sabesp]], [[Equatorial]]) | 0.55 / 0.62 | 0.20 / 0.33 | Yes (most, in equities) |
| Fuel / cyclical ([[Vibra]]) | 0.62 | 0.28 | Yes |
| Global / defensive equities ([[Natura]], [[JBS]]) | 0.21 / 0.44 | — | Least (in equities) |

Two clusters fall out: a rate-factor cluster (duration bonds + rate-sensitive domestic equities, 0.39–0.62) and an off-factor cluster (cash and FIIs, ~0).

## Duration is the equity correlation

Within fixed income, an ETF's correlation to Brazilian equities rises monotonically with its duration: cash 0.08 → short IPCA 0.41 → full IPCA 0.39 → long IPCA 0.47, with the bond ETFs correlating 0.71 with each other. A "fixed-income" allocation in duration form is not a diversifier from the equity book — it is a leveraged bet on the same Selic-cut expectation the stocks already price. Only the floating-rate cash sleeve ([[LFTS11]]) sits off the factor by construction.

## Within equities, the rate-sensitive sectors load most

The same factor sorts the equity book. Rate-sensitive domestic names — regulated utilities ([[Sabesp]] 0.55, [[Equatorial]] 0.62) and the fuel-distribution cyclical [[Vibra]] (0.62) — carry the highest [[EWZ]] beta and the highest overlap with bonds (0.20–0.33 vs [[IMAB11]]). Global or defensive names load least: [[Natura]] (Latam consumer, 0.21) and [[JBS]] (USD-listed global protein, 0.44). The EWZ index is a blend, but its rate-sensitive domestic core is what makes the duration bonds correlate with it.

## The FII anomaly — resolved

FIIs are the puzzle: they are rate-sensitive in theory (a falling Selic re-rates their distribution yield upward), yet they are uncorrelated with both equities (~0.11) and bonds (~0.07) in daily returns. Three things resolve it:

- Illiquidity and retail ownership — FII prices move on their own thin order flow, not in lockstep with the liquid bond/equity markets.
- Yield, not duration — the rate sensitivity shows up slowly, as the distribution yield drifts against the Selic over months, rather than in a daily mark like a bond.
- Segmentation — FIIs correlate ~0.5 within a segment (the logistics cohort [[HGLG11]]/[[XPLG11]]/[[BTLG11]]) but ~0 across segments ([[XPML11]] malls vs logistics ≈ −0.01). There is no single "FII factor," let alone a market factor.

So FIIs are a genuine daily / tactical diversifier — the one Brazilian income asset that is orthogonal to the rate-and-equity complex day to day — even though they are not rate-immune over the full cycle, and they carry segment-concentration risk.

![[br-asset-classes-chart.png]]
*Normalized — [[EWZ]] (equities) vs [[IMAB11]] (IPCA duration) vs [[HGLG11]] (a FII) vs [[LFTS11]] (cash). Equities and IPCA duration share the rate-cycle path; the FII and cash each go their own way.*

## Portfolio implication

- Only floating-rate cash ([[LFTS11]]) and FIIs actually diversify the Brazil-rate-and-equity complex on a daily basis.
- Duration "fixed income" overlaps the equity book — size it as a rate bet, not as a hedge.
- Inside equities, dial domestic-rate beta up (utilities, fuel) or down (global/defensive) deliberately; it is the same Selic factor either way.

## Related

- [[Brazilian fixed-income ETFs]] — the duration spectrum
- [[FII]] — the off-factor income sleeve
- [[Brazilian fixed income]] — the broader instrument menu
- [[EWZ]] — Brazil equity benchmark
- [[Brazil]] — Selic / macro backdrop
