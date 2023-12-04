#!usr/bin/python3
"""Fetches a url using urllib package
"""
import urllib.request
with urllib.request.urlopen("https://intranet.hbtn.io/status") as res:
    data = res.read()
    print("Body response:")
    print("	- type:", type(data))
    print("     - content:", data)
    print("     - utf8 content:", data.decode('utf-8'))
