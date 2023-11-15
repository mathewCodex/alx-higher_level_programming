#!/usr/binpython3
"""Def a class myInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Override == operator"""
        return self.real != value

    def __ne__(self, value):
        """override != operator with == behaviour"""
        return self.real == value
