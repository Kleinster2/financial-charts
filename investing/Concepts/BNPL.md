---
aliases:
  - Buy Now Pay Later
  - buy now pay later
  - pay-in-four
  - pay in 4
  - installment payments
---
#concept #fintech #payments #consumer

**BNPL** (Buy Now, Pay Later) -- consumer credit model that splits purchases into interest-free installments at checkout. Originated as fintech disruptor of credit cards; now being absorbed by the banks it was designed to bypass.

---

## How it works

The canonical BNPL product is "pay-in-four": a purchase is split into 4 equal biweekly payments over 6-8 weeks, with no interest and no credit check. The merchant pays a fee (3-8% of transaction value) to the BNPL provider, who assumes the credit risk and pays the merchant upfront.

Variations include longer-term installments (3-60 months, often with interest), debit-linked plans, and card-linked installments from traditional banks.

---

## Market size

### US

| Metric | Value | Source |
|--------|-------|--------|
| 2019 pay-in-4 volume | $2.2B | [[CFPB]] |
| 2023 originations | 335.8M loans, $45.2B | [[CFPB]] Dec 2025 report |
| 2023 pay-in-4 volume | $43.9B | [[CFPB]] |
| 2023 active users | 53.6M (6.3 loans/user/year) | [[CFPB]] |
| 2023 avg loan size | $135 (inflation-adjusted) | [[CFPB]] |
| 2025 estimated volume | ~$70B (~1.1% of credit card spend) | Richmond Fed |
| 2025 estimated users | 91.5M | eMarketer |
| Growth rate (2021-2025) | ~20%/year, decelerating | Multiple |

### Global

| Metric | Value |
|--------|-------|
| 2025 projected GMV | $560B |
| 2024 provider revenue | ~$19B |
| 2025 projected revenue | ~$23B |
| Largest region | Asia-Pacific (36.4% of revenue) |
| North America share | 29-32% of revenue |
| 2027 projected users | ~900M |

---

## Key players

### Fintech BNPL

| Provider | Revenue (2024) | Key metric | Status |
|----------|----------------|------------|--------|
| [[Klarna]] | $2.8B | ~35% global market share, 150M users | IPO filed ([[NYSE]]) |
| [[Affirm]] | $2.3B | 377K merchants, $25B+ GMV | Public (AFRM) |
| [[PayPal]] | -- | $33B global BNPL volume | Most commonly used (56% of US BNPL users) |
| [[Afterpay]] ([[Block]]) | -- | 348K merchants | Acquired 2022 ($29B) |
| [[Sezzle]] | -- | Highest fintech satisfaction (624/1000) | Public (SEZL) |
| [[Zip]] | -- | Australia/US | Public (ASX: ZIP) |

Top 6 providers account for ~94% of US BNPL lending ([[CFPB]]).

### Bank-issued (card-linked installments)

| Provider | Product | Channel | Limit |
|----------|---------|---------|-------|
| [[JPMorgan Chase]] | [[Chase Pay In 4]] | Debit | $50-$400 |
| [[JPMorgan Chase]] | [[Chase Pay Over Time]] | Credit | $100+ |
| [[Citigroup]] | Citi Flex Pay | Credit | Varies |
| [[American Express]] | Plan It | Credit | Varies |
| [[Bank of America]] | -- | Credit | Varies |

Bank-issued card-linked installments consistently outrank fintech BNPL on customer satisfaction: [[JPMorgan Chase|Chase]] leads at 706/1000 vs Sezzle's 624 for the highest-scoring fintech (J.D. Power).

---

## The bank absorption

BNPL started as a fintech assault on credit card economics. It is now being absorbed by the banks:

1. [[Apple Pay]] Later launched 2023, discontinued June 2024. [[Apple]] shifted to a partner model -- [[Affirm]], [[Citigroup|Citi]], [[HSBC]], [[Monzo]], Fiserv -- rather than owning credit risk. If Apple can't justify BNPL balance sheet risk, standalone BNPL is structurally disadvantaged.

2. [[JPMorgan Chase]] built a walled garden: own BNPL products ([[Chase Pay In 4]], [[Chase Pay Over Time]]), banned third-party BNPL on Chase credit cards (Oct 2024), then partnered with [[Klarna]] on merchant acquiring (Feb 2025). Block competitors at the consumer level, embrace them where they generate processing fees.

3. Bank advantages are structural: lower cost of capital (deposits vs VC funding), existing customer relationships (~80M checking accounts for Chase alone), regulatory status (nationally chartered banks already supervised by OCC), and no new app install required.

4. Fintech disadvantages are also structural: profitability pressure (most BNPL fintechs were unprofitable through 2023), merchant fee compression, credit losses in economic downturns, and regulatory convergence (CFPB classification as credit cards means compliance burden).

The market is bifurcating: banks are capturing prime/near-prime consumers and higher-ticket installments, while fintechs retain low-ticket impulse retail and subprime access.

---

## Credit quality

