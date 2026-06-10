# AI-Powered Smart Study Planner
AI-Powered Smart Study Planner is a Python-based project that helps students create personalized weekly study schedules.

## Features
   ✅ Analyze subjects based on attendance, previous marks, and target marks
   ✅ Predict recommended study hours using Linear Regression
   ✅ Calculate priority scores for subjects
   ✅ Generate a weekly study timetable automatically
   ✅ Combine AI predictions with rule-based recommendations

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* Machine Learning (Linear Regression)

## Project Structure

AI-Study-Planner/

├── dataset/

│ ├── student_data.csv

│ └── study_rules.csv

├── models/

│ └── study_hours_model.pkl

├── training/

│ └── train_model.py

├── utils/

│ ├── planner.py

│ └── timetable.py

├── main.py

├── requirements.txt

└── README.md

---

## How It Works

1. User enters subject details
2. System calculates performance gap
3. AI model predicts study hours
4. Rule-based system validates recommendations
5. Final study hours are generated
6. Weekly timetable is automatically created

---

## Machine Learning Model

This project uses Linear Regression to predict study hours based on:

- Attendance
- Previous Marks
- Target Marks

The model is trained using historical study-performance data.

---
