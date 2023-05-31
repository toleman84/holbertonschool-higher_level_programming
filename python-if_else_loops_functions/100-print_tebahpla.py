#!/usr/bin/python3
for letters in range(122, 96, -1):
    print(chr(letters) if letters % 2 == 0 else chr(letters-32), end="")
