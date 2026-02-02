#concept #credit #structure #legal

# SPV Financing

**Borrow through a subsidiary** — a Special Purpose Vehicle (SPV) is a separate legal entity created to isolate specific assets or liabilities. In SPV financing, a company creates a subsidiary to issue debt secured by specific collateral, keeping it separate from the parent's obligations.

---

## How it works

```
Parent Company
    ↓ creates
SPV (Special Purpose Vehicle)
    ↓ holds
Specific Assets (real estate, receivables, IP)
    ↓ issues
Debt secured by those assets only
```

**Key feature:** SPV creditors can only claim the SPV's assets — they can't reach up to the parent. This is "bankruptcy remote" structure.

---

## Why companies use SPVs

| Benefit | Explanation |
|---------|-------------|
| **Asset isolation** | Protect specific assets from parent's creditors |
| **Bankruptcy remote** | SPV survives if parent fails (and vice versa) |
| **Better credit terms** | Lenders underwrite the asset, not the whole company |
| **Off-balance sheet** | May not consolidate (depends on control) |
| **Specific collateral** | Ring-fence the best assets for targeted financing |

---

## Common SPV structures

| Structure | Assets | Use case |
|-----------|--------|----------|
| **PropCo** | Real estate | Property financing |
| **Receivables SPV** | Accounts receivable | Securitization |
| **IP HoldCo** | Intellectual property | Licensing royalties |
| **Project finance** | Single project | Infrastructure, energy |
| **CMBS conduit** | Mortgages | Commercial mortgage securities |

---

## Case study: Saks Global

[[Saks Global]] used multiple SPVs:

### Flagship PropCo

```
Saks Global Holdings LLC (parent)
    └── Saks Fifth Avenue HoldCo LLC ("HoldCo II")
            └── Saks Flagship Real Property LLC ("Flagship PropCo")
                    └── Owns [[611 Fifth Avenue]]
```

The flagship ($3.6B) was isolated in its own SPV. [[Amazon]] invested at HoldCo II level, expecting this structure would protect their interest. It didn't — in bankruptcy, the flagship was pledged for [[DIP financing]].

### SGUS (financing SPV)

| Entity | Purpose | Debt issued |
|--------|---------|-------------|
| **SGUS** | Financing subsidiary | $762M SPV Notes |

In the August 2025 [[Distressed debt exchange]], Saks created SGUS to issue senior notes. The proceeds were loaned to the operating company via intercompany loans. This gave SGUS noteholders the most senior position in the [[Payment waterfall]].

---

## SPV vs. direct borrowing

| Factor | SPV Financing | Direct Borrowing |
|--------|---------------|------------------|
| Collateral | Specific assets in SPV | General corporate assets |
| Creditor recourse | Limited to SPV | Full recourse to parent |
| Rates | Often lower (asset quality) | Depends on corporate credit |
| Flexibility | Structured for the deal | Standard corporate terms |
| Complexity | Higher (legal structure) | Lower |

---

## Risks of SPV financing

### For lenders
| Risk | Explanation |
|------|-------------|
| **Asset value decline** | Only recourse is the SPV's assets |
| **Structural subordination** | Parent creditors may have other claims |
| **Fraudulent conveyance** | Courts can collapse SPV into parent |
| **Intercompany loans** | SPV may have loaned proceeds to parent (now an unsecured claim) |

### For parent
| Risk | Explanation |
|------|-------------|
| **Covenant restrictions** | SPV debt may limit parent's flexibility |
| **Cross-default** | SPV default triggers parent default |
| **Lost assets** | If SPV fails, parent loses those assets |

---

## Bankruptcy dynamics

**The SPV advantage:** If structured correctly, SPV is "bankruptcy remote" — parent's bankruptcy doesn't trigger SPV default.

**The reality (Saks):** In practice, parent companies often need SPV assets to survive. Courts may:
- Allow parent to pledge SPV assets for DIP
- Substantively consolidate SPV into parent
- Find guarantees that link them

**Amazon's trap:** They invested at HoldCo II (which owned Flagship PropCo) thinking the structure protected them. But HoldCo II had no independent directors — decisions rolled up to parent management, who pledged the flagship anyway.

---

## Related concepts

| Concept | Relationship |
|---------|--------------|
| [[Ground lease]] | Real estate SPV structure |
| [[Lien priority]] | SPV debt has specific collateral |
| [[Payment waterfall]] | SPV creditors get their collateral first |
| [[DIP financing]] | Can prime SPV structures in bankruptcy |
| Securitization | SPVs that issue asset-backed securities |

---

## Investment implications

**For credit investors:**
- Understand what's actually in the SPV
- Intercompany loans may make SPV claim worthless
- "Bankruptcy remote" has limits

**For equity investors:**
- SPV structures can trap value away from equity
- Watch for assets moving into SPVs pre-distress
- Amazon's Saks experience: SPV didn't protect them

**Due diligence:**
- What assets are in the SPV?
- What debt is at SPV vs. parent level?
- Are there intercompany loans?
- Who controls the SPV (independent directors)?
- What are cross-default provisions?

---

## Related

- [[Saks bankruptcy]] — SGUS and Flagship PropCo structures
- [[611 Fifth Avenue]] — held in Flagship PropCo SPV
- [[Minority investor subordination]] — how SPV structure failed Amazon
- [[Payment waterfall]] — SPV creditors in priority stack
- [[DIP financing]] — can override SPV protections
- [[AI infrastructure vehicles]] — AI data center application ([[Meta]]-[[Blue Owl]] template)
- [[AI infrastructure financing]] — broader AI financing context
- [[Private market secondaries]] — VC syndication SPVs (Thrive model)

*Updated 2026-01-26*
