#!/usr/bin/env python3
import os, sys
from PIL import Image

src = "/home/somak/python_practice/Python-Project/project-7-image-PIL"

for root, dir, files in os.walk(src):
    for infile in files:
        try:
            with Image.open(infile) as im:
                print(infile, im.format, "%dx%d" % im.size, im.mode)
                im.rotate(90).resize((128,128)).convert("RGB").save(infile+".jpg")
        except IOError:
            print("cannot open", infile)
