#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the body of the response
"""
if __name__ == "__main__":
    import sys
    import urllib.request
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            the_page = response.read().decode('utf-8')
            print(the_page)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
