#!/usr/bin/env python3

import re
import sys
import csv
import os
from collections import OrderedDict

mainfile = "syslog.log"

def read_user_file(mainfile):
    user_error_list = []
    user_info_list = []
    with open(mainfile, "r") as f1:
        for user_line in f1:
            user_line = user_line.strip()
            result = re.search(r"ERROR ([\w' ]*) ", user_line)
            if result is None:
                #User extraction for INFO Message
                regex = r"\((.*)\)"
                user = re.search(regex, user_line)
                user_info_list.append(user[1])
            else:
                #User extraction for Error Message
                regex = r"\((.*)\)"
                user = re.search(regex, user_line)
                user_error_list.append(user[1])

    return user_info_list, user_error_list

def process_user_data(user_first_list):
    new_user_info_list = []
    for info_data in user_first_list:
        new_user_info_list.append(info_data)
        user_info_data = {}
        for user_info in set(new_user_info_list):
            user_info_data[user_info] = new_user_info_list.count(user_info)
    return user_info_data

def process_error_data(user_second_list):
    new_user_error_list = []
    for error_data in user_second_list:
        new_user_error_list.append(error_data)
        user_error_data = {}
        for user_error in set(new_user_error_list):
            user_error_data[user_error] = new_user_error_list.count(user_error)
    return user_error_data

user_first_list,  user_second_list = read_user_file(mainfile)
dictionary_info = process_user_data(user_first_list)
dictionary_error = process_error_data(user_second_list)

total_list = []
for key in dictionary_info:
    total_list.append(key)

for key in dictionary_error:
    total_list.append(key)

unique_user_list = []
for i in total_list:
    if i not in unique_user_list:
        unique_user_list.append(i)

unique_user_list.sort()

keys = ["Username", "INFO", "ERROR"]
with open('user_statistic.csv', 'w') as test_csv:
    writer = csv.writer(test_csv)
    writer.writerow(keys)

for i in unique_user_list:
    if i in dictionary_info.keys():
        if i in dictionary_error.keys():
            j = []
            j = [i, dictionary_info[i], dictionary_error[i]]
            with open('user_statistic.csv', 'a') as test_csv:
                writer = csv.writer(test_csv)
                writer.writerow(j)
        else:
            j = []
            j = [i, dictionary_info[i], 0]
            with open('user_statistic.csv', 'a') as test_csv:
                writer = csv.writer(test_csv)
                writer.writerow(j)
    else:
        j = []
        j = [i, 0, dictionary_error[i]]
        with open('user_statistic.csv', 'a') as test_csv:
            writer = csv.writer(test_csv)
            writer.writerow(j)
