---
aliases: [Hierarchical Risk Parity, HRP]
tags: [concept, portfolio-construction, risk, clustering]
---

# Hierarchical Risk Parity

Hierarchical Risk Parity (HRP) is a portfolio-construction method that uses hierarchical clustering of the correlation matrix to allocate risk, avoiding the covariance-matrix inversion that makes [[Equal Risk Contribution]] and [[Mean-variance optimization|mean-variance optimization]] unstable. It was introduced by Marcos López de Prado (2016).

*Chart not applicable: Hierarchical Risk Parity is a portfolio-construction method, not a tradeable instrument or price series.*

---

## The problem it solves

Optimization-based methods — mean-variance, and the optimizer behind [[Equal Risk Contribution]] — invert the covariance matrix. That inversion is fragile:

- Small estimation errors in the covariances produce large, unstable weight swings.
- Near-singular matrices (highly correlated assets, short history) are ill-conditioned.
- Results often concentrate in a few extreme positions.

HRP sidesteps inversion entirely, trading theoretical optimality for robustness.

## The three steps

### 1. Tree clustering

Convert correlations to distances and cluster:

$$d_{ij} = \sqrt{0.5\,(1 - \rho_{ij})}$$

Hierarchical clustering on this distance produces a dendrogram — the asset similarity structure. Correlated assets (two equity sleeves, two bond sleeves) join at small distances; genuine diversifiers join far out.

### 2. Quasi-diagonalization

Reorder the covariance matrix using the dendrogram leaf order so similar assets sit adjacent and the largest correlations gather into diagonal blocks. No numbers change — only the ordering — but the matrix becomes block-structured.

### 3. Recursive bisection

Allocate top-down through the tree: split into two clusters, divide risk between them by inverse cluster variance, then recurse inside each cluster until single assets remain. Lower-variance branches receive more weight at each split.

## Versus the optimization methods

| Aspect | Mean-variance / ERC | HRP |
|--------|---------------------|-----|
| Matrix inversion | Required | None |
| Estimation-error sensitivity | High | Low |
| Stability / turnover | Lower / higher | Higher / lower |
| Theoretical foundation | Strong | Heuristic |
| Many assets, short history | Degrades | Holds up |

HRP does not guarantee true equal risk contribution — it is a heuristic, sensitive to the clustering linkage choice — but it stays feasible even with singular matrices and scales to large universes. Use [[Equal Risk Contribution]] when theoretical purity matters; HRP when robustness and asset count do.

## Variants

- HERC (Hierarchical Equal Risk Contribution): apply [[Equal Risk Contribution]] within each cluster instead of inverse variance.
- NCO (Nested Clustering Optimization): optimize within clusters, HRP between them.
- Alternative distance metrics: mutual information, tail dependence, dynamic conditional correlation.

## Connection to the vault's cluster validation

The first HRP step — correlation-distance hierarchical clustering, $d=\sqrt{0.5(1-\rho)}$, read off a dendrogram — is the same machinery the vault's own cluster-validation framework uses to test whether a peer cohort is real. The cohort dendrograms, join-distance topology, and correlation-distance metric throughout the vault's cluster work are HRP's tree-clustering step repurposed: López de Prado built it to allocate risk; the vault uses it to answer "where does this name actually trade." Same distance, same linkage family, different question.

## Related

- [[Equal Risk Contribution]] — the optimization-based target HRP approximates without matrix inversion
- [[Risk Budgeting]] — the broader allocate-by-risk framework
- [[Risk Parity]] — parent strategy; the vault's cluster-validation methodology reuses HRP's clustering step
- [[Stock-Bond Correlation Regime]] — the correlations HRP clusters on are regime-dependent
