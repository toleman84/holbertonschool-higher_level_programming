#!/usr/bin/python3
def uppercase(str):
    for to_up in str:
        if ord(to_up) >= 97 and ord(to_up) <= 122:
            to_up = chr(ord(to_up) - 32)
        print("{}".format(to_up), end="")
    print("")
