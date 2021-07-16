#Nifty50 stock price Scrapper MySql Table  query :

use stock;
create table nifty50new
(
    Symbol varchar(50),
    Date datetime,
    Prev_Close float,
    Open_Price float,
    High_Price float,
    Low_Price float,
    Last_Price float,
    Close_Price float,
    Average_Price float,
    Total_Traded_Quantity float,
    Deliverable_Qty float,
    deliveryToTradedQuantity float,
    last_sync datetime unique
)



#BankNifty Stock Price Scrapper MySql  Table query :

create table banknifty
(
Symbol varchar(50),
Average_Price float,
pChange float,
Date varchar(50) ,
Prev_Close float,
Open_Price float,
High_Price float,
Low_Price float,
Last_Price float,
Close_Price float,
Total_Traded_Quantity float,
Deliverable_Qty float,
deliveryToTradedQuantity float,
last_sync datetime
)




#Global Indexes FUT Price Scrapper MySql Table query :

create table globalfut
(
name varchar(50),
LTP varchar(50) ,
HIGH varchar(50),
LOW varchar(50),
points_chang varchar(50),
perct_chg varchar(50),
country_name varchar(50),
last_sync datetime
)


#Indian Market Sentiment Indexes Scrapper MySql Table query :

create table sentimentindex
(
indexval float(50),
last_sync datetime
)

#Indian Market Sectorial Analysis Scrapper MySql Table query :
create table sectors
(
name varchar(50),
lastPrice varchar(50),
chg varchar(50),
pChange varchar(50),
last_sync datetime
)







