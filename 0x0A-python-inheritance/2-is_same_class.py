#!/usr/bin/python3
"""Def a class-checking func"""


def is_same_class(obj, a_class):
    """Check if an object is exact to an instance"""
    if type(obj) == a_class:
        return True
    return False
