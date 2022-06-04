#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    le = len(my_list)
    reverseList = []
    for i in range(len(my_list)):
        le -= 1
        reverseList.append(my_list[le]) 
    for j in range(len(reverseList)):
        print("{:d}".format(int(reverseList[j])))
