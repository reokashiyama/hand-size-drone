from machine import Pin
import time

gp18 = Pin(18, Pin.OUT)

while True:
    gp18.value(1)
    time.sleep(1)
    gp18.value(0)
    time.sleep(1)