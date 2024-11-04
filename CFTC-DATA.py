from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
#====================
'''
In the previous editions,
I was looking to create a dictionary to divide the data,
so I decided to change the edition with the help of Pandas.
'''

browser = webdriver.Firefox()
browser.get('https://www.cftc.gov/dea/options/financial_lof.htm')
time.sleep(2)


s = str(browser.find_element(By.XPATH , '/html/body/pre').text)
lines = s.split("\n")
lines = [line for line in lines if line.strip()]
#=========================================================
#we creat text to see what we do and change our data
f = open("AllData-first-edition.txt", "a")
f.write(str(lines)+"\n""\n"+str(PAIR))
f.close()
#=========================================================
# my index is pair 
pairlist=[]
f = open("pairlist.txt", "a")
text = "Pair:" +"\n""\n"
for i in range(6, len(lines)-1, 17):
    dash_index2 = lines[i].find("- ")
    key = lines[i][:dash_index2].strip()
    text+= str(key)+"\n"
    pairlist.append(key)
    
f.write(text)
f.close()
#=========================================================
# we collect positions number line for a pair
positions=[]
f = open("positions.txt", "a")
text1 = "positions:" +"\n""\n"
for i in range(9, len(lines)-1, 17):
    dash_index2 = lines[i].find("- ")
    key = lines[i][:dash_index2].strip()
    key2= key.replace(',', '')
    positions2 = key2.split()
    #=========================
    def safe_float_conversion(s):
        try:
            return float(s)
        except ValueError:
            return None
    #===========================
    # Convert and filter out None values
    float_numbers = [safe_float_conversion(comp) for comp in positions2 if safe_float_conversion(comp) is not None]
    text1+= str(float_numbers)+"\n"
    positions.append(float_numbers)
    
f.write(text1)
f.close()
#=========================================================
# we collect Changepositions number line for a pair
Changepositions=[]
f = open("Changepositions.txt", "a")
text2 = "Changepositions:" +"\n""\n"
for i in range(11, len(lines)-1, 17):
    dash_index2 = lines[i].find("- ")
    key = lines[i][:dash_index2].strip()
    key2= key.replace(',', '')
    components = key2.split()
    #=========================
    def safe_float_conversion(s):
        try:
            return float(s)
        except ValueError:
            return None
    #===========================
    # Convert and filter out None values
    float_numbers = [safe_float_conversion(comp) for comp in components if safe_float_conversion(comp) is not None]
    text2+= str(float_numbers)+"\n"
    Changepositions.append(float_numbers)
    
f.write(text2)
f.close()
browser.quit()
#=========================================================
#======================DataFrames=========================
#=========================================================
topic = ['Long_Dealers','Short_Dealers','Spreading_Dealers',
        'Long_AssetManager','Short_AssetManager','Spreading_AssetManager',
        'Long_Leveraged','Short_Leveraged','Spreading_Leveraged',
        'Long_Reportables','Short_Reportables','Spreading_Reportables',
        'Long_Nonreportable','Short_Nonreportable']
df = pd.DataFrame(data=Changepositions,index=pairlist,columns=topic)
#=========================================================
#======================Sell_Signals=========================
sell = df[(df['Long_Leveraged'] < df['Short_Leveraged']) &
            (df['Long_AssetManager'] < df['Short_AssetManager'])]
sell = sell[['Long_AssetManager','Short_AssetManager','Long_Leveraged', 'Short_Leveraged']]
# Convert DataFrame to string with index
Selldata_str_with_index = sell.to_string(index=True)
# Print & SaveText the string with index
print(Selldata_str_with_index)
selltext= "CFTC-Sell-filters"+"\n""\n"
f = open("Sell.txt", "a")   
f.write(Selldata_str_with_index)
f.close()
#=========================================================
#======================Buy_Signals=========================
buy = df[(df['Long_Leveraged'] > df['Short_Leveraged']) &
            (df['Long_AssetManager'] > df['Short_AssetManager'])]
buy = buy[['Long_AssetManager','Short_AssetManager','Long_Leveraged', 'Short_Leveraged']]
# Convert DataFrame to string with index
Buydata_str_with_index = buy.to_string(index=True)
# Print & SaveText the string with index
print(Buydata_str_with_index)
buytext= "CFTC-Buy-filters"+"\n""\n"
f = open("Buy.txt", "a")   
f.write(Buydata_str_with_index)
f.close()


f.write(text)
f.close()
#=========================================================
browser.quit()
print("OK remove")
