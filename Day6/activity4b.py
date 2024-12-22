import time

from machine import Pin
from neopixel import NeoPixel

# Define the stirp and pin number
GRBled = NeoPixel(Pin(2),1)

while True:
    for i in range(255):
        GRBled.fill((i,0,0))
        GRBled.write()
        time.sleep(0.005)
    for i in reversed(range(255)):
        GRBled.fill((0,i,0))
        GRBled.write()
        time.sleep(0.005)
        