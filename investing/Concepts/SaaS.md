---
aliases: [Software as a Service, Cloud Software, Software-as-a-service, Subscription software]
---
#concept #business-model #software #cloud

**SaaS** — Software as a Service. A delivery and pricing model where software is hosted centrally and sold as a subscription rather than a perpetual license. The defining characteristic is recurring revenue — which drives premium valuations, predictable cash flows, and high switching costs.

---

## Why SaaS commands premium valuations

Recurring revenue changes the economics of software:

| Property | Perpetual license | SaaS subscription |
|----------|-------------------|-------------------|
| Revenue recognition | Upfront lump sum | Spread over contract |
| Customer relationship | Ends at sale | Continuous |
| Switching costs | Low (own the software) | High (data, workflows, integrations) |
| Gross margins | 50-70% | 75-85% |
| Expansion revenue | Requires new sale | Upsell within account (NRR) |
| Typical EV/Revenue | 1-3x | 5-15x |

The valuation premium exists because a SaaS company with 120% NRR grows even if it signs zero new customers. See [[Cloud vs on-premise valuation]] for the full framework.

---

## Market size

| Year | Size | Growth |
|------|------|--------|
| 2025 | $408-429B | — |
| 2026 | $418B+ | ~18% CAGR |
| 2034 | $1.25-1.48T | 18.7% CAGR |

99% of businesses use at least one SaaS solution. Average org uses 112 SaaS apps (vs 16 in 2017).

Regional: North America 47% (~$212B), Europe ~25%, APAC ~20% (fastest growth), RoW ~8%.

---

## Key metrics

See [[SaaS metrics]] for full definitions, formulas, and benchmarks.

| Metric | What it measures | Good target |
|--------|-----------------|-------------|
| NRR (Net Revenue Retention) | Expansion vs churn from existing customers | >120% |
| Gross margin | Scalability | >75-80% |
| Rule of 40 | Growth + FCF margin balance | >40% |
| Magic number | Sales efficiency | >0.75-1.0x |
| CAC payback | Cash flow velocity | <12 months |
| LTV/CAC | Unit economics | >3x |

---

## AI disruption risk (Feb 2026 repricing)

The market is repricing which SaaS categories survive AI agents:

- AI-native revenue becoming material ([[Datadog]] 11%+)
- Agents replacing traditional workflows — [[Anthropic]] and [[OpenAI]] repositioned as general-purpose agent platforms
- Feb 2026 selloff: large-cap SaaS -25% to -40% YTD, workflow tools (MNDY, BRZE) -49% to -51%, while SPY flat
- Financial Times framework: non-essential workflow SaaS (highest risk) vs systems of record (medium) vs agent infrastructure (beneficiary)
- See [[SaaS stock meltdown 2026]] for full data and charts

---

## China structural differences

China's SaaS market operates under fundamentally different dynamics:

- Cheap engineering talent inverts build-vs-buy — in the US, a $50/seat/month SaaS tool beats diverting a $200K/year engineer to build internally; in China, large enterprises (especially SOEs) maintain huge IT departments that build custom solutions for less than the subscription would cost
- Lower ARPUs — the build-vs-buy inversion means SaaS vendors can't charge US-level prices even though their own labor costs are also lower
- Platform bundling — [[WeChat]]/[[DingTalk]]/[[Feishu]] bundle SaaS-like tools for free, compressing standalone TAM
- Government/SOE customers dominate enterprise spend, creating lumpy, relationship-driven sales cycles
- [[Xinchuang]] (foreign software replacement mandate) creates captive demand for domestic vendors through 2027
- Nearly all Chinese SaaS companies hit profitability inflection in 2025-2026 after years of cloud transition losses
- Key players: [[Kingdee International]], [[Yonyou Network]], [[Kingsoft Office]], [[Glodon]], [[Beisen]], [[Ming Yuan Cloud]], [[Weimob]], [[Youzan]], [[Sangfor Technologies]]

---

## Segment taxonomy

| Segment | Value proposition | AI exposure | Examples |
|---------|-------------------|-------------|----------|
| **Horizontal** | Broad business functions across industries (CRM, HR, ITSM) | High — agents commoditize the workflow UI | [[Salesforce]], [[Workday]], [[ServiceNow]] |
| **Vertical** | Industry-specific, deeply embedded, often regulatory-driven | Low — domain knowledge + compliance = durable moat | Veeva, Procore, Toast, [[Shopify]] (commerce vertical) |
| **Infrastructure** | Data plumbing, monitoring, developer tools | Beneficiary — more AI = more infra demand | [[Snowflake]], [[Datadog]], [[Confluent]], [[Supabase]] |
| **Collaboration** | Team coordination, project management, messaging | High — AI agents replace the "coordination tax" | Slack, [[Notion]], Asana, Monday |
| **SMB** | Small business operations (payments, payroll, storefront) | High — simple workflows, price-sensitive customers | [[Block]], Gusto, [[Shopify]] |

