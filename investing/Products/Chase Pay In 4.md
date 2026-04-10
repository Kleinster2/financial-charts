---
aliases:
  - Chase Pay in 4
  - Chase BNPL
  - JPMCB BNPL
---
#product #bnpl #fintech #usa

**Chase Pay In 4** -- [[JPMorgan Chase]]'s debit-card BNPL product. Splits eligible purchases into 4 interest-free biweekly payments. Launched 2024.

| Metric | Value |
|--------|-------|
| Parent | [[JPMorgan Chase]] |
| Channel | Chase debit card (checking account) |
| Purchase range | $50--$400 |
| Max across active plans | $400 |
| Payments | 4 equal, biweekly |
| Interest | 0% |
| Fees | $0 on-time; $5 late/missed |
| Credit check | None |
| Credit bureau reporting | Yes (Experian, TransUnion) |
| Setup window | Within 7 days of purchase |
| Eligibility | Chase checking customer 6+ months, active debit card, 18+ |

---

## How it works

1. Customer makes a debit card purchase ($50--$400)
2. Within 7 days, selects "Pay in 4" in the Chase Mobile app or chase.com
3. Full purchase amount is refunded to checking account within 24 hours
4. Four equal payments debited biweekly, starting 2 weeks after setup

No payment is due at plan creation. The refund-then-recharge mechanic effectively converts a completed debit purchase into a short-term installment loan.

---

## Exclusions

Ineligible account types: Chase First Banking, High School Checking, Secure Banking, business accounts, J.P. Morgan Private Bank.

Ineligible purchases: cash-like transactions, payments to third-party BNPL providers ([[Affirm]], [[Klarna]], [[Afterpay]]).

---

## Strategic context

Chase Pay In 4 is one leg of [[JPMorgan Chase]]'s installment payment walled garden:

| Product | Channel | Amount | Term | Fee |
|---------|---------|--------|------|-----|
| Chase Pay In 4 | Debit card | $50--$400 | 8 weeks (4 biweekly) | $0 / $5 late |
| [[Chase Pay Over Time]] | Credit card | $100+ | 3--24 months | Up to 1.72%/mo |
| [[Klarna]] partnership | Merchant acquiring | Varies | Klarna terms | Processing fees to JPM |

The three products cover different segments: small debit purchases (Pay In 4), larger credit card purchases (Pay Over Time), and merchant-side checkout (Klarna via JPMorgan Payments' 900,000+ merchants).

In October 2024, Chase banned its credit cards from being used to repay third-party BNPL providers -- blocking [[Affirm]], [[Klarna]], and [[Afterpay]] at the consumer level while funneling installment demand into its own products. Then in February 2025, it partnered with [[Klarna]] on the merchant-acquiring side, making Klarna available through JPMorgan Payments' Commerce Solutions Platform ($2T+ annual transaction volume). The logic: block BNPL as a consumer credit competitor, embrace it as a checkout option that generates processing fees.

---

## Competitive landscape

| Provider | Type | Purchase limit | Late fees | Credit check | Merchant network |
|----------|------|----------------|-----------|--------------|-----------------|
| Chase Pay In 4 | Bank-issued (debit) | $400 | $5 | No | Any Chase debit purchase |
| [[Affirm]] Pay in 4 | Standalone BNPL | Varies by merchant | $0 | Soft pull | 300K+ merchants |
| [[Klarna]] Pay in 4 | Standalone BNPL | Up to $17,500 | Up to $7 | Soft pull | 500K+ merchants |
| [[Afterpay]] ([[Block]]) | Standalone BNPL | Varies ($2K typical) | Capped at 25% of installment | No | 100K+ merchants |
| [[Apple Pay]] Later | Platform BNPL | -- | -- | -- | Discontinued 2024 |

Chase's advantage is distribution: ~80M consumer checking accounts, no new app install, no separate credit application. The disadvantage is the $400 cap -- far below standalone BNPL providers -- and restriction to Chase debit card purchases only.

---

## Regulatory environment

The [[CFPB]] issued an interpretive rule in May 2024 classifying BNPL "pay-in-four" products as credit cards under Regulation Z, requiring dispute rights, refund obligations, and periodic billing statements. The rule was revoked under new CFPB leadership in March 2025, though the legal basis (BNPL = credit card under TILA) was not explicitly repudiated.

Chase Pay In 4, as a bank-issued product from a nationally chartered bank, is already subject to OCC supervision and federal consumer lending rules -- giving it a regulatory advantage over fintech BNPL providers that faced the interpretive rule as new compliance burden.

---

## Market context

US BNPL market (all providers):

| Metric | Value |
|--------|-------|
| 2023 originations | 335.8M loans, $45.2B |
| 2023 pay-in-4 volume | $43.9B (up from $2.2B in 2019) |
| 2025 estimated total | ~$70B (~1.1% of credit card spending) |
| Growth rate | ~20%/year since 2021 |
| Active BNPL users (2023) | 53.6M |

Bank-issued BNPL (card-linked installments from [[JPMorgan Chase]], [[Citigroup]], [[Bank of America]]) is the fastest-growing segment and the primary competitive threat to standalone fintech BNPL providers.

---

## Related

- [[JPMorgan Chase]] -- parent (largest US bank, ~80M consumer accounts)
- [[Chase Pay Over Time]] -- sibling product (credit card installments)
- [[Klarna]] -- partner (merchant acquiring) and blocked competitor (consumer credit)
- [[Affirm]] -- competitor (standalone BNPL leader)
- [[Afterpay]] -- competitor (acquired by [[Block]])
- [[Apple Pay]] -- Apple Pay Later discontinued 2024; shifted to bank partnerships
- [[Payments Networks]] -- BNPL as structural threat to traditional card economics
- [[Fintech]] -- sector context
