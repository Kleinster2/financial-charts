---
aliases: [Cloud computing, Cloud, Cloud infrastructure, Public cloud, The cloud]
tags: [concept, technology, cloud, infrastructure]
---

# Cloud computing

Cloud computing is the on-demand delivery of compute, storage, networking, and software services over the internet on a pay-as-you-go basis, replacing owned and operated data centers with rented capacity from large providers. It turned IT infrastructure from a capital expense (buy servers) into an operating expense (rent capacity), and is the demand engine behind the [[Data center infrastructure|data-center buildout]] and the AI-compute capex supercycle.

## Synthesis

Cloud computing is no longer just an IT cost-model shift. It is the infrastructure layer behind AI training and inference, the largest hyperscaler capex program, and now a regulated platform-gatekeeper surface. The same characteristics that make cloud attractive to enterprises - managed services, ecosystem breadth, security integration, and developer defaults - also create switching costs that regulators can read as lock-in.

---

## Service models

| Layer | What the provider runs | Examples |
|-------|------------------------|----------|
| IaaS — [[IaaS\|Infrastructure-as-a-Service]] | Compute, storage, networking (raw virtual machines) | AWS EC2, Azure VMs, Google Compute Engine |
| PaaS — Platform-as-a-Service | Runtime, databases, dev tooling | AWS Lambda, Azure App Service, Google App Engine |
| SaaS — Software-as-a-Service | Finished applications | Salesforce, Microsoft 365, ServiceNow |

The stack rests on [[Virtualization]] — abstracting physical hardware into pooled, allocatable virtual resources is what makes multi-tenant cloud economically possible.

## Deployment models

- Public cloud — shared multi-tenant infrastructure from a hyperscaler.
- Private cloud — dedicated infrastructure (on-prem or hosted) for one organization.
- Hybrid / multi-cloud — a mix, increasingly the enterprise default for resilience, data sovereignty, and avoiding lock-in.

## The hyperscalers

The market is a concentrated oligopoly of global-scale providers:

| Provider | Platform | Parent |
|----------|----------|--------|
| [[AWS]] | Amazon Web Services | [[Amazon]] |
| [[Microsoft Azure]] | Azure | [[Microsoft]] |
| [[Google Cloud]] | GCP | [[Alphabet]] |
| Oracle Cloud | [[OCI]] | [[Oracle]] |
| [[Alibaba Cloud]] | Aliyun | [[Alibaba]] |
| [[Tianyi Cloud]] | China Telecom Cloud | [[China Telecom]] |

![[cloud-computing-chart.png]]
*The investable expression of the theme — the [[SKYY]] cloud-computing ETF normalized against software ([[IGV]]) and the market ([[SPY]]), through 2026-06-18.*

[[Edge cloud|Edge computing]] extends the model by pushing compute closer to where data is generated (low latency, local processing), complementing the centralized hyperscaler data centers rather than replacing them.

## EU DMA cloud gatekeeper push (Jun 2026)

The [[European Commission]]'s Jun 25 2026 preliminary position that [[AWS]] and [[Microsoft Azure]] should be [[Digital Markets Act]] gatekeepers reframes cloud as regulated platform infrastructure, not merely rented compute. The regulatory theory matches the cloud business model: high switching costs, entrenched enterprise estates, broad ecosystems, and AI procurement make the largest clouds gateways between software providers and end customers.

See [[EU cloud DMA preliminary findings 2026]].

## Why it matters

- Disrupted traditional [[IT services|IT outsourcing]] — hyperscaler self-service eroded the legacy facilities-management/managed-hosting model, pushing IT-services firms up the stack toward migration, integration, and AI deployment.
- The AI-compute demand driver — model training and inference run on cloud GPU capacity, making the hyperscalers the largest buyers of [[Nvidia|AI accelerators]] and the primary tenants of the [[Data center infrastructure|data-center buildout]].
- A capex supercycle — hyperscaler capital spending on data centers, power, and silicon is now one of the largest single demand lines in global markets.

## Related

- [[IaaS]] — the infrastructure layer of the cloud stack
- [[Virtualization]] — the foundational technology that makes multi-tenant cloud possible
- [[Edge cloud]] — distributed compute extending the cloud to the edge
- [[IT services]] — the outsourcing model the cloud disrupted and reshaped
- [[Data center infrastructure]] — the physical layer cloud runs on
- [[Digital Markets Act]] — [[EU]] regulatory frame now reaching cloud gatekeepers
- [[Amazon]], [[Microsoft]], [[Alphabet]], [[Oracle]], [[Alibaba]] — the hyperscalers
- [[Enterprise AI adoption]] — a major current demand driver

*Created 2026-06-21 to resolve the [[IT services]]/[[IaaS]]/[[Virtualization]] dead links. Expansion candidate: cloud-market share data, hyperscaler capex figures, growth rates, margin economics.*
