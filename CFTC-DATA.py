from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import datetime
import time
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
f = open("AllData-first-edition.txt", "a")
f.write(str(lines)+"\n""\n"+str(PAIR))
f.close()
#=========================================================
# we collect the name of pairs to another text file
f = open("Data-first-edition.txt", "a")
text = "Pair:" +"\n""\n"
for i in range(6, len(lines)-1, 17):
    dash_index2 = lines[i].find("- ")
    key = lines[i][:dash_index2].strip()
    text+= str(key)+"\n""\n"
    

f.write(text)
f.close()
#=========================================================
browser.quit()
print("OK remove")
