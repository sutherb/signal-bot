
import json
import requests
import locale

import os

from semaphore import Bot, ChatContext



locale.setlocale(locale.LC_ALL, '')

response = requests.get("https://api.coingecko.com/api/v3/coins/list")
coinListData = json.loads(response.text)

requestedCoin = "btc"

foundCoinId = ''

for coinItemData in coinListData:
    if coinItemData["symbol"] == requestedCoin:
        try:
            print('Found it')
            foundCoinId = coinItemData['id']
        except KeyError:
            print("Coin symbol not found")



response2 = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=" + foundCoinId)
coinData = json.loads(response2.text)



print("Price for "+ requestedCoin)
print(locale.currency(coinData[0]["current_price"]))



response = requests.get("https://api.coingecko.com/api/v3/coins/list")
coinListData = json.loads(response.text)


def findCoin(requestedCoin):

  foundCoinId = ""

  for coinItemData in coinListData:
    if coinItemData["symbol"] == requestedCoin:
      try:
        print('Found it')
        foundCoinId = coinItemData['id']
        print(foundCoinId)

        #return locale.currency(coinData[0]["current_price"])

      except KeyError:
        print("exception, coin not found")
        return "Error retrieving coin "+requestedCoin

  if foundCoinId == "":
    print("Coin symbol not found")
    return "Error retrieving coin '"+requestedCoin+"'"

  response2 = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=" + foundCoinId)
  coinData = json.loads(response2.text)

  return "Current price of "+requestedCoin+" is "+locale.currency(coinData[0]["current_price"])

  #print("Price for "+ requestedCoin)
  #print(locale.currency(coinData[0]["current_price"]))


async def echo(ctx: ChatContext) -> None:
  if not ctx.message.empty():
    
    await ctx.message.typing_started()


    #requestedCoin = "btc"

    #requestedCoin = ctx.message.get_body()
    
    parsedMessage = ctx.message.get_body()

    requestedCoin = parsedMessage
    


    await ctx.message.reply(findCoin(requestedCoin))
    #await ctx.message.reply("Current price of "+requestedCoin+" is "+findCoin(requestedCoin))
    
    #await ctx.message.reply(ctx.message.get_body())
    await ctx.message.typing_stopped()


async def main():
  """Start the bot."""
  # Connect the bot to number.
  async with Bot(os.environ["SIGNAL_PHONE_NUMBER"]) as bot:
    bot.register_handler("", echo)

    # Run the bot until you press Ctrl-C.
    await bot.start()



if __name__ == '__main__':
    import anyio
    anyio.run(main)




