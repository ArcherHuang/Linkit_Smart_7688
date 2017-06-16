# *********************************************************************
# Version:     2017.06.16
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Upload Image To Dropbox
# *********************************************************************
# 
# 1. update opkg
#    opkg update  
#    opkg install fswebcam
#
# 2. Take a picture
#    fswebcam -i 0 -d v4l2:/dev/video0 --no-banner -p YUYV --jpeg 95 --save ./test.jpg
#
# 3. Install Dropbox SDK
#    pip install dropbox
#    https://www.dropbox.com/developers-v1/core/start/python
#
# *********************************************************************

# Include SDK
import dropbox
import os

# Take a picture
command = 'fswebcam -i 0 -d v4l2:/dev/video0 --no-banner -p YUYV --jpeg 95 --save ./image.jpg'
os.system(command)

# Set Access Token
access_token = 'input_access_token'
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

# Upload Image to Dropbox
f = open('./image.jpg', 'rb')
response = client.put_file('/App/Picture/image.jpg', f)
print "uploaded:", response
f.close()
