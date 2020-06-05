

#this script that advertises a bluetooth low energy beacon  for 15 seconds


import time #<-----classs library for a first party module

from bluetooth.ble import BeaconService #<-------class library for a third party module

#create an instance of an object form the 3rd party class

service = BeaconService() #<--creatong beacon service


service.start_advertising("11111111-2222-3333-4444-555555555555", 1, 1, 1, 200) #<--advertising a signal

time.sleep(15)

service.stop_advertising()

print("Done.")

