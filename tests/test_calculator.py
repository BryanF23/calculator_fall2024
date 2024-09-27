"""
This module contains tests for the Calculator class, testing
its basic arithmetic methods: add, subtract, multiply, and divide.
"""

import pytest

# Parameterized tests for the add method
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
])
def test_add(calc, a, b, expected):
    """
    Test the add method of the Calculator class.
    
    Args:
        calc: Instance of the Calculator class.
        a: First number to add.
        b: Second number to add.
        expected: Expected result of the addition.
    """
    assert calc.add(a, b) == expected

# Parameterized tests for the subtract method
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-1, -1, 0),
    (0, 0, 0),
    (2.5, 1.0, 1.5),
])
def test_subtract(calc, a, b, expected):
    """
    Test the subtract method of the Calculator class.
    
    Args:
        calc: Instance of the Calculator class.
        a: First number.
        b: Number to subtract from 'a'.
        expected: Expected result of the subtraction.
    """
    assert calc.subtract(a, b) == expected

# Parameterized tests for the multiply method
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, -1, 1),
    (0, 5, 0),
    (1.5, 2, 3.0),
])
def test_multiply(calc, a, b, expected):
    """
    Test the multiply method of the Calculator class.
    
    Args:
        calc: Instance of the Calculator class.
        a: First number to multiply.
        b: Second number to multiply.
        expected: Expected result of the multiplication.
    """
    assert calc.multiply(a, b) == expected

# Parameterized tests for the divide method
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-9, -3, 3),
    (7.5, 2.5, 3.0),
])
def test_divide(calc, a, b, expected):
    """
    Test the divide method of the Calculator class.
    
    Args:
        calc: Instance of the Calculator class.
        a: Dividend.
        b: Divisor.
        expected: Expected result of the division.
    """
    assert calc.divide(a, b) == expected

# Test division by zero
def test_divide_by_zero(calc):
    """
    Test that dividing by zero raises a ZeroDivisionError.
    
    Args:
        calc: Instance of the Calculator class.
    """
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)
