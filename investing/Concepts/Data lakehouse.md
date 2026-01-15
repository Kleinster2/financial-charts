# Data lakehouse

Architectural pattern combining data lake flexibility with data warehouse performance — the current battleground between Databricks and Snowflake.

## Theory

**Data warehouse (traditional):**
- Structured data, schema-on-write
- Optimized for BI/analytics queries
- Expensive storage, fast queries
- Example: Snowflake, Redshift, BigQuery

**Data lake:**
- Raw data, schema-on-read
- Cheap storage (S3/ADLS/GCS)
- Flexible formats (JSON, Parquet, Avro)
- Slow queries without optimization

**Lakehouse = both:**
- Cheap lake storage + warehouse query performance
- Open formats (Parquet) + metadata layer (Delta, Iceberg)
- ACID transactions on object storage
- Single source of truth for all workloads

## Key technologies

| Technology | Origin | Status |
|------------|--------|--------|
| Delta Lake | [[Databricks]] | De facto standard, donated to Linux Foundation |
| Apache Iceberg | Netflix | Growing adoption, Snowflake's choice |
| Apache Hudi | Uber | Less traction, merging with Iceberg |

## Competitive dynamics

### [[Databricks]]
- Coined "lakehouse," native architecture
- Delta Lake ecosystem advantage
- Stronger on ML/AI workloads
- Private, potential IPO candidate

### [[Snowflake]]
- Warehouse-first, adding lake features
- Iceberg support for open formats
- Stronger on BI/SQL workloads
- Public, premium valuation

### Hyperscalers
- AWS (Athena + Glue), Azure (Synapse), GCP (BigLake)
- Bundling lakehouse features into platforms
- Price pressure on pure-play vendors

## Investment implications

- Lakehouse is consensus architecture — warehouse vs lake debate over
- Databricks vs Snowflake is the key battleground
- Open formats reduce lock-in but slow switching still exists ([[Data gravity]])
- Watch for pricing pressure as hyperscalers commoditize

## Related

- [[Databases]] — broader context
- [[Database companies]] — sector hub
- [[Databricks]] — lakehouse originator
- [[Snowflake]] — primary competitor
- [[Data gravity]] — lakehouse increases data stickiness
