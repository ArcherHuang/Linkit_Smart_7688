import os

os.system('mjpg_streamer -i "input_uvc.so -r 640x480 -f 15 -d /dev/video0" -o "output_http.so"')