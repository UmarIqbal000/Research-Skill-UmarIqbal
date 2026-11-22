---
name: research-skill-umariqbal
description: Complete academic research paper ecosystem. Generates publication-grade research papers, identifies research gaps, runs scientific simulations or parses experimental data, produces publication figures (Nature/IEEE palettes, 300+ DPI & vector PDF), marks difficulty across 4 tiers (easy, medium, hard, extreme), humanizes prose to eliminate AI detection, strictly prohibits em dashes, compiles clean LaTeX/DOCX/PDF manuscripts with workspace cleanup, and generates academic conference presentation decks (PPTX). Use whenever the user asks to write, research, draft, or polish an academic paper, explore research trends, conduct gap analysis, generate scientific figures, or build conference slides.
---

# Research Paper Ecosystem: Master Skill Guide

Welcome to **Research-Skill-UmarIqbal**, a comprehensive research ecosystem designed to transform concepts, research fields, raw data, or literature surveys into publication-ready manuscripts, scientific figures, and conference presentations.

---

## 1. Quick Navigation and Progressive Disclosure

Load only the specific reference modules required for the active stage:

| Stage | Focus Area | Detailed Reference File |
| :--- | :--- | :--- |
| **Stage 1** | Topic discovery, trending vectors, arXiv search | [01_topic_and_trend_discovery.md](references/01_topic_and_trend_discovery.md) |
| **Stage 2** | SOTA matrix, prior art check, research gap analysis | [02_novelty_and_gap_analysis.md](references/02_novelty_and_gap_analysis.md) |
| **Stage 3** | Difficulty tier calibration (Easy, Medium, Hard, Extreme) | [03_difficulty_matrix.md](references/03_difficulty_matrix.md) |
| **Stage 4** | Numerical simulation, user data ingestion, benchmarks | [04_data_and_simulation_engine.md](references/04_data_and_simulation_engine.md) |
| **Stage 5** | Publication-grade plots, architecture schematics, vector PDF | [05_academic_figures_and_plots.md](references/05_academic_figures_and_plots.md) |
| **Stage 6** | Academic humanizer, zero AI tells, **NO EM DASHES** | [06_humanizer_and_no_emdash_rule.md](references/06_humanizer_and_no_emdash_rule.md) |
| **Stage 7** | Section-by-section writing (Abstract, Intro, Method, Eval) | [07_section_by_section_writing.md](references/07_section_by_section_writing.md) |
| **Stage 8** | Journal formatting (IEEE, ACM, Springer, Elsevier, Nature, APA) | [08_journal_and_conference_styles.md](references/08_journal_and_conference_styles.md) |
| **Stage 9** | LaTeX/DOCX compilation to PDF and artifact cleanup | [09_compilation_and_cleanup.md](references/09_compilation_and_cleanup.md) |
| **Stage 10** | Academic conference slide deck generation (16:9 PPTX) | [10_academic_pptx_presentations.md](references/10_academic_pptx_presentations.md) |
| **Stage 11** | Lucid rigor and accessible scholarly language | [11_accessible_scholarly_language.md](references/11_accessible_scholarly_language.md) |

---

## 2. Core Execution Workflow

Follow this closed-loop sequence whenever conducting a research task:

```
User Prompt (Topic, Question, Field, or Data)
     │
     ▼
[Stage 1] Ingest or Discover Topic ──► Query arXiv / Literature / Frontier Catalog
     │
     ▼
[Stage 2] Prior Art & Gap Verification ──► Construct SOTA Matrix & Verify Novelty Gate
     │
     ▼
[Stage 3] Confirm Difficulty Tier ──► Easy / Medium / Hard / Extreme
     │
     ▼
[Stage 4] Execute Simulation or Ingest Data ──► Monte Carlo / Dynamics / User CSV
     │
     ▼
[Stage 5] Render Publication Figures ──► 300 DPI PNG + Vector PDF (89mm / 183mm)
     │
     ▼
[Stage 6] Section Drafting & Humanization ──► Purge AI Vocabulary & Enforce NO EM DASHES
     │
     ▼
[Stage 7] Build & Compile Documents ──► LaTeX pdflatex + bibtex OR Academic DOCX
     │
     ▼
[Stage 8] Workspace Cleanup ──► Purge .aux, .log, .out, .bbl, .blg
     │
     ▼
[Stage 9] Optional PPTX Presentation ──► 16:9 Action Titles + 2-Column Exhibits
```

