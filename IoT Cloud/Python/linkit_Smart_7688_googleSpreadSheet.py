# *******************************************************************************************************
# Version:     2017.06.14 
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + Google Spreadsheet
# *******************************************************************************************************
# 
# 1. update opkg & disable bridge
# 	 opkg update
# 	 uci set yunbridge.config.disabled=0
# 	 uci commit
#    reboot
#
# 2. install gspread
#    pip install gspread oauth2client
# *******************************************************************************************************

import time
import sys 
import gspread
from oauth2client.service_account import ServiceAccountCredentials

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient
value = bridgeclient()

# Uue Credential
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('ooo.json', scope)
client = gspread.authorize(creds)
 
# Set Sheet
#sheet = client.open("7688data").sheet1
sheet = client.open("7688data").worksheet("sensingData")

# Get Value
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)

# print(sheet.acell('B2').value)
# print(sheet.cell(1, 2).value)

# print(sheet.range('A1:B4'))

# Display Row Count
# print(sheet.row_count)

while True:
    h0 = value.get("h")
    t0 = value.get("t")
    print "Humi: " + h0
    print "Temp: " + t0

    # Write Value
    rowValue = [t0, h0]
    print(sheet.row_count)
    index = sheet.row_count + 1
    sheet.insert_row(rowValue, index)
    time.sleep(5)
