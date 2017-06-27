# pip install pytz

import time
from datetime import datetime
from pytz import timezone
import pytz
import httplib
import json
import serial

s = None

def setup(): 
	global s 
	s = serial.Serial("/dev/ttyS0", 57600) 

setup()

while True:

	conn = httplib.HTTPConnection("api.coindesk.com")
	conn.request("GET", "/v1/bpi/currentprice.json")
	r1 = conn.getresponse()
	print r1.status, r1.reason

	data1 = r1.read()
	print data1

	json_obj = json.loads(data1)
	print "json_obj: \n" 

	tpe = pytz.timezone('Asia/Taipei')
	updateTime = json_obj["time"]["updatedISO"]
	datetime_obj = datetime.strptime( updateTime, "%Y-%m-%dT%H:%M:%S+00:00" )
	tpeTime = tpe.fromutc(datetime.fromtimestamp(time.mktime(datetime_obj.timetuple())))
	date_str = tpeTime.strftime("%Y-%m-%d %H:%M:%S")
	print date_str
	print date_str.split(' ')[0]
	print date_str.split(' ')[1]

	print json_obj["bpi"]["USD"]["rate"] + " " + json_obj["bpi"]["USD"]["code"]

	# stringValue = date_str.split(' ')[0] + " " + date_str.split(' ')[1] + " " + json_obj["bpi"]["USD"]["rate"] + " " + json_obj["bpi"]["USD"]["code"]
	# print stringValue
	z = "%s~%s~%s %s\n" % (date_str.split(' ')[0], date_str.split(' ')[1], json_obj["bpi"]["USD"]["rate"], json_obj["bpi"]["USD"]["code"])
	print z
	s.write(z.encode())

	time.sleep(60);
