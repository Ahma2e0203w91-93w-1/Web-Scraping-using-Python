#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[14]:


# Connect to Website and pull in data

URL = 'https://en.wikipedia.org/wiki/Venture_round'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")



title = soup2.find(id="firstHeading").get_text()




print(title)

# Clean up the data a little bit


title = title.strip()

print(title)

# In[15]:


# Create a Timestamp for your output to track when data was collected

import datetime

today = datetime.date.today()

print(today)


# In[16]:


# Create CSV and write headers and data into the file

import csv 

header = ['Title', 'Date']
data = [title, today]


with open('WikepediaWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[21]:


#Now we are appending data to the csv

with open('C:/Users/Ahmad Hassan/Desktop/Portfolio Data Analyst/Wikipedia Web Scraping/WikepediaWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:


#Now we are appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:





# In[22]:


import pandas as pd

df = pd.read_csv(r'C:/Users/Ahmad Hassan/Desktop/Portfolio Data Analyst/Wikipedia Web Scraping/WikepediaWebScraperDataset.csv')

print(df)


# In[23]:


# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it
# out with this script

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('ahmad.khokhar0055@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Title "
    body = "of this page is"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'ahmad.khokhar0055@gmail.com',
        msg
     
    )


# In[ ]:




