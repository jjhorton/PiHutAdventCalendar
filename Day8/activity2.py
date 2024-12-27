from machine import Pin
from neopixel import NeoPixel
import time

ring = NeoPixel(Pin(2), 12)

# Turn off
ring.fill((0,0,0))
ring.write()
time.sleep(1)

# send data to four LEDs
ring[0] = (0,0,10)
ring[3] = (0,0,10)
ring[6] = (0,0,10)
ring[9] = (0,0,10)

ring.write()
