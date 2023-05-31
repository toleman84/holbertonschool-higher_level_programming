#!/usr/bin/python3
def uppercase(str):
    for to_up in str:
        to_up = chr(ord((str) - 32))
        print("{}".format(to_up), end="")
