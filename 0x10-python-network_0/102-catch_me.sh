#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing you got me!
curl -s -X PUT "0.0.0.0:5000/catch_me" -o /dev/null ; printf "You got me!"
