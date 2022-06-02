#!/usr/bin/python3
if __name__ == "__main__":
    length = len(args)
    sum = 0
    for i in range(length):
        sum += int(args[i])
    print("{}".format(sum))
