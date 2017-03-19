# ******************************************************************************************
# Import Package                                                                           #
# ******************************************************************************************

import sys
import time
import datetime
import requests
import json

# ******************************************************************************************
# Set Firebase URL, Date, Time, Location                                                   #                                                                         #
# ******************************************************************************************

firebase_url = 'https://temperaturehumidity-6aa.firebaseio.com/'
temperature_location = 'Taipei';
t = time.time();
date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')

# ******************************************************************************************
# Get Temperature, Humidity                                                                #                                                                         #
# ******************************************************************************************

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient
value = bridgeclient()
temperature = value.get("t")
humidity = value.get("h")

print date + ',' + temperature_location + ',' + str(temperature) + ',' + str(humidity)
  
# ******************************************************************************************
# Insert Data                                                                              #
# ******************************************************************************************    

data = {'date':date,'temperature':temperature,'humidity':humidity}
result = requests.post(firebase_url + '/' + temperature_location + '/temperaturehumidity.json', data=json.dumps(data))
print 'Status Code = ' + str(result.status_code) + ', Response = ' + result.text