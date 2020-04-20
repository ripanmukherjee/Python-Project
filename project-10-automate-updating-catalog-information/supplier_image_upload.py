#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://35.188.36.216/upload/"
#src = "/home/student-01-ddb99c85d7c8/supplier-data/images/"
src = "/home/somak/python_practice/Python-Project/project-10-automate-updating-catalog-information/supplier-data/images/"

for infile in os.listdir(src):
    try:
        if infile.endswith(".jpeg"):
            with open(src+infile, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
    except IOError:
        print("cannot open", infile)
