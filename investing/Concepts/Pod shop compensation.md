---
aliases: [pod shop pay, multi-manager pay, multi-manager compensation, hedge fund PM pay, $100mn PM package, pass-through compensation, accelerator pay, centre book]
---
#concept #hedgefunds #finance #compensation

How [[Multi-manager hedge funds|pod shops]] pay portfolio managers — the pass-through fee model that lets PM packages clear $100mn and frequently reach $175mn with accelerator structures. The mechanism solves netting risk for the firm and pushes most operating expenses, including PM bonuses, onto LPs. The talent-war arithmetic that makes [[Millennium]], [[Citadel]], [[Balyasny]], and [[Point72]] willing to write nine-figure offers is structurally enabled by this fee architecture.

---

## Synthesis

Three things hold this together. First, the pass-through fee model — used by more than 80% of multi-strategy firms by 2025 — charges almost all operating costs (PM bonuses, technology, data, entertainment) directly to LPs, rather than absorbing them into a 2% management fee. Second, that structure solves netting risk, the historical problem that brought down weaker funds: when some pods lose money in a year, traditional funds had to cut top-PM bonuses to balance the book, which then triggered star defections. Pass-through means winners get paid regardless of firm-wide performance. Third, with retention secured, the firms compete for new hires through layered package components — cash advance, team budget, cost savings, and the "accelerator" that boosts profit share on the first tranche of gains. A senior PM can clear $100mn from these components alone, and with a strong accelerator hit, $175mn or more.

The LP cost is real. [[Balyasny]]'s Atlas Enhanced fund returned 15.2% gross in 2023 but only 2.8% net after $768mn in pass-through expenses, primarily compensation — a 12.4 pp drag that effectively re-routed most of the year's alpha into the talent pool. The industry's open question, as articulated by sceptics quoted in the [[Financial Times|FT]] piece, is whether hedge funds can keep generating enough excess return to justify these packages. The counter is that even if multi-manager funds cool, [[Jane Street]], [[Citadel Securities]], or family offices like [[BlueCrest]] ([[Michael Platt]]'s vehicle, ~$50-60bn proprietary) will simply step in to bid for the same talent.

---

## The pass-through fee model

Traditional hedge funds used "2 and 20" — 2% management fee covering all operating costs, 20% performance fee on gains. The model worked when funds were small and operations cheap, but it broke down as pod shops scaled to hundreds of PMs across global offices with billions in data, technology, prime brokerage, and compensation overhead.

The pod-shop alternative: charge investors directly for the firm's operating expenses, including PM bonuses, analyst salaries, data subscriptions, hedging costs, client entertainment, real estate, and technology. The management fee shrinks or disappears; the performance fee stays around 20%; but the line item that used to be implicit in "2 and 20" now appears as an itemised pass-through.

| Component | Traditional 2 and 20 | Pass-through model |
|---|---|---|
| Management fee | 2% of AUM | 0-2% |
| Performance fee | 20% of gains | 20-30% of gains |
| Operating expenses | Absorbed by manager | Charged to LPs directly |
| Effective total fee | ~3-4% in good years | 7-10%+ commonly, up to 15%+ in high-expense years |
| PM bonuses | Paid from manager's 20% cut | Paid from LP pass-through |

