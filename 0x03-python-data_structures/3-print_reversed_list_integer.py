#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    reverseList = []
    for i in range(len(my_list)):
        reverseList.append(my_list[i]) 
    print("{:d}".format(int(reverseList)))
