import sys
import csv

def main():
    transactions = []
    print("--- Personal Finance Manager ---")
    while True:
        try:
            action = input("Action (add/show/exit): ").lower().strip()
            if action == "add":
                item = input("Item: ")
                amount = input("Amount: ")
                transactions = add_transaction(transactions, item, amount)
            elif action == "show":
                balance = calculate_balance(transactions)
                print(f"Current Balance: {format_currency(balance)}")
            elif action == "exit":
                sys.exit("Data saved (simulated). Goodbye!")
        except EOFError:
            break

def add_transaction(data, item, amount):
    try:
        amount = float(amount)
        data.append({"item": item, "amount": amount})
        return data
    except ValueError:
        print("Invalid amount!")
        return data

def calculate_balance(data):
    return sum(t['amount'] for t in data)

def format_currency(value):
    return f"${value:,.2f}"

if __name__ == "__main__":
    main()
