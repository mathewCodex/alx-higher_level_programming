#!/usr/bin/python3
"""Def a class Rect that inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry



class Rectangle(BaseGeometry):
    """Rep a rect using BaseGeometry"""

    def __init__(self, width, height):
        """Init a new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
