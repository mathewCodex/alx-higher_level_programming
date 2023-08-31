#!/usr/bin/python3

"""Define a class sqr."""


class Square:
    """Rep a Sqr"""

    def __int__(self, size=0):
        """Init a new Sqr
        Args:
            size (int): The size of the new sqr
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of sqr"""
        return (self.__size * self.__size)
