# Data and Scientific Simulation Engine

This guide governs how the research ecosystem sources, simulates, or derives data and experimental results for the manuscript.

---

## 1. The Three Data Modalities

A research paper requires empirical or numerical evidence. The ecosystem supports three distinct data paths:

### Modality A: User-Provided Data and Experimental Logs
When the user supplies raw data (CSV, JSON, NumPy arrays, log files, or text transcripts):
- **Data Integrity Rule**: Never downsample, drop rows, or fabricate values. The user's data is ground truth.
- **Dimensionality Matching**: If a figure or table requires paired columns or specific targets, ask the user to confirm the mapping rather than guessing.
- **Reporting**: Calculate genuine descriptive statistics: means, medians, standard deviations, confidence intervals, and interquartile ranges.

### Modality B: Built-in Scientific Simulation Engine
When real-world empirical data is unavailable or when theoretical models require validation, execute controlled numerical simulations via `scripts/simulation_engine.py`:
1. **Monte Carlo Stochastic Convergence**:
   - Evaluate asymptotic convergence rates, variance reduction, and random walk dynamics across 100 to 10,000 trials.
2. **Dynamical Systems and Differential Equations**:
   - Simulate coupled non-linear ODEs or PDEs (e.g., epidemic diffusion, population dynamics, chemical kinetics, circuit transient response).
3. **Multi-Agent and Distributed Systems**:
   - Simulate decentralized consensus, Byzantine fault tolerance, message delay distributions, and peer-to-peer packet drops.
4. **Machine Learning Benchmarking**:
   - Generate realistic optimization trajectories, synthetic loss curves with calibrated noise, learning rate decay schedules, and ablation metrics across model variants.

### Modality C: Literature-Derived Baseline Extraction
When comparing against published state-of-the-art baselines:
- Extract published metric values (e.g., Accuracy, F1-score, Latency, Throughput, FLOPs) directly from cited prior papers.
- Always attribute baseline scores to their exact source citation (e.g., "Baseline metrics for Model X are sourced from [12], evaluated under identical test conditions").
- Never guess or modify a published baseline result.

---

## 2. Statistical Rigor Protocol

For all experimental reporting:
1. **Multi-Seed Execution**:
   Always report results averaged over at least 3 to 5 independent runs or random seeds.
2. **Error Bars and Uncertainty**:
   Report uncertainty as `Mean +/- Standard Deviation` or with 95% confidence interval brackets.
3. **Significance Testing**:
   When claiming that Method A outperforms Method B, execute a paired t-test or Wilcoxon signed-rank test and report the p-value (e.g., `p < 0.01`).
4. **No Cherry-Picking**:
   Report failure modes or regimes where the proposed method does not provide an advantage. Reviewers appreciate transparent discussions of limitations.

---

## 3. Formatting Data Tables

Follow minimal-ink principles (LaTeX `booktabs`):
- Use only three horizontal lines: `\toprule`, `\midrule`, and `\bottomrule`.
- Never use vertical grid lines in academic tables.
- Bold the top-performing value in each column; underline the second-best performer.
- Include a descriptive caption above the table explaining all abbreviations and units.

---

## 4. Universal Style Note

Never use em dashes in table notes, descriptions, or simulation narratives. Use parentheses, colons, or commas.
