---
aliases: [SBC, stock-based comp, stock compensation, equity compensation]
tags:
  - concept
  - accounting
  - valuation
---

# Stock-based compensation

#concept #accounting #valuation

**Stock-based compensation (SBC)** — non-cash expense where companies pay employees with equity (stock options, RSUs) instead of cash. Ubiquitous in tech. Matters for investors because it dilutes existing shareholders and is excluded from [[Free cash flow]], inflating the metric that drives most valuations.

---

## Mechanics

1. **Company grants RSUs/options** to employees as part of compensation
2. **New shares are issued** when they vest → dilutes existing shareholders
3. **Company buys back shares** to offset dilution → costs real cash
4. **SBC is excluded from FCF** because it's a "non-cash" expense under GAAP

The paradox: SBC is "non-cash" on the income statement, but requires cash buybacks to prevent dilution. The cash cost is real — it just shows up in a different line item (financing activities, not operations).

---

## The FCF debate

**Standard FCF formula:**
```
FCF = Operating Cash Flow − Capex
```

SBC is added back to operating cash flow (non-cash item), so FCF looks higher than it would if employees were paid in cash.

**Adjusted FCF (SBC-inclusive):**
```
Adjusted FCF = Operating Cash Flow − Capex − SBC
```

**Why it matters:** A company with $40B FCF and $20B SBC has very different economics than one with $40B FCF and $2B SBC, even though both report the same headline FCF.

### Three schools of thought

| Approach | Treatment | Used by |
|----------|-----------|---------|
| **Ignore SBC** | Use reported FCF as-is | Most sell-side, momentum investors |
| **Subtract SBC from FCF** | Treat SBC as a cash-equivalent expense | Buffett, value investors, some buyside |
| **Use diluted share count** | Don't adjust FCF, but value on fully diluted basis | Middle ground approach |

**Buffett's view:** "If options aren't a form of compensation, what are they? If compensation isn't an expense, what is it? And if expenses shouldn't go into the calculation of earnings, where in the world should they go?"

---

## The buyback treadmill

Companies issue shares via SBC → must buy them back to prevent dilution → buybacks "sterilize" SBC but consume real cash.

**The trap:** Investors see headline buyback numbers and assume shareholder-friendly capital return. In reality, a large % of buybacks merely offset SBC dilution — shareholders aren't getting richer, they're staying even.

### Sterilization ratio

```
Sterilization ratio = Buyback $ used to offset SBC / Total buyback $
```

Higher ratio = more buybacks wasted on treading water vs. actual share count reduction.

---

## Meta case study

[[Meta]] is the poster child for the SBC debate in Big Tech.

### SBC trajectory

| Year | SBC Expense | Revenue | SBC as % Revenue |
|------|-------------|---------|------------------|
| 2021 | $9.2B | $118.0B | 7.8% |
| 2022 | $11.6B | $116.6B | 9.9% |
| 2023 | $14.0B | $134.9B | 10.4% |
| 2024 | $16.7B | $164.5B | 10.1% |
| 2025 | $20.4B | $200.9B | 10.2% |

*Source: MacroTrends, company filings*

### Buyback sterilization (10-year view)

| Metric | Value |
|--------|-------|
| Total buybacks (2017-2025) | ~$148B |
| Share count reduction | Only 3.9% |
| Sterilization rate | **82%** of buybacks offset SBC |
| FCF consumed by sterilization | ~64% over period |

Only 18% of $148B in buybacks actually reduced the float. The rest just offset dilution.

### The TikTok math (why it's wrong)

A viral TikTok (Feb 2026) claimed Meta's "real" FCF drops from $43.6B to $1.6B after subtracting $42B in SBC. The math is flawed:

1. **SBC was ~$20B, not $42B.** The video inflated the number by ~2×
2. **Double-counting.** If you subtract SBC from FCF, you can't also count the buyback cash spent to offset that same SBC. The cost is already reflected in lower net cash
3. **"1,000× FCF" is nonsensical.** Even using adjusted FCF ($43.6B − $20.4B = ~$23.2B), Meta trades at ~70× adjusted FCF — expensive but not absurd

**What IS fair criticism:**
- 82% buyback sterilization is genuinely high
- SBC as ~10% of revenue is a real cost investors should adjust for
- The gap between reported FCF and SBC-adjusted FCF is material (~$20B)
- Off-balance-sheet obligations (Hyperion SPV) add further complexity. See [[Meta]] debt profile

---

## Big Tech SBC comparison

| Company | 2024 SBC | Revenue | SBC % Rev | Buyback sterilization |
|---------|----------|---------|-----------|----------------------|
| [[Meta]] | $16.7B | $164.5B | 10.1% | ~82% (10yr) |
| [[Google\|Alphabet]] | ~$22B | $350B | ~6.3% | ~50-60% |
| [[Microsoft]] | ~$10B | $245B | ~4.1% | ~30-40% |
| [[Apple]] | ~$11B | $391B | ~2.8% | ~5-10% |

Apple is the gold standard — buybacks massively exceed SBC, so shareholders actually benefit. Meta is the worst among Mag 7 for sterilization.

---

## How to adjust valuations

### Method 1: SBC-adjusted FCF yield

```
Adjusted FCF = Reported FCF − SBC
Adjusted FCF yield = Adjusted FCF / Market cap
```

### Method 2: Fully diluted EV/FCF

Use fully diluted share count (including unvested RSUs and in-the-money options) in the denominator.

### Method 3: Treat SBC as capex

Add SBC to capex in the FCF formula. Conceptually treats equity compensation as an investment in human capital.

---

## Why companies love SBC

| Benefit | Detail |
|---------|--------|
| **Cash preservation** | Pay employees without cash outflow |
| **Alignment** | Employees care about stock price |
| **Tax deduction** | Companies deduct SBC at exercise/vesting (usually higher than grant-date value) |
| **FCF optics** | Inflates the headline metric investors watch |
| **Retention** | Vesting schedules create golden handcuffs |

---

## Risks and criticisms

| Issue | Detail |
|-------|--------|
| **Dilution** | Shareholders lose ownership without cash return |
| **Buyback treadmill** | Cash wasted maintaining share count, not growing it |
| **Moral hazard** | Employees prefer SBC → pushes companies toward equity-heavy comp |
| **Market cap circularity** | Higher stock price → SBC worth more → need more buybacks → less real cash for shareholders |
| **Cuts signal distress** | When companies cut SBC (as [[Meta]] did 5% in 2025, 10% in 2024), employees may leave for competitors |

---

## Related

- [[Meta]] — poster child for SBC/buyback dynamics
- [[Free cash flow]] — SBC excluded from standard FCF
- [[Apple]] — gold standard for buyback efficiency (low sterilization)
- [[Google]] — high absolute SBC but lower % of revenue
- [[Microsoft]] — moderate SBC, efficient buybacks

---

Sources:
- Taylor Morgan Capital, "Apple vs. Meta: 10 Years of Buybacks & Sterilization of SBC" (2025)
- TDM Growth Partners, "SBC Dilution Benchmarking — 2024 Update" (2025)
- MacroTrends — Meta SBC data
- mannhowie.com, "How to treat stock compensation when valuing companies?"
- Warren Buffett, 2002 Berkshire Hathaway annual letter

*Created 2026-02-26*
