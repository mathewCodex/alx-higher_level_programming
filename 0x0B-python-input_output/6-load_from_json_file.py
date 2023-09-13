#!/usr/bin/python3
"""Writes an obj from a json file"""
import json


def load_from_json_file(filename):
    """create an obj from a json file"""
    with open(filename, "r") as f:
    return json.load(f)
