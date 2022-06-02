#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(argv[0]))
    elif length > 1:
        print("{} arguments:".format(length))
        for i in range(0,length + 1) :
            print("{}: {}".format(argv[i]))
