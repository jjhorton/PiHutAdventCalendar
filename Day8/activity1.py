from machine import Pin
from neopixel import NeoPixel

ring = NeoPixel(Pin(2), 12)

ring[0] = (0,0,0)

ring.write()