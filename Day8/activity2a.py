from machine import Pin
from neopixel import NeoPixel
import time

ring = NeoPixel(Pin(2), 12)

# Turn off
ring.fill((0,0,0))
ring.write()
time.sleep(1)

# Create a list of the LEDs to use
myleds = [0,3,6,9]

# send data to four LEDs
for i in myleds:
    ring[i] = (10,0,0)
    ring.write()
