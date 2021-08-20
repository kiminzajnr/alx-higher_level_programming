#!/usr/bin/python3
"""takes in a URL, sends a rquest to the URL
and displays the value of the variable
X-Request-Id it the response header
"""
if __name__ == "__main__":
    import sys
    import requests
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
