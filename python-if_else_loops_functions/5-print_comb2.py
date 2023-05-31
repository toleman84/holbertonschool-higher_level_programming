#!/usr/bin/python3
for number in range(99):
    print("{0:0=2d}".format(number), end=", ")
    if number == 98:
        print("99")
