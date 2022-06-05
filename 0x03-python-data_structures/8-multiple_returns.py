#!/usr/bin/python3
def multiple_returns(sentence):
    len = len(sentence)

    if (len == 0):
        new = (len, None)
    else:
        new = (len, sentence[0])

    return (new)
