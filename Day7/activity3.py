import time
from machine import Pin, ADC
from neopixel import NeoPixel

#set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# define the LED pin number (2)
GRBled = NeoPixel(Pin(2), 1)

# Define our colors
red = 0,255,0
amber = 255,175,150
green = 255,0,0

reading=0

GRBvalue = 0

while True:
    reading = potentiometer.read_u16()
    
    GRBvalue = round(reading* (255/65535))
    
    print("Analogue: ",reading)
    print("GRB:      ",GRBvalue)
    
    GRBled.fill((0,0,GRBvalue))
    GRBled.write()
    time.sleep(0.1)
            