# **************************************************************************************************************************
# Version:     2016.06.30 
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + WoT
# **************************************************************************************************************************
# 
# 1. update opkg & install wget & disable bridge
# 	 opkg update
# 	 opkg install wget
# 	 uci set yunbridge.config.disabled=0
# 	 uci commit
#
# 2. install setuptools
#	 curl https://bootstrap.pypa.io/ez_setup.py -k -o - | python
#
# 3. install six
# 	 wget --no-check-certificate https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz
# 	 tar zxvf six-1.10.0.tar.gz
#	 cd six-1.10.0
#	 python setup.py install
#
# 4. install Websocket
#	 wget --no-check-certificate https://pypi.python.org/packages/source/w/websocket-client/websocket_client-0.32.0.tar.gz
#	 tar zxvf websocket_client-0.32.0.tar.gz
#	 cd websocket_client-0.32.0
#	 python setup.py install
# 
# Dashboard
# 	http://52.42.77.220/dashboard/index.html#57615d8a54242e1f2a000ee5
# **************************************************************************************************************************

import time
import sys  
import websocket
import datetime

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient
value = bridgeclient()

websocket.enableTrace(True)
ws = websocket.create_connection("ws://wot.city/object/584132afe8dfd8d226000365/send")

while True:
	h0 = value.get("h")
	t0 = value.get("t")
	print "Humi: " + h0
	print "Temp: " + t0
	
	t = time.time();
	date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
	vals = "{\"date\":\""+date+"\",\"temperature\":"+t0+",\"h\":"+h0+"}"
	time.sleep(1);
	ws.send(vals);
	print vals;