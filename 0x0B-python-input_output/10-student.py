#!/usr/python3
"""Student class def"""


class Student:
    """Def a student"""
    def __init__(self, first_name, last_name, age):
        """instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retreives a dict rep of Student if attr 
        is alist of stings, only attr name contained in the list"""
        if type(attrs) == list and all(type(elem) == str for elem in attrs):
           return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__ 
