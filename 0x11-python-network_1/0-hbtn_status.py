#!/usr/bin/python3
# Fetches 'https://alx-intranet.hbtn.io/status'
from urllib import request

output = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}"""


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    with request.urlopen(url) as response:
        content = response.read()
        print(output.format(type(content), content, content.decode('utf-8')))
