# AI storage bottleneck

#concept #ai #infrastructure #bottleneck

**AI storage bottleneck** — The phenomenon where GPUs sit idle waiting for training data. **70% of AI training time is I/O, not compute.** Only 7% of teams achieve >85% GPU utilization. The core thesis for [[AI Storage]] sector.

---

## The problem

### GPU idle time

| Metric | Value | Source |
|--------|-------|--------|
| Training time spent on I/O | **70%** | [[Microsoft]] |
| [[Teams]] with >85% GPU utilization | **7%** | Industry survey |
| Typical GPU utilization | 15-50% | Various |

**Translation:** $30K+ GPUs spend most of their time waiting for data.

### Why it happens

```
Storage throughput << GPU processing speed

H100 GPU: 3,958 TFLOPS (FP8)
Typical storage: 10-50 GB/s
Required for saturation: 100+ GB/s per GPU
```

The GPU can process data faster than storage can deliver it.

---

## Bottleneck sources

| Source | Problem | Impact |
|--------|---------|--------|
| **Storage I/O** | Traditional systems too slow | Primary bottleneck |
| **Network transfer** | Remote data takes time | Latency spikes |
| **CPU preprocessing** | Augmentation on CPU | CPU maxed, GPU idle |
| **Checkpointing** | Saving model state | Training pauses |

### LLM vs Vision workloads

| Workload | Data requirement |
|----------|------------------|
| LLM training | 10+ GB/s sustained read |
| Computer vision | Even higher (images/video) |
| Multimodal | Combination of both |

---

## The math

**Epoch AI scaling limit:**

> "Training runs past 2e28 FLOP are infeasible because data movement time dominates arithmetic time."

At frontier scale, storage becomes THE limiting factor, not compute.

---

## Solutions

### Hardware

| Solution | How it helps |
|----------|--------------|
| **All-flash storage** | 10-100x faster than HDD |
| **NVMe/NVMe-oF** | Low-latency access |
| **GPUDirect Storage** | Bypass CPU, direct GPU-to-storage |
| **Parallel file systems** | Distributed throughput |

### Software

| Solution | How it helps |
|----------|--------------|
| **Distributed data loading** | Parallel prefetch |
| **Local caching** | NVMe cache for hot data |
| **Async prefetching** | Load next batch while training |
| **Data pipeline optimization** | Eliminate CPU bottlenecks |

### Architecture

| Approach | Benefit |
|----------|---------|
| **Co-located storage** | Minimize network hops |
| **Tiered storage** | Hot data on flash, cold on object |
| **[[Data lakehouse]]** | Unified data layer |

---

## Who benefits

### Storage vendors

| Company | Positioning |
|---------|-------------|
| [[Pure Storage]] | Enterprise incumbent, NVIDIA certified |
| VAST Data | AI-native architecture |
| Weka | GPU-direct optimized |
| DDN | HPC heritage |

### Adjacent beneficiaries

| Category | Examples |
|----------|----------|
| Flash memory | [[SanDisk]], [[Samsung]], [[SK Hynix]], [[Micron]] |
| Networking | Arista, [[Cisco]] (InfiniBand, Ethernet) |
| Data orchestration | Alluxio, Hammerspace |

---

## Investment implications

### The thesis

**If:**
- GPU time is expensive ($2-4/hr for H100)
- 70% of time is wasted on I/O
- Storage solutions can recover even 20-30% utilization

**Then:**
- ROI on storage is enormous
- Premium pricing justified
- First-mover advantage matters (certifications)

### Valuation framework

| Metric | Implication |
|--------|-------------|
| GPU idle cost | Quantifies storage value |
| Certification moats | Defensibility |
| Hyperscaler adoption | Validation |

---

## Risks to thesis

| Risk | Counter |
|------|---------|
| Hyperscalers build in-house | Enterprise still needs vendors |
| Algorithmic efficiency gains | Data needs still growing |
| Commoditization | Certifications create stickiness |

---

## Related

### Sister sector
- [[AI Storage]] — the companies solving this problem

### Parent sector
- [[AI Infrastructure]] — broader context

### Actors
- [[Pure Storage]] — incumbent leader
- VAST Data — AI-native challenger
- Weka — GPU-direct specialist
- [[NVIDIA]] — GPU maker, certification authority

### Adjacent concepts
- [[Power constraints]] — another AI infrastructure bottleneck
- [[Water constraints]] — cooling bottleneck

---

Sources:
- [Hammerspace - Storage Bottleneck](https://hammerspace.com/is-your-current-ai-data-storage-sabotaging-your-ai-training-the-hidden-bottleneck-in-gpu-clusters/)
- [Alluxio - I/O Bottleneck](https://www.alluxio.io/blog/gpus-are-fast-i-o-is-your-bottleneck/)
- [Epoch AI - Data Movement Limits](https://epoch.ai/blog/data-movement-bottlenecks-scaling-past-1e28-flop)

*Created 2026-01-14*
