---
aliases: [century bond, 100-year bond, century bonds]
---
#concept #fixed-income

**Century Bond** — A bond with a 100-year maturity. Extremely rare for corporates due to business model obsolescence risk over such a timeframe.

---

## Why century bonds matter

Century bonds sit at the extreme end of the duration spectrum. They appeal to issuers who want to lock in rates for a lifetime and to investors (pensions, insurers) who need long-duration assets to match liabilities.

| Feature | Detail |
|---------|--------|
| Maturity | 100 years |
| Primary issuers | Sovereigns, universities, utilities, railroads |
| Investor base | Pension funds, insurance companies, sovereign wealth funds |
| Key risk | Issuer may not exist in 100 years |
| Duration sensitivity | Extreme — small rate changes produce large price swings |

---

## Corporate century bonds

Corporates rarely issue century bonds because acquisitions, technological disruption, and business model shifts make 100-year credit assessment nearly impossible.

| Issuer | Year | Coupon | Outcome |
|--------|------|--------|---------|
| [[Disney]] | 1993 | ~7.55% | Still outstanding — "Sleeping Beauty bonds" |
| Coca-Cola | 1993 | ~7.45% | Still outstanding |
| [[Motorola]] | 1997 | — | Issuer declined — top-25 company at issuance, now 232nd by market cap |
| J.C. Penney | 1997 | — | Bankrupt 2020 — just 23 years into a century bond |
| [[IBM]] | 2011 | ~5.6% | Still outstanding |
| Norfolk Southern | 2010 | — | Still outstanding (railroad = century-scale asset base) |
| **[[Google\|Alphabet]]** | **2026** | TBD | Sterling-denominated, first tech century bond since Motorola 1997 |

Railroads and consumer staples survive; tech and retail are higher risk. The J.C. Penney bankruptcy 23 years in is the cautionary case.

---

## Sterling century bond market

The sterling century bond market is especially small — only three issuers before Alphabet:

| Issuer | Year | Type |
|--------|------|------|
| University of Oxford | 2017 | Academic institution |
| EDF | — | French state-backed utility |
| Wellcome Trust | 2018 | Charitable foundation |

Alphabet's planned sterling century bond (Feb 2026) is the first corporate entry and the first tech issuer ever in this market.

---

## Why tech companies avoid them

| Risk | Explanation |
|------|-------------|
| Business model obsolescence | No tech company has maintained dominance for 100 years — the industry is ~75 years old |
| Acquisition risk | Tech companies get acquired, merged, or restructured frequently |
| Regulatory risk | Antitrust, regulation can reshape tech markets over decades |
| Historical precedent | [[Motorola]] was America's most valuable brand in 1997; within a decade [[Nokia]] then [[Apple]] destroyed its relevance |

[[Michael Burry]] flagged this pattern explicitly when Alphabet announced its century bond in Feb 2026 — comparing it to Motorola's issuance at the peak of its influence.

---

## Embedded options on century bonds

Century bonds carry standard IG embedded options, but the extreme maturity makes them behave differently:

| Feature | Standard long bond | Century bond |
|---------|-------------------|--------------|
| Make-whole call | Moderately expensive | Essentially worthless to issuer at issuance — NPV of 100 years of coupons is prohibitive |
| Par call date | 3-6 months before maturity | Critical question — if set at year 30-40, the century bond is really a callable long bond |
| Duration sensitivity | High | Extreme — small rate changes produce outsized price moves |
| Investor option value | Minimal | Zero (no put provisions in standard IG) |

The par call date is the key embedded option on a century bond. If [[Google|Alphabet]] sets a par call at year 30, investors bear 100 years of credit risk but only get guaranteed duration through year 30. After that, if rates fall, Alphabet calls at par and investors face reinvestment risk. If rates rise, Alphabet lets the bond run and investors hold an underwater position for decades.

This asymmetry means century bond investors are short a call option — they receive a higher coupon than a 30-year bond as compensation, but the option-adjusted spread (OAS) may be tighter than the nominal spread suggests. The Alphabet sterling century bond terms (including par call date) are not yet public — prospectus expected after pricing (~Feb 10).

---

## Related

- [[Google]] — $20B USD bond sale + sterling century bond (Feb 2026)
- [[Motorola]] — 1997 century bond, cautionary precedent
- [[Michael Burry]] — warned Alphabet century bond mirrors Motorola decline
- [[Morgan Stanley]] — estimates $400B hyperscaler bond issuance in 2026
- [[Oracle]] — $25B bond sale (Jan 2026), part of hyperscaler debt wave
