import os
import pickle
import csv

try:
    from sklearn.linear_model import LinearRegression  # type: ignore[import]
except ImportError as exc:
    raise ImportError(
        "scikit-learn is required to train the model. Install it with 'pip install scikit-learn'"
    ) from exc


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

csv_path = os.path.join(
    BASE_DIR,
    "dataset",
    "student_data.csv"
)

model_path = os.path.join(
    BASE_DIR,
    "models",
    "study_hours_model.pkl"
)

X = []
y = []

with open(csv_path, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        X.append([
            float(row["attendance"]),
            float(row["previous_marks"]),
            float(row["target_marks"])
        ])
        y.append(float(row["study_hours"]))

model = LinearRegression()

model.fit(
    X,
    y
)

with open(
    model_path,
    "wb"
) as file:

    pickle.dump(
        model,
        file
    )

print(
    "AI model trained successfully!"
)