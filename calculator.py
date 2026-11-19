import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return square_root(a^2+b^2)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithm requires a positive argument and a positive base other than 1.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b