# Imports
from machine import Pin
import time

# Set up out button name and GPIIO pin Number
redbutton = Pin(2,Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True:
    time.sleep(0.2) #short delay
    
    if redbutton.value() == 1:
        print("Red Button Pressed")
        
    if greenbutton.value() == 1:
        print("Green Button Pressed")