By 2025, more than 80% of multi-strategy firms used some form of pass-through structure ([Bloomberg](https://www.bloomberg.com/graphics/2025-hedge-fund-investment-fees/)). The model is now near-universal among the major pod shops — [[Millennium]], [[Citadel]] Wellington, [[Point72]], [[Balyasny]], [[ExodusPoint]], [[Schonfeld]].

The arithmetic for LPs in a soft year is brutal. [[Balyasny]]'s Atlas Enhanced fund reported a 15.2% gross return in 2023 but only 2.8% net after $768mn in pass-through expenses, with employee compensation the dominant line ([Wall Street Oasis](https://www.wallstreetoasis.com/forum/hedge-fund/economics-of-pass-through-mm)). LPs accept this because the long-run net returns still beat the alternatives — but the structure means that in years when alpha is thin, almost all of it flows to the staff before the LP sees anything.

---

## Netting risk — the problem the model solves

The core mechanical reason pass-through emerged is netting risk. Under the old structure, the firm's 20% performance fee was calculated on net firm-wide gains. When some pods lost money, those losses netted against the winners, shrinking the bonus pool the firm could pay its top PMs.

The downstream consequence — and the existential threat to weaker funds — was a doom loop. Mediocre firm-wide performance meant top performers received less than their individual contribution warranted. Competitors picked off the disgruntled stars with bigger guarantees. Their departures further damaged firm performance. The next year was worse. Funds that hit netting risk typically did not recover.

Pass-through severs the link. PM bonuses are an LP-absorbed expense, not a deduction from a firm-wide performance pool. A top PM who makes $250mn for the firm receives the contractually-defined share of that personal P&L regardless of whether other pods lost money. The firm pays out what it owes the winners; the LPs absorb the cost of the losers.

This is why the structure scaled so completely across the multi-manager industry — it transferred the most dangerous firm-level risk (mass star defection after a soft year) onto the LP base, in exchange for the higher headline fees the LPs accept.

---

## The worked example — $250mn to $36mn

The Financial Times' September 2025 explainer walked through how a single PM's $250mn in trading profits nets down to a $36mn take-home. The example uses round numbers and a standard 20% profit share; the actual mechanics vary by negotiation, but the order-of-magnitude flow is representative.

### Setup — capital structure

The multi-manager raises $50bn from investors. With bank leverage, that becomes $200bn to deploy across the firm's pods. Most of the capital sits with the "long tail" of PMs ($182bn in the FT example); a few top PMs each get billions ($5bn, $2bn, $1bn for PM1, PM2, PM3); a central "centre book" holds $10bn used to copy the PMs' best trades.

![[pod-shop-capital-raise.png]]
*Source: Financial Times. $50bn investor capital becomes the base for the multi-manager structure.*

![[pod-shop-leverage.png]]
*Source: Financial Times. Bank leverage takes the $50bn to $200bn of buying power.*

![[pod-shop-pm-allocation.png]]
*Source: Financial Times. PM allocation example — a small number of top PMs run billions, the majority of capital sits with the long tail.*

![[pod-shop-centre-book.png]]
*Source: Financial Times. The centre book holds back ~$10bn to copy winning PM trades.*

### Trading profit

PM1, allocated $5bn, generates a 5% return — $250mn in trading profits for the firm.

![[pod-shop-pm-return.png]]
*Source: Financial Times. PM1's $5bn allocation, 5% return, yields $250mn in gross trading profits.*

### Expenses charged "above the line"

Before PM1's profit share is calculated, $14mn in expenses are deducted from the $250mn trading profit:

| Expense | Amount |
|---|---|
| Leverage and trading costs | $5mn |
| Data and research | $3mn |
| Hedging costs | $3mn |
| Analysts' salary | $3mn |
| Total above-the-line | $14mn |

![[pod-shop-expenses.png]]
*Source: Financial Times. $14mn in operating costs deducted before profit share is calculated.*

This brings the net trading profit attributable to PM1's pod to $236mn.

### Profit share

PM1's contract specifies a 20% share of the net trading profit. 20% of $236mn = $47mn.

![[pod-shop-cut-of-profits.png]]
*Source: Financial Times. PM1 keeps 20% of the $236mn net trading profit — $47mn.*

### Discretionary bonus

PMs are also eligible for discretionary bonuses on top of the contractual share. In the FT example, this adds $2mn.

![[pod-shop-discretionary-bonus.png]]
*Source: Financial Times. $2mn discretionary bonus added to the contractual share.*

### Centre book payment

When PM1's trades were copied by the firm's centre book, PM1 receives a payment back — $1mn in the example. This is the mechanism that turns alpha-generating PMs into internal alpha-sources for the wider firm, with explicit compensation for the IP.

![[pod-shop-centre-book-payment.png]]
*Source: Financial Times. Centre book payment of $1mn for trades the firm's central book copied.*

### Analysts' bonuses — paid out of PM's pocket

Here the structure flips against the PM. Analysts on PM1's team need bonuses too, and at many firms these come out of the PM's compensation rather than the firm's pass-through. In the FT example, $14mn in analyst bonuses is deducted from PM1's pay.

![[pod-shop-analysts-bonus.png]]
*Source: Financial Times. PM pays analyst bonuses from their own pocket — $14mn deducted.*

### Take-home

Starting from $250mn in firm-side trading profit, after the $14mn in above-the-line expenses, the $47mn profit share, $2mn discretionary bonus, $1mn centre book payment, and the $14mn analyst-bonus pay-out: PM1 takes home $36mn.

![[pod-shop-take-home.png]]
*Source: Financial Times. After all flows, PM1 takes home $36mn on $250mn of trading profit — about 14.4% of the gross.*

---

## Above-the-line vs below-the-line — where costs land matters

A negotiation detail that can swing PM take by millions: whether expenses sit "above the line" or "below the line."

If above the line, costs are netted off trading profits before the PM's percentage cut is calculated. In the worked example, $14mn deducted above the line means the PM's 20% is calculated on $236mn — yielding $47mn.

If below the line, costs are deducted after the PM takes their cut. The PM's 20% is calculated on the full $250mn = $50mn, and the $14mn comes out afterwards, leaving $36mn — a $3mn swing on the same numbers.

In practice, PMs negotiate which specific expenses sit where. Some costs the PM has direct influence over (analyst salary, specific data subscriptions) tend to be below the line so the PM has skin in the game; firm-wide costs (compliance, prime brokerage, shared infrastructure) tend to be above the line. The distribution varies by firm and by the leverage the individual PM has in the negotiation.

---

## Package components for new hires — building to $100mn

To poach PMs from rivals, the multi-managers offer layered package components on top of the standard profit share. These are how a senior PM hire — like [[Steve Schurr]]'s $100mn move from [[Balyasny]] to [[Millennium]] in April 2025 — gets to nine figures.

### Team budget

The hiring firm gives the PM a budget to build their own team of analysts and support staff. In the FT example: $30mn.

![[pod-shop-team-budget.png]]
*Source: Financial Times. $30mn team budget to recruit analysts and support staff for the incoming PM.*

### Cash advance

To compensate for deferred pay forfeited at the old employer, foregone earnings during garden leave, and the time it takes to hit full earnings potential at the new firm, the PM receives a cash advance. The FT example uses $60mn. The article notes "the most talented people can command cash advances in the tens of millions of dollars," payable either upfront or staggered over a few years.

![[pod-shop-cash-advance.png]]
*Source: Financial Times. $60mn cash advance covering lost pay, garden leave, and career risk.*

### Cost savings

The hiring firm waives or reduces a portion of the standard pass-through expense bill the PM would otherwise face. In the FT example: $10mn shaved off the expected costs.

![[pod-shop-cost-savings.png]]
*Source: Financial Times. $10mn knocked off the PM's expected pass-through cost bill.*

### Package total

These three components — team budget + cash advance + cost savings — sum to the FT example's headline $100mn.

![[pod-shop-package-total.png]]
*Source: Financial Times. The magic $100mn — but the upside doesn't stop here.*

---

## The accelerator — turbocharging the upside

On top of the negotiated package, the PM may also receive an "accelerator" — a higher profit share on a defined first tranche of gains. The FT example: instead of the standard 20% profit share, the PM gets 27.5% on the first $1bn of trading profits.

Mathematically, that 7.5 pp uplift on a $1bn gain delivers $75mn — depending on performance, this can be the most lucrative single component of the package. Combined with the $100mn base package, total potential pay reaches $175mn or higher.

![[pod-shop-accelerator.png]]
*Source: Financial Times. Accelerator boosts profit share to 27.5% on the first $1bn of gains — $75mn of additional upside.*

The trade-off the hiring firm faces: cash guarantees lock in the cost regardless of performance ("someone can just come along and suck at trading and walk away with investors' money," as one family-office executive told the FT), while accelerators only pay out if the PM actually generates the gains. Hedge funds typically push the structure toward more accelerator, less guarantee — for new hires they want to motivate, against PM preferences to lock in the cash.

Cold-research framing: industry coverage confirms profit shares "rising to 24.5% for the best portfolio managers at top multistrategy hedge funds like Citadel, Millennium and Balyasny" ([Hedgeweek](https://www.hedgeweek.com/multi-manager-hedge-funds-escalate-talent-war-arms-race-with-nine-figure-pay-packages/)), with accelerators conditioned on Sharpe ratio thresholds — the firm protects itself from a PM who hits high absolute returns through pure leverage rather than skill.

---

## The centre book — internal copying of PM trades

The "centre book" is a pool of firm capital — $10bn in the FT example — held back from individual PM allocations and used to copy the best PM trades. Mechanically, it's a multiplier: when a PM identifies a trade that the centre-book risk committee believes is genuinely high-conviction, the firm can scale that exposure beyond the PM's personal allocation.

The PM receives a payment back when their trades are copied — $1mn in the worked example. This creates aligned incentives: PMs want their best ideas amplified into the centre book (more capital deployed against their conviction, plus the copy payment), and the firm wants to systematically harvest the highest-conviction signals across hundreds of independent pods.

The centre book is also a key piece of pod-shop risk management. It concentrates capital into the trades the firm believes are most defensible across multiple PM reviews, and provides a mechanism for the firm to express conviction across pods rather than only within them.

---

## Talent war — the FT's $100mn proof-points

The FT article's framing data point — [[Steve Schurr]]'s move from [[Balyasny]] to [[Millennium]] for ~$100mn in early 2025 — has been independently confirmed by [Bloomberg](https://www.bloomberg.com/news/articles/2025-04-29/millennium-poaches-balyasny-s-schurr-with-100-million-offer), [Hedgeweek](https://www.hedgeweek.com/millennium-lures-balyasny-veteran-with-100m-package/), and others. Schurr was Balyasny's senior managing director of Fundamental Equities, joined [[Millennium]] after a one-year garden leave, with the package including upfront compensation, performance-based carry, and team-hiring budget — i.e., the standard layered structure described above.

Schurr's path through the industry is itself diagnostic of the talent flows: he worked at [[Point72]] and Kynikos Associates before joining [[Balyasny]] as a PM in 2021, was promoted to the firm's leadership team in 2023, then was poached by [[Millennium]] in 2025. Each move was reportedly negotiated with multiple bidders, and the FT-reported $100mn package is consistent with what other top PMs have received in 2024-2025.

Other proof points from the cold-research pass: Kevin Liu, a tech-focused stock picker, was signed by [[Point72]] in early 2025 after a bidding battle involving [[Citadel]], [[Millennium]], and [[Balyasny]] — package reportedly "tens of millions" over five years plus mentorship from [[Steve Cohen]]. The pattern of multi-firm bidding wars for senior PMs is now the industry's default mode of hiring at this level.

---

## What happens when the multi-managers cool

The FT article closes with a question the industry is asking openly: as multi-strategy returns converge toward industry averages in 2024-2025, can the pay packages persist? Two scenarios.

The bearish case: if pod-shop returns commoditise — the [[Multi-manager hedge funds|convergence pattern documented in the multi-manager hedge funds note]] — LPs eventually push back on pass-through costs, fee structures compress, and the headline PM packages contract. A "Mbappé will be paid less next year" quote in the FT pushed back on this, but the industry is watching 2026 carefully.

The bullish case for talent pay (bearish for hedge funds specifically): even if multi-managers cool, other capital pools are positioned to pick up the bidding. [[Jane Street]] (~$20bn capital, ~$20bn 2024 revenue) and [[Citadel Securities]] (separate from [[Citadel]] LLC) increasingly compete for the same trader profiles, with proprietary capital and partnership-equity economics that hedge funds cannot match. Family offices like [[BlueCrest]] — Michael Platt's $50-60bn proprietary vehicle, up 73% in 2025 — sit on capital they can deploy on talent without LP pressure.

The dominant industry executive view, as quoted in the FT: pay "will keep increasing every year; it's just the market." The market here is the durable scarcity of PMs who can generate consistent high-Sharpe trading profits, which is a smaller pool than the number of firms competing for them. Until that imbalance reverses, the bidding war continues — and the structural choice for capital allocators becomes whether to compete in the talent bid or accept being on the wrong side of it.

---

## Critique — where the model strains

| Critique | Detail |
|---|---|
| Fee drag on LPs | 7-15% effective fees in pass-through years; Balyasny Atlas Enhanced 2023 net 2.8% on 15.2% gross |
| Misalignment | PM with $60mn cash advance has reduced incentive in year-one performance |
| Above/below-line games | Negotiated expense classification creates non-transparent compensation variance |
| Career-arbitrage culture | PMs hop firms every 3-5 years for re-negotiation; reduces loyalty incentive |
| Crowding | 300+ pods across 6 firms tend to converge on similar trades, eroding alpha |
| Talent pool exhaustion | Limited number of PMs who can produce the returns to justify the packages |

The dominant critique LPs articulate is the first one — total fees can consume most of the gross return, particularly in soft years. The dominant critique allocators articulate among themselves is the last one — the talent pool may not be deep enough to support the scale at which capital has flowed into the model.

---

## Related

### Parent concept
- [[Multi-manager hedge funds]] — the pod-shop structure this compensation model operates within

### Firms using this structure
- [[Millennium]] — pioneer, where [[Steve Schurr]] landed for ~$100mn in 2025
- [[Citadel]] — Ken Griffin, also competing aggressively in the talent war
- [[Balyasny]] — Schurr's origin firm before the Millennium move
- [[Point72]] — Steve Cohen, signed Kevin Liu after a bidding battle
- [[ExodusPoint]] — Michael Gelband (ex-Millennium), pod-shop peer
- [[Schonfeld]] — pod-shop peer

### Alternative bidders for talent
- [[Jane Street]] — proprietary trading firm increasingly competing for the same profiles
- [[Citadel Securities]] — Citadel's market-making arm, separate from the hedge fund
- [[BlueCrest]] — [[Michael Platt]]'s family office, $50-60bn proprietary, +73% in 2025

### People
- [[Steve Schurr]] — Balyasny → Millennium ~$100mn move (Apr 2025), the FT framing data point
- [[Izzy Englander]] — Millennium founder, the offering hand
- [[Michael Platt]] — BlueCrest founder, alternative-bidder example

### Adjacent concepts
- [[Stock-based compensation]] — different mechanism, similar dynamics in tech
- [[Hedge fund capital concentration]] — the LP-flow side of pod-shop dominance
- [[Statistical arbitrage]] — the strategy space where stat-arb pods most directly use the structure

---

Sources:
- [FT — How top hedge funds can pay traders $100mn](https://www.ft.com/content/4e56e245-93e5-4129-9972-602abe3dbd23) (Costas Mourselas, Sept 22 2025) — primary source for the worked example and infographics
- [Bloomberg — Millennium Poaches Balyasny's Schurr With $100 Million Offer](https://www.bloomberg.com/news/articles/2025-04-29/millennium-poaches-balyasny-s-schurr-with-100-million-offer) — primary Schurr confirmation
- [Bloomberg — Growing List of Hedge Fund Passthrough Fees Cuts Into Client Profits](https://www.bloomberg.com/graphics/2025-hedge-fund-investment-fees/) — pass-through prevalence and LP cost
- [Hedgeweek — Multi-manager hedge funds escalate talent war 'arms race' with nine-figure pay packages](https://www.hedgeweek.com/multi-manager-hedge-funds-escalate-talent-war-arms-race-with-nine-figure-pay-packages/) — accelerator and 24.5% profit-share confirmation
- [Wall Street Oasis — Economics of pass through MM](https://www.wallstreetoasis.com/forum/hedge-fund/economics-of-pass-through-mm) — Balyasny Atlas Enhanced 2023 net-of-fees data point
- [INSEAD Knowledge — The Rise of the "Pod Shop"](https://knowledge.insead.edu/economics-finance/rise-pod-shop) — academic framing

*Created 2026-05-19*
