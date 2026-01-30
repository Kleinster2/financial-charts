---
aliases: [Power Usage Effectiveness, power usage effectiveness]
---
#concept #datacenter #efficiency #sustainability

**PUE** (Power Usage Effectiveness) — Standard metric for data center energy efficiency. Ratio of total facility power to IT equipment power. Lower = better. 1.0 = perfect.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Introduced | 2006 |
| Standardized | ISO/IEC 30134-2:2016 |
| Creator | The Green Grid |
| Industry average | ~1.58-1.8 |
| Best-in-class | <1.2 |
| Perfect score | 1.0 |

*Updated 2026-01-29*

---

## Formula

```
PUE = Total Facility Energy / IT Equipment Energy
```

**Total facility energy** = IT equipment + cooling + lighting + power delivery

**IT equipment energy** = Compute + storage + networking

---

## Benchmarks

| PUE | Rating | Notes |
|-----|--------|-------|
| 1.0 | Perfect | Theoretical ideal |
| <1.2 | Excellent | Best-in-class hyperscale |
| 1.2-1.4 | Very good | Modern efficient DCs |
| 1.4-1.6 | Good | Above average |
| 1.6-1.8 | Average | Industry typical |
| >2.0 | Poor | Legacy infrastructure |

---

## Why PUE matters

**The universal DC efficiency language:**

- **Comparability**: Standard metric across industry
- **Trend tracking**: Monitor efficiency over time
- **Green bond eligibility**: Targets often in bond covenants
- **Cost driver**: Lower PUE = lower opex

---

## Brazil DC targets

| Company | PUE Target | Notes |
|---------|------------|-------|
| [[Scala Data Centers]] | <1.40 (avg), <1.30 (new) | Green bond covenant |
| [[Elea Data Centers]] | — | Zero-water cooling systems |

---

## Limitations

| Issue | Detail |
|-------|--------|
| Not comprehensive | Ignores IT equipment efficiency |
| Climate-dependent | Easier to achieve in cool climates |
| Comparability limits | Different configs make cross-DC comparison hard |
| Gaming potential | Measurement methodology varies |

PUE alone doesn't capture renewable energy use, water consumption ([[WUE]]), or carbon intensity.

---

## Related metrics

| Metric | Measures |
|--------|----------|
| **PUE** | Energy efficiency |
| **WUE** | Water usage effectiveness |
| **CUE** | Carbon usage effectiveness |
| **ERE** | Energy reuse effectiveness |

---

## Related

- [[Data Centers]] — sector
- [[Scala Data Centers]] — PUE <1.40 target (green bond covenant)
- [[Elea Data Centers]] — efficiency focus
- [[Green bonds]] — efficiency targets in covenants
- [[Sustainability-linked bonds]] — PUE as common KPI
- [[Sustainalytics]] — verifies PUE compliance
