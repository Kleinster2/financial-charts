---
aliases: []
tags: [actor, defi, derivatives, tokenization, private]
---

# PreStocks

PreStocks — [[Solana]]-based tokenized pre-IPO exposure platform, integrated with [[Jupiter]] (Solana DEX aggregator). Launched August 2025. Claims 1:1 backing by actual pre-IPO shares, similar in design to Jarsy; primary competitor to [[Ventuals]] in the crypto-native AI-lab exposure category. Together with Ventuals, helped drive tokenized implied [[Anthropic]] valuation to ~$1.6T by May 2026 — roughly 4.2x the Feb $380B primary round.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Chain | [[Solana]] (via Jupiter integration) |
| Launch | August 2025 |
| Model | Asset-backed tokens (1:1 claimed) |
| Settlement | Instant (DEX-integrated) |
| Status | Tokenized exposure to [[Anthropic]] (and other AI labs) implicated by [[Anthropic]]'s May 11 2026 void notice covering tokenized securities |

---

## Design

PreStocks tokenizes claim-on-equity rights rather than offering pure synthetic exposure ([[Ventuals]]). The structural distinction:

- [[Ventuals]] perps are *synthetic* — never touch real shares; speculation on a number anchored by a hybrid oracle
- PreStocks tokens are claimed to be *asset-backed* — represent claim on actual pre-IPO shares held in custody by the platform

The asset-backed model exposes PreStocks to both custody risk (does it actually hold the shares?) and to the [[Anthropic]] / [[OpenAI]] May 11-12 2026 void mechanism. If the underlying SPV chain feeding tokens into the platform is declared void by the issuer, the token holders' claim on shares dissolves — the chain of title never existed under Delaware bylaws.

The platform reportedly has no public audit proofs of share backing as of mid-2026, which is the chief structural risk for token holders even before the issuer pushback layer.

---

## Anthropic May 11 2026 void notice — exposure

[[Anthropic]]'s May 11 2026 help-center notice explicitly named "tokenized securities" as an unauthorized mechanism for indirect [[Anthropic]] exposure (alongside SPVs and forward contracts). PreStocks was not named individually but is within the targeted category. The structural significance for PreStocks: if the platform's [[Anthropic]] share inventory was routed through any of the named unauthorized SPV operators ([[Open Door Partners]], [[Unicorns Exchange]], [[Pachamama Capital]], [[Lionheart Ventures]], [[Sydecar]], [[Upmarket]], or new offerings on [[Forge Global]] / [[Hiive]]), those positions are now declared void and the corresponding tokens are effectively unbacked.

Full structural treatment: [[Tokenized private shares#Issuer pushback: void declarations (May 11-12, 2026)]]. Dated-event hub: [[Anthropic SPV void May 11 2026]] (Events/).

---

## Related

- [[Ventuals]] — synthetic-perp competitor (different model: never touches real shares)
- [[Hyperliquid]] — underlying L1 for Ventuals (contrast with PreStocks's Solana/Jupiter base)
- [[Anthropic]] — May 11 2026 void notice covers tokenized securities category
- [[OpenAI]] — May 12 2026 parallel void notice
- [[SpaceX]] — also tokenized on PreStocks
- [[Tokenized private shares]] — concept hub; tokenization category structure
- [[Private market secondaries]] — concept hub; full structural treatment of the May 11-12 void mechanism
- [[Solana]] — underlying chain
- [[Jupiter]] — DEX aggregator integration

*Sources: [[Ventuals]] competitor table (existing vault entry); [Spendnode — Anthropic Voids Unauthorized Stock Trades as Tokens Imply $1.6T](https://www.spendnode.io/blog/anthropic-voids-unauthorized-stock-trades-1-6t-tokenized-may-2026/) (May 2026); [Anthropic Help Center](https://support.claude.com/en/articles/13704655-unauthorized-anthropic-stock-sales-and-investment-scams).*
