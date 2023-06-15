#!/usr/bin/python3
def add_integer(a, b=98):
    """doc function"""
    
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif isinstance(b, float):
        a = int(a)

    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    elif isinstance(b, float):
        b = int(b)

    return a + b
