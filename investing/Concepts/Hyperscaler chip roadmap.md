#concept #reference #hyperscaler #asic

Custom AI chip programs across hyperscalers. Updated Dec 2025.

---

## Google

| Chip | Node | HBM | IC Design | Launch |
|------|------|-----|-----------|--------|
| TPU v6e (Trillium) | 4nm | HBM3e | Broadcom | 2024 |
| **TPU v7 (Ironwood)** | 3nm | **192GB HBM3E** | Broadcom | **Nov 2025 ✓** |
| TPU v7e (A5921) | 3nm | HBM3e | **MediaTek** | 2026 |
| TPU v8p | 2nm | TBC | Broadcom | 2028 |
| TPU v8e | 2nm | TBC | **MediaTek*** | 2028 |

**TPU v7 Ironwood** (Nov 2025): Inference-focused. 4,614 FP8 TFLOPS, 192GB HBM3E (6x Trillium), 9.6 Tb/s ICI, 9,216-chip superpod = 42.5 Exaflops. [[Anthropic]] committed to 1M+ chips starting 2026.

MediaTek appearing = Broadcom disintermediation progressing.

---

## Meta

| Chip | Node | HBM | IC Design | Launch |
|------|------|-----|-----------|--------|
| MTIA 1 (Athena) | 5nm | — | Broadcom/Andes | 2024 |
| MTIA 1.5 (Iris) | 3nm | HBM3e | Broadcom/Andes | 2026 |
| **MTIA Training** | 3nm | HBM3e | **In-house (RISC-V)** | **2026** |
| MTIA 2 | 2nm | HBM4 | Broadcom/Andes* | 2027 |

**Update (Mar 2025)**: Meta testing first in-house **training** chip (RISC-V based). Acquired Rivos for ~$2B to accelerate custom silicon. Currently running 350K H100s, $65B AI infra budget for 2025.

---

## Amazon

| Chip | Node | HBM | IC Design | Launch |
|------|------|-----|-----------|--------|
| Inferentia v2.5 | 5nm | HBM3 | Marvell | 2024 |
| Trainium v2 (Cayman) | 5nm | HBM3 | Marvell | 2024 |
| Trainium v2 Ultra | 5nm | HBM3e | Marvell | 2025 |
| **Trainium3** | **3nm** | **144GB HBM3e** | Marvell/Alchip | **Dec 2025 ✓** |
| Trainium4 (Maverick) | 2nm | HBM3e | Alchip/Marvell/Broadcom* | 2028 |

**Trainium3** (Dec 2, 2025): AWS's first 3nm chip. 2.52 PFLOPS FP8, 144GB HBM3e, 4.9 TB/s bandwidth. 4.4x more compute vs Trn2. Trn3 UltraServers = 144 chips/system. "Multibillion-dollar business" per AWS CEO.

**Trainium4 roadmap**: 6x FP4, 3x FP8, 4x memory bandwidth. Will support NVIDIA NVLink Fusion — first hyperscaler custom chip with NVLink compatibility.

**Inferentia discontinued**: AWS stopped making inference-only chips. Inference converging with training; Trainium handles both.

**Graviton5** (Dec 2025): Most powerful AWS CPU, announced at re:Invent.

---

## Microsoft

| Chip | Node | HBM | IC Design | Launch |
|------|------|-----|-----------|--------|
| Maia 100 (Athena) | 5nm | HBM3 | GUC | 2024 |
| Maia 200 (Braga) | 3nm | HBM4 | GUC | **2026 (delayed)** |
| Maia 280 | 3nm | HBM4 | GUC | 2027 (new) |
| Maia 300 (Griffin) | 3nm | HBM3e | Marvell | 2027 |
| Maia 2 | **Intel 18A** | TBC | GUC | TBC |

**Maia 200 delayed**: Design changes from OpenAI requests caused instability. Staff turnover (20% on some teams). Scaled back ambitions through 2028.

**Intel Foundry angle**: Maia 2 reportedly going to Intel 18A — first major external win, US-based supply chain.

---

## Others

| Company | Chip | Node | IC Design | Foundry | Launch |
|---------|------|------|-----------|---------|--------|
| **OpenAI** | Titan v.1 | 3nm | Broadcom | TSMC | **H2 2026** |
| OpenAI | Titan v.2 | 2nm | Broadcom | TSMC | 2028 |
| **xAI** | X1 | 3nm | Broadcom/GUC* | **Samsung Taylor** | **2026-27** |
| Apple | Belta | 3nm | Broadcom | TSMC | 2027 |
| Softbank | Gen1 | 3nm | Broadcom | TSMC | 2027 |
| Softbank | Gen2 | 2nm | Broadcom | TSMC | 2028 |
| Bytedance | Gen1/2 | 5nm/3nm | Broadcom | TSMC | 2026-27 |
| Bytedance | APU | 3nm | **MediaTek** | TSMC | TBD |

**OpenAI-Broadcom** (Oct 2025): 10GW capacity commitment, ~$10B deal. Custom systolic array accelerators on Broadcom Ethernet stack. "Control your destiny" — Hock Tan.

**xAI-Samsung** (Dec 2025): Taylor fab deal finalized. Production early 2026, full scale 2027. Near Tesla Austin HQ. Validates [[Short TSMC long Korea]].

---

## Key takeaways

**Foundry diversification emerging**:
- TSMC still dominant (Google, Amazon, OpenAI, Apple)
- Samsung gaining: xAI Taylor, potentially AMD
- Intel 18A: Microsoft Maia 2 (if confirmed = major validation)

**Memory**: HBM3e standard (144-192GB), HBM4 coming 2026-27. Validates [[Long memory]].

**IC Design shift**:
- Broadcom still dominant (OpenAI $10B deal)
- MediaTek appearing: Google TPUv7e, Bytedance APU
- Marvell strong with Amazon
- Meta going in-house with RISC-V

**Speed of iteration**: Google and Amazon shipping new generations within months of announcement. Microsoft struggling with delays.

---

*Updated 2025-12-30*

Sources: [Google Ironwood](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads), [AWS Trainium3](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/), [OpenAI-Broadcom](https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/), [Samsung-xAI](https://dataconomy.com/2025/12/19/samsung-xai-ai-chip-deal/)

## Related

- [[Google]] — customer (TPU v7 Ironwood, Broadcom/MediaTek)
- [[Amazon]] — customer (Trainium3, Marvell/Alchip)
- [[Microsoft]] — customer (Maia 200 delayed, GUC)
- [[Meta]] — customer (MTIA, going in-house with RISC-V)
- [[OpenAI]] — customer (Titan v.1, Broadcom)
- [[xAI]] — customer (X1, Samsung Taylor)
- [[TSMC]] — foundry (dominant for most)
- [[Samsung]] — foundry (xAI, potentially AMD)
- [[Intel Foundry Services]] — foundry (Microsoft Maia 2 on 18A)
- [[Broadcom]] — IC design (dominant, OpenAI $10B)
- [[MediaTek]] — IC design (emerging, Google TPU v7e)
- [[Marvell]] — IC design (Amazon relationship)
