---
aliases: [hyperscaler debt, tech bond issuance, hyperscaler bonds, AI bond wave]
---
#concept #fixed-income #ai

**Hyperscaler bond issuance** — The wave of corporate debt issuance by [[AI hyperscalers]] to fund AI infrastructure capex that is exceeding free cash flow. Emerged as a distinct pattern in 2025, accelerating sharply in 2026 as the Big 4 capex envelope moved toward roughly $725B and free cash flow compressed.

---

## Why this matters

AI capex is now outpacing cash generation at most hyperscalers, forcing them into debt markets at scale. This creates a structural shift — tech companies that were historically net-cash are becoming leveraged borrowers.

| Company | 2026 capex | Cash from ops (est.) | Gap | LT debt |
|---------|-----------|----------------------|-----|---------|
| [[Amazon]] | $200B | $180B | -$20B | Filing signals raise |
| [[Google\|Alphabet]] | $185B | $195B | +$10B (pre-buybacks) | $46.5B (4x in 2025) |
| [[Meta]] | $135B | $130B | -$5B | $60B+ (Blue Owl SPV) |
| [[Microsoft]] | ~$80B | ~$95B | +$15B | Most resilient (BNP) |
| [[Oracle]] | ~$25B+ | — | — | $93B total debt |

---

## Deal tracker (2025-2026)

### Corporate bond sales

| Date | Issuer | Amount | Demand | Key detail |
|------|--------|--------|--------|------------|
| Oct 2025 | [[Meta]] | $30B | $125B (4x) | 6-part (5-40yr), part of $60B Blue Owl Hyperion |
| Nov 2025 | [[Google\|Alphabet]] | $17.5B | ~$90B | Prior USD sale |
| Feb 3, 2026 | [[Oracle]] | $25B | — | Single-day record |
| **Feb 9, 2026** | **[[Google\|Alphabet]]** | **$20B** | **$100B+** | **7 tranches, longest 2066 at ~95 bps. Largest tech bond offering in history** |
| Feb 10, 2026 (est.) | [[Google\|Alphabet]] | TBD | — | Sterling debut incl. [[Century Bond]] + Swiss franc debut |
| TBD | [[Amazon]] | TBD | — | Filed regulatory notice signaling capital raise |
| May 2026 | [[Google\|Alphabet]] | ~€9B + C$9.5B | — | Euro and Canadian-dollar senior notes after Q1 debt proceeds of $31.4B |

### Alphabet Feb 9 USD tranches (detail)

| Tranche | Amount | Coupon | Maturity | Spread |
|---------|--------|--------|----------|--------|
| 3-year | $2.5B | 3.700% | 2029 | T+27 |
| 5-year | $3.0B | 4.100% | 2031 | — |
| 7-year | $3.0B | 4.400% | 2033 | — |
| 10-year | $4.25B | 4.800% | 2036 | — |
| 20-year | $1.5B | 5.500% | 2046 | — |
| 30-year | $4.0B | 5.650% | 2056 | — |
| 40-year | $1.75B | 5.750% | 2066 | ~T+95 (from ~T+120) |

### Embedded options

Standard IG make-whole call expected across all hyperscaler deals (confirmed in prior Alphabet, Meta, Oracle prospectuses):

| Feature | Detail |
|---------|--------|
| Make-whole call | Redeemable at any time at greater of par or NPV of remaining coupons (Treasury + spread) |
| Par call date | Typically 3-6 months before maturity — after which issuer redeems at 100% |
| Sinking fund | None |
| Tax call | Par redemption if withholding obligations arise |

For the sterling [[Century Bond]], the par call date is the key embedded option question. If set at year 30-40, the century bond effectively becomes a callable long bond — investors bear full duration risk without guaranteed duration reward. The make-whole call itself is essentially worthless to the issuer at issuance (too expensive to exercise on a 5.75%+ coupon in a ~4.5% rate environment).

424B2 for the Feb 2026 USD deal expected after close (Feb 13). Sterling prospectus not yet available.

### Structured / project finance

See [[AI infrastructure deals]] for SPV and [[GPU-as-collateral]] structures ([[xAI]] $20B, [[CoreWeave]] $18B, Crusoe-[[OpenAI]] $15B, [[BlackRock]] AIP $100B target).

---

## Scale of the wave

| Metric | Value | Source |
|--------|-------|--------|
| Hyperscaler bonds issued (2025) | $121B | BofA Securities (5 names: AMZN, GOOG, META, MSFT, ORCL) |
| Hyperscaler bonds forecast (2026) | **$400B** | [[Morgan Stanley]] |
| Total IG issuance forecast (2026) | **$2.25T** (record) | [[Morgan Stanley]] |
| Global bond issuance pace (Feb 2026) | Hit $1T in record time | Bloomberg |
| High-grade inflows (week of Feb 4) | $6.44B | 5-year high |
| TD Securities expected IG (week of Feb 10) | $80B | 2x normal pace |

