#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
the value of X-Request-Id varialble found in the header
of the response
"""
if __name__ == "__main__":
    import sys
    import urllib.request
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
