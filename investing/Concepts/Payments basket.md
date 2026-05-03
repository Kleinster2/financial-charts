---
aliases: [Payments cluster, US payments, Payments stocks]
tags: [concept/cluster, payments, fintech, financials]
---

# Payments basket

> [!failure] Cluster status: falsified as single basket — splits into 4+ sub-factors (May 2026)
> Intra-cluster correlation only 0.40 across V/MA/AXP/PYPL/FIS/FISV/COF/SHOP. PC1 only 48.4%. Hierarchical clustering at 0.4 reveals 4 distinct groups: card networks (V+MA tight pair, correlation 0.87 — the cleanest pair in the entire validation pass); consumer credit / issuer (AXP+COF cluster with banks); processors (FIS, FISV) singletons; digital commerce (PYPL singleton, SHOP joins broad ETFs). The "payments" framing is a sector taxonomy that does not produce a tradable factor. See "Cluster validation" section below.

The 8-name "payments" cohort — card networks (V, MA), card-issuer-network hybrid (AXP), consumer credit (COF), payment processors (FIS, FISV), and digital wallets / commerce platforms (PYPL, SHOP) — does not cluster as one factor. It splits into 4+ sub-factors corresponding to distinct business models.

---

## Constituents and algorithmic clustering

| Sub-cluster | Members | Cluster correlation | Note |
|---|---|---|---|
| Card networks duopoly | V, MA | 0.87 | Cleanest pair in the entire validation pass; same business model (interchange-based two-sided network) |
| Consumer credit / issuer | AXP + COF | (cluster with banks JPM/BAC/WFC at 0.4) | AXP is network+issuer hybrid; COF is bank-issuer; both trade on credit-cycle factor |
| Payment processors | FIS, FISV | Each a singleton | Bank-back-end services; trade on bank IT spending cycle, not network growth |
| Digital wallets / commerce | PYPL (singleton), SHOP (joins broad ETFs) | Idiosyncratic | PYPL on its multi-year reset; SHOP on commerce-growth + general SaaS factor |

The "payments sector" frame groups them by what they do (move money) but the equity returns reflect what they ARE economically.

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/payments.yaml`. Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation (8-name) | 0.40 (range 0.17-0.87) | Far below 0.50 floor; bimodal range |
| V-MA pair | 0.87 | Tightest pair anywhere in the validation pass |
| Tightest cross-business-model pair | AXP-COF = 0.79 | Consumer credit factor (bank-like) |
| PC1 explained variance | 48.4% | Just below the 50% multi-factor floor |
| Hierarchical clustering at 0.4 | V+MA pair; AXP+COF cluster with banks; FIS/FISV/PYPL singletons; SHOP joins broad ETFs | 4 distinct groups |
| Cluster vs banks | 0.35 (+0.05) | Some payments names ARE in the bank factor (AXP, COF) |
| Cluster vs broad ETFs | 0.43 (-0.02 NEGATIVE) | Payments names trade with broad market more than each other |

### Pairwise correlations (1Y)

|  | V | MA | AXP | PYPL | FIS | FISV | COF | SHOP |
|---|---|---|---|---|---|---|---|---|
| V | — | 0.87 | 0.46 | 0.31 | 0.43 | 0.24 | 0.40 | 0.29 |
| MA | 0.87 | — | 0.51 | 0.27 | 0.48 | 0.29 | 0.50 | 0.33 |
| AXP | 0.46 | 0.51 | — | 0.28 | 0.47 | 0.21 | 0.79 | 0.46 |
| PYPL | 0.31 | 0.27 | 0.28 | — | 0.57 | 0.31 | 0.27 | 0.47 |
| FIS | 0.43 | 0.48 | 0.47 | 0.57 | — | 0.45 | 0.40 | 0.41 |
| FISV | 0.24 | 0.29 | 0.21 | 0.31 | 0.45 | — | 0.20 | 0.17 |
| COF | 0.40 | 0.50 | 0.79 | 0.27 | 0.40 | 0.20 | — | 0.42 |
| SHOP | 0.29 | 0.33 | 0.46 | 0.47 | 0.41 | 0.17 | 0.42 | — |

Two correlation peaks dominate the matrix:
- V-MA = 0.87 (network duopoly)
- AXP-COF = 0.79 (consumer credit factor)

Everything else is 0.20-0.50 noise.

---

## What each sub-factor actually trades on

| Sub-factor | Names | Dominant driver |
|---|---|---|
| Card networks | V, MA | Global card spend volume; cross-border travel; interchange fee regulation |
| Consumer credit / issuer | AXP, COF | Credit losses; consumer health; net charge-off rates; FICO migration |
| Bank-back-end processors | FIS, FISV | Bank IT spending cycles; long sales cycles; integration revenue |
| Digital wallets | PYPL | Cross-border + Venmo + Braintree mix; 2024-26 reset story |
| Commerce platforms | SHOP | Merchant GMV growth; Shop Pay adoption; broader SaaS factor |

These are five distinct businesses — the only thing they share is "money moves through them." Equity returns reflect the underlying economics, not the surface taxonomy.

---

## The card networks duopoly — see dedicated note

V-MA pairwise correlation of 0.87 is the tightest pair in the entire validation pass. Now formalized as its own sub-cluster note: see [[Card networks duopoly]] for full validation, structural analysis, and trade implications. The duopoly trades as essentially one stock with ~6% idiosyncratic spread (PC1 explains 93.7% of variance).

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long card networks | V + MA (equal-weighted, intra 0.87) | Global card spend volume + interchange |
| Long consumer credit | AXP + COF (intra 0.79) | Consumer health + credit cycle |
| Long bank IT spending | FIS + FISV (intra 0.45 — looser) | Bank technology spending cycles |
| Long PYPL | Solo | PYPL idiosyncratic reset story |
| Long SHOP | Solo | Commerce platform + general SaaS |
| AVOID: long "payments basket" (8-name) | Dilutes 4-5 unrelated factors | No clean exposure |
| Pair: long V-MA / short AXP-COF | Captures network vs credit-cycle factor differential | Cross-payment-business-model |

---

## Related

### Member actors

- [[Visa]] — card network duopoly
- [[Mastercard]] — card network duopoly
- [[American Express]] — network + issuer hybrid (clusters with banks via consumer credit factor)
- [[Capital One]] — consumer credit issuer (clusters with AXP + banks)
- [[PayPal]] — digital wallet (singleton; multi-year reset)
- [[FIS]] — payment processor (singleton)
- [[Fiserv]] — payment processor (singleton)
- [[Shopify]] — commerce platform (clusters with broad ETFs)

### Adjacent concept notes

- [[Payment waterfall]] — payments-stack technology framework
- [[Mega banks basket]] — AXP and COF cluster with mega banks at 0.4
- [[Banking primer]] — sector hub adjacent to consumer credit

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/payments.yaml` — config for this test

*Created 2026-05-03 — falsified-cluster note documenting the payments sector's 4+ sub-factor structure*
