"""
Generate Visual Assets for README
Creates high-resolution header banner and pipeline architecture graphics.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def create_banner(output_path: str):
    """Generate a sleek, modern academic header banner."""
    fig, ax = plt.subplots(figsize=(12, 3.2), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3.2)
    ax.axis("off")
    
    # Background gradient or solid deep navy
    bg = patches.Rectangle((0, 0), 12, 3.2, facecolor="#0B192C", edgecolor="none")
    ax.add_patch(bg)
    
    # Subtle accent glow shape
    accent_bar = patches.Rectangle((0, 0), 0.25, 3.2, facecolor="#008DDA", edgecolor="none")
    ax.add_patch(accent_bar)
    
    # Title
    ax.text(0.6, 2.1, "RESEARCH-SKILL-UMARIQBAL", fontsize=24, fontweight="bold", 
            color="#FFFFFF", fontfamily="sans-serif")
    
    # Subtitle
    ax.text(0.6, 1.5, "The Autonomous Academic Research & Publication Ecosystem", 
            fontsize=13, fontweight="bold", color="#41B06E", fontfamily="sans-serif")
    
    # Secondary description
    ax.text(0.6, 1.05, "Literature Gap Analysis  •  Scientific Simulation  •  Publication Figures (Nature/IEEE)  •  Anti-AI Humanization  •  PPTX Decks", 
            fontsize=9.5, color="#B0C4DE", fontfamily="sans-serif")
    
    # Feature Pills
    pills = [
        ("Zero Em-Dashes", "#E74C3C"),
        ("4 Difficulty Tiers", "#3498DB"),
        ("Multi-Journal LaTeX", "#9B59B6"),
        ("Word DOCX + PDF", "#E67E22"),
        ("16:9 Academic Slides", "#1ABC9C")
    ]
    
    x_pos = 0.6
    for label, color in pills:
        box = patches.FancyBboxPatch((x_pos, 0.35), len(label)*0.11 + 0.3, 0.45,
                                     boxstyle="round,pad=0.08",
                                     facecolor="#1E3E62", edgecolor=color, linewidth=1.2)
        ax.add_patch(box)
        ax.text(x_pos + (len(label)*0.11 + 0.3)/2, 0.53, label, fontsize=8.5, 
                fontweight="bold", color="#FFFFFF", ha="center", va="center", fontfamily="sans-serif")
        x_pos += len(label)*0.11 + 0.55
        
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(output_path, dpi=300, bbox_inches="tight", pad_inches=0)
    plt.close()


def create_pipeline_graphic(output_path: str):
    """Generate a clean visual flowchart of the 8-stage research pipeline."""
    fig, ax = plt.subplots(figsize=(12, 3.8), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3.8)
    ax.axis("off")
    
    # Background
    bg = patches.Rectangle((0, 0), 12, 3.8, facecolor="#F8FAFC", edgecolor="#CBD5E1", linewidth=1)
    ax.add_patch(bg)
    
    ax.text(6.0, 3.4, "END-TO-END RESEARCH EXECUTION PIPELINE", 
            fontsize=12, fontweight="bold", color="#0F172A", ha="center", fontfamily="sans-serif")
    
    stages = [
        {"num": "01", "name": "Topic & Trends", "desc": "arXiv API & Active Frontiers", "color": "#1E40AF", "bg": "#EFF6FF"},
        {"num": "02", "name": "Gap Analysis", "desc": "SOTA Matrix & Novelty Gate", "color": "#0D9488", "bg": "#F0FDFA"},
        {"num": "03", "name": "Simulation", "desc": "Monte Carlo & ML Benchmarks", "color": "#7C3AED", "bg": "#F5F3FF"},
        {"num": "04", "name": "Figures", "desc": "Nature/IEEE Vector PDF & PNG", "color": "#C026D3", "bg": "#FDF4FF"},
        {"num": "05", "name": "Humanizer", "desc": "Zero AI Tells & No Em-Dashes", "color": "#DC2626", "bg": "#FEF2F2"},
        {"num": "06", "name": "Build & Clean", "desc": "LaTeX/DOCX to PDF + Cleanup", "color": "#D97706", "bg": "#FFFBEB"},
        {"num": "07", "name": "Presentations", "desc": "16:9 Widescreen PPTX Deck", "color": "#059669", "bg": "#ECFDF5"}
    ]
    
    start_x = 0.5
    box_w = 1.35
    gap = 0.28
    
    for i, st in enumerate(stages):
        x = start_x + i * (box_w + gap)
        # Stage card
        card = patches.FancyBboxPatch((x, 0.7), box_w, 2.2, boxstyle="round,pad=0.08",
                                      facecolor=st["bg"], edgecolor=st["color"], linewidth=1.5)
        ax.add_patch(card)
        
        # Number pill
        num_box = patches.Circle((x + box_w/2, 2.5), 0.22, facecolor=st["color"], edgecolor="none")
        ax.add_patch(num_box)
        ax.text(x + box_w/2, 2.5, st["num"], fontsize=9, fontweight="bold", color="#FFFFFF", ha="center", va="center")
        
        # Text
        ax.text(x + box_w/2, 1.9, st["name"], fontsize=9.5, fontweight="bold", color="#1E293B", ha="center", va="center")
        ax.text(x + box_w/2, 1.25, st["desc"], fontsize=7.5, color="#64748B", ha="center", va="center", wrap=True, multialignment="center")
        
        # Arrow to next stage
        if i < len(stages) - 1:
            ax.annotate("", xy=(x + box_w + gap - 0.04, 1.8), xytext=(x + box_w + 0.04, 1.8),
                        arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=1.5))
            
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(output_path, dpi=300, bbox_inches="tight", pad_inches=0.05)
    plt.close()


if __name__ == "__main__":
    assets_dir = os.path.abspath("c:/Users/umari/Downloads/Agy-General/Research_Skill_UmarIqbal/assets")
    create_banner(os.path.join(assets_dir, "banner.png"))
    create_pipeline_graphic(os.path.join(assets_dir, "pipeline_workflow.png"))
    print("Assets generated in:", assets_dir)