See [[AI SaaS Disruption]] for full analysis of how AI disrupts each segment differently, including the China leapfrog risk.

---

## Correlation structure

SaaS is far less monolithic than the market treats it. 252-day rolling correlations reveal distinct clusters:

### Individual stock vs IGV (SaaS ETF)

| Ticker | Company | Segment | vs IGV | vs SPY | vs QQQ |
|--------|---------|---------|--------|--------|--------|
| WDAY | [[Workday]] | Systems of record | 0.29 | -0.10 | -0.07 |
| PANW | [[Palo Alto Networks]] | Security | 0.21 | 0.11 | 0.13 |
| NOW | [[ServiceNow]] | Workflow | 0.18 | 0.15 | 0.17 |
| MNDY | Monday.com | Workflow | 0.17 | -0.17 | -0.11 |
| BRZE | Braze | Comms | 0.17 | 0.04 | 0.04 |
| CRWD | [[CrowdStrike]] | Security | 0.14 | 0.05 | 0.06 |
| ZS | [[Zscaler]] | Security | 0.14 | 0.05 | 0.09 |
| CRM | [[Salesforce]] | Systems of record | 0.13 | 0.15 | 0.16 |
| DDOG | [[Datadog]] | Infrastructure | 0.12 | 0.06 | 0.08 |
| ADBE | [[Adobe]] | Creative | 0.11 | 0.08 | 0.06 |
| HUBS | [[HubSpot]] | Comms | 0.10 | -0.02 | 0.01 |
| PLTR | [[Palantir]] | Analytics | 0.09 | -0.01 | 0.02 |
| SNOW | [[Snowflake]] | Infrastructure | 0.08 | 0.09 | 0.12 |
| SHOP | [[Shopify]] | SMB | 0.02 | 0.04 | 0.02 |
| SAP | [[SAP]] | Systems of record | 0.02 | 0.30 | 0.32 |
| SQ | [[Block]] | SMB | 0.00 | 0.04 | 0.02 |
| ORCL | [[Oracle]] | Systems of record | -0.02 | 0.05 | 0.06 |

*Notably low correlations across the board.* IGV is a poor proxy for any individual SaaS name. SAP correlates more with SPY (0.30) than with its own sector ETF (0.02) — it's a European industrial bellwether, not a growth SaaS stock.

### Intra-segment clustering

| Segment | Stocks | Avg pairwise r | Interpretation |
|---------|--------|----------------|----------------|
| Security | PANW, CRWD, ZS | **0.67** | Tightest cluster. Trades as a group. |
| Infrastructure | SNOW, DDOG | **0.62** | Strong co-movement. Data infra basket. |
| Systems of record | CRM, WDAY, SAP, ORCL | **0.11** | Barely correlated. SAP/ORCL trade like value; CRM/WDAY trade like growth. |
| SMB | SHOP, SQ | **0.00** | Zero correlation. Different businesses wearing the same label. |

**Key insight:** "SaaS" is not a coherent sector for portfolio construction. Security and infrastructure cluster tightly and can be traded as baskets. Systems of record and SMB are idiosyncratic — each stock trades on its own fundamentals. The Feb 2026 selloff hit them all indiscriminately, which created dispersion opportunities for investors who understood the segment differences.

*Data: 252-day rolling returns, market_data.db as of March 14, 2026*

---

## Investment themes

- Vertical SaaS — industry-specific solutions with higher switching costs and deeper workflow integration
- Consolidation — platform expansion ([[Salesforce]], [[ServiceNow]]), tuck-in acquisitions for AI, vertical roll-ups
- Multi-cloud — enterprise flexibility demands, vendor diversification

---

## Risks

| Risk | Impact |
|------|--------|
| AI disruption | Agents commoditize workflow tools |
| Macro sensitivity | Enterprise spending cuts hit discretionary SaaS first |
| Valuation compression | Rising rates reduce NPV of future cash flows |
| Hyperscaler bundling | [[Microsoft]], [[Google]], [[Amazon]] bundle SaaS features into platform |
| Customer budget fatigue | 112 apps per org is unsustainable |

---

## Related

- [[SaaS metrics]] — ARR, NRR, Rule of 40, unit economics
- [[Cloud vs on-premise valuation]] — why SaaS trades at 5-15x vs 1-3x
- [[SaaS stock meltdown 2026]] — Feb 2026 AI-driven repricing
- [[Xinchuang]] — China's foreign software replacement mandate
- [[Enterprise AI adoption]] — AI trend reshaping SaaS

*Created 2026-01-09, restructured 2026-02-24*
