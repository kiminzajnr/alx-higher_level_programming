#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the body of the response
"""
if __name__ == "__main__":
    import sys
    import requests
    r = requests.get(sys.argv[1])
    if r.status_code > 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
