#concept #healthcare #science

**Medical sciences primer** — foundational biology and drug development concepts for healthcare investing. Understanding the science helps evaluate pipeline risk, competitive moats, and why drugs fail.

> **Key insight:** Drug development is hard because biology is complex. 90% of drugs that enter clinical trials fail. The survivors command premium valuations for a reason.

## Central dogma of biology

The fundamental flow of genetic information:

```
DNA → RNA → Protein → Function
     (transcription) (translation)
```

| Component | What it is | Drug targets |
|-----------|------------|--------------|
| **DNA** | Genetic blueprint, in nucleus | Gene therapy, CRISPR |
| **RNA** | Instructions copied from DNA | mRNA vaccines, siRNA, ASOs |
| **Proteins** | Molecular machines that do work | Small molecules, antibodies |

**Why this matters:** Most drugs target proteins. Newer modalities (mRNA, gene therapy) intervene earlier in the chain.

## Drug modalities

Different ways to intervene in disease:

### Small molecules

Traditional pills/capsules. Chemically synthesized.

| Property | Value |
|----------|-------|
| Size | <1,000 daltons |
| Administration | Usually oral |
| Manufacturing | Chemical synthesis (cheap) |
| Examples | Aspirin, statins, Keytruda |

**Advantages:** Oral dosing, cheap to make, can enter cells
**Disadvantages:** Off-target effects, limited to "druggable" targets (~20% of proteins)

### Biologics (large molecules)

Proteins made in living cells. Includes antibodies.

| Property | Value |
|----------|-------|
| Size | 150,000+ daltons |
| Administration | Injection/infusion |
| Manufacturing | Cell culture (expensive) |
| Examples | Humira, Keytruda, insulin |

**Antibodies (mAbs):** Y-shaped proteins that bind specific targets. Monoclonal = identical copies.

**Advantages:** Highly specific, can hit "undruggable" targets
**Disadvantages:** Can't enter cells, expensive, injection only

### mRNA

Instructions that tell cells to make proteins temporarily.

| Property | Value |
|----------|-------|
| Mechanism | Cell makes the protein drug |
| Duration | Days to weeks |
| Examples | COVID vaccines (Pfizer, Moderna) |

**Advantages:** Fast to design, body makes the protein
**Disadvantages:** Delivery challenges, stability, duration limited

See [[Moderna]].

### Gene therapy

Permanently alter DNA to fix or add genes.

| Type | Mechanism | Duration |
|------|-----------|----------|
| Gene replacement | Add working copy of broken gene | Permanent |
| Gene editing (CRISPR) | Cut/modify specific DNA sequences | Permanent |
| Gene silencing | Block expression of harmful gene | Variable |

**Advantages:** Potential cures (one-time treatment)
**Disadvantages:** Safety unknowns, delivery hard, very expensive ($1-3M per treatment)

See [[CRISPR Therapeutics]], [[Vertex]].

### Cell therapy

Use living cells as treatment.

| Type | Mechanism | Examples |
|------|-----------|----------|
| CAR-T | Engineer patient's T-cells to attack cancer | Kymriah, Yescarta |
| Stem cells | Replace damaged tissue | Early stage |

**Advantages:** Living drug that can adapt
**Disadvantages:** Manufacturing nightmare, patient-specific

### Antibody-drug conjugates (ADCs)

Antibody + toxic payload. "Smart bomb" approach.

```
Antibody (targeting) → Linker → Payload (cell-killing)
```

**Advantages:** Delivers toxin directly to cancer cells
**Disadvantages:** Complex manufacturing, linker stability

## Clinical trial phases

The gauntlet every drug must pass:

| Phase | Purpose | Size | Duration | Success rate |
|-------|---------|------|----------|--------------|
| **Preclinical** | Lab/animal testing | — | 2-4 years | — |
| **Phase 1** | Safety, dosing | 20-100 | 1-2 years | ~65% |
| **Phase 2** | Efficacy signal | 100-500 | 2-3 years | ~30% |
| **Phase 3** | Confirm efficacy | 1,000-5,000 | 3-4 years | ~60% |
| **FDA Review** | Regulatory approval | — | 6-12 months | ~85% |

**Cumulative odds:** ~10% of Phase 1 drugs reach approval.

**Phase 2 is the valley of death** — most failures happen here when efficacy doesn't translate from small to larger trials.

