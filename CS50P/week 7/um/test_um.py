from um import count

def test_single_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_multiple_um():
    assert count("um, um, UM") == 3
    assert count("Um, hello, um, world") == 2

def test_word_with_um():
    assert count("yummy") == 0
    assert count("instrumentation") == 0
    assert count("album") == 0
