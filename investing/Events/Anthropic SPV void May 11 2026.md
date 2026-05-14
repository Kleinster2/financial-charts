---
aliases: [Anthropic void declaration, OpenAI void declaration, May 2026 issuer void declarations, AI lab SPV void]
tags: [event, private-markets, secondaries, regulatory, ai-labs]
date: 2026-05-11
actors: [Anthropic, OpenAI, Forge Global, Hiive, Ventuals, PreStocks, Destiny Tech100]
---
#event #private-markets #secondaries #regulatory #ai-labs

# Anthropic SPV void declaration — May 11 2026

On May 11, 2026, [[Anthropic]] posted a public notice declaring all unauthorized secondary transfers of its stock void under Delaware corporate law. [[OpenAI]] followed with identical-language notice on May 12. Both notices named specific platforms publicly. The void-not-voidable framing is the most aggressive position Delaware law allows an issuer to take — it eliminates equitable defenses for downstream good-faith buyers and treats voided chains as if the trades never happened. [[Anthropic]]'s tokenized implied valuation had reached roughly $1.6T against its $380B February 2026 primary round before the notice; [[OpenAI]]'s parallel tokenized market dropped 36% in 24 hours; the listed retail-access vehicle [[Destiny Tech100]] (NYSE: DXYZ) closed -25.05% on May 12 even though its underlying [[Anthropic]] position is board-approved.

---

## Synthesis

The May 11–12 declarations flip the AI labs from incremental enforcement (case-by-case ROFR exercises, individual cease-and-desist letters) to a categorical issuer-side void of an entire parallel retail market. The void-versus-voidable distinction matters because a voidable regime leaves downstream good-faith buyers with equitable defenses (they paid honest money, did not know the chain was unauthorized, kept the position); a void regime eliminates those defenses and forces recourse against the seller, not against the underlying shares. The economics of retail-access vehicles change in a single press cycle.

The coordination — two of the three trophy private issuers issuing near-identical language in the same week — is the structurally important fact. The third trophy issuer is [[SpaceX]], which has not joined as of May 13. The asymmetry is itself a tradable feature: if [[SpaceX]] follows, every retail-access product in this space is on notice simultaneously; if it does not, the market reads a fork between the AI-lab issuer posture and the spaceflight-issuer posture.

---

## Timeline

| Date | Event |
|------|-------|
| Through 2024–2025 | AI labs enforce transaction-by-transaction: ROFR exercises on employee transfers, cease-and-desist letters to specific funds, blocks on specific SPV stacks. No categorical issuer posture. |
| Oct 2025 | [[Ventuals]] launches on [[Hyperliquid]] — synthetic perpetual futures on [[Anthropic]] / [[OpenAI]] / [[SpaceX]] valuations. No underlying shares touched. |
| Late 2025 – Apr 2026 | Tokenized implied valuations diverge from primary-round prices. [[Anthropic]] tokenized implied reaches ~$1.6T against [[Anthropic]]'s $380B Feb 2026 primary round (4.2x premium). |
| Apr 2026 | [[Anthropic]] reportedly negotiating next primary round at ~$900B (TechCrunch). Gap between primary and tokenized markets becomes the operational trigger. |
| May 11, 2026 | [[Anthropic]] posts public notice: any sale or transfer of [[Anthropic]] stock not approved by the board is void and will not be recognized on the books. SPVs explicitly disallowed. Specific platforms named. |
| May 12, 2026 | [[OpenAI]] follows with identical legal language. [[OpenAI]] tokenized perp markets drop -36% in 24 hours. [[Destiny Tech100]] (DXYZ) closes -25.05% on [[NYSE]]. |
| May 12, 2026 | [[Forge Global]] publicly disputes inclusion, calls it erroneous, points to its issuer-approval workflow. [[Sydecar]] disputes inclusion, says it operates only administratively. |
| As of May 13 | [[SpaceX]] has not issued a parallel notice. Dispute over [[Forge Global]] / [[Sydecar]] inclusion unresolved. |

---

## Who was named

### Issuers
- [[Anthropic]] — primary actor on the May 11 notice. AI lab behind Claude. $380B Feb 2026 venture round.
- [[OpenAI]] — parallel May 12 notice with identical language. AI lab behind ChatGPT. ~$850B implied in current private rounds.
- [[OpenAI Foundation]] — the non-profit parent that controls [[OpenAI]] governance; not the operating issuer for shares.

