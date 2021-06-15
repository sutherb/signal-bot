def msgRcv (timestamp, source, groupID, message, attachments):
   print ("Message", message)  #, "received in group", signal.getGroupName (groupID)
   return

from pydbus import SessionBus
from gi.repository import GLib

bus = SessionBus()
loop = GLib.MainLoop()

signal = bus.get('org.asamk.Signal')

signal.onMessageReceived = msgRcv
loop.run()