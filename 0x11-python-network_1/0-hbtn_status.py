#!/usr/bin/python3
# Fetches 'https://alx-intranet.hbtn.io/status'
from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

output = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}"""

with request.urlopen(url) as response:
    content = response.read()
    print(output.format(type(content), content, content.decode('utf-8')))
