#!/usr/bin/python3
"""Def a rect subclass sqr"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rep a sqr"""

    def __init__(self, size):
        """Init  a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
