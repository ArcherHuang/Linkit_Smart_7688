# *********************************************************************
# Version:     2016.06.30 
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + LASS
# *********************************************************************
# 
# 1. update opkg & disable bridge
# 	 opkg update
# 	 uci set yunbridge.config.disabled=0
# 	 uci commit
#
# 2. install mqtt & httplib
#	 pip install paho-mqtt
#
# *********************************************************************

import time
import sys  
import paho.mqtt.client as mqtt
import os

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient
value = bridgeclient()


# *********************************************************************
# MQTT Config

MQTT_SERVER = "gpssensor.ddns.net"
MQTT_PORT = 1883
MQTT_ALIVE = 60
#MQTT_TOPIC = "LASS/Test/PM25"
#MQTT_TOPIC = "DeveloperTest"
#MQTT_TOPIC = "LASS/Test/#"
MQTT_TOPIC = "LASS/Test/PM25"

# *********************************************************************
# Data Format
# https://lass.hackpad.com/LASS-Data-specification-1dYpwINtH8R

ver_format=3
fmt_opt=1
app="LinkItSmart7688-Archer"
ver_app="0.0.3"
device_id="Archer_Temp_Humi_Dust"
device="LinkItSmart7688Duo"
tick=0
datestr="2016-08-30"
timestr="15:50:01"
gps_fix=0
gps_num=0
gps_alt=0
gps_lat=25.0336762
gps_lon=121.5404092

#msg example
packstr = "|ver_format=%i|fmt_opt=%i|app=%s|ver_app=%s|device_id=%s|device=%s" % (ver_format,fmt_opt,app,ver_app,device_id,device)
packstr_fix = "|tick=%i|date=%s|time=%s|gps_fix=%i|gps_num=%i|gps_alt=%i|gps_lat=%f|gps_lon=%f" % (tick,datestr,timestr,gps_fix,gps_num,gps_alt,gps_lat,gps_lon)
print "%s%s" %(packstr,packstr_fix)

# *********************************************************************

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)	

while True:
    d0 = value.get("d")
    h0 = value.get("h")
    t0 = value.get("t")

    packstr_sensor="|s_t0=%s|s_h0=%s|s_d0=%s" %(t0,h0,d0)
    payload = packstr + packstr_fix + packstr_sensor

    print "send payload: " + payload
    print "packstr_sensor: " + packstr_sensor

    mqtt_client.publish(MQTT_TOPIC, payload, qos=1)
    time.sleep(10)