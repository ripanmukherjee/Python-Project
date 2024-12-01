#!/usr/bin/env python3

import re
import csv

mainfile = "syslog.log"


def read_user_file(mainfile):
    user_error_list = []
    user_info_list = []
    with open(mainfile, "r") as f1:
        for user_line in f1:
            user_line = user_line.strip()
            user_match = re.search(r"\((.*)\)", user_line)
            if not user_match:
                continue

            user = user_match.group(1)
            if "ERROR" in user_line:
                user_error_list.append(user)
            else:
                user_info_list.append(user)

    return user_info_list, user_error_list


def process_user_data(user_first_list):
    user_info_data = {}
    for user_info in user_first_list:
        if user_info in user_info_data:
            user_info_data[user_info] += 1
        else:
            user_info_data[user_info] = 1
    return user_info_data


def process_error_data(user_second_list):
    user_error_data = {}
    for user_error in user_second_list:
        if user_error in user_error_data:
            user_error_data[user_error] += 1
        else:
            user_error_data[user_error] = 1
    return user_error_data


user_first_list, user_second_list = read_user_file(mainfile)
dictionary_info = process_user_data(user_first_list)
dictionary_error = process_error_data(user_second_list)

# Create a unique sorted list of usernames
unique_user_list = sorted(set(dictionary_info.keys()).union(dictionary_error.keys()))

# Prepare CSV writing in one go
keys = ["Username", "INFO", "ERROR"]
with open('user_statistic.csv', 'w', newline='') as test_csv:
    writer = csv.writer(test_csv)
    writer.writerow(keys)

    for user in unique_user_list:
        info_count = dictionary_info.get(user, 0)
        error_count = dictionary_error.get(user, 0)
        writer.writerow([user, info_count, error_count])
