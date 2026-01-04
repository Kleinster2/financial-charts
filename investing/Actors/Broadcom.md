---
aliases: [AVGO]
---
#actor #fabless #enabler #interconnect

# Broadcom (AVGO)

Fabless chip designer that enables hyperscaler custom AI silicon. Also major networking and optical player.

---

## Role in AI supply chain

Broadcom sits between hyperscalers and foundries:

```
Hyperscaler (spec) → Broadcom (design) → TSMC (fab) → Hyperscaler (consume)
```

They're not a hyperscaler — they're an **enabler** that provides:
- Custom AI chip design (ASICs)
- Networking silicon for AI clusters
- Switching and routing chips

---

## Key customers

| Customer | Product | Scale |
|----------|---------|-------|
| Google | TPU design | Massive (internal + cloud) |
| **Anthropic** | TPUv7 | **~1M units direct** |
| Meta | Custom AI silicon | Large |
| OpenAI | Titan chips | $10B deal |
| Others | Various ASICs | Varies |

**Anthropic deal (Jan 2026, per SemiAnalysis):**
- ~1,000,000 TPUv7 units purchased directly from Broadcom
- Deployed in Anthropic-controlled facilities (not Google Cloud)
- DC infrastructure from [[TeraWulf]], [[Hut 8]], [[Cipher Mining]]
- [[FluidStack]] handles deployment operations
- Largest single TPU deployment ever

---

## Key risk: Hyperscaler disintermediation

See [[Hyperscaler chip roadmap]] for full details.

**MediaTek appearing in designs:**
- Google TPUv7e, TPUv8e
- Microsoft Maia 400
- Bytedance APU

This isn't just Google — it's spreading.

---

## Google disintermediation (original risk)

Google TPUv8 has two paths:
- **Sunfish (TPUv8ax)**: Broadcom turnkey — full bundle, higher ASP
- **Zebrafish (TPUv8x)**: Google sources wafers/memory directly, MediaTek for supporting chips

**The economics:**
- Broadcom charges ~55% margins on TPUs
- This costs Google ~$15B/year — a "tax"
- [[NVIDIA]] Blackwell in 2026 will restore GPU cost leadership
- Google must cut ASIC costs to compete with Blackwell unit economics
- Zebrafish isn't just diversification — it's survival

If volume shifts to Zebrafish, Broadcom loses ASP and margin. This is existential pressure, not just negotiation tactics.

---

## Optical/Interconnect business

**Silicon photonics:**
- Acquiring silicon photonics technology
- Alternative to traditional optical (InP)
- Data center interconnects
- Competing with [[Coherent]], [[Lumentum]]

**Networking silicon:**
- Tomahawk switch chips (Ethernet)
- Jericho routing chips
- High-speed SerDes
- Powers [[Arista Networks]] switches

**AI cluster connectivity:**
- Ethernet fabric silicon
- Competing with InfiniBand (NVIDIA)
- NVLink alternatives
- Scale-out networking

Broadcom is both ASIC designer AND networking/optical player.

---

## Why it matters for this vault

- Every custom AI chip they design goes to [[TSMC]]
- Alternative to [[NVIDIA]] GPU path for hyperscalers
- Custom silicon trend = more foundry demand
- But doesn't change TSMC concentration — Broadcom is fabless and uses TSMC

---

## Chip sourcing

- **Foundry**: [[TSMC]] (95% of external wafers)
- **Samsung exposure**: Low — not exploring alternatives
- **F26 purchase commitments**: Only $106M — unusual flexibility while others fight for capacity

---

## Revenue mix shift

| Period | Non-AI % of semi | Non-AI revenue |
|--------|------------------|----------------|
| 1QFY22 | ~90% | ~$5.5B |
| Peak (1QFY23) | ~85% | ~$6.3B |
| 4QFY25 | ~40% | ~$4.6B |
| 1QFY26E | ~35% | ~$4.1B |

- Non-AI down 30% from peak, first y/y growth in 9 quarters
- Wireless = lowest margin in non-AI
- Rest of non-AI (networking, storage) = higher margin than XPU
- No sharp recovery expected in F26
- **Implication**: AI dependency deepening, legacy business structurally smaller

---

## Customer concentration (FY25)

| Metric | Value |
|--------|-------|
| Top 5 customers | 40% of revenue |
| Largest distributor | 32% of revenue |
| Apple | $7B+ |
| China | 17% ($7.6B) |
| Distributor channel | 48% of revenue |

High concentration = risk if Google (Zebrafish) or Apple reduce orders.

---

## For theses

- **[[Long Broadcom]]** — ASIC explosion thesis, $14.5B → $100B F27E
- [[Long TSMC]] — Broadcom's custom chips all go to TSMC, reinforces moat
- [[Short TSMC long Korea]] — neutral to bearish Korea; more TSMC demand, not Samsung

---

## Recent developments (Dec 2025)

**OpenAI deal (Oct 2025):**
- $10B commitment, 10GW capacity
- Custom Titan chips, H2 2026 production
- Stock +9% on announcement

**Citi projections:**
- F25: $14.5B ASIC revenue
- F26E: $50.5B (+248%)
- F27E: $100B (+98%)

**Stock**: +50% YTD, market cap $1.5T+

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | AVGO (NASDAQ) |
| Market cap | ~$1.1T |
| Revenue (FY25) | ~$52B |
| AI revenue (FY25) | ~$14.5B |
| AI revenue (F27E) | $100B (Citi) |
| Gross margin | ~65% |
| Dividend yield | ~1.1% |

---

## Related

- [[Google]] — major customer (TPU design), disintermediating
- [[Anthropic]] — customer (~1M TPUv7 direct purchase)
- [[Meta]] — customer (custom ASICs)
- [[OpenAI]] — customer ($10B Titan chip deal)
- [[TSMC]] — foundry (95% of wafers)
- [[NVIDIA]] — competitor (GPU vs ASIC)
- [[MediaTek]] — competitor (Zebrafish threat)
- [[Coherent]] — competitor (optical)
- [[Lumentum]] — competitor (optical)
- [[Arista Networks]] — customer (networking silicon)
- [[TeraWulf]], [[Hut 8]], [[Cipher Mining]] — DC partners for Anthropic TPUs
- [[FluidStack]] — deployment partner for Anthropic
- [[Long Broadcom]] — thesis
- [[Hyperscaler chip roadmap]] — disintermediation risk context
