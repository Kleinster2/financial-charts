# Vector databases

Databases optimized for storing and querying high-dimensional embeddings — the core data structure for AI/ML applications.

## Theory

**What are embeddings?**
- Dense numerical representations of data (text, images, audio)
- Similar items have similar vectors (close in vector space)
- Enable semantic search, recommendations, RAG pipelines

**Why specialized databases?**
- Traditional indexes (B-trees) don't work for high-dimensional similarity
- Require approximate nearest neighbor (ANN) algorithms
- Trade exactness for speed at scale

## Market landscape

### Pure-play vector DBs (private)
- **Pinecone** — managed, serverless, largest funding (~$138M)
- **Weaviate** — open source core, hybrid search
- **Chroma** — developer-focused, lightweight
- **Qdrant** — Rust-based, open source
- **Milvus/Zilliz** — scalable, enterprise-focused

### Incumbent extensions
- **pgvector** — [[Postgres]] extension, "good enough" for many use cases
- **MongoDB Atlas Vector Search** — [[MongoDB]] adding vector capabilities
- **Elasticsearch** — dense vector search added
- **[[Snowflake]]** / **[[Databricks]]** — adding vector features

## Investment thesis

**Bull case:**
- AI adoption = vector DB demand (RAG is everywhere)
- Specialized DBs outperform general-purpose at scale
- IPO pipeline if market matures

**Bear case:**
- pgvector commoditizes the space (free, integrated)
- Hyperscalers add native vector support
- Market fragments, no clear winner
- LLM context windows expanding, reducing RAG need

## Thesis implications

- Watch for consolidation — too many players for market size
- Pinecone best positioned for IPO, but valuation risk
- [[Postgres]] ecosystem wins if pgvector is "good enough"
- Hyperscaler absorption likely for smaller players

## Related

- [[Databases]] — broader technology context
- [[Postgres]] — pgvector as competitive threat
- [[AI infrastructure financing]] — capital flows
- [[Data gravity]] — vector data creates stickiness
