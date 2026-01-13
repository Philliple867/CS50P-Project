import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")

def convert(s):
    # Regex to capture hours, minutes (optional), and AM/PM for both start and end times
    regex = r"^(\d{1,2})(?::([0-5]\d))? (AM|PM) to (\d{1,2})(?::([0-5]\d))? (AM|PM)$"
    if matches := re.search(regex, s):
        groups = matches.groups()

        # Convert start time and end time
        time1 = format_time(groups[0], groups[1], groups[2])
        time2 = format_time(groups[3], groups[4], groups[5])

        return f"{time1} to {time2}"
    else:
        raise ValueError

def format_time(hour, minute, period):
    h = int(hour)
    if h > 12:
        raise ValueError

    if period == "PM" and h != 12:
        h += 12
    elif period == "AM" and h == 12:
        h = 0

    m = int(minute) if minute else 0
    return f"{h:02}:{m:02}"

if __name__ == "__main__":
    main()
