# ************************************************************************************
# Version:     2016.03.19 
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + WebSocket-based MQTT 
# ************************************************************************************
#
# 1. Build from source
#    git clone https://github.com/aws/aws-iot-device-sdk-python.git
#    cd aws-iot-device-sdk-python
#    python setup.py install
#
# 2. OpenSSL version 1.0.1+ (TLS version 1.2) compiled with the Python executable for X.509 certificate-based mutual authentication
#    To check your version of OpenSSL, use the following command in a Python interpreter:
#
#    python
#    import ssl
#    ssl.OPENSSL_VERSION
#    control + z
#
# 3. export AWS_ACCESS_KEY_ID=<your aws access key id string>
#    export AWS_SECRET_ACCESS_KEY=<your aws secret access key string>
#
# 4. export -p 
#
# 5. update opkg & bridge
# 	 opkg update
# 	 uci set yunbridge.config.disabled=0
# 	 uci commit
#    reboot

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import time
import datetime
import json

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient
value = bridgeclient()

host = ".iot.us-east-1.amazonaws.com"
rootCAPath = "./root-CA.crt"

# Custom MQTT message callback
def customCallback(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")

myAWSIoTMQTTClient = AWSIoTMQTTClient("basicPubSub", useWebsocket=True)
myAWSIoTMQTTClient.configureEndpoint(host, 443)
myAWSIoTMQTTClient.configureCredentials(rootCAPath)

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe("sensingData/TemperatureHumidity/Room2", 1, customCallback)
time.sleep(2)

# Publish to the same topic in a loop forever
while True:
	humidity = value.get("Humidity")
	temperature = value.get("Temperature")
	print "Humi: " + humidity
	print "Temp: " + temperature

	t = time.time();
	date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
	print "humidity: %d, temperature: %d" % (float(humidity), float(temperature))
	myAWSIoTMQTTClient.publish("sensingData/TemperatureHumidity/Room2", json.dumps({"time": date, "temperature": temperature, "humidity": humidity}), 1)
	time.sleep(1)