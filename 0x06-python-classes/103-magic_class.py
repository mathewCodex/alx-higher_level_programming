#!/usr/bin/python3

"""Def a MagicClass Mathcing
    exactly a bytecode provided by HB
"""
import math

class MagicClass:
    """Rep aCircle"""

    def __int__(self, radius=0):
    """Init a Magic class
    Args:
        radius (float or int): The rad of 
     new Magic class"""
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass"""
        return (2 * math.pi * self.__radius)
