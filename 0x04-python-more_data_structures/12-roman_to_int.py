#!/usr/bin/python3
def to_substract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            to_sub += n

    return (max_list - to_sub)

def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return 0
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    int_val = 0
    for i in range(len(roman_string)):
        if i > 0 and roman[roman_string[i]] > roman[roman_string[i - 1]]:
            int_val += roman[roman_string[i]] - \
                2 * roman[roman_string[i - 1]]
        else:
            int_val += roman[roman_string[i]]
    return int_val
