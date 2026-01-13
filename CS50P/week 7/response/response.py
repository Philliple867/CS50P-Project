from validator_collection import checkers
import sys

def main():
    # Read email from user input
    email = input("What's your email address? ")
    # Validate and print result
    if validate(email):
        print("Valid")
    else:
        print("Invalid")

def validate(s):
    # Use validator-collection to check if s is a valid email
    return checkers.is_email(s)

if __name__ == "__main__":
    main()
