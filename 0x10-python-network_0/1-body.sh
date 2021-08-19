#!/bin/bash
# takes in a URL, sends a GET request to the URL and displays the body of the response
curl -sb /dev/null -X GET "$1"
