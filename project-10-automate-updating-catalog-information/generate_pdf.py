#!/usr/bin/env python3
import os
import json
import locale
import sys
import reports
import report_email
from datetime import date

#path = "/home/student-01-ddb99c85d7c8/supplier-data/descriptions/"
path = "/home/somak/python_practice/Python-Project/project-10-automate-updating-catalog-information/supplier-data/descriptions/"
dir_list = os.listdir(path)

def generate_paragraph(PDF_paragraph_summary):
    for infile in dir_list:
        counter = 0
        text = ""
        with open(path+infile) as file:
            for lines in file:
                lines = lines.strip()
                if counter == 0:
                    key = "name"
                    val = lines
                    text = key + ": " + val
                    PDF_paragraph_summary = PDF_paragraph_summary+text+"<br/>"
                    counter += 1
                elif counter == 1:
                    key = "weight"
                    val =lines
                    text = key + ": " + val
                    PDF_paragraph_summary = PDF_paragraph_summary+text+"<br/>"+"\n\n"
                    counter += 1
                else:
                    pass

    #print(PDF_paragraph_summary)
    return PDF_paragraph_summary

if __name__ == "__main__":
    PDF_paragraph_summary = ""
    paragraph = generate_paragraph(PDF_paragraph_summary)
    print(paragraph)
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    title = "Processed Update on " + d2
    attachment = "processed.pdf"
    reports.generate_report(attachment, title, paragraph)

    ## For Email Sending
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    email_subject = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    #message = report_email.generate(sender, receiver, email_subject, email_body, "/tmp/processed.pdf")
    #report_email.send(message)
