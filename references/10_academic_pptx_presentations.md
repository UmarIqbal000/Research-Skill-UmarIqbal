# Academic Presentations (PPTX) Guide

This guide establishes the standards for creating high-impact academic conference presentations and seminar slide decks using `scripts/pptx_generator.py`.

---

## 1. Core Philosophy: The Ghost Deck Principle

An academic presentation differs fundamentally from a marketing pitch:
1. **The Ghost Deck Test**:
   Read only the slide titles in sequence. If the titles alone convey the complete logical argument of your paper from motivation to conclusion, the deck is structured correctly. If a slide title is a generic label (e.g., "Results" or "Method"), the test fails.
2. **Action Titles, Not Topic Labels**:
   - *Wrong*: "Experimental Results"
   - *Correct*: "Our Framework Reduces Training Latency by 38% Across All Benchmark Datasets"
   - *Wrong*: "Proposed Architecture"
   - *Correct*: "Decentralized Momentum Aggregation Eliminates Client Drift in Non-IID Settings"
3. **Evidence-Led Exhibits**:
   Every content slide carries one primary exhibit (a figure, table, or schematic) with a clear takeaway.
4. **Slides Support the Speaker**:
   Body text should provide orientation and evidence, not replace the spoken narrative. Limit body text to 3 to 4 crisp takeaways per slide.

---

## 2. Standard 10-Slide Academic Deck Structure

1. **Slide 1: Title & Authors**:
   Paper title, author names, affiliations, conference/venue name, and date.
2. **Slide 2: Motivation & Context**:
   The broad real-world or theoretical challenge and why it demands attention today.
3. **Slide 3: The Critical Research Gap**:
   Why existing state-of-the-art methods fail; the exact technical bottleneck.
4. **Slide 4: Core Insight & Architecture**:
   The foundational intuition and high-level system diagram.
5. **Slide 5: Formal Algorithmic Mechanism**:
   Key equations, algorithmic steps, or theoretical guarantees explained intuitively.
6. **Slide 6: Primary Experimental Results**:
   Main comparison against baselines; figure on the left, quantitative gains on the right.
7. **Slide 7: Ablation Analysis & Component Validation**:
   Evidence demonstrating that each specific design decision contributes to performance.
8. **Slide 8: Scalability and Robustness**:
   Behavior under stress, noise, distribution shifts, or large-scale parameters.
9. **Slide 9: Conclusion & Open Directions**:
   Summary of key contributions, practical impact, and future work.
10. **Slide 10: References & Acknowledgments**:
    Full bibliographic citations for borrowed data and contact information.

---

## 3. Visual & Typographic Standards

- **Aspect Ratio**: 16:9 widescreen format (13.33 in x 7.5 in / 33.86 cm x 19.05 cm).
- **Color Palette**:
  - Background: Pure White (`#FFFFFF`) or very light off-white (`#F8F9FA`).
  - Primary Headers: Deep Academic Navy (`#1F4E79`).
  - Accent / Focus: Mid Blue (`#2E75B6`) or Crimson (`#C00000`).
  - Body Text: Charcoal Slate (`#333333`).
- **Typography**:
  - Title Font: Arial, Calibri, or Helvetica (Bold, 24 to 28 pt).
  - Body Text: 16 to 18 pt regular, left-aligned.
  - Footnote / Source: 11 to 12 pt muted gray (`#666666`).
- **Layout Grid**:
  - Two-column split layout for result slides:
    - Left Column (55% width): High-resolution plot or architecture graphic.
    - Right Column (40% width): 3 bulleted insights interpreting the data.
- **Prohibited Elements**:
  - No decorative clip art, generic stock icons inside colored circles, or animated transitions.
  - **No em dashes**: Use colons, parentheses, or commas in slide bullet points.
