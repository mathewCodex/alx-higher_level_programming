#!/usr/bin/python3
"""A function that appends a str to the end of txt file"""



def append_write(filename="", text=""):
    """appends a string at the end of a text file
    and returns the number of characters added"""
    with open(filename, mode="a+", encoding="utf-8") as f:
        return f.write(text)
