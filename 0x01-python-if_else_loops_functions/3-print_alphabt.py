#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 113:
        continue
    elif letter == 101:
        continue
    else:
        print("{}".format(chr(letter)), end="")
