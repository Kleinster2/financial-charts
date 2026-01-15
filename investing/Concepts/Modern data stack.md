# Modern data stack

The ecosystem of cloud-native, modular tools that replaced legacy monolithic data platforms.

## Architecture

```
Sources → Ingestion → Storage → Transform → BI/Analytics
           (ELT)      (Warehouse)  (dbt)     (Looker, etc)
```

## Key layers

### Ingestion (ELT)
- **Fivetran** — managed connectors, leader, acquired by ~$5.6B
- **Airbyte** — open source alternative, growing
- **Stitch** — Talend-owned, smaller player
- Shift from ETL (transform before load) to ELT (transform after load)

### Storage / Warehouse
- [[Snowflake]], [[Databricks]], BigQuery, Redshift
- See [[Database companies]], [[Data lakehouse]]

### Transformation
- **dbt (data build tool)** — SQL-based transformations, huge adoption
- dbt Labs raised $222M, potential IPO candidate
- "Analytics engineering" as a discipline

### BI / Analytics
- **Looker** — acquired by Google
- **Tableau** — acquired by Salesforce
- **Power BI** — Microsoft bundled
- **Metabase, Preset, Hex** — newer entrants

### Orchestration
- **Airflow** — open source standard
- **Dagster** — modern alternative
- **Prefect** — cloud-native orchestration

## Investment implications

| Dynamic | Effect |
|---------|--------|
| Modular = best-of-breed | Each layer has venture-backed competition |
| Consolidation pressure | Too many tools, enterprises want fewer vendors |
| dbt centrality | Transformation layer sticky, dbt well-positioned |
| Hyperscaler bundling | AWS/GCP/Azure adding native tools |

## Thesis angles

- **dbt Labs** — watch for IPO, strong ecosystem moat
- **Fivetran** — private, high valuation, competition from Airbyte
- **Consolidation plays** — Snowflake/Databricks acquiring pieces
- **Open source pressure** — Airbyte, Metabase commoditizing layers

## Buzzwords to watch

- **Data mesh** — organizational pattern, decentralized data ownership
- **Data fabric** — automated data integration layer
- **Data contracts** — schema agreements between producers/consumers
- **Semantic layer** — metrics definitions above the warehouse

## Related

- [[Database companies]] — warehouse layer
- [[Data lakehouse]] — storage architecture
- [[Streaming data]] — real-time ingestion alternative
- [[Data gravity]] — stack accumulates switching costs
