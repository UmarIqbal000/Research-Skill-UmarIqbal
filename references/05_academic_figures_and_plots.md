# Academic Figures and Visualization Standards

This guide governs the generation of publication-grade figures, diagrams, and plots suitable for premier journals (Nature, Science, IEEE, ACM, Springer, Elsevier).

---

## 1. Core Visualization Principles

1. **One Figure, One Core Message**:
   A reviewer scans a figure in less than five seconds. The main takeaway must be immediate. Eliminate decorative borders, heavy backgrounds, and redundant legends.
2. **Restrained, Colorblind-Safe Palettes**:
   Default matplotlib colors (tab10) or Excel palettes look amateur. Use 2 to 4 semantic colors with one accent color. Ensure high contrast under grayscale printing.
3. **Print-Dimension First**:
   Always set dimensions explicitly before rendering:
   - **Single-Column Width**: 89 mm (3.5 inches).
   - **Double-Column Width**: 183 mm (7.2 inches).
   - **Aspect Ratio**: Typically 4:3 or 16:9 for multi-panel composite figures.
4. **Vector First with 300+ DPI Raster Previews**:
   Save the master file as vector PDF or SVG for crystal-clear vector rendering. Save a companion 300 DPI PNG preview for immediate viewing.

---

## 2. Standard Academic Color Palettes

### Palette 1: Nature / Science Minimalist
- Primary Deep Navy: `#1F4E79`
- Accent Crimson: `#C00000`
- Slate Steel: `#595959`
- Warm Ochre: `#D99B00`
- Neutral Background: `#FFFFFF`

### Palette 2: IEEE Engineering Blue
- Deep Blue: `#004080`
- Cyan Tech: `#0080FF`
- Cool Gray: `#708090`
- Alert Orange: `#E65100`

### Palette 3: High-Contrast Perceptual (Viridis / Magma)
- Ideal for continuous heatmaps, surface scans, and density plots.

---

## 3. Supported Figure Archetypes

Use `scripts/academic_figures.py` to generate the following standard archetypes:

1. **System Architecture / Pipeline Diagram**:
   - Clean horizontal block flow showing input data, transformation modules, algorithmic core, and final output.
   - Distinct color coding for proposed components versus baseline modules.

2. **Performance Curves with Uncertainty Bands**:
   - Solid lines for the proposed method; dashed or dotted lines for competing baselines.
   - Semi-transparent shaded error regions (`alpha=0.15` to `0.25`) representing standard deviation or 95% confidence intervals.

3. **Grouped Ablation Bar Charts**:
   - Clear value labels positioned directly above bars.
   - Clean horizontal baseline at y=0 without vertical grid lines.

4. **Multi-Metric Radar / Spider Charts**:
   - Useful for comparing algorithms across 5 or more competing criteria (e.g., Accuracy, Speed, Memory, Robustness, Energy).

5. **Correlation or Attention Heatmaps**:
   - Annotated numeric values inside cells for matrices smaller than 10x10.
   - Diverging or sequential colormaps with an explicit colorbar and clear labels.

---

## 4. Typography and Legibility Rules

- **Font Family**: Arial, Helvetica, or Computer Modern Sans-Serif. Never use stylized or cursive fonts.
- **Font Sizes**:
  - Title / Panel Label (e.g., "(a)", "(b)"): 10 to 12 pt bold.
  - Axis Labels: 9 to 10 pt bold.
  - Tick Labels and Legend: 8 to 9 pt regular.
  - In-Plot Annotations: 7 to 8 pt regular.
- **Tick Marks**: Place ticks pointing outward or omit tick lines and rely on clean values.
- **No Em Dashes**: Never use em dashes in axis labels, legend labels, or figure captions. Use parentheses or colons (e.g., "Latency (ms)" instead of "Latency — ms").
