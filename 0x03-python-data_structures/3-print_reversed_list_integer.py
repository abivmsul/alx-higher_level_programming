#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    reverseList = []
    for i in range(len(my_list)):
        reverseList[length] = my_list[i]
        length -= 1
    print("{:d}".format(int(reverseList)))
