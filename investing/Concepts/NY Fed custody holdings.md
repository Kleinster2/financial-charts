---
aliases: [foreign official custody holdings, Fed custody holdings, H.4.1 custody data, foreign central bank Treasury holdings]
tags: [concept, macro, treasuries, indicator]
---

# NY Fed custody holdings

The [[Federal Reserve|NY Fed]] holds U.S. [[Treasuries]] and agency securities in custody for foreign central banks, monetary authorities, and international institutions. Over 200 account holders maintain 550+ accounts. The weekly data (H.4.1 report) is the highest-frequency public signal of foreign official demand for US government debt — and thus a real-time proxy for global dollar confidence.

---

## Synthesis

This indicator matters most during crises. When foreign central banks sell, the signal is not just reduced demand for Treasuries — it's that the global dollar system is under stress. Countries sell reserves to defend currencies, pay for oil, or plug fiscal gaps. The March 2026 selloff ($82B in one month) is the fastest drawdown since the March 2020 COVID panic, driven by the same combination: commodity shock + currency defense + fiscal need. The difference is scale — 2020 saw ~$270B over a quarter; the current pace would match that by May if sustained.

The connection to the [[Basis trade]] is the tail risk. Foreign CB selling depresses cash Treasury prices, widening the cash-futures basis, triggering margin calls on leveraged hedge fund positions (estimated $1-1.4T gross notional). Forced unwinds amplify the selling. March 2020 is the precedent — 10Y yield spiked ~60bp in two weeks before the Fed intervened with direct purchases. The [[FIMA Repo Facility]] was created specifically to give foreign CBs an alternative to dumping Treasuries on the open market.

---

## Data structure

| Field | Detail |
|-------|--------|
| Source | [[Federal Reserve]] H.4.1 release |
| Full name | "Factors Affecting Reserve Balances of Depository Institutions" |
| Release | Every Thursday, ~4:30 PM ET |
| FRED series | WMTSECL1 (Treasuries, Wednesday level), WSEFINTL1 (total), WFASECL1 (agency/MBS) |
| URL | https://www.federalreserve.gov/releases/h41/current/ |
| Location in report | Table 1A, "Memorandum Items" |

The H.4.1 shows both weekly averages and Wednesday snapshot levels. It covers only what is physically held at the NY Fed — total foreign holdings of Treasuries (~$8.5T per TIC data) are much larger, as many are held through other custodians.

Caveat: TIC data (monthly, 2-month lag) and H.4.1 custody data (weekly) measure different things. Declines in NY Fed custody may reflect transfers to other custodians rather than outright sales. But rapid weekly drops during crises are almost always real selling.

---

## Historical levels

| Date | Treasuries held | Event |
|------|----------------|-------|
| Dec 2002 | Series inception | — |
| Mar 2021 | ~$3.14T (record) | Post-COVID reserve accumulation |
| Mar 2025 | ~$2.91T | Pre-Iran war baseline |
| Feb 11, 2026 | $2.801T | Pre-Iran-conflict peak |
| Mar 25, 2026 | $2.694T | Initial Iran war drawdown, -$82B |
| Apr 8, 2026 | $2.693T | Latest, cumulative -$108B from Feb 11 |

Latest H.4.1 (week ending Apr 8, 2026):

| Category | Wednesday level | Change since Feb 11 |
|----------|----------------|---------------------|
| Treasuries (WMTSECL1) | $2.693T | -$108B |
| Total custody (Treasuries + MBS) | ~$2.98T | similar pace |

---

## Largest foreign holders (TIC data, Dec 2025)

| Country | Holdings | Notes |
|---------|----------|-------|
| [[Japan]] | $1,185B | Largest holder |
| [[United Kingdom]] | $866B | Includes custodial holdings for others |
| [[China]] | $684B | Down from ~$1.3T peak (Nov 2013) |

Belgium ($481B) and Luxembourg ($425B) are outsized because they serve as custodial locations for other countries including [[China]]. TIC tracks where bonds sit, not beneficial owners.

China's decline: $1.3T (Nov 2013) → $697B (Jul 2025, lowest since Oct 2008). Reductions of $173B (2022), $51B (2023), $57B (2024).

---

## March 2026 selloff — Iran war catalyst

Holdings dropped $82B from Feb 25 to late March 2026, the fastest drawdown since the March 2020 COVID panic.

Drivers:
- Currency defense: [[Turkey]] sold $22B in foreign government bonds from FX reserves since Feb 27 (see [[Robin J. Brooks]] Turkey crisis analysis — CB sold 50t gold, intervention at Mar 2025 crisis scale)
- Oil import financing: [[India]], Thailand, and other Asian oil importers liquidating reserves to pay surging crude costs
- Fiscal gap-filling: commodity importers subsidizing domestic fuel prices
- [[Eurozone]] inflation hit 2.5% in March — energy shock constraining [[ECB]] rate cuts, pushing European yields higher and competing for the same capital

*Source: FT exclusive (Mar 31, 2026), CNBC market recap (Mar 31, 2026)*

---

## Basis trade transmission channel

When foreign CBs sell large volumes of cash Treasuries:

1. Cash bond prices fall → basis (cash-futures spread) widens
2. Leveraged basis trade positions (~$1-1.4T gross notional, 10-20x leverage) face margin calls
3. Forced unwinds: hedge funds fire-sell cash Treasuries, scramble to cover short futures
4. Dealers have limited balance sheet to absorb flows
5. Self-reinforcing selloff

