import time
from machine import Pin
from neopixel import NeoPixel

#define the LED pin number and numbe rof leds
GRBled = NeoPixel(Pin(2), 1)


GRBled.fill((0,0,255))

GRBled.write()