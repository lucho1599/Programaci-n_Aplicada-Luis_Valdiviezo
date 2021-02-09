# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:46:20 2021

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
    
    json_data=requests.get(url).json()
    json_status=json_data["info"]["statuscode"]
    
    if json_status==0:
        print("API Status: "+str(json_status)+"A successful route call. \n")
        print("Directions from " + (orig) + " to " +(dest))
        print("Trip Duration:  "+ str(json_data["route"]["formattedTime"]))
        print("Kilometers:     "+ str((json_data["route"]["distance"])*1.61))
        print("Fuel Used(Ltr): "+ str((json_data["route"]["fuelUsed"])*3.78))
        print("=====================================================")
        
        
