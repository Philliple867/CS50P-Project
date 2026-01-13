from bank import value

def test_value_zero():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0

def test_value_twenty():
    assert value("hey") == 20
    assert value("How you doing?") == 20

def test_value_hundred():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
