"""C1: Rule-based medical diagnosis expert system (forward + backward chaining).
For learning purposes only - not a real medical tool.
"""

RULES = {
    "Flu": {"fever", "cough", "sore_throat"},
    "Allergy": {"sneezing", "runny_nose", "watery_eyes"},
    "Viral Infection": {"fever", "body_ache", "headache"},
}


def forward_chaining(symptoms):
    """Data-driven: from known symptoms, derive all diseases whose rule fires."""
    return [d for d, conditions in RULES.items() if conditions <= symptoms]


def backward_chaining(goal, symptoms):
    """Goal-driven: check whether the symptoms support the suspected disease.

    Returns (supported, missing). supported is None if the disease is unknown.
    """
    if goal not in RULES:
        return None, set()
    missing = RULES[goal] - symptoms
    return (not missing), missing


def ask(prompt, default):
    """Read user input; fall back to the default on empty input or no stdin."""
    try:
        value = input(prompt).strip()
        return value if value else default
    except (EOFError, KeyboardInterrupt):
        print()
        return default


def parse_symptoms(text):
    """Turn 'Sore Throat, fever' into {'sore_throat', 'fever'}."""
    return {s.strip().lower().replace(" ", "_")
            for s in text.split(",") if s.strip()}


def find_disease(name):
    """Case-insensitive lookup of a disease name in RULES."""
    lookup = {k.lower(): k for k in RULES}
    return lookup.get(name.strip().lower(), name.strip())


def main():
    known = sorted(set().union(*RULES.values()))
    print("Known symptoms:", ", ".join(known))

    symptoms = parse_symptoms(
        ask("Enter symptoms (comma separated) "
            "[default: fever, cough, sore throat]: ",
            "fever, cough, sore throat"))
    print("Symptoms entered:", sorted(symptoms))

    unknown = symptoms - set(known)
    if unknown:
        print("Note: these symptoms are not used by any rule:", sorted(unknown))

    print("\nForward Chaining:")
    found = forward_chaining(symptoms)
    if found:
        for disease in found:
            print("Possible:", disease)
    else:
        print("No disease matches the given symptoms.")

    print("\nBackward Chaining:")
    goal = find_disease(ask("Enter suspected disease [default: Flu]: ", "Flu"))
    supported, missing = backward_chaining(goal, symptoms)
    if supported is None:
        print("Unknown disease:", goal, "| Known:", ", ".join(RULES))
    elif supported:
        print("Goal", goal, "is supported by the symptoms.")
    else:
        print("Goal", goal, "is not supported. Missing symptoms:",
              sorted(missing))


if __name__ == "__main__":
    main()
