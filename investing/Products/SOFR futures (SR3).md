---
aliases: [SOFR futures, SR3, SR3 futures, 3M SOFR futures, three-month SOFR futures]
tags: [product, instrument, futures, rates, cme, sofr]
---
#product #instrument #futures #rates #sofr

# SOFR futures (SR3)

3-month cash-settled futures contract on the [[SOFR|Secured Overnight Financing Rate]] (SOFR). Listed by [[CME Group|CME]] under symbol **SR3**, with one contract per delivery month going out roughly 10 years. The instrument that replaced 3-month Eurodollar futures (retired 2023) as the benchmark for medium-term US dollar rate expectations. Extends the [[Rate expectations]] curve out 2-3 years past where [[Fed Funds futures (ZQ)|ZQ]] coverage ends.

---

## Contract specifications

| Spec | Value |
|------|-------|
| Symbol root | SR3 |
| Listing | [[CME Group]] (CME Globex) |
| Underlying | 3-month compounded SOFR rate over the contract reference quarter |
| Contract size | $25 per basis point per contract (= $1M × 90/360 × 0.01) |
| Tick size | 0.005 (= $12.50 per tick) front months; 0.0025 for whites/reds |
| Settlement | Cash-settled to compounded SOFR rate over the IMM reference period |
| Delivery month codes | H M U Z (Mar, Jun, Sep, Dec — quarterly IMM dates) |
| Quote | 100 minus implied rate (e.g. 96.1550 → 3.8450%) |
| Listed depth | ~40 quarterly contracts (~10 years) |
| Predecessor | Eurodollar (ED) futures, retired Apr 2023 |
| First listing | May 2018 |
| Liquidity tier | Whites (year 1), Reds (year 2), Greens (year 3), Blues (year 4) |

---

## Price-to-rate identity

Same convention as [[Fed Funds futures (ZQ)|ZQ]] and the retired Eurodollar contract:

```
implied_rate (%) = 100 − futures_price
```

A SR3 contract trading at 96.1550 implies a 3.8450% compounded average SOFR rate over its 3-month reference period. The reference period for an IMM-dated contract begins on the third Wednesday of the contract month and ends on the third Wednesday of the next quarterly month.

---

## What "3-month compounded SOFR" means

SR3 settles to the daily compounded SOFR rate over the 3-month reference period, not a simple average. Each day's published SOFR rate compounds into the next, and the contract pays out the resulting annualized rate. Two implications:

1. Daily SOFR spikes (quarter-end repo stress, dealer balance-sheet constraints) flow through the compounding and into settlement. SR3 captures repo-market stress that [[Fed Funds futures (ZQ)|ZQ]] does not.
2. The contract is forward-looking from the perspective of any pre-reference-period quote: a SR3 contract listed today for a Sep 2026 reference period prices a 3-month rate that does not yet exist. Market pricing reflects forward expectations of the path of overnight SOFR, similar to how Eurodollar futures historically priced forward 3-month USD LIBOR.

---

## SOFR vs Fed Funds

[[SOFR]] is the volume-weighted median of overnight Treasury repo trades, published daily by the [[New York Fed]]. The Fed Funds effective rate is the volume-weighted median of overnight unsecured interbank loans of reserve balances. The two are anchored together by arbitrage (banks can borrow in either market) but can diverge:

| Source of divergence | Direction | Example |
|---------------------|-----------|---------|
| Repo stress | SOFR spikes above Fed Funds | Sept 17 2019 (SOFR ~5.25%, FF target 2.00-2.25%) |
| ON RRP demand | SOFR floored near ON RRP rate | 2021-2022 zero-rate era |
| IOR vs target range mid | Pushes Fed Funds toward IOR | Most normal regimes |
| Year-end / quarter-end | SOFR rises temporarily | Routine repo seasonal |

When the two diverge, SR3 prices the SOFR path and [[Fed Funds futures (ZQ)|ZQ]] prices the Fed Funds path — they are not interchangeable. Under normal repo conditions the gap is a few basis points and the SR3 / ZQ strip splice in the vault's `fed_rate_expectations.py` works cleanly.

---

## The Eurodollar transition

Eurodollar futures (ED) were the dominant USD short-rate futures contract for forty years, settling to 3-month USD LIBOR. The 2017 [[FCA]] LIBOR transition decision and the 2021 ICE LIBOR cessation forced the migration:

- 2022: CME started incentives for ED→SR3 conversion
- April 14 2023: Final ED contract settled
- 2023-2025: SR3 absorbed essentially all liquidity from the front 5 years of the ED strip
- Late 2024: SR3 average daily volume exceeded peak ED ADV

The transition went smoother than feared mainly because SR3 had been listed since 2018 with steady liquidity growth, so dealers and asset managers had migrated their hedging by the time ED retired. The structural shift it introduced: SOFR is a secured rate (repo-backed), where LIBOR was unsecured (panel bank credit). This means SR3 lacks the bank-credit risk premium that LIBOR carried — useful for clean rate pricing, but it means SR3 cannot be used to read bank credit conditions the way ED FRA-OIS could.

---

## Convexity bias

For long-dated SR3 contracts the futures-vs-forward bias is meaningful. A SR3 contract maturing in 8 years carries a small but non-zero convexity adjustment relative to the equivalent forward rate from the OIS swap curve. The adjustment is positive (futures-implied rate above the forward) and grows with maturity and the volatility of short rates.

This is the bias that OIS-curve construction strips out — the swap curve, not the futures strip, is the right input for derivative valuation. The vault's `fed_rate_expectations.py` does not correct for this, which is fine for "what is the strip pricing?" reads but not for trade construction at the long end.

---

## Where the vault uses SR3

- [[Rate expectations]] — extends the implied path chart past the ZQ horizon (~3 years), generates the longer-dated portion of `fed-rate-expectations.png`
- [[Fed Funds futures (ZQ)]] — the companion instrument for the front end
- [[Term premium]] — uses the SR3 strip as the expected short-rate input out to ~3 years before transitioning to OIS swap curve modeling for longer horizons
- [[SOFR]] — the underlying rate, with its own concept note

---

## Tooling

The vault's `fed_rate_expectations.py` downloads SR3 contracts after ZQ to build the full curve:

```python
def download_sr3_curve():
    """Download SR3 (3-month SOFR) futures for longer-dated expectations."""
    for yr in range(now.year, now.year + 3):
        for code in CODE_ORDER:
            sym = f"SR3{code}{yr_short:02d}.CME"
            ...
```

The script plots SR3 as a dashed orange line behind the solid blue ZQ strip. Only the quarterly IMM months exist for SR3 (H/M/U/Z), so the SR3 portion of the chart has fewer points than the ZQ portion (monthly) for any given time horizon.

---

## Related

- [[CME Group]] — listing exchange operator
- [[Fed Funds futures (ZQ)]] — companion instrument for front-end Fed Funds path
- [[SOFR]] — underlying rate
- [[Rate expectations]] — the concept consuming both ZQ and SR3
- [[Federal Reserve]] — the institution whose policy SOFR ultimately tracks
- [[New York Fed]] — publishes daily SOFR
- [[Term premium]] — short-rate expectations input
- [[Treasuries]] — duration assets pricing off the SOFR-derived short-rate path
- [[FCA]] — drove the LIBOR transition that created the SR3 migration window
