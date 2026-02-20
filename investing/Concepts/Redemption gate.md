---
aliases: [fund gate, gating, redemption suspension, fund suspension, redemption halt, liquidity gate]
---
#concept #credit #risk #liquidity

**Redemption gate** — A mechanism allowing fund managers to restrict or halt investor withdrawals. Gates exist because of the fundamental **liquidity mismatch** at the heart of many pooled investment vehicles: investors expect periodic access to their capital, but the underlying assets can't be sold quickly without losses. When redemption requests overwhelm a fund's liquid reserves, the manager faces a choice — honor redemptions (fire-selling assets, punishing remaining investors) or gate (trapping everyone equally).

Gates are the financial equivalent of closing the bank doors during a run.

---

## Types

### 1. Investor-level gate
Caps how much any **single investor** can redeem per period (e.g., 25% of their holdings per quarter). Remaining requests roll to the next period.

### 2. Fund-level gate
Caps **total fund redemptions** per period (e.g., 5% of NAV per quarter). If requests exceed the cap, they're pro-rated across all redeeming investors. Most common type.

### 3. Temporary suspension
**All redemptions halted** for a defined or indefinite period during extraordinary circumstances. Manager must typically notify investors in writing and may need legal counsel. Common during market dislocations.

### 4. Permanent halt
Redemption mechanism **eliminated entirely**. Fund shifts to wind-down mode — returning capital through asset sales and distributions over time. The most extreme form. Example: [[Blue Owl OBDC II redemption gate]] (Feb 2026).

### 5. Partial suspension (side pocket)
Specific illiquid or hard-to-value assets are **segregated** into a side pocket. Investors can redeem the liquid portion but their share of the side pocket is locked until those assets are sold or mature.

### 6. In-kind redemption
Instead of cash, investors receive **actual securities** from the portfolio. Shifts the liquidation burden to the investor. Common in ETFs; rare but possible in hedge funds.

---

## How it works

```
Redemption requests surge
        ↓
Fund's liquid reserves insufficient
        ↓
Manager invokes gate provision
        ↓
Investors notified in writing
        ↓
Redemptions capped, delayed, or halted
        ↓
Fund sells assets in orderly fashion (or winds down)
        ↓
Capital returned over time via distributions
```

**Key tension:** Gates protect remaining investors from fire-sale losses, but they trap capital and destroy trust. Once a gate is imposed, it often **accelerates** redemption pressure on similar funds — investors elsewhere rush to redeem *before* they get gated too.

---

## When gates get triggered

- **Redemption surge** exceeds liquid reserves or quarterly caps
- **Asset illiquidity** — underlying holdings can't be sold without significant losses
- **Market dislocation** — forced selling would lock in losses at the worst time
- **NAV uncertainty** — assets can't be reliably valued (e.g., post-crisis)
- **Contagion risk** — honoring early redemptions would harm remaining investors (first-mover advantage)
- **Regulatory action** — authorities may order suspension (rare)

---

## The game theory

Gates create a **prisoner's dilemma**:

| | You redeem early | You stay |
|---|---|---|
| **Others redeem** | You get out at NAV (win) | You're stuck holding depreciated assets (lose) |
| **Others stay** | You get liquidity (win) | Fund operates normally (neutral) |

The rational move is always to redeem early → which is exactly what causes the run → which forces the gate. This is why gates are **self-fulfilling**: the mere *possibility* of a gate incentivizes the behavior that triggers it.

Once one fund gates, **contagion** follows — investors in similar funds rush to redeem before they're gated too. This is the mechanism behind systemic liquidity crises.

---

## Notable historical gates

