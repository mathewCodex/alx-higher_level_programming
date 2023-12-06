#!/usr/bin/python3
"""Man's Uses github api to display a github Id based on a given credentials
Usage: ./10-my_github.py <GitHub username> <Github password>
 - Man it finna be the basic Authentication to access the ID.
 """
 import sys
 import requests
 from requests.auth import HTTPBasicAuth


 if __name__ == "__main__":
     auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
     r = requests.get("https://api.github.com/user", auth=auth)
     print(r.json().get("id"))
