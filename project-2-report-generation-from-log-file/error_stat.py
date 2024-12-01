#!/usr/bin/env python3

import csv
import re

mainfile = "syslog.log"
errorfile = "errorlog.out"

def read_error_file(errorfile):
    error_list = []
    with open(errorfile, "r") as f1:
        for error_line in f1:
            error_line = error_line.strip()
            result = re.search(r"ERROR ([\w' ]*) ", error_line)
            if result is None:
                print("Not Match")
            else:
                paranthesis_position = error_line.find("(")
                new_error_line = error_line[6:paranthesis_position-1]
                error_list.append(new_error_line)
    return error_list

def process_data(error_list):
    new_error_list = []
    for error_data in error_list:
        new_error_list.append(error_data)
        error_data = {}
        for error_desciption in set(new_error_list):
            error_data[error_desciption] = new_error_list.count(error_desciption)
    return error_data

def write_error_csv(dictionary):
    items = [(v, k) for k, v in dictionary.items()]
    items.sort()
    items.reverse()
    items = [(k, v) for v, k in items]
    #print(items)
    keys = ["Error", "Count"]
    with open('error_message.csv', 'w') as error_csv:
        writer = csv.writer(error_csv)
        writer.writerow(keys)
        writer.writerows(items)

read_list = read_error_file(errorfile)
dictionary = process_data(read_list)
write_error_csv(dictionary)
