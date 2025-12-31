#actor #fabless #ai #gpu

**NVIDIA** — dominant AI accelerator company with hardware + software moat.

## Core thesis

NVIDIA's moat isn't just GPUs — it's [[CUDA moat|CUDA]], the software ecosystem that locks in AI developers. Hardware can be challenged; rebuilding a decade of software tooling cannot.

---

## Key strengths

- **CUDA ecosystem**: 10+ years of libraries, tools, developer knowledge
- **AI training dominance**: >90% market share in data center AI
- **Vertical integration**: Hardware + software + networking (Mellanox)
- **Customer lock-in**: Switching costs are software, not silicon
- **Infrastructure expansion**: Acquiring layers competitors depend on (see below)

---

## Manufacturing relationships

| Foundry | Relationship |
|---------|--------------|
| [[TSMC]] | Primary — locks capacity at leading edge |
| [[Samsung]] | Secondary — some legacy nodes |

NVIDIA + Apple locking [[TSMC]] 2nm capacity forces [[AMD]] and others to alternatives.

---

## Competitive position

| Competitor | Threat level | Notes |
|------------|--------------|-------|
| [[AMD]] | Rising | NodAI acquisition, software improving |
| Intel | Low | Far behind on AI accelerators |
| Custom silicon (Google TPU, Amazon) | Medium | Hyperscalers building own chips |

---

## Moat expansion strategy

NVIDIA actively acquires infrastructure that competitors also depend on:

| Acquisition | What | Why it matters |
|-------------|------|----------------|
| **Groq ($20B, Dec 2025)** | LPU inference chips | Largest deal ever. 10x faster, 1/10th energy for inference. Entering non-GPU market. |
| SchedMD (Dec 2025) | SLURM workload scheduler | AMD/Intel users rely on it |
| Run:AI | Kubernetes orchestration | AI cluster management |
| Mellanox | Networking | AI cluster connectivity |

Pattern: buying "neutral" infrastructure + potential competitors, raising switching costs beyond CUDA.

---

## China market dynamics

See [[Export controls]] for full context.

**Before controls:** 95% China AI chip share
**After controls:** ~0% (tight restrictions)
**H200 approved (Dec 2025):** 25% cut to US govt on sales, shipping before Lunar New Year. Could recover 10-25% share.

**US strategic calculus:**
- H200 is "previous gen" — B200 (Blackwell) is 3.1x faster
- Rubin (2026) widens gap further
- Release old tech while monopolizing cutting edge
- Build ecosystem defense against Chinese chip makers

**Chinese competition:**
- Huawei 910C: 76% of H200 compute, 2/3 memory bandwidth
- Cambricon, Hygon even further behind
- Even "outdated" H200 beats all Chinese alternatives

**Dual ecosystem forming:**
- Training: NVIDIA (high barriers)
- Inference: Chinese chips (cost sensitive, volume)

---

## Key vulnerabilities

- CUDA moat eroding if alternatives mature (ROCm, Triton, JAX)
- Customer concentration in hyperscalers who want alternatives
- Valuation assumes continued dominance
- Supply constrained by [[TSMC]] and [[Advanced packaging|CoWoS]]
- China revenue capped by export controls (but H200 provides partial recovery)

---

## Quick stats

| Metric | Value |
|--------|-------|
| AI training share | >90% |
| Primary foundry | [[TSMC]] |
| Packaging | [[TSMC]] CoWoS (constrained) |
| **2026 backlog** | **$275B** |
| **Stock YTD** | **+37%** (underperforming memory) |

*Updated 2025-12-30*

---

## Recent developments (Dec 2025)

**CES 2026 preview (Jan 6):**
- Blackwell Ultra ramp update
- Rubin architecture roadmap (next-gen after Blackwell)
- Jensen Huang keynote

**Major orders:**
- **ByteDance $14B** NVIDIA order for 2026 (H200s, HBM3E 8Hi)
- Continued hyperscaler demand

**Foundry diversification:**
- Exploring [[Samsung]] as second foundry (post-Groq deal)
- Would reduce TSMC dependency

**RTX PRO 5000:**
- Blackwell workstation GPU: 72GB GDDR7, 2,142 TOPS

---

## Market expectations

**Priced in:**
- Continued AI training dominance
- CUDA moat holds
- [[TSMC]] supply secured

**Not priced in (potential surprises):**
- AMD software reaches parity (CUDA moat cracks)
- Hyperscaler defection to custom silicon
- [[TSMC]] packaging constraints limit shipments

**Market positioning (Dec 2025):**
- Michael Burry: put positions disclosed Nov 2025
- Insider selling: $496M in 90 days, zero buying
- Sentiment indicator — insiders cashing out at highs
- **Stock +37% YTD vs Micron +229%, SK Hynix +220%** — memory outperforming GPU

---

## For theses

- [[Long TSMC]] — NVIDIA locks TSMC capacity, reinforces moat
- [[Long memory]] — every GPU needs HBM from SK Hynix/Samsung
- [[Long OSAT and test equipment]] — GPU testing drives ASE/Cohu demand

---

Related: [[Foundry Wars]], [[AI Race]], [[CUDA moat]], [[AMD]], [[TSMC]], [[Advanced packaging]], [[SK Hynix]]
