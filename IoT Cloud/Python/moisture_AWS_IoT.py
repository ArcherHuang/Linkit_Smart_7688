from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient  
import sys  
import logging  
import time  
import getopt  
import json  
import datetime

# Read in command-line parameters
host = "a3iprlpgye4dmu.iot.us-east-1.amazonaws.com"  
rootCAPath = "./root-CA.crt"  
certificatePath = "./.cert.pem"  
privateKeyPath = "./.private.key"

myAWSIoTMQTTClient = AWSIoTMQTTClient("publish")  
myAWSIoTMQTTClient.configureEndpoint(host, 8883)  
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)  
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing  
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz  
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec  
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()

sys.path.insert(0, '/usr/lib/python2.7/bridge/')  
from bridgeclient import BridgeClient as bridgeclient  
value = bridgeclient()

# Publish to the same topic in a loop forever
while True:  
    moisture = value.get("m")
    print "moisture: " + moisture

    t = time.time();
    date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
    
    myAWSIoTMQTTClient.publish("sensingData/Moisture/Room1", json.dumps({"time": date, "Moisture": moisture}), 1)
    time.sleep(1)