### Tokenized / synthetic platforms
- [[Ventuals]] — perp DEX on [[Hyperliquid]] offering synthetic exposure to private-company valuations. Settlement in dollar-pegged stablecoins; no underlying shares touched.
- [[PreStocks]] — [[Solana]]-based platform claiming 1:1 backing by pre-IPO shares held in custody.

### Traditional secondary venues (broker-dealer licensed)
- [[Forge Global]] — licensed broker-dealer for private secondaries. Publicly disputed inclusion. Mid-acquisition by [[Charles Schwab]].
- [[Hiive]] — licensed broker-dealer. Issuer-approval workflow.

### SPV operators (pooled vehicles)
- [[Open Door Partners]], [[Unicorns Exchange]], [[Pachamama Capital]], [[Lionheart Ventures]], [[Upmarket]] — bundle accredited or retail money into SPVs for trophy-name exposure, sometimes through stacked layers.

### Back-office administrator
- [[Sydecar]] — fund-formation plumbing for SPV sponsors. Disputed inclusion, said it operates only administratively.

### Listed retail-access vehicle (collateral damage)
- [[Destiny Tech100]] (NYSE: DXYZ) — closed-end fund holding board-approved [[Anthropic]] and [[OpenAI]] positions inside SPVs. Closed -25.05% on May 12 not because its own positions were voided but because the market repriced the legitimacy premium on every retail-accessible AI-lab vehicle in sympathy.

---

## The void-vs-voidable mechanics

Under Delaware corporate law, an issuer can deem unauthorized transfers either:

| Stance | Effect on downstream good-faith buyers |
|--------|---------------------------------------|
| Voidable | Equitable defenses available: buyer paid fair value, did not know chain was unauthorized, can argue to keep position |
| Void | No equitable defenses. Chain treated as if it never existed. Buyer's recourse runs against the seller, not against the shares. |

Crypto lawyer Gabriel Shapiro flagged "void" as the most aggressive legal position the issuers could have chosen. The legal economics for downstream buyers — particularly retail buyers who bought tokenized exposure through asset-backed platforms claiming 1:1 share backing — fundamentally change: their claim now runs against whatever SPV or pooled vehicle sold them the exposure, not against the underlying [[Anthropic]] or [[OpenAI]] shares.

For purely synthetic platforms like [[Ventuals]], the legal exposure is structurally different: [[Ventuals]] perps never claimed to hold underlying shares, they pay out from a stablecoin pool based on an oracle's published valuation. The void notices do not directly invalidate synthetic exposure, but they remove one of the inputs that gave the published valuations a thin veneer of legitimacy (the existence of asset-backed parallel markets at the same number).

---

## Market impact

| Channel | Move | Source |
|---------|------|--------|
| [[Anthropic]] tokenized implied valuation | $1.6T → reset (specific number not published) | Spendnode, Cryptopolitan |
| [[OpenAI]] tokenized perp markets | -36% in 24 hours | Cryptopolitan, Phemex |
| [[Destiny Tech100]] (DXYZ) close | $71.24 → $53.40 (-25.05%) on May 12 | NYSE close |
| [[Destiny Tech100]] sigma read | -4.3σ beta-adjusted (vault `quick_movers.py`) | Vault mover screen May 13 |

[[Destiny Tech100]] is the most visible listed price-discovery event because it actually traded on a regulated exchange. The fund's underlying [[Anthropic]] and [[OpenAI]] SPV positions are board-approved and therefore not voided by the May 11 declaration; the -25% move reprices the legitimacy premium on every retail-accessible AI-lab vehicle, not the NAV of DXYZ's positions. A second leg lower in DXYZ would suggest the issuer pushback is becoming the dominant frame for the entire retail-access category.

---

## What to watch

- Does [[SpaceX]] join? Three-issuer coordination would close the gap; two-issuer coordination with the spaceflight issuer holding back creates a structural asymmetry between AI-lab exposure and spaceflight exposure
- Resolution of the [[Forge Global]] / [[Sydecar]] inclusion dispute. If [[Anthropic]] retracts, the credibility of the issuer-side blocklist takes a hit. If [[Anthropic]] holds firm, broker-dealer-licensed secondary venues are exposed to issuer veto in ways they previously were not. [[Forge Global]] is also mid-acquisition by [[Charles Schwab]] — the dispute interacts with deal-close timing
- [[Ventuals]] oracle behavior post-announcement. The published valuations were one of the inputs that made tokenized markets read as price discovery; the oracle's post-announcement readings determine whether [[Ventuals]] becomes a legitimacy-laundering venue or shrinks back to pure punter speculation
- [[SEC]] / state-securities-regulator response. Synthetic equity derivatives on US private companies, offered to US persons through US-IP-geofenced offshore protocols, is the BitMEX / Binance fact pattern. The issuer void notice gives any future enforcement action a cleaner premise
- Next [[Anthropic]] primary round pricing. If the gap between primary-round and tokenized prices was the operational trigger, the next primary round becomes the marker for whether enforcement compressed the gap

