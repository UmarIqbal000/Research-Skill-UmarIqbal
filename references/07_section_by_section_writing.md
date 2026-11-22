# Section-by-Section Manuscript Drafting Guide

This guide provides precise drafting instructions for each section of a research paper, ensuring structural coherence, logical flow, and reviewer-friendly presentation.

---

## 1. Title and Abstract

### Title
- Keep the title specific, concise, and declarative.
- Mention the core mechanism and the target problem directly.
- Avoid vague buzzwords like "A Novel Approach for..." or "Towards Next-Generation...".
- **Rule**: Never use em dashes or hyphens acting as dashes in titles.

### Abstract (150 to 250 words)
Follow the 5-sentence formula:
1. **Context & Motivation** (1 sentence): State the domain and why the broad problem is significant.
2. **The Specific Bottleneck / Gap** (1 sentence): State the precise limitation of existing techniques.
3. **Proposed Method & Insight** (1-2 sentences): Introduce the method and explain the core mechanism that overcomes the limitation.
4. **Key Quantitative Result** (1-2 sentences): Present concrete numbers comparing against the strongest baseline (e.g., "improves accuracy by 5.4% while reducing communication costs by 42%").
5. **Broader Significance** (1 sentence): State what this capability unlocks for the field.

---

## 2. Introduction

The introduction must establish the paper's thesis within the first three paragraphs:

### Paragraph 1: The Hook and Scientific Context
- Open with the foundational problem. Establish the real-world or theoretical necessity.
- Do not use formulaic openers like "In recent years, X has attracted increasing attention." Open with the core operational requirement.

### Paragraph 2: The Bottleneck and Failure of Prior Art
- Explain why the problem remains challenging.
- Group prior approaches into 1 or 2 conceptual categories and pinpoint where their assumptions break down.

### Paragraph 3: The Core Technical Insight
- Introduce the proposed approach.
- State the physical, mathematical, or algorithmic insight that makes this approach succeed where baselines fail.

### Paragraph 4: Teaser / Overview Figure Callout
- Reference Figure 1 (the system diagram or teaser plot) to provide visual intuition for the concept before technical equations appear.

### Paragraph 5: Explicit Contribution List
Use a crisp, numbered list where each item names a specific, verifiable outcome:
- We formulate [Method Name], a principled framework that addresses [specific limitation].
- We establish theoretical convergence guarantees, proving that [Theorem outcome] holds under [conditions].
- We conduct extensive empirical evaluations across [N] benchmark datasets, achieving a [X]% performance improvement over state-of-the-art baselines.

---

## 3. Related Work

- Structure related work by **thematic categories**, not as an unorganized chronological list.
- For each category:
  1. Summarize the general strategy employed by those works.
  2. Acknowledge their strengths.
  3. Clearly articulate the distinction and advance of the proposed work.
- Avoid citation dumping (e.g., avoid "Many methods exist [1-12]"). Cite specific representative papers and explain how your approach diverges.

---

## 4. Problem Formulation and Mathematical Framework

1. **Notation Table**: Define symbols, tensor ranks, index sets, and mathematical spaces before writing equations.
2. **System Model**: Formally state the input domain, output space, and governing physical or operational assumptions.
3. **Objective Function**: Explicitly write the optimization target or loss formulation. State whether the objective is convex, non-convex, constrained, or unconstrained.
4. **Intuition First**: Follow every major equation with a brief sentence explaining what it computes in intuitive terms.

---

## 5. Proposed Methodology

1. **High-Level Architectural Overview**: Walk the reader through the pipeline from raw input to finished output.
2. **Component-by-Component Formulation**: Dedicate a subsection to each key algorithmic module.
3. **Formal Algorithm Block**: Include a structured algorithm block (Algorithm 1) specifying:
   - Input parameters and hyperparameters.
   - Initialization states.
   - Step-by-step update loop.
   - Output artifacts and return values.
4. **Theoretical Properties**: Present any formal Lemmas, Theorems, or Propositions establishing stability, convergence rates, or complexity.

---

## 6. Experimental Evaluation

Structure the evaluation around 3 to 4 specific research questions:
- *RQ1 (Overall Performance)*: Does the proposed method outperform state-of-the-art baselines on standard metrics?
- *RQ2 (Ablation Analysis)*: How much does each individual component contribute to the overall performance?
- *RQ3 (Sensitivity & Robustness)*: How does the method perform under hyperparameter variations, distribution shifts, or extreme conditions?
- *RQ4 (Computational Efficiency)*: What is the training time, memory footprint, or communication cost compared to alternatives?

For each table and figure:
- Provide an informative caption explaining the metrics and experimental setup.
- Highlight the best results in bold.
- Explicitly discuss the data in the body text: lead with comparisons against the strongest competitor rather than trivial baselines.

---

## 7. Discussion and Limitations

- Dedicate an explicit subsection to honest limitations:
  - Scenarios or edge cases where the method degrades.
  - Computational or memory dependencies.
  - Open theoretical questions left for future exploration.
- Reviewers strongly respect transparent self-critique; it demonstrates scholarly maturity.

---

## 8. Conclusion

- Provide a concise summary of the core findings without repeating the abstract verbatim.
- Reiterate the primary advance and outline promising directions for future inquiry.

---

## 9. Universal Formatting Constraint

**No em dashes permitted**: Enforce this constraint continuously across all written sections.
