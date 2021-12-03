"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of num1 and num2."""
    total = num1 + num2
    return total


def subtract(num1, num2):
    """Return the value of num1 minus num2."""
    total = num1 - num2
    return total

def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""
    total = num1 * num2
    return total

def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""
    total = num1 / num2
    return total

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    total = num1 ** num2
    return total


def square(num1):
    """Return the square of num1."""
    total = power(num1, 2)

    return total

def cube(num1):
    """Return the cube of num1."""
    total = num1 * num1 * num1
    return total



def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    total = num1 % num2
    return total

def add_mult(num1, num2, num3):
    """Return the sum of num1, num2 and num3."""
    addition = add(num1,num2)
    total = multiply(addition, num3)
    
    return total

def add_cubes(num1, num2):
    cube_1 = cube(num1)
    cube_2 = cube(num2)
    total = cube_1 + cube_2
    return total
