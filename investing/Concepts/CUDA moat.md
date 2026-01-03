#concept #moat #nvidia #software

**CUDA** is [[NVIDIA]]'s software platform for GPU computing. It's the primary moat — hardware can be matched, software ecosystems cannot be rebuilt quickly.

---

## What CUDA is

- Programming model for GPU-accelerated computing
- Libraries: cuDNN (deep learning), cuBLAS (linear algebra), TensorRT (inference)
- 10+ years of optimization, documentation, community knowledge
- De facto standard for AI/ML development

---

## Why it's a moat

| Hardware moat | Software moat |
|---------------|---------------|
| Can be matched in 2-3 years | Takes 5-10 years to replicate |
| Specs are visible | Ecosystem is invisible |
| Customers compare benchmarks | Developers compare productivity |

AI researchers don't choose GPUs — they choose CUDA. The hardware follows.

---

## Analogy to foundry lock-in

| TSMC | NVIDIA |
|------|--------|
| [[Process design kit]] | CUDA + libraries |
| Years of design optimization | Years of code optimization |
| Engineers learn the quirks | Developers learn the APIs |
| Switching = re-verify everything | Switching = re-write everything |

Same dynamic: accumulated knowledge creates switching costs.

---

## Challengers

| Alternative | Owner | Status |
|-------------|-------|--------|
| ROCm | [[AMD]] | Improving post-NodAI, still behind |
| Triton | OpenAI | Compiler, not full stack |
| JAX/XLA | Google | TPU-focused |
| oneAPI | Intel | Minimal traction |

---

## Is the moat cracking?

**Signs of erosion:**
- [[AMD]] NodAI acquisition driving software-hardware co-design
- PyTorch improving non-CUDA support
- Hyperscalers want alternatives (cost, supply)
- Open source pressure on CUDA lock-in

**Signs of durability:**
- Inertia — existing codebases are CUDA
- Performance gap still exists for many workloads
- NVIDIA keeps investing in software
- **NVIDIA expanding moat to infrastructure layer** (see below)

---

## Moat expansion: infrastructure layer

NVIDIA is extending lock-in beyond CUDA into infrastructure:

**SchedMD / SLURM acquisition (Dec 2025)**:
- SLURM = widely used open source workload scheduler
- Used by: Mistral, Meta FAIR, universities, neoclouds
- Critical: AMD/Intel users also depend on SLURM
- NVIDIA commits to keep it "open source, vendor-neutral" — skepticism warranted
- Slinky project (SLURM on Kubernetes) future uncertain — neoclouds depend on it

**Other infrastructure plays:**
- DGX Cloud
- Run:AI (acquired)
- Networking (Mellanox)

Pattern: NVIDIA buying infrastructure that competitors also rely on. Each layer adds switching costs.

---

## Current view

CUDA moat is real but not permanent. AMD has moved from "0% chance" to "non-zero chance" of challenging it. Timeline: 2-4 years to know if AMD software reaches parity.

SLURM acquisition is a defensive move — NVIDIA locking down another layer before AMD/Intel can build momentum.

---

## Related

- [[NVIDIA]] — owner (CUDA software ecosystem)
- [[AMD]] — challenger (ROCm, NodAI acquisition)
- [[Customer lock-in via co-design]] — mechanism (same dynamic as foundry PDKs)
- [[Process design kit]] — analogy (switching costs from accumulated knowledge)
