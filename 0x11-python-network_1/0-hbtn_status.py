#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status using the urllib package
"""
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    data = response.read()
    print("Body response:")
    print("	- type:", type(data))
    print("	- content:", data)
    print("	- utf8 content:", data.decode('utf-8'))
