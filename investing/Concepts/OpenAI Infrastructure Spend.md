#concept #ai #infrastructure

**OpenAI Infrastructure Spend** — tracking [[OpenAI]]'s compute investment plans, infrastructure deals, and the gap between announced commitments and actual spend targets.

---

## Compute spend reset (Feb 20, 2026)

OpenAI told investors it's now targeting **~$600B in total compute spend by 2030**, down from the **$1.4T infrastructure commitment** touted by [[Sam Altman]] in late 2025.

| Metric | Previous | Revised |
|--------|----------|---------|
| Infrastructure target | $1.4T ("commitments") | **~$600B** (compute spend) |
| Timeline | Vague ("coming years") | **By 2030** |
| 2030 revenue forecast | Not disclosed | **$280B** |

**Key nuance:** The $1.4T included partner commitments ([[SoftBank]], [[Oracle]] for [[Stargate]]); the $600B is OpenAI's own compute spend (training + inference). Still a massive number but more grounded and directly tied to revenue projections.

The spending plan is meant to more directly tie to expected revenue growth — with $280B projected for 2030, split roughly equally between consumer ([[ChatGPT]]) and enterprise businesses. The implied compute-to-revenue ratio: ~2:1.

**CFO argument (Jan 2026):** Sarah Frier published blog claiming revenue tracks compute 1:1 — 10x revenue growth (2023–2025) alongside 9.5x compute growth. Implies more capital = more revenue. The $600B/$280B ratio suggests this relationship may not hold at scale.

*Source: CNBC, Feb 20, 2026.*

---

## Stargate infrastructure

### UAE Stargate (per SemiAnalysis, Jan 2026)

| Metric | Value |
|--------|-------|
| Location | UAE |
| Power source | 4x [[Ansaldo Energia]] AE94.3 gas turbines |
| Gross capacity | 1.3GW |
| Derated capacity | **1GW** (desert heat penalty −23%) |
| Phase 1 | 200MW by YE2026 |
| Status | "Going well" |

**Key insight:** On-site gas turbines = [[BYOP]] (Bring Your Own Power). Desert heat derates capacity by 23%.

**Texas Abilene (contrast):** "GPUs not going BRRR" — UAE progressing faster than domestic site.

**Turbine supplier:** [[Ansaldo Energia]] (Italian)

---

## Cerebras compute deal (Jan 14, 2026)

| Metric | Value |
|--------|-------|
| Deal value | **$10B+** |
| Compute | 750 MW |
| Duration | 2026–2028 |
| Use case | Inference (especially coding) |

**Why [[Cerebras]]:**
- 15x faster responses than GPU-based systems
- [[Sam Altman]] was early Cerebras investor
- Diversifies away from [[NVIDIA]]/[[Microsoft]] dependency

**Cerebras CEO:** "Largest high-speed AI inference deployment in the world."

---

## Nvidia inference concerns (Feb 2026)

**[[Reuters]] exclusive (Feb 2):** OpenAI dissatisfied with some [[NVIDIA]] chips, actively seeking alternatives.

| Issue | Detail |
|-------|--------|
| Problem | Inference speed for specific workloads |
| Affected products | [[Codex]] (coding), agent-to-agent comms |
| Need | Faster "time to first token" |
| Target | ~10% of inference compute from alternatives |

**Chip requirements:**
- SRAM-heavy architecture (memory embedded on silicon)
- Traditional GPUs rely on external memory → slower fetch times
- Inference needs more memory bandwidth than training

**Alternatives explored:**

| Company | Status |
|---------|--------|
| [[AMD]] | GPUs purchased |
| [[Cerebras]] | Commercial deal signed (Jan 2026) |
| [[Groq]] | Talks shut down after [[NVIDIA]] acquisition |

**Impact on Nvidia investment:**
- Nvidia's proposed $100B stake (announced Sept 2025) delayed for months
- Expected to close "within weeks" — still in negotiations
- [[Jensen Huang]]: Investment "was never a commitment" (Bloomberg)
- Huang denies drama: "There's no drama involved" (CNBC Feb 3)

**[[Sam Altman]] response (Feb 2):** Nvidia makes "the best AI chips in the world." OpenAI hopes to remain "gigantic customer for a very long time."

**[[NVIDIA]] defensive moves:**
- Acquired [[Groq]] IP for $20B (Dec 2025)
- Hired away Groq chip designers
- Non-exclusive licensing deal — Groq pivoting to cloud software

*Updated 2026-02-04*

---

## $100B+ mega-round (Feb 2026)

Largest private funding round in history. ~90% from strategic investors. First tranche closing by end of February.

| Investor | Amount | Status |
|----------|--------|--------|
| [[Amazon]] | Up to **$50B** | In talks |
| [[SoftBank]] | ~**$30B** | In talks (on top of prior $41B) |
| [[NVIDIA]] | Up to **$30B** | In talks |
| [[Microsoft]] | TBD | Expected |
| VCs + SWFs | TBD | Later tranche |

*Source: Bloomberg/CNBC, Feb 2026.*

$850B+ post-money ($730B pre-money). [[Amazon]] potentially contributing half the round — would make them a major OpenAI stakeholder alongside [[Microsoft]] and [[SoftBank]]. [[NVIDIA]] increasing from $250M (Oct 2024) to up to $30B signals deepening strategic ties despite inference chip tensions.

### Prior $50B Middle East round (Jan 2026)

| Detail | Value |
|--------|-------|
| Raise | $50B+ |
| Valuation | $750–830B |
| Key investors | [[MGX]] (Abu Dhabi), other Gulf SWFs |
| Status | Superseded by $100B+ mega-round (Feb 2026) |

---

## Related

- [[OpenAI]] — parent actor
- [[Stargate]] — joint venture with [[SoftBank]]
- [[AI infrastructure financing]] — GW economics (1 GW = $10B funding)
- [[Cerebras]] — $10B+ inference compute deal
- [[NVIDIA]] — primary GPU supplier, inference tensions
- [[Ansaldo Energia]] — turbine supplier (UAE Stargate)
- [[BYOP]] — on-site power generation pattern
- [[Power constraints]] — grid gap context
- [[UAE Tech]] — Stargate UAE site (1GW)
- [[AI Infrastructure]] — sector hub
- [[Model lab economics]] — profitability analysis
