#! /usr/bin/env python3

import os
import requests

#path = "/data/feedback"
#dir_list = os.listdir(path)

dir_list = os.listdir("/home/somak/python_practice/Python-Project/project-8-response-request/feedback_data")
new_json = []

for infile in dir_list:
    counter = 0
    #with open("/data/feedback/"+infile) as file:
    with open("/home/somak/python_practice/Python-Project/project-8-response-request/feedback_data/"+infile) as file:
        dic = {}
        for lines in file:
            lines = lines.strip()
            if counter == 0:
                key = "title"
                val = lines
                dic[key] = val
                counter += 1
            elif counter == 1:
                key = "name"
                val = lines
                dic[key] = val
                counter += 1
            elif counter == 2:
                key = "date"
                val = lines
                dic[key] = val
                counter += 1
            else:
                if counter == 3:
                    key = "feedback"
                    val = lines
                    dic[key] = val

    new_json.append(dic)
    response = requests.post("http://34.70.238.31/feedback/", data=dic)
    response.ok

#print(new_json)
