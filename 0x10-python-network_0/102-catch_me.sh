#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing you got me!
curl -s -X PUT -H "Origin: HolbertonSchool" -d -L "user_id=98" "$1"
