import paho.mqtt.client as mqtt
import re
import httplib, urllib
import socket
import sys
import time

# *********************************************************************
MQTT_SERVER = "gpssensor.ddns.net"
MQTT_PORT = 1883
MQTT_ALIVE = 3600
MQTT_TOPIC = "LASS/Test/#"
#MQTT_TOPIC = "DeveloperTest"

LASS_DEVICE_ID="Archer_Temp_Humi_Dust"
ThingSpeak_API_Key = "SXGI1HG16NIQVBIK"
# *********************************************************************

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("mqtt payload=%s" %(msg.payload))
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
        if (value_devId == LASS_DEVICE_ID):
            params = urllib.urlencode({'field1': value_dust, 'field2': value_temperature, 'field3': value_humidity, 'key': ThingSpeak_API_Key})
            print "params: " + params
            post_to_thingspeak(params)
    except:
         return

# Post the data to ThingSpeak
def post_to_thingspeak(payload):
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("api.thingspeak.com:80")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/update", payload, headers)
    response = conn.getresponse()
    print( response.status, response.reason, payload, time.strftime("%c"))
    data = response.read()
    conn.close()


mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)
mqtt_client.loop_forever()