---

## Why this matters beyond the immediate price moves

Three structural points:

1. The indefinite private window — [[OpenAI]] eight years old and private, [[Anthropic]] four and private, [[SpaceX]] twenty-three and private — creates the demand. Retail investors broadly cannot buy the most consequential companies of the era directly. A multi-trillion-dollar asset class sits behind a wall of accredited-investor and qualified-purchaser rules.
2. The structural arbitrage opportunity. Where there is retail demand at this scale, supply gets manufactured. Through 2024-2025 dozens of platforms built workarounds — SPV stacks, tokenization platforms, pure synthetic derivatives. The May 11-12 notices are the first categorical issuer pushback on the entire category, not just specific transactions.
3. The valuation-gap trigger. The void notices became the operationally rational issuer move when the unauthorized market was setting the headline valuation number for the company (4.2x the primary-round price). When the parallel market's published numbers feed into mainstream press as legitimate price discovery, the cost of inaction crosses the cost of confrontation.

---

## Sources

- TechCrunch — [Anthropic warns investors against secondary platforms offering access to its shares](https://techcrunch.com/2026/05/12/anthropic-warns-investors-against-secondary-platforms-offering-access-to-its-shares/) (May 12, 2026)
- Cryptopolitan — [Anthropic declares secondary share trades void, raising litigation risk across global markets](https://www.cryptopolitan.com/anthropic-secondary-share-trades-void/) (May 12, 2026)
- Coindesk — [Anthropic warns against unauthorized stock exposure as token markets imply trillion-dollar valuation](https://www.coindesk.com/markets/2026/05/12/anthropic-fights-unauthorized-stock-exposure-as-token-markets-imply-trillion-dollar-valuation) (May 12, 2026)
- Spendnode — [Anthropic Voids Unauthorized Stock Trades as Tokens Imply $1.6T](https://www.spendnode.io/blog/anthropic-voids-unauthorized-stock-trades-1-6t-tokenized-may-2026/) (May 12, 2026)
- Phemex — [Anthropic Denies Unauthorized Stock Sales; Token Drops 25%](https://phemex.com/news/article/anthropic-clarifies-stock-sale-policy-prestocks-token-plummets-25-80668) (May 12, 2026)
- Glitchwire — [Anthropic Warns Investors: Unauthorized Stock Sales Are Void and Could Be Outright Fraud](https://glitchwire.com/news/anthropic-warns-investors-unauthorized-stock-sales-are-void-and-could-be-outrigh/) (May 12, 2026)
- Anthropic Help Center — [Unauthorized Anthropic stock sales and investment scams](https://support.claude.com/en/articles/13704655-unauthorized-anthropic-stock-sales-and-investment-scams) (the issuer notice itself)
- Vault — [[Reports/2026-05-13-explain-ventuals-perps-and-may-2026-void-declarations]] earlier-session /explain report for broader narrative context

---

## Related

- [[Private market secondaries]] — full structural treatment of the void mechanism and the implied-valuation gap table
- [[Tokenized private shares]] — the synthetic vs. asset-backed split and the post-void legitimacy gap
- [[Anthropic]] — issuer of the May 11 notice
- [[OpenAI]] — issuer of the May 12 parallel notice
- [[SpaceX]] — the third trophy issuer, has not joined as of May 13
- [[Destiny Tech100]] — listed retail-access vehicle, -25% on May 12
- [[Ventuals]] — synthetic perpetuals platform on [[Hyperliquid]]
- [[PreStocks]] — asset-backed tokenization platform on [[Solana]]
- [[Forge Global]] — licensed broker-dealer; disputed inclusion
- [[Hiive]] — licensed broker-dealer
- [[Sydecar]] — fund-formation administrator; disputed inclusion
- [[Open Door Partners]], [[Unicorns Exchange]], [[Pachamama Capital]], [[Lionheart Ventures]], [[Upmarket]] — pooled SPV operators on the named list
- [[Charles Schwab]] — pending [[Forge Global]] acquirer; affects dispute timing
- [[SEC]] — regulator with prior enforcement pattern on similar fact patterns
