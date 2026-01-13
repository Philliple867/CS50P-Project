import sys
import csv
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        sys.exit(f"Could not read {input_file}")

    updated_data = []

    try:
        with open(input_file, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                last, first = row["name"].split(", ")
                updated_data.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_data)

if __name__ == "__main__":
    main()
