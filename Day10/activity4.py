#imports
from machine import Pin
from neopixel import NeoPixel
import time

# LED details
GPIOnumber = 2
LEDcount = 15

strand = NeoPixel(Pin(GPIOnumber), LEDcount)

red = 255,0,0
green = 0,255,0

ledindex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

strand.fill((0,0,0))
strand.write()
time.sleep(1)

for led in ledindex:
    
    if (led % 2) ==0 in ledindex:
        strand[led] = (red)
    else:
        strand[led] = (green)
        
    strand.write()
