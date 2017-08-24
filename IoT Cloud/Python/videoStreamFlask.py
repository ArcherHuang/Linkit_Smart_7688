# pip install flask
# http://mylinkit.local:8080/?action=stream

from flask import Flask
from flask import json
from flask import Response
from flask import request
import os

#f = os.popen('ifconfig br-lan | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # AP model
f = os.popen('ifconfig apcli0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # Station model

inet_addr = f.read()
app = Flask(__name__)

# *****************************************************************************************
# POST http://mylinkit.local:5000/api/v1.0/videoOn
# *****************************************************************************************
@app.route("/api/v1.0/videoOn", methods=['GET'])
def setvideoon():
	os.system('mjpg_streamer -i "input_uvc.so -r 640x480 -f 15 -d /dev/video0" -o "output_http.so"')
	return json.dumps({"status": 200, "comment": "call video on Finish"})

if __name__ == '__main__': 
	app.debug = True
	#print "inet_addr: " + inet_addr
	app.run(
		host = inet_addr,
		port = 5000
	)