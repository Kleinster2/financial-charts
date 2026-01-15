# Data gravity

The phenomenon where data accumulates mass — attracting applications, services, and more data — creating powerful switching costs.

## Theory

Coined by Dave McCrory (2010). Core insight: moving compute to data is easier than moving data to compute.

**Why data has "mass":**
- Storage is cheap, but egress is expensive
- Data grows faster than bandwidth
- Compliance/residency requirements anchor data geographically
- Integrations and dependencies multiply over time

## Investment implications

| Dynamic | Effect |
|---------|--------|
| Switching costs | Customers rarely migrate once data accumulates |
| Land-and-expand | Small initial workloads become sticky over time |
| Pricing power | Vendors can raise prices on captive data |
| Moat depth | Data gravity compounds — older customers are stickier |

## Where it matters

- **Cloud providers** — AWS/Azure/GCP benefit most; once data lands, workloads follow
- **[[Snowflake]]** — consumption model + data sharing creates gravity
- **[[Databricks]]** — lakehouse accumulates raw data, harder to leave
- **[[MongoDB]]** — Atlas stickiness from operational data gravity

## Counterforces

- **Multi-cloud strategies** — enterprises actively fighting lock-in
- **Open formats** — Parquet, Iceberg reduce switching friction
- **Data portability regulations** — EU pushing for easier migration

## Related

### Sister sector
- [[Database companies]] — this concept explains WHY database vendors have stickiness

### Technology
- [[Databases]] — gravity affects all database vendor dynamics
- [[Data lakehouse]] — architectural pattern that increases gravity
