import mysql.connector
from nsetools import Nse
import datetime
import time
mydb = mysql.connector.connect(host="localhost",user='root',passwd = 'root', database = 'stock')
mycursor = mydb.cursor()
nse = Nse()
L = ['HDFCBANK','ICICIBANK',"AXISBANK","SBIN","KOTAKBANK","INDUSINDBK","AUBANK","BANDHANBNK","FEDERALBNK","IDFCFIRSTB","RBLBANK","PNB"]
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
while True:
    time.sleep(330)
    try:
            mycursor.execute("TRUNCATE TABLE `banknifty`")
            print('db truncated........')
            for i in L:
                        df = nse.get_quote(f'{i}')
                        Symbol = str(i)
                        Average_Price = df['basePrice']
                        Last_Price = df['lastPrice']
                        x = datetime.datetime.now()
                        Date = x.date()
                        pChange = df['pChange']
                        Open_Price = df['open']
                        High_Price = df['dayHigh']
                        Low_Price = df['dayLow']
                        Close_Price = df['lastPrice']
                        Prev_Close = df["previousClose"]
                        Total_Traded_Quantity = df['quantityTraded']
                        Deliverable_Qty = df['deliveryQuantity']
                        totalTradedVolume = df['totalTradedVolume']
                        deliveryToTradedQuantity = ((Deliverable_Qty / Total_Traded_Quantity) * 100)
                        averagePrice = df['averagePrice']
                        last_sync = datetime.datetime.now()
                        val = [Symbol, Average_Price, pChange, Date, Prev_Close, Open_Price, High_Price, Low_Price,
                               Close_Price,
                               Total_Traded_Quantity, Deliverable_Qty, deliveryToTradedQuantity, last_sync]
                        #print(Close_Price)
                        sql = f"insert into banknifty (Symbol,Average_Price,pChange, Date,Prev_Close,Open_Price,High_Price,Low_Price,Close_Price,Total_Traded_Quantity,Deliverable_Qty,deliveryToTradedQuantity,last_sync) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                        mycursor.execute(sql, val)
                        print(val)
                        mydb.commit()
    except:
        deliveryToTradedQuantity = 0
        Deliverable_Qty = 0
print(".........................................................................................................................")

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

