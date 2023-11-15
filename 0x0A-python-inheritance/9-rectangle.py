#!/usr/bin/python3
"""Def a class Rectangle that inherits from BaseGeometry"""


class BaseGeometry:
    """public instance method"""

    def area(self):
        """calc area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate val"""
        x = type(value)
        if x is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rect inherits from BGY"""

    def __init__(self, width, height):
        """initialize of privates"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """implement area"""
        return self.__width * self.height

    def __str__(self):
        """return a str rep"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
