#!/bin/bash
# Takes in a URL as an argumrnt, sends a GET Request to the URL, and displays the body of the response
curl -H X-School-User-Id:98 -s "$1" /route_5
