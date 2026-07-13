def check_logic(statement: str) -> str:
    if "always" in statement and "except" in statement:
        return "Inconsistent: 'always' contradicts 'except'."
    if "never" in statement and "but" in statement:
        return "Inconsistent: 'never' contradicts the following clause."
    return "No obvious logical inconsistencies detected."

if __name__ == "__main__":
    tests = [
        "I always follow the rules except on weekends.",
        "I never eat sugar but I had cake yesterday.",
        "The sky is blue."
    ]

    for t in tests:
        print(t, "->", check_logic(t))
