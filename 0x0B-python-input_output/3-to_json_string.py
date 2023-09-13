#!/usr/bin/python3
"""Def a str-to-JSON func"""
import json


def to_json_string(my_obj):
    """Return the JSON rep of a str obj"""
    return json.dumps(my_obj)
