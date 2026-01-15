# Databases

Technology trends and architectural shifts in database infrastructure.

## Foundational theory

**ACID properties** — guarantees for reliable transactions:
- **Atomicity** — transactions fully complete or fully rollback
- **Consistency** — data remains valid after transactions
- **Isolation** — concurrent transactions don't interfere
- **Durability** — committed data survives failures

**CAP theorem** — distributed systems can only guarantee two of three:
- **Consistency** — all nodes see same data simultaneously
- **Availability** — every request gets a response
- **Partition tolerance** — system works despite network failures

*Investment implication:* CAP tradeoffs explain why different databases exist. OLTP systems (Postgres) prioritize consistency; distributed NoSQL (Cassandra, DynamoDB) often trade consistency for availability.

## Key dynamics

- **Cloud migration** — on-prem to managed services (AWS RDS, Azure SQL, GCP Cloud SQL)
- **Separation of storage and compute** — enables elastic scaling, pay-per-query models
- **Real-time analytics** — OLTP/OLAP convergence, streaming ingestion
- **Vector databases** — embedding storage for AI/ML workloads, RAG applications
- **Open source pressure** — [[Postgres]] ecosystem expanding, commoditizing proprietary features

## Architectural categories

| Category | Examples | Use case |
|----------|----------|----------|
| OLTP | Postgres, MySQL, CockroachDB | Transactional workloads |
| OLAP | Snowflake, Databricks, ClickHouse | Analytics, data warehousing |
| Document | MongoDB, Couchbase | Flexible schemas, JSON |
| Vector | Pinecone, Weaviate, Chroma | AI embeddings, similarity search |
| Time-series | InfluxDB, TimescaleDB | IoT, metrics, observability |

## AI implications

- LLM context windows expanding but RAG still needed for proprietary data
- Vector DB demand tied to enterprise AI adoption curve
- Databricks/Snowflake competing to own AI data layer

## Related

- [[Database companies]] — investable sector hub
- [[Postgres]] — dominant open source ecosystem
- [[Supabase]] — Postgres-based BaaS, open source Firebase alternative
- [[Neon]] — serverless Postgres, acquired by Databricks
- [[PlanetScale]] — serverless MySQL, built on Vitess
- [[Data gravity]] — switching cost dynamics
- [[Data lakehouse]] — warehouse/lake convergence
- [[Vector databases]] — AI embedding storage
- [[Modern data stack]] — ecosystem context
- [[Streaming data]] — real-time processing
- [[AI infrastructure financing]] — capital flows into AI data stack
