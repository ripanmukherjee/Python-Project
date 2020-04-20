#!/usr/bin/env python3
from network import *
import shutil
import psutil
import report_email
import os

def check_disk_usage(disk):
    """Verify that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    """Verify that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75

"""If there's not enough disk, or not enough CPU or not Internet Connection print error"""

Error = 0

if not check_disk_usage("/"):
   print("Error - Available disk space is less than 20%")
   email_subject = "Error - Available disk space is less than 20%"
   Error = 1
elif not check_cpu_usage():
    print("Error - CPU usage is over 80%")
    email_subject = "Error - CPU usage is over 80%"
    Error = 1
elif not check_localhost() and check_connectivity():
    print("Error - localhost cannot be resolved to 127.0.0.1")
    email_subject = "Error - localhost cannot be resolved to 127.0.0.1"
    Error = 1
else:
    print("Every thing is okay!!")


if Error == 1:
    ## For Email Sending
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    email_subject = "Upload Completed - Online Fruit Store"
    email_body = "Please check your system and resolve the issue as soon as possible."
    #message = report_email.generate_alert(sender, receiver, email_subject, email_body)
    #report_email.send(message)
