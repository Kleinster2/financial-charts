---
aliases: [AMZN]
---
#actor #hyperscaler #usa

# Amazon (AWS)

Tier 1 AI hyperscaler, largest cloud provider, major custom silicon player (Trainium, Graviton). [[Anthropic]]'s primary cloud partner.

---

## Why it matters

Amazon is central to multiple vault theses:
- **Anthropic investor**: $8B total, primary cloud/training partner
- **Custom silicon**: Trainium competing with NVIDIA for training
- **Infrastructure scale**: $200B AWS backlog, multi-GW buildouts
- **Foundry customer**: [[TSMC]] 3nm for Trainium3

---

## Custom chip portfolio

### Trainium (AI training/inference)
| Generation | Node | Status | Key specs |
|------------|------|--------|-----------|
| Trainium1 | 7nm | Legacy | First gen |
| Trainium2 | 5nm | Shipping (Dec 2024) | NeuronCore-v3 |
| **Trainium3** | **3nm** | **Shipping (Dec 2025)** | 2.52 PFLOPs FP8, 144GB HBM3e, 4.9 TB/s |
| Trainium4 | TBD | Development | NVLink Fusion support |

**Trainium3 UltraServer**: 144 chips per server, scales to 1M chips (10x previous gen), 40% more energy efficient.

**Trainium4**: First hyperscaler custom chip with **NVIDIA NVLink Fusion** compatibility — can interoperate with NVIDIA GPUs.

### Inferentia (inference — discontinued)
- Inferentia2 was last generation
- Stopped development — inference converging with training workloads
- Trainium now handles both

### Graviton (general compute)
| Generation | Status |
|------------|--------|
| Graviton4 | Shipping |
| **Graviton5** | **Announced Dec 2025** — most powerful AWS CPU |

---

## Anthropic partnership

| Metric | Value |
|--------|-------|
| Total investment | $8B (minority stake) |
| Q3 2025 unrealized gain | $9.5B (mark-to-market at $183B valuation) |
| Infrastructure | Project Rainier ($11B Indiana DC) |
| Chip commitment | 1M Trainium chips for Anthropic |
| Relationship | "Primary cloud and training partner" |

Anthropic using Trainium2/3 to train and deploy Claude models. Strategic alignment: Amazon needs AI differentiation, Anthropic needs compute scale.

---

## Infrastructure investments

| Project | Amount | Capacity | Timeline |
|---------|--------|----------|----------|
| Project Rainier (Indiana) | $11B | — | Opened Oct 2025 |
| Northern Indiana expansion | $15B | 2.4 GW | Announced Dec 2025 |
| Government AI/supercomputing | $50B | 1.3 GW | Breaking ground 2026 |
| **AWS backlog** | **$200B** | — | — |

**Total new capacity**: 3.7 GW committed

### AWS AI Factories (Dec 2025)
- On-premises AI infrastructure for enterprises/government
- NVIDIA + Trainium + AWS networking
- Operates like private AWS Region
- Targets compliance/sovereignty requirements

---

## Partnerships

| Partner | Relationship |
|---------|--------------|
| [[Anthropic]] | $8B investor, cloud partner, 1M chips |
| [[NVIDIA]] | 15-year collaboration, NVLink Fusion coming |
| [[Marvell]] | Trainium/Inferentia design partner |
| OpenAI | Potential $10B investment (reported) |

---

## Thesis implications

| Thesis | Impact |
|--------|--------|
| [[Long Anthropic]] | Amazon's $9.5B gain validates valuation |
| [[Long TSMC]] | Trainium3 = 3nm TSMC demand |
| [[Power constraints]] | +3.7 GW capacity additions |
| [[Hyperscaler chip roadmap]] | Trainium3/4 major custom silicon milestone |

---

## What to watch

- [ ] Trainium3 customer adoption beyond Anthropic
- [ ] Trainium4 NVLink Fusion benchmarks (expected 2026)
- [ ] Anthropic IPO timing and Amazon's stake value
- [ ] AWS AI Factories enterprise traction
- [ ] Project Rainier utilization rates

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | AMZN (NASDAQ) |
| Market cap | ~$2.4T |
| Revenue (TTM) | ~$620B |
| AWS revenue | ~$110B/year |
| AI capex | $75B+ (2025) |
| P/E | ~45x |

*Updated 2026-01-05*

## Related

- [[Anthropic]] — $8B investor, primary cloud partner
- [[NVIDIA]] — chip supplier, NVLink Fusion partner
- [[Marvell]] — Trainium design partner
- [[TSMC]] — foundry for Trainium3 (3nm)
- [[Google]] — hyperscaler competitor
- [[Microsoft]] — hyperscaler competitor
- [[Meta]] — hyperscaler competitor
- [[AI hyperscalers]] — peer category
- [[Hyperscaler chip roadmap]] — custom silicon context
- [[Nuclear power for AI]] — power strategy
