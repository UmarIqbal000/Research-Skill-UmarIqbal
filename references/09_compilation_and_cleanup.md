# Compilation and Workspace Cleanup Guide

This guide establishes the protocols for compiling LaTeX source code into publication-ready PDFs, generating formatted Word documents, and automatically purging transient build artifacts.

---

## 1. LaTeX Compilation Pipeline

To resolve all cross-references, citations, and table alignments, the build process must follow a standard multi-pass sequence:

### Multi-Pass Execution Sequence:
1. **Pass 1 (Initial parse)**:
   `pdflatex -interaction=nonstopmode -halt-on-error document.tex`
   Generates initial `.aux` and citation index keys.
2. **Pass 2 (Bibliography resolution)**:
   `bibtex document`
   Resolves citations against the companion `.bib` file and produces `.bbl`.
3. **Pass 3 (Cross-reference linking)**:
   `pdflatex -interaction=nonstopmode document.tex`
   Integrates bibliography numbers and updates figure/table numbers.
4. **Pass 4 (Final layout stabilization)**:
   `pdflatex -interaction=nonstopmode document.tex`
   Resolves any lingering page-break shifts or cross-page table splits.

---

## 2. DOCX Generation and Conversion Pipeline

For users requiring Microsoft Word formats:
1. `scripts/docx_generator.py` uses `python-docx` to construct the `.docx` file programmatically from the structured paper data.
2. The script applies professional typography: standard margins (1 inch / 25.4 mm), 11 pt font, styled headings, formatted equations, and clean academic tables.
3. If PDF conversion of the `.docx` is requested, the pipeline invokes `docx2pdf` to output a matching PDF document.

---

## 3. Automated Workspace Cleanup Protocol

LaTeX and word processor compilers generate numerous temporary intermediate files that clutter workspaces and repositories.

### Files Flagged for Automatic Deletion:
The cleanup routine in `scripts/latex_compiler.py` automatically purges:
- `.aux` (Auxiliary cross-reference state)
- `.log` (Compiler execution transcript)
- `.out` (Hyperref bookmark tree)
- `.bbl` (Formatted bibliography cache, after final PDF verification)
- `.blg` (BibTeX log)
- `.toc` (Table of contents cache)
- `.lof` / `.lot` (List of figures and tables)
- `.synctex.gz` (Editor synchronization archive)
- `.fls` (File list log)
- `.fdb_latexmk` (Latexmk build tracker)

### Preserved Artifacts:
- `document.tex` (Pristine master LaTeX source)
- `references.bib` (Complete BibTeX bibliography)
- `figures/` (Vector and preview figure files)
- `document.pdf` (Finished compiled publication PDF)
- `document.docx` (Finished Word document, if requested)
- `presentation.pptx` (Finished conference slides, if requested)

---

## 4. Error Diagnostics and Recovery

If `pdflatex` fails with a non-zero exit code:
1. Read the final 30 lines of `document.log`.
2. Common fixes:
   - *Undefined control sequence*: Check for missing LaTeX packages (e.g., `amsmath`, `booktabs`, `graphicx`, `hyperref`).
   - *Special character unescaped*: Ensure characters like `%`, `_`, `&`, `#` in normal text are properly escaped with backslashes.
   - *Em-dash violation*: Confirm no raw em dashes exist in the source file. Replace with commas, colons, or parentheses.
3. Re-run the compile script to ensure a clean build.
