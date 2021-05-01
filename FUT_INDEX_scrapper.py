import js as js
import json
import numpy as np
import pandas as pd
'''import requests
from bs4 import BeautifulSoup as BS
import mysql.connector
from nsetools import Nse
import datetime
import time

mydb = mysql.connector.connect(host="localhost",user='root',passwd = 'root', database = 'stock')
mycursor = mydb.cursor()

st_list = []
url = 'https://in.investing.com/indices/indices-futures'

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
page = requests.get(url, headers=agent)

soup = BS(page.content, 'lxml')
data = soup.find_all('tr',{"class":"common-table-item u-clickable"})
df = dict()
final_data = [];
while True:
    for x in data:
            #print(x)
            try:
                Index_Name = x.find('a', {"class": "js-instrument-page-link"}).get_text()
                LTP_class = x.find('td',{"class":"col-last u-txt-align-end"})
                LTP_num = LTP_class.find('span',{"class":"text"}).get_text()
                HIGH_class = x.find('td', {"class": "col-high"})
                HIGH_num = HIGH_class.find('span', {"class": "text"}).get_text()
                LOW_class = x.find('td', {"class": "col-low"})
                LOW_num = LOW_class.find('span', {"class": "text"}).get_text()
                points_chng =  x.find('td', {"class": "col-chg"})
                points_chng_num = points_chng.find("span",{"class": "text"}).get_text()
                pct_chng = x.find('td', {"class": "col-chg_pct"})
                pct_num = pct_chng.find("span",{"class": "text"}).get_text()
                last_sync = datetime.datetime.now()
                frame = {
                    Index_Name: [
                                            {
                                                "LTP": LTP_num,
                                                "HIGH": HIGH_num,
                                                "LOW": LOW_num,
                                                "points_chang": points_chng_num,
                                                "%chng": pct_num,
                                            }
                               ]
                       }
                final_data.append(frame)
                for Index_Name, LTP in frame.items():
                    pass
                    #print('{} {}'.format(Index_Name, LTP))
            except:
                points_chng_num = "NONE"
                pct_num = "NONE"
    print(final_data)'''
import yfinance as yf
data = yf.download(tickers='UBER', period='1d', interval='1d')
print(data)

# sub folder is updated