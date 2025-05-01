class DayException(Exception):
    def __init__(self, day_of_week):
        self.day = day_of_week

    def __str__(self):
        return self.day


def analyze_day(input_day):
    week = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    if 0 < input_day <= len(week):
        return week[input_day-1]
    else:
        raise DayException(f"Day out of range: {input_day}")


try:
    day = int(input("Enter a day (1-7):"))
    print(analyze_day(day))
except DayException as e:
    print("Day error:", e)
except ValueError as e:
    print("Value error:", e)
