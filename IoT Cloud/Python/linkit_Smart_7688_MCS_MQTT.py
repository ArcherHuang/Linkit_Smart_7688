# *********************************************************************
# Version:     2016.09.06
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + MCS
# *********************************************************************
# 
# 1. update opkg & disable bridge & install paho-mqtt
# 	 opkg update
# 	 uci set yunbridge.config.disabled=0
# 	 uci commit
#    pip install paho-mqtt
#    reboot
# *********************************************************************

import paho.mqtt.client as mqtt
import time
import sys  
import json

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient
value = bridgeclient()

# *********************************************************************
# MQTT Config

deviceId = "DBKHFNIw"
deviceKey = "8fszdReA51m0vRjq"
dataChnId1 = "Temperature"
dataChnId2 = "Humidity"
MQTT_SERVER = "mqtt.mcs.mediatek.com"
MQTT_PORT = 1883
MQTT_ALIVE = 60
MQTT_TOPIC1 = "mcs/" + deviceId + "/" + deviceKey + "/" + dataChnId1
MQTT_TOPIC2 = "mcs/" + deviceId + "/" + deviceKey + "/" + dataChnId2

# *********************************************************************

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)	

while True:
    h0 = value.get("h")
    t0 = value.get("t")
    payload = {"dataChnId":dataChnId1,"value":t0}
    print dataChnId1 + " : " + t0
    mqtt_client.publish(MQTT_TOPIC1, json.dumps(payload), qos=1)
    payload = {"dataChnId":dataChnId2,"value":h0}
    print dataChnId2 + " : " + h0
    mqtt_client.publish(MQTT_TOPIC2, json.dumps(payload), qos=1)
    time.sleep(1)