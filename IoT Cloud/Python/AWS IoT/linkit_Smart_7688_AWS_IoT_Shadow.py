from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import sys
import time
import json
import datetime

# Shadow JSON schema:
#
# Name: sensingData
# {
#	"state": {
#		"desired":{
#			"time":<INT VALUE>,
#			"temperature":<INT VALUE>,
#			"humidity":<INT VALUE>
#		}
#	}
#}

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient
value = bridgeclient()

# Custom Shadow callback
def customShadowCallback_Update(payload, responseStatus, token):
	# payload is a JSON string ready to be parsed using json.loads(...)
	# in both Py2.x and Py3.x
	if responseStatus == "timeout":
		print("Update request " + token + " time out!")
	if responseStatus == "accepted":
		payloadDict = json.loads(payload)
		print("~~~~~~~~~~~~~~~~~~~~~~~")
		print("Update request with token: " + token + " accepted!")
		print("property: " + str(payloadDict))
		print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
	if responseStatus == "rejected":
		print("Update request " + token + " rejected!")

def customShadowCallback_Delete(payload, responseStatus, token):
	if responseStatus == "timeout":
		print("Delete request " + token + " time out!")
	if responseStatus == "accepted":
		print("~~~~~~~~~~~~~~~~~~~~~~~")
		print("Delete request with token: " + token + " accepted!")
		print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
	if responseStatus == "rejected":
		print("Delete request " + token + " rejected!")

# Read in command-line parameters
useWebsocket = False
host = ".iot.us-east-1.amazonaws.com"
rootCAPath = "./root-CA.crt"
certificatePath = "./sensingData.cert.pem"
privateKeyPath = "./sensingData.private.key"

# Init AWSIoTMQTTShadowClient
myAWSIoTMQTTShadowClient = None
if useWebsocket:
	myAWSIoTMQTTShadowClient = AWSIoTMQTTShadowClient("shadowUpdate", useWebsocket=True)
	myAWSIoTMQTTShadowClient.configureEndpoint(host, 443)
	myAWSIoTMQTTShadowClient.configureCredentials(rootCAPath)
else:
	myAWSIoTMQTTShadowClient = AWSIoTMQTTShadowClient("shadowUpdate")
	myAWSIoTMQTTShadowClient.configureEndpoint(host, 8883)
	myAWSIoTMQTTShadowClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# Connect to AWS IoT
myAWSIoTMQTTShadowClient.connect()

# Create a deviceShadow with persistent subscription
sensingData = myAWSIoTMQTTShadowClient.createShadowHandlerWithName("sensingData", True)

# Delete shadow JSON doc
# sensingData.shadowDelete(customShadowCallback_Delete, 5)

# Update shadow
while True:
	humidity = value.get("Humidity")
	temperature = value.get("Temperature")
	print "Humi: " + humidity
	print "Temp: " + temperature
	t = time.time();
	date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
	print "humidity: %d, temperature: %d" % (float(humidity), float(temperature))
	JSONPayload = json.dumps({"state":{"desired":{"time": date, "temperature": temperature, "humidity": humidity}}})
	sensingData.shadowUpdate(JSONPayload, customShadowCallback_Update, 5)
	time.sleep(1)