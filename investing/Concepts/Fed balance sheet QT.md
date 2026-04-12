---
aliases: [quantitative tightening, SOMA runoff, Fed SOMA Treasuries, Treasuries held outright, TREAST]
tags: [concept, macro, monetary-policy, treasuries, indicator]
---

# Fed balance sheet QT

Quantitative tightening (QT) is the [[Federal Reserve|Fed]]'s program of shrinking its Treasury and MBS holdings by letting securities roll off as they mature, rather than reinvesting the proceeds. It's the opposite of [[Quantitative easing|QE]]. The Fed's Treasury holdings are reported weekly in the H.4.1 release as SOMA (System Open Market Account) Treasuries held outright — FRED series [[TREAST]]. This is the single cleanest measure of Fed demand (or withdrawal) for US government debt.

---

## Synopsis

The Fed has run off $1.36T of Treasuries since peaking at $5.77T in June 2022 — a 24% reduction over ~3.5 years. The pace has decelerated: QT slowed in June 2024 (Treasury runoff cap lowered from $60B/mo to $25B/mo) and the program entered its terminal phase in early 2026, with the Fed holding at roughly $4.2-4.4T.

QT matters for Treasury market structure because every dollar the Fed runs off is a dollar the private market must absorb. When the Fed was the largest single holder, its net buying cushioned issuance volatility. Now the marginal buyer is the private sector — and within the private sector, [[Basis trade|leveraged hedge funds]] have taken on a disproportionate role (37% of net issuance 2022-2024 per NY Fed research, see [[Treasury International Capital]]).

The Tett thesis depends on this handoff. The Fed is shrinking (TREAST ↓), foreign official holders are trimming ([[NY Fed custody holdings|WMTSECL1]] ↓), and the replacement demand is price-sensitive leveraged funds. If basis-trade economics deteriorate, [[Scott Bessent|Bessent]]'s $10T rollover hits a buyer gap.

---

## Data structure

| Field | Detail |
|-------|--------|
| Source | [[Federal Reserve]] H.4.1 weekly release |
| Full name | "Factors Affecting Reserve Balances of Depository Institutions" |
| Release | Every Thursday, ~4:30 PM ET |
| FRED series | `TREAST` (Treasuries held outright, Wednesday level) |
| Related series | `WSHOMCB` (MBS held outright), `WSHONBNL` (Treasury notes & bonds only, nominal) |
| URL | https://www.federalreserve.gov/releases/h41/current/ |
| Units | Millions of dollars, weekly |

---

## Historical levels

| Date | TREAST | Event |
|------|--------|-------|
| Pre-COVID (Feb 2020) | ~$2.45T | Normal QE balance |
| Jun 2022 | $5.77T | QT start, balance sheet peak |
| Jan 2023 | $5.46T | $60B/mo runoff pace |
| Jan 2024 | $4.75T | Full pace ($60B Treasury cap) |
| Jun 2024 | ~$4.55T | QT taper — cap lowered to $25B |
| Jan 2025 | $4.29T | Slower runoff |
| Jan 2026 | $4.24T | Near-terminal pace |
| Apr 2026 | $4.41T | Current (some reinvestment noise) |

Total runoff: -$1.36T from peak (-23.6%).

![[treast-fed-soma-treasuries.png]]
*Fed SOMA Treasuries held outright (TREAST), 2010-2026. Peak $5.77T in June 2022; current $4.41T. The deceleration after mid-2024 reflects the June 2024 taper decision halving the Treasury runoff cap. Source: Fed H.4.1 / FRED.*

---

## QT pace and the taper decision

The original June 2022 QT plan set runoff caps at $60B/month for Treasuries and $35B/month for agency MBS. In June 2024 the [[FOMC]] halved the Treasury cap to $25B/month (MBS cap unchanged), citing funding market signals and a desire to slow the draining of bank reserves. The practical effect: the last ~24 months of QT have removed substantially less Treasury supply from the market than the first 24 months.

The slowdown decision matters for the Tett thesis in two ways. First, it signals the Fed is sensitive to private-market absorption capacity — which is the very fragility hedge fund absorption exposes. Second, it means the Treasury market has been getting supply relief from the Fed side even as foreign central banks have been trimming — partially masking the compositional shift in private demand.

---

## Why QT is a Treasury demand indicator

When analysts talk about Treasury demand, they often focus on foreign buyers (TIC, custody data) and domestic private buyers (banks, funds, households, hedge funds). The Fed is implicitly treated as the residual. But QT inverts that logic — every dollar of runoff is a dollar of *negative* Fed demand, transferred to the private market.

Combined with net Treasury issuance:
- Fed balance sheet running off: ~$300-400B/year Treasury supply returned to market
- Net new issuance: ~$2T/year for deficit financing
- Private market total absorption need: ~$2.3-2.4T/year

Against this backdrop, [[Basis trade|leveraged hedge fund]] absorption of 37% of net notes/bonds issuance (2022-2024) covers ~$700-800B/year — a structural share that didn't exist pre-QE. The hedge fund role exists because QT created the demand vacuum.

See [[Basis trade]], [[Treasury International Capital]].

---

## Relationship to reserve balances

QT is ultimately constrained by bank reserves. The Fed watches:
- Reserve balances (WRESCRT, ~$3.0T currently)
- Overnight reverse repo usage ([[ON RRP]]; RRPONTSYD, ~$150B currently)
- [[SOFR]] and fed funds printing behavior

If reserves approach "ample" threshold (~$3T), the Fed must stop QT to avoid funding market stress — the 2019 repo crisis precedent. The June 2024 taper was partly motivated by early signs of funding market tightness.

Current path: QT likely ends in 2026 as reserves approach target. From that point, the Fed's balance sheet stops shrinking and new Treasury issuance must be absorbed entirely by the private market.

---

## Connections

QT, foreign custody, TGA, and TIC composition together form a Treasury market structure dashboard. Each answers a different question:

| Series | Question |
|--------|----------|
| `TREAST` (this note) | How fast is the Fed withdrawing? |
| [[NY Fed custody holdings\|WMTSECL1]] | Are foreign CBs staying or leaving? |
| [[Treasury General Account\|WTREGEN]] | How much cash does Treasury have before forced issuance? |
| TIC holdings by country | Who's filling the gap — stable or leveraged? |

The vault dashboard on page 68 of the sandbox shows all four.

---

## Related

- [[Federal Reserve]] — SOMA portfolio manager, H.4.1 publisher
- [[Quantitative easing]] — the counterpart policy
- [[NY Fed custody holdings]] — foreign official demand signal
- [[Treasury General Account]] — Treasury cash dynamics
- [[Treasury International Capital]] — who's filling the demand gap
- [[Basis trade]] — the private-market demand channel that scaled with QE/QT
- [[Scott Bessent]] — $10T rollover facing post-QT market
- [[ON RRP]] — related plumbing indicator
- [[SOFR]] — funding market stress signal
