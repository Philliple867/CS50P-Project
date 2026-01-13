from numb3rs import validate

def test_format():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False

def test_range():
    assert validate("256.0.0.1") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.1.1000") == False
    assert validate("cat.dog.rat.pig") == False
