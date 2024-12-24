import time
from machine import Pin, ADC
from neopixel import NeoPixel
import random

potentiometer = ADC(Pin(28))

GRBled = NeoPixel(Pin(2),1)

flash = 0

while True:
    flash = potentiometer.read_u16()/65000
    
    g = random.randint(0,255)
    r = random.randint(0,255)
    b = random.randint(0,255)
    
    GRBled.fill((g,r,b))
    GRBled.write()
    
    time.sleep(flash)