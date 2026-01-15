# Postgres

Open source relational database that has become the de facto standard for new application development.

## Relational theory

**Relational model** — data organized in tables (relations) with rows and columns, connected via keys. Invented by Edgar Codd (1970) at IBM.

**Normalization** — design process to reduce redundancy:
- **1NF** — atomic values, no repeating groups
- **2NF** — no partial dependencies on composite keys
- **3NF** — no transitive dependencies

*Investment implication:* Relational model's rigidity is a feature for transactional systems — predictable performance, data integrity. Document DBs (MongoDB) trade this for flexibility, but Postgres JSONB often delivers both.

**SQL** — declarative query language, standardized (ANSI). Postgres's strict compliance makes migration easier vs MySQL's quirks or Oracle's extensions.

## Why Postgres won

- **Extensions** — PostGIS, pgvector, TimescaleDB extend into specialized domains
- **SQL standard compliance** — easier migration, broader tooling
- **Community** — decades of stability, no single corporate owner
- **Cloud-native fit** — managed offerings from every hyperscaler

## Competitive pressure

| Target | Impact |
|--------|--------|
| [[Oracle]] | Enterprises migrating off expensive licenses |
| [[MongoDB]] | JSONB handles document workloads in Postgres |
| Proprietary analytics | Extensions + columnar storage narrowing gap |

## Postgres-native companies

Private companies building Postgres infrastructure:

- **Supabase** — Postgres-as-a-platform, Firebase alternative
- **Neon** — serverless Postgres, branching for dev workflows
- **Timescale** — time-series extension, managed cloud
- **Crunchy Data** — enterprise Postgres, Kubernetes operator
- **EDB (EnterpriseDB)** — Oracle migration tooling, enterprise support

## Investment implications

- Postgres commoditizes databases — moats shift to tooling, scale, DX
- Oracle's on-prem decline accelerates as migration friction drops
- Postgres-native startups competing for "modern data stack" budgets
- Hyperscalers (Aurora Postgres, Cloud SQL, Azure) capture most volume

## Thesis angles

- **Short Oracle** — Postgres migration + cloud transition pressure
- **Watch Postgres IPOs** — Supabase, Neon if they go public
- **Long hyperscalers** — benefit from Postgres adoption without building it

## Related

- [[Databases]] — broader technology context
- [[Database companies]] — sector hub
- [[Vector databases]] — pgvector extends Postgres into AI
- [[Modern data stack]] — Postgres-native companies in ecosystem
- [[Data gravity]] — Postgres data accumulates switching costs
- [[Oracle]] — primary disruption target
