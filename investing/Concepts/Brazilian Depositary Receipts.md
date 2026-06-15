---
aliases: [BDR, BDRs, Brazilian Depositary Receipt, Brazilian Depositary Receipts, Recibo de ações estrangeiras, BDR Nível I]
tags: [concept, instrument, brazil, b3, cross-listing]
---

# Brazilian Depositary Receipts

A Brazilian Depositary Receipt (BDR) is a certificate issued by a Brazilian depositary institution that represents shares of a foreign-listed company and trades on [[B3]] in reais, letting a [[Brazil]]-resident investor hold a non-Brazilian equity without an offshore account or câmbio. It is the Brazilian member of the [[Depositary receipts|depositary-receipt]] family — the same instrument as the US [[American Depositary Receipts|ADR]], built on the same sponsored/unsponsored, multi-level template under Brazilian rules. The whole instrument splits along one axis that governs everything else: whether the foreign company sponsors the program. [[#Sponsorship and levels|Patrocinado (sponsored)]] BDRs run in three levels with the issuer's involvement and graduated [[CVM]] disclosure; [[#Sponsorship and levels|não-patrocinado (unsponsored)]] BDRs exist only as Level I, created by a depositary without the company's participation, and are the bulk of the US-stock receipts a retail investor sees. The ticker's last digits encode the type — [[#Sponsorship and levels|31 through 35]] — so the symbol itself tells you what you are holding. Since [[#Who can buy|2020]] the unsponsored Level I line is open to retail, not just qualified investors, which is why a name like [[SpaceX securities note|SPCX34]] can list on [[B3]] the same day as its [[Nasdaq]] debut. For an investor the decisions that matter are [[#Taxation for a Brazil resident|tax]] (no R$20k isenção) and [[#Synthesis|liquidity, voting, and currency]], not the legal plumbing.

## What a BDR is

A BDR is a receipt, not the share itself. A depositary institution in Brazil holds the underlying foreign shares in custody abroad and issues certificates against them that trade on [[B3]] and settle locally in reais. The receipt's economics track the underlying one-for-one, adjusted by two things: the paridade (how many BDRs equal one foreign share) and the USD/BRL rate. A holder gets economic exposure to the foreign company but, because the depositary is the registered shareholder, generally no voting rights in the underlying.

The paridade is set per program and is not always 1:1 — [[SpaceX securities note|SPCX34]] is 1:15, so fifteen BDRs represent one [[SpaceX]] Class A share, pricing each receipt near a fifteenth of the Nasdaq line. The ratio is a packaging choice to land the receipt in a retail-friendly per-unit price band, not a difference in underlying value.

## Sponsorship and levels

The classification is set by [[B3]] and the [[CVM]] and is legible directly from the ticker's final digit:

| Type | Level | Ticker ends in | Company involved | CVM registration |
|---|---|---|---|---|
| Patrocinado | I | 31 | Yes | Issuer and BDR dispensed from CVM registration |
| Patrocinado | II | 32 | Yes | Foreign-issuer registration with CVM required |
| Patrocinado | III | 33 | Yes, with a public distribution in Brazil | Foreign-issuer registration with CVM required |
| Não patrocinado | I only | 34 or 35 | No, created by a depositary | Exempt from foreign-issuer registration |

A patrocinado (sponsored) program means the foreign company knows about and participates in the issuance, contracts the depositary, and commits to fuller disclosure to Brazilian investors under [[CVM]] rules. Level III is the only one that allows a primary public distribution — raising new capital — in Brazil, which is why a foreign-domiciled company using B3 as a genuine fundraising venue carries the 33 suffix.

A não patrocinado (unsponsored) program can only be Level I. A depositary creates the receipts off the company's existing foreign listing, without the company necessarily being party to it, with lighter disclosure and no foreign-issuer registration. This is the form most US single-stock receipts take — the 34 line — and it is the form a new US listing acquires almost mechanically once a depositary decides there is Brazilian demand.

## Who can buy

Before 2020 BDRs were effectively walled off from ordinary investors: trading was limited to investidores qualificados (broadly, those with more than R$1 million in financial holdings). A 2020 overhaul of the [[CVM]] and [[B3]] rules opened unsponsored Level I BDRs to the varejo (retail) market. Since then a BDR is bought like any Brazilian stock or ETF — through a home broker, in reais, with no special qualification. That rule change is what makes the same-day-as-IPO retail availability of [[SpaceX securities note|SPCX34]] possible at all; a decade ago it would have been a qualified-investor instrument.

## Taxation for a Brazil resident

Tax is the sharpest practical difference between a BDR and a Brazilian ação, and it runs against the BDR:

| Item | Treatment |
|---|---|
| Capital gain on sale | 15% common operations, 20% day-trade |
| R$20k/month exemption | Does not apply — every gain is taxable regardless of sale size |
| Dividends | Taxed on the progressive table (7.5% to 27.5%), self-assessed |
| Collection | Investor pays via DARF; the broker does not withhold the gain |
| Declaration | Holdings from R$1,000 must be declared; any realized gain must be declared |

The missing R$20k isenção is the line that matters. A Brazilian holding ordinary shares on [[B3]] pays no tax on gains in any month where total sales stay under R$20,000; the same investor selling BDRs owes 15% on the first real of profit. For a frequent trader that friction can outweigh the convenience of local settlement and tilt the decision toward the offshore route.

## Access routes

A Brazil resident has two ways to hold a foreign name, and the BDR is only one of them:

- BDR on [[B3]] — in reais, through a local home broker, no offshore account and no câmbio. The depositary holds the underlying abroad and the receipt settles domestically.
- Direct offshore — buy the actual foreign share through an international broker ([[Interactive Brokers]], [[BTG Pactual]] international, [[Avenue Securities|Avenue]], [[Banco Inter|Inter]], [[Nomad]]), settling in USD outside Brazil. See [[Offshore investing for Brazilians]] for the platform cohort, mechanics, and tax.

The trade-off is convenience versus directness. The BDR keeps everything inside the Brazilian system in reais but adds a depositary layer, can be far less liquid than the home listing, and carries the worse tax treatment. The offshore account gives direct ownership, voting where it exists, and usually deeper liquidity, at the cost of currency conversion and offshore reporting. Both embed USD/BRL — neither is a currency-hedged way to own the company.

## BDRs in this vault

| Ticker | Company | Type (by suffix) | Securities / actor note |
|---|---|---|---|
| SPCX34 | [[SpaceX]] | Não patrocinado Nível I (34) | [[SpaceX securities note]] |
| MELI34 | [[MercadoLibre]] | Não patrocinado Nível I (34) | [[MercadoLibre]] |
| ROXO34 | [[Nubank]] | Não patrocinado Nível I (34; ex-NUBR33) | [[Nubank]] |
| PAGS34 | [[PagSeguro]] | Não patrocinado Nível I (34) | [[PagSeguro securities note]] |
| XPBR31 | [[XP Inc]] | Patrocinado Nível I (31) | [[XP Inc]] |
| STOC31 | [[StoneCo]] | Patrocinado Nível I (31) | [[StoneCo securities note]] |
| INBR32 | [[Banco Inter]] | Patrocinado Nível II (32) — Nasdaq-migration receipt | [[Banco Inter]] |
| AURA33 | [[Aura Minerals]] | Patrocinado Nível III (33) — primary B3 listing | [[Aura Minerals securities note]] |

The in-vault cases now span every category, and the suffix reads the spectrum top to bottom. The unsponsored Level I line (34) is the most common — [[SpaceX securities note|SPCX34]], [[MercadoLibre|MELI34]], [[Nubank|ROXO34]] (re-tickered from NUBR33 in Aug 2023), and [[PagSeguro|PAGS34]] are depositary-created receipts of US-listed companies with no Brazilian sponsorship. The sponsored lines reflect deeper company involvement: [[XP Inc|XPBR31]] and [[StoneCo|STOC31]] are patrocinado Level I, [[Banco Inter|INBR32]] is patrocinado Level II (the receipt Brazilian holders got when the bank redomiciled to [[Nasdaq]]: INTR), and [[Aura Minerals|AURA33]] is the lone patrocinado Level III — a foreign-domiciled, Brazil-linked miner that used the BDR as its actual fundraising listing on [[B3]]. Same wrapper, eight different reasons to exist.

## Most liquid BDRs

The cases above are the vault's covered BDRs — Brazil-linked names plus the SpaceX and Aura situations — but they are not the most traded. BDR turnover on [[B3]] reached roughly R$1bn/day in the first half of 2025, and the volume concentrates in the US-megacap unsponsored Level I line (suffix 34) — the "Magnificent 7," not the domestic names. The liquidity leaders are Tesla and Nvidia, each turning over more than R$130mn/day:

| BDR | Company | Note |
|---|---|---|
| TSLA34 | [[Tesla]] | most-traded BDR (~R$138mn/day, 1H 2025) |
| NVDC34 | [[Nvidia]] | #2 (~R$132mn/day) |
| AAPL34 | [[Apple]] | |
| MSFT34 | [[Microsoft]] | |
| AMZO34 | [[Amazon]] | |
| GOGL34 | [[Alphabet]] | |
| M1TA34 | [[Meta]] | ex-FBOK34, re-tickered after the Facebook → Meta rename |

All seven are não patrocinado Nível I, the same form as [[SpaceX securities note|SPCX34]] — a depositary creates the receipt off the US listing with no company involvement. The tickers are deliberately offset from the US symbols to avoid clashing with B3 codes: Amazon is AMZO34 (not AMZN34), Nvidia NVDC34, Alphabet GOGL34, Meta M1TA34. For a Brazilian these are the practical face of the BDR market — the deepest, most liquid way to hold the megacaps in reais — while the typed examples above illustrate the structural range.

## Synthesis

A BDR is an access wrapper, not a distinct asset, so the analytical content sits in four structural reads rather than in valuation. First, voting: the depositary is the shareholder of record, so a BDR holder usually gets none — moot for a controlled dual-class name like [[SpaceX securities note|SPCX]], where public Class A already carries almost no vote against [[Elon Musk]]'s supervoting Class B, but a real giveaway for names where the vote has value. Second, liquidity: the BDR line can be a thin shadow of the home market, with wider spreads, and that is most acute for a freshly listed receipt sitting on top of an already thin-float IPO. Third, tax: the absent R$20k isenção makes the BDR the less efficient wrapper for an active trader, which is the honest argument for the offshore route. Fourth, currency: the receipt embeds USD/BRL with no hedged class, so a BDR is always simultaneously a position in the company and in the real.

For the vault the instrument matters because it makes US coverage directly actionable from a Brazilian brokerage. Every megacap and most liquid US names carry a 34-suffix receipt, and a new listing acquires one almost mechanically — so a thesis written here on a Nasdaq name is, in practice, one ticker translation away from a reais order.

## Related

- [[Depositary receipts]] — the parent instrument class (ADR / GDR / BDR)
- [[American Depositary Receipts]] — the US sibling variant
- [[B3]] — the exchange where BDRs are admitted and trade
- [[CVM]] — the regulator; defines the sponsored/unsponsored levels and authorized the 2020 retail opening
- [[Offshore investing for Brazilians]] — the offshore (USD, abroad) counterpart route
- [[Foreign private issuer]] — the US wrapper on a foreign company, mirror of the BDR's Brazilian wrapper
- [[SpaceX securities note]] — SPCX34, the unsponsored Level I receipt that prompted this note
- [[Aura Minerals]] — AURA33, sponsored Level III used as a primary B3 listing
- [[Banco Inter]] — INBR31, sponsored Level I from the Nasdaq redomicile
- [[Interactive Brokers]] / [[BTG Pactual]] — the offshore alternative to the BDR route
- [[SpaceX]] — issuer of the SPCX34 underlying

---

*Created 2026-06-14. Instrument classification and ticker-suffix convention from [[B3]] and the Portal do Investidor (gov.br/investidor); retail-access history and tax treatment from RFB-based guidance (InvestNews, InfoMoney, accessed Jun. 2026); SPCX34 paridade and pricing from B3 Bora Investir and Investidor10. Level reads for AURA33 / INBR31 follow the B3 suffix convention plus each company's listing structure. Chart data not applicable: this is an instrument-class concept, not a single price series — per-name BDR price records belong in the relevant securities notes. Not a peer cohort, so the cluster-validation gate does not apply.*
