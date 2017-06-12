# ************************************************************************************************************
# Version:     2017.06.12 
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + Blynk App
# ************************************************************************************************************
# 
# 1. update opkg & disable bridge & commit& reboot
# 	 opkg update
# 	 uci set yunbridge.config.disabled=0
# 	 uci commit
#    reboot
#
# Reference
#    http://docs.blynkapi.apiary.io/#reference
# ************************************************************************************************************

from urllib2 import Request, urlopen
import time
import sys

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

auth_token = "2354861abd2541febd7ad25f604d57bf"

while True:
    value = bridgeclient()
    t0 = value.get("t")
    h0 = value.get("h")
    print "Temp: " + t0
    print "Humi: " + h0

    if float(t0) > 20:
        values = """
        {
            "body": "Temperature > 20"
        }
        """

        headers = {
            'Content-Type': 'application/json'
        }

        request = Request("http://blynk-cloud.com/" + auth_token + "/notify", data=values, headers=headers)

        response_body = urlopen(request).read()
        print response_body

    time.sleep(10)