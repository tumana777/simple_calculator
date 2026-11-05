import pytest

from calculator import add, subtract, multiply, divide, square, power

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_square():
    assert square(2) == 4

def test_power():
    assert power(2, 3) == 7