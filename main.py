from utils.planner import analyze_subject
from utils.timetable import generate_timetable


def get_subject_data():

    subjects = []

    number_of_subjects = int(
        input("Enter number of subjects: ")
    )

    print()

    for i in range(number_of_subjects):

        print(f"Subject {i + 1}")

        subject_name = input(
            "Subject Name: "
        )

        attendance = float(
            input("Attendance (%): ")
        )

        previous_marks = float(
            input("Previous Marks: ")
        )

        target_marks = float(
            input("Target Marks: ")
        )

        print()

        analysis = analyze_subject(
            subject_name,
            attendance,
            previous_marks,
            target_marks
        )

        subjects.append(
            analysis
        )

    return subjects


def display_subject_analysis(subjects):

    print("\n" + "=" * 50)
    print("SUBJECT ANALYSIS")
    print("=" * 50)

    for subject in subjects:

        print(f"\nSubject: {subject['subject']}")

        print(
            f"Attendance: {subject['attendance']}%"
        )

        print(
            f"Previous Marks: {subject['previous_marks']}"
        )

        print(
            f"Target Marks: {subject['target_marks']}"
        )

        print(
            f"Gap: {subject['gap']}"
        )

        print(
            f"Priority Score: {subject['priority']}"
        )

        print(
            f"Rule-Based Hours: "
            f"{subject['rule_hours']} hrs/week"
        )

        print(
            f"AI Predicted Hours: "
            f"{subject['ai_hours']} hrs/week"
        )

        print(
            f"Final Recommended Hours: "
            f"{subject['recommended_hours']} hrs/week"
        )


def display_timetable(timetable):

    print("\n" + "=" * 50)
    print("WEEKLY STUDY TIMETABLE")
    print("=" * 50)

    for day, sessions in timetable.items():

        print(f"\n{day}")

        if sessions:

            for subject, hours in sessions.items():

                print(
                    f"  {hours} Hour(s) → {subject}"
                )

        else:

            print(
                "  No Study Session"
            )


def main():

    print("\nSMART STUDY PLANNER")
    print("=" * 50)

    subjects = get_subject_data()

    subjects.sort(
        key=lambda x: x["priority"],
        reverse=True
    )

    display_subject_analysis(
        subjects
    )

    timetable = generate_timetable(
        subjects
    )

    display_timetable(
        timetable
    )


if __name__ == "__main__":
    main()