#!/usr/bin/python3
"""Def a sqr Class"""
from models.rectangle import  Rectangle



class Square(Rectangle):
    """Rep a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init a new square
        Args:
            size (int): the size of the new sqr
            x (int): The x coor
            y (int): ---
            id (int): the identity
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the Square
        Args:
            *args (ints): New attr val
                - 1st args rep id attr
                - 2nd args rep size attr
                - 3rd args rep x attr
                - 4th args rep y attr
            **kwargs (dict): New key/value pairs
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Ret the dict rep of the square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() rep of the Sqr"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
