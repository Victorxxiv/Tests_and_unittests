# test_math_utils.py
import pytest
from math_utils import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.fixture
def numbers():
    return (2, 3)

def test_add(numbers):
    a, b = numbers
    assert add(a, b) == 5
