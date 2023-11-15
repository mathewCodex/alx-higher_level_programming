#!/usr/bin/python3
def weight_average(my_list=[]):
    """ return weighted average """
    totalNum = 0
    den = 0
    if my_list == []:
        return 0
    for elem in myList:
        totalNum += elem[0] * elem[1]
        den += elem[1]

    return (num / den)