### Trial design concepts

| Term | Meaning |
|------|---------|
| **Randomized** | Patients randomly assigned to drug vs control |
| **Double-blind** | Neither patient nor doctor knows assignment |
| **Placebo-controlled** | Control group gets inactive treatment |
| **Endpoint** | What you measure (tumor shrinkage, survival, etc.) |
| **p-value** | Statistical significance (<0.05 = significant) |
| **Hazard ratio** | Risk reduction vs control (<1 = drug is better) |

## Regulatory pathways

### Standard approval

Full clinical trial package. Takes 10-15 years, costs $1-2B.

### Accelerated pathways

| Pathway | Criteria | Benefit |
|---------|----------|---------|
| **Fast Track** | Serious condition, unmet need | More FDA meetings |
| **Breakthrough** | Substantial improvement over existing | Intensive FDA guidance |
| **Accelerated** | Surrogate endpoint acceptable | Earlier approval |
| **Priority Review** | Significant advance | 6 months vs 10 months |

**Accelerated approval risk:** Drug approved on surrogate endpoint, but confirmatory trial may fail (see: Aduhelm controversy).

### Biosimilars

Near-copies of biologics after patent expiry. Not identical (biologics are too complex), but clinically equivalent.

**Why it matters:** Humira biosimilars now competing. Cheaper, but not as cheap as generic small molecules.

## Key biology concepts

### Immune system basics

| Component | Role | Drug relevtic |
|-----------|------|---------------|
| **T-cells** | Kill infected/cancer cells | CAR-T, checkpoint inhibitors |
| **B-cells** | Make antibodies | Autoimmune targets |
| **Macrophages** | Eat debris, present antigens | Cancer immunotherapy |
| **Cytokines** | Signaling molecules | Inflammation targets |

### Cancer biology

| Concept | Meaning | Drug relevtic |
|---------|---------|---------------|
| **Oncogene** | Mutated gene driving growth | Targeted inhibitors |
| **Tumor suppressor** | Broken brake on growth | Harder to drug |
| **PD-1/PD-L1** | Immune checkpoint | Keytruda, Opdivo |
| **HER2** | Growth receptor | Herceptin |
| **KRAS** | "Undruggable" oncogene | Now druggable (Sotorasib) |

### Metabolism

| Concept | Relevance |
|---------|-----------|
| **GLP-1** | Hormone regulating appetite/insulin | Ozempic, Wegovy |
| **Insulin resistance** | Cells don't respond to insulin | Diabetes drugs |
| **Lipid metabolism** | Cholesterol processing | Statins, PCSK9 |

## Why drugs fail

| Reason | Frequency | Example |
|--------|-----------|---------|
| **Lack of efficacy** | ~50% | Worked in mice, not humans |
| **Safety/toxicity** | ~30% | Unexpected side effects |
| **Commercial** | ~10% | Not better than existing drugs |
| **Operational** | ~10% | Trial design, enrollment |

**The translation problem:** Animal models don't predict human response well. This is why Phase 2 (first real human efficacy data) is so risky.

## Valuation implications

| Stage | Typical valuation approach |
|-------|---------------------------|
| Preclinical | Option value, platform |
| Phase 1 | Risk-adjusted NPV, low probability |
| Phase 2 | Binary event, high volatility |
| Phase 3 | Risk-adjusted peak sales |
| Approved | DCF on actual sales |

**Rule of thumb:** Phase 3 data can move stocks 50%+ in either direction. Phase 2 even more volatile.

## Moats in biopharma

| Moat type | Example |
|-----------|---------|
| **Patent protection** | 20 years from filing (less in practice) |
| **Regulatory exclusivity** | Orphan drug (7 years), biologics (12 years) |
| **Manufacturing complexity** | Biologics hard to copy |
| **Clinical data** | Competitors must run own trials |
| **Platform** | mRNA (Moderna), AI (Recursion) |

---

## Related

- [[Healthcare]] — sector overview
- [[Biopharma]] — drug development investing
- [[Life Sciences]] — tools and diagnostics
- [[Moderna]] — mRNA platform
- [[CRISPR Therapeutics]] — gene editing
- [[Vertex]] — gene therapy pioneer
- [[Eli Lilly]] — GLP-1 leader
- [[Novo Nordisk]] — GLP-1 leader
