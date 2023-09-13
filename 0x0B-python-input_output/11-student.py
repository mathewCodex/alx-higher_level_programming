#!/usr/bin/python3
"""The student class def a student"""



class Student:
    def __init__(self, first_name, last_name, age):
        """instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict rep of student
        instance"""
        if type(attrs) == list and all(type(elem) == str for elem in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace all attr of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)
