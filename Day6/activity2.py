#Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2), 1)

# Define some GRB colour variables
white = 240,140,255
red = 0,255,0
green = 255,0,0
blue = 0,0,255
yellow = 255,175,150
orange = 238,223,105
pink = 150,150,200
purple = 40,100,255
iceblue = 150,25,200
unicorn = 175,150,255
bogey = 215,100,0

# Fille the LED with a colour variable
GRBled.fill((green))

GRBled.write()

#Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2), 1)

# Define some GRB colour variables
white = 240,140,255
red = 0,255,0
green = 255,0,0
blue = 0,0,255
yellow = 255,175,150
orange = 238,223,105
pink = 150,150,200
purple = 40,100,255
iceblue = 150,25,200
unicorn = 175,150,255
bogey = 215,100,0

# Define our colour list
colours = [white, red, green, blue, yellow, orange, pink, purple, iceblue, unicorn, bogey ]

# Fille the LED with a colour variable
while True:
    for colour in colours:
        GRBled.fill((colour))
        GRBled.write()
        time.sleep(0.1)