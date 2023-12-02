#!/usr/bin/python3
"""Dis the X-re-id header var of a req"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.header.get("X-Request-Id"))
