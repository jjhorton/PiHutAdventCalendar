# Imports
from machine import Pin
from neopixel import NeoPixel
import time

# LED details
GPIOnumber = 2
LEDcount = 15

# Define the strand pin number and number of LEDs from variables
strand = NeoPixel(Pin(GPIOnumber), LEDcount)

# Colour variables
red = 255,0,0
green = 0,255,0

# LED index list
ledindex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Turn off all LEDs before program start
strand.fill((0,0,0))
strand.write()
time.sleep(1)

while True:
    
    for led in ledindex:
        if (led % 2) == 0:
            strand[led] = (red)
        else:
            strand[led] = (green)
        strand.write()
    
    time.sleep(0.5)
    
    for led in ledindex:
        if (led % 2) == 0:
            strand[led] = (green)
        else:
            strand[led] = (red)
        strand.write()
    
    time.sleep(0.5)    