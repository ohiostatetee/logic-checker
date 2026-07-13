"""
🧠 Logic Checker
A simple Python tool that evaluates the logical consistency of statements.
Useful for AI evaluation, reasoning analysis, and micro‑task workflows.

Part of the Catatonix AI Evaluation Toolkit.
Author: Thomas Moore (Catatonix)
"""

import sys
import json
from typing import List, Dict

CONTRADICTION_PAIRS = [
    ("is", "is not"),
    ("true", "false"),
    ("yes", "no"),
    ("always", "never"),
]

def find_contradictions(text: str) -> List[Dict[str, str]]:
    text_lower = text.lower()
    results = []
    for positive, negative in CONTRADICTION_PAIRS:
        if positive in text_lower and negative in text_lower:
            results.append({"positive": positive, "negative": negative})
    return results

def consistency_score(text: str) -> float:
    contradictions = find_contradictions(text)
    score = max(0.0, 1.0 - (0.15 * len(contradictions)))
    return round(score, 2)

def analyze_text(text: str) -> Dict:
    return {
        "input_text": text,
        "consistency_score": consistency_score(text),
        "contradictions_found": find_contradictions(text),
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python logic_checker.py \"Your text here\"")
        sys.exit(1)
    print(json.dumps(analyze_text(sys.argv[1]), indent=2))

if __name__ == "__main__":
    main()
