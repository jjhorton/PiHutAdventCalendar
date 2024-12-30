from machine import Pin, ADC
from neopixel import NeoPixel
import time
import random

GPIOnumber = 2
LEDcount = 15    

ring = NeoPixel(Pin(GPIOnumber), LEDcount)

potentiometer = ADC(Pin(28))

ring.fill((0,0,0))
ring.write()
time.sleep(1)

LEDdivision = (65535/LEDcount)

while True:
    reading = round( (potentiometer.read_u16())/LEDdivision)
    
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    for ledon in range (reading):
        ring[ledon] = (r,g,b)
        
    for ledoff in range((reading), LEDcount, 1):
        ring[ledoff] = (0,0,0)
    
    ring.write()
    time.sleep(0.1)