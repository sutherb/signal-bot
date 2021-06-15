
import re
import os
import base64

from pydbus import SessionBus
from gi.repository import GLib

from pricebot import findCoin, findRatio
from capbot import marketCap
from chartbot import chartCoin
from filebot import getFile


bus = SessionBus()
loop = GLib.MainLoop()


signal = bus.get('org.asamk.Signal')




def msgRcv (timestamp, source, groupID, message, attachments):
    print ("Message:\n", message)  
  
    messageSwitch = re.split(r'\ +', message)

    print (source)
    print (groupID)
    print (message)

    returnMessage = ""
    
    if len(messageSwitch) > 0:
        
        print(messageSwitch[0])

        if messageSwitch[0] == "/cap":
            marketCap()            

        if messageSwitch[0] == "/p":
            args = messageSwitch[1].lower()    
            print (messageSwitch[1])

            if args == "ethbtc":
                findRatio()
            else:
                findCoin(args)


        if messageSwitch[0] == "/c":
            args = messageSwitch[1].lower()
            coinSymbol = messageSwitch[1].lower()

            chartCoin(args)


    attachment = []
    if returnMessage == "getchart":
        attachment = getFile(returnMessage)


    if groupID:
        signal.sendGroupMessage(returnMessage, attachment, groupID)
    else:
        signal.sendMessage(returnMessage, attachment, [source])  #sometimes phone number (source) must be in a list [], and sometimes not!
        


    #can just add bot by phone # in signal.  no need for logic to approve invite, just happens
    #if messageSwitch[0] == "/join":
    #    print (messageSwitch[1])
    #    groupLink = str(messageSwitch[1])
    #    os.system('date') 
    #    os.system('./signal-cli -u +14377009675 joinGroup --uri "'+groupLink+'"')


    return

    
    
signal.onMessageReceived = msgRcv

loop.run()