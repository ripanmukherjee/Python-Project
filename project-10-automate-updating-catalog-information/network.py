#!/usr/bin/env python3
import requests
import socket

"""Verify the locakhost"""
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost

"""Checking the connectivity"""
def check_connectivity():
    request = requests.get("http://www.google.com")
    status_code = request
    return status_code
