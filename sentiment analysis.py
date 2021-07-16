import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
import mysql.connector
from nsetools import Nse
import datetime
import time
import plotly.graph_objects as go
import numpy as np

import re
mydb = mysql.connector.connect(host="localhost",user='root',passwd = 'root', database = 'stock')
mycursor = mydb.cursor()


url = 'https://www.tickertape.in/market-mood-index'
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

while True:
    page = requests.get(url, headers=agent)
    soup = BS(page.content, 'lxml')
    data = soup.find('div',{"class":"jsx-3758077420"})
    index = data.find('span',{"class":"jsx-3758077420"}).get_text()
    index = float(index)
    last_sync = datetime.datetime.now()
    val = [index,last_sync]
    sql = f"insert into sentimentindex (indexval,last_sync) values (%s,%s)"
    mycursor.execute(sql, val)
    ind = index
    timme = last_sync
    mydb.commit()
    print('Value updated.......')
    print(index)
    time.sleep(180)

