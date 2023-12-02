#!/usr/bin/python3
""" Fetches https:*****"""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body res:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
