
import json
import requests

#import matplotlib.pyplot as plt

#plt.rcParams['axes.facecolor'] = 'darkblue'


#import numpy as np
#from datetime import datetime


import requests
import pandas as pd
import mplfinance as mpf


#response = requests.get("https://api.coingecko.com/api/v3/coins/list", timeout=10)
#coinListData = json.loads(response.text)


with open("coinListData.json", "r") as openfile:
    coinListDataDump = json.load(openfile)

coinListData = json.loads(coinListDataDump)


def chartCoin(requestedCoin, range):
    
    #tempMessage = "Charts coming soon!"
    #print (tempMessage)
    #return tempMessage  #remove this line when chartbot is working
    
    coinId = ""

    print('request')
    print(requestedCoin)

    if requestedCoin == "flash":
        coinId = "flash-stake"
    if requestedCoin == "fli":
        coinId = "eth-2x-flexible-leverage-index"
    if requestedCoin == "eth":
        coinId = "ethereum"

    else:
        for coinItemData in coinListData:
            if coinItemData["symbol"] == requestedCoin:
                coinId = coinItemData['id']
    
    if coinId == "":
        print("Coin symbol not found")
        return "Coin symbol not found: "+requestedCoin
    
    print('Found it')
    print(coinId+"\n\n")



    try:
        
        interval = 'm'
        if (range):
            interval = range

        'default is 30 days, 2 hr sample'
        pInterval = '&days=30'
        resample = '2h'
        #1/7/14/30/90/180/365/max

        #y hy q m 2w w d max
        if (interval == 'y' or interval == 'year'):
            pInterval = '&days=365'
            resample = '1w'
        if (interval == 'h' or interval == 'halfyear'):
            pInterval = '&days=180'
            resample = '4d'
        if interval == 'q' or interval == 'quarter':
            pInterval = '&days=90'
            resample = '1d'
        if interval == 'm' or interval == 'month':
            pInterval = '&days=30'
            resample = '8h'
        if interval == '2w' or interval == '2week':
            pInterval = '&days=14'
            resample = '4h'
        if interval == 'w' or interval == 'week':
            pInterval = '&days=7'
            resample = '4h'
        if interval == 'd' or interval == 'day':
            pInterval = '&days=1'
            resample = '30min'
        if (interval == 'x' or interval == 'max'):
            pInterval = '&days=max'
            resample = '1m'

        #interval doesn't work on api  &interval=daily
        requestString = 'https://api.coingecko.com/api/v3/coins/'+coinId+'/market_chart?vs_currency=usd'+pInterval
        r = requests.get(requestString)
        print(requestString)
        d = r.json()

        #print(d) #shows resulting data from coingecko

        df = pd.DataFrame(d['prices'], columns = ['dateTime', 'price'])
        df['date'] = pd.to_datetime(df['dateTime'], unit='ms')

        #ohlcdf = df.set_index('date')['price'].resample('4h').ohlc()

        ohlcdf = df.set_index('date')['price'].resample(resample).ohlc()
        print(ohlcdf)  # shows coingecko data as a nice table
        
        #popup chart here, also save
        mpf.plot(ohlcdf,type='candle',style='yahoo', savefig='chart.png')







        #responseMarketChart = requests.get("https://api.coingecko.com/api/v3/coins/"+coinId+"/market_chart?vs_currency=usd&days=30&interval=daily", timeout=10)
        #responseMarketChart = requests.get("https://api.coingecko.com/api/v3/coins/"+coinId+"/ohlc?vs_currency=usd&days=30", timeout=10)
        #print(pd)
        #df = pd.read_json(responseMarketChart.text)
        #print(df)

        #dfPrices = df["prices"]
        #print(dfPrices)

        #dates = []
        #prices = []
        #priceSet = []
        """         
        for point in range(len(pd)):
            tmpSet = []
            tmpSet.append(datetime.utcfromtimestamp(df[point][0]/1000).strftime('%y-%b-%d'))
            tmpSet.append(df[point][1])
            tmpSet.append(df[point][2])
            tmpSet.append(df[point][3])
            tmpSet.append(df[point][4])
            priceSet.append(tmpSet)
        """
        #dates.append(datetime.utcfromtimestamp(dfPrices[price][0]/1000).strftime('%y-%b-%d'))
        #prices.append(dfPrices[price][1])


        ##datetime.utcfromtimestamp(dfPrices[price][0]/1000).strftime('%Y-%m-%d %H:%M:%S')

        ##plt.figure(figsize=(10,10))




        #fig = plt.figure()
        #fig.patch.set_facecolor('black')

        #ax=fig.add_subplot(111, label=coinId)
        #ax.plot(dates, prices, color="green")
        #ax.set_xlabel("Date", color="C0")
        #ax.set_ylabel("Price", color="C0")

        #ax.tick_params(axis='x', colors="white")
        #ax.tick_params(axis='y', colors="white")
        #plt.xticks(rotation=70, ha="right")


        #plt.title(coinId)
        
        
        #plt.show()
        #save chart as file
        #plt.savefig("chart.png")

        return "gotchart"


    except KeyError as e:
        print(e)

        print("Error generating chart for coin "+requestedCoin)
        return "Error generating chart for coin "+requestedCoin

    return




    


    #plt.subplot(args, kwargs)
    
    
    return 

