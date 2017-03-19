import serial 
import time
from flask import Flask
from flask import json
from flask import Response
from flask import request
import os

s = None
#f = os.popen('ifconfig br-lan | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # AP model
f = os.popen('ifconfig apcli0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # Station model
inet_addr = f.read()
app = Flask(__name__)

# *********************************************************************
# open serial COM port to /dev/ttyS0, which maps to UART0(D0/D1)
# the baudrate is set to 57600 and should be the same as the one
# specified in the Arduino sketch uploaded to ATMega32U4.
# *********************************************************************

def setup(): 
  global s 
  s = serial.Serial("/dev/ttyS0", 57600) 

# *****************************************************************************************
# POST http://mylinkit.local:5000/api/v1.0/turnOnOffLED
# *****************************************************************************************
@app.route("/api/v1.0/turnOnOffLED", methods=['POST'])
def setvideoon():
	value = request.form['value']
	if value == 'on':
		s.write("1") 
	else:
		s.write("0")	
	return json.dumps({"status": 200, "comment": "call turnOnOffLED Finish"})

if __name__ == '__main__': 
	setup() 
	app.debug = True
	#print "inet_addr: " + inet_addr
	app.run(
		host = inet_addr,
		port = 5000
	)