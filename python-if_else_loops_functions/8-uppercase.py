#!/usr/bin/python3
def uppercase(str):
    for to_up in str:
        if to_up >= 97 and to_up <= 122:
            to_up = chr(ord(to_up) - 32)
        print("{}".format(to_up), end="")
    print("")
