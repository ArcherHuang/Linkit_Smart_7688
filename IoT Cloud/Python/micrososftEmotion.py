# -*- coding: UTF-8 -*-

# ******************************************************************************************
# Import Package                                                                           #
# ******************************************************************************************

import httplib, json, urllib, base64

# ******************************************************************************************
# Get Service API Key                                         #
# ******************************************************************************************

apiKey = ""

# ******************************************************************************************
# Set Request Header                                                                       #
# ******************************************************************************************

contentType = "application/octet-stream"

headers = {
	'Content-Type': contentType,
	'Ocp-Apim-Subscription-Key': apiKey,
}

host = 'api.projectoxford.ai'
requestURL = '/emotion/v1.0/recognize'
localFilePath = './test.jpg'

# ******************************************************************************************
# POST Microsoft Emotion API                                                               #
# ******************************************************************************************

try:
	conn = httplib.HTTPSConnection(host)
	conn.request("POST", requestURL, open(localFilePath, 'rb'), headers)
	response = conn.getresponse()
	print(response.status, response.reason)
	data = response.read()
	conn.close()
	print(data)
except Exception as e:
	print("[Errno {0}] {1}".format(e.errno, e.strerror))
	print(e.message)