---
aliases: [LITE, Lumentum Holdings]
tags: [actor, interconnect, optical, usa]
---

**Lumentum** — optical component maker with the only 200Gbps EML shipping at scale. Critical bottleneck supplier for 800G/1.6T AI data center interconnects. Strategic [[NVIDIA]] partner since March 2026.

---

## Synopsis

Lumentum sits at a chokepoint in the AI infrastructure stack: its electro-absorption modulated lasers (EMLs) enable the high-speed transceivers that connect GPUs inside data center clusters. The 200Gbps EML — which Lumentum alone ships at volume — is the building block for 1.6T transceivers (8 lanes × 200G), the next generation of AI networking. Revenue has nearly doubled from trough ($308M in Q4 FY2024) to $666M in Q2 FY2026, driven entirely by AI-related demand for datacom lasers. The company also makes ROADMs and optical circuit switches (R300), positioning it in the emerging optical switching layer for AI clusters. The March 2026 [[NVIDIA]] $2B strategic investment transformed the relationship from supplier to aligned partner.

---

## Why it matters for AI interconnects

EML = electro-absorption modulated laser. Combines laser + modulator in one chip. Higher speed, lower power than alternatives like directly modulated lasers or silicon photonics approaches. Critical for 800G+ transceivers.

Lumentum's lead:
- Only 200Gbps EML shipping at scale — 2+ year technology lead
- Enables 1.6T transceivers (8 × 200G lanes)
- Supply constrained — demand outpaces fab capacity
- Customer base includes transceiver makers ([[Coherent]], [[Lumentum]] → [[Fabrinet]] for contract manufacturing), hyperscalers directly, and network OEMs like [[Arista Networks]]

Transceiver architecture context:

| Generation | Architecture | EML requirement |
|------------|-------------|-----------------|
| 800G | 8 × 100G or 4 × 200G | 200G EML preferred |
| 1.6T | 8 × 200G | 200G EML required |
| 3.2T (next) | 8 × 400G | Next-gen EML |

---

## Product portfolio

| Category | Products |
|----------|----------|
| Datacom lasers | 200G EMLs, VCSELs |
| ROADMs | Reconfigurable optical add-drop multiplexers |
| Optical switching | R300 Optical Circuit Switch |
| 3D sensing | [[Consumer]] electronics (declining segment) |
| [[Telecom]] | Coherent components |

The datacom laser business is where the growth is. 3D sensing (historically tied to smartphone face-unlock) has been a drag and is being de-emphasized.

---

## Financials

Fiscal year ends June 30. Revenue trough was mid-2024; the ramp since then has been steep and accelerating.

| Quarter | Revenue | Net income | Margin |
|---------|---------|------------|--------|
| Q3 FY2024 (Mar 2024) | $337M | -$82M | -24% |
| Q4 FY2024 (Jun 2024) | $308M | -$253M | -82% |
| Q1 FY2025 (Sep 2024) | $337M | -$82M | -24% |
| Q2 FY2025 (Dec 2024) | $402M | -$61M | -15% |
| Q3 FY2025 (Mar 2025) | $425M | -$44M | -10% |
| Q4 FY2025 (Jun 2025) | $481M | $213M | 44% |
| Q1 FY2026 (Sep 2025) | $534M | $4M | 1% |
| Q2 FY2026 (Dec 2025) | $666M | $78M | 12% |

Q4 FY2025 net income spike ($213M on $481M rev) likely includes a one-time gain — operating income was still negative that quarter (-$8M). The Dec 2025 quarter is the first clean profitable quarter: $64M operating income on $666M revenue, 65.5% YoY revenue growth.

Annual: FY2024 was the trough at $1.36B rev, -$547M net loss. FY2025 recovered to $1.65B, roughly breakeven. TTM revenue run rate is now ~$2.1B.

![[lite-fundamentals-chart.png]]
*LITE price history since 2020*

![[lite-waterfall.png]]
*Quarterly income waterfall — latest available quarter*

![[lite-sankey.png]]
*Revenue flow breakdown*

---

## NVIDIA $2B strategic investment (Mar 2, 2026)

[[NVIDIA]] investing $2B in Lumentum — equity, multibillion-dollar purchase commitment, capacity rights for ultra-high-power lasers for co-packaged optics. Nonexclusive. Funding new US fabrication facility. LITE +8% premarket. Transforms the NVIDIA relationship from adjacent to strategic partner — NVIDIA becomes a shareholder with aligned incentives. See [[NVIDIA photonics investment March 2026]] for full deal structure and technical context.

