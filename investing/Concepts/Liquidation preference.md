---
aliases: [Liquidation pref, Liq pref]
---
#concept #venturecapital #privateequity

Liquidation preference — contractual right giving preferred shareholders priority over common shareholders in a liquidity event (IPO, acquisition, wind-down). Determines who gets paid first and how much.

---

## How it works

In a liquidity event, proceeds are distributed in order:
1. Debt holders (secured, then unsecured)
2. Preferred shareholders (by seniority — latest series first)
3. Common shareholders (founders, employees)

If proceeds run out before reaching a tier, lower tiers get nothing.

---

## Key parameters

| Parameter | Options | Effect |
|-----------|---------|--------|
| Multiple | 1x, 2x, 3x | How many times the original investment is returned before common gets paid. 1x = get your money back. 2x = get double. |
| Participation | Participating / non-participating | Whether preferred holders double-dip (see below) |
| Seniority | Standard / pari passu | Whether later series get paid before earlier ones, or all preferred is treated equally |
| Cap | Capped / uncapped | For participating preferred, a ceiling on total return before converting to common |

---

## Participating vs non-participating

Non-participating (investor-friendly, simpler):
- Investor chooses: take the liquidation preference OR convert to common and take pro-rata share
- Cannot do both
- Standard in late-stage / founder-friendly deals
- [[SpaceX]]: all series are 1x non-participating

Participating (investor-friendly, more aggressive):
- Investor gets their liquidation preference AND their pro-rata share of remaining proceeds
- "Double-dipping" — get money back first, then share in the upside too
- Common in early-stage deals where investors take more risk
- Sometimes capped (e.g., 3x cap = participation stops at 3x return)

---

## Seniority stack

Standard seniority: later rounds get paid first.

Example using [[SpaceX]] cap table:

| Priority | Series | Issue price |
|----------|--------|-------------|
| 1st | Series N | $270.00 |
| 2nd | Series M | $220.00 |
| 3rd | Series L | $214.00 |
| ... | ... | ... |
| Last | Series E | $4.50 |
| After all preferred | Common | — |

In a down exit, later investors (who paid more) recover first. Early investors and common may get wiped out.

Pari passu: all preferred series share pro-rata regardless of when they invested. Less common.

---

## When it matters (and when it doesn't)

Matters in down exits:
- Company sells for less than total capital raised
- Preference stack determines who recovers and who gets wiped
- 2x or 3x multiples can consume all proceeds, leaving common with nothing

Irrelevant in up exits:
- When exit valuation far exceeds invested capital, every preferred holder converts to common and takes pro-rata
- Their equity stake is worth more than the preference payout
- [[SpaceX]] at $800B+ vs ~$12B raised: preferences are meaningless — everyone converts

---

## Red flags

- Stacked 2x+ participating preferred across multiple rounds: founders and employees can get zeroed even in a decent exit
- "Ratchet" provisions: anti-dilution that adjusts conversion ratios in down rounds, further diluting common
- Accumulated dividends on preferred: adds to the preference stack over time

---

## Related

- [[SpaceX]] — 10 preferred series, all 1x non-participating
- [[Rule 22e-4]] — SEC liquidity rule affecting how funds value preferred shares
- [[Dual-class shares]] — related control mechanism (voting vs economic rights)
