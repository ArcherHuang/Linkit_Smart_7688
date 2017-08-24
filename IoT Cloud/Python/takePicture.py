# opkg update  
# opkg install fswebcam

import os

os.system('fswebcam -i 0 -d v4l2:/dev/video0 --no-banner -p YUYV --jpeg 95 --save ./test.jpg')