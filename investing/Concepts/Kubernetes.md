---
aliases: [K8s]
tags: [concept, infrastructure, cloud, containerization]
---

#concept #infrastructure #cloud

**Kubernetes** — open-source container orchestration system originally designed at [[Google]] (internal codename Borg), released in 2014. The dominant framework for running containerized workloads across clusters of servers.

---

## Why it matters for memory/compute theses

Kubernetes made it possible to run multiple applications efficiently on a single server — a clear efficiency gain. At widespread adoption (late 2010s), there were concerns that demand for servers and memory would fall because companies needed fewer hardware resources to produce the same results.

Outcome: the opposite occurred. Lower per-workload cost unlocked new deployments and encouraged much greater total usage. This is a canonical [[Jevons Paradox]] case cited against first-order efficiency-reduces-demand readings — including in the Apr 2026 [[TurboQuant]] debate, where Kim Young-gun ([[Mirae Asset]] Securities) invoked "déjà vu" over Kubernetes when arguing that KV-cache compression should expand rather than contract [[HBM]] demand.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Origin | [[Google]] (internal Borg), open-sourced 2014 |
| Governance | Cloud Native Computing Foundation (CNCF) |
| Dominance | De-facto standard for container orchestration |
| Category | Infrastructure framework |

---

## Related

- [[Jevons Paradox]] — efficiency-increases-consumption precedent cited for AI compute
- [[TurboQuant]] — Apr 2026 memory-compression debate where Kubernetes parallel surfaced
- [[Google]] — origin organization
- [[Mirae Asset]] — Kim Young-gun research note citing the parallel
- [[Google Cloud]] — hyperscaler offering managed Kubernetes (GKE)

*Created 2026-04-12 as stub (dead-link resolution from TurboQuant / Jevons Paradox updates)*
