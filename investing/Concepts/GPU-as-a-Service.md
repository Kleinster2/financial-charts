---
aliases: [GPUaaS, GPU as a Service]
---
#concept #ai #compute #infrastructure

GPU-as-a-Service (GPUaaS) — a business model in which an operator owns or leases [[NVIDIA|NVIDIA]]-class high-performance GPUs and rents compute capacity to third parties, typically under long-term contracts. The model spans hyperscalers ([[AWS]], [[Microsoft|Azure]], [[Google|GCP]]), neoclouds ([[CoreWeave]], [[Nebius]], [[Lambda Labs]]), crypto-to-AI converts ([[IREN]], [[Hut 8]], [[Core Scientific]]), and — as of Apr 2026 — shell-company pivots ([[NewBird AI]], née [[Allbirds]]).

---

## The stack

| Layer | Examples | Economics |
|-------|----------|-----------|
| Chips | [[NVIDIA]] H100/H200/B200, [[AMD]] MI300, Google TPU | Capex-heavy, cycle-sensitive ([[GPU depreciation cycle]]) |
| Power + land | Reusable across mining/AI ([[Crypto-to-AI pivot]]) | Multi-year PPAs, scarcity pricing |
| Deployment | [[FluidStack]], integrators | Cabling, burn-in, testing |
| Cloud layer | [[CoreWeave]], [[Nebius]], [[Lambda Labs]] | Contracted revenue, $1–4M/MW/year |
| Customers | Hyperscalers, AI labs ([[Anthropic]], [[OpenAI]]), enterprises | Long-term lease under [[Neocloud financing]] |

## Why it's a distinct business model

- Recurring revenue vs. one-shot GPU sale
- Contract duration reduces hyperscaler capex volatility
- Amortized across customers, unlike dedicated on-premise
- Exposed to [[GPU Financing Risk]] and [[GPU rental price index]] movements

## Three entry paths

1. Greenfield neocloud — raise capital, buy GPUs, sign hyperscaler contracts ([[CoreWeave]] model)
2. Infrastructure pivot — already own power/land/cooling, buy GPUs ([[Crypto-to-AI pivot]])
3. Shell pivot — acquire a public listing, raise on it, buy GPUs ([[NewBird AI]]; see [[Shell company AI pivot]])

## Related

- [[Crypto-to-AI pivot]] — infrastructure-reuse entry path
- [[Shell company AI pivot]] — listing-reuse entry path
- [[Neocloud financing]] — financing structures
- [[GPU Financing Risk]] — balance-sheet risk
- [[GPU rental price index]] — pricing benchmark
- [[GPU depreciation cycle]] — accounting/capex timing
- [[AI compute demand curve]] — demand backdrop
- [[CoreWeave]], [[Nebius]], [[Lambda Labs]] — public neocloud comparables
- [[NewBird AI]] — Apr 2026 shell-pivot entrant
