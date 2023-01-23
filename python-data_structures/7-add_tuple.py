#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    try:
        a = tuple_a[0]
    except:
        a = 0
    try:
        b = tuple_b[0]
    except:
        b = 0

    try:
        c = tuple_a[1]
    except:
        c = 0
    try:
        d = tuple_b[1]
    except:
        d = 0

    return((a + b), (c + d))
