#!/usr/bin/python3
"""check if object is instance of class or subclass"""


def is_kind_of_class(obj, a_class):
    """Check if an objects ia an instance"""
    x = isinstance(obj, a_class)
    if x:
        return True
    return False
