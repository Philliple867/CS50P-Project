import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(10)
    assert jar2.capacity == 10

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(6)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.withdraw(8)
