# *********************************************************************
# Version:     2016.09.06
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + MCS
# *********************************************************************
# 
# 1. update opkg & install wget & disable bridge
#    opkg update
#    opkg install wget
#    uci set yunbridge.config.disabled=0
#    uci commit
#
# 2. install mqtt
#    pip install paho-mqtt
#
# *********************************************************************

import time
import sys  
import httplib, urllib
import json

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

deviceId = "DjpJIckU"
deviceKey = "fFZLPwndLgDTggMU"


def post_to_mcs(payload):
    headers = {"Content-type": "application/json", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers)
    response = conn.getresponse()
    print( response.status, response.reason, json.dumps(payload), time.strftime("%c"))
    data = response.read()
    conn.close()

while True:
    h0 = value.get("Humidity")
    t0 = value.get("Temperature")
    payload = {"datapoints":[{"dataChnId":"Humidity","values":{"value":h0}},{"dataChnId":"Temperature","values":{"value":t0}}]}
    post_to_mcs(payload)
    time.sleep(10)
	