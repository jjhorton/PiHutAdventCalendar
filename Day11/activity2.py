from machine import Pin
import time

from neopixel import NeoPixel

key1 = Pin(11,Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10,Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13,Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12,Pin.IN, Pin.PULL_DOWN)

# LED detail
GPIOnumber = 2
LEDcount = 15

# Define the strand pin number and number of LEDs
strand = NeoPixel(Pin(GPIOnumber), LEDcount)

off = 0,0,0
green = 0,255,0
blue = 0,0,255
white = 255,255,255
yellow = 255,255,0
pink = 255,0,255
aqua = 0,255,255

ledindex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

strand.fill((0,0,0))
strand.write()
time.sleep(1)

def blinky1(colour1, colour2):
    for led in ledindex:
        if (led%2)==0:
            strand[led] = (colour1)
        else:
            strand[led] = (colour2)
        strand.write()
        
while True:
    time.sleep(0.1)
    
    if key1.value() == 1:
        blinky1(aqua,green)
    elif key2.value() == 1:
        blinky1(white,blue)
    elif key3.value() == 1:
        blinky1(yellow,pink)
    elif key4.value() == 1:
        blinky1(off,off)