| Date | Fund | Type | What happened |
|------|------|------|---------------|
| **June 2007** | Bear Stearns High-Grade Structured Credit Fund | Suspension | Froze $1.6B in redemptions after subprime losses. Investors sought ~$250M — fund couldn't pay. **The opening act of the 2008 financial crisis.** Both funds liquidated by July. |
| **2008** | Dozens of hedge funds | Various | GFC triggered mass gating. ~18% of hedge fund assets were gated at peak (HFR data). Citadel, DE Shaw, Tudor among those restricting withdrawals. |
| **Dec 2015** | Third Avenue Focused Credit Fund | Permanent halt | $788M junk bond fund blocked all redemptions and liquidated. Triggered high-yield panic. First US mutual fund to gate since 2008. |
| **2016** | UK property funds (post-Brexit) | Suspension | £15B+ in open-ended property funds suspended after Brexit vote. Standard Life, Aviva, M&G, Henderson all gated within days. |
| **2018** | GAM Absolute Return Bond Fund | Suspension | $11B fund suspended after star manager Tim Haywood fired for due diligence failures. Wound down over 2+ years. |
| **June 2019** | Woodford Equity Income Fund | Suspension → liquidation | Neil Woodford's £3.7B fund suspended after illiquid positions couldn't be sold to meet redemptions. Liquidated Jan 2020. UK's biggest fund scandal in a decade. |
| **March 2020** | Multiple (COVID) | Various | Property funds, credit funds gated during COVID panic. £20B+ in UK property funds suspended. |
| **Late 2022** | Blackstone BREIT/BCRED | Fund-level gate (caps hit) | Redemption requests exceeded quarterly 5% NAV cap. Managed within existing structure — no suspension — but spooked markets. |
| **Feb 2026** | [[Blue Owl OBDC II redemption gate\|Blue Owl OBDC II]] | **Permanent halt** | First retail BDC to permanently end redemptions. Sold $1.4B at 99.7% par, shifting to wind-down distributions. Triggered [[Private credit retail liquidity crisis 2026]]. |

---

## The pattern

Every major gate follows the same script:

1. **Assets become illiquid** (or their liquidity is revealed to have been illusory)
2. **Redemptions accelerate** as investors front-run the problem
3. **Manager gates** — framing it as "orderly" and "in investors' best interest"
4. **Contagion** — similar funds see redemption spikes
5. **Narrative shifts** from "isolated incident" to "systemic concern"
6. **Regulators respond** (usually too late)

Bear Stearns 2007 → GFC. OBDC II 2026 → ? The question is always the same: **is this the only one, or the first one?**

---

## Structural context

### Why gates are becoming more common
- **Retailization of alternatives** — PE/credit firms selling semi-liquid products to retail investors who expect bank-like access to their money
- **Liquidity mismatch by design** — funds hold illiquid assets but offer quarterly redemption windows to attract capital
- **Low-vol illusion** — private credit/PE marks assets quarterly (smoothing volatility), making them *look* safer than they are until stress hits
- **Herding** — everyone piled into the same trades (private credit software, leveraged buyouts) during the low-rate era

### Regulatory landscape
- **US:** Limited regulation of private fund gates. SEC proposed liquidity risk management rules (2022-23) but enforcement is light. Sen. Warren called for stress tests and disclosure after OBDC II (Feb 2026).
- **UK:** FCA tightened rules after Woodford — longer notice periods, more disclosure, but open-ended property fund problem persists.
- **EU:** AIFMD requires "liquidity management tools" including gates and swing pricing. ESMA pushing for mandatory tools post-COVID.

---

## Key terms

| Term | Meaning |
|------|---------|
| **Gate provision** | Contractual clause in fund docs authorizing the manager to restrict redemptions |
| **Lock-up period** | Initial period (often 1-2 years) where no redemptions allowed at all |
| **Notice period** | Required advance notice for redemption requests (30-90 days typical) |
| **Redemption window** | Specific dates when redemptions are processed (quarterly, monthly) |
| **Queue / pro-rata** | When requests exceed the gate cap, they're either queued (FIFO) or pro-rated |
| **Side pocket** | Segregated illiquid assets that can't be redeemed |
| **Swing pricing** | Adjusting NAV to pass transaction costs to redeeming investors |
| **Soft gate** | Redemptions allowed but with a penalty fee (e.g., 2-5% early redemption fee) |
| **Hard gate** | Redemptions blocked entirely |

---

## Related

- [[Private credit retail liquidity crisis 2026]] — current systemic event
- [[Blue Owl OBDC II redemption gate]] — first retail BDC permanent halt
- [[March 2020 liquidity crisis]] — COVID-era gates
- [[Private credit]] — market context
- [[Liquidity mismatch]] — root cause
- [[Bank run]] — same dynamics, different wrapper
