#!/usr/bin/python3
"""A function that convert a str to a txt"""
def write_file(filename="", text=""):
    """Writing a str to a utf-8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
