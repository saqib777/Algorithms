import pytest
from gcd_lcm import gcd_recursive, gcd_iterative, lcm, gcd_multiple, lcm_multiple, extended_gcd


def test_gcd_basic():
    assert gcd_recursive(48, 18) == 6
    assert gcd_iterative(48, 18) == 6

def test_gcd_coprime():
    assert gcd_recursive(7, 13) == 1

def test_gcd_same_number():
    assert gcd_recursive(12, 12) == 12

def test_gcd_one():
    assert gcd_recursive(1, 99) == 1

def test_gcd_zero():
    assert gcd_recursive(0, 5) == 5
    assert gcd_recursive(5, 0) == 5

def test_gcd_both_match():
    for a, b in [(48,18),(100,75),(36,24),(17,5)]:
        assert gcd_recursive(a,b) == gcd_iterative(a,b)

def test_lcm_basic():
    assert lcm(4, 6) == 12
    assert lcm(12, 18) == 36

def test_lcm_coprime():
    assert lcm(7, 13) == 91

def test_lcm_same():
    assert lcm(5, 5) == 5

def test_gcd_multiple():
    assert gcd_multiple([12, 18, 24]) == 6
    assert gcd_multiple([7, 14, 21]) == 7

def test_lcm_multiple():
    assert lcm_multiple([4, 6, 10]) == 60
    assert lcm_multiple([2, 3, 4])  == 12

def test_extended_gcd():
    g, x, y = extended_gcd(35, 15)
    assert g == 5
    assert 35*x + 15*y == g

def test_extended_gcd_coprime():
    g, x, y = extended_gcd(3, 7)
    assert g == 1
    assert 3*x + 7*y == 1

@pytest.mark.parametrize("a, b, expected", [
    (12, 8, 4),
    (100, 75, 25),
    (17, 5, 1),
    (0, 9, 9),
])
def test_parametrized(a, b, expected):
    assert gcd_iterative(a, b) == expected
