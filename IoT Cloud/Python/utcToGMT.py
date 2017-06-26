# pip install pytz

from datetime import datetime
import pytz

tpe = pytz.timezone('Asia/Taipei')
utcnow = datetime.utcnow()
print utcnow

tpeTime = tpe.fromutc(utcnow)
print tpeTime

print "Now: ", tpeTime
print "Today's date: ", tpeTime.strftime('%Y-%m-%d') 

print "year:", tpeTime.year
print "month:", tpeTime.month
print "day:", tpeTime.day
print "hour:", tpeTime.hour
print "minute:", tpeTime.minute
print "second:", tpeTime.second