The $400B hyperscaler forecast represents a 2.4x increase from 2025. If realized, hyperscaler debt alone would account for ~18% of total US IG issuance.

---

## May 2026 cash-return break

The May 8 FT / [[Visible Alpha]] capex pass makes the debt wave easier to explain: capex is no longer comfortably funded by post-dividend surplus cash. [[Alphabet]] reported no Q1 2026 Class A/C repurchases and $31.4B of debt proceeds; [[Meta]] reported no Q1 repurchases and $59.0B of senior notes outstanding; [[Amazon]] said Q1 2026 financing inflows rose to $52.8B and that it expects additional financing activity in 2026.

This does not mean every hyperscaler is credit-stressed. [[Microsoft]] remains the cleanest balance sheet and can fund more internally than peers. The structural change is that shareholder-return policy, bond issuance, and AI infrastructure capacity are now one integrated capital-allocation decision.

*Sources: [FT article](https://www.ft.com/content/b3dfaba9-17a2-4fac-90fe-4ab3ca7c9494), May 8 2026; [Alphabet Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm); [Meta Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm); [Amazon Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/amzn-20260331.htm).*

---

## Spread dynamics

Spreads remain historically tight despite the supply surge — demand is absorbing the flood:

| Deal | Initial guidance | Final pricing | Tightening |
|------|-----------------|---------------|------------|
| Alphabet 2066 tranche | ~120 bps over Treasuries | ~95 bps | -25 bps |
| [[Meta]] 40-year tranche | — | T+110 | — |
| IG OAS (Feb 5) | — | 76 bps | Near cycle lows |

New issues underperformed JPMorgan US Liquid Index by 4 bps over the 10 days prior to Feb 7 — the largest underperformance since October. Early sign of indigestion.

---

## Skeptics

| Voice | Argument |
|-------|----------|
| [[Michael Burry]] | Alphabet [[Century Bond]] mirrors [[Motorola]] 1997 — tech dominance is fragile over 100 years |
| [[Richard Bernstein Advisors]] | "Everything bubble" — AI credit risk creates asymmetric downside for bondholders |
| Alexander Morris (F/m Investments) | "Leaves little upside and even less room for error" |
| Ali Meli (Monachil Capital) | "It doesn't take too many adverse events to create a selloff" |
| [[BNP Paribas]] | FCF at Oracle, Alphabet, Amazon, Meta "plummeting toward negative territory" |

The bull case: hyperscalers have unmatched revenue bases ($400B+ for Alphabet), massive cash generation, and AI spending is creating durable competitive moats. The bear case: credit investors bear downside risk without AI upside, and 40-year bonds on 5-10 year tech cycles is a fundamental mismatch.

---

## Software credit contagion (Feb 2026)

AI disruption is hitting credit markets beyond issuers — software leveraged loans fell 4% YTD through Feb 6. BDC equity index dropped 4.6% in the week of Feb 3. Average BDC software exposure exceeds 20% of portfolios ([[Barclays]]). See [[Credit markets]] for details.

---

## Quick stats

| Metric | Value |
|--------|-------|
| 2025 hyperscaler issuance | $121B (BofA) |
| 2026 forecast | $400B (Morgan Stanley) |
| Largest single deal | Alphabet $20B (Feb 9, 2026) |
| Longest tech maturity | Alphabet 100-year sterling (Feb 2026) |
| IG spread (Feb 2026) | ~76 bps (near cycle low) |

*Created 2026-02-09*

---

## Related

- [[Credit markets]] — broader IG/HY context, spread chart, RBA positioning
- [[AI infrastructure deals]] — SPV and project finance structures
- [[Century Bond]] — Alphabet 100-year sterling bond, historical precedents
- [[Hyperscaler capex]] — the spending driving the debt wave
- [[AI infrastructure financing]] — overview of financing mechanisms
- [[Google]] — $20B USD + sterling century bond (Feb 2026)
- [[Oracle]] — $25B single-day sale (Feb 2026)
- [[Meta]] — $30B corporate + $60B Blue Owl SPV (Oct 2025)
- [[Amazon]] — signaling capital raise
- [[Microsoft]] — most resilient FCF position
- [[Morgan Stanley]] — $400B issuance forecast
- [[Michael Burry]] — century bond skeptic
- [[Richard Bernstein Advisors]] — "everything bubble" call on credit
- [[Investment grade bonds]] — asset class context
