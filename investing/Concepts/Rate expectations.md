---
aliases: [Fed rate expectations, rate path, implied rate path, fed funds futures, FedWatch]
---
#concept #rates #macro #fed

**Rate expectations** — What the futures market prices for the path of the [[Federal Reserve]]'s policy rate. Derived from Fed Funds futures (ZQ) and [[SOFR]] futures (SR3) on the [[CME Group|CME]]. The market's real-time bet on how many cuts or hikes are coming, and when.

---

## Synthesis

As of Mar 2026, the market prices a slow, shallow easing cycle — ~57bp over 21 months to a terminal rate around 3.07%. No single FOMC meeting commands >50% cut probability. This is a "grudging grind" narrative: the Fed will ease, but only because the economy softens enough to justify it, not because inflation is beaten or the Fed wants to get ahead of a downturn. The lack of front-loading distinguishes this from Dec 2023's pivot repricing, when the market briefly priced 6+ cuts. The SR3 curve turning upward past 2027 suggests term premium is reasserting — the market doesn't believe the terminal rate is permanently low. Key risk: if tariff-driven inflation reignites (see [[2026 Iran conflict market impact]], [[Inflation expectations]]), the entire curve reprices higher and the ~2 cuts evaporate.

---

## Current implied path

![[fed-rate-expectations.png]]
*Fed Funds futures (ZQ, monthly) + 3M SOFR futures (SR3, quarterly). Updated via `fed_rate_expectations.py`.*

| Metric | Value |
|--------|-------|
| Current target range | 3.50%–3.75% |
| Current effective rate | 3.64% |
| Implied terminal rate | ~3.07% (Dec 2027) |
| Total implied easing | ~57bp (~2.3 cuts of 25bp) |
| Curve shape | Gradual, not front-loaded |

### Key contract months

| Contract | Month | Implied Rate | Change from now |
|----------|-------|-------------|-----------------|
| ZQH26 | Mar 2026 | 3.640% | — |
| ZQM26 | Jun 2026 | 3.560% | -8bp |
| ZQU26 | Sep 2026 | 3.395% | -25bp |
| ZQZ26 | Dec 2026 | 3.235% | -41bp |
| ZQM27 | Jun 2027 | 3.145% | -50bp |
| ZQZ27 | Dec 2027 | 3.065% | -58bp |

---

## FOMC meeting probabilities

![[fed-fomc-probabilities.png|697]]
*Implied probability of a 25bp cut at each FOMC meeting. Approximation — ZQ contracts reflect month-average rates, not precise post-meeting levels. CME FedWatch uses intra-month weighting for higher precision.*

No single meeting currently prices >50% probability of a cut. The highest is Jul 29, 2026 at ~28%. Easing is distributed across many meetings — the market sees a slow grind lower, not a decisive pivot.

---

## How it works

Fed Funds futures (ZQ) settle at the monthly average effective fed funds rate. Price = 100 minus implied rate. A ZQ contract at 96.36 implies a 3.64% average rate for that month. Available monthly, ~21 months forward.

[[SOFR]] futures (SR3) — 3-month SOFR rate contracts. Same math (100 minus price). Extend further out (~2+ years) but represent the secured overnight rate rather than the fed funds rate. The two track closely because SOFR sits near the bottom of the fed funds target range.

Meeting-level probabilities — if the ZQ contract *before* an FOMC meeting implies rate X, and the contract *after* implies rate Y, the drop (X - Y) divided by 0.25 gives the probability of a 25bp cut. This is a simplification — true [[CME Group|CME FedWatch]] methodology weights by the number of days before/after the meeting within the month.

---

## Interpretation

The curve tells you what's priced. When the implied path diverges from Fed dot plots or economic data, that's where the trade is:

- Curve steeper than dots — market more dovish than Fed. If the Fed delivers, rates positions rally. If Fed pushes back, short-end sells off. See [[Steepener trade]].
- Curve flatter than dots — market sees fewer cuts than Fed projects. Usually means inflation sticky or economy resilient.
- Front-end flat, back-end steep — no imminent cuts priced, but eventual easing expected. Current shape (Mar 2026).
- Sharp step between months — a specific FOMC meeting is expected to deliver.

---

## Tooling

```bash
# Snapshot: implied rate path chart + table
python scripts/fed_rate_expectations.py

# FOMC meeting probabilities
python scripts/fed_rate_expectations.py --mode fomc

# How a specific contract's implied rate has shifted over time
python scripts/fed_rate_expectations.py --mode history --history-contract ZQZ26.CBT

# Table only (no chart)
python scripts/fed_rate_expectations.py --table --no-chart
```

Data source: [[CME Group|CME]] via yfinance. ZQ contracts on CBOT, SR3 on CME. Updated on demand — not stored in the database.

---

## Related

- [[Federal Reserve]] — the institution setting the rate
- [[Jerome Powell]] — current Fed chair
- [[SOFR]] — secured overnight rate, closely tracks effective fed funds
- [[Steepener trade]] — directional bet on the yield curve shape
- [[Inflation expectations]] — the other side of the dual mandate
- [[Treasuries]] — rates flow through to all duration assets
- [[Fed pivot December 2023]] — last major repricing of the rate path
- [[Fed independence]] — political risk to the rate-setting process
- [[CME Group]] — exchange where these futures trade
