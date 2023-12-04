#!/usr/bin/python3
"""DIsplays the X-req-id header var of a req to a given URL.
Using = ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
