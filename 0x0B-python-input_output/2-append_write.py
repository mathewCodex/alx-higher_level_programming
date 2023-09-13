#!/usr/bin/python3
"""A function that appends a str to the end of UTF8 txt file"""



def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
