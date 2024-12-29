from machine import Pin, ADC
from neopixel import NeoPixel
import time

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
    
    for ledon in range (reading):
        ring[ledon] = (0,0,255)
        
    for ledoff in range((reading), LEDcount, 1):
        ring[ledoff] = (0,0,0)
    
    ring.write()
    time.sleep(0.1)