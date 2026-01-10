#actor #semiconductors #ai #startup #hardware

**Etched** — AI hardware startup building the "Sohu" chip. Betting everything on the Transformer architecture.

---

## The Thesis: Burn the Boats

Etched is a contrarian bet against flexibility:
*   **NVIDIA GPUs:** General purpose (can run anything, but inefficient).
*   **Groq/Cerebras:** Specialized architectures (better, but still programmable).
*   **Etched:** Hard-coded ASIC for Transformers (zero programmability).

**The Gamble:** If the Transformer architecture (GPT, Llama, etc.) remains dominant, Etched offers **order-of-magnitude** better performance and efficiency. If architectures shift (e.g., to SSMs/Mamba), Etched chips become paperweights.

---

## Sohu Chip

*   **Function:** Dedicated Transformer ASIC.
*   **Performance:** Claims 10x faster/cheaper token generation than H100.
*   **Efficiency:** Massive tokens-per-watt advantage.
*   **Target:** The "Decode" phase of inference (generating tokens one by one).

---

## Investors

*   **Primary:** Positive Sum, Founders Fund.
*   **Valuation:** ~$500M+ (Seed/Series A stage).

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

---

*Created 2026-01-09*
