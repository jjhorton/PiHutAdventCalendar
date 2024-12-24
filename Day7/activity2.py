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

while True:
    reading = potentiometer.read_u16()
    print(reading)
    time.sleep(0.1)
    
    if reading <= 20000:
        GRBled.fill((red))
        GRBled.write()
    elif 20000 < reading < 40000:
        GRBled.fill((amber))
        GRBled.write()
    elif reading >= 40000:
        GRBled.fill((green))
        GRBled.write()
