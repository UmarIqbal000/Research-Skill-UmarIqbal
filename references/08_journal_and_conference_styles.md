# Journal and Conference Formatting Styles Guide

This guide specifies formatting rules, LaTeX classes, column arrangements, and citation conventions across the major academic publishing bodies.

---

## 1. Overview of Publishing Formats

| Venue Family | LaTeX Class / Engine | Column Layout | Citation Style | Section Numbering | Best For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **IEEE** | `\documentclass[journal]{IEEEtran}` | Two-column | Numeric `[1]` | Roman numerals (I, II, III) | Electrical engineering, telecommunications, robotics, computer systems |
| **ACM** | `\documentclass[sigconf]{acmart}` | Two-column | Numeric `[1]` | Arabic numbers (1, 1.1) | Computer science conferences, software engineering, human-computer interaction |
| **Springer** | `\documentclass{llncs}` | Single-column | Numeric `[1]` | Arabic numbers (1, 1.1) | Lecture Notes in Computer Science, European AI conferences |
| **Elsevier** | `\documentclass[5p,twocolumn]{elsarticle}` | Two-column (or 1-col) | Numeric `[1]` or Author-Year | Arabic numbers (1., 1.1.) | Materials science, physics, chemical engineering, biomedical informatics |
| **Nature / Science** | `\documentclass{article}` | Single-column | Superscript numbers `^1` | Unnumbered bold headings | Cross-disciplinary breakthroughs, biology, physical sciences |
| **NeurIPS / ML** | `\documentclass{article}` with `neurips_style.sty` | Single-column (wide) | Author-Year `(Smith, 2024)` | Arabic numbers (1, 1.1) | Machine learning, deep learning, computational statistics |
| **APA 7th Edition** | `\documentclass{article}` | Single-column | Author-Year `(Smith, 2024)` | Unnumbered descriptive headings | Social sciences, psychology, applied management, education |

---

## 2. Style-Specific Implementation Rules

### IEEE Format (`IEEEtran`)
- **Structure**: Title, authors with affiliations in an author block, Abstract, Index Terms (keywords).
- **Section Headers**: Use `\section{Introduction}`, which automatically compiles to Roman numerals (e.g., `I. INTRODUCTION`).
- **Equations**: Number sequentially on the right margin `(1)`. Refer to them in prose as `(1)` without the word "Eq." unless starting a sentence.
- **Figures & Tables**: Single-column figures use `\begin{figure}`, span two columns using `\begin{figure*}`. Captions go below figures and above tables.

### ACM Format (`acmart`)
- **Preamble**: Requires `\acmConference`, `\acmYear`, `\acmDOI`.
- **CCS Concepts**: Generate and include formal ACM Computing Classification System XML blocks.
- **Keywords**: Provide comma-separated keywords immediately after the abstract.

### Springer LNCS (`llncs`)
- **Structure**: Single-column with generous margins.
- **Headings**: Run-in headings for subsubsections.
- **Bibliography**: Uses `splncs04.bst` for references.

### Elsevier Format (`elsarticle`)
- **Frontmatter**: Encapsulate title, authors, affiliations, abstract, and keywords within the `\begin{frontmatter} ... \end{frontmatter}` environment.
- **Affiliations**: Linked to authors via numeric or letter superscripts (`\address[1]{...}`).
- **Highlights**: Provide 3 to 5 bullet points summarizing findings prior to the abstract if required.

### Nature & Science Formats
- **Opening Summary**: The abstract is an unreferenced 150-word paragraph directly continuing into the main text without an "Abstract" header.
- **Headings**: Minimal use of section headers. Subheadings are short, bold, and unnumbered.
- **Methods Section**: Main body focuses on narrative discovery and evidence. Detailed technical methods appear in an end-matter "Methods" section.
- **Citations**: Placed as superscripts after punctuation (e.g., `...prior observations.^1,2`).

### NeurIPS / ICML / ICLR Format
- **Layout**: Clean single-column layout with 0.5-inch margins and clear line numbers for double-blind peer review.
- **Theorems**: Formal theorem, lemma, proposition environments with distinct numbering.
- **Checklist**: Concludes with the mandatory reproducibility and ethics checklist.

---

## 3. DOCX and PDF Output Requirements

When generating Microsoft Word (`.docx`) documents:
- Use consistent styles: `Title` (24pt bold), `Heading 1` (16pt bold), `Heading 2` (13pt bold), `Normal` (11pt Times New Roman or Calibri, 1.15 line spacing).
- Format tables with top and bottom borders and a light header separator; omit vertical lines.
- Convert `.docx` to PDF cleanly without disrupting table alignments or figure placements.

---

## 4. Universal Typography Directive

Never use em dashes in any journal style template. Replace with colons, parentheses, commas, or separate sentences.
