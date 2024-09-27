"""
This module contains basic arithmetic operations for testing.
"""

def addition(a, b):
    """
    Return the sum of two numbers.
    
    Args:
        a (float): First number.
        b (float): Second number.
        
    Returns:
        float: The sum of `a` and `b`.
    """
    return a + b

def subtraction(a, b):
    """
    Return the difference between two numbers.
    
    Args:
        a (float): First number.
        b (float): Second number.
        
    Returns:
        float: The result of `a` minus `b`.
    """
    return a - b

def multiplication(a, b):
    """
    Return the product of two numbers.
    
    Args:
        a (float): First number.
        b (float): Second number.
        
    Returns:
        float: The product of `a` and `b`.
    """
    return a * b

def division(a, b):
    """
    Return the division of two numbers.
    
    Args:
        a (float): First number.
        b (float): Second number.
        
    Returns:
        float: The result of `a` divided by `b`.
        
    Raises:
        ZeroDivisionError: If `b` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
