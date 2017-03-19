import time
import sys
import ibmiotf.application
import ibmiotf.device
import json

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

deviceOptions = {
  "org": "組織 ID",
  "type": "裝置類型",
  "id": "裝置 ID",
  "auth-method": "token",
  "auth-token": "鑑別記號"
}

try:
	deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
	humidity = value.get("h")
	temperature = value.get("t")
	msg = json.JSONEncoder().encode({"d":{"Temperature":temperature, "Humidity":humidity}})
	print "send payload: " + msg
	deviceCli.publishEvent("TemperatureHumidity", "json", msg)
	time.sleep(1)
