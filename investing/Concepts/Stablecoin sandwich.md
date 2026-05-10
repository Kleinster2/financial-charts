---
aliases: [stablecoin sandwich, fiat-stablecoin-fiat]
tags: [concept, payments, stablecoin, fintech, remittance]
created: 2026-05-10
---

# Stablecoin sandwich

The stablecoin sandwich is the operating model for using a stablecoin as the middle layer of a fiat-to-fiat cross-border transfer. A sender hands over local currency in country A, an on-ramp converts it to a USD-pegged stablecoin like [[Circle|USDC]] or [[Tether|USDT]], the stablecoin moves across a blockchain to a partner in country B, and an off-ramp converts it back to country B's local currency for delivery. The blockchain leg is structurally invisible to the end user — the sender sees their dollars on the app, the receiver sees their pesos or reais in a local wallet or bank account. The mechanism's value comes from collapsing the multi-day correspondent-banking chain into seconds, eliminating the 3-5% FX markup that traditional cross-border banking imposes, and giving each country's local liquidity a direct on/off ramp to the dollar without needing reciprocal banking relationships.

The name describes the structural pattern — fiat slice on either end, stablecoin filling in the middle — and is now canonical across the payments-infrastructure industry, used by [[Stripe]], [[Circle]], Fipto, BVNK, and Dynamic.xyz in their own documentation.

---

## Mechanism

| Step | Action | Operator type | Economics |
|------|--------|---------------|-----------|
| 1. On-ramp | Local fiat → stablecoin in country A | Licensed payment institution, money transmitter, or local crypto exchange | Captures local FX spread |
| 2. Cross-border transfer | Stablecoin moves across blockchain to country B partner | Blockchain (Ethereum, Solana, Tron, Base, Arc) | Per-transaction gas fee, typically <$0.05 |
| 3. Off-ramp | Stablecoin → local fiat in country B | Licensed payment institution or local crypto exchange | Captures local FX spread |

Total user-facing cost is the sum of two FX spreads (which can be tight when local liquidity is deep) plus near-zero on-chain transfer cost — versus correspondent banking's stacked correspondent fees, lifting fees, and central FX markup.

---

## Why it works

Three structural advantages over correspondent banking:

1. Liquidity is sourced locally on each end. The on-ramp shop only needs deep liquidity in its own currency-to-USDC market; the off-ramp shop only needs deep liquidity in USDC-to-its-currency. Neither needs a reciprocal banking relationship with the other's banks.
2. Settlement is irrevocable and near-instant on-chain. The correspondent banking model has T+1 to T+5 settlement risk; the sandwich has block-time finality (1-15 seconds on most chains).
3. The dollar leg is universal collateral. Stablecoin liquidity pools in USDC and USDT are deep against nearly every major fiat — a sender's USDT in Singapore can be off-ramped into Philippine pesos, Brazilian reais, Mexican pesos, or Nigerian naira without intermediate FX hops.

---

## The "$5M friction" framing

A sharp framing for where the stablecoin sandwich actually wins, from [[Matt Higginson]] (McKinsey) on Bloomberg TV (May 2026): you don't actually want a $5M transfer to be instant — the friction of correspondent banking is a feature that prevents costly mistakes on large transactions. Speed and irrevocability are pure downside on a treasury wire. But on a $200 remittance from a worker in New York to a family in Manila, every minute of delay and every dollar of friction is pure cost.

The implication: the stablecoin sandwich is a small-and-SMB cross-border instrument, not an enterprise treasury one. The competitive frontier is the under-$10K cross-border transfer where banking fees consume 2-8% of the principal — exactly the corridor where remittance is dominant.

---

## Cost trajectory (Philippine corridor example)

The Philippine remittance corridor is the cleanest cost compression case, per [[Wei Zhou]] ([[Coins.ph]] CEO):

| Era | Cost per $1 | Mechanism |
|-----|------------|-----------|
| ~2015 | ~8% | Correspondent banking, Western Union, MoneyGram |
| ~2025 | 2-4% | App-based digital remitters ([[Remitly]], WorldRemit) |
| ~2026 stablecoin rail | ~0.5% (50 bps) | Stablecoin sandwich ([[Remitly]] / [[Coins.ph]]) |
| Target | 20-30 bps | Zhou's stated medium-term goal |

The compression math: Philippine annual remittance inflow is ~$35B (over 7% of GDP), so each 1% cost saved is ~$350M per year retained by workers and recipients rather than paid to intermediaries.

---

## Live operators

