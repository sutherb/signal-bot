
import json
import requests
import locale

#import math
#import cmd, sys

#import re
#from gi.repository import GLib
#loop = GLib.MainLoop()

locale.setlocale(locale.LC_ALL, '')



with open("coinListData.json", "r") as openfile:
    coinListDataDump = json.load(openfile)

coinListData = json.loads(coinListDataDump)


def coinListDataRefresh():
    response = requests.get("https://api.coingecko.com/api/v3/coins/list", timeout=10)
    coinListData = json.loads(response.text)
    coinListDataDump = json.dumps(response.text)


    with open("coinListData.json", "w") as outfile:
        outfile.write(coinListDataDump)

    return


def formatPrice(price):
    priceAsNumber = float(price)
    coinPriceString = ""
 
    if priceAsNumber > 100:
        coinPriceString = str(locale.currency(priceAsNumber, symbol=False, grouping=True)).split('.')[0]
    if priceAsNumber <= 100 and priceAsNumber >= 1 :
        coinPriceString = str(locale.currency(priceAsNumber, symbol=False, grouping=True))
    if priceAsNumber < 1 and priceAsNumber >= 0.05:
        smallPrice = "%.2f" % priceAsNumber
        coinPriceString = str(smallPrice)
    if priceAsNumber < 0.05 and priceAsNumber >= 0.0005:
        smallPrice = "%.4f" % priceAsNumber
        coinPriceString = str(smallPrice)
    if priceAsNumber < 0.0005:
        smallPrice = "%.8f" % priceAsNumber
        coinPriceString = str(smallPrice)

    return coinPriceString


def spacer(text, spaces):
    if len(text) == (spaces -1):
        return " "+text
    if len(text) == (spaces -2):
        return "  "+text
    if len(text) == (spaces -3):
        return "   "+text
    if len(text) == (spaces -4):
        return "    "+text
    
    return text


def emojiRange(percent):

    if percent < -70:
        return "🚮"
    if percent >= -70 and percent < -60:
        return "💥"
    if percent >= -60 and percent < -50:
        return "💣"
    if percent >= -50 and percent < -40:
        return "💀"
    if percent >= -40 and percent < -30:
        return "😱"
    if percent >= -30 and percent < -25:
        return "😨"
    if percent >= -25 and percent < -20:
        return "😲"
    if percent >= -20 and percent < -15:
        return "😢"
    if percent >= -15 and percent < -10:
        return "😰"
    if percent >= -10 and percent < -5:
        return "😅"
    if percent >= -5 and percent < -2:
        return "😔"
    if percent >= -2 and percent < -1:
        return "😑"
    if percent >= -1 and percent < 0:
        return "😕"
    if percent >= 0 and percent < 1:
        return "😏"
    if percent >= 1 and percent < 2:
        return "😄"
    if percent >= 2 and percent < 3:
        return "😀"
    if percent >= 3 and percent < 5:
        return "😮"
    if percent >= 5 and percent < 10:
        return "🍻"
    if percent >= 10 and percent < 15:
        return "🎉"
    if percent >= 15 and percent < 20:
        return "💸"
    if percent >= 20 and percent < 25:
        return "💰"
    if percent >= 25 and percent < 30:
        return "🔥"
    if percent >= 30 and percent < 40:
        return "🌙"
    if percent >= 40 and percent < 50:
        return "🌗"
    if percent >= 50 and percent < 60:
        return "🌕"
    if percent >= 60 and percent < 70:
        return "⭐"
    if percent >= 70 and percent < 80:
        return "🚀"
    if percent >= 80 and percent < 90:
        return "🎆"
    if percent >= 90 and percent < 100:
        return "🌌"
    if percent >= 100:
        return "✨"


def findRatio():
                    
    responseUSD = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&id=btc,eth", timeout=10)
    coinData = json.loads(responseUSD.text)

    priceBTC = coinData[0]["current_price"]
    priceETH = coinData[1]["current_price"]

    ratio = str(priceETH / priceBTC)

    returnMessage = "ETH/BTC ratio is "+ratio[0:6]+""
    print (returnMessage)
    return returnMessage


