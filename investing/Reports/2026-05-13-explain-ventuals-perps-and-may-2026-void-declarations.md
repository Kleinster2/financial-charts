---
name: Ventuals perps and the May 2026 issuer void declarations — explainer
type: explainer
topic: "[[Private market secondaries]]"
depth: standard
generated: 2026-05-13 03:30
sources_read: 12
tags: [report, explainer]
---

# Ventuals perps and the May 2026 issuer void declarations — what's going on, in plain terms

For about eighteen months, retail traders had built a parallel market for shares of three trophy private companies — [[Anthropic]], [[OpenAI]], and [[SpaceX]] — using synthetic crypto contracts, tokenized share claims, and pooled investment vehicles that the companies themselves had never sanctioned. On May 11 and May 12, 2026, the two AI-lab issuers said in writing that none of those trades count. [[Anthropic]] posted a public notice declaring every secondary transfer of its stock that its board has not approved to be void — not merely voidable, but legally treated as if the transfer never happened. [[OpenAI]] followed with an identical-language notice the next day. Both notices named specific platforms by name. The market for tokenized [[OpenAI]] contracts dropped 36% in twenty-four hours, and a listed retail vehicle that holds [[Anthropic]] shares closed down 25% on the day after.

## Who's involved

The issuers are [[Anthropic]] (the AI lab behind the Claude assistant, last priced at $380 billion in a February 2026 venture round) and [[OpenAI]] (the AI lab behind ChatGPT, in a parallel late-stage round at roughly $850 billion). Both are still private companies — they have never had public stock — and both have grown faster than any private companies in history.

The trading venues split into two camps. On the synthetic side is [[Ventuals]], a startup that launched in October 2025 on [[Hyperliquid]] (a decentralized derivatives exchange that runs on its own blockchain). [[Ventuals]] lets anyone with a crypto wallet bet on whether [[Anthropic]]'s, [[OpenAI]]'s, or [[SpaceX]]'s valuation will go up or down using a [[Perpetuals|perpetual future]] — a derivative invented in crypto markets that mimics owning the underlying asset without ever actually buying it. Settlement happens in dollar-pegged stablecoins; no shares change hands. On the asset-backed side is [[PreStocks]], a [[Solana]]-based platform that claims its tokens are 1:1 backed by actual pre-IPO shares held in custody. Together, the two platforms drove the tokenized implied [[Anthropic]] valuation to roughly $1.6 trillion by mid-May 2026.

The traditional secondary market got named too. [[Forge Global]] and [[Hiive]] are licensed broker-dealers that match private buyers and sellers under direct issuer-approval workflows; both ended up on [[Anthropic]]'s blocklist for what the notice called "new offerings" on the platforms. Below them sit pure pooled-vehicle operators — [[Open Door Partners]], [[Unicorns Exchange]], [[Pachamama Capital]], [[Lionheart Ventures]], [[Upmarket]] — that bundle retail or accredited money into SPVs (special-purpose vehicles, single-investment fund structures) to buy and resell exposure to the trophy names. [[Sydecar]], a back-office administrator that provides only fund-formation plumbing for sponsors, also appeared on the list.

Finally, the most visible listed casualty is [[Destiny Tech100]] (ticker DXYZ on the NYSE), a closed-end fund that holds [[Anthropic]] shares inside a board-approved SPV. It closed down 25.05% on May 12 — not because its own position was voided, since the board signed off on it, but because the market repriced the legitimacy premium on every retail-accessible AI-lab vehicle in sympathy.

## Why it matters

Three things make these announcements consequential beyond the immediate price moves.

First, the void-versus-voidable distinction is the most aggressive stance Delaware corporate law allows an issuer to take. Under a voidable regime, a downstream good-faith buyer who paid honest money for a fund interest could argue equitable defenses — they did not know the chain was unauthorized, they paid fair value, they should keep their position. Under a void regime, the law treats the chain as having never existed. The downstream buyer's recourse runs against the seller who sold something they did not have the right to sell, not against the underlying shares. The legal economics of retail-access vehicles change in a single press cycle.

Second, the announcements were coordinated. Two of the three trophy issuers issued near-identical legal language in the same week. The third trophy issuer is [[SpaceX]], which has not issued a parallel notice as of May 13. If [[SpaceX]] follows, every retail product in this space is on notice simultaneously. If it does not, the asymmetry itself becomes part of the trade.

Third, the implied valuations on tokenized markets had diverged dramatically from the prices private investors were actually paying. [[Anthropic]]'s tokenized perp had implied a $1.6 trillion valuation against the $380 billion February primary round — a 4.2x premium. The void announcement is the issuers explicitly disclaiming the legitimacy of the inventory feeding those prices.