Precedent — March 2020: foreign investors sold ~$270-287B in Q1 2020. 10Y yield spiked ~60bp between Mar 9-23. Fed intervened with direct Treasury purchases on Mar 15 and 23 *"to support smooth functioning of markets."*

The [[FIMA Repo Facility]] (launched Mar 2020, made permanent Jul 2021) was specifically designed to give foreign CBs an alternative — borrow against Treasuries rather than selling them. Its usage in the current crisis is not yet public.

See [[Basis trade]], [[March 2020 liquidity crisis]]

---

## The TIC undercounting problem (NY Fed research, 2026)

NY Fed economists discovered that TIC data systematically undercounts cross-border hedge fund Treasury flows by ~$1.4T. Most leveraged funds are domiciled in the [[Cayman Islands]] for tax and regulatory reasons, but TIC reporting fails to capture the full scale of their positions. See [[Treasury International Capital]] for the dedicated concept note.

Correcting for this, the Cayman Islands — not [[Japan]] or [[China]] — is the largest foreign holder of US Treasuries. Between 2022 and 2024, hedge funds absorbed 37% of net notes/bonds issuance, nearly matching all other foreign investors combined (OFR data). Foreign ownership overall has dropped below 30% (from 46% in 2008), but the headline masks a compositional shift: demand has migrated from price-insensitive central banks to price-sensitive leveraged funds running [[Basis trade|basis]] and swap trades.

This reframes the custody data above. The $82B in central bank selling is real and concerning — but the deeper question is who is replacing that demand. If the answer is predominantly hedge funds running 10-20x leveraged spread trades, the Treasury market's "buyer of last resort" has moved from entities that hold through volatility (central banks) to entities that amplify it (hedge funds). [[Scott Bessent|Bessent]]'s $10T rollover next year depends on this fragile demand base persisting.

[[Kenneth Griffin]] of [[Citadel]] argues hedge fund demand is net positive — it softened the QE unwind and provides apolitical liquidity. The counterargument: March 2020, April 2025, and the early [[2026 Iran conflict market impact|Iran war]] all showed these positions unwind violently under stress, even if the thesis is correct.

*Source: NY Fed research, OFR, FT (Gillian Tett, Apr 3 2026)*

---

## Why it matters for the vault

The custody data connects three vault threads:

1. [[Iran conflict oil price timeline]] — the commodity shock forcing reserve drawdowns
2. [[Basis trade]] — the financial stability risk from forced unwinds
3. [[Treasuries]] — the structural demand picture for US government debt

The $288B YoY decline also intersects with the [[China]] dedollarization narrative (China down ~$600B from peak) and the broader question of whether the dollar's reserve currency status is eroding gradually or holding steady.

---

## Treasury market structure dashboard (four-lens framework)

WMTSECL1 is most informative read alongside three other weekly/monthly series. Each answers a different question about the Treasury market; together they triangulate the [[Gillian Tett]] thesis on compositional fragility.

| Lens | Series | What it answers |
|------|--------|-----------------|
| Foreign official demand | `WMTSECL1` (this note) | Are foreign central banks staying or leaving? |
| Fed demand | [[Fed balance sheet QT\|TREAST]] | How fast is the Fed withdrawing from the market? |
| Treasury runway | [[Treasury General Account\|WTREGEN]] | How much cash before forced issuance? |
| Private composition | [[Treasury International Capital\|TIC holdings]] | Who's replacing exiting demand — stable or leveraged? |

Current readings (Apr 8, 2026):
- WMTSECL1: $2.693T, -$108B since Feb 11 (CBs exiting)
- TREAST: $4.41T, -$1.36T from 2022 peak (Fed withdrawing via [[Fed balance sheet QT|QT]])
- WTREGEN: $748B (moderate buffer — [[Scott Bessent|Bessent]] has runway but limited flexibility)
- TIC composition: Cayman ($433B reported, ~$1.8T true) rising as Japan/China stagnate

The pattern: two of the three traditional "sticky" demand sources (Fed and foreign CBs) are retreating simultaneously. The gap has been filled by leveraged [[Basis trade|hedge fund]] demand (37% of net issuance 2022-2024 per NY Fed research) — price-sensitive buyers who will exit if spreads deteriorate. With the $10T rollover landing in 2027, the dashboard's message is that the margin for error is narrowing from multiple sides simultaneously.

This dashboard lives on page 68 of the sandbox workspace.

---

## Related

- [[Treasuries]] — the asset class
- [[Federal Reserve]] — custodian, H.4.1 publisher
- [[Fed balance sheet QT]] — parallel demand-side series in the same dashboard
- [[Treasury General Account]] — Treasury runway series in the same dashboard
- [[Treasury International Capital]] — ownership composition data
- [[Basis trade]] — transmission channel for financial instability
- [[March 2020 liquidity crisis]] — precedent for CB selling → basis trade unwind
- [[FIMA Repo Facility]] — backstop created to prevent forced Treasury sales
- [[Iran conflict oil price timeline]] — current crisis catalyst
- [[Iran conflict economic disruption]] — broader economic impact
- [[Turkey]] — $22B selling since Feb 27
- [[China]] — structural decline from $1.3T peak
- [[Robin J. Brooks]] — Turkey reserve analysis, financial stability concerns ("skeletons in the closet")
- [[Gillian Tett]] — compositional fragility thesis
