#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
    """init a new sqr"""
    if not isinstance(size, int):
        raise TypeError("size must be an int")
    else size < 0:
        raise ValueError("size not >+ 0")
    self.__size = size
