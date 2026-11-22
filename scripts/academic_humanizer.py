"""
Academic Humanizer and Anti-AI Detector Engine
Cleans AI-tell artifacts, strips invisible zero-width watermarks,
enforces sentence burstiness and readability standards,
and strictly eliminates all em dashes.
"""

import re
import sys
from typing import Dict, List, Tuple, Any


# AI Telltale Words and Academic Replacements
BANNED_AI_VOCAB = {
    r"\bdelve\b": "examine",
    r"\bdelving\b": "examining",
    r"\btapestry\b": "structure",
    r"\bpivotal\b": "central",
    r"\btestament to\b": "evidence of",
    r"\bunderscore\b": "highlight",
    r"\bunderscores\b": "highlights",
    r"\bintricate\b": "complex",
    r"\brealm\b": "domain",
    r"\bmultifaceted\b": "varied",
    r"\bseamlessly\b": "directly",
    r"\bseamless\b": "direct",
    r"\bfoster\b": "support",
    r"\bfostering\b": "supporting",
    r"\bpaves the way for\b": "enables",
    r"\bpaving the way for\b": "enabling",
    r"\bsheds light on\b": "clarifies",
    r"\bshedding light on\b": "clarifying",
    r"\bserves as\b": "is",
    r"\bacts as\b": "functions as",
    r"\bin order to\b": "to",
    r"\bit is worth noting that\b": "",
    r"\bit should be noted that\b": "",
    r"\bnotably,\b": "",
    r"\bimportantly,\b": "",
    r"\bgroundbreaking\b": "substantial",
    r"\bvibrant\b": "active"
}

# Superficial Participle Tails
SUPERFICIAL_TAILS = [
    r",\s*highlighting\s+the\s+importance\s+of\b[^,\.]*",
    r",\s*showcasing\s+its\s+effectiveness\b[^,\.]*",
    r",\s*underscoring\s+its\s+potential\b[^,\.]*",
    r",\s*marking\s+a\s+significant\s+step\b[^,\.]*"
]


def purge_zero_width_watermarks(text: str) -> str:
    """Strip hidden zero-width Unicode tracking characters and byte order marks."""
    zero_width_chars = [
        "\u200B",  # Zero width space
        "\u200C",  # Zero width non-joiner
        "\u200D",  # Zero width joiner
        "\uFEFF",  # Zero width no-break space / BOM
        "\u202A", "\u202B", "\u202C", "\u202D", "\u202E"  # BiDi controls
    ]
    cleaned = text
    for char in zero_width_chars:
        cleaned = cleaned.replace(char, "")
    return cleaned


def purge_em_dashes(text: str) -> Tuple[str, int]:
    """
    STRICT EM-DASH PURGE:
    Completely eliminates em dashes (Unicode em dash, LaTeX textemdash, triple hyphens, double hyphens)
    and recasts them cleanly using commas, colons, or parentheses.
    """
    count = 0
    
    # 1. Unicode Em Dash (—) with optional surrounding spaces
    em_pattern = re.compile(r"\s*—\s*")
    matches = em_pattern.findall(text)
    count += len(matches)
    # Replace em-dash surrounded by spaces with comma or colon based on context
    cleaned = re.sub(r"\s*—\s*", ", ", text)
    
    # 2. LaTeX \textemdash
    latex_em = re.compile(r"\s*\\textemdash\s*")
    count += len(latex_em.findall(cleaned))
    cleaned = re.sub(r"\s*\\textemdash\s*", ", ", cleaned)
    
    # 3. Triple hyphens (---)
    triple_h = re.compile(r"\s*---\s*")
    count += len(triple_h.findall(cleaned))
    cleaned = re.sub(r"\s*---\s*", ", ", cleaned)
    
    # 4. Double hyphens used as dashes (space -- space or word--word)
    double_dash = re.compile(r"(\w)\s*--\s*(\w)")
    count += len(double_dash.findall(cleaned))
    cleaned = double_dash.sub(r"\1, \2", cleaned)
    
    # Clean up any accidental double commas or comma-periods
    cleaned = re.sub(r",\s*,", ",", cleaned)
    cleaned = re.sub(r",\s*\.", ".", cleaned)
    
    return cleaned, count


def humanize_text(text: str) -> Dict[str, Any]:
    """
    Execute full academic humanization pipeline:
    - Purges zero-width tokens and watermarks
    - Eliminates banned AI vocabulary
    - Strips superficial "-ing" tails
    - Strictly removes all em dashes
    - Analyzes sentence length and burstiness
    """
    cleaned = purge_zero_width_watermarks(text)
    cleaned, em_dash_count = purge_em_dashes(cleaned)
    
    replacements_made = []
    
    # Replace Banned Vocabulary
    for pattern, replacement in BANNED_AI_VOCAB.items():
        matches = re.findall(pattern, cleaned, flags=re.IGNORECASE)
        if matches:
            replacements_made.append(f"{pattern} -> {replacement} ({len(matches)} occurrences)")
            cleaned = re.sub(pattern, replacement, cleaned, flags=re.IGNORECASE)
            
    # Strip superficial tails
    for tail_pattern in SUPERFICIAL_TAILS:
        cleaned = re.sub(tail_pattern, "", cleaned, flags=re.IGNORECASE)
        
    # Clean up whitespace
    cleaned = re.sub(r"[ \t]+", " ", cleaned)
    cleaned = re.sub(r"\n\s*\n\s*\n+", "\n\n", cleaned)
    
    # Sentence Length / Burstiness Analysis
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", cleaned) if s.strip()]
    lengths = [len(s.split()) for s in sentences]
    
    overlong_sentences = [
        {"sentence": s, "word_count": len(s.split())}
        for s in sentences if len(s.split()) > 32
    ]
    
    avg_length = sum(lengths) / len(lengths) if lengths else 0
    
    return {
        "cleaned_text": cleaned,
        "em_dashes_removed": em_dash_count,
        "vocabulary_replacements": replacements_made,
        "total_sentences": len(sentences),
        "average_sentence_length": round(avg_length, 1),
        "overlong_sentence_count": len(overlong_sentences),
        "overlong_sentences": overlong_sentences[:3]
    }


if __name__ == "__main__":
    sample = (
        "In order to delve into this intricate tapestry of decentralized optimization—which serves as a pivotal cornerstone—"
        "we present our groundbreaking framework, highlighting the importance of robustness. Furthermore, notably, it is worth noting that "
        "our approach underscores seamless coordination across edge nodes."
    )
    res = humanize_text(sample)
    print("Original Text:")
    print(sample)
    print("\nCleaned Text:")
    print(res["cleaned_text"])
    print(f"\nStats: Em-dashes removed={res['em_dashes_removed']}, Vocab replacements={len(res['vocabulary_replacements'])}")
