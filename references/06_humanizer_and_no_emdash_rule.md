# Academic Humanizer and Anti-AI Detector Protocol

This guide establishes the mandatory rules for removing AI artifacts, eliminating telltale vocabulary, calibrating sentence rhythms, and strictly enforcing the prohibition of em dashes across all research documents.

---

## 1. Core Humanization Principles

Academic writing written by experienced human scholars has distinct characteristics:
- It is direct, objective, and evidence-bound.
- It uses third-person plural ("we") or impersonal passive when appropriate.
- Every claim is tied to an explicit number, table, figure, or citation.
- It varies in sentence length (burstiness): short direct assertions balance substantive explanations.
- It avoids promotional hype, decorative adjectives, and formulaic AI transition formulas.

---

## 2. The Strict NO EM DASH Rule (Non-Negotiable)

**Directive**: Under no circumstances should an em dash (`—`, `\textemdash`, `---`, or `--` acting as a dash) be included in the manuscript, abstract, captions, code comments, or presentations.

### Transformation Strategies for Em Dashes:
1. **Recast with Parentheses**:
   - *AI Draft*: The proposed algorithm—which operates without central coordination—converges in polynomial time.
   - *Humanized*: The proposed algorithm (which operates without central coordination) converges in polynomial time.
2. **Recast with Colons**:
   - *AI Draft*: We observe a key limitation—gradient updates diverge under non-IID data.
   - *Humanized*: We observe a key limitation: gradient updates diverge under non-IID data.
3. **Recast with Commas or Semicolons**:
   - *AI Draft*: Prior methods require full synchronization—imposing severe network overhead.
   - *Humanized*: Prior methods require full synchronization, which imposes severe network overhead.
4. **Split into Two Concise Sentences**:
   - *AI Draft*: Edge nodes possess constrained memory—this forces aggressive quantization.
   - *Humanized*: Edge nodes possess constrained memory. This limitation forces aggressive quantization.

---

## 3. The AI Vocabulary Ban List

The following words and phrases are telltale markers of generic large language model generation. They must be eliminated or replaced:

| Banned AI Word / Phrase | Why It Is Flagged | Academic Replacement |
| :--- | :--- | :--- |
| **delve / delving** | Universal LLM favorite | examine, analyze, investigate, study |
| **tapestry / rich tapestry** | Figurative cliché | combination, spectrum, collection, structure |
| **pivotal / crucial role** | Inflated significance | central, key, critical factor, primary |
| **testament to** | Promotional hyperbole | evidence of, indicates, demonstrates |
| **underscore / underscores** | Overused transition verb | highlights, confirms, shows, reveals |
| **intricate / nuances** | Vague complexity filler | complex, detailed, specific properties |
| **realm / landscape** | Abstract fluff | domain, setting, context, field |
| **multifaceted / myriad** | Empty quantifier | varied, multiple, several, distinct |
| **seamless / seamlessly** | Marketing buzzword | directly, consistently, without interruption |
| **foster / harness** | Overused active filler | enable, support, implement, utilize |
| **paves the way for** | Vague forward-looking hype | enables, provides a foundation for |
| **sheds light on** | Journalistic cliché | clarifies, reveals, explains, resolves |
| **serves as / acts as** | Copula avoidance | is, functions as |
| **in order to** | Wordy filler | to |
| **it is worth noting that** | Boilerplate padding | Cut entirely; state the fact directly |

---

## 4. Syntactic Rhythm and Burstiness Calibration

### Rule A: Eliminate Participle "-ing" Tails
LLMs habitually append weak participle clauses to pad sentences.
- *AI Draft*: The model achieves 94% accuracy, highlighting its effectiveness and showcasing its potential for deployment.
- *Humanized*: The model achieves 94% accuracy, which exceeds the baseline by 4.2 percentage points (Table 2).

### Rule B: Split Clause-Stacked Sentences
Sentences containing more than 30 words or chaining three subordinate clauses ("which", "that", "while", "whereby") must be split into two crisp statements.
- *AI Draft*: Existing frameworks, while showing empirical promise across standard synthetic distributions, suffer from acute communication overhead, which makes real-time edge orchestration impractical.
- *Humanized*: Existing frameworks show empirical promise on synthetic data. However, high communication overhead prevents their deployment on real-time edge networks.

### Rule C: Varied Sentence Openers
Do not begin three consecutive sentences with conjunctions like "Moreover,", "Furthermore,", "Additionally,", or "In particular,". Connect ideas logically through substantive nouns and verbs.

---

## 5. Watermark and Zero-Width Unicode Purging

To ensure clean processing and eliminate hidden tracking tokens, `scripts/academic_humanizer.py` automatically strips:
- Zero-width spaces (`\u200B`)
- Zero-width non-joiners (`\u200C`)
- Zero-width joiners (`\u200D`)
- Byte order marks (`\uFEFF`)
- Telltale Unicode quotation marks and homoglyphs, replacing them with standard ASCII equivalents.

---

## 6. Claim-to-Evidence Discipline

Every empirical claim in the paper must be accompanied by its supporting evidence:
- Weak: "Our method is significantly faster."
- Strong: "Our method reduces per-epoch training latency by 38% compared to FedAvg (Figure 4)."
- If a numerical claim lacks empirical evidence, soften the verb to calibrated hedging: "suggests", "is consistent with", or "indicates".