"""
/gas

🛴 Safe Low: 77 Gwei < 30mins 
:car: Normal: 84 GWei <5 min
🏍 Fast: 101 GWei <1 min
🏎 Fastest: 111 GWei 1-2 Blocks



"""


def findCoin(requestedCoin):

    coinId = ""

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
        
        responseUSD = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&price_change_percentage=1h,24h,7d&ids=" + coinId, timeout=10)
        coinData = json.loads(responseUSD.text)
        responseSAT = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=btc&ids=" + coinId, timeout=10)
        coinDataSAT = json.loads(responseSAT.text)
        responseETH = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=eth&ids=" + coinId, timeout=10)
        coinDataETH = json.loads(responseETH.text)

        coinPrice = coinData[0]["current_price"]
        coinSatPrice = "%.8f" % coinDataSAT[0]["current_price"]
        coinEthPrice = "%.6f" % coinDataETH[0]["current_price"]

        coinPriceString = formatPrice(coinPrice)
        coinPriceStringSat = coinSatPrice
        coinPriceStringEth = coinEthPrice

        coinName = str(coinData[0]["name"])
        coinSymbol = str(requestedCoin).upper()
        coinLow24h = str(formatPrice(coinData[0]["low_24h"]))
        coinHigh24h = str(formatPrice(coinData[0]["high_24h"]))

        coinPriceChange1h = spacer(str("%.1f" % coinData[0]["price_change_percentage_1h_in_currency"]), 7)
        coinPriceChange24h = spacer(str("%.1f" % coinData[0]["price_change_percentage_24h_in_currency"]), 7)
        coinPriceChange7d = spacer(str("%.1f" % coinData[0]["price_change_percentage_7d_in_currency"]), 7)
        
        coinMarketCapRank = str(coinData[0]["market_cap_rank"])
        coinMarketCap = str(formatPrice(coinData[0]["market_cap"]))
        coinTotalVol = str(formatPrice(coinData[0]["total_volume"]))


        icon1h = emojiRange(coinData[0]["price_change_percentage_1h_in_currency"])
        icon24h = emojiRange(coinData[0]["price_change_percentage_24h_in_currency"])
        icon7d = emojiRange(coinData[0]["price_change_percentage_7d_in_currency"])

        returnMessage = (coinName+" ("+coinSymbol+")\n"
            "==========================\n"
            "Price: $"+coinPriceString+"\n"+coinPriceStringSat+" ₿ | "+coinPriceStringEth+" Ξ\n"
            "24h Low:  $"+coinLow24h+"\n"
            "24h High: $"+coinHigh24h+"\n"
            "1h:  "+coinPriceChange1h+"%  "+icon1h+"\n"
            "24h: "+coinPriceChange24h+"%  "+icon24h+"\n"
            "7d:  "+coinPriceChange7d+"%  "+icon7d+"\n"
            "Cap: # "+coinMarketCapRank+" | $"+coinMarketCap+"\n"
            "Vol: $"+coinTotalVol+"\n"
        )
        

        print (returnMessage)

        return returnMessage

    except KeyError:
        print("Error retrieving coin "+requestedCoin)
        return "Error retrieving coin "+requestedCoin

    return



"""
def msgRcv (message):
    print ("Message:\n", message)  #, "received in group", signal.getGroupName (groupID)
  
    messageSwitch = re.split(r'\ +', message)

    if messageSwitch[0] == "/p":
        
        print (messageSwitch[1])
        coinSymbol = messageSwitch[1].lower()
        
        if coinSymbol == "ethbtc":
            findRatio()
        else:
            findCoin(coinSymbol)

    if messageSwitch[0] == "/c":
        coinSymbol = messageSwitch[1].lower()

        generateChart(coinSymbol)

        



    return

"""

#message = input("Type switch with command (example: /p btc): ")
#msgRcv(message)



""" 

def msgRcv (timestamp, source, groupID, message, attachments):
     print ("Message:\n", message)  #, "received in group", signal.getGroupName (groupID)
  
    messageSwitch = re.split(r'\ +', message)

    if messageSwitch[0] == "/p":
        print (messageSwitch[1])
        coinSymbol = messageSwitch[1]
        findCoin(coinSymbol)




    return


signal.onMessageReceived = msgRcv




loop.run()



 """