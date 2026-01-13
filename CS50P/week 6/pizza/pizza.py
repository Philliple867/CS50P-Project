import sys
import csv
import os
from tabulate import tabulate

def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check file extension
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Check if file exists
    if not os.path.exists(filename):
        sys.exit("File does not exist")

    # Read CSV and print table
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            table = []
            for row in reader:
                table.append(row)

            # Print the table using grid format
            print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
