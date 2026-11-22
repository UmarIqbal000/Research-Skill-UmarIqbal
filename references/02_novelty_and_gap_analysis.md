# Novelty and Gap Analysis Guide

This guide defines the methodology for surveying prior literature, verifying novelty, and pinpointing unaddressed research gaps.

---

## 1. The Core Objective

A research paper must make a distinct, identifiable contribution. To establish this, the agent must determine:
1. What solutions have already been proposed?
2. What are their specific structural, theoretical, or empirical limitations?
3. Exactly what gap remains unaddressed?

If a prior paper has already solved the exact problem under the same conditions, the proposed topic must be pivoted or refined before drafting begins.

---

## 2. Five-Step Prior Art Verification Protocol

### Step 1: Broad Literature Retrieval
Retrieve 10 to 20 recent relevant papers using `scripts/novelty_gap_analyzer.py` or scholarly APIs. Collect:
- Title, authors, venue, publication year.
- Central objective and methodology.
- Reported performance and experimental settings.
- Explicitly stated limitations or future work.

### Step 2: Construct the State-of-the-Art (SOTA) Comparison Matrix
Tabulate the closest 4 to 8 works across consistent technical dimensions:

| Prior Work | Proposed Method | Assumed Conditions | Theoretical Guarantees | Empirical Scalability | Known Failure Mode / Gap |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Paper A (2023) | Primal-dual descent | Convex objectives only | Asymptotic rate O(1/k) | Tested up to 10 nodes | Fails under non-convex losses |
| Paper B (2024) | Gradient compression | Full-mesh topology | Heuristic, no bound | High communication load | Degrades on asynchronous networks |
| Paper C (2025) | Local momentum SGD | Homogeneous devices | Bounded variance assumption | Moderate | High sensitivity to client drift |

### Step 3: Identify the Triple Research Gap
Identify three distinct, concrete failure modes or omissions in existing literature:
1. **Structural/Assumptive Gap**: Prior works rely on unrealistic assumptions (e.g., synchronous clocks, perfectly convex landscapes, zero packet loss, independent noise).
2. **Computational/Efficiency Gap**: Existing methods achieve accuracy only at prohibitive computational or communication costs that prevent real-world scaling.
3. **Generalization/Robustness Gap**: SOTA degrades catastrophically when subjected to distribution shifts, adversarial inputs, or non-stationary dynamics.

### Step 4: Run the Novelty Gatekeeper Check
Answer three adversarial questions:
- *Has this exact mechanism been applied to this exact problem before?* If yes: Reject or pivot.
- *Is the improvement merely a naive hyperparameter sweep or cosmetic wrapper around an existing baseline?* If yes: Elevate the methodological depth.
- *Can the proposed contribution be summarized in one sharp, falsifiable sentence?* If no: Clarify the core mechanism.

### Step 5: Formulate the Contribution Statement
Draft the contributions using precise, active prose:
- "First, we introduce [Mechanism Name], an algorithmic formulation that eliminates [specific assumption]."
- "Second, we establish a theoretical bound demonstrating [rate or property] under [explicit conditions]."
- "Third, we evaluate on [Benchmarks/Simulations], showing a [X]% reduction in [Cost Metric] while matching baseline accuracy."

---

## 3. Negative Guidelines: AI Tells to Avoid

- Do not use hollow claims such as "To the best of our knowledge, we are the first to study X". Instead, explicitly state what prior works did and where they stopped.
- Do not cite lists of 10 papers in a single bracket without differentiation (e.g., avoid `[1-10]`). Contrast specific works directly.
- **Strict Grammar Directive**: Never use em dashes anywhere in the analysis. Use colons, parentheses, commas, or semicolons instead.
