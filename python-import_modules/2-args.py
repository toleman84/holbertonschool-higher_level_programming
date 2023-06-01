#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lengh = len(sys.argv)
    arg = sys.argv

    if lengh == 1:
        print("0 arguments.")
    elif lengh == 2:
        print("{} argument:".format(lengh - 1))
        for lengh_arg in range(1, lengh):
            print("{}: {}".format(lengh_arg, arg))
    elif lengh > 2:
        print("{} arguments:".format(lengh - 1))
        for lengh_arg in range(1, lengh):
            print("{}: {}".format(lengh_arg, argv[lengh_arg]))
