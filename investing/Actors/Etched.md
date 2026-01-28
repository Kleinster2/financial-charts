#actor #semiconductors #ai #startup #hardware

**Etched** — AI hardware startup building the "Sohu" chip. Betting everything on the [[Transformer]] architecture.

---

## The Thesis: Burn the Boats

Etched is a contrarian bet against flexibility:
*   **NVIDIA GPUs:** General purpose (can run anything, but inefficient).
*   **Groq/[[Cerebras]]:** Specialized architectures (better, but still programmable).
*   **Etched:** Hard-coded ASIC for Transformers (zero programmability).

**The Gamble:** If the [[Transformer]] architecture (GPT, [[Llama]], etc.) remains dominant, Etched offers **order-of-magnitude** better performance and efficiency. If architectures shift (e.g., to SSMs/Mamba), Etched chips become paperweights.

---

## Sohu Chip

*   **Function:** Dedicated [[Transformer]] ASIC.
*   **Performance:** Claims 10x faster/cheaper token generation than H100.
*   **Efficiency:** Massive tokens-per-watt advantage.
*   **[[Target]]:** The "Decode" phase of inference (generating tokens one by one).

---

## Funding

| Round | Date | Amount | Valuation | Lead |
|-------|------|--------|-----------|------|
| Series A | 2024 | $120M | — | Primary Venture Partners |
| Series B | Jan 2026 | **$500M** | **$5B** | Stripes |
| **Total raised** | | **~$1B** | | |

**Key investors:**
- [[Peter Thiel]]
- [[Stripes LLC]] (led Series B)
- Positive Sum
- [[Ribbit Capital]]
- [[Founders Fund]]
- Primary Venture Partners

**Production:** Partnered with [[TSMC]] Emerging Businesses Group.

---

## Team

Recruited from [[Broadcom]], Cypress Semiconductor, and other chip companies.

---

## Role in Inference Stack

See [[Long inference stack]].
Etched represents the extreme end of the **specialization spectrum**:
`CPU (General) -> GPU (Parallel) -> LPU (Groq) -> ASIC (Etched)`

---

## Related

- [[Long inference stack]] — the broader thesis
- [[NVIDIA]] — the incumbent to disrupt
- [[Groq]] — the programmable competitor
- [[Inference disaggregation]] — the structural trend
- [[Power constraints]] — efficiency driver
- [[TSMC]] — manufacturing partner
- [[Broadcom]] — talent source

---

*Updated 2026-01-15*
