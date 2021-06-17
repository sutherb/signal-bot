
import json
import requests

#import matplotlib.pyplot as plt

#plt.rcParams['axes.facecolor'] = 'darkblue'

#import pandas as pd
#import numpy as np
#from datetime import datetime


import requests
import pandas as pd
import mplfinance as mpf


response = requests.get("https://api.coingecko.com/api/v3/coins/list", timeout=10)
coinListData = json.loads(response.text)



def chartCoin(requestedCoin):
    
    #tempMessage = "Charts coming soon!"
    #print (tempMessage)
    #return tempMessage  #remove this line when chartbot is working
    
    coinId = ""


    print(requestedCoin)

    if requestedCoin == "flash":
        coinId = "flash-stake"
    if requestedCoin == "fli":
        coinId = "eth-2x-flexible-leverage-index"
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

        pInterval = '&days=7
        #1/7/14/30/90/180/365/max
        if interval == 'y':
            pInterval = '&days=365'
            resample = '2h'
        if interval == 'q':
            pInterval = '&days=90'
            resample = '2h'
        if interval == 'm':
            pInterval = '&days=30'
            resample = '24h'
        if interval == 'w':
            pInterval = '&days=7'
            resample = '2h'
        if interval == 'd':
            pInterval = '&days=1'
            resample = '2h'

        #interval doesn't work on api  &interval=daily
        r = requests.get('https://api.coingecko.com/api/v3/coins/'+coinId+'/market_chart?vs_currency=usd'+pInterval)
        d = r.json()

        #print(d)

        df = pd.DataFrame(d['prices'], columns = ['dateTime', 'price'])
        df['date'] = pd.to_datetime(df['dateTime'], unit='ms')

        #ohlcdf = df.set_index('date')['price'].resample('4h').ohlc()

        ohlcdf = df.set_index('date')['price'].resample(resample).ohlc()
        print(ohlcdf)
        mpf.plot(ohlcdf,type='candle',style='yahoo')



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
        ##plt.savefig("chart.png")

        returnMessage = "getchart"

        #print (returnMessage)

        return returnMessage

    except KeyError as e:
        print(e)

        print("Error generating chart for coin "+requestedCoin)
        return "Error generating chart for coin "+requestedCoin

    return




    


    #plt.subplot(args, kwargs)
    
    
    return 

