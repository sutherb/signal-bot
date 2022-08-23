
import re
import os
import base64

from pydbus import SessionBus
from gi.repository import GLib

from pricebot import findCoin, findRatio, coinListDataRefresh
from capbot import marketCap
from chartbot import chartCoin
from help import helpScreen




def msgRcv (message):
    print ("Message:\n", message)  #, "received in group", signal.getGroupName (groupID)
  
    messageSwitch = re.split(r'\ +', message)
    messageLength = len(messageSwitch)

    if messageLength > 0 and messageLength < 2:
        
        print(messageSwitch[0])

        if messageSwitch[0] == "/refresh":
            coinListDataRefresh()

        if messageSwitch[0] == "/cap":
            marketCap()

        if messageSwitch[0] == "/ethbtc":
            findRatio()

        if messageSwitch[0] == "/?":
            helpScreen()

    if messageLength >= 2:
        args = messageSwitch[1].lower()

        if messageSwitch[0] == "/p":
                
            print (messageSwitch[1])

            if args == "ethbtc":
                findRatio()
            else:
                findCoin(args)


        if messageSwitch[0] == "/c":
            
            coinSymbol = messageSwitch[1].lower()
            range = ''
            if (len(messageSwitch) > 2):
                range = messageSwitch[2].lower()

            print (range)
            chartCoin(coinSymbol, range)
            


    return



message = input("Type switch with command (example: /p btc): ")
msgRcv(message)


