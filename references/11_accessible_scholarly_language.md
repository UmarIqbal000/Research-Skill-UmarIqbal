# Accessible Scholarly Language and Readability Standards

This guide enforces the "Lucid Rigor" principle: academic writing must be intellectually rigorous without being unnecessarily difficult, opaque, or convoluted to read.

---

## 1. The Core Principle: Lucid Rigor

Many academic papers suffer from "defensive complexity": authors intentionally use obscure vocabulary, long passive chains, and convoluted mathematical notation to make their work appear profound. This obfuscates good science.

**Our Standard**: High-impact research should be understandable to any interested researcher or practitioner in adjacent disciplines.
- State complex concepts using direct, concrete language.
- Define intuitive physical analogies before diving into equations.
- Never use a ten-dollar word when a familiar one expresses the thought with equal precision.

---

## 2. Seven Rules for Clear Academic Prose

### Rule 1: Concrete Agents and Actions
Avoid burying the main action of a sentence inside nominalized abstract nouns (e.g., turning verbs into nouns ending in *-tion*, *-ment*, or *-ence*).
- *Obscure*: "The achievement of convergence acceleration is made possible through the utilization of localized gradient aggregation."
- *Lucid*: "Localized gradient aggregation accelerates convergence."

### Rule 2: Intuition First, Formalism Second
When introducing a mathematical formula or algorithm:
1. First, state what problem it solves in one plain-English sentence.
2. Present the formal equation or notation.
3. Then explain what the trade-off or balance in the formula means intuitively.
- *Example*: "To prevent local models from over-fitting private client distributions, we add a drift penalty to the objective function: [Equation]. The parameter $\lambda$ controls how strongly local weights are pulled back toward the global consensus."

### Rule 3: Shorten and Unstack Sentences
Keep average sentence length between 15 and 25 words. If a sentence exceeds 30 words or contains more than two dependent clauses, split it.
- *Obscure*: "Although decentralized networks demonstrate remarkable scalability across simulated topologies, their propensity to suffer from Byzantine corruption under asynchronous conditions, which degrades global consensus, poses severe implementation barriers."
- *Lucid*: "Decentralized networks scale well across simulated topologies. However, under asynchronous conditions, Byzantine nodes frequently disrupt global consensus and degrade system reliability."

### Rule 4: Ban Pretentious and Arcane Jargon
Replace self-important academic filler with clean equivalents:
- *Notwithstanding the fact that* -> *Although*
- *In a multiplicity of instances* -> *Often*
- *Bespoke methodology* -> *Custom method*
- *Cognizant of* -> *Aware of*
- *Facilitate the elucidation of* -> *Clarify* or *Explain*
- *Effectuate* -> *Perform* or *Execute*
- *Ameliorate* -> *Improve*

### Rule 5: Active vs. Passive Voice Calibration
Use the passive voice when the object or process is the true focus (e.g., "The samples were heated to 100°C"). Use the active voice when describing the authors' reasoning or methodological actions:
- *Passive & Stiff*: "An analysis was performed by us regarding the latency bounds."
- *Active & Clear*: "We analyzed the latency bounds."

### Rule 6: Use Explicit Signposts
Guide the reader through complex arguments using transparent logical transitions:
- *Contrast*: "In contrast,", "However,", "On the other hand,"
- *Consequence*: "Consequently,", "As a result,", "Therefore,"
- *Condition*: "Under this assumption,", "When $k > 10$,"
- *Example*: "For example,", "Specifically,"

### Rule 7: Absolute Prohibition of Em Dashes
Never use an em dash (`—` or `--`). Use commas, colons, parentheses, or separate sentences. Em dashes often encourage authors to insert disjointed thoughts into otherwise coherent sentences.

---

## 3. Readability Self-Test Checklist

Before finalizing any section, verify:
1. Can an undergraduate student or engineer from an adjacent field read the abstract and understand what was done and why?
2. Are all acronyms defined on their first mention?
3. Does each paragraph begin with a clear topic sentence?
4. Are all symbols in equations defined immediately below the equation?
5. Has every em dash been eliminated and replaced with clean punctuation?
