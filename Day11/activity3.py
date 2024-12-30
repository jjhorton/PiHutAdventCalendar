from machine import Pin
import time

key1 = Pin(11,Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10,Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13,Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12,Pin.IN, Pin.PULL_DOWN)

blockLED = Pin(25, Pin.OUT)

flash = 0

def program1():
    blockLED.value(1)
    time.sleep(flash)
    blockLED.value(0)
    time.sleep(flash)
    
while True:
    while key1.value() == 1:
        flash = 1
        program1()
    while key2.value() == 1:
        flash = 0.5
        program1()
    while key3.value() == 1:
        flash = 0.1
        program1()
    while key4.value() == 1:
        flash = 0.05
        program1()