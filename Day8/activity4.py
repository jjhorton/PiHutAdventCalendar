from machine import Pin
from neopixel import NeoPixel
import time

ring = NeoPixel(Pin(2), 12)

myleds = [0,1,2,3,4,5,6,7,8,9,10,11]

ring.fill((0,0,0))
ring.write()
time.sleep(1)

while True:
    for i in myleds:
        ring[i] = (0,0,10)
        ring.write()
        
        time.sleep(0.3)
        
        ring.fill((0,0,0))
        ring.write()