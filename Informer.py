#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
import time
import os
import re
from datetime import datetime

#import webbrowser
import json

from bs4 import BeautifulSoup

# set options to be headless, ..
from selenium import webdriver

import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


# In[7]:


token = '5090261134:AAG1iRgvxYFaj4dbZgbnv8CNZj6vglR-jTA'
chat_id = '1599874688'


# In[8]:


coin = int(input('Welcher Coin ist von Interesse 1 - USDC, 2 - USDT, 3 both? '))
higher_or_lower = int(input("In welche Richtung 1 - higher, 2 - lower, 3 both? "))
lower = float(input("Was ist die untere Grenze (Format 1.185)? ") or '1.185')
higher = float(input("Was ist die obere Grenze (Format 1.205)? ") or '1.205')


# In[ ]:


params = {"chat_id":chat_id, "text":f"ArbitrageBot starting"}
url = f"https://api.telegram.org/bot{token}/sendMessage"
message = requests.post(url, params=params)

while True:
    driver = webdriver.Chrome('/Users/felixfrohboese/Documents/10_Data_Science/Data_Science_Projects/DeFiChain_Arbitrage/chromedriver', options=options)
    #driver.implicitly_wait(3)

    driver.get('https://www.krypto-sprungbrett.com/stock-token-apr/')
    driver.implicitly_wait(1)

    try: 
        usdc = float(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/article/div[2]/table[2]/tbody[2]/tr[2]/td[4]').text)
        usdt = float(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/article/div[2]/table[2]/tbody[2]/tr[2]/td[5]').text)

        if usdc < lower and coin != 2 and higher_or_lower != 1: 
            params = {"chat_id":chat_id, "text":f"dUSDC has low: {usdc}"}
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            message = requests.post(url, params=params)

        if usdt < lower and coin != 1 and higher_or_lower != 1: 
            params = {"chat_id":chat_id, "text":f"dUSDT has low: {usdt}"}
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            message = requests.post(url, params=params)

        if usdc > higher and coin != 2 and higher_or_lower != 2: 
            params = {"chat_id":chat_id, "text":f"dUSDC has high: {usdc}"}
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            message = requests.post(url, params=params)

        if usdt > higher and coin != 1 and higher_or_lower != 2: 
            params = {"chat_id":chat_id, "text":f"dUSDT has high: {usdt}"}
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            message = requests.post(url, params=params)
            
    except:
        pass

            
    driver.implicitly_wait(5)
    driver.close()
    

#Datetime
#now = datetime.now()
#date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

#prices.update({date_time: [usdc, usdt]})


# In[ ]:


#import sys, select

#print("You have ten seconds to answer!")

#i, o, e = select.select([sys.stdin], [], [], 10)

#if i:
#    print("You said", sys.stdin.readline().strip())
#else:
#    print("You said nothing!")


# In[ ]:





# In[ ]:





# In[ ]:


#timestamp = datetime.timestamp(now)
#print("timestamp =", timestamp)

#year = now.strftime("%Y")
#month = now.strftime("%m")
#day = now.strftime("%d")
#time = now.strftime("%H:%M:%S")

#print("date and time:",date_time)


# In[ ]:


#options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
# open it, go to a website, and get results
#driver = webdriver.Chrome(options=options)
# wd.get('https://www.pgatour.com')
# print(wd.page_source)  # results
# divs = wd.find_elements_by_css_selector('div')


# In[ ]:


#with open("/Users/felixfrohboese/Documents/10_Data_Science/Data_Science_Projects/DeFiChain_Arbitrage/token.txt") as file:
#    token = file.read()


# In[ ]:


#answer = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
#answer

#content = answer.content
#data = json.loads(content)
#data

#answer = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
#content = answer.content
#data = json.loads(content)
#data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




