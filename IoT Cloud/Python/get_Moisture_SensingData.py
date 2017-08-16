# **************************************************************************************************************************
# Version:     2017.8.16 
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge
# **************************************************************************************************************************
# 
# 1. update opkg & install wget & disable bridge
# 	 opkg update
# 	 uci set yunbridge.config.disabled=0
# 	 uci commit
#        reboot

import sys  
import time

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

while True:
	h0 = value.get("m")
	print "Humi: " + h0
	time.sleep(1);