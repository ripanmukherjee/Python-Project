#! /usr/bin/env python3

import os
import requests

#path = "/home/student-01-ddb99c85d7c8/supplier-data/descriptions/"
path = "/home/somak/python_practice/Python-Project/project-10-automate-updating-catalog-information/supplier-data/descriptions/"
url = url = "http://35.188.36.216/fruits/"

dir_list = os.listdir(path)
new_json = []

for infile in dir_list:
    counter = 0
    with open(path+infile) as file:
        dic = {}
        for lines in file:
            lines = lines.strip()
            if counter == 0:
                key = "name"
                val = lines
                dic[key] = val
                counter += 1
            elif counter == 1:
                key = "weight"
                if lines.endswith("lbs"):
                    #print(lines[:3])
                    val = int(lines[:3])
                    dic[key] = val
                    counter += 1
            elif counter == 2:
                key = "description"
                val = lines
                dic[key] = val
                counter += 1
            else:
                pass

        dic.update({"image_name" : infile[:3]+".jpeg"})

    #new_json.append(dic)
    print(dic)
    response = requests.post(url, data=dic)
    print(response.ok)

#print(new_json)
