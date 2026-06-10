DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]


def generate_timetable(subjects):

    timetable = {
        day: {}
        for day in DAYS
    }

    remaining_hours = {}

    for subject in subjects:

        remaining_hours[
            subject["subject"]
        ] = subject[
            "recommended_hours"
        ]

    day_index = 0

    while any(
        hours > 0
        for hours in remaining_hours.values()
    ):

        for subject in subjects:

            name = subject["subject"]

            if remaining_hours[name] > 0:

                day = DAYS[day_index]

                if name not in timetable[day]:

                    timetable[day][name] = 0

                timetable[day][name] += 1

                remaining_hours[name] -= 1

                day_index = (
                    day_index + 1
                ) % 7

    return timetable