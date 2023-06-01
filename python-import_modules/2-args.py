#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    lengh = len(sys.argv)

    if lengh == 0:
        print("0 arguments.")
    else:
        print("{} argument:".format(lengh))
