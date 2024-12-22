import time

from machine import Pin
from neopixel import NeoPixel

# Define the stirp and pin number
GRBled1 = NeoPixel(Pin(2),1)
GRBled2 = NeoPixel(Pin(5),1)

while True:
    for i in range(255):
        GRBled1.fill((i,0,0))
        GRBled1.write()
        time.sleep(0.005)
    
    GRBled1.fill((0,0,0))
    GRBled1.write()
    
    for i in reversed(range(255)):
        GRBled2.fill((0,i,0))
        GRBled2.write()
        time.sleep(0.005)
        