import math

def power(a, b): 
    return a ** b 

def factorial(n): 
    if n < 0 : 
        raise ValueError("""Factorial is not defined for negative numbers""")
    return math.factorial(n)

def square_root(n):
    if n < 0:
        raise ValueError("Square root of negative number is not real")
    return math.sqrt(n)