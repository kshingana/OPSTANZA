import mysql.connector
from nsetools import Nse
import datetime
import time
mydb = mysql.connector.connect(host="localhost",user='root',passwd = 'root', database = 'stock')
mycursor = mydb.cursor()
nse = Nse()
df = []
index_codes = nse.get_index_list()
L = ['NIFTY 50', 'NIFTY NEXT 50', 'NIFTY100 LIQ 15', 'NIFTY BANK', 'INDIA VIX', 'NIFTY 100', 'NIFTY 500', 'NIFTY MIDCAP 100', 'NIFTY MIDCAP 50', 'NIFTY INFRA', 'NIFTY REALTY', 'NIFTY ENERGY', 'NIFTY FMCG', 'NIFTY MNC', 'NIFTY PHARMA', 'NIFTY PSE', 'NIFTY PSU BANK', 'NIFTY SERV SECTOR', 'NIFTY IT', 'NIFTY SMLCAP 100', 'NIFTY 200', 'NIFTY AUTO', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY DIV OPPS 50', 'NIFTY COMMODITIES', 'NIFTY CONSUMPTION', 'NIFTY CPSE', 'NIFTY FIN SERVICE', 'NIFTY GROWSECT 15', 'NIFTY50 VALUE 20', 'NIFTY50 TR 2X LEV', 'NIFTY50 PR 2X LEV', 'NIFTY50 TR 1X INV', 'NIFTY50 PR 1X INV', 'NIFTY ALPHA 50', 'NIFTY50 EQL WGT', 'NIFTY100 EQL WGT', 'NIFTY100 LOWVOL30', 'NIFTY MID LIQ 15', 'NIFTY PVT BANK', 'NIFTY100 QUALTY30', 'NIFTY GS 8 13YR', 'NIFTY GS 10YR', 'NIFTY GS 10YR CLN', 'NIFTY GS 4 8YR', 'NIFTY GS 11 15YR', 'NIFTY GS 15YRPLUS', 'NIFTY GS COMPSITE', 'NIFTY MIDCAP 150', 'NIFTY SMLCAP 50', 'NIFTY SMLCAP 250', 'NIFTY MIDSML 400', 'NIFTY200 QUALTY30']
#print(index_codes)
for i in L:
    index_quotes = nse.get_index_quote(f'{i}')
    df.append(index_quotes)
    print(index_quotes)
#print(df)

while True:
    for j in range (len(df)):
        name = df[j]['name']
        lastPrice = df[j]['lastPrice']
        chg= df[j]['change']
        pChange = df[j]['pChange']
        last_sync = datetime.datetime.now()
        val = [name, lastPrice,chg,pChange,last_sync]
        sql = f"insert into sectors (name, lastPrice,chg,pChange,last_sync) values (%s,%s,%s,%s,%s)"
        mycursor.execute(sql,val)
        mydb.commit()
    print("db updated..............")
    time.sleep(90)




