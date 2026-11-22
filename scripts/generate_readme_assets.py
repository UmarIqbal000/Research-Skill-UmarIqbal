"""
Ultra-High-Quality Visual Asset Generator for README
Renders 4K/600 DPI publication-grade graphics, banners, and composite showcases.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def generate_ultra_banner(output_path: str):
    """Generate an ultra-crisp modern open-source banner."""
    fig, ax = plt.subplots(figsize=(14, 4.2), dpi=400)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 4.2)
    ax.axis("off")
    
    # Gradient-like background with layered panels
    bg = patches.Rectangle((0, 0), 14, 4.2, facecolor="#070F2B", edgecolor="none")
    ax.add_patch(bg)
    
    # Geometric decorative ambient shapes
    glow1 = patches.Circle((13.0, 3.8), 2.2, facecolor="#1B1A55", alpha=0.6, edgecolor="none")
    glow2 = patches.Circle((0.5, 0.4), 1.8, facecolor="#535C91", alpha=0.3, edgecolor="none")
    ax.add_patch(glow1)
    ax.add_patch(glow2)
    
    # Left accent vertical bar
    accent = patches.Rectangle((0, 0), 0.35, 4.2, facecolor="#00ADB5", edgecolor="none")
    ax.add_patch(accent)
    
    # Subtitle Category Tracker
    ax.text(0.8, 3.3, "AUTONOMOUS RESEARCH ECOSYSTEM & AGENT SKILL", fontsize=11, fontweight="bold",
            color="#00FFF5", fontfamily="sans-serif", alpha=0.9)
    
    # Main Title
    ax.text(0.8, 2.35, "Research-Skill-UmarIqbal", fontsize=32, fontweight="heavy",
            color="#FFFFFF", fontfamily="sans-serif")
    
    # Mission Tagline
    ax.text(0.8, 1.65, "From Raw Concepts and Data to Submission-Ready Academic Manuscripts and Slide Decks",
            fontsize=13, fontweight="medium", color="#EEEEEE", fontfamily="sans-serif")
    
    # Pillars description
    ax.text(0.8, 1.15, "arXiv Discovery  •  Gap Analysis  •  Scientific Simulation  •  Nature/IEEE Figures  •  Anti-AI Humanizer  •  Zero Em-Dashes",
            fontsize=10.5, color="#A6B1E1", fontfamily="sans-serif")
    
    # Badges row
    badges = [
        ("Zero Em-Dashes", "#FF2E63", "#380017"),
        ("4 Difficulty Tiers", "#08D9D6", "#002B2B"),
        ("Multi-Journal LaTeX", "#F38181", "#331212"),
        ("Word DOCX + PDF", "#FCE38A", "#2E2805"),
        ("16:9 Conference Slides", "#95E1D3", "#0E2B25"),
        ("Auto Workspace Cleanup", "#A8D8EA", "#0E222B")
    ]
    
    x = 0.8
    for label, border_color, fill_color in badges:
        bw = len(label) * 0.115 + 0.35
        card = patches.FancyBboxPatch((x, 0.32), bw, 0.48, boxstyle="round,pad=0.06",
                                      facecolor=fill_color, edgecolor=border_color, linewidth=1.4)
        ax.add_patch(card)
        ax.text(x + bw/2, 0.52, label, fontsize=9, fontweight="bold",
                color="#FFFFFF", ha="center", va="center", fontfamily="sans-serif")
        x += bw + 0.28
        
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(output_path, dpi=400, bbox_inches="tight", pad_inches=0)
    plt.close()


def generate_ultra_pipeline(output_path: str):
    """Generate an ultra-crisp modern flowchart of the pipeline."""
    fig, ax = plt.subplots(figsize=(14, 4.4), dpi=400)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 4.4)
    ax.axis("off")
    
    # Clean background
    bg = patches.Rectangle((0, 0), 14, 4.4, facecolor="#F8FAFC", edgecolor="#E2E8F0", linewidth=1.5)
    ax.add_patch(bg)
    
    # Section Header
    ax.text(7.0, 3.9, "END-TO-END RESEARCH EXECUTION ARCHITECTURE",
            fontsize=14, fontweight="bold", color="#0F172A", ha="center", fontfamily="sans-serif")
    ax.text(7.0, 3.55, "Autonomous closed-loop progression from concept formulation to compiled dissemination",
            fontsize=9.5, color="#64748B", ha="center", fontfamily="sans-serif")
    
    stages = [
        {"num": "01", "name": "Topic & Trends", "desc": "arXiv API Queries\nFrontier Scouting", "color": "#2563EB", "bg": "#EFF6FF"},
        {"num": "02", "name": "Gap Analysis", "desc": "SOTA Matrix\nTriple Gap Check", "color": "#0D9488", "bg": "#F0FDFA"},
        {"num": "03", "name": "Difficulty Tier", "desc": "Easy / Med / Hard\nExtreme Tier", "color": "#7C3AED", "bg": "#F5F3FF"},
        {"num": "04", "name": "Simulation", "desc": "Monte Carlo\nODE & ML Data", "color": "#DB2777", "bg": "#FDF2F8"},
        {"num": "05", "name": "Visual Figures", "desc": "Nature/IEEE Style\n300 DPI & Vector", "color": "#EA580C", "bg": "#FFF7ED"},
        {"num": "06", "name": "Humanizer", "desc": "Anti-AI Linter\nZero Em-Dashes", "color": "#DC2626", "bg": "#FEF2F2"},
        {"num": "07", "name": "Multi-Build", "desc": "LaTeX & DOCX\nPDF + Cleanup", "color": "#0284C7", "bg": "#F0F9FF"},
        {"num": "08", "name": "Presentations", "desc": "16:9 Slide Deck\nAction Titles", "color": "#16A34A", "bg": "#F0FDF4"}
    ]
    
    start_x = 0.45
    box_w = 1.38
    gap = 0.28
    
    for i, st in enumerate(stages):
        x = start_x + i * (box_w + gap)
        
        # Subtle Drop Shadow
        shadow = patches.FancyBboxPatch((x + 0.02, 0.48), box_w, 2.5, boxstyle="round,pad=0.07",
                                        facecolor="#E2E8F0", edgecolor="none", alpha=0.5)
        ax.add_patch(shadow)
        
        # Main Card
        card = patches.FancyBboxPatch((x, 0.52), box_w, 2.5, boxstyle="round,pad=0.07",
                                      facecolor=st["bg"], edgecolor=st["color"], linewidth=1.6)
        ax.add_patch(card)
        
        # Number Badge
        num_circle = patches.Circle((x + box_w/2, 2.58), 0.24, facecolor=st["color"], edgecolor="none")
        ax.add_patch(num_circle)
        ax.text(x + box_w/2, 2.58, st["num"], fontsize=10, fontweight="bold", color="#FFFFFF", ha="center", va="center")
        
        # Stage Title
        ax.text(x + box_w/2, 1.95, st["name"], fontsize=9.5, fontweight="bold", color="#0F172A", ha="center", va="center")
        
        # Stage Description
        ax.text(x + box_w/2, 1.15, st["desc"], fontsize=8, color="#475569", ha="center", va="center", multialignment="center")
        
        # Connection Arrow
        if i < len(stages) - 1:
            ax.annotate("", xy=(x + box_w + gap - 0.03, 1.8), xytext=(x + box_w + 0.03, 1.8),
                        arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=1.8))
            
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(output_path, dpi=400, bbox_inches="tight", pad_inches=0.05)
    plt.close()


def generate_ultra_composite_showcase(output_path: str):
    """Generate a high-res 4-panel composite showcase figure for the README."""
    fig = plt.figure(figsize=(14, 7.5), dpi=350)
    
    # 2x2 Grid with custom spacing
    gs = fig.add_gridspec(2, 2, hspace=0.32, wspace=0.22, left=0.06, right=0.96, top=0.93, bottom=0.08)
    
    # Panel (a): Convergence Curve with Uncertainty
    ax1 = fig.add_subplot(gs[0, 0])
    rounds = np.arange(1, 41)
    prop_mean = 52.0 + 44.5 / (1.0 + np.exp(-0.28 * (rounds - 9)))
    base_mean = 50.0 + 37.2 / (1.0 + np.exp(-0.16 * (rounds - 14)))
    prop_std = 1.0 * np.exp(-rounds / 18.0) + 0.35
    base_std = 1.8 * np.exp(-rounds / 22.0) + 0.75
    
    ax1.plot(rounds, prop_mean, label="Proposed (Adaptive Momentum)", color="#1F4E79", lw=2.4)
    ax1.fill_between(rounds, prop_mean - prop_std, prop_mean + prop_std, color="#1F4E79", alpha=0.22)
    ax1.plot(rounds, base_mean, label="Baseline SOTA (SCAFFOLD)", color="#888888", ls="--", lw=1.8)
    ax1.fill_between(rounds, base_mean - base_std, base_mean + base_std, color="#888888", alpha=0.15)
    ax1.set_title("(a) Convergence Rate Under Asymmetric Noise", fontsize=11, fontweight="bold", pad=8)
    ax1.set_xlabel("Communication Rounds", fontsize=9.5, fontweight="bold")
    ax1.set_ylabel("Accuracy (%)", fontsize=9.5, fontweight="bold")
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend(frameon=True, facecolor="white", edgecolor="#D1D5DB", fontsize=8.5, loc="lower right")
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    
    # Panel (b): Dual-Axis Performance Trade-off
    ax2 = fig.add_subplot(gs[0, 1])
    models = ["FedAvg", "FedProx", "SCAFFOLD", "Proposed (Ours)"]
    x = np.arange(len(models))
    w = 0.35
    accs = [82.4, 85.1, 88.6, 94.8]
    lats = [48.2, 44.5, 39.0, 22.4]
    
    bar1 = ax2.bar(x - w/2, accs, w, label="Accuracy (%)", color="#1F4E79", edgecolor="black", lw=0.6)
    ax2.set_ylabel("Accuracy (%)", color="#1F4E79", fontweight="bold", fontsize=9.5)
    ax2.set_ylim([75, 100])
    ax2.set_xticks(x)
    ax2.set_xticklabels(models, fontweight="bold", fontsize=9)
    ax2.set_title("(b) Multi-Model Performance Trade-Off", fontsize=11, fontweight="bold", pad=8)
    ax2.spines["top"].set_visible(False)
    
    ax2_r = ax2.twinx()
    bar2 = ax2_r.bar(x + w/2, lats, w, label="Latency (ms)", color="#C00000", edgecolor="black", lw=0.6, alpha=0.88)
    ax2_r.set_ylabel("Per-Round Latency (ms)", color="#C00000", fontweight="bold", fontsize=9.5)
    ax2_r.set_ylim([0, 60])
    ax2_r.spines["top"].set_visible(False)
    
    for b in bar1:
        yval = b.get_height()
        ax2.text(b.get_x() + b.get_width()/2, yval + 0.6, f"{yval:.1f}", ha="center", va="bottom", fontsize=8, fontweight="bold")
    for b in bar2:
        yval = b.get_height()
        ax2_r.text(b.get_x() + b.get_width()/2, yval + 1.2, f"{yval:.1f}ms", ha="center", va="bottom", fontsize=8, fontweight="bold")
        
    # Panel (c): Architecture Modular Flow
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.axis("off")
    ax3.set_title("(c) Decentralized System Architecture Flow", fontsize=11, fontweight="bold", pad=8)
    
    blocks = [
        {"name": "Heterogeneous\nData Input", "x": 0.04, "w": 0.18, "c": "#E0F2FE", "ec": "#0284C7"},
        {"name": "Local Drift\nEstimation", "x": 0.28, "w": 0.18, "c": "#F3E8FF", "ec": "#7E22CE"},
        {"name": "Adaptive Momentum\nConsensus (Ours)", "x": 0.52, "w": 0.22, "c": "#DCFCE7", "ec": "#15803D"},
        {"name": "Global Target\nConvergence", "x": 0.79, "w": 0.17, "c": "#FFEDD5", "ec": "#C2410C"}
    ]
    for blk in blocks:
        patch = patches.FancyBboxPatch((blk["x"], 0.25), blk["w"], 0.55, boxstyle="round,pad=0.03",
                                      facecolor=blk["c"], edgecolor=blk["ec"], lw=1.6)
        ax3.add_patch(patch)
        ax3.text(blk["x"] + blk["w"]/2, 0.525, blk["name"], ha="center", va="center",
                 fontsize=8.5, fontweight="bold", color="#0F172A")
        
    arr = dict(arrowstyle="->", lw=2.0, color="#475569")
    ax3.annotate("", xy=(0.27, 0.525), xytext=(0.23, 0.525), arrowprops=arr)
    ax3.annotate("", xy=(0.51, 0.525), xytext=(0.47, 0.525), arrowprops=arr)
    ax3.annotate("", xy=(0.78, 0.525), xytext=(0.75, 0.525), arrowprops=arr)
    
    # Panel (d): Multi-Format Deliverable Suite Matrix
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis("off")
    ax4.set_title("(d) Autonomous Multi-Format Deliverables Suite", fontsize=11, fontweight="bold", pad=8)
    
    outputs = [
        ("IEEE / ACM / Springer LaTeX", "Compiles to publication PDF with zero build junk", "#0284C7"),
        ("Microsoft Word (.docx)", "Academic typographic hierarchy, formulas, and tables", "#2563EB"),
        ("16:9 Academic Slides (.pptx)", "Ghost deck principle, action titles, 2-column exhibits", "#16A34A"),
        ("Vector Figures & Data Tables", "Publication print dimensions (89 mm / 183 mm) at 300+ DPI", "#D97706")
    ]
    
    for idx, (head, sub, color) in enumerate(outputs):
        y_c = 0.85 - idx * 0.24
        bullet = patches.FancyBboxPatch((0.02, y_c - 0.08), 0.03, 0.16, boxstyle="round,pad=0.01",
                                        facecolor=color, edgecolor="none")
        ax4.add_patch(bullet)
        ax4.text(0.08, y_c + 0.02, head, fontsize=10, fontweight="bold", color="#0F172A")
        ax4.text(0.08, y_c - 0.08, sub, fontsize=8.5, color="#64748B")
        
    plt.savefig(output_path, dpi=350, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    assets_dir = os.path.abspath("c:/Users/umari/Downloads/Agy-General/Research_Skill_UmarIqbal/assets")
    generate_ultra_banner(os.path.join(assets_dir, "banner.png"))
    generate_ultra_pipeline(os.path.join(assets_dir, "pipeline_workflow.png"))
    generate_ultra_composite_showcase(os.path.join(assets_dir, "composite_showcase.png"))
    print("Ultra-high quality assets generated in:", assets_dir)
