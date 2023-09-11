#!/usr/bin/python3
"""Def a Rect subclass square"""
Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """Rep a sqr"""

    def __init__(self, size):
        """Init a new sqr"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
