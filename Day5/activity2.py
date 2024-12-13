from machine import Pin
import time

# Set up switch input pins
dip1 = Pin(6, Pin.IN, Pin.PULL_DOWN)
dip2 = Pin(5, Pin.IN, Pin.PULL_DOWN)
dip3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
dip4 = Pin(3, Pin.IN, Pin.PULL_DOWN)
dip5 = Pin(2, Pin.IN, Pin.PULL_DOWN)

while True:
    if dip1.value() == 1:
        print("Switch 1:ON")
    else:
        print("Switch 1:OFF")
    if dip2.value() == 1:
        print("Switch 2:ON")
    else:
        print("Switch 1:OFF")
    if dip3.value() == 1:
        print("Switch 3:ON")
    else:
        print("Switch 1:OFF")
    if dip4.value() == 1:
        print("Switch 4:ON")
    else:
        print("Switch 1:OFF")
    if dip5.value() == 1:
        print("Switch 5:ON")
    else:
        print("Switch 1:OFF")
        
    print("----------")
    time.sleep(5)
    