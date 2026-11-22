"""
LaTeX Compilation and Automated Cleanup Engine
Executes multi-pass pdflatex/bibtex builds to generate publication PDFs,
diagnoses compilation errors, and purges transient build artifacts.
"""

import os
import sys
import shutil
import subprocess
from typing import Dict, Any, List


# Extensions to clean up after successful build
CLEANUP_EXTENSIONS = [
    ".aux", ".log", ".out", ".bbl", ".blg", ".toc",
    ".lof", ".lot", ".synctex.gz", ".fls", ".fdb_latexmk"
]


def find_pdflatex() -> str:
    """Locate pdflatex executable in system PATH or common MiKTeX/TeX Live paths."""
    pdflatex = shutil.which("pdflatex")
    if pdflatex:
        return pdflatex
        
    candidates = [
        r"C:\Users\umari\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe",
        r"C:\Program Files\MiKTeX\miktex\bin\x64\pdflatex.exe",
        r"C:\texlive\2024\bin\windows\pdflatex.exe"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return "pdflatex"


def find_bibtex() -> str:
    """Locate bibtex executable."""
    bibtex = shutil.which("bibtex")
    if bibtex:
        return bibtex
    candidates = [
        r"C:\Users\umari\AppData\Local\Programs\MiKTeX\miktex\bin\x64\bibtex.exe",
        r"C:\Program Files\MiKTeX\miktex\bin\x64\bibtex.exe"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return "bibtex"


def cleanup_artifacts(directory: str, base_name: str) -> List[str]:
    """Purge temporary auxiliary files while preserving master source and PDF."""
    removed = []
    for ext in CLEANUP_EXTENSIONS:
        target = os.path.join(directory, f"{base_name}{ext}")
        if os.path.exists(target):
            try:
                os.remove(target)
                removed.append(f"{base_name}{ext}")
            except Exception:
                pass
    return removed


def compile_latex(
    tex_path: str,
    run_bibtex: bool = True,
    auto_cleanup: bool = True
) -> Dict[str, Any]:
    """
    Compile a LaTeX file into PDF using a 4-pass pipeline and clean up artifacts.
    """
    tex_path = os.path.abspath(tex_path)
    if not os.path.exists(tex_path):
        return {"success": False, "error": f"File not found: {tex_path}"}
        
    work_dir = os.path.dirname(tex_path)
    base_name = os.path.splitext(os.path.basename(tex_path))[0]
    pdf_path = os.path.join(work_dir, f"{base_name}.pdf")
    
    pdflatex = find_pdflatex()
    bibtex = find_bibtex()
    
    log_file = os.path.join(work_dir, f"{base_name}.log")
    
    # Pre-clean prior failed auxiliary files so Pass 1 doesn't read stale/empty .bbl
    for ext in [".aux", ".bbl", ".blg", ".out", ".log"]:
        stale = os.path.join(work_dir, f"{base_name}{ext}")
        if os.path.exists(stale):
            try:
                os.remove(stale)
            except Exception:
                pass

    # Pass 1: Initial pdflatex
    cmd1 = [pdflatex, "-interaction=nonstopmode", "-halt-on-error", f"{base_name}.tex"]
    p1 = subprocess.run(cmd1, cwd=work_dir, capture_output=True, text=True)
    if p1.returncode != 0:
        return {
            "success": False,
            "error": "Pass 1 (initial pdflatex) failed",
            "log": p1.stdout[-1500:] if p1.stdout else p1.stderr
        }
        
    # Pass 2: BibTeX (if requested)
    if run_bibtex:
        bib_file = os.path.join(work_dir, f"{base_name}.bib")
        aux_file = os.path.join(work_dir, f"{base_name}.aux")
        if os.path.exists(bib_file) or os.path.exists(aux_file):
            subprocess.run([bibtex, base_name], cwd=work_dir, capture_output=True, text=True)
            
    # Pass 3: Cross-reference resolution
    subprocess.run(cmd1, cwd=work_dir, capture_output=True, text=True)
    
    # Pass 4: Final layout stabilization
    p4 = subprocess.run(cmd1, cwd=work_dir, capture_output=True, text=True)
    
    if not os.path.exists(pdf_path):
        return {
            "success": False,
            "error": "PDF generation failed: Output file was not created.",
            "log": p4.stdout[-1500:] if p4.stdout else p4.stderr
        }
        
    # Automatic Cleanup
    removed_files = []
    if auto_cleanup:
        removed_files = cleanup_artifacts(work_dir, base_name)
        
    pdf_size_kb = round(os.path.getsize(pdf_path) / 1024, 1)
    
    return {
        "success": True,
        "pdf_path": pdf_path,
        "size_kb": pdf_size_kb,
        "cleaned_artifacts": removed_files,
        "message": f"Successfully compiled {base_name}.pdf ({pdf_size_kb} KB) with clean workspace."
    }


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(f"Compiling: {target}")
        result = compile_latex(target)
        print(result)
    else:
        print("LaTeX Compiler Engine ready. pdflatex located at:", find_pdflatex())
