# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:31:47 2021

@author: luisv
"""
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key =  "QvrROLQbeGnXmsgha3A7O4tiYI5XHBUo"
#The "while True" construct creates an endless loop.
while True:
    orig = input("Starting Location: ")
    if orig=="quit" or orig=="q":
        break
    dest = input("Destination: ")
    if dest=="quit" or dest=="q":
        break        
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + (url))
    
   

