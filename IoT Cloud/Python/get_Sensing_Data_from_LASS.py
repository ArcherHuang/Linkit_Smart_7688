import paho.mqtt.client as mqtt
import re
import sys

# *********************************************************************
MQTT_SERVER = "gpssensor.ddns.net"
MQTT_PORT = 1883
MQTT_ALIVE = 60
#MQTT_TOPIC = "LASS/Test/PM25"
#MQTT_TOPIC = "DeveloperTest"
MQTT_TOPIC = "LASS/Test/#"

LASS_DEVICE_ID="Archer_Temp_Humi_Dust"
# *********************************************************************

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print("mqtt payload=%s" %(msg.payload))
    items = re.split('\|',str(msg.payload))
    for item in items:
    	#print "item: " + item
        if item == '':
            continue 
        pairs = re.split('=',item)
        #print "pairs[0]: " + pairs[0]
        #print "pairs[1]: " + pairs[1]
        if (len(items)==1):
            continue
        if (pairs[0] == "device_id"):
            value_devId = pairs[1]
        elif (pairs[0] == "s_d0"):
            value_dust = pairs[1]
        elif (pairs[0] == "s_t0"):
            value_temperature = pairs[1]
        elif (pairs[0] == "s_h0"):
            value_humidity = pairs[1]

    try:
        print "value_devId:" + value_devId
        print "LASS_DEVICE_ID:" + LASS_DEVICE_ID
        if (value_devId == LASS_DEVICE_ID):
            print("mqtt payload=%s" %(msg.payload))
    except:
        return
         
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)
mqtt_client.loop_forever()