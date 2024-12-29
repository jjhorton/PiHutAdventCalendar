from machine import Pin
from neopixel import NeoPixel
import time

# LED details
GPIOnumber = 2
LEDcount = 15

myColour = 255,0,0
strand = NeoPixel(Pin(GPIOnumber), LEDcount)

#turn off all the LEDs before program starts
strand.fill((0,0,0))
strand.write()
time.sleep(1)

while True:
    
    for i in range(LEDcount):
        strand[i] = (myColour)
        strand.write()
        time.sleep(0.09)
        
        strand.fill((0,0,0))
        strand.write()
        
    for i in reversed (range(LEDcount)):
        
        strand[i] = (myColour)
        strand.write()
        
        time.sleep(0.09)
        
        strand.fill((0,0,0))
        strand.write()
        
    