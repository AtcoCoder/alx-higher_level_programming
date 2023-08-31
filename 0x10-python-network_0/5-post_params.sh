#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X POST -d  "email=test@gmail%2Ecom&subject=I+will+always+be+here+for+PLD" -s "$1"
