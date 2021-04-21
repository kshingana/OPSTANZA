#import js as js
#import numpy as np
#import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
import mysql.connector
#from nsetools import Nse
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
final_data = []

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
			country = x.find('td', {"class": "col-flag"})
			name = str(x.find('span', {"class": "flag"}))
			i = name.find('-')
			j = name.find('"', i)
			country_name = name[i + 1:j]
			country_name = country_name.upper()
			if Index_Name=='China A50':
				country_name='CHINA'
			elif Index_Name=='US 30':
				country_name='NORTH AMERICA'
			frame = {
					"name": Index_Name,
					"LTP": LTP_num,
					"HIGH": HIGH_num,
					"LOW": LOW_num,
					"points_chang": points_chng_num,
					"%chng": pct_num,
					"country_name":country_name
				   }
			#print(frame)
			final_data.append(frame)
		except AttributeError:
			country_name = 'None'
		except:
			points_chng_num = "NONE"
			pct_num = "NONE"

#print(final_data[0])
while True:
	for i in range(len(final_data)):
		k  = final_data[i]
		name = k['name']
		LTP = k['LTP']
		HIGH = k['HIGH']
		LOW = k['LOW']
		points_chang = k['points_chang']
		perct_chg = k['%chng']
		country_name = k['country_name']
		last_sync = datetime.datetime.now()
		val = [name,LTP,HIGH,LOW,points_chang,perct_chg,country_name,last_sync]
		sql = f"insert into globalfut (name,LTP,HIGH,LOW,points_chang,perct_chg,country_name,last_sync) values (%s,%s,%s," \
			  f"%s,%s,%s,%s,%s) "
		mycursor.execute(sql, val)
		print(val)
		mydb.commit()
	print(".........................................................................")
	time.sleep(180)
	mycursor.execute("TRUNCATE TABLE `globalfut`")
	mydb.commit()
	print('db updated........')
	time.sleep(10)