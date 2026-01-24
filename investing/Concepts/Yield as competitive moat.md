#concept #moat #execution

In semiconductor manufacturing, **yield** (percentage of working chips per wafer) directly determines profitability and customer trust. It's the hardest moat to replicate.

> **Key insight:** Yield is accumulated learning, not a technology you can buy. You can license a process node; you cannot license the thousands of micro-optimizations that make it work at scale.

---

## What yield means

| Term | Definition |
|------|------------|
| Yield | % of chips on a wafer that work |
| Die yield | Working chips / total chips per wafer |
| Wafer yield | % of wafers that pass qualification |
| Line yield | Combined impact of all process steps |

**Example math:**
- 100 chips per wafer, 70% yield = 70 good chips
- At $10K wafer cost: $143/chip at 70% yield vs $200/chip at 50% yield
- 20 percentage point yield difference = 40% cost difference

---

## Why it matters

**The yield cascade:**

| Low yield impact | Consequence |
|-----------------|-------------|
| Higher cost per chip | Uncompetitive pricing |
| Unpredictable supply | Customers can't plan |
| Quality issues | Defects in shipped products |
| Ramp delays | Miss product launch windows |
| Customer defection | Switch to reliable foundry |

**The trust problem:** Customers need to commit designs 18-24 months ahead. They won't bet on a foundry with yield uncertainty.

---

## Current state (late 2025)

| Foundry | Node | Yield | Notes |
|---------|------|-------|-------|
| [[TSMC]] | 3nm | 70-80% | Mature, shipping at volume |
| [[TSMC]] | 2nm | 60%+ | Ramping, expected to improve |
| [[Samsung]] | 3nm GAA | 55-65% | Improved from early struggles |
| [[Samsung]] | 2nm | Unknown | Not yet in production |
| [[Intel Foundry Services]] | Intel 3 | 60%+ | Internal only |
| [[Intel Foundry Services]] | 18A | Unknown | Not yet in production |

**The gap:** TSMC's 2-year head start on 3nm GAA means accumulated yield learning Samsung can't shortcut.

---

## Why yield is hard to catch up

**Yield improvement comes from:**

| Source | Can it be copied? |
|--------|-------------------|
| Equipment tuning | Partially (same tools) |
| Process recipes | Yes (can license) |
| Defect learning | No (must be earned) |
| Operator expertise | No (takes years) |
| Supplier relationships | Partially |
| Institutional knowledge | No (accumulated over decades) |

**The uncomfortable truth:** TSMC's yield advantage is the result of 30+ years of continuous improvement. There's no shortcut.

---

## How yield compounds advantage

| TSMC yield advantage | Knock-on effect |
|---------------------|-----------------|
| Lower cost per chip | Better pricing |
| More chips per wafer | Higher capacity |
| Reliable supply | Customer trust |
| Faster qualification | Time-to-market |
| Higher margins | R&D reinvestment |
| Customer stickiness | Volume growth |

**The flywheel:** High yields → more customers → more volume → more learning → higher yields.

---

## Strategic implications

**For TSMC:**
- Treats yield maturity as prerequisite for geographic expansion
- Won't deploy immature processes in new fabs (see [[Node lag as strategy]])
- Yield leadership protects against price competition

**For Samsung:**
- Must achieve rapid yield improvement to validate [[Samsung Taylor pivot]]
- Can't win on price if yields are inferior
- Every yield miss extends TSMC's lead

**For Intel:**
- 18A yield will determine foundry viability
- Internal chips are proving ground
- External customers won't commit without yield proof

---

## Investment implications

**What to watch:**
- Earnings calls: yield commentary, ramp updates
- Customer wins: high-volume customers signal yield confidence
- Pricing: foundries with lower yields must discount

**The yield tell:** When a foundry stops talking about yield improvements, it's either mature (TSMC) or a problem (everyone else).

*Updated 2026-01-04*

---

## Related

- [[Foundry monopoly consolidation]] — broader framework (yield is one of 5 reinforcing dynamics)
- [[TSMC]] — leader (60-70%+ mature yields)
- [[Samsung]] — improving (55-60% at 2nm, up from 10-20%)
- [[Intel Foundry Services]] — unproven (18A yields TBD)
- [[Customer lock-in via co-design]] — related moat
- [[Advanced packaging]] — related moat (CoWoS)
- [[Execution risk in foundries]] — manifestation (low yields = customer loss)
