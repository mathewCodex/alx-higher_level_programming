#!/usr/bin/python3
"""Json file writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Write an obj to atext file using JSON rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
