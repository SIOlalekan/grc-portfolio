from pathlib import Path
import yaml

CONTROL_LIBRARY = Path("controls/control-library.yml")

STATUS_SCORES = {
    "compliant": 1.0,
    "partially_compliant": 0.5,
    "non_compliant": 0.0,
    "not_applicable": None,
}

SEVERITY_WEIGHTS = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4,
}


def load_controls():
    with open(CONTROL_LIBRARY, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return data.get("controls", [])


def ask_status(control):
    print("\n" + "=" * 70)
    print(f"{control['control_id']} | {control['title']}")
    print(f"Framework: {control['framework']}")
    print(f"Severity: {control['severity'].upper()}")
    print()
    print(control["assessment_question"])
    print()
    print("1. Compliant")
    print("2. Partially compliant")
    print("3. Non-compliant")
    print("4. Not applicable")

    choices = {
        "1": "compliant",
        "2": "partially_compliant",
        "3": "non_compliant",
        "4": "not_applicable",
    }

    while True:
        answer = input("Select 1-4: ").strip()

        if answer in choices:
            return choices[answer]

        print("Invalid selection. Please enter 1, 2, 3 or 4.")


def calculate_score(results):
    total_weight = 0
    achieved_weight = 0

    for result in results:
        status = result["status"]

        if status == "not_applicable":
            continue

        severity = result["severity"]
        weight = SEVERITY_WEIGHTS.get(severity, 1)
        score = STATUS_SCORES[status]

        total_weight += weight
        achieved_weight += score * weight

    if total_weight == 0:
        return 0

    return round((achieved_weight / total_weight) * 100, 1)


def print_report(results):
    score = calculate_score(results)

    compliant = sum(
        1 for item in results if item["status"] == "compliant"
    )

    partial = sum(
        1 for item in results if item["status"] == "partially_compliant"
    )

    non_compliant = sum(
        1 for item in results if item["status"] == "non_compliant"
    )

    not_applicable = sum(
        1 for item in results if item["status"] == "not_applicable"
    )

    print("\n")
    print("=" * 70)
    print("TRUSTREADY GRC ASSESSMENT REPORT")
    print("=" * 70)

    print(f"\nOverall weighted compliance score: {score}%")

    print("\nAssessment summary")
    print(f"Compliant:             {compliant}")
    print(f"Partially compliant:   {partial}")
    print(f"Non-compliant:         {non_compliant}")
    print(f"Not applicable:        {not_applicable}")

    gaps = [
        result
        for result in results
        if result["status"] in {
            "partially_compliant",
            "non_compliant",
        }
    ]

    if gaps:
        print("\nPriority gaps")
        print("-" * 70)

        gaps.sort(
            key=lambda item: SEVERITY_WEIGHTS.get(
                item["severity"], 1
            ),
            reverse=True,
        )

        for gap in gaps:
            print(
                f"{gap['control_id']} | "
                f"{gap['severity'].upper()} | "
                f"{gap['status']} | "
                f"{gap['title']}"
            )

    else:
        print("\nNo compliance gaps identified.")


def main():
    controls = load_controls()

    if not controls:
        print("No controls were found in the control library.")
        return

    print("=" * 70)
    print("TRUSTREADY GRC ASSESSMENT ENGINE")
    print("=" * 70)

    print(f"\nLoaded {len(controls)} controls.")

    results = []

    for control in controls:
        status = ask_status(control)

        results.append(
            {
                "control_id": control["control_id"],
                "title": control["title"],
                "framework": control["framework"],
                "severity": control["severity"],
                "status": status,
            }
        )

    print_report(results)


if __name__ == "__main__":
    main()
