#!/usr/bin/python3
for number in range(0, 100):
    if number < 99:
        print("{}".format(number), end="")
        print(", ", end="")
    elif number == 98:
        print("", end="")
