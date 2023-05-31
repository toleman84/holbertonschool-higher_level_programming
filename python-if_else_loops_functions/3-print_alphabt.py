#!/usr/bin/python3
for abc in range(97, 123):
    if abc not in "113, 101":
        print("{}".format(chr(abc)), end="")
