from project import add_transaction, calculate_balance, format_currency

def test_add_transaction():
    data = []
    assert add_transaction(data, "Coffee", "5.5") == [{"item": "Coffee", "amount": 5.5}]
    assert add_transaction(data, "Invalid", "abc") == [{"item": "Coffee", "amount": 5.5}]

def test_calculate_balance():
    data = [{"item": "Salary", "amount": 1000}, {"item": "Rent", "amount": -400}]
    assert calculate_balance(data) == 600

def test_format_currency():
    assert format_currency(1000) == "$1,000.00"
    assert format_currency(5.5) == "$5.50"
