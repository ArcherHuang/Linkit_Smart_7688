
import sys   
import json  
import datetime 
import time
from flask import Flask
from flask import json
from flask import Response
from flask import request
import os

#f = os.popen('ifconfig br-lan | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # AP model
f = os.popen('ifconfig apcli0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # Station model
inet_addr = f.read()
app = Flask(__name__)

sys.path.insert(0, '/usr/lib/python2.7/bridge/')  
from bridgeclient import BridgeClient as bridgeclient 
value = bridgeclient()

# *****************************************************************************************
# POST http://mylinkit.local:5000/api/v1.0/turnOnOffLED
# GET  http://192.168.43.72:5000/api/v1.0/getData
# *****************************************************************************************

@app.route("/api/v1.0/getData", methods=['GET'])
def getData():	
	temperature = value.get("t")
	humidity = value.get("h")
	moisture = value.get("m")
	return json.dumps({"status": 200, "moisture": moisture,"temperature":temperature,"humidity":humidity})

if __name__ == "__main__":
	app.debug = True
	print "inet_addr: " + inet_addr
	app.run(
		host = inet_addr,
		port = 5000
	)

