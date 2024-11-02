from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import datetime
import time
import telegram
import asyncio
from bs4 import BeautifulSoup
import requests
import telegram
import asyncio
#====================

browser = webdriver.Firefox()
browser.get('https://www.cftc.gov/dea/options/financial_lof.htm')
time.sleep(2)


s = str(browser.find_element(By.XPATH , '/html/body/pre').text)
lines = s.split("\n")
lines = [line for line in lines if line.strip()]
PAIR = []
for i in range(1, len(lines)-1, 17):
    chunk = "\n".join(lines[i:i+17])
    PAIR.append(chunk)
#=========================================================
#we need to make_dictionary with this data at another function
'''
cot_info = {}
for i in PAIR:
    make_dictionary(i,cot_info)
'''
#=========================================================
#we creat text to see what we do and change our data
f = open("Data-first-edition.txt", "a")
f.write(str(lines)+"\n""\n"+str(PAIR))
f.close()
#=========================================================
browser.quit()
print(lines)
print(PAIR)
print("OK remove")
