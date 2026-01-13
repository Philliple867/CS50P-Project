import sys
import os

def main():
    # Check if exactly one command-line argument is provided
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if the file has a .py extension
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Check if the file exists
    if not os.path.exists(filename):
        sys.exit("File does not exist")

    # Count the lines
    print(count_lines(filename))

def count_lines(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            # Strip whitespace to check if the line is empty or a comment
            stripped_line = line.lstrip()
            if stripped_line and not stripped_line.startswith("#"):
                count += 1
    return count

if __name__ == "__main__":
    main()