## The context

To understand why this happened now, three threads have to fit together.

The first is the indefinite private window. In the 1990s, transformational companies went public within a few years of founding. Today they wait a decade or more. [[OpenAI]] is eight years old and not public. [[Anthropic]] is four and not public. [[SpaceX]] is twenty-three and not public. The result is that retail investors — meaning anyone without accredited-investor status, broadly $1 million in net worth excluding the primary residence or $200,000 in income — cannot legally buy the most consequential companies of the era directly. A multi-trillion-dollar asset class sits behind a wall.

The second is the structural arbitrage opportunity. Where there is demand at this scale, supply gets manufactured. Through 2024 and 2025, dozens of platforms built workarounds. SPVs pooled small allocations from accredited investors and sold pro-rata interests, sometimes through stacked layers that obscured the underlying. Tokenization platforms claimed to hold real shares and issued digital claims that retail could buy. Pure synthetic derivatives like [[Ventuals]] perps did not even pretend to touch the underlying — they let anyone with a crypto wallet bet on a number. Volume on [[Ventuals]] reached $215 million cumulative within four months of its October 2025 launch, small in absolute terms but enough that the implied valuations published continuously on its order book were being cited in mainstream press as legitimate price discovery.

The third is the issuer's tolerance ceiling. Until May 2026, the trophy AI labs had publicly opposed unauthorized sales but acted transaction by transaction — exercising rights of first refusal on specific employee transfers, blocking specific funds, sending cease-and-desist letters case by case. The May 11–12 notices flipped from incremental enforcement to a categorical declaration of voidance, with platforms named publicly. The proximate trigger appears to have been the gap between the published implied valuations on the tokenized markets ($1.6 trillion for [[Anthropic]]) and the price the company itself was negotiating in its next primary round (reportedly around $900 billion per TechCrunch). When the unauthorized market starts setting the headline valuation number for your company, the cost of inaction becomes higher than the cost of confrontation.

## What's contested and what to watch

The first contested question is the [[Forge Global]] and [[Hiive]] inclusion. Both platforms publicly disputed their listing — [[Forge Global]] called the inclusion erroneous and pointed to its issuer-approval workflow; [[Sydecar]] said it operates only administratively. The dispute had not been resolved as of May 13. If [[Forge Global]] forces a retraction, the credibility of the issuer-side blocklist takes a hit; if [[Anthropic]] holds firm, broker-dealer-licensed secondary venues are exposed to issuer veto in ways they previously were not. [[Forge Global]] is also mid-acquisition by [[Charles Schwab]], which adds an additional time-pressure dimension.

The second is whether [[SpaceX]] joins. Its absence from the parallel announcement is conspicuous. The third is what happens to listed retail-access vehicles like [[Destiny Tech100]] — their underlying SPV positions are board-approved and therefore not directly voided, but the premium-to-NAV they trade at depends on retail belief in the asset class. The May 12 -25% move is the market's first attempt to reprice that premium; a second leg lower would suggest the issuer pushback is becoming the dominant frame for the whole category.

The fourth is regulatory. Synthetic equity derivatives on US private companies, offered to US persons through US-IP-geofenced offshore protocols, is precisely the fact pattern the [[SEC]] pursued in earlier rounds against BitMEX, Binance, and others. The void announcement gives any future enforcement action a cleaner premise — the issuers themselves are now on record that the trades are unauthorized.

## Where to read deeper in the vault

- [[Private market secondaries]] — full structural treatment of the void mechanism, the implied-valuation gap table, and the read for retail-access vehicles
- [[Tokenized private shares]] — the synthetic vs. asset-backed split and the post-void legitimacy gap
- [[Ventuals]] — the perp DEX itself: market design, oracle mechanics, open-interest caps, full investment case
- [[PreStocks]] — the asset-backed counterpart on [[Solana]]
- [[Destiny Tech100]] — the listed retail-access vehicle that took the parallel hit
- [[Anthropic]] and [[OpenAI]] — the issuer notices themselves, embedded in each company's actor note

## Gaps

- [[Jarsy]] — referenced as [[Ventuals]]'s asset-backed competitor; no note yet exists
- [[Earlybird]] — [[Solana]]-based prediction-market-style pre-IPO platform; no note
- USDH — [[Hyperliquid]]'s dollar-pegged stablecoin used for [[Ventuals]] settlement; no note
- The [[Ventuals]] oracle's post-announcement behavior — vault describes the mechanism but does not yet track post-announcement readings
