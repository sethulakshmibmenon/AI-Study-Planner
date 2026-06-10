import csv
import pickle
import os


def predict_study_hours(
    attendance,
    previous_marks,
    target_marks
):

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    model_path = os.path.join(
        base_dir,
        "models",
        "study_hours_model.pkl"
    )

    with open(
        model_path,
        "rb"
    ) as file:

        model = pickle.load(file)

    input_data = [[
        attendance,
        previous_marks,
        target_marks
    ]]

    prediction = model.predict(
        input_data
    )

    return round(
    float(prediction[0]),
    1
)


def calculate_gap(
    previous_marks,
    target_marks
):

    return max(
        0,
        target_marks - previous_marks
    )


def calculate_priority(
    gap,
    attendance
):

    priority = (
        gap +
        ((100 - attendance) / 2)
    )

    return round(
        priority,
        2
    )


def get_recommended_hours(
    attendance,
    previous_marks,
    target_marks
):

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    csv_path = os.path.join(
        base_dir,
        "dataset",
        "study_rules.csv"
    )

    with open(
        csv_path,
        mode="r"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if (
                float(row["attendance_min"])
                <= attendance <=
                float(row["attendance_max"])
                and
                float(row["previous_min"])
                <= previous_marks <=
                float(row["previous_max"])
                and
                float(row["target_min"])
                <= target_marks <=
                float(row["target_max"])
            ):

                return int(
                    row["recommended_hours"]
                )

    return 1


def analyze_subject(
    subject_name,
    attendance,
    previous_marks,
    target_marks
):

    gap = calculate_gap(
        previous_marks,
        target_marks
    )

    priority = calculate_priority(
        gap,
        attendance
    )

    rule_hours = get_recommended_hours(
        attendance,
        previous_marks,
        target_marks
    )

    ai_hours = predict_study_hours(
        attendance,
        previous_marks,
        target_marks
    )

    final_hours = round(
        (rule_hours + ai_hours) / 2
    )

    return {
        "subject": subject_name,
        "attendance": attendance,
        "previous_marks": previous_marks,
        "target_marks": target_marks,
        "gap": gap,
        "priority": priority,
        "rule_hours": rule_hours,
        "ai_hours": ai_hours,
        "recommended_hours": final_hours
    }