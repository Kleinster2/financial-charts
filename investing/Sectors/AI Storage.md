# AI Storage

#sector #ai #storage #infrastructure

**AI Storage** — Enterprise storage systems optimized for AI training and inference workloads. **$30-36B market (2025), 24% CAGR.** Critical bottleneck — GPUs idle 70% of time waiting for data. Sub-sector of [[AI Infrastructure]].

---

## Market size

| Metric | Value |
|--------|-------|
| 2025 market | $30-36B |
| 2030 projected | $75-120B |
| CAGR | 24% |
| Top 5 share | 55-60% |

---

## Competitive landscape

### Incumbents (enterprise)

| Company | Ticker | Market cap | AI positioning |
|---------|--------|------------|----------------|
| **[[Pure Storage]]** | PSTG | $24B | NVIDIA Elite partner, DGX certified |
| **NetApp** | NTAP | $25B | Hybrid cloud, ONTAP AI |
| **Dell EMC** | DELL | $95B | PowerScale, broad portfolio |
| **Hitachi Vantara** | Private | — | Enterprise, hybrid |
| **HPE** | HPE | $25B | Cray heritage, HPC |

### AI-native challengers

| Company | Status | Valuation | Differentiation |
|---------|--------|-----------|-----------------|
| **VAST Data** | Private | $9B → $25-30B | Software-only, exabyte-scale |
| **Weka** | Private | $1.6B | WekaFS, GPU-direct |
| **DDN** | Private | — | HPC heritage, Lustre |
| **Hammerspace** | Private | — | Global data orchestration |

---

## Key players deep dive

### VAST Data

| Metric | Value |
|--------|-------|
| Founded | 2016 |
| HQ | New York |
| Valuation | $9B (Series E) → targeting $25-30B |
| Total raised | ~$400M |
| ARR | $200M (Jan 2025) → $600M-1B projected |
| Key deal | $1.17B CoreWeave contract (Nov 2025) |
| Investors | NVIDIA, Tiger Global, Goldman, Fidelity |

**Positioning:** Software-only, single-namespace at exabyte scale. "Fastest-selling data infrastructure startup in history."

### Weka

| Metric | Value |
|--------|-------|
| Founded | 2013 |
| HQ | Campbell, CA |
| Valuation | $1.6B (Series E, May 2024) |
| Total raised | $415M |
| ARR | $100M+ (2024) |
| Investors | NVIDIA, Qualcomm, Generation IM |

**Positioning:** WekaFS parallel file system, GPU-direct optimized. Restructured early 2025 to focus on enterprise AI.

### [[Pure Storage]]

| Metric | Value |
|--------|-------|
| Ticker | PSTG |
| Market cap | $24B |
| Revenue | $3.5B |
| Key product | FlashBlade//S (AI optimized) |
| Moat | NVIDIA Elite partner, 5,000+ FlashStack customers |

**Positioning:** Enterprise incumbent with deepest NVIDIA certifications. Subscription model (Evergreen).

---

## Certification hierarchy

NVIDIA certifications matter — enterprise buyers want validated stacks:

| Certification | What it means | Who has it |
|---------------|---------------|------------|
| DGX SuperPOD | Certified for B300 clusters | Pure, VAST, DDN |
| HGX HPS | Certified for B200/H200 | Pure, NetApp |
| GPUDirect Storage | Direct GPU-to-storage I/O | Pure, VAST, Weka, DDN |
| NVIDIA-Certified Storage | Enterprise AI factory ready | Pure (Foundation + Enterprise) |

---

## Why storage is the bottleneck

See sister concept: [[AI storage bottleneck]]

**The problem:**
- GPUs process data faster than storage can deliver
- 70% of training time = waiting for I/O (Microsoft data)
- Only 7% of teams achieve >85% GPU utilization

**The solution:** High-throughput flash storage with GPU-direct capabilities.

---

## Competitive dynamics

| Dimension | Incumbents (Pure, NetApp) | Challengers (VAST, Weka) |
|-----------|---------------------------|--------------------------|
| Enterprise trust | ✓ Proven | Building |
| NVIDIA certs | ✓ Deep | Catching up |
| Pricing | Premium | Aggressive |
| Architecture | Evolved legacy | AI-native |
| Channel | ✓ Established | Direct-heavy |

**Key question:** Do AI-native architectures (VAST, Weka) displace incumbents, or do incumbents' certifications and channels win?

---

## Investment relevance

**Bull case:**
- 24% CAGR market growth
- Storage is genuine bottleneck (GPU idle time)
- NVIDIA ecosystem creates certification moats
- Hyperscaler capex = sustained demand

**Bear case:**
- Commoditization pressure
- Hyperscalers may build in-house
- Multiple well-funded competitors
- VAST at $25-30B may be priced for perfection

---

## Related

### Parent sector
- [[AI Infrastructure]] — umbrella sector

### Sister concept
- [[AI storage bottleneck]] — why this sector matters

### Actors (public)
- [[Pure Storage]] — PSTG, $24B
- NetApp — NTAP, $25B
- Dell — DELL, $95B

### Actors (private)
- VAST Data — $9B → $25-30B
- Weka — $1.6B
- DDN — private

### Adjacent
- [[NVIDIA]] — certification authority, investor in VAST/Weka
- CoreWeave — major VAST customer ($1.17B deal)

---

Sources:
- [MarketsandMarkets - AI Storage](https://www.marketsandmarkets.com/Market-Reports/ai-powered-storage-market-29450656.html)
- [TechCrunch - VAST Data $25B](https://techcrunch.com/2025/06/10/ai-storage-platform-vast-data-aimed-for-25b-valuation-in-new-round-sources-say/)
- [Weka Series E](https://www.weka.io/company/weka-newsroom/press-releases/weka-nets-140m-in-series-e-funding-at-1-6b-valuation/)

*Created 2026-01-14*
