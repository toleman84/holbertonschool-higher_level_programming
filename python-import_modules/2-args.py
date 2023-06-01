#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    lengh = len(sys.argv)

    if lengh == 1:
        print("0 arguments.")
    elif lengh > 1:
        print("{} argument:".format(lengh))
