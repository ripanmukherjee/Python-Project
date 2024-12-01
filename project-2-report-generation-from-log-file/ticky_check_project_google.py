#!/usr/bin/env python3

import re
import csv

mainfile = "syslog.log"
errorfile = "errorlog.out"


def read_error_file(errorfile):
    error_list = []
    with open(errorfile, "r") as f1:
        for error_line in f1:
            error_line = error_line.strip()
            result = re.search(r"ERROR ([\w' ]*) ", error_line)
            if result:
                paranthesis_position = error_line.find("(")
                new_error_line = error_line[6:paranthesis_position - 1]
                error_list.append(new_error_line)
    return error_list


def process_data(error_list):
    error_data = {}
    for error_description in error_list:
        if error_description in error_data:
            error_data[error_description] += 1
        else:
            error_data[error_description] = 1
    return error_data


def write_error_csv(dictionary):
    items = [(v, k) for k, v in dictionary.items()]
    items.sort(reverse=True, key=lambda x: x[0])
    keys = ["Error", "Count"]
    with open('error_message.csv', 'w') as error_csv:
        writer = csv.writer(error_csv)
        writer.writerow(keys)
        writer.writerows((k, v) for v, k in items)


def read_user_file(mainfile):
    user_error_list = []
    user_info_list = []
    with open(mainfile, "r") as f1:
        for user_line in f1:
            user_line = user_line.strip()
            paranthesis_position_first = user_line.find("(")
            paranthesis_position_second = user_line.find(")")
            if paranthesis_position_first != -1 and paranthesis_position_second != -1:
                user = user_line[paranthesis_position_first + 1:paranthesis_position_second]
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


def write_user_statistics(dictionary_info, dictionary_error):
    unique_user_list = sorted(set(dictionary_info.keys()).union(dictionary_error.keys()))
    keys = ["Username", "INFO", "ERROR"]
    with open('user_statistic.csv', 'w') as test_csv:
        writer = csv.writer(test_csv)
        writer.writerow(keys)
        for user in unique_user_list:
            info_count = dictionary_info.get(user, 0)
            error_count = dictionary_error.get(user, 0)
            writer.writerow([user, info_count, error_count])


read_list = read_error_file(errorfile)
dictionary = process_data(read_list)
write_error_csv(dictionary)

user_first_list, user_second_list = read_user_file(mainfile)
dictionary_info = process_user_data(user_first_list)
dictionary_error = process_error_data(user_second_list)
write_user_statistics(dictionary_info, dictionary_error)
