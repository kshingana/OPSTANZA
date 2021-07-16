import time
import requests
import json
import pandas as pd
import sqlite3

expiry_dt = '22-Jul-2021'


conn = sqlite3.connect('data/stock.db')
db = sqlite3.connect('data/stock.db')
nse_url = 'https://www.nseindia.com/api/option-chain-indices?symbol='
symbols = ['BANKNIFTY', 'NIFTY']


def start_fetching():
    for symbol in symbols:
        fetch_nse_data(symbol)
    time.sleep(180)


def create_schemas():
    for symbol in symbols:
        db.execute(
            "CREATE TABLE IF NOT EXISTS `" + symbol + "` ( `strikePrice` INTEGER, `expiryDate` TEXT, `type` TEXT, "
                                                      "`underlying` TEXT, `identifier` TEXT, `openInterest` INTEGER, "
                                                      "`changeinOpenInterest` INTEGER, `pchangeinOpenInterest` REAL, "
                                                      "`totalTradedVolume` INTEGER, `impliedVolatility` REAL, "
                                                      "`lastPrice` REAL, `change` REAL, `pChange` REAL, "
                                                      "`totalBuyQuantity` INTEGER, `totalSellQuantity` INTEGER, "
                                                      "`bidQty` INTEGER, `bidprice` REAL, `askQty` INTEGER, "
                                                      "`askPrice` REAL, `underlyingValue` REAL, `last_sync` TEXT, "
                                                      "UNIQUE(strikePrice, type, last_sync, expiryDate))")
        db.commit()

def start():
    create_schemas()
    while True:
        start_fetching()


def fetch_nse_data(symbol):
    req_url = nse_url + symbol
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'accept-language': 'en,gu;q=0.9,hi;q=0.8',
        'accept-encoding': 'gzip, deflate, br'
    }

    try:
        page = requests.get(req_url, headers=headers)
        dajs = json.loads(page.text)
        fetch_oi(dajs, expiry_dt, symbol)
    except:
        print('error getting data -' + symbol)

def add_details(dt, type_value, last_sync): # ==> ? what this function does ? ? ?
    dt.insert(2, "type", [type_value] * dt.shape[0], True)
    dt.insert(3, "last_sync", [last_sync] * dt.shape[0], True)


def fetch_oi(dajs, expiry_dt, symbol):
    ce_values = [data['CE'] for data in dajs['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
    pe_values = [data['PE'] for data in dajs['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]

    last_sync = dajs['records']['timestamp']

    ce_dt = pd.DataFrame(ce_values).sort_values(['strikePrice'])
    add_details(ce_dt, 'CE', last_sync)

    pe_dt = pd.DataFrame(pe_values).sort_values(['strikePrice'])
    add_details(pe_dt, 'PE', last_sync)

    final_dt = pd.concat([ce_dt, pe_dt], ignore_index=True).sort_values(['strikePrice'])

    try:
        final_dt.to_sql(symbol, db, if_exists='append', index=False)
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
    print(last_sync, symbol)

def main():
    start()

if __name__ == '__main__':
    main()