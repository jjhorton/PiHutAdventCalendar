from machine import Pin
from neopixel import NeoPixel
import time

GPIOnumber = 2
LEDcount = 15

strand = NeoPixel(Pin(GPIOnumber), LEDcount)

#led index list
ledindex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

strand.fill((10,0,0))
strand.write()
time.sleep(1)

while True:
    
    for led in ledindex:
        for i in range(255,10,-1):
            strand[led] = (i,i,i)
            strand.write()
            time.sleep(0.001)
        
        strand[led] = (10,0,0)
        strand.write() 