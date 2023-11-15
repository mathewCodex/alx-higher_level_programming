#!/usr/bin/python3
"""func that def a class student"""


class Student:
    """Rep a student"""
    def __init__(self, first_name, last_name, age):
        """Init a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictinonary of the student rep"""
        return self.__dict__
