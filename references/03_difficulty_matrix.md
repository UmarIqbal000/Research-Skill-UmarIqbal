# Research Difficulty Matrix and Progression Guide

This guide establishes the specifications for the four difficulty tiers: Easy, Medium, Hard, and Extreme. The tier dictates the mathematical density, theoretical depth, experimental requirements, and analytical rigor of the manuscript.

---

## 1. Summary Comparison Rubric

| Feature Dimension | Tier 1: Easy | Tier 2: Medium | Tier 3: Hard | Tier 4: Extreme |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Goal** | High accessibility, conceptual clarity, practical implementation | Peer-reviewed publication in standard journals and conferences | Top-tier venue acceptance (NeurIPS, ICML, CVPR, IEEE TPAMI) | Groundbreaking landmark discovery (Nature, Science, STOC/FOCS) |
| **Mathematical Depth** | Basic algebra, intuitive formulas, plain-text explanations | Formal problem definition, objective functions, optimization steps | Formal Theorems, Lemmas, propositions, convergence bounds | Novel mathematical framework, full proofs from first principles |
| **Theoretical Rigor** | Conceptual motivation and logical explanation | Formalization of problem setup and algorithmic complexity | Formal asymptotic analysis, generalization or stability guarantees | Lower and upper bounds, min-max optimality, complete technical appendix |
| **Empirical Scope** | 1 to 2 benchmark comparisons or representative case studies | 3 to 5 standard baselines across recognized datasets | Comprehensive SOTA baselines, multi-seed statistical significance | Frontier-scale simulation or exhaustive empirical validation across regimes |
| **Ablation Studies** | Basic component check | Component-by-component isolation with percentage gains | Multi-dimensional sensitivity, parameter sweeps, stress tests | Cross-domain stress testing, failure-mode mapping, Pareto frontiers |
| **Target Readership** | Students, practitioners, cross-disciplinary engineers | Academic researchers, regular conference reviewers | Domain experts, senior program committees | World-leading scientific authorities, editors-in-chief |

---

## 2. Tier Specifications in Detail

### Tier 1: Easy (Foundational / Pedagogical)
- **Philosophy**: Remove all barriers to entry. The reader must understand the problem, the solution, and the results on the first read.
- **Mathematical Formulations**:
  - Keep notation minimal and intuitive. Avoid stacked indices or excessive tensor notation.
  - Every equation must be accompanied by an immediate sentence translating each symbol into physical or intuitive terms.
  - Example: State a loss function as a clear sum of prediction error and a regularizer penalty with an explicit explanation of what the penalty balances.
- **Visuals**:
  - Clear workflow block diagram showing inputs moving to outputs.
  - Bar charts and line plots with large, readable fonts and obvious trends.
- **Language**:
  - Direct, conversational scholarly prose. Clear analogies and practical examples.

### Tier 2: Medium (Standard Peer-Reviewed)
- **Philosophy**: Produce a competitive submission meeting the standards of IEEE Transactions, ACM SIG, Elsevier, or Springer conferences.
- **Mathematical Formulations**:
  - Rigorous definitions of state spaces, parameter vectors, and objective functions.
  - Explicit algorithmic presentation using formal algorithmic environments (Input, Output, Step-by-step loop).
  - Standard complexity calculations: Big-O time and space complexity.
- **Empirical Rigor**:
  - Comparison against 3 to 5 established baselines.
  - Error bars, standard deviations across 3 to 5 random seeds, and confidence intervals.
  - Standard ablation table showing the impact of removing individual components.
- **Language**:
  - Strict scholarly register. Every claim is tied to a specific table, figure, or citation.

### Tier 3: Hard (Advanced Rigorous / Premier Conference)
- **Philosophy**: Match the theoretical and empirical expectations of flagship venues (NeurIPS, ICML, ICLR, CVPR, IEEE TPAMI).
- **Mathematical Formulations**:
  - Formal mathematical structure: Definition, Assumption, Lemma, Theorem, Proof sketch, Corollary.
  - Rigorous theoretical derivation: Convergence rates, sample complexity, Lyapunov stability, or PAC-Bayesian generalization bounds.
  - Complete asymptotic complexity analysis including constants where relevant.
- **Empirical Rigor**:
  - Testing on standard high-difficulty benchmarks.
  - Multi-seed runs with paired statistical significance tests (e.g., p < 0.01).
  - Exhaustive ablation sweeps over hyperparameter grids, noise levels, and distribution shifts.
- **Language**:
  - Analytical and exact. Clear differentiation between proven theorems and empirical observations.

### Tier 4: Extreme (Breakthrough Landmark)
- **Philosophy**: Formulate a paper of enduring historical significance, targeting Nature, Science, PNAS, or foundational theoretical theory conferences.
- **Mathematical Formulations**:
  - Introduction of novel mathematical paradigms or theoretical formulations resolving long-standing bottlenecks.
  - Complete, unassailable proofs provided in a dedicated Mathematical Appendix.
  - Proofs establishing both lower bounds (fundamental limits) and matching upper bounds (optimal algorithms).
- **Empirical Rigor**:
  - Massive-scale simulations spanning several orders of magnitude across physical or computational regimes.
  - Demonstration of Pareto-optimal frontiers that strictly dominate existing paradigms.
  - Robustness across pathological edge cases, severe noise, and adversarial environments.
- **Language**:
  - Authoritative, profound, yet lucid. The opening summary and introduction must be understandable to any trained scientist, while the theoretical core remains uncompromisingly rigorous.

---

## 3. Universal Rule Across All Tiers

Regardless of whether the paper is Easy or Extreme, **no em dashes may be used**. Structure sentences with commas, colons, parentheses, or separate concise statements.
