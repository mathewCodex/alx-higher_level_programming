#!/usr/bin/python3

"""A class name square"""

class Square:
    """Rep a Sqr"""

    def __int__(self, size=0):
        """Init a new square
        Args:
            size (int): The size of the new sqr
        """
        self.size = size

    @property
    def size(self):
        """Get/set curr sqr"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Def the == comparison to a sqr"""
    return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Def the < comparison to a sqr"""
        return self.area() < other.area()


    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