---

## 3. The Four Difficulty Tiers (Quick Summary)

Always calibrate mathematical depth and empirical scope to the requested tier:

- **Easy (Foundational / Pedagogical)**:
  - Intuitive explanations, high school or basic undergraduate algebra.
  - Transparent analogies, zero gatekeeping jargon.
  - Practical demonstration with 1-2 benchmark datasets or qualitative case studies.
- **Medium (Standard Peer-Reviewed)**:
  - High-impact conference/journal caliber (IEEE, ACM, Elsevier, Springer).
  - Formal problem definition, objective functions, pseudo-code algorithm block.
  - 3 to 5 baseline comparisons with standard deviation error bars across multiple seeds.
- **Hard (Advanced Rigorous)**:
  - Flagship venues (NeurIPS, ICML, CVPR, IEEE TPAMI).
  - Formal Theorems, Lemmas, propositions, convergence rates, and asymptotic bounds.
  - Exhaustive ablation sweeps, multi-seed statistical significance (p < 0.01), edge-case stress testing.
- **Extreme (Breakthrough Landmark)**:
  - Nature, Science, STOC/FOCS, Breakthrough level.
  - Novel mathematical paradigm, complete proofs from first principles in a dedicated Technical Appendix.
  - Lower and upper bounds, min-max optimality, large-scale multi-regime simulation.
  - Written with profound authority yet crystal-clear intuition in opening sections.

---

## 4. The Universal Non-Negotiable Directives

1. **STRICT PROHIBITION OF EM DASHES**:
   - Never use `—`, `\textemdash`, `---`, or `--` acting as a dash.
   - Recast with commas, colons, parentheses, semicolons, or separate concise sentences.
   - Run `python scripts/academic_humanizer.py` to audit all drafts.
2. **ACCESSIBLE SCHOLARLY LANGUAGE (LUCID RIGOR)**:
   - Ensure the language is accessible to readers across adjacent fields.
   - Avoid pretentious vocabulary (*delve*, *tapestry*, *pivotal*, *testament*, *underscore*, *intricate*, *multifaceted*, *seamless*).
   - Define intuition before formulas; define every mathematical symbol immediately following the equation.
3. **CLAIM-TO-EVIDENCE DISCIPLINE**:
   - Every empirical claim must name an exact number, table, figure, or citation.
   - Empirical papers *provide evidence* and *show*; they do not *prove* universal truths.
4. **AUTOMATIC WORKSPACE CLEANUP**:
   - Never leave messy intermediate compiler files (`.aux`, `.log`, `.bbl`, `.blg`, `.out`, `.synctex.gz`) in the workspace.
   - Retain only master source files (`.tex`, `.bib`), graphics (`figures/`), final output (`.pdf`, `.docx`), and presentation (`.pptx`).

---

## 5. CLI Execution Recipes

The ecosystem includes a unified command-line interface `cli.py`:

```bash
# 1. Run complete research paper generation (End-to-End)
python cli.py run --topic "Decentralized Edge Intelligence" --difficulty medium --format ieee --output ./outputs/paper_ieee

# 2. Run an easy-tier paper for students and practitioners
python cli.py run --topic "Federated Learning for Healthcare" --difficulty easy --format generic --output ./outputs/paper_easy

# 3. Run an extreme-tier theoretical paper
python cli.py run --topic "Non-Convex Multi-Agent Consensus" --difficulty extreme --format nature --output ./outputs/paper_extreme

# 4. Search arXiv for recent breakthroughs
python cli.py search --query "byzantine federated learning" --limit 5

# 5. Clean and humanize an existing text file
python cli.py humanize --file draft.txt --output cleaned_draft.txt

# 6. Compile LaTeX manuscript to PDF with auto-cleanup
python cli.py compile --tex ./outputs/paper_ieee/manuscript.tex
```
