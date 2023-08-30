#!/usr/bin/python3

"""Define a class sqr."""

class Square:
    """rep a square"""
    def __init__(self, size=0):
        """init a new sqr
        Args:
            size (int): The size of new sqr
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the cur area of sqr"""
        return (self.__size * self.__size)
