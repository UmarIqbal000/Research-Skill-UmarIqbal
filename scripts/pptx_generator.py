"""
Academic Conference Slide Deck Generator (PPTX)
Creates 16:9 widescreen academic conference presentations using python-pptx.
Implements the Ghost Deck Principle, Action Titles, and strict academic design standards.
Strictly eliminates em dashes across all slides.
"""

import os
import sys
from typing import List, Dict, Any, Optional
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor


# Academic Presentation Theme Colors
NAVY_PRIMARY = RGBColor(0x1F, 0x4E, 0x79)
BLUE_ACCENT = RGBColor(0x2E, 0x75, 0xB6)
CRIMSON_ALERT = RGBColor(0xC0, 0x00, 0x00)
TEXT_DARK = RGBColor(0x22, 0x22, 0x22)
MUTED_GRAY = RGBColor(0x66, 0x66, 0x66)
LIGHT_BG = RGBColor(0xF8, 0xF9, 0xFA)


def create_academic_deck(
    title: str,
    subtitle: str,
    presenter_info: str,
    slides_data: List[Dict[str, Any]],
    output_path: str = "presentation.pptx"
) -> Dict[str, Any]:
    """
    Generate an academic presentation adhering to communication-first design rules.
    """
    prs = Presentation()
    
    # Configure 16:9 Widescreen (13.33 x 7.5 inches)
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)
    
    blank_layout = prs.slide_layouts[6] # Blank slide
    
    # -------------------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------------------
    slide1 = prs.slides.add_slide(blank_layout)
    
    # Title Text Box
    t_box = slide1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.33), Inches(2.2))
    tf = t_box.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = title.replace("—", ", ").replace("--", ", ")
    p1.font.name = "Arial"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = NAVY_PRIMARY
    
    # Subtitle
    p2 = tf.add_paragraph()
    p2.text = subtitle.replace("—", ", ").replace("--", ", ")
    p2.font.name = "Arial"
    p2.font.size = Pt(18)
    p2.font.color.rgb = BLUE_ACCENT
    p2.space_before = Pt(12)
    
    # Presenter Information
    auth_box = slide1.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(11.33), Inches(1.5))
    tf_auth = auth_box.text_frame
    p_auth = tf_auth.paragraphs[0]
    p_auth.text = presenter_info.replace("—", ", ").replace("--", ", ")
    p_auth.font.name = "Arial"
    p_auth.font.size = Pt(14)
    p_auth.font.color.rgb = MUTED_GRAY
    
    # -------------------------------------------------------------------------
    # CONTENT SLIDES
    # -------------------------------------------------------------------------
    for slide_data in slides_data:
        slide = prs.slides.add_slide(blank_layout)
        
        # Action Title (Top banner)
        action_title = slide_data.get("action_title", "Takeaway Sentence")
        action_title = action_title.replace("—", ", ").replace("--", ", ")
        
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.73), Inches(1.2))
        tf_h = header_box.text_frame
        tf_h.word_wrap = True
        p_h = tf_h.paragraphs[0]
        p_h.text = action_title
        p_h.font.name = "Arial"
        p_h.font.size = Pt(22)
        p_h.font.bold = True
        p_h.font.color.rgb = NAVY_PRIMARY
        
        # Category Tracker (Small breadcrumb above title)
        category = slide_data.get("category", "").upper()
        if category:
            p_cat = tf_h.add_paragraph()
            p_cat.text = category
            p_cat.font.name = "Arial"
            p_cat.font.size = Pt(10)
            p_cat.font.bold = True
            p_cat.font.color.rgb = BLUE_ACCENT
            p_cat.space_before = Pt(0)
            # Re-order so category is above title
            p_h.text, p_cat.text = p_cat.text, p_h.text
            p_h.font.size, p_cat.font.size = Pt(10), Pt(22)
            p_h.font.color.rgb, p_cat.font.color.rgb = BLUE_ACCENT, NAVY_PRIMARY
            
        # Check layout mode: 2-column exhibit vs text-focused
        image_path = slide_data.get("image_path", "")
        bullets = slide_data.get("bullets", [])
        
        if image_path and os.path.exists(image_path):
            # Left Column: Exhibit Image
            slide.shapes.add_picture(image_path, Inches(0.8), Inches(1.8), width=Inches(5.8))
            
            # Right Column: Bullet Takeaways
            text_box = slide.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.5), Inches(4.8))
            tf_b = text_box.text_frame
            tf_b.word_wrap = True
            
            for idx, b_text in enumerate(bullets):
                cleaned_b = b_text.replace("—", ", ").replace("--", ", ")
                p = tf_b.paragraphs[0] if idx == 0 else tf_b.add_paragraph()
                p.text = cleaned_b
                p.font.name = "Arial"
                p.font.size = Pt(16)
                p.font.color.rgb = TEXT_DARK
                p.space_after = Pt(14)
                p.level = 0
        else:
            # Full Width Bulleted Layout
            text_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.73), Inches(5.0))
            tf_b = text_box.text_frame
            tf_b.word_wrap = True
            
            for idx, b_text in enumerate(bullets):
                cleaned_b = b_text.replace("—", ", ").replace("--", ", ")
                p = tf_b.paragraphs[0] if idx == 0 else tf_b.add_paragraph()
                p.text = cleaned_b
                p.font.name = "Arial"
                p.font.size = Pt(18)
                p.font.color.rgb = TEXT_DARK
                p.space_after = Pt(16)
                p.level = 0
                
        # Optional Footer Citation
        footnote = slide_data.get("footnote", "")
        if footnote:
            fn_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.8), Inches(11.73), Inches(0.4))
            tf_fn = fn_box.text_frame
            p_fn = tf_fn.paragraphs[0]
            p_fn.text = footnote.replace("—", ", ").replace("--", ", ")
            p_fn.font.name = "Arial"
            p_fn.font.size = Pt(10)
            p_fn.font.color.rgb = MUTED_GRAY
            
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    prs.save(output_path)
    
    return {
        "pptx_path": output_path,
        "total_slides": len(prs.slides),
        "size_kb": round(os.path.getsize(output_path) / 1024, 1)
    }


if __name__ == "__main__":
    sample_slides = [
        {
            "category": "Context & Challenge",
            "action_title": "Heterogeneous Edge Devices Diverge Rapidly Under Asynchronous Updates",
            "bullets": [
                "Local dataset non-identifiability causes aggressive client drift.",
                "Centralized coordination introduces prohibitive communication latency across low-bandwidth nodes.",
                "Prior heuristics fail to guarantee bounded asymptotic variance."
            ],
            "footnote": "Source: McMahan et al. (2017); Karimireddy et al. (2020)"
        },
        {
            "category": "Core Methodology",
            "action_title": "Adaptive Trimmed-Mean Aggregation Guarantees Asymptotic Consensus",
            "bullets": [
                "Nodes exchange localized momentum vectors rather than raw parameters.",
                "Adversarial perturbations are filtered via geometric center trimming.",
                "Proven convergence rate: O(1 / sqrt(K)) under arbitrary non-convex objectives."
            ],
            "footnote": "Theorem 1 & Proposition 2 in manuscript"
        }
    ]
    res = create_academic_deck(
        title="Adaptive Momentum Aggregation for Edge Networks",
        subtitle="Provable Convergence and High-Throughput Decentralized Consensus",
        presenter_info="Umar Iqbal | Advanced Research Systems | IEEE INFOCOM 2026",
        slides_data=sample_slides,
        output_path="test_deck.pptx"
    )
    print("Academic Deck Generator Test Output:", res)