| Operator | Sender side | Receiver side | Stablecoin |
|----------|------------|--------------|-----------|
| [[Remitly]] + [[Coins.ph]] | US, GCC, Korea, Japan | Philippines (pesos) | USDC (likely primary) |
| [[PayPal]] Xoom | US | Multiple corridors | PYUSD / USDC routing |
| [[MoneyGram]] / Stellar | US | Multiple corridors | USDC on Stellar |
| Bitso Business | LatAm + global | Brazil, Mexico, Argentina | USDC, USDT |
| [[Stripe]] Bridge | Enterprise B2B global | Multiple corridors | USDC (post-Bridge acquisition) |
| BVNK | Enterprise B2B global | Multiple corridors | USDC, USDT |

Other notable corridors where the sandwich is dominant or emerging: Mexico/LatAm USD remit corridors (via Bitso and Tron-routed USDT), Brazil/Argentina dollar-access flows (now formally classified as FX operations under BCB resolutions), Turkey/Nigeria/GCC remit corridors with high USDT throughput.

---

## Stablecoins as conduit, not destination

A key strategic framing from [[Wei Zhou]] and reinforced by [[Sebastian Gunningham]] ([[Remitly]] CEO): receivers in the destination market generally do not want to hold stablecoin balances themselves. They want dollar-denominated financial services at home — but in a familiar app or bank format, not in a crypto wallet they have to learn to manage. So the stablecoin is the conduit, not the destination — invisible plumbing that lets a peso-to-dollar service exist without needing a peso/dollar correspondent banking relationship.

The corollary is that growth in the sandwich does not require crypto adoption to grow. It requires only that the back-end routing economics keep beating correspondent banking, and that the front-end UX continues to abstract the blockchain layer away.

---

## Risk surface

| Risk | Description |
|------|------------|
| Reserve quality | If the stablecoin in the middle de-pegs mid-transit, the receiver gets less than the sender sent (UST collapse May 2022 is the case study) |
| Regulatory disconnect | Sender country and receiver country may apply different stablecoin rules — US [[GENIUS Act]] requires 1:1 reserves but Brazil treats stablecoin remit as FX operations |
| Issuer concentration | [[Tether]] / [[Circle]] dominance means most sandwiches route through ~2 issuers; an issuer-level event ripples across all corridors using its stablecoin |
| Off-ramp liquidity | Thin local currency pairs (e.g. niche African corridors) may have wider USDC-to-local spreads than correspondent banking when corridor volume is small |
| Compliance gaps | KYC/AML on the on-ramp and off-ramp must be sufficient — failure on either end exposes the corridor to enforcement risk |

---

## Why this isn't a card-network threat

The stablecoin sandwich competes against correspondent banking and traditional remitters, not against [[Visa]]/[[Mastercard]] consumer checkout. The latter is protected by consumer credit extension, chargebacks, and the ~$150B interchange pool — none of which apply to remittance flows. The two systems are structurally different markets that happen to overlap on the "moving money across borders" label.

See [[Stablecoins]] for the broader stablecoin-as-payment-rail thesis.

---

## Related

### Operating examples
- [[Coins.ph]] — Philippine off-ramp operator
- [[Remitly]] — US/global sender, selective stablecoin rail routing
- [[Stripe]] — Bridge subsidiary, enterprise B2B sandwich
- [[PayPal]] — Xoom retail operator, PYUSD and USDC routing
- [[MoneyGram]] — Stellar/USDC operator
- [[Circle]] — USDC issuer, also direct payment network (CPN)
- [[Tether]] — USDT issuer, dominant in offshore/EM sandwich routes

### Parent and sibling concepts
- [[Stablecoins]] — parent ecosystem
- [[Cross-border payments]] — broader category
- [[Crypto]] — sector context
- [[Fintech]] — adjacent industry frame

### Research and measurement
- [[Matt Higginson]] — McKinsey, $5M friction framing
- [[Artemis Analytics]] — measurement infrastructure
- [[McKinsey]] — Feb 2026 stablecoin payments paper (with Artemis)

### Regulatory
- [[GENIUS Act]] — US framework, enables compliant sandwich legs
- [[MAS]] — Singapore framework
- [[MiCA]] — EU framework
- [[Brazilian real stablecoins]] — Brazil's FX-operations classification
- [[Sopnendu Mohanty]] — Singapore architectural framing

### Corridors
- [[Philippines]] — flagship sandwich corridor
- [[Brazil]] — FX-classified, yield-bearing stablecoin variant
