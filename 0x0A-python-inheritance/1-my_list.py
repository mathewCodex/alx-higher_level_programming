#!/usr/bin/python3
"""Def print  list in ascending order
     and inheritance from class myList"""


class MyList(list):
    """Implementing sorted printing"""
    def print_sorted(self):
        """ascending order"""
        print(sorted(self))
