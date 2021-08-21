#!/usr/bin/python3
"""takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter
as a parameter
"""
if __name__ == "__main__":
    import sys
    import requests
    if len(sys.argv) == 1:
        value = ""
    else:
        value = sys.argv[1]
    params = {'q': value}
    url = 'http://603d1bc940b5.ae4d45e0.alx-cod.online:5000/search_user'
    r = requests.post(url, data=params)
    if r.headers.get('content-type') == 'application/json' and r.json():
        id_ = r.json().get('id')
        name = r.json().get('name')
        print("[{}] {}".format(id_, name))
    elif not r.json():
        print("No result")
    elif r.headers.get('content-type') != ('application/json'):
        print("Not a valid JSON")
