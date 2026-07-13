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
            results.append(
                {
                    "type": "contradiction",
                    "positive_phrase": positive,
                    "negative_phrase": negative,
                }
            )

    return results


def consistency_score(text: str) -> float:
    # Very simple heuristic: fewer contradictions → higher score
    contradictions = find_contradictions(text)
    base_score = 1.0
    penalty = 0.15 * len(contradictions)
    score = max(0.0, base_score - penalty)
    return round(score, 2)


def analyze_text(text: str) -> Dict:
    contradictions = find_contradictions(text)
    score = consistency_score(text)

    return {
        "input_text": text,
        "consistency_score": score,
        "contradictions_found": contradictions,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python logic_checker.py \"Your text here\"")
        sys.exit(1)

    text = sys.argv[1]
    result = analyze_text(text)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
