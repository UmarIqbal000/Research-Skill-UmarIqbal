#!/usr/bin/env python3
"""
Research-Skill-UmarIqbal Command Line Interface (CLI)
Unified interface for the complete academic research ecosystem.
"""

import os
import sys
import argparse
import json

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from scripts.topic_discovery import search_arxiv, get_trending_domains, synthesize_topic_brief
from scripts.novelty_gap_analyzer import build_sota_matrix, evaluate_novelty
from scripts.simulation_engine import run_benchmark_simulation, run_monte_carlo_simulation
from scripts.academic_figures import plot_convergence_curve, plot_comparative_bars
from scripts.academic_humanizer import humanize_text
from scripts.latex_compiler import compile_latex
from scripts.docx_generator import create_academic_docx
from scripts.pptx_generator import create_academic_deck
from scripts.pipeline_runner import execute_research_pipeline


def main():
    parser = argparse.ArgumentParser(
        description="Research-Skill-UmarIqbal: Unified Academic Research Ecosystem CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run complete end-to-end research paper generation
  python cli.py run --topic "Federated Edge Healthcare" --difficulty easy --format ieee --output ./outputs/paper1

  # Search arXiv preprints
  python cli.py search --query "decentralized learning" --limit 5

  # Run scientific simulation
  python cli.py simulate --difficulty hard

  # Humanize a draft text file (purges zero-width chars and all em dashes)
  python cli.py humanize --file draft.txt

  # Compile LaTeX to PDF with auto-cleanup
  python cli.py compile --tex ./outputs/paper1/manuscript.tex
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available Commands")
    
    # RUN (Full Pipeline)
    run_parser = subparsers.add_parser("run", help="Execute complete end-to-end research pipeline")
    run_parser.add_argument("--topic", type=str, required=True, help="Research topic, question, or domain")
    run_parser.add_argument("--difficulty", type=str, default="medium", choices=["easy", "medium", "hard", "extreme"], help="Target difficulty tier")
    run_parser.add_argument("--format", type=str, default="ieee", choices=["ieee", "acm", "elsevier", "nature", "generic"], help="Journal formatting style")
    run_parser.add_argument("--output", type=str, default="./outputs/research_paper", help="Output directory")
    run_parser.add_argument("--no-presentation", action="store_true", help="Skip presentation deck generation")
    run_parser.add_argument("--no-docx", action="store_true", help="Skip Word document generation")
    run_parser.add_argument("--no-pdf", action="store_true", help="Skip LaTeX PDF compilation")
    run_parser.add_argument("--author", type=str, default="Umar Iqbal", help="Primary author name")
    run_parser.add_argument("--institution", type=str, default="Advanced Systems Laboratory", help="Author institution")
    
    # SEARCH (arXiv / Trends)
    search_parser = subparsers.add_parser("search", help="Search arXiv preprints and explore trending frontiers")
    search_parser.add_argument("--query", type=str, help="Search keywords")
    search_parser.add_argument("--limit", type=int, default=5, help="Maximum results to return")
    search_parser.add_argument("--trends", action="store_true", help="List trending frontier domains")
    
    # SIMULATE
    sim_parser = subparsers.add_parser("simulate", help="Run scientific simulation or benchmark generator")
    sim_parser.add_argument("--difficulty", type=str, default="medium", choices=["easy", "medium", "hard", "extreme"])
    sim_parser.add_argument("--monte-carlo", action="store_true", help="Run Monte Carlo diffusion simulation")
    sim_parser.add_argument("--trials", type=int, default=500, help="Number of Monte Carlo trials")
    
    # HUMANIZE
    hum_parser = subparsers.add_parser("humanize", help="Clean text of AI tells, watermarks, and all em dashes")
    hum_parser.add_argument("--file", type=str, help="Input text file to humanize")
    hum_parser.add_argument("--text", type=str, help="Raw text string to humanize")
    hum_parser.add_argument("--output", type=str, help="Output file for cleaned text")
    
    # COMPILE
    comp_parser = subparsers.add_parser("compile", help="Compile LaTeX document to PDF with auto-cleanup")
    comp_parser.add_argument("--tex", type=str, required=True, help="Path to .tex file")
    comp_parser.add_argument("--no-cleanup", action="store_true", help="Keep auxiliary build files")
    
    args = parser.parse_args()
    
    if args.command == "run":
        res = execute_research_pipeline(
            topic=args.topic,
            output_dir=os.path.abspath(args.output),
            difficulty=args.difficulty,
            journal_format=args.format,
            make_presentation=not args.no_presentation,
            make_docx=not args.no_docx,
            compile_pdf=not args.no_pdf,
            author_name=args.author,
            institution=args.institution
        )
        print("\nResearch Pipeline Completed Successfully!")
        print(f"Artifacts generated in: {os.path.abspath(args.output)}")
        
    elif args.command == "search":
        if args.trends:
            print(json.dumps(get_trending_domains(), indent=2))
        elif args.query:
            results = search_arxiv(args.query, max_results=args.limit)
            print(json.dumps(results, indent=2))
        else:
            print("Please specify --query or --trends. Run with -h for help.")
            
    elif args.command == "simulate":
        if args.monte_carlo:
            res = run_monte_carlo_simulation(num_trials=args.trials)
            print(f"Monte Carlo ({args.trials} trials) Final Mean: {res['final_mean']}, Std: {res['final_std']}")
        else:
            res = run_benchmark_simulation(args.difficulty)
            print(f"Benchmark Results ({args.difficulty.upper()} tier):")
            for row in res["benchmark_table"]:
                print(f"  {row['model']}: Acc={row['accuracy']}%, Latency={row['latency_ms']}ms, Memory={row['memory_mb']}MB")
                
    elif args.command == "humanize":
        input_text = ""
        if args.file and os.path.exists(args.file):
            with open(args.file, "r", encoding="utf-8") as f:
                input_text = f.read()
        elif args.text:
            input_text = args.text
        else:
            print("Please specify --file or --text. Run with -h for help.")
            return
            
        result = humanize_text(input_text)
        print(f"Humanization Complete:")
        print(f"  - Em dashes removed: {result['em_dashes_removed']}")
        print(f"  - Vocabulary replacements: {len(result['vocabulary_replacements'])}")
        print(f"  - Average sentence length: {result['average_sentence_length']} words")
        
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(result["cleaned_text"])
            print(f"Cleaned text written to: {args.output}")
        else:
            print("\nCleaned Text Output:\n")
            print(result["cleaned_text"])
            
    elif args.command == "compile":
        res = compile_latex(args.tex, auto_cleanup=not args.no_cleanup)
        print(res.get("message", res.get("error")))
        
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
