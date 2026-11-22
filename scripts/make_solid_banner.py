"""
Generate Centered Ultra-Premium Banner PNG without any left blue line.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def create_centered_banner(output_path: str):
    fig = plt.figure(figsize=(12, 3.4), dpi=300, facecolor="#080C14")
    ax = fig.add_axes([0, 0, 1, 1], facecolor="#080C14")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3.4)
    ax.axis("off")
    
    # Ambient center glow
    glow = patches.Circle((6.0, 1.7), 3.2, facecolor="#1E3A8A", alpha=0.25, edgecolor="none")
    ax.add_patch(glow)
    
    # Subtle uniform border
    border = patches.FancyBboxPatch((0.05, 0.05), 11.9, 3.3, boxstyle="round,pad=0.04",
                                    facecolor="none", edgecolor="#1E293B", linewidth=1.2)
    ax.add_patch(border)
    
    # Top Tag (Centered at x=6.0)
    top_w = 3.6
    top_x = 6.0 - top_w / 2
    pill_top = patches.FancyBboxPatch((top_x, 2.75), top_w, 0.38, boxstyle="round,pad=0.04",
                                      facecolor="#0F172A", edgecolor="#38BDF8", linewidth=1.2)
    ax.add_patch(pill_top)
    ax.plot(top_x + 0.28, 2.94, marker='o', markersize=4.5, color="#38BDF8")
    ax.text(6.08, 2.94, "AUTONOMOUS RESEARCH ECOSYSTEM", fontsize=8.5, fontweight="bold",
            color="#38BDF8", ha="center", va="center", fontfamily="sans-serif")
    
    # Brand Title (Centered at x=6.0)
    ax.text(6.0, 2.05, "Research-Skill-UmarIqbal", fontsize=28, fontweight="bold",
            color="#FFFFFF", ha="center", fontfamily="sans-serif")
    
    # Subtitle (Centered at x=6.0)
    ax.text(6.0, 1.48, "From Raw Concepts and Data to Submission-Ready Academic Manuscripts and Slide Decks",
            fontsize=11.5, color="#94A3B8", ha="center", fontfamily="sans-serif")
    
    # Feature Badges Row (Centered at x=6.0)
    badges = [
        ("Zero Em-Dashes", "#E11D48", "#1E1E2E"),
        ("4 Difficulty Tiers", "#0EA5E9", "#0C2538"),
        ("Multi-Journal LaTeX", "#A855F7", "#241530"),
        ("Word DOCX + PDF", "#F97316", "#2E1C0C"),
        ("16:9 Academic Slides", "#10B981", "#092B20"),
        ("Clean Workspace", "#64748B", "#1E293B")
    ]
    
    # Calculate total width
    pill_widths = [len(label) * 0.105 + 0.32 for label, _, _ in badges]
    gap = 0.20
    total_w = sum(pill_widths) + gap * (len(badges) - 1)
    start_x = 6.0 - total_w / 2
    
    cur_x = start_x
    for i, (label, border_c, bg_c) in enumerate(badges):
        bw = pill_widths[i]
        p = patches.FancyBboxPatch((cur_x, 0.58), bw, 0.46, boxstyle="round,pad=0.05",
                                   facecolor=bg_c, edgecolor=border_c, linewidth=1.3)
        ax.add_patch(p)
        ax.plot(cur_x + 0.15, 0.81, marker='o', markersize=3.8, color=border_c)
        ax.text(cur_x + 0.26 + (bw - 0.26)/2, 0.81, label, fontsize=8.2, fontweight="bold",
                color="#FFFFFF", ha="center", va="center", fontfamily="sans-serif")
        cur_x += bw + gap
        
    # Bottom Sub-bar (Centered at x=6.0)
    ax.text(6.0, 0.22, "arXiv Discovery  •  Gap Analysis  •  Scientific Simulation  •  Nature/IEEE Figures  •  Anti-AI Humanizer",
            fontsize=8.5, color="#475569", ha="center", fontfamily="sans-serif")
    
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print("Centered banner created at:", output_path)


if __name__ == "__main__":
    banner_png = "c:/Users/umari/Downloads/Agy-General/Research_Skill_UmarIqbal/assets/banner.png"
    create_centered_banner(banner_png)
