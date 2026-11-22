# Topic and Trend Discovery Guide

This guide governs how the research ecosystem discovers trending research vectors, explores emerging frontiers across disciplines, and refines a user's initial idea into a concrete research direction.

---

## 1. Discovery Modes

The framework supports three input modalities:

1. **User-Specified Topic or Question**:
   - The user provides an exact question, title, or hypothesis (e.g., *"Investigate communication overhead in decentralized federated learning with Byzantine workers"*).
   - Action: Directly scope the topic, identify keyword variations, and proceed to literature synthesis and gap analysis.

2. **Broad Field or Domain Specification**:
   - The user names a broad discipline (e.g., *"Reinforcement Learning"*, *"Bioinformatics"*, *"Photovoltaic Materials"*, *"Smart Grid Cybersecurity"*).
   - Action: Execute active trend analysis via arXiv and scholarly databases to surface high-velocity topics published in the last 6 to 18 months. Identify high-potential sub-problems.

3. **Autonomous Trend Scouting (Open Exploration)**:
   - The user asks: *"What is currently trending in AI/science?"* or *"Find an impactful research topic for me"*.
   - Action: Query trending preprints and cross-reference high-citation growth clusters across the primary discovery taxonomy:
     - Machine Learning & Agentic Systems (`cs.AI`, `cs.LG`, `cs.CL`)
     - Computer Vision & Multimodal Perception (`cs.CV`)
     - Quantum Computing & Information Physics (`quant-ph`)
     - Computational Biology & Genomics (`q-bio.BM`, `q-bio.GN`)
     - Robotics & Autonomous Systems (`cs.RO`)
     - Cybersecurity & Cryptography (`cs.CR`)
     - Clean Energy & Materials Informatics (`cond-mat.mtrl-sci`)

---

## 2. Topic Qualification Criteria

Before advancing a discovered topic into the manuscript pipeline, verify four qualification filters:

1. **Analytical Tractability**:
   Can the central research question be evaluated rigorously through empirical simulation, benchmark datasets, or mathematical derivation?
2. **Defensible Novelty**:
   Is the problem sufficiently distinct from settled baselines? Avoid saturated trivial extensions (e.g., standard benchmarking of an existing model on a standard dataset without algorithmic or theoretical innovation).
3. **Reproducibility & Scope**:
   Does the topic allow clear parameter definition, ablation studies, and meaningful comparative plots?
4. **Scholarly Audience Value**:
   Does the solution address a demonstrable bottleneck (e.g., convergence speed, sample efficiency, memory footprint, robustness, or accuracy)?

---

## 3. Query Generation Strategy

When searching arXiv or scholarly indices via `scripts/topic_discovery.py`, generate tiered keyword queries:

- **Broad Core**: Primary domain terms (e.g., `"Federated Learning"`, `"Edge Computing"`).
- **Bottleneck Modifier**: Specific challenges (e.g., `"Byzantine fault tolerance"`, `"communication efficiency"`, `"non-IID distribution"`).
- **Methodological Target**: Algorithmic or structural mechanisms (e.g., `"quantization"`, `"differential privacy"`, `"consensus protocols"`).

Synthesize queries using boolean operators:
`("Federated Learning" OR "Decentralized Learning") AND ("Communication Efficient" OR "Bandwidth Constrained") AND ("Non-IID" OR "Heterogeneous")`

---

## 4. Topic Brief Output Contract

Present the topic to the user or pipeline in a structured Topic Brief:

```markdown
### Research Topic Brief
- Working Title: [Concise, informative title without buzzwords]
- Target Domain: [e.g., Distributed Machine Learning / Network Systems]
- Core Problem Statement: [2-3 sentences explaining the exact bottleneck]
- Primary Motivation: [Why this problem matters now and who benefits]
- Proposed Methodological Angle: [High-level technical approach]
- Intended Difficulty Tier: [Easy / Medium / Hard / Extreme]
```
