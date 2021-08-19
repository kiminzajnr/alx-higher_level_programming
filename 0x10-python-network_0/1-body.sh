#!/bin/bash
# takes in a URL, sends a GET request to the URL and displays the body of the response
status=$(curl -o /dev/null -s -w '%{http_code}' "$1"); [[ $status == 200 ]] &&  curl -sb -X GET "$1"
