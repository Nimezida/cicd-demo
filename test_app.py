from app import add, subtract, multiply, is_even

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_is_even():
    assert is_even(4) == True
    assert is_even(3) == False