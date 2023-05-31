#!/usr/bin/python3
for letters in range(122, 96, -1):
    if letters % 2 == 0:
        print(chr(letters))
    else:
        letter = letters - 32
        print(chr(letter))
