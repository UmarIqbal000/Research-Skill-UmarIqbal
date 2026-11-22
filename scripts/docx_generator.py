"""
Academic Word Document (DOCX) Generator
Creates publication-grade formatted Word documents (.docx) with academic typography,
structured sections, tables, captions, equations, and references.
Optionally converts to PDF via docx2pdf.
"""

import os
import sys
from typing import Dict, List, Any, Optional
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


def set_cell_border(cell, **kwargs):
    """
    Set cell borders for academic tables (booktabs style: top/bottom borders only).
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = tcPr.first_child_found_in("w:tcBorders")
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)
    
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = 'w:{}'.format(edge)
            element = tcBorders.find(qn(tag))
            if element is None:
                element = OxmlElement(tag)
                tcBorders.append(element)
            for key, val in edge_data.items():
                element.set(qn('w:{}'.format(key)), str(val))


def create_academic_docx(
    title: str,
    authors: List[str],
    affiliations: List[str],
    abstract: str,
    keywords: List[str],
    sections: List[Dict[str, Any]],
    tables: Optional[List[Dict[str, Any]]] = None,
    figure_paths: Optional[List[Dict[str, str]]] = None,
    references: Optional[List[str]] = None,
    output_path: str = "manuscript.docx",
    convert_to_pdf: bool = False
) -> Dict[str, Any]:
    """
    Construct a complete academic Word document.
    """
    doc = Document()
    
    # Page Setup: Standard 1 inch margins
    sections_setup = doc.sections[0]
    sections_setup.top_margin = Inches(1.0)
    sections_setup.bottom_margin = Inches(1.0)
    sections_setup.left_margin = Inches(1.0)
    sections_setup.right_margin = Inches(1.0)
    
    # Configure Normal Style
    style_normal = doc.styles['Normal']
    font_normal = style_normal.font
    font_normal.name = 'Times New Roman'
    font_normal.size = Pt(11)
    font_normal.color.rgb = RGBColor(0x22, 0x22, 0x22)
    
    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(12)
    run_title = p_title.add_run(title)
    run_title.font.name = 'Times New Roman'
    run_title.font.size = Pt(18)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
    
    # Authors
    p_auth = doc.add_paragraph()
    p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_auth.paragraph_format.space_after = Pt(4)
    run_auth = p_auth.add_run(", ".join(authors))
    run_auth.font.name = 'Times New Roman'
    run_auth.font.size = Pt(11)
    run_auth.font.bold = True
    
    # Affiliations
    p_aff = doc.add_paragraph()
    p_aff.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_aff.paragraph_format.space_after = Pt(16)
    run_aff = p_aff.add_run("; ".join(affiliations))
    run_aff.font.name = 'Times New Roman'
    run_aff.font.size = Pt(10)
    run_aff.font.italic = True
    run_aff.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    
    # Abstract
    p_abs_head = doc.add_paragraph()
    p_abs_head.paragraph_format.space_after = Pt(4)
    run_abs_h = p_abs_head.add_run("Abstract")
    run_abs_h.font.bold = True
    run_abs_h.font.size = Pt(11)
    
    p_abs = doc.add_paragraph()
    p_abs.paragraph_format.space_after = Pt(8)
    p_abs.paragraph_format.left_indent = Inches(0.4)
    p_abs.paragraph_format.right_indent = Inches(0.4)
    p_abs.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run_abs = p_abs.add_run(abstract)
    run_abs.font.size = Pt(10)
    run_abs.font.italic = True
    
    # Keywords
    p_kw = doc.add_paragraph()
    p_kw.paragraph_format.space_after = Pt(16)
    p_kw.paragraph_format.left_indent = Inches(0.4)
    run_kwh = p_kw.add_run("Keywords: ")
    run_kwh.font.bold = True
    run_kwh.font.size = Pt(10)
    run_kwt = p_kw.add_run(", ".join(keywords))
    run_kwt.font.size = Pt(10)
    
    # Sections
    for sec in sections:
        # Heading 1
        h1 = doc.add_paragraph()
        h1.paragraph_format.space_before = Pt(14)
        h1.paragraph_format.space_after = Pt(6)
        r_h1 = h1.add_run(sec.get("title", "Section"))
        r_h1.font.name = 'Times New Roman'
        r_h1.font.size = Pt(13)
        r_h1.font.bold = True
        r_h1.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
        
        # Paragraphs
        for para_text in sec.get("paragraphs", []):
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.line_spacing = 1.15
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.add_run(para_text)
            
    # Tables (if provided)
    if tables:
        for tbl_data in tables:
            caption = tbl_data.get("caption", "Table")
            headers = tbl_data.get("headers", [])
            rows = tbl_data.get("rows", [])
            
            p_tc = doc.add_paragraph()
            p_tc.paragraph_format.space_before = Pt(12)
            p_tc.paragraph_format.space_after = Pt(4)
            r_tc = p_tc.add_run(caption)
            r_tc.font.bold = True
            r_tc.font.size = Pt(10)
            
            table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            
            # Header Row
            for col_idx, h_text in enumerate(headers):
                cell = table.cell(0, col_idx)
                cell.text = h_text
                set_cell_border(cell, top={"val": "single", "sz": "12", "color": "000000"},
                                       bottom={"val": "single", "sz": "6", "color": "000000"})
                for p in cell.paragraphs:
                    for r in p.runs:
                        r.font.bold = True
                        r.font.size = Pt(9.5)
                        
            # Data Rows
            for row_idx, r_data in enumerate(rows):
                for col_idx, val in enumerate(r_data):
                    cell = table.cell(row_idx + 1, col_idx)
                    cell.text = str(val)
                    if row_idx == len(rows) - 1:
                        set_cell_border(cell, bottom={"val": "single", "sz": "12", "color": "000000"})
                    for p in cell.paragraphs:
                        for r in p.runs:
                            r.font.size = Pt(9.5)
                            
    # Figures (if provided)
    if figure_paths:
        for fig_data in figure_paths:
            f_path = fig_data.get("path", "")
            caption = fig_data.get("caption", "Figure")
            if os.path.exists(f_path):
                p_img = doc.add_paragraph()
                p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_img.paragraph_format.space_before = Pt(12)
                p_img.paragraph_format.space_after = Pt(4)
                doc.add_picture(f_path, width=Inches(fig_data.get("width_in", 4.5)))
                
                p_fc = doc.add_paragraph()
                p_fc.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_fc.paragraph_format.space_after = Pt(12)
                r_fc = p_fc.add_run(caption)
                r_fc.font.size = Pt(9.5)
                r_fc.font.italic = True
                
    # References
    if references:
        h_ref = doc.add_paragraph()
        h_ref.paragraph_format.space_before = Pt(16)
        h_ref.paragraph_format.space_after = Pt(6)
        r_href = h_ref.add_run("References")
        r_href.font.bold = True
        r_href.font.size = Pt(13)
        r_href.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
        
        for idx, ref in enumerate(references, 1):
            p_r = doc.add_paragraph()
            p_r.paragraph_format.space_after = Pt(4)
            p_r.paragraph_format.left_indent = Inches(0.3)
            p_r.paragraph_format.first_line_indent = Inches(-0.3)
            run_num = p_r.add_run(f"[{idx}] ")
            run_num.font.bold = True
            run_num.font.size = Pt(9.5)
            run_txt = p_r.add_run(ref)
            run_txt.font.size = Pt(9.5)
            
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    doc.save(output_path)
    
    result = {"docx_path": output_path, "size_kb": round(os.path.getsize(output_path) / 1024, 1)}
    
    if convert_to_pdf:
        try:
            from docx2pdf import convert
            pdf_path = os.path.splitext(output_path)[0] + ".pdf"
            convert(output_path, pdf_path)
            if os.path.exists(pdf_path):
                result["pdf_path"] = pdf_path
        except Exception as e:
            result["pdf_conversion_error"] = str(e)
            
    return result


if __name__ == "__main__":
    res = create_academic_docx(
        title="Decentralized Optimization on Heterogeneous Edge Networks",
        authors=["Umar Iqbal", "Antigravity Research Team"],
        affiliations=["Department of Computer Science, Advanced Systems Laboratory"],
        abstract="This paper introduces an adaptive momentum aggregation scheme for edge nodes operating under non-IID data distributions.",
        keywords=["Federated Learning", "Edge Computing", "Decentralized Optimization"],
        sections=[
            {"title": "1. Introduction", "paragraphs": ["Edge computing architectures face acute bandwidth limitations.", "We introduce a lightweight aggregation protocol."]},
            {"title": "2. Experimental Results", "paragraphs": ["Evaluations demonstrate a 38% reduction in network latency."]}
        ],
        references=["McMahan et al., Communication-Efficient Learning of Deep Networks, AISTATS 2017."],
        output_path="sample_academic.docx"
    )
    print("DOCX Generator Test Output:", res)
