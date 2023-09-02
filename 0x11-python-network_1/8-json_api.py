#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}
    response = requests.post(url, data=data)
    try:
        content = response.json()
        if len(content) > 0:
            print("[{}] {}".format(content.get('id'), content.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
