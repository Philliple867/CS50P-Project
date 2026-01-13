from twttr import shorten

def test_lowercase():
    # Test lowercase vowels
    assert shorten("twitter") == "twttr"

def test_uppercase():
    # Test uppercase vowels
    assert shorten("PYTHON") == "PYTHN"

def test_numbers():
    # Test that numbers are not removed
    assert shorten("12345") == "12345"

def test_punctuation():
    # Test that punctuation is not removed
    assert shorten("hello, world!") == "hll, wrld!"
