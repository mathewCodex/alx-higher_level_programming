#!/usr/bin/python3
"""Def a class-check func"""


def is_same_class(obj, a_class):
    """check for an instance"""
    if type(obj) == a_class:
        return True
    return False        
