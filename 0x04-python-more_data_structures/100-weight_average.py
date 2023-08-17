#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for tups in myList:
        num += tup[0] * tup[i]
        den += tup[1]

    return (num / den)
