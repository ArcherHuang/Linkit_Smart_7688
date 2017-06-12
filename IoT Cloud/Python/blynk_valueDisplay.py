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

auth_token = "9417dea3d1a248549cf3df7008785282"
input_pin = "V0"

while True:
    value = bridgeclient()
    t0 = value.get("t")
    h0 = value.get("h")
    print "Temp: " + t0
    print "Humi: " + h0

    requestString = "http://blynk-cloud.com/" + auth_token + "/update/" + input_pin + "?value=" + t0
    print "requestString: " + requestString
    # http://blynk-cloud.com/9417dea3d1a248549cf3df7008785282/update/V0?value=1234

    request = Request(requestString)
    response_body = urlopen(request).read()
    print response_body

    time.sleep(10)