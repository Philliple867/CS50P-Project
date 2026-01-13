import sys
from datetime import date
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        # Validate date format YYYY-MM-DD
        dob = date.fromisoformat(birth_date)
        today = date.today()

        # Calculate minutes
        diff = today - dob
        total_minutes = diff.days * 24 * 60

        # Convert to words without "and"
        output = p.number_to_words(total_minutes, wantlist=False)
        output = output.replace(" and ", " ").capitalize()
        print(f"{output} minutes")

    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