| Metric | Value | Context |
|--------|-------|---------|
| BNPL delinquency rate | <2% | vs 3.5% all consumer debt, 8.8% credit cards |
| Klarna delinquency | 0.88% (Q2 2025) | Down from 1.03% Q2 2024 |
| Affirm 90+ day delinquency | 0.7% (Dec 2024) | -- |
| Charge-off rate | 1.83% (2023) | Down from 2.63% (2022) |
| Late fee incidence | 4.1% of loans (2023) | Down from 5.2% (2022) |
| Users with late payment | 42% (2025) | Up from 34% (2023) |

The divergence between low official delinquency rates and rising late payment self-reporting reflects measurement gaps. Most BNPL loans are not reported to credit bureaus, creating "phantom debt" invisible to other lenders. A consumer can stack multiple BNPL obligations across providers without any single lender seeing the full picture.

BNPL approval rates rose from 56% (2019) to 79% (2022) as providers made more counteroffers and approved more subprime borrowers -- widening the credit box during a period of easy money.

---

## Regulatory timeline

| Date | Event |
|------|-------|
| 2020-2023 | [[CFPB]] opens market monitoring orders to major BNPL providers |
| Sep 2022 | [[CFPB]] publishes first BNPL market report |
| May 2024 | [[CFPB]] interpretive rule: BNPL classified as credit cards under Reg Z/TILA |
| Jul 2024 | Interpretive rule effective -- requires dispute rights, refund obligations, billing statements |
| Oct 2024 | [[JPMorgan Chase]] bans third-party BNPL payments on Chase credit cards |
| Mar 2025 | [[CFPB]] (new leadership) files intent to revoke interpretive rule |
| Jun 2025 | [[CFPB]] confirms no revised rule ("procedurally defective") |
| Dec 2025 | [[CFPB]] publishes updated market report (335.8M loans, $45.2B in 2023) |

International: [[EU]] Consumer Credit Directive (2023) requires BNPL providers to conduct creditworthiness assessments. [[Australia]] (Treasury) proposed regulation in 2024 to bring BNPL under the National Credit Act.

The regulatory pendulum: the May 2024 CFPB rule would have imposed credit card-level consumer protections on BNPL. Its revocation leaves BNPL in a regulatory gray zone -- not quite credit cards, not quite unregulated. Bank-issued BNPL products face no incremental burden (already supervised), giving them a structural advantage over fintechs in a tightening regulatory environment.

---

## Origins

| Year | Event |
|------|-------|
| Early 1900s | Department store layaway and catalog installment plans (Sears) |
| 2005 | [[Klarna]] founded in Stockholm |
| 2012 | [[Affirm]] founded by [[Max Levchin]] (PayPal Mafia) |
| 2014 | [[Afterpay]] founded in Sydney |
| 2016 | Klarna launches BNPL feature, gains international recognition |
| 2020-2021 | COVID e-commerce boom drives BNPL adoption; pay-in-4 volume 20x from 2019 |
| Jan 2022 | [[Block]] acquires [[Afterpay]] for $29B |
| 2023-2024 | Bank-issued alternatives proliferate; Apple Pay Later launches and dies |
| 2024-2025 | Regulatory cycle (CFPB rule, then revocation); market consolidation |

---

## Investment implications

BNPL is not a standalone sector thesis anymore -- it's a feature being commoditized into existing payments infrastructure. The question is who captures the margin:

- [[Klarna]] IPO is the test case: can a BNPL-native company sustain premium valuation as banks offer equivalent products with lower CAC?
- [[Affirm]] trades on GMV growth but faces merchant fee pressure and bank competition on the prime segment
- [[JPMorgan Chase]], [[Citigroup]], [[American Express]] benefit from BNPL as a retention/engagement feature on existing cards -- incremental margin, not a new business
- [[Payments Networks]] ([[Visa]], [[Mastercard]]) are enablers regardless of who wins -- installment routing is volume for the networks

The structural winner is whoever owns the checkout moment. Banks own the card. Fintechs own the app. The battle is over which relationship the consumer defaults to.

---

## Related

- [[Chase Pay In 4]] -- bank-issued debit BNPL ([[JPMorgan Chase]])
- [[Chase Pay Over Time]] -- bank-issued credit card installments ([[JPMorgan Chase]])
- [[Klarna]] -- largest BNPL provider globally, IPO candidate
- [[Affirm]] -- US BNPL leader by merchant count
- [[Afterpay]] -- acquired by [[Block]] (2022, $29B)
- [[PayPal]] -- most commonly used BNPL in US (56% of users)
- [[Apple Pay]] -- Apple Pay Later discontinued 2024; shifted to bank partnerships
- [[CFPB]] -- regulatory authority (interpretive rule issued May 2024, revoked 2025)
- [[Fintech]] -- sector context
- [[Payments Networks]] -- card networks as infrastructure layer
- [[Fintech boom (2020-2021)]] -- historical context (BNPL adoption wave)
- [[Credit card rate cap]] -- related consumer credit policy risk
