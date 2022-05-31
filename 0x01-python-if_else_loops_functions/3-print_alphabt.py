#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 'q':
        continue
    elif letter == 'e':
        continue
    else:
        print("{}".format(chr(letter)), end="")
