import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # \b is a word boundary, ensuring we only match "um" as a whole word
    # re.IGNORECASE makes it match "Um", "UM", or "um"
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
