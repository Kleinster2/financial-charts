#concept #semiconductor #manufacturing #lithography

# Multi-patterning

Technique extending [[DUV lithography]] to smaller nodes via multiple exposure/etch cycles. Enables 7nm with 193nm light. China's workaround for EUV ban. Practical limit ~5nm due to cumulative defects.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Purpose | Extend DUV resolution |
| Key techniques | SADP, SAQP, LELE |
| Practical limit | ~7nm (5nm with severe penalties) |
| Cost vs EUV | Cheaper at 7nm, expensive at 5nm |
| China reliance | Primary advanced node approach |

---

## Why needed

**DUV wavelength (193nm) cannot directly pattern sub-40nm features.**

Single exposure resolution limit: ~40nm
Target features at 7nm node: ~20nm pitch

Solution: Multiple exposures to subdivide patterns.

---

## Key techniques

### LELE (Litho-Etch-Litho-Etch)

| Step | Action |
|------|--------|
| 1 | First lithography exposure |
| 2 | Etch pattern |
| 3 | Second lithography exposure |
| 4 | Etch second pattern |

**Pros:** Flexible, established
**Cons:** Two full litho steps = expensive

### SADP (Self-Aligned Double Patterning)

| Step | Action |
|------|--------|
| 1 | Pattern core structures |
| 2 | Deposit spacer film |
| 3 | Etch spacers (creates 2x density) |
| 4 | Remove core |

**Pros:** More cost-effective than LELE
**Cons:** Less flexible pattern options

### SAQP (Self-Aligned Quadruple Patterning)

| Step | Action |
|------|--------|
| 1-3 | First SADP cycle |
| 4-6 | Second SADP cycle |
| Result | 4x original density |

**Pros:** Reaches 5nm-class features
**Cons:** 4 opportunities for defects

---

## Process complexity

| Node | DUV steps | EUV steps |
|------|-----------|-----------|
| 7nm | 34 | 9 |
| 5nm | 50+ | 12-15 |

| Node | DUV masks | EUV masks |
|------|-----------|-----------|
| 7nm | 80-85 | 25-30 |
| 5nm | 100+ | 35-40 |

More steps = more defect opportunities, longer cycle time.

---

## Cost trade-offs

| Node | DUV multi-patterning | EUV |
|------|---------------------|-----|
| **7nm** | **Cheaper** | More expensive |
| **5nm** | **More expensive** | Cheaper |

Crossover point: ~7nm. Below that, EUV economics win.

---

## The 5nm wall

Multi-patterning breaks down at 5nm:

| Problem | Impact |
|---------|--------|
| Overlay precision | Each step compounds misalignment |
| Line roughness | Accumulates with each cycle |
| Defects | 4 steps = 4x defect opportunities |
| Yield | **Abrupt collapse** if tolerances exceeded |

Unlike gradual degradation, yield can drop suddenly when overlay budget exhausted.

---

## China's approach

With [[EUV lithography]] banned, [[SMIC]] uses extreme multi-patterning:

| Node | Method | Status |
|------|--------|--------|
| 7nm | SAQP | Production (Huawei Mate 60 Pro) |
| 5nm | Extreme SAQP | Testing |

**Penalties:**

| Metric | SMIC | TSMC |
|--------|------|------|
| 7nm yield | ~50% | ~76% (at launch) |
| 5nm yield (projected) | 30-40% | ~80% |
| 5nm cost | **+50%** vs TSMC | Baseline |

---

## Why China can't compete at 5nm

| Factor | Impact |
|--------|--------|
| Yield | 30-40% vs 80% = 2x waste |
| Cost | +50% per good wafer |
| Throughput | Slower cycle time |
| Cumulative | Economics unworkable |

Multi-patterning is **not a viable long-term substitute** for EUV at advanced nodes.

---

## Where multi-patterning works

| Application | Viability |
|-------------|-----------|
| 7nm and above | Cost-effective |
| Mature nodes | Standard approach |
| Select layers | Even with EUV, some layers use DUV |
| Memory | 3D NAND uses multi-patterning |

---

## Related

**Technology:**
- [[DUV lithography]] — base technology being extended
- [[EUV lithography]] — alternative that avoids multi-patterning
- [[High-NA EUV]] — further reduces patterning needs

**Companies:**
- [[ASML]] — DUV supplier
- [[Nikon]] — DUV supplier
- [[SMIC]] — relies on multi-patterning

**Context:**
- [[Export controls]] — forces China to use multi-patterning
- [[Semiconductor manufacturing]] — where technique fits

*Created 2026-01-28*
