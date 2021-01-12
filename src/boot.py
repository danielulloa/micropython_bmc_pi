from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'ssid'
password = 'password'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

# ESP32 GPIO 26
r1 = Pin(2, Pin.OUT)
r2 = Pin(12, Pin.OUT)
r3 = Pin(13, Pin.OUT)
r4 = Pin(14, Pin.OUT)
