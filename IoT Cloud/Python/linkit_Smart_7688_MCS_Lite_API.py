import time
import sys  
import httplib, urllib
import json

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

deviceId = "B1trqusM-"
deviceKey = "bd2f16cd1d7883f9b07861a38838539ab944745e3adcf6af5f6ed3dd36e67732"
serverIP = "192.168.43.85"
serverPort = "3000"


def post_to_mcslite(payload):
    headers = {"Content-type": "text/csv", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection( serverIP + ":" + serverPort )
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10) 

    conn.request("POST", "/api/devices/" + deviceId + "/datapoints.csv", payload, headers)
    response = conn.getresponse()
    print( response.status, response.reason, payload, time.strftime("%c"))
    data = response.read()
    conn.close()

while True:
    value = bridgeclient()
    h0 = value.get("h")
    t0 = value.get("t")
    t0String = "Temperature,," + t0
    h0String= "Humidity,," + h0
    payload =  t0String + "\n" + h0String + "\n"
    post_to_mcslite(payload)
    time.sleep(10)