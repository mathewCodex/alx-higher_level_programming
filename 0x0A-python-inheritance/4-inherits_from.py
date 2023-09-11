#!/usr/bin/python3
"""Def an inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checkif an object is an inheritance of a class"""
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
