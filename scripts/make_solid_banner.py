"""
Generate Ultra-Premium Banner PNG without any white margins.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def create_solid_banner(output_path: str):
    # Fixed 12 x 3.4 inches at 300 DPI = 3600 x 1020 pixels
    fig = plt.figure(figsize=(12, 3.4), dpi=300, facecolor="#080C14")
    ax = fig.add_axes([0, 0, 1, 1], facecolor="#080C14") # Fill 100% of the figure
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3.4)
    ax.axis("off")
    
    # Left vertical glow accent bar
    accent = patches.Rectangle((0, 0), 0.15, 3.4, facecolor="#38BDF8", edgecolor="none")
    ax.add_patch(accent)
    
    # Ambient soft circular glow
    glow1 = patches.Circle((11.2, 3.0), 2.2, facecolor="#1E3A8A", alpha=0.35, edgecolor="none")
    glow2 = patches.Circle((1.5, 0.4), 1.6, facecolor="#06B6D4", alpha=0.20, edgecolor="none")
    ax.add_patch(glow1)
    ax.add_patch(glow2)
    
    # Top Tag
    pill_top = patches.FancyBboxPatch((0.55, 2.72), 3.2, 0.38, boxstyle="round,pad=0.04",
                                      facecolor="#0F172A", edgecolor="#38BDF8", linewidth=1.2)
    ax.add_patch(pill_top)
    ax.plot(0.72, 2.91, marker='o', markersize=5, color="#38BDF8")
    ax.text(0.90, 2.91, "AUTONOMOUS RESEARCH ECOSYSTEM", fontsize=8.5, fontweight="bold",
            color="#38BDF8", va="center", fontfamily="sans-serif")
    
    # Brand Title
    ax.text(0.55, 2.05, "Research-Skill-UmarIqbal", fontsize=28, fontweight="bold",
            color="#FFFFFF", fontfamily="sans-serif")
    
    # Subtitle
    ax.text(0.55, 1.48, "From Raw Concepts and Data to Submission-Ready Academic Manuscripts and Slide Decks",
            fontsize=11.5, color="#94A3B8", fontfamily="sans-serif")
    
    # Feature Badges Row
    badges = [
        ("Zero Em-Dashes", "#E11D48", "#1E1E2E"),
        ("4 Difficulty Tiers", "#0EA5E9", "#0C2538"),
        ("Multi-Journal LaTeX", "#A855F7", "#241530"),
        ("Word DOCX + PDF", "#F97316", "#2E1C0C"),
        ("16:9 Academic Slides", "#10B981", "#092B20"),
        ("Clean Workspace", "#64748B", "#1E293B")
    ]
    
    x = 0.55
    for label, border_c, bg_c in badges:
        bw = len(label) * 0.105 + 0.32
        p = patches.FancyBboxPatch((x, 0.58), bw, 0.46, boxstyle="round,pad=0.05",
                                   facecolor=bg_c, edgecolor=border_c, linewidth=1.3)
        ax.add_patch(p)
        # Dot
        ax.plot(x + 0.16, 0.81, marker='o', markersize=4, color=border_c)
        ax.text(x + 0.28, 0.81, label, fontsize=8.5, fontweight="bold",
                color="#FFFFFF", va="center", fontfamily="sans-serif")
        x += bw + 0.22
        
    # Sub-bar
    ax.text(0.55, 0.22, "arXiv Discovery  •  Gap Analysis  •  Scientific Simulation  •  Nature/IEEE Figures  •  Anti-AI Humanizer",
            fontsize=8.5, color="#475569", fontfamily="sans-serif")
    
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print("Solid banner created at:", output_path)


if __name__ == "__main__":
    banner_png = "c:/Users/umari/Downloads/Agy-General/Research_Skill_UmarIqbal/assets/banner.png"
    create_solid_banner(banner_png)
