#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    sum = add(a, b)
    print("{} + {} = {}".format(a, b, sum))

    res = sub(a, b)
    print("{} - {} = {}".format(a, b, res))

    multi = mul(a, b)
    print("{} * {} = {}".format(a, b, multi))

    div2 = div(a, b)
    print("{} / {} = {}".format(a, b, div2))
