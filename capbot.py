import json
import requests
import locale

locale.setlocale(locale.LC_ALL, '')


def marketCap():
    
    response = requests.get("https://api.coingecko.com/api/v3/global", timeout=10)
    responseBTC = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin", timeout=10)
    marketData = json.loads(response.text)
    bitcoinData = json.loads(responseBTC.text)

    #divide btc marketcap by dominance to get total, gecko won't directly give this value..

    btcDominance = marketData["data"]["market_cap_percentage"]["btc"]
    btcDominanceStr = "%.1f" % btcDominance

    btcMarketcap = marketData["data"]["total_market_cap"]["btc"]
    btcMarketvol = marketData["data"]["total_volume"]["btc"]
    ethMarketcap = marketData["data"]["total_market_cap"]["eth"]

    ethbtcRatio = btcMarketcap / ethMarketcap
    ethbtcRatioStr = "%.4f" % ethbtcRatio

    
    priceBTC = bitcoinData[0]["current_price"]
    marketcapTotal = btcMarketcap * priceBTC / 1000000000
    marketcapTotalStr = str(locale.currency(marketcapTotal, symbol=False, grouping=True)).split('.')[0]

    marketVolTotal = btcMarketvol * priceBTC / 1000000000
    marketVolTotalStr = str(locale.currency(marketVolTotal, symbol=False, grouping=True)).split('.')[0]

    returnMessage = ("Current Crypto Market Data\n"
        "==========================\n"
        "Overall Marketcap: $" + marketcapTotalStr + " billion\n"
        "Overall Market Vol:  $" + marketVolTotalStr + " billion\n"
        "Bitcoin Dominance: " + btcDominanceStr + "%\n"
        "ETH/BTC ratio:     " + ethbtcRatioStr 
    )
    
    print(returnMessage)
    return returnMessage
