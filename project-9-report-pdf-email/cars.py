#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails
import os


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.Returns a list of lines that summarize the information."""
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales = 0
  dict1 = {}
  dictionary = {}
  for item in data:
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item

    if item["total_sales"] > max_sales:
        max_sales = item["total_sales"]
        total_sales = item

    dict1 = item['car']
    for k, v in dict1.items():
        if k == "car_year":
            new_key = v
            new_value = item["total_sales"]
            if new_key in dictionary:
                old_value = dictionary[new_key]
                new_value = int(new_value) + int(old_value)
                dictionary.update({new_key : new_value})
            else:
                dictionary.update({new_key : new_value})


  max_key = max(dictionary, key=dictionary.get)
  all_values = dictionary.values()
  max_value = max(all_values)

  summary = [
    "The {} generated the most revenue: ${}".format(format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(format_car(total_sales["car"]), total_sales["total_sales"]),
    "The most popular year was {} with {} sales.".format(max_key, max_value)
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  #print(summary)

  ## For PDF generation
  PDF_table_data = cars_dict_to_table(data)
  PDF_title_subject = "Sales summary for last month"
  PDF_paragraph_summary = ""
  for text in summary:
      PDF_paragraph_summary = PDF_paragraph_summary+"<br/>"+text

  #print(table_summary)

  reports.generate("cars.pdf", PDF_title_subject, PDF_paragraph_summary, PDF_table_data)

  ## For Email Sending
  #sender = "automation@example.com"
  #receiver = "{}@example.com".format(os.environ.get('USER'))
  email_subject = PDF_title_subject
  email_body = ""
  for text in summary:
      email_body = email_body+"\n"+text

  #message = emails.generate(sender, receiver, email_subject, email_body, "cars.pdf")
  #emails.send(message)

if __name__ == "__main__":
  main(sys.argv)
