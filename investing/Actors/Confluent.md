---
aliases: [Apache Kafka company]
---
#actor #software #data #usa #acquired

Confluent — Commercial steward of Apache Kafka, the dominant real-time data streaming platform. Founded by Kafka's creators at [[LinkedIn]]. Acquired by [[IBM]] for $11B (March 2026). Delisted from Nasdaq.

---

## Synopsis

Confluent was the company behind Apache Kafka — the open-source distributed event streaming platform that became the backbone of real-time data infrastructure at virtually every large enterprise. Co-founded in 2014 by Jay Kreps, Jun Rao, and Neha Narkhede — the three [[LinkedIn]] engineers who created Kafka — Confluent commercialized the technology through managed cloud services (Confluent Cloud) and an enterprise on-premise distribution (Confluent Platform). By 2025, the company had ~$1B in subscription revenue, 4,900+ customers, and 1,400+ customers spending $100K+ in ARR. Cloud revenue was growing 28-38% YoY, and the platform was expanding into stream processing (Apache Flink), data governance, and AI-adjacent use cases like RAG pipelines and streaming agents.

[[IBM]] announced the acquisition on December 8, 2025 for $31/share ($11B enterprise value, 34% premium). The deal closed March 17, 2026 — unusually fast, with HSR clearing without a second request. IBM's thesis: agentic AI systems need real-time data streams, and owning the Kafka commercial ecosystem gives IBM the "data fabric" layer between its hybrid cloud (Red Hat) and AI platform (watsonx). Confluent is now absorbed into IBM's Data and AI division.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Former ticker | CFLT (Nasdaq; delisted Mar 17, 2026) |
| Acquirer | [[IBM]] |
| Deal value | **$11B** ($31/share, all-cash) |
| Revenue (FY2024) | ~$777M |
| Cloud revenue growth | 28-38% YoY (2025) |
| Customers | 4,900+ |
| $100K+ ARR customers | 1,412 (Q1 2025) |
| Founded | 2014 |
| IPO | June 2021 |
| Founders | Jay Kreps, Jun Rao, Neha Narkhede |

---

## What Confluent built

Apache Kafka is the de facto standard for real-time event streaming:
- Created at [[LinkedIn]] (2011), open-sourced to Apache
- Processes trillions of events per day across enterprises globally
- Used by 80%+ of Fortune 100 companies

Confluent's product stack:

| Product | Purpose |
|---------|---------|
| Confluent Cloud | Fully managed Kafka-as-a-service |
| Confluent Platform | Self-managed enterprise distribution |
| Confluent Private Cloud | Hybrid deployment |
| WarpStream | Kafka-compatible, cloud-native (acquired) |
| Connectors | 200+ pre-built data integrations |
| Stream Governance | Schema registry, data quality, lineage |
| Flink (stream processing) | Real-time transformations and analytics |
| Tableflow | Topics → Iceberg/Delta Lake tables |
| Confluent Intelligence | Real-time context-aware AI |
| Streaming Agents | AI agent automation on data streams |

---

## Financials

| Year | Total Revenue | Cloud Revenue | Cloud Growth | Subscription Revenue |
|------|--------------|---------------|-------------|---------------------|
| 2023 | ~$585M | ~$100M/qtr by Q4 | 46% YoY | — |
| 2024 | ~$777M | $138M (Q4) | 38% YoY | — |
| 2025 (Q1) | — | $143M | 34% | $261M (+26%) |
| 2025 (Q2) | — | $151M | 28% | $271M (+21%) |

Non-GAAP operating margin turned positive in Q2 FY2024 — three consecutive positive quarters by Q4. The shift to cloud was working: higher-margin, stickier, consumption-based revenue.

---

## Leadership

| Role | Person | Notes |
|------|--------|-------|
| CEO & co-founder | Jay Kreps | Co-created Kafka at LinkedIn |
| Co-founder | Jun Rao | Kafka co-creator |
| Co-founder | Neha Narkhede | Kafka co-creator, departed 2020 |

---

## IBM acquisition timeline

| Date | Event |
|------|-------|
| Dec 8, 2025 | IBM announces definitive agreement, $31/share (34% premium) |
| Jan 12, 2026 | HSR waiting period expires (no second request) |
| Feb 12, 2026 | Stockholders approve (~62% pre-pledged) |
| Mar 16, 2026 | Final day of CFLT trading on Nasdaq |
| Mar 17, 2026 | Deal closes. CFLT delisted. Absorbed into IBM Data and AI division. |

$1.1B in 0% convertible notes (due 2027) triggered Fundamental Change provisions — noteholders can require repurchase at par.

Employee RSUs converted to [[IBM]] equity awards for retention.

---

## Why IBM bought Confluent

IBM's thesis centers on [[Agentic AI]]:

1. Real-time data for AI agents — autonomous AI systems need live data streams to make decisions. Kafka is the plumbing.
2. Integrated stack — IBM now owns hardware (IBM Z) → data streaming (Confluent/Kafka) → AI (watsonx). Full vertical.
3. Enterprise lock-in — legacy enterprises migrating to cloud are already on Kafka. Owning the commercial entity locks them into the IBM ecosystem.
4. Competitive positioning — [[Amazon]] (MSK), [[Microsoft]] (Azure Event Hubs), and [[Google]] (Pub/Sub) all offer managed Kafka. With Confluent as a subsidiary, IBM controls the upstream technology.

---

## Competitive impact

Pressured by the deal:
- [[Snowflake]], [[MongoDB]] — competing against an integrated IBM stack
- [[Amazon]], [[Microsoft]] — their managed Kafka services now depend on a competitor's upstream technology
- Independent data streaming startups — IBM + Confluent is a formidable combo

IBM's promise: maintain open ecosystem, continue supporting multi-cloud. Market is skeptical — the incentives to favor IBM's cloud over competitors' are obvious.

---

## Cap table / Investors (pre-acquisition)

| Round | Amount | Valuation |
|-------|--------|-----------|
| Total raised | $1.3B | — |
| IPO (Jun 2021) | — | ~$9.1B (at IPO) |
| Peak market cap | ~$25B (late 2021) |
| Pre-deal trading | ~$23/share |
| Acquisition | $31/share | $11B EV |

Key investors: [[Benchmark]], [[Index Ventures]], [[Sequoia]], [[Coatue]]

---

## Related

- [[IBM]] — acquirer ($11B, March 2026)
- [[Apache Kafka]] — core technology
- [[Snowflake]] — competitor (data platform)
- [[MongoDB]] — competitor (data platform)
- [[Amazon]] — competitor (AWS MSK)
- [[Microsoft]] — competitor (Azure Event Hubs)
- [[Agentic AI]] — strategic rationale (real-time data for AI agents)
- [[AI consolidation]] — pattern (big tech acquiring data infrastructure)

### Sources
- [IBM Newsroom: Acquisition Announcement](https://newsroom.ibm.com/2025-12-08-ibm-to-acquire-confluent-to-create-smart-data-platform-for-enterprise-generative-ai) (Dec 8, 2025)
- [Confluent Blog: IBM to Acquire Confluent](https://www.confluent.io/blog/ibm-to-acquire-confluent/)
- [TipRanks: Deal Closes](https://www.tipranks.com/news/company-announcements/ibm-completes-confluent-acquisition-company-delists-from-nasdaq) (Mar 17, 2026)
