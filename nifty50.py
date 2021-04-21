import mysql.connector
from nsetools import Nse
import datetime
import time
mydb = mysql.connector.connect(host="localhost",user='root',passwd = 'root', database = 'stock')
mycursor = mydb.cursor()
nse = Nse()
L = ['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BPCL', 'BHARTIARTL', 'BRITANNIA',
     'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GAIL', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO',
     'HINDALCO', 'HINDUNILVR', 'HDFC', 'ICICIBANK', 'ITC', 'IOC', 'INDUSINDBK', 'INFY', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI',
     'NTPC', 'NESTLEIND', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SHREECEM', 'SBIN', 'SUNPHARMA', 'TCS', 'TATAMOTORS', 'TATASTEEL',
     'TECHM', 'TITAN', 'UPL', 'ULTRACEMCO', 'WIPRO']

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

count=0
while count <=100 :

        for i in L:
                df = nse.get_quote(f'{i}')
                Symbol = str(i)
                Average_Price =df['basePrice']
                Last_Price = df['lastPrice']
                x =  datetime.datetime.now()
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
                deliveryToTradedQuantity = ((Deliverable_Qty/Total_Traded_Quantity)*100)
                averagePrice = df['averagePrice']
                df = nse.get_quote(f'{i}')
                Symbol = str(i)
                Average_Price =df['basePrice']
                Last_Price = df['lastPrice']
                x =  datetime.datetime.now()
                Date = x.date()
                pChange = df['pChange']
                Open_Price = df['open']
                High_Price = df['dayHigh']
                Low_Price = df['dayLow']
                Close_Price = df['closePrice']
                Prev_Close = df["previousClose"]
                Total_Traded_Quantity = df['quantityTraded']
                Deliverable_Qty = df['deliveryQuantity']
                totalTradedVolume = df['totalTradedVolume']
                deliveryToTradedQuantity = ((Deliverable_Qty/Total_Traded_Quantity)*100)
                averagePrice = df['averagePrice']
                last_sync = datetime.datetime.now()
                val = [Symbol, Average_Price, pChange, Date, Prev_Close, Open_Price, High_Price, Low_Price, Close_Price,
                       Total_Traded_Quantity, Deliverable_Qty, deliveryToTradedQuantity, last_sync]
                sql = f"insert into nifty50new (Symbol,Average_Price,pChange, Date,Prev_Close,Open_Price,High_Price,Low_Price,Close_Price,Total_Traded_Quantity,Deliverable_Qty,deliveryToTradedQuantity,last_sync) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                mycursor.execute(sql, val)
                print(val)
                mydb.commit()
        time.sleep(260)
        print(".........................................................................................................................")
        time.sleep(30)
        print('db updated........')
        mycursor.execute("TRUNCATE TABLE `nifty50new`")
        mydb.commit()
        print('db truncated........')
        time.sleep(10)
        count+=1
print(count)


'''----------------------------------------------------------------------------------------------------------------------------------------------------------------'''





