#!/usr/bin/python3
"""return py data structure"""
import json


def from_json_string(my_str):
    """ret an object(python data struct) 
    rep by a json string"""
    data = json.loads(my_str)
    return data
