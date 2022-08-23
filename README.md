# signal-bot

These Python script use the Signal bot created by AsamK https://github.com/AsamK/signal-cli
Please see this account for getting the Signal bot functioning first.  It allows communication between Signal chats and the scripts found here.
Note that a working Signal account is required, which in turn requires an active phone number.  
I got around this issue by getting a free phone number from an Android app (Text+ for example).


Purpose of my project is to provide cryptocurrency price bot and chart bot functionality to Signal chat, which returns price and chart data from Coingecko.com API.


Once the Signal account is working, it can be added like any other user and messaged directly, or added to chat groups.  
It will listen for valid commands and respond accordingly.


Commands:

Pricebot:
Example: /p btc

Chartbot:
Examples: /c weth
  With range: /c btc month
  Range shortcut: /c btc 2w
    Ranges (default is month): ma(x), (y)ear, (h)alfyear, (q)uarter, (m)onth, (2w)eek,(w)eek, (d)ay
        
Misc. Commands:
  Market Data: /cap
  ETH/BTC Dominance: /ethbtc
  Refresh coin list: /refresh
  Help screen for these commands: /?

