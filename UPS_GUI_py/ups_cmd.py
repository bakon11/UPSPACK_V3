#!/usr/bin/python3

from upspackv2 import *

test = UPS2("/dev/ttyAMA0")
version,vin,batcap,vout = test.decode_uart()
print("--------------------------------")
print("       UPS Version:"+version)
print("--------------------------------")

version,vin,batcap,vout = test.decode_uart()
    
if vin == "NG":
  print("USB input adapter : NOT connected!")
else:
  print("USB input adapter : connected!")
  print("Battery Capacity: "+batcap+"%")
  print("UPS Output Voltage: "+vout+" mV")
  print("\n")
        