---

## OFC 2026

Joint demo with [[Marvell]]: COLORZ 800 ZR/ZR+ DCI interop with Lumentum's R300 Optical Circuit Switch — demonstrating end-to-end data center interconnect with optical switching. The R300 is Lumentum's play to replace electrical patch panels in AI clusters with programmable optical switching fabric. See [[OFC 2026]].

---

## Optical switching

Beyond lasers, the R300 Optical Circuit Switch targets AI cluster networking. ROADM technology repurposed for data center optical switching — programmable, non-blocking, low-latency optical paths between GPU racks. Growing relevance as AI cluster scale drives demand for optical (not electrical) switching fabric. The OFC 2026 demo with [[Marvell]] is the commercial proof point.

---

## Competitive position

| Competitor | Segment | How Lumentum differs |
|------------|---------|---------------------|
| [[Coherent]] | Full transceiver modules | Lumentum supplies components into the module |
| [[Broadcom]] | Silicon photonics | Traditional III-V optical approach vs Si photonics |
| Source Photonics | Transceivers | Component supplier, not module maker |
| [[Coherent]] (fmr. II-VI) | Lasers | Lumentum's EML lead at 200G |

The competitive moat is the 200G EML technology lead. The open question is how long that lead persists — whether silicon photonics at scale (Broadcom, [[Intel]]) eventually closes the gap, or whether III-V compound semiconductors retain a structural advantage at these speeds.

---

## Dynamics and open questions

The revenue ramp from $308M (Jun 2024 trough) to $666M (Dec 2025) is a 2.2× acceleration in 18 months — driven almost entirely by AI datacom demand. The stock has gone from a 52-week low of $49 to nearly $960, reflecting the market repricing Lumentum from a struggling optical company to an AI infrastructure bottleneck.

Open questions:
- How much of the 200G EML monopoly translates into pricing power vs. capacity commitments at fixed margins?
- NVIDIA's $2B investment secures supply for NVIDIA — does it lock out other hyperscalers, or does the nonexclusive structure preserve optionality?
- 3D sensing drag: this segment generated significant revenue historically ($400M+ annual at peak). How fast does it decline, and does the AI ramp more than offset it?
- The 3.2T transceiver generation (8 × 400G) will need a next-gen EML. Is Lumentum investing in 400G development, or does silicon photonics become competitive at that node?
- Customer concentration risk: if [[Coherent]] and a handful of hyperscalers represent the bulk of datacom laser revenue, how diversified is the demand base?

---

## Sector correlation

Daily return correlations since Jan 2025 (available optical/networking peers):

| Peer | Correlation | Relationship |
|------|-------------|-------------|
| [[Broadcom]] (AVGO) | 0.50 | Silicon photonics competitor, AI networking |
| [[Marvell]] (MRVL) | 0.40 | Joint demo partner, DSP supplier for transceivers |
| [[Arista Networks]] (ANET) | 0.38 | Network switching OEM, same AI capex cycle |

[[Coherent]] (COHR) and [[Fabrinet]] (FN) — the closest optical peers — are not yet in the database. Adding them would give a more complete correlation picture.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | LITE |
| Price | $897.30 (Apr 10, 2026) |
| Market cap | $63.8B |
| Shares outstanding | 71.4M |
| 52-week range | $49.13 – $960.00 |
| P/E (trailing) | 256× |
| P/E (forward) | 59× |
| EPS (diluted) | $3.49 |
| Revenue (TTM) | ~$2.1B |
| Q2 FY2026 revenue | $666M (+65.5% YoY) |
| Beta | 1.39 |
| Analyst target | $748 (consensus) |
| HQ | San Jose, CA |
| FY end | June 30 |

---

## Related

- [[Coherent]] — customer (transceiver maker) and competitor (post II-VI merger)
- [[Fabrinet]] — contract manufacturer
- [[Arista Networks]] — adjacent (network OEM)
- [[NVIDIA]] — strategic investor ($2B, GPU clusters need optical)
- [[AI hyperscalers]] — end customers (800G/1.6T demand)
- [[Marvell]] — COLORZ 800 / R300 joint demo at OFC 2026
- [[OFC 2026]] — R300 Optical Circuit Switch demo
- [[NVIDIA photonics investment March 2026]] — full deal structure
- [[Broadcom]] — silicon photonics competitor
- [[Lumentum securities]] — price history and technicals
