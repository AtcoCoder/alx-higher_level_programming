#!/usr/bin/python3
"""Fetches 'https://alx-intranet.hbtn.io/status'"""
from urllib import request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
