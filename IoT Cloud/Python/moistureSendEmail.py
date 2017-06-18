import sys  
import time
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

def sendGmailSmtp(strGmailUser,strGmailPassword,strRecipient,strSubject,strContent):
    strMessage = MIMEMultipart()
    strMessage['From'] = strGmailUser
    strMessage['To'] = strRecipient
    strMessage['Subject'] = strSubject
    strMessage.attach(MIMEText(strContent))
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(strGmailUser, strGmailPassword)
    mailServer.sendmail(strGmailUser, strRecipient, strMessage.as_string())
    mailServer.close()
    return 'send successed'

while True:
    m0 = value.get("m")
    print "Moisture: " + m0

    if int(m0) < 400:
        print sendGmailSmtp('From','From_Password','To','Subject',"Send EMail Moisture: " + m0)
        print "Send EMail Moisture: " + m0
    time.sleep(1);