# signal-bot

These Python scripts use the Signal bot created by AsamK https://github.com/AsamK/signal-cli
Please see this account for getting the Signal bot functioning first.  It allows communication between Signal chats and the scripts found here.
Note that a working Signal account is required, which in turn requires an active phone number.

Purpose of this project is to provide cryptocurrency price bot and chart bot functionality to Signal chat, which returns price and chart data from Coingecko.com API.
This is for personal use.

Keep in mind any chat the Signal account used is added to can access all messages in those chats (required so the script can detect commands)


Once the Signal account is working, it can be added like any other user and messaged directly, or added to chat groups.  

First run the AsamK script, then run signalswitch.py 


To test just the scripts being used without bothering with Signal, use testswitch.py in a terminal and you can just enter commands as if you were in Signal.



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


