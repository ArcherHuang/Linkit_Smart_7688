# *****************************************************************************************
# Version:     2016.06.30 
# Author:      Archer Huang
# License:     MIT
# Description: Get Sensing Data from WoT.City
# *****************************************************************************************

import websocket

websocket.enableTrace(True)
ws = websocket.create_connection("ws://wot.city/object/584132afe8dfd8d226000365/viewer")

while True:
	result = ws.recv()
	print "Received '%s'" % result