import signal
import time
import sys
import json
import ibmiotf.application

def myEventCallback(myEvent):
	print("%-33s%-32s%s: %s" % (myEvent.timestamp.isoformat(), myEvent.device, myEvent.event, json.dumps(myEvent.data)))

def interruptHandler(signal, frame):
	client.disconnect()
	sys.exit(0)


options = {
  "org": "組織 ID",
  "id": "裝置 ID",
  "auth-method": "apikey",
  "auth-key": "API 金鑰",
  "auth-token": "鑑別記號"
}

try:
	client = ibmiotf.application.Client(options)
	client.connect()
except Exception as e:
	print(str(e))
	sys.exit()

print("(Press Ctrl+C to disconnect)")
client.deviceEventCallback = myEventCallback
client.subscribeToDeviceEvents()

while True:
	time.sleep(1)
