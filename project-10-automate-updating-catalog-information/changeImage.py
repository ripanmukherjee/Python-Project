#!/usr/bin/env python3

import os, sys
from PIL import Image

#src = "/home/student-01-ddb99c85d7c8/supplier-data/images/"
src = "/home/somak/python_practice/Python-Project/project-10-automate-updating-catalog-information/supplier-data/images/"

for infile in os.listdir(src):
    try:
        if infile.endswith(".tiff"):
            outfile = infile[:3]+".jpeg"
            Image.open(src+infile).resize((600, 400)).convert('RGB').save(src+outfile)
    except IOError:
        print("cannot open", infile)
