#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    sum = 0
    for i in range(length):
        sum += int(sys.argv[i])
    print("{}".format